"""Check the contracts of [ORG]AIOC-PPD.

1. Every contracts/*.schema.json is a sound JSON Schema 2020-12.
2. For each schema <name>, every contracts/examples/<name>/valid-*.json validates against it, and
   every must-fail-*.json is refused, with at least one error at the JSON pointer and keyword its
   entry in that folder's MUST-FAIL-REASONS.json names; a must-fail file with no entry, or an entry
   with no file, fails. A release notice's notice_id is its content address: 'PPDN-' + SHA-256 of
   the canonical notice without notice_id (keys sorted, separators ',' and ':', UTF-8, non-ASCII
   kept); a must-fail example is otherwise valid, so its notice_id is its content address too.
3. The design return contract (blueprint Annex B): --design-return gives the Library's
   library/contracts/design-return.schema.json, whose SHA-256 must equal contracts/PINS.json
   design_return_contract.sha256; every contracts/examples/design-return/*.json validates against
   it; an `accepted` return that has ended is `answered by release`, by the release it names.
   Without --design-return, check 3 prints SKIPPED and the script exits 2, never 0.

Usage: python3 tools/check_contracts.py --design-return <49GAION-protocol at the pinned commit>/library/contracts/design-return.schema.json
Exit 0 when every check passes; 1 on any failure; 2 when check 3 was skipped and nothing failed.
"""
import argparse, hashlib, json, pathlib, sys
import jsonschema

ROOT = pathlib.Path(__file__).resolve().parent.parent
C = ROOT / "contracts"
EX = C / "examples"
ID_FIELDS = {"release-notice": ("notice_id", "PPDN-")}


def content_address(obj, id_field, prefix):
    body = {k: v for k, v in obj.items() if k != id_field}
    canon = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return prefix + hashlib.sha256(canon.encode("utf-8")).hexdigest()


def pointer(path):
    return "".join("/" + str(p).replace("~", "~0").replace("/", "~1") for p in path)


def check_own(fmt):
    """Checks 1 and 2."""
    failures, counts = 0, {"valid": 0, "must-fail": 0}
    for sf in sorted(C.glob("*.schema.json")):
        name = sf.name[: -len(".schema.json")]
        schema = json.loads(sf.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
        v = jsonschema.Draft202012Validator(schema, format_checker=fmt)
        folder = EX / name
        reasons_file = folder / "MUST-FAIL-REASONS.json"
        reasons = json.loads(reasons_file.read_text(encoding="utf-8")) if reasons_file.exists() else {}
        seen = set()
        files = sorted(folder.glob("valid-*.json")) + sorted(folder.glob("must-fail-*.json"))
        if not files:
            print(f"FAIL {name}: no example in contracts/examples/{name}/"); failures += 1
        for f in files:
            doc = json.loads(f.read_text(encoding="utf-8"))
            errs = list(v.iter_errors(doc))
            address_ok = True
            if name in ID_FIELDS:
                idf, prefix = ID_FIELDS[name]
                address_ok = doc.get(idf) == content_address(doc, idf, prefix)
            if f.name.startswith("valid-"):
                counts["valid"] += 1
                ok = not errs and address_ok
                why = errs[0].message if errs else "the ID is not the content address of the body"
            else:
                counts["must-fail"] += 1
                seen.add(f.name)
                entry = reasons.get(f.name)
                found = {(pointer(e.absolute_path), e.validator) for e in errs}
                if not errs:
                    ok, why = False, "NOT REJECTED"
                elif entry is None:
                    ok, why = False, "no entry in MUST-FAIL-REASONS.json"
                elif (entry["path"], entry["keyword"]) not in found:
                    ok, why = False, f"rejected, but not at {entry['path']!r} by '{entry['keyword']}': {sorted(found)}"
                elif not address_ok:
                    ok, why = False, "the ID is not the content address: not otherwise valid"
                else:
                    ok, why = True, ""
            print(("pass" if ok else "FAIL") + f" {name}/{f.name}" + ("" if ok else f": {why}"))
            failures += 0 if ok else 1
        for n in sorted(set(reasons) - seen):
            print(f"FAIL {name}/MUST-FAIL-REASONS.json: entry {n} names no must-fail file"); failures += 1
    return failures, counts


def check_design_return(path, fmt):
    """Check 3. Returns (failures, skipped, examples)."""
    pin = json.loads((C / "PINS.json").read_text(encoding="utf-8")).get("design_return_contract")
    if not pin or not all(pin.get(k) for k in ("repository", "path", "commit", "sha256")):
        print("FAIL check 3: contracts/PINS.json has no complete design_return_contract pin"); return 1, False, 0
    files = sorted((EX / "design-return").glob("*.json"))
    if not path:
        print("SKIPPED check 3 (design return contract): no --design-return given"); return 0, True, len(files)
    raw = pathlib.Path(path).read_bytes()
    got = hashlib.sha256(raw).hexdigest()
    if got != pin["sha256"]:
        print(f"FAIL check 3: the design return contract has SHA-256 {got}, not the pinned {pin['sha256']}"); return 1, False, len(files)
    schema = json.loads(raw.decode("utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    v = jsonschema.Draft202012Validator(schema, format_checker=fmt)
    failures = 0 if files else 1
    if not files:
        print("FAIL check 3: no example in contracts/examples/design-return/")
    for f in files:
        doc = json.loads(f.read_text(encoding="utf-8"))
        errs = list(v.iter_errors(doc))
        ok, why = not errs, (errs[0].message if errs else "")
        if ok and doc.get("kind") == "accepted" and doc.get("status") != "open":
            if doc.get("status") != "answered by release" or doc.get("answered_by") != doc["release"]["release_id"]:
                ok, why = False, "an accepted return ends as answered by release, by the release it names"
        print(("pass" if ok else "FAIL") + f" design-return/{f.name}" + ("" if ok else f": {why}"))
        failures += 0 if ok else 1
    return failures, False, len(files)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check the contracts of [ORG]AIOC-PPD.")
    ap.add_argument("--design-return", help="the Library's design return contract at the commit pinned in contracts/PINS.json (check 3)")
    a = ap.parse_args(argv)
    fmt = jsonschema.Draft202012Validator.FORMAT_CHECKER
    f12, counts = check_own(fmt)
    f3, skipped, returns = check_design_return(a.design_return, fmt)
    failures = f12 + f3
    print(f"{counts['valid']} valid, {counts['must-fail']} must-fail, design-return examples {returns}; "
          f"check 3 {'SKIPPED' if skipped else 'run'}; {failures} failures")
    if failures:
        return 1
    return 2 if skipped else 0


if __name__ == "__main__":
    sys.exit(main())
