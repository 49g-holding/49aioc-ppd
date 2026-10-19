```yaml
# ── Blueprint metadata (machine-readable; the panel generator and the back-office builder read this block) ──
blueprint:
  aioc: "[ORG]AIOC-PPD"
  parent: "[ORG]AIOC-CH"                  # example code of the Charter; each organisation writes its own Charter's code (Standard §1.7, item 13)
  full_name: "Process and Position Design"
  organisation: "<organisation>"          # filled in each organisation's own copy
  type: "specialised"
  org_aion: "[ORG]AION"
  blueprint_version: "v0.5.1"
  status: "draft"
  template:
    name: "49GAION AIOC Blueprint Template"
    version: "v1.5.0, with the unreleased v1.6.0 additions on main"
    source: "github.com/49g-holding/49GAION-aioc, template/AIOC-BLUEPRINT-TEMPLATE.md @ e89ed1d"
  mother:
    name: "49GAION Process and Position Design"
    version: "part card v2 (DRAFT)"
    source: "github.com/49g-holding/49GAION-protocol, library/cards/process-and-position-design.part-card.json and Protocol §17, items 1 to 11 (pull requests #33 and #36); Standard §3.1, items 3 and 6 (49GAION pull requests #66 and #68; DR-0014, DR-0018). This text is its mother blueprint"
  writing_repository: "<org>aioc-ppd"
  code_project: "<org>aioc-ppd, on the organisation's code platform"
  panel_register_id: "none yet"
  capabilities:
    standard: ["Chief of Staff", "Office", "Input socket", "Panel"]
    functional: ["Release Intake and Returns", "Needs Requests", "Process Architecture", "Process Writing", "Position Shaping", "Structure", "Workload", "Operational Walkthrough", "Independent Review", "Decision Package and Release", "Returns from Delivery and Implementation"]
```

# Blueprint · `[ORG]AIOC-PPD` · Process and Position Design · `v0.5.1`

**Draft, 15 October 2026; v0.4.0, 16 October 2026, connects the chain on both sides (`decisions/DR-0004`): every return to the Target Operating Model now follows the Library's design return contract and always ends; each decided release is announced to Delivery and Implementation directly, and its returns come back here and end in the same way. v0.5.0, 16 October 2026, reads what the TOM release now also states (`decisions/DR-0005`; TOM blueprint `v0.6.0`, Annex H): the objectives cascade starts from its strategy frame; the critical value streams are designed first; work delivered outside becomes a hand-off, never an in-house process; today's activity profile is read for workload; priority orders the work. v0.5.1, 19 October 2026: the Chief of Staff takes its COS code `[ORG]CELL-COSPPD` (`decisions/DR-0006`).** Written by `[ORG]AIOC-OCO` on the directions recorded in `decisions/DR-0001` to `decisions/DR-0005`. This is the first blueprint of Process and Position Design, written for any organisation as the mother text of the Library part 49GAION Process and Position Design (Protocol §17). Every rule rests on a 49GAION text, on the blueprint of `[ORG]AIOC-TOM` (cited by section and version), or is new here and marked **New**. Nothing here has run. Every fixed test reads `NOT_RUN`.

> **Process and Position Design in one page**
>
> Process and Position Design (PPD) takes an organisation's decided target operating model and designs how its work runs and the positions that carry it. It is the stage after the Target Operating Model (TOM), and a part of its own.
>
> **What goes in**
> 1. The decided TOM release, handed over directly by `[ORG]AIOC-TOM`, by reference and hash. PPD reads its role register first, then its value streams (which are critical), capabilities (how each is delivered), decision domains and hand-offs, and its strategy on one page, outside parties' journeys, priorities and how the work runs today.
> 2. The organisation's other sources, only from Source Lifecycle: the processes, procedures, policies, volumes and times it already has.
> 3. Answers to what the release and the sources do not say. PPD never asks a person. It asks the Chief of Staff of Source Lifecycle, who gets the answer approved and recorded.
>
> **The link with TOM goes both ways.** PPD never changes the TOM release. When it finds a defect, it sends a return straight back to TOM, naming the part and the reason: cannot use, missing what; contradiction found; assumption invalid; request kind unsupported. The elements the return touches wait; the rest of the work goes on. TOM answers with a new decided release, or the organisation answers by decision, and the two go back and forth in rounds, each with a deadline. No return is left open: it ends answered, or set aside by decision and carried forward as a known defect or a decided assumption, so that PPD delivers.
>
> **The link with Delivery and Implementation works the same way.** PPD tells Delivery and Implementation (DI) of each decided release at once. DI sends back what it cannot use, and PPD carries each return to an end in the same way.
>
> **What PPD does, in ten stages, processes first**
> 1. Admit: check the request, the release and the connections.
> 2. Read the release: account for every role, phase, capability, decision domain and hand-off, or return it.
> 3. Architecture: the processes under each part of the model, in three levels, each with one owner.
> 4. Critical processes: choose the processes that cross parts or lie on a critical value stream, and design them first, in the order of their priority.
> 5. Write each process: purpose, trigger, steps in role lanes, what goes in and out of each step, the decision at each step and who decides it, exceptions and escalation, measures, volumes and step times. Each step also says when it is done, its worst error and whether it can be undone, what kind of act it is, where its input comes from and how far it is trusted, how confidential it is, and its risk, control and record.
> 6. Shape the positions: group the steps and decisions of each role into positions, and generate each job description from what the position holds. No job description is written by hand.
> 7. Structure: group the positions into units (teams, sections, departments), each with its head position and a generated charter; reporting lines, spans and layers, standing forums with charters, and the crosswalk from the organisation as it is today.
> 8. Workload: the work each position carries, from the volumes and step times of its processes, beside how the work runs today where the release records it.
> 9. Walk: test the design against realistic situations.
> 10. Decide and release: the organisation decides each element; the release is frozen, filed in Source Lifecycle, and Delivery and Implementation is told at once.
>
> Each stage has one input, one output and one test that says when it is done. Critical processes are written twice, separately, by two authors of two engine families. Every stage is checked by three or more other engines before the next starts. A person, the PPD Design Lead, rules on what they still dispute.
>
> **What comes out: the PPD Release**
> - the process architecture and the process book;
> - the decision-rights register and the authority matrix;
> - the policy register;
> - the controls catalogue and the segregation-of-duties check;
> - the position register, with a job description and a competence profile for every position;
> - the objectives cascade, from the goals and critical numbers of the decided strategy frame down to each position's measures;
> - the unit register, with a generated charter for each unit;
> - organisation charts, standing forums with their charters and tiers, and the review calendar;
> - structure scenarios side by side, when the organisation asks for them;
> - the workload of each position, its peak-load check, and the end-to-end time of each process and value stream;
> - the crosswalk from today's organisation;
> - the walkthrough report and the quality checks;
> - the Decision Package.
>
> **Who decides.** The organisation's Requesting Authority decides each element: accept, correct or reject. Silence decides nothing. PPD designs positions only (Standard §1.1, item 9). It makes no choice of what fills a position; that belongs to a later stage.

**Where this blueprint stands.** Fifth draft (`v0.5.0` supersedes `v0.4.0`; `v0.5.1` gives the Chief of Staff its COS code; §14). The stages, their inputs, outputs and done-tests are set (§5.0). The engine rules it shares with `[ORG]AIOC-TOM` (the Review Panel rule, two authors, labels, decision rules, and the receiving end of returns) are carried from the TOM blueprint `v0.6.0` by section, not copied (§5.9; Annex E). The decisions only a human seat can take are listed once, in §13.

---

## 0. Identity and lineage

| Field | Value |
|---|---|
| Code | `[ORG]AIOC-PPD`. Collision check (Naming Standard §5 and R6): the initials do not recreate `AIOC`, `AION` or `49GAION`, and do not read as a version suffix. The code is the one Protocol §17 gives the Library part in an `[ORG]AION`. Each organisation records it in its register before the repository is created (Naming Standard R9) |
| Full name | Process and Position Design |
| Description | "`[ORG]AIOC-PPD` is `<organisation>`'s Process and Position Design core, built from 49GAION Process and Position Design" |
| Kind | AIOC |
| Parent | `<code of the Charter of this [ORG]AION>`; the cards use the example code `[ORG]AIOC-CH`. A top-level AIOC (Standard §1.7, item 13). A change of parent is the listed type `change-parent` |
| Inner units | `[ORG]CELL-PDL`, `[ORG]CELL-COSPPD`, `[ORG]POD-PRI`, `[ORG]POD-PA`, `[ORG]POD-PPW`, `[ORG]POD-PPS`, `[ORG]POD-PS`, `[ORG]POD-PW`, `[ORG]POD-PR`: seven Pods with their fifteen Cells, and two Cells directly under the AIOC (§17). No inner AIOC |
| HOAC label | `[ORG]HOAC-ACS`, held by its top Cell, the PPD Design Lead `[ORG]CELL-PDL` (`label_holder`) |
| Accountable to | `<code of the Cell carrying [ORG]HOAC-TM>`; the cards use the example code `[ORG]CELL-TMS` (Naming Standard R15). That Cell signs this AIOC's install, its `change-parent` and its `restart-stopped-unit` (Standard §5.3, item 4; §4.4, item 3) |
| Type | Specialised: the organisation needs its processes and positions designed from its decided operating model (§16) |
| `[ORG]AION` | `[ORG]AION`, based on 49GAION Standard `v1.5.0`, with the unreleased `v1.6.0` texts on main |
| Versioned Definition | this file; the Panel and the Back office are built from it |
| Organisation | `<organisation>` |
| Made from | the Library part 49GAION Process and Position Design, part card `v2` (DRAFT), and Protocol §17, items 1 to 11, merged on 15 October 2026 (`decisions/DR-0001`; `49GAION/DR-0014`, `DR-0018`) |
| Template | 49GAION AIOC Blueprint Template `v1.5.0` at `e89ed1d` (with the `v1.6.0` additions: mechanism register and Reserve, checks that are not fixed tests, the added Configuration rows, position codes only) |
| Mother | 49GAION Process and Position Design, part card `v2`. This text is its mother blueprint |
| Blueprint version and status | `v0.5.1` · draft |
| Accountable seat (`[ORG]HOAC-ACS`) | the PPD Design Lead, `[ORG]CELL-PDL`, a HOAC position. Who occupies it is top management's own mechanism; this AIOC never sees it (Standard §1.1, item 9) |
| Reports to | the Cell carrying `[ORG]HOAC-TM` |
| Writing repository | `<org>aioc-ppd`, plus `-records` for an organisation's runs and `-records-restricted` for run records that touch a Strictly confidential source (Naming Standard R9). The mother text lives in a public repository and holds no organisation data |
| Code project | `<org>aioc-ppd`, on the organisation's code platform |
| Panel | not yet built |
| Back office | not yet built |
| Attribution | Powered by 49GAION |

**Lineage.** The stage after the operating model was first proposed as "positions and job descriptions". A study of how leading organisation-design practices run this stage, made on 15 October 2026, found that every one of them designs processes and decision rights together with the roles below the operating model, and warns that a structure drawn without them fails. The governing seat then directed a separate AIOC, linked directly to the TOM, never merged with it or with the stage after it (`decisions/DR-0001`; `49GAION/DR-0014`). The study is summarised in `docs/HISTORY.md`. No earlier code or result is carried here.

---

## 1. Card (49GAION Operating Protocol §3)

```yaml
card:
  unit_kind: "AIOC"
  code: "[ORG]AIOC-PPD"
  parent: "[ORG]AIOC-CH"                  # example code of the Charter, the root AIOC; only it has parent none (Standard §1.7, item 13)
  inner_units: ["[ORG]CELL-PDL", "[ORG]CELL-COSPPD", "[ORG]POD-PRI", "[ORG]POD-PA", "[ORG]POD-PPW", "[ORG]POD-PPS", "[ORG]POD-PS", "[ORG]POD-PW", "[ORG]POD-PR"]
  type: "specialised"
  org_aion: "[ORG]AION"
  card_version: "v0.5.1"
  input_door: "Chief of Staff"
  wake: { method: "queue", verified: false }
  receives:
    - kind: "run request"                 # a Work Item from the Requesting Authority's Cell, through the HU input port; references only
      format: "Work Item (Protocol §4.1) whose sources field holds one TOM Release reference and, optionally, the children in scope"
      acceptance_test: "TEST-PPD v3, cases 1, 23"
      decision_needed: false
    - kind: "release notice"              # from [ORG]AIOC-TOM, directly, through the tool gateway
      format: "release notice of [ORG]AIOC-TOM (its contracts/release-notice.schema.json, urn:49gaion:library:tom:release-notice:v0.5): the TOM Release ID, version and manifest hash, its filed reference, and the returns it answers"
      acceptance_test: "TEST-PPD v3, cases 2, 3, 24, 25"
      decision_needed: false
    - kind: "return answer"               # from [ORG]AIOC-TOM: the end, or the next round, of a return this AIOC sent
      format: "the return at its next version (49GAION-protocol library/contracts/design-return.schema.json, pinned in contracts/PINS.json)"
      acceptance_test: "TEST-PPD v3, cases 98, 99, 104"
      decision_needed: false
    - kind: "return"                      # from [ORG]AIOC-DI, directly, on elements of a PPD Release (§5.11)
      format: "design return (49GAION-protocol library/contracts/design-return.schema.json, pinned in contracts/PINS.json)"
      acceptance_test: "TEST-PPD v3, cases 101-103"
      decision_needed: true
    - kind: "source reference"            # the organisation's other sources, from the output socket of [ORG]AIOC-SL
      format: "source reference (ID + version + hash; held or not held)"
      acceptance_test: "TEST-PPD v3, cases 4, 30"
      decision_needed: false
    - kind: "needs answer"                # the output of a needs request sub-item
      format: "needs answer, by reference only"
      acceptance_test: "TEST-PPD v3, cases 8, 33"
      decision_needed: false
    - kind: "needs status"                # accepted, returned or asked, from [ORG]AIOC-SL
      format: "needs status"
      acceptance_test: "TEST-PPD v3, case 31"
      decision_needed: false
  delivers:
    - kind: "return"                      # to [ORG]AIOC-TOM, directly; also filed into [ORG]AIOC-SL as a design report
      format: "design return (49GAION-protocol library/contracts/design-return.schema.json, pinned in contracts/PINS.json), prefix PPDR"
      usual_receivers: ["[ORG]AIOC-TOM", "[ORG]AIOC-SL"]
    - kind: "needs request"
      format: "needs request, as a sub-item of the run Work Item"
      usual_receivers: ["[ORG]AIOC-SL"]
    - kind: "missing report"
      format: "Missing Report, one per pass"
      usual_receivers: ["[ORG]AIOC-SL"]
    - kind: "PPD Release filing"
      format: "PPD Release manifest and its parts (Annex A), filed as a source of origin kind process and position design; filing receipt"
      usual_receivers: ["[ORG]AIOC-SL"]
    - kind: "release notice"              # to the next stage, by reference (Protocol §20, item 9)
      format: "release notice (contracts/release-notice.schema.json): the PPD Release ID, version and manifest hash, the TOM Release it rests on, its filed reference, and the returns it answers; never release text"
      usual_receivers: ["[ORG]AIOC-DI"]
    - kind: "return answer"               # the end of a return from [ORG]AIOC-DI, or its next round (§5.11)
      format: "the return at its next version (49GAION-protocol library/contracts/design-return.schema.json): its status, the answering release or decision reference, and for a return set aside, its carried_forward_on"
      usual_receivers: ["[ORG]AIOC-DI"]
  anatomy:
    panel: { health: { tests: true, metrics: ["stuck", "returned", "late", "run state", "returns open", "returns answered", "returns from DI open", "returns past deadline", "return round", "needs open", "needs past deadline", "processes by state", "positions by state", "assumptions open", "reviews held", "review budget used"] } }
    back_office: { converses_with_humans: false, hosts: ["Chief of Staff", "Office"], protocol_traffic: true }
    definition: { location: "<org>aioc-ppd, blueprint/PPD-BLUEPRINT.md", version: "v0.5.1" }
    delivery: { rollback: "one-click" }
    connectors:
      - { role: "operating model source", connector: "[ORG]AIOC-TOM release port", access_managed_in: "panel" }   # the grant is signed at the tool gateway as connect-external-port (Protocol §17, item 8)
      - { role: "source of record", connector: "[ORG]AIOC-SL output socket", access_managed_in: "panel" }      # as above (Protocol §13, item 5)
      - { role: "next design stage", connector: "[ORG]AIOC-DI input port: release notices out, returns in", access_managed_in: "panel" }   # signed by the [ORG]HOAC-ACS position over this AIOC (Protocol §20, item 9; H-16)
    gateway: { metering_id: "<per-AIOC metering id>" }
  full_name: "Process and Position Design"
  version: "0.5.1"
  lineage: { id: "[ORG]AIOC-PPD", version: "0.5.1", relation: "original" }
  lifecycle_state: "designed"
  blueprint_version: "v0.5.1"
  template_version: "v1.5.0"
  accountable_to: "[ORG]CELL-TMS"         # example code of the Cell carrying [ORG]HOAC-TM (Naming Standard R15); never a Cell inside this AIOC
  top_cell: "[ORG]CELL-PDL"
  hoac: "[ORG]HOAC-ACS"
  label_holder: "[ORG]CELL-PDL"
  fixed_test: { id: "TEST-PPD", version: "v3", owner: "[ORG]CELL-TMS" }
  skills:
    - { id: "ppd-release-intake", name: "Reading a decided operating model, and returning its defects", tags: ["design", "intake"] }
    - { id: "ppd-process-design", name: "Process architecture and process design", tags: ["design"] }
    - { id: "ppd-position-design", name: "Positions and generated job descriptions", tags: ["design"] }
    - { id: "ppd-structure", name: "Reporting lines, forums and crosswalk", tags: ["design"] }
    - { id: "ppd-walkthrough", name: "Operational walkthrough of processes and positions", tags: ["assurance"] }
    - { id: "ppd-returns", name: "Returns both ways, each carried to an end", tags: ["coordination"] }
  ports:
    - { unit: "[ORG]AIOC-PPD", port: "ai-in", direction: "input", type: "AI", identification: "technical-key", accepted_content: ["release notice", "return answer", "return", "source reference", "needs answer", "needs status"], authority_limit: "read only, within the scopes signed for the TOM and Source Lifecycle connections; returns only on the connection signed with [ORG]AIOC-DI", audit_trail: "unit register; the serve logs of [ORG]AIOC-TOM and [ORG]AIOC-SL; the Work Item record", required_tests: ["TEST-PPD v3"], enforcement: "shared-gateway-outside-unit" }
    - { unit: "[ORG]AIOC-PPD", port: "ai-out", direction: "output", type: "AI", identification: "technical-key", accepted_content: ["return", "needs request", "missing report", "needs status", "PPD Release filing", "release notice", "return answer"], authority_limit: "returns, requests, reports, filings, notices and answers only, by reference; files only its own releases and design reports; never an instruction to a person", audit_trail: "Work Item record and the unit register", required_tests: ["TEST-PPD v3"], enforcement: "shared-gateway-outside-unit" }
    - { unit: "[ORG]AIOC-PPD", port: "hu-in", direction: "input", type: "HU", identification: "live-human-sign-in-at-gateway", accepted_content: ["run request from the Requesting Authority's Cell (references only)", "run control and configuration from the PPD Design Lead (never a source)"], authority_limit: "the signer's authority_scope; nothing received here is a source", audit_trail: "Office record", required_tests: ["TEST-PPD v3"], enforcement: "shared-gateway-outside-unit" }
    - { unit: "[ORG]AIOC-PPD", port: "hu-out", direction: "output", type: "HU", identification: "live-human-sign-in-at-gateway", accepted_content: ["run brief to the PPD Design Lead", "ruling sheets to the PPD Design Lead", "release notice to the Requesting Authority's Cell"], authority_limit: "information only; never a question about the organisation", audit_trail: "Office record", required_tests: ["TEST-PPD v3"], enforcement: "shared-gateway-outside-unit" }
    - { unit: "[ORG]AIOC-PPD", port: "stop", direction: "input", type: "HU", identification: "live-human-sign-in-at-gateway", accepted_content: ["stop"], authority_limit: "stop only", audit_trail: "unit register", required_tests: ["TEST-PPD v3"], enforcement: "shared-gateway-outside-unit", stop_door: true }
  configuration:                          # every slot is set by the organisation (§15); an empty slot fails the joining test
    office_accountable_human: { value: "<set by the organisation>", set_by: "<position>", date: "<date>", version: "<vN>" }
    central_head: { value: "<the OCO of this [ORG]AION>", set_by: "<position>", date: "<date>", version: "<vN>" }
    discussion_limits: { value: "<set by the organisation>", set_by: "<position>", date: "<date>", version: "<vN>" }
    waiting_deadlines: { value: "<per status>", set_by: "<Cell carrying [ORG]HOAC-TM>", date: "<date>", version: "<vN>" }
    bounce_limit: { value: "<number>", set_by: "<position>", date: "<date>", version: "<vN>" }
    chain_depth: { value: "<number, at least 1>", set_by: "<position>", date: "<date>", version: "<vN>" }
    halt_request_priority: { value: "immediate", set_by: "<position>", date: "<date>", version: "<vN>" }
    budget_cap: { value: "<amount per period>", set_by: "<Cell carrying [ORG]HOAC-TM>", date: "<date>", version: "<vN>" }
    unattended_action: "read-record-triage"
    requesting_authority_cell: { value: "<set by the organisation>", set_by: "<Cell carrying [ORG]HOAC-GOV>", date: "<date>", version: "<vN>" }
    rows_per_pass: { value: 12, set_by: "<position>", date: "<date>", version: "<vN>" }
    non_response_passes: { value: "<set by the organisation>", set_by: "<Cell carrying [ORG]HOAC-TM>", date: "<date>", version: "<vN>" }
    review_engines: { value: 3, set_by: "<position>", date: "<date>", version: "<vN>" }
    review_families_min: { value: 2, set_by: "<position>", date: "<date>", version: "<vN>" }
    reduced_review_permitted: { value: "no", set_by: "<Cell carrying [ORG]HOAC-TM>", date: "<date>", version: "<vN>" }
    review_budget_per_run: { value: "<set by the organisation>", set_by: "<Cell carrying [ORG]HOAC-TM>", date: "<date>", version: "<vN>" }
    span_range: { value: "<set by the organisation>", set_by: "<Cell carrying [ORG]HOAC-TM>", date: "<date>", version: "<vN>" }
    layers_max: { value: "<set by the organisation>", set_by: "<Cell carrying [ORG]HOAC-TM>", date: "<date>", version: "<vN>" }
    workload_period: { value: "<set by the organisation>", set_by: "<position>", date: "<date>", version: "<vN>" }
    return_round_deadline: { value: "<set by the organisation>", set_by: "<Cell carrying [ORG]HOAC-TM>", date: "<date>", version: "<vN>" }
    return_rounds_max: { value: "<set by the organisation>", set_by: "<Cell carrying [ORG]HOAC-TM>", date: "<date>", version: "<vN>" }
```

**Joining the protocol.** This AIOC joins only after every input and output on this card passes fixed samples (the joining test, Protocol §11, item 1; Standard §3.2, item 4). It also needs `[ORG]AIOC-TOM` to send release notices and answer returns (made in the TOM blueprint `v0.5.0`), and Source Lifecycle to accept filings of origin kind `process and position design`. Its link with `[ORG]AIOC-DI` is not a condition of joining: without it, this AIOC stands alone. Until then its `lifecycle_state` stays `designed` and no Work Item is routed to it. The cards of its Pods and Cells are set in §17 and generated into `cards/`.

---

## 2. Organisation table and placement

### 2.1 Organisation table

The blueprint writes `[ORG]` for the organisation's prefix (Naming Standard R13). Positions only; who occupies each one is top management's own mechanism (Standard §1.1, item 9; §5.2, Position Principle).

| Term in the blueprint | In `<organisation>` |
|---|---|
| The Top Office (decisions are signed by human Cells carrying HOAC labels) | `<filled by the organisation>` |
| `[ORG]AIOC-OCO` | `<filled>` |
| The Charter of this `[ORG]AION` | `<code>` |
| The Cell carrying `[ORG]HOAC-TM` | `<code>` |
| The engineering division | `<filled>` |
| The builder of every tool | `<filled>` |
| The Library blueprint this core is made from | 49GAION Process and Position Design, part card `v2`; Protocol §17; this text is its mother blueprint |
| **The Requesting Authority**: the position that asks for the design and decides it | `<code of the human Cell carrying [ORG]HOAC-GOV>`, or of a human Cell carrying a HOAC label whose `authority_scope`, delegated by that Cell under `delegate-authority`, covers the design decisions of this AIOC (Standard §4.2, items 5 and 8; §4.4, item 8). It is a position, never this AIOC's Design Lead position |
| **The PPD Design Lead position** | a HOAC position (`[ORG]HOAC-ACS`), a legal persona. Who occupies it is top management's own mechanism; this AIOC never sees it |
| **The operating model source** | `[ORG]AIOC-TOM`: it hands over its decided release directly, and receives this AIOC's returns |
| **The source of record** | `[ORG]AIOC-SL`: every other source, every question to the organisation, and every filing |
| **The next stage** | `[ORG]AIOC-DI`: it is told of each decided PPD Release directly, and sends its returns here (§5.11) |
| **The engine register** | held at the tool gateway, in the Charter (Standard §4.4, item 11); read by this AIOC as `[ORG]AIOC-TOM` reads it (TOM blueprint `v0.5.0`, Annex E.12) |

### 2.2 Placement

- **Where it sits.** A top-level AIOC under the Charter, beside `[ORG]AIOC-SL` and `[ORG]AIOC-TOM`. It is the stage after the target operating model (Protocol §17, item 1).
- **Its role.** It turns a decided target operating model into the organisation's processes and the positions that carry them, decided by the organisation's own authority.
- **Scope.**
  - **It does:** read the decided TOM release, role register first; return every defect it finds to `[ORG]AIOC-TOM`; ask, through Source Lifecycle, for what the release and the sources lack; lay out the process architecture; choose the critical processes; write each process; shape positions from the steps and decisions they hold; generate job descriptions, the decision-rights register and the authority matrix; draw reporting lines and forums; map today's organisation to the target; compute workload; walk the design through situations; have every stage checked under the Review Panel rule; prepare the decision; release, file and hand over.
  - **It does not:** change the TOM release; ask any person anything about the organisation; name a person; read who occupies a position; choose what fills a position; set pay (H-07); write the full text of a policy; invent a measure, a volume, a time or a limit; decide anything for the organisation.
- **Shapes it serves.** Any shape the TOM release covers: one person's work, a single entity, a group of entities, or a group with independent institutions inside it. Where the release covers several entities, processes that cross entities follow the release's hand-offs register and counterparty register.
- **Boundaries with other AIOCs.**
  - **`[ORG]AIOC-TOM`** designs the operating model. This AIOC reads its decided release and returns defects; it never redesigns the model. A return is a request to TOM, never a change (§5.1; Annex B).
  - **`[ORG]AIOC-SL`** holds every source and every contact with a person. This AIOC holds only references and its own design records. It files its releases and its returns there.
  - **`[ORG]AIOC-DI`**, the next stage, is told of each decided PPD Release directly (§5.10), reads it from Source Lifecycle by reference, and returns its defects to this AIOC under the same contract; each ends by §5.11.
  - **`[ORG]AIOC-OCO`** installs, fixes and upgrades this AIOC; it never grades it (Standard §2.3, item 9).
- **Overlap.** None known. Where an organisation already holds process maps or job descriptions, they are sources, read through Source Lifecycle and mapped in the crosswalk (§5.6).

---

## 3. Positions

| Position (standard title) | Purpose | Reports to | Run today by | Deputy |
|---|---|---|---|---|
| PPD Design Lead | the accountable position of this AIOC and the owner of its path: owns the fixed tests of its parts; rules on contested review findings; accepts a reduced review level within the TM Cell's permission; attests the method. Answers for the method, never for the organisation's choices | the Cell carrying `[ORG]HOAC-TM` | a HOAC position (`[ORG]HOAC-ACS`); who occupies it is top management's own mechanism, never seen by this AIOC | as top management arranges (`appoint-acting-filler`, Standard §4.1, item 12) |
| Chief of Staff | keep each run moving, honest and traced; the only door to `[ORG]AIOC-TOM` and to Source Lifecycle | PPD Design Lead | an agent (`[ORG]CELL-COSPPD`) | none; the run halts |
| Release Reader | read the TOM release, account for every element, and draft returns | Chief of Staff | an agent (`[ORG]CELL-PRR`) | none; the step halts |
| Process Architect | lay out the process architecture and propose the critical processes | Chief of Staff | an agent (`[ORG]CELL-PPA`) | none; the step halts |
| First Process Author | write each process, as author A | Chief of Staff | an agent (`[ORG]CELL-PFPA`) | none; the step halts |
| Second Process Author | write each critical process a second time, blind to author A, on an engine of the other family | Chief of Staff | an agent (`[ORG]CELL-PSPA`) | none; the step halts |
| Process Reconciler | reconcile two locked drafts of a process into one | Chief of Staff | an agent (`[ORG]CELL-PPR`) | none; the step halts |
| Position Builder | group steps and decisions into positions | Chief of Staff | an agent (`[ORG]CELL-PPB`) | none; the step halts |
| Structure Designer | draw reporting lines, forums and the crosswalk | Chief of Staff | an agent (`[ORG]CELL-PSD`) | none; the step halts |
| Workload Analyst | compute workload from volumes and step times | Chief of Staff | an agent (`[ORG]CELL-PWA`) | none; the step halts |
| Situation Author | write walkthrough situations, blind to the design | Chief of Staff | an agent (`[ORG]CELL-PSA`) | none; the step halts |
| Situation Walker | walk the situations through processes and positions | Chief of Staff | an agent (`[ORG]CELL-PSW`) | none; the step halts |
| Blind Reviewer, seats A–E | review a locked output, alone first, then in debate | Chief of Staff | agents (`[ORG]CELL-PBRA` to `[ORG]CELL-PBRE`) | none; any seat covers another |

- **Every human position is a HOAC position.** This AIOC has one, the PPD Design Lead. The organisation may add more in this AIOC's own design (§17).
- **No natural person** (Standard §1.1, item 9). Every human position this AIOC deals with, its own and the organisation's, is a HOAC position. It addresses positions only, through their HU ports.
- The **Requesting Authority** is not a position of this AIOC (§2.1). It decides the design; this AIOC prepares the decision.
- No AI Cell signs anything (Protocol §10, item 3). Each AI Cell's bot has its own identity card (§17).
- Job descriptions, the decision-rights register, the authority matrix and the organisation charts are made by code steps of the Chief of Staff, never by a Cell (§5.5, §5.6). Code is a tool, never a seat.

---

## 4. Standard capabilities

Defaults are in `docs/STANDARD-CAPABILITIES.md` of `49GAION-aioc` at `e89ed1d` (`v1.5.0`, with the `v1.6.0` additions). The differences are listed in §11.

### 4.1 Office
#### Definition
Default · form: **single Chief of Staff**. An Office forms only if the Design Lead needs more than one Chief of Staff; it is proposed to the Design Lead, never self-created.
#### Process (SOP)
Default.
#### Role card
None while the form is a single Chief of Staff.
#### Fixed test
TEST-PPD-COSPPD v3 (TEST-PPD v3, case 73) · result `NOT_RUN`

### 4.2 Chief of Staff
#### Definition
Default, **managing** kind, with these additions:
- **The only door.** It is the only Cell of this AIOC that sends anything outside it: returns to `[ORG]AIOC-TOM`, an `accepted` return included; needs requests, Missing Reports and filings to `[ORG]AIOC-SL`; the release notice to `[ORG]AIOC-DI` and the answers to its returns. The six external ports sit on its card (§17).
- **No question to a person.** It never asks any person anything about the organisation. Every question for the organisation goes to the Chief of Staff of `[ORG]AIOC-SL` as a needs request (§5.2). Its only human contact is its own HOAC position, the PPD Design Lead, about the run.
- **An orchestrator that never judges itself.** It runs the gates of each run (Annex C), dispatches the Cells, locks outputs, runs the code steps, draws the Review Panel and writes the run record. It never rules on a finding, never dismisses or downgrades one, and never lowers a review (TOM blueprint `v0.5.0`, §5.8, carried).
#### Process (SOP)
Default, plus:
1. **Admission (S0).** On a run request: open the run record; check that the request carries references only; receive or fetch the release notice; have the Input socket build Input Pack P0 (§4.3); check gate T0 (Annex C.2) → *P0 and the T0 record* (evidence: the T0 record, with P0's ID).
2. **One run at a time.** One run per organisation. A second run in parallel needs the Design Lead's approval, recorded in the run record → *run slot* (evidence: run record).
3. **Returns.** Collect the return drafts of the Pods; have each reviewed at its review point; send each to `[ORG]AIOC-TOM` under the Library's design return contract and file it into `[ORG]AIOC-SL` as a design report, with the same hash; mark the elements it touches `held: return open`; on TOM's answer, re-open them, or carry them forward on the basis a set-aside decision states (Annex B.1) → *return sent; return ended* (evidence: the return at each version, and its filing receipt).
4. **Passes.** Batch the Pods' needs candidates into passes of at most `rows_per_pass` rows, one decision per row; send each pass with its Missing Report → *pass sent* (evidence: Work Item IDs in the needs log).
5. **Waiting.** Overdue requests and returns follow the waiting deadlines and escalation (Protocol §4.6, item 1). Past `non_response_passes`, the run stops as `non-response`, and every element resting on a missing fact goes to decision as an assumption → *ageing record* (evidence: the needs log).
6. **Answers.** Hand each needs answer and each new release notice to the Input socket, which makes a new pack version; re-open only the work that cites what changed → *re-opened items* (evidence: the pack's increment).
7. **Code steps.** Run the code steps of §5.5 and §5.6 (job descriptions, decision-rights register, authority matrix, charts) and of §5.7 (workload) → *generated parts* (evidence: the step's output hash, re-generated byte-identical).
8. **Stops and revocation.** A stop takes effect at the gateway on every part; the Chief of Staff is itself stopped. A revoked or narrowed connection holds the run as `held: connection revoked`; no restart is needed when a new connection is signed → *held run* (evidence: unit register).
9. **Returns from DI.** Run §5.11 for every return received from `[ORG]AIOC-DI`, whether or not a run is open → *each return carried to its end* (evidence: the returns log).
#### Role card
| Field | Content |
|---|---|
| Name | Chief of Staff |
| Position and seat | the position Chief of Staff; accountable seat: the PPD Design Lead (`[ORG]HOAC-ACS`) |
| Performed by | an agent (`[ORG]CELL-COSPPD`, full name PPD Chief of Staff) |
| Purpose | keep each run moving, honest and traced; be this AIOC's voice to the Design Lead and its only door to TOM, Source Lifecycle and DI |
| Authority limits | alone: dispatch, lock, record, run code steps, send returns and needs requests that passed their review, file a release whose elements are decided, send its release notice to DI, admit or refuse a return from DI by the contract, generate its brief, send its rows and its answer; needs the Design Lead: a second run in parallel, a budget above the cap, any change to configuration, a ruling on a finding, a reduced review level; never: ask a person anything about the organisation, change the TOM release, answer a needs request itself, take anything from the Design Lead as a source, decide for the Requesting Authority, rule on or dismiss a finding, sign, close a Work Item this AIOC performed, write a job description by hand, answer or classify a return from DI, edit a filed PPD Release, let a return wait without its round and deadline |
| Write location | the run record and this AIOC's Work Items |
| Reports to | the PPD Design Lead |
| Escalation | to the Design Lead in one line, with evidence linked; a stop goes to the stop door, never through this Cell |
| Tools and access | the TOM, Source Lifecycle and DI connections through the tool gateway, within their signed scopes; the code steps of the code project; no credential in any instruction |
| Deputy and cover | none; on failure the run halts and the Design Lead is told |
| Fixed test and score | TEST-PPD-COSPPD v3 (§9), plus the default Chief of Staff test |
| Card version and status | v0.4.0 · draft |
#### Fixed test
TEST-PPD-COSPPD v3 · result `NOT_RUN`

### 4.3 Input socket
#### Definition
Default, with this AIOC's standard format, the **Input Pack**, as in the TOM blueprint `v0.5.0` §4.3, parts 1 to 3 and 6 to 8, read with these changes:
1. **Two kinds of input.** The **release**: the decided TOM Release, by manifest and parts, each by hash, from the release notice. The **sources**: the organisation's other sources, by reference from Source Lifecycle's output socket, cut into atoms and labelled once (TOM Annex B, carried).
2. **The release is read, never atomised as a source.** Its elements keep their own IDs (`ROLE-n`, `HO-n`, `CPR-n`, `CHILD-…` and the ledger entry IDs). Every element of this AIOC's output traces to a release element or a source atom.
3. **The release check.** A release is admitted only when: its manifest validates; its final status is decided; its hash equals the copy filed in Source Lifecycle; and its role register re-compiles from its parts (TOM Annex E.17, rule 6). Otherwise nothing of it is used, and a return goes back with the failed condition (Annex B).
4. **A new release** from `[ORG]AIOC-TOM` makes a new pack version. The elements that changed re-open the work that cites them; decided work that cites nothing changed is kept by hash.
5. **Nothing that arrives through a human port is a source.** A run request is admitted only if it carries references; the words around them are not admitted.
6. The pack's ID is `PPDI-` followed by the SHA-256 of its body.
#### Process (SOP)
Default (receive, identify, normalise, check, deliver), run by the Chief of Staff through the socket's code steps. A refused item comes back with its reason and never enters.
#### Role card
Default; performed by the Chief of Staff (`[ORG]CELL-COSPPD`) through the socket's code steps.
#### Fixed test
TEST-PPD v3, cases 2, 3, 4, 23, 24, 25, 30, 33 · result `NOT_RUN`

### 4.4 Panel
#### Definition
Default. The Panel also shows, for each run: the run state and its flags with their ages; the TOM release in use and any newer one; every return, both ways, with its round, the deadline of that round, its state and its age (a return past its deadline in red, here and on the other stage's Panel); every needs request; each gate with its result; per review, its point, verdict and findings; the assumptions waiting for decision; the decision state of each element.
#### Process (SOP)
Default.
#### Role card
Default.
#### Fixed test
Default Panel test · result `NOT_RUN`

---
## 5. Functional capabilities

Ten stages (§5.0) are performed by the Input socket (§4.3: S0) and these capabilities: Release Intake and Returns (S1); Process Architecture (S2, S3); Process Writing (S4); Position Shaping (S5); Structure (S6); Workload (S7); Operational Walkthrough (S8); Decision Package and Release (S9). Needs Requests (§5.2) is a service every stage uses. Returns from Delivery and Implementation (§5.11) runs outside the runs, on each return received. Independent Review (§5.9) is the rule that closes every stage. Each capability is written in the four-part form (Annex A of the template), with one added row, **Done when**, which names its gate. Each step reads: **position**: action → *output* (evidence). Rules that apply to every capability are in Annex A (release parts and field lists), Annex B (returns), Annex C (run states and gates), Annex D (what this AIOC never does) and Annex E (what is carried from the TOM blueprint).

**One word per meaning.**
- **Release**, unqualified, is the TOM Release this run reads. **PPD Release** is this AIOC's output.
- **Role**: a role-type of the TOM release's role register (`ROLE-n`). **Position**: a position this AIOC designs (`POS-n`). A role may give rise to several positions; a position belongs to exactly one role.
- **Process** (`PRC-n`): a level-3 entry of the process architecture. **Step** (`STP-n`): one step of a process, in one role lane. **Decision** (`DEC-n`): a decision taken at a step.
- **Return** (`PPDR-n`): this AIOC's notice to `[ORG]AIOC-TOM` about its release (Annex B.1). A return from `[ORG]AIOC-DI` about a PPD Release carries DI's prefix (`DIR-n`; Annex B.2; §5.11).
- **Assumption**: a value no source gives (a volume, a time, a limit, a measure), marked as such and put to decision. It is never a fact.

### 5.0 The stages: input, output, done-test

| ID | Plain name | Run state | Gate | Exact input | Exact output | Done-test | Human decision |
|---|---|---|---|---|---|---|---|
| S0 | **Admit** | `admitting` | T0 | The run Work Item (references only). The release notice from `[ORG]AIOC-TOM`. The connection grants to TOM and Source Lifecycle. The engine register. | Input Pack `P0`; the run record, opened; the RP0 review record. | **T0** (Annex C.2): the request carries references only; the release check passes (§4.3, part 3); both connections are signed and in scope; the engine register holds eligible engines; `requesting_authority_cell` is set. | Requesting Authority: opens the run. Seats over TOM and Source Lifecycle: sign the connections. |
| S1 | **Read the release** | `reading` | T1 | P0 (or later); the release, role register first. | The **release-reading record** (Annex A.1); return drafts (Annex B). | **T1**: every role, value-stream phase, capability, decision domain and hand-off of the release in scope is `used`, `returned` or `out of scope` with a reason; the strategy frame, the journeys, the value case and the activity profile are recorded as the release states them; every return draft passed RP1 and was sent. | Requesting Authority: the children in scope, if the request did not name them. |
| S2 | **Architecture** | `architecting` | T2 | The release-reading record; the release; the pack's sources of current processes. | The **process architecture** (Annex A.2): levels 1 to 3, each level-3 process with one owner role. | **T2**: every phase and capability in scope has at least one process; every hand-off in scope belongs to one process; no process traces to nothing; RP2 settled clear. | Requesting Authority: the architecture rows. |
| S3 | **Critical processes** | `choosing` | T3 | The decided architecture. | The **critical-process choice**, with its reasons; the order in which processes are written. | **T3**: every process that crosses two parts of the release, or lies on a critical value stream, is either chosen or set aside with a reason; the order follows the priority of the elements each process carries; RP3 settled clear; the choice decided. | Requesting Authority: the choice and the order. |
| S4 | **Write the processes** | `writing` | T4 | Per process: its architecture entry; the release elements it carries; the pack's atoms for it. | Per process: its **process record** (Annex A.3). For a critical process: two locked drafts, the difference register and the reconciled record (Annex E, two authors). The **policy register** (Annex A.4) and the **controls catalogue** (Annex A.11), compiled by code from the process records. | **T4**, per process: each step has one accountable role and an input and output; each decision has exactly one decider; each lane hand-off is matched at both ends; each exception names its escalation; each measure, volume and time has a source or is an assumption; each step carries its done-when, worst error and reversibility, act kinds, input source and trust, confidentiality, risks, controls and record (§5.4, rules 11 and 12); the modelling conventions report no `error`; the end-to-end time is computed; RP4 settled with no unresolved `MATERIAL` finding. | Requesting Authority: assumptions; contradictions touching the process; control gaps; measure targets. PPD Design Lead: rulings. |
| S5 | **Shape the positions** | `shaping` | T5 | The written processes; the role register. | The **position register** (Annex A.5); the **job descriptions** (Annex A.6), generated by code; the **decision-rights register** and the **authority matrix** (Annex A.7), generated by code; the **objectives cascade** (Annex A.12), generated by code. | **T5**: every step and decision sits in exactly one position; every position holds at least one; every position belongs to one role; every position passes the segregation-of-duties rules or its breach is put to decision; every competence traces to a step or decision; the generated parts re-generate byte-identical; RP5 settled with no unresolved `MATERIAL` finding. | Requesting Authority: positions; decision limits with no source; job families and levels with no source; segregation rules with no source; separation breaches. |
| S6 | **Structure** | `structuring` | T6 | The position register; the release's parts and governance; the pack's sources of the current organisation. | The **unit register** and the **unit charters** (Annex A.15, charters generated by code); **reporting lines**, the **organisation charts** (generated by code), the **forum register** with charters and tiers, the **review calendar** (generated by code), the **result lines**, and the **crosswalk** (Annex A.8); the **structure scenarios** (Annex A.13) when `structure_scenarios` is above one. | **T6**: every position belongs to exactly one unit; every unit has one head position from among its own positions, one parent unit and a charter that traces to its positions; no unit loop; every position has one reporting line and no line forms a loop; spans and layers reported against the configured ranges; every forum has a charter and a tier; every measure has a forum that reviews it; every current unit, position and process in the sources is mapped or marked with a reason; with scenarios, each is shown on the same measures and one is decided; RP6 settled with no unresolved `MATERIAL` finding. | Requesting Authority: units and their heads; reporting lines that depart from the units; forums; span and layer findings; result lines with no source; the structure scenario; crosswalk rows marked `retired`. |
| S7 | **Workload** | `loading` | T7 | The written processes (volumes, step times); the position register; the time available per position, from a source or a decision. | The **workload register** (Annex A.9) and the **peak-load check and value-stream times** (Annex A.14), generated by code. | **T7**: every figure traces to the steps it sums; every input is a source or a decided assumption; every peak figure traces to its peak volumes and step times; RP7 settled clear. | Requesting Authority: the time available; assumptions; peak findings. |
| S8 | **Walk** | `walking` | T8 | The walk input, compiled by code from S2 to S7; a blind brief for the Situation Author. | The sealed situation set; the trace; the finding register; the **walkthrough report**. | **T8**: situations sealed before the walk; every situation traced to its end or to a finding; every finding fixed or put to decision; RP8 settled with no unresolved `MATERIAL` finding. | Requesting Authority: notice choices. PPD Design Lead: rulings. |
| S9 | **Decide and release** | `deciding`; end states `released`, then `filed` | T9, then T10 | Every reviewed part of S1 to S8, by hash; every pack version; the settled review records. | The **quality checks**; the Design Lead's attestation of T0 to T8; the **Decision Package** (Annex A.10); then the **PPD Release** manifest and its parts; the filing receipt; the release notice to `[ORG]AIOC-DI` (`contracts/release-notice.schema.json`). | **T9**: every element decided (`ACCEPT`, `CORRECT`, `REJECT`) and the final status decided; every process carries its owner position and its re-approval date; silence decided nothing. **T10**: the manifest is content-addressed; every element traces to a release element or a source atom; the release lint passes; the release is filed and reads back by hash; the release notice is sent. | Requesting Authority: each element and the final status. PPD Design Lead: the attestation. |

**Not stages: services and rules used by every stage.**

| Name | What it is | Output | Done-test |
|---|---|---|---|
| **Returns** (§5.1) | Every stage may find a defect in the release. It drafts a return; the Chief of Staff sends it to TOM after review | a return (Annex B.1) | Annex B, Done when |
| **Returns from DI** (§5.11) | DI may return a defect of a PPD Release. The Chief of Staff carries it to an end | the return at each version | §5.11, Done when |
| **Asking** (§5.2) | Every stage raises needs candidates; the Chief of Staff asks the Chief of Staff of `[ORG]AIOC-SL` | needs requests; one Missing Report per pass | each request ends answered by reference or with another outcome of the needs-answer contract |
| **Review Panel rule** (§5.9) | The rule that closes every stage | a review record and a verdict | §5.9, Done when |
| **Two authors** (Annex E) | Each critical process is written twice, blind, by two authors of two families, then reconciled | two locked drafts; the difference register; one reconciled record | TOM blueprint `v0.5.0`, Annex G, Done when, read with "process" for "child" |

**Run states.** `admitting` (S0) → `reading` (S1) → `architecting` (S2) → `choosing` (S3) → `writing` (S4) → `shaping` (S5) → `structuring` (S6) → `loading` (S7) → `walking` (S8) → `deciding` (S9) → `released` → `filed`. Endings, flags and holds: Annex C.1.

### 5.1 Release Intake and Returns

#### Definition
| Field | Content |
|---|---|
| Name | Release Intake and Returns |
| Purpose | read the decided TOM release so that nothing in it is lost, and send every defect back to the part that made it |
| Trigger | T0 passed; a new release notice; a defect found at any stage |
| Inputs | the Input Pack; the release, role register first |
| Outputs | the release-reading record (Annex A.1); returns (Annex B) |
| Performed by | the Release Reader (`[ORG]CELL-PRR`) in the Release Intake Pod (`[ORG]POD-PRI`); the Chief of Staff sends |
| Done when | T1 (§5.0); for a return, Annex B, Done when |
| Rules | 1. **Role register first.** The Release Reader reads every entry of the role register before any other part, and records for each: `used` (the processes that will carry it), `returned` (with the return) or `out of scope` (with the reason). 2. **Then the rest.** Every value-stream phase, capability, decision domain, hand-off (`HO-n`) and counterparty crossing (`CPR-n`) of the children in scope is accounted the same way. **New** in v0.5.0: so are the strategy frame, each outside party's journey (`JNY-n`), the value case (`VC-n`) and the current-state activity profile (TOM blueprint `v0.6.0`, Annex H), with each capability's delivery model and maturity, each stream's criticality and each element's decided priority. An element the release states as `not given`, `not decided`, `not set`, `unknown` or `no observation` is recorded as such and never filled. 3. **Never changed.** The release is read as decided. No element of it is edited, merged, split or dropped by this AIOC. A role register entry that no process uses is returned, never deleted. 4. **Returns, not fixes.** A defect becomes a return of one kind (Annex B): `cannot use` (with what is missing), `contradiction found`, `assumption invalid` or `request kind unsupported`. When the whole release is used without defect, the run sends one `accepted` return. 5. **The touched elements wait.** The elements a return touches, and only those, are held as `held: return open` until the return ends: answered by a new decided release, answered by a decision of the Requesting Authority, or set aside by that decision, in which case they go forward on the stated basis, each marked as a `known defect` or a `decided assumption` (Annex B.1, rule 5). The rest of the work goes on. 6. **Back and forth, in rounds.** TOM's answer arrives on the return itself and, for an answer by release, as a new release notice. A new release makes a new pack version; the work that cites a changed element re-opens; decided work that cites nothing changed is kept by hash. If the new release still does not answer, the same return is sent again in its next round. Each round has its deadline; TOM escalates past it (TOM blueprint `v0.5.0`, §5.10). Each pass is a new version; nothing is overwritten. 7. **Filed too.** Each return is also filed into Source Lifecycle as a design report, with the same hash, so that a revised TOM request can cite it (TOM blueprint `v0.5.0`, `docs/CARRIED-RULES.md` §4.4, item 5). 8. **Not a person.** A return names release parts, elements and fact-types, never a person. |

#### Process (SOP)
1. **Release Reader**: read the role register entry by entry, then the other parts of the children in scope → *release-reading record, draft* (evidence: one row per element).
2. **Release Reader**: for each element that cannot be used as decided, draft a return with its kind, its elements and its evidence → *return draft* (evidence: the draft, citing the elements and atoms).
3. **Chief of Staff**: lock the record and the drafts; run review point RP1 (§5.9) → *settled review* (evidence: the RP1 record).
4. **Chief of Staff**: send each return to `[ORG]AIOC-TOM`, file it into `[ORG]AIOC-SL`, mark the touched elements held → *sent return* (evidence: the Work Item and the filing receipt, with one hash).
5. **Chief of Staff**: on a new release notice, have the Input socket make a new pack version, re-open what cites a changed element, and close each answered return → *re-opened items; closed returns* (evidence: the pack's increment; the return's status).

#### Role card
| Field | Content |
|---|---|
| Name | Release Reader |
| Position and seat | Release Reader; accountable seat: the PPD Design Lead |
| Performed by | an agent (`[ORG]CELL-PRR`, full name PPD Release Reader) |
| Purpose | account for every element of the release, and draft every return |
| Authority limits | alone: read, record, draft returns; never: change the release, send a return itself, ask a person, decide what an element means where the release is silent (that is a return) |
| Write location | the run record |
| Reports to | Chief of Staff |
| Escalation | to the Chief of Staff, with the elements and evidence |
| Tools and access | the Input Pack only; no tools, no outside access, a fresh context per dispatch |
| Fixed test and score | TEST-PPD-PRR v3 (§9) |
| Card version and status | v0.3.0 · draft |

#### Fixed test
TEST-PPD-PRI v3 and TEST-PPD-PRR v3 · result `NOT_RUN`

### 5.2 Needs Requests

#### Definition
As in the TOM blueprint `v0.5.0` §5.2, carried, with these changes. What this AIOC typically asks for: the organisation's current process documents and procedures; volumes per period; step times; decision limits (for example spending thresholds); measures already in use; the time available per position per period; the policies a process applies. Each request names the process, step or decision it is for, and the unit of a figure. One decision per row; at most `rows_per_pass` rows per pass. A request never names a person. Done when: each request ends answered by reference, or with another outcome of the needs-answer contract, and its sub-item is `done` only when the Input socket's acceptance test passes.
#### Process (SOP)
As carried: the Pods raise needs candidates; the Chief of Staff batches, reviews (RPa), sends, waits, and admits each answer through the Input socket as a new pack version.
#### Role card
Performed by the Chief of Staff (§4.2).
#### Fixed test
TEST-PPD v3, cases 8, 31, 32, 33, 34 · result `NOT_RUN`

### 5.3 Process Architecture

#### Definition
| Field | Content |
|---|---|
| Name | Process Architecture |
| Purpose | lay out every process the decided model needs, in levels, and choose which to design first |
| Trigger | T1 passed |
| Inputs | the release-reading record; the release; the organisation's current processes, from the pack |
| Outputs | the process architecture (Annex A.2); the critical-process choice |
| Performed by | the Process Architect (`[ORG]CELL-PPA`) in the Architecture Pod (`[ORG]POD-PA`) |
| Done when | T2 and T3 (§5.0) |
| Rules | 1. **Three levels.** Level 1 is a value-stream phase or a capability of the release; level 2 groups processes; level 3 is a process with a trigger and an end. Every level-3 process traces to at least one level-1 entry. 2. **One owner.** Each level-3 process has one owner role from the role register; from S5 the owner is a position of that role. 3. **Hand-offs belong somewhere.** Every hand-off in scope (`HO-n`) and every crossing with an outside party (`CPR-n`) belongs to exactly one process, which names it. 4. **Today's processes are evidence.** A current process named in the sources is mapped to the architecture or marked `not carried` with its reason; the crosswalk (§5.6) uses this. 5. **Critical first.** The processes that cross two or more parts of the release, and those on a value stream the release marks critical (TOM Annex H.3), are proposed as critical. The Process Architect proposes an order with its reasons: first by the highest decided priority of the release elements each process carries (`must`, then `should`, then `could`; TOM Annex H.7), then critical before other; the Requesting Authority decides the choice and the order. 6. **A general pattern is a method, never evidence** (TOM Annex B.5, carried). 7. **Reference models as methods.** A reference process taxonomy, a leading-practice flow or a measure library may be used to check the architecture for completeness. Each is recorded in `method_refs` and is never evidence: what it suggests becomes a needs request or a finding, never a process on its own. 8. **As the capability is delivered** (**New** in v0.5.0; TOM Annex H.2). A capability delivered `in-house` gets its processes. One delivered as a `shared service` gets them in the child that provides it, and the consuming child's process hands off to it. One `outsourced` or delivered by a `partner` gets no in-house process for the delivered work: its process is the hand-off to the outside party, on the crossings that deliver it, and the steps that oversee it (instruct, receive, check, pay). A capability whose delivery model is `not decided` is designed only as far as the delivery model does not decide it; the rest is a return (`cannot use`, missing the delivery model). 9. **Journeys** (**New** in v0.5.0; TOM Annex H.5). Code checks each outside party's journey against the processes that carry its crossings: each moment sits in a process, and the moments follow, through the process hand-offs, in the journey's order. A moment in no process, or out of order, is a finding. 10. **Maturity sets the measures** (**New** in v0.5.0; TOM Annex H.4). Each process of a capability whose decided target maturity is 4 (`measured`) or 5 (`improving`) carries at least one measure; one without is a finding. |

#### Process (SOP)
1. **Process Architect**: draft the architecture from the release-reading record and the pack → *architecture draft* (evidence: one row per process, with its trace).
2. **Chief of Staff**: run RP2, then send the architecture rows to the Requesting Authority → *decided architecture* (evidence: decision references).
3. **Process Architect**: propose the critical processes and their order → *choice draft* (evidence: reasons per process).
4. **Chief of Staff**: run RP3, then send the choice for decision → *decided choice* (evidence: decision references).

#### Role card
| Field | Content |
|---|---|
| Name | Process Architect |
| Position and seat | Process Architect; accountable seat: the PPD Design Lead |
| Performed by | an agent (`[ORG]CELL-PPA`, full name PPD Process Architect) |
| Purpose | the whole map of processes, traced to the model, and the order of work |
| Authority limits | alone: draft the architecture and the choice; never: drop an element of the release, decide the choice, ask a person |
| Write location | the run record |
| Reports to | Chief of Staff |
| Escalation | to the Chief of Staff; a defect in the release is a return draft |
| Tools and access | the Input Pack only; a fresh context per dispatch |
| Fixed test and score | TEST-PPD-PPA v3 (§9) |
| Card version and status | v0.3.0 · draft |

#### Fixed test
TEST-PPD-PA v3 and TEST-PPD-PPA v3 · result `NOT_RUN`

### 5.4 Process Writing

#### Definition
| Field | Content |
|---|---|
| Name | Process Writing |
| Purpose | write each process so that any reader knows what starts it, who does each step, who decides, what passes between steps, and what happens when it goes wrong |
| Trigger | T3 passed; processes are written in the decided order |
| Inputs | per process: its architecture entry; the release elements it carries; the pack's atoms for it |
| Outputs | the process record (Annex A.3); for a critical process, two locked drafts and the difference register; the policy register (Annex A.4), compiled by code |
| Performed by | the First Process Author (`[ORG]CELL-PFPA`); for a critical process also the Second Process Author (`[ORG]CELL-PSPA`) and the Process Reconciler (`[ORG]CELL-PPR`); in the Process Writing Pod (`[ORG]POD-PPW`) |
| Done when | T4 (§5.0) |
| Rules | 1. **Lanes are roles.** Each step sits in one lane, and a lane is a role of the role register (positions come at S5). 2. **Things pass, not activities.** Each step has an input and an output that name a thing (a request, a record, a decision, a payment instruction). Each step's output is the next step's input, or an output of the process. 3. **One accountable role per step.** 4. **One decider per decision.** Each decision uses one notation: one role decides; others recommend, must agree, give input or carry out. A decision with no decider or with two fails. A decision the release gives to a role is kept with that role; a conflict is a return (`contradiction found`). 5. **Exceptions.** Each exception names its trigger, what happens, and the escalation route to a role with authority over it. 6. **Measures.** Each measure has its definition, its unit and its source, or is a decision row. None is invented. 7. **Volumes and times.** Each step carries its volume per period and its time per occurrence, from a source, or as an assumption with its basis, put to decision. 8. **Policies are named, not written.** Each rule a step applies cites a policy. The policy register lists each policy with its owner role and its source; a policy with no source is listed `needed`. This AIOC never writes the text of a policy. 9. **Two authors for a critical process.** Both authors write blind to each other, on engines of two families; code compares the locked drafts; the Process Reconciler disposes every material difference on the sources, or keeps only what both share and puts the rest to decision (TOM Annex G, carried). A non-critical process has one author and the same review. 10. **No filler.** A step is done by a role. It never says what fills the role. 11. **What each step must also say.** Its `done_when`: a property of its output that a reader can check. Its worst error, and whether that error can be undone (`yes`, `partly`, `no`). The kinds of act it is, from a fixed list: `decide`, `approve`, `sign`, `pay or commit money`, `communicate outside`, `physical`, `record`, `check`, `calculate`, `write`. Where its input comes from (`own record`, `outside party`, `system`, `request of a position`) and how far it is trusted (`verified`, `unverified`). The confidentiality class of what it handles, from the organisation's classification. Each has a source, or is an assumption put to decision. 12. **Risk, control and record.** Each step names its risks (what can go wrong, starting from its worst error), the controls that answer them, and the record it leaves. A step whose worst error cannot be undone, or whose act is to sign, to pay or commit money, or to communicate outside, carries at least one control, or the gap is a decision row. A control is designed from the sources or proposed for decision; it never claims that the organisation complies with anything. Code compiles the controls catalogue (Annex A.11) from the process records. 13. **Measures of three kinds.** Each process has measures of quality, of time and of cost, each with its definition, unit and source; a missing kind is a decision row. Each target is a decision, or reads `not set`. From S6, each measure names the forum that reviews it. 14. **Variants.** One process may carry variants for an entity, a site or a product. A variant names what it applies to, the steps where it differs and its reason; it changes no other step. 15. **Modelling conventions.** The conventions of `modelling_conventions` run by code on every record. A convention marked `error` blocks T4; one marked `warning` is reported. Rules 1 to 5 and 11 are always `error`. 16. **End-to-end time.** Code computes each process's end-to-end time along its main path, from its step times and the waiting time before each step, each from a source or a decided assumption. A missing term marks the figure incomplete. |

#### Process (SOP)
1. **First Process Author** (and, for a critical process, **Second Process Author**, blind): write the process record → *locked draft(s)* (evidence: draft hashes).
2. **Chief of Staff**: for a critical process, run the compare code step → *difference register* (evidence: the register).
3. **Process Reconciler**: reconcile into one record, disposing every material difference with its reason → *reconciled record* (evidence: the dispositions).
4. **Chief of Staff**: run the process checks and the modelling conventions by code (rules 2 to 4, 6, 7, 11 to 16), and compute the end-to-end time, then RP4 → *settled review* (evidence: the RP4 record; the convention results).
5. **Chief of Staff**: compile the policy register and the controls catalogue from the process records → *policy register; controls catalogue* (evidence: each re-compiles byte-identical).
6. **Chief of Staff**: send assumption, contradiction, control-gap and target rows for decision → *decided rows* (evidence: decision references).

#### Role card
| Field | Content |
|---|---|
| Name | First Process Author; Second Process Author; Process Reconciler |
| Position and seat | each its own position; accountable seat: the PPD Design Lead |
| Performed by | agents (`[ORG]CELL-PFPA`, `[ORG]CELL-PSPA`, `[ORG]CELL-PPR`) |
| Purpose | authors: write a process record from the release and the sources; reconciler: make one record from two |
| Authority limits | alone: write within the process record's fields; never: see the other author's draft before both are locked; settle a difference by choice; invent a figure; write a policy's text; ask a person |
| Write location | the run record |
| Reports to | Chief of Staff |
| Escalation | to the Chief of Staff; a defect in the release is a return draft |
| Tools and access | the Input Pack only; a fresh context per dispatch; author engines of two families (Annex E) |
| Fixed test and score | TEST-PPD-PFPA v3, TEST-PPD-PSPA v3, TEST-PPD-PPR v3 (§9) |
| Card version and status | v0.3.0 · draft |

#### Fixed test
TEST-PPD-PPW v3 and the tests of its Cells · result `NOT_RUN`

### 5.5 Position Shaping

#### Definition
| Field | Content |
|---|---|
| Name | Position Shaping |
| Purpose | shape the positions that carry the processes, each built from what it holds |
| Trigger | T4 passed for every process of the slice |
| Inputs | the written processes; the role register |
| Outputs | the position register (Annex A.5); the job descriptions (Annex A.6); the decision-rights register and the authority matrix (Annex A.7) |
| Performed by | the Position Builder (`[ORG]CELL-PPB`) in the Position Shaping Pod (`[ORG]POD-PPS`); the generated parts by the Chief of Staff's code steps |
| Done when | T5 (§5.0) |
| Rules | 1. **From the steps.** The Position Builder groups the steps and decisions of each role into positions. Every step and decision sits in exactly one position; every position holds at least one. 2. **One role.** Every position belongs to exactly one role of the role register. Work that fits no role is a return (`cannot use`), never a new role. 3. **Why this grouping.** Each grouping records its reason: the same expertise, the same counterpart, the same location, the same decision chain, or the release's own grouping. 4. **Separation.** A position that both takes a decision and checks that same decision fails, unless the Requesting Authority accepts it as a known defect. 5. **Generated, never written.** Each job description is generated by code from what the position holds: its purpose (from its processes' purposes), its accountabilities (its steps), its decisions and their limits, the positions it works with (its lane hand-offs), its measures and its reporting line (after S6). A field that does not trace to the position's steps and decisions fails the lint. 6. **Decision rights.** The decision-rights register lists every decision with its decider position, the others' parts and its limit. A limit with no source is a decision row. The authority matrix is generated from it. 7. **Positions only.** A job description names positions by code and title. It never names a person or a pay amount, and never says what fills the position. 8. **Job families and levels.** Each position carries its job family and its level when a source gives them or the Requesting Authority decides them. With neither, each field reads `not given` and the position goes on without it. They are never invented. Pay stays outside this AIOC (H-07). 9. **Segregation of duties.** Code checks every position against the segregation-of-duties rules of the controls catalogue (Annex A.11), for example one position both starting and approving the same payment, or both keeping an asset and recording it. Rule 4 is one of these rules. Each breach is listed with any compensating control and put to decision. A rule with no source is a decision row. 10. **Competence profile.** For each step and decision a position holds, the Position Builder states the knowledge and skill it needs, from the organisation's competence framework when a source gives one. The job description lists them as the position's competence profile. A competence that traces to no step or decision fails the lint. It never names a course, a provider or a person. 11. **The objectives cascade.** Code links each one-year goal and each critical number of the release's decided strategy frame (TOM Annex H.1; for a release that carries no strategy frame, each goal a source gives) to the measures of its value streams, then of its processes, then of the steps each position holds (Annex A.12). A goal with no measure under it, or a measure that serves no goal, is a finding. A goal the strategy frame marks `not given` makes no row; it is listed in the Decision Package, and no goal is written in its place. |

#### Process (SOP)
1. **Position Builder**: propose the positions, with their reasons → *position register, draft* (evidence: every step and decision placed once).
2. **Chief of Staff**: run the placement and segregation checks by code (rules 1, 2, 4, 9) → *check record* (evidence: the record).
3. **Chief of Staff**: generate the job descriptions with their competence profiles, the decision-rights register, the authority matrix and the objectives cascade → *generated parts* (evidence: re-generated byte-identical).
4. **Chief of Staff**: run RP5, then send position rows, limit rows, segregation rules with no source and separation breaches for decision → *decided rows* (evidence: decision references).

#### Role card
| Field | Content |
|---|---|
| Name | Position Builder |
| Position and seat | Position Builder; accountable seat: the PPD Design Lead |
| Performed by | an agent (`[ORG]CELL-PPB`, full name PPD Position Builder) |
| Purpose | group steps and decisions into positions, with reasons |
| Authority limits | alone: propose positions; never: write a job description, add a role, set a limit, name what fills a position, ask a person |
| Write location | the run record |
| Reports to | Chief of Staff |
| Escalation | to the Chief of Staff; work that fits no role is a return draft |
| Tools and access | the written processes and the role register only; a fresh context per dispatch |
| Fixed test and score | TEST-PPD-PPB v3 (§9) |
| Card version and status | v0.3.0 · draft |

#### Fixed test
TEST-PPD-PPS v3 and TEST-PPD-PPB v3 · result `NOT_RUN`

### 5.6 Structure

#### Definition
| Field | Content |
|---|---|
| Name | Structure |
| Purpose | group the positions into units, set who each position reports to, where positions meet, and how today's organisation maps to the target |
| Trigger | T5 passed |
| Inputs | the position register; the release's parts and governance skeleton; the pack's sources of the current organisation |
| Outputs | the unit register and the unit charters (Annex A.15); reporting lines; organisation charts (generated by code); the forum register with charters; the crosswalk (Annex A.8) |
| Performed by | the Structure Designer (`[ORG]CELL-PSD`) in the Structure Pod (`[ORG]POD-PS`) |
| Done when | T6 (§5.0) |
| Rules | 0. **Units first.** The Structure Designer groups the positions into units under each part of the release: teams, sections, departments, named in the organisation's own words. Each grouping records its reason: the same process or value stream, the same expertise, the same counterpart, the same location, or the release's own grouping. Every position belongs to exactly one unit; every unit holds at least one position, has one head position from among its own positions and one parent unit (the top units of a part sit under the part), and no unit tree forms a loop. Each unit's charter is generated by code from what its positions hold: its mandate (the processes and decisions it is accountable for), its head, its member positions, its forums, its measures and its result line; a charter line that traces to nothing fails the lint. 1. **One line.** Every position has one reporting line, within its part of the release, unless the release's governance places it elsewhere. By default a position reports to its unit's head, and a unit's head to the head of the parent unit; a line that departs from the units is a decision row. No line forms a loop. 2. **Spans and layers are checks.** They are reported against `span_range` and `layers_max`. A value outside the range is a finding for decision, never an automatic change. 3. **Forums.** Each standing forum the processes need (a committee, a board, a review meeting) has a charter: its purpose, the decisions it takes or advises on, its member positions, its chair position, its cadence, its inputs and its outputs. A forum takes only decisions the decision-rights register gives it. 4. **The crosswalk.** Every current unit, position and process named in the sources is mapped to a target element, or marked `retired` or `not mapped`, each with its reason. A `retired` row is a decision row. 5. **Charts are generated** from the reporting lines, never drawn by hand. 6. **Tiers and the review calendar.** Each forum carries its tier: `daily`, `weekly`, `monthly`, `quarterly` or `annual`. Code generates the review calendar from the forum register and the measures each forum reviews. A measure that no forum reviews, or a tier the processes need that no forum holds, is a finding for decision. 7. **The result line.** Each part of the release names the line of the organisation's results it moves most (for example revenue, cost, cash or risk), from a source or a decision. 8. **Structure scenarios.** When `structure_scenarios` is above one, the Structure Designer proposes that many structures. Code shows them side by side on the same measures: positions, management positions, spans, layers and cost. Cost appears only where the organisation gives cost rates per job family and level as a source; with none, it reads `not given`. The Requesting Authority chooses one; this AIOC never chooses. |

#### Process (SOP)
1. **Structure Designer**: propose the units with their heads and reasons, the reporting lines and the forums, and draft the crosswalk → *structure draft* (evidence: one row per unit, position, forum and current element).
2. **Chief of Staff**: run the unit and line checks, the span and layer report, and generate the unit charters, the charts, the review calendar and, with scenarios, the side-by-side view → *check record; charts; review calendar; scenario view* (evidence: re-generated byte-identical).
3. **Chief of Staff**: run RP6, then send the rows for decision → *decided rows* (evidence: decision references).

#### Role card
| Field | Content |
|---|---|
| Name | Structure Designer |
| Position and seat | Structure Designer; accountable seat: the PPD Design Lead |
| Performed by | an agent (`[ORG]CELL-PSD`, full name PPD Structure Designer) |
| Purpose | units, reporting lines, forums and the crosswalk |
| Authority limits | alone: propose; never: change a position's steps, move a position out of its role, write a unit charter by hand, change a span or layer to fit a range, retire a current element without a decision, ask a person |
| Write location | the run record |
| Reports to | Chief of Staff |
| Escalation | to the Chief of Staff |
| Tools and access | the position register, the release and the pack; a fresh context per dispatch |
| Fixed test and score | TEST-PPD-PSD v3 (§9) |
| Card version and status | v0.3.0 · draft |

#### Fixed test
TEST-PPD-PS v3 and TEST-PPD-PSD v3 · result `NOT_RUN`

### 5.7 Workload

#### Definition
| Field | Content |
|---|---|
| Name | Workload |
| Purpose | show the work each position carries, traced to its processes |
| Trigger | T6 passed |
| Inputs | the volumes and step times of the written processes; the position register; the time available per position per `workload_period`, from a source or a decision |
| Outputs | the workload register (Annex A.9), generated by code |
| Performed by | the Workload Analyst (`[ORG]CELL-PWA`) in the Structure Pod (`[ORG]POD-PS`) checks the inputs; the Chief of Staff's code step computes |
| Done when | T7 (§5.0) |
| Rules | 1. **The sum.** A position's workload for the period is the sum, over the steps it holds, of volume times step time. 2. **Traced.** Every figure names the steps it sums and the source or decided assumption of each input. 3. **Time, not anything else.** The register shows time per period against the time available. It draws no other conclusion. 4. **Gaps stay visible.** A step with no volume or no time is listed as a gap, and its position's figure is marked incomplete. 5. **Peak load.** Where a source gives a peak period and its volume, code computes each position's time needed in that period against its time available (Annex A.14). A peak above the time available is a finding for decision, never a change to a position. 6. **End-to-end time of a value stream.** Code adds the end-to-end times of the processes along each value stream (§5.4, rule 16). A missing term marks it incomplete. 7. **How the work runs today** (**New** in v0.5.0; TOM Annex H.8). The release's current-state activity profile is today's reading of the work, by role-type and process. It may be cited, by its atoms, as the basis of a volume or a step time of a process that replaces a process it names; and code shows today's figure beside the designed one, per process, in the workload register. It is never about a person, and it changes no position. Where it reads `no observation`, nothing stands in its place. |

#### Process (SOP)
1. **Workload Analyst**: check every input's source or assumption; raise needs candidates for gaps → *input check* (evidence: one row per step).
2. **Chief of Staff**: compute the register, the peak-load check and the value-stream times by code → *workload register; peak-load check* (evidence: re-computed byte-identical).
3. **Chief of Staff**: run RP7, then send the time-available row, the assumptions and the peak findings for decision → *decided rows* (evidence: decision references).

#### Role card
| Field | Content |
|---|---|
| Name | Workload Analyst |
| Position and seat | Workload Analyst; accountable seat: the PPD Design Lead |
| Performed by | an agent (`[ORG]CELL-PWA`, full name PPD Workload Analyst) |
| Purpose | make sure every workload input has a source or a decision |
| Authority limits | alone: check inputs and raise needs candidates; never: estimate a figure, change a position, ask a person |
| Write location | the run record |
| Reports to | Chief of Staff |
| Escalation | to the Chief of Staff |
| Tools and access | the written processes and the position register; a fresh context per dispatch |
| Fixed test and score | TEST-PPD-PWA v3 (§9) |
| Card version and status | v0.3.0 · draft |

#### Fixed test
TEST-PPD-PWA v3 · result `NOT_RUN`

### 5.8 Operational Walkthrough

#### Definition
As in the TOM blueprint `v0.5.0` §5.7, carried, read with "processes, positions and decisions" for "operating model". The Situation Author writes situations blind to the design, from a blind brief compiled by code (the parts of the release in scope, the roles, the hand-offs; never the process records). The set is sealed before the walk. The Situation Walker walks each situation through the processes, positions, decisions and forums, and records where it holds and where it breaks: a step with no position, a decision with no decider, a hand-off that ends nowhere, an exception with no escalation, a forum asked to decide what it may not. Done when: T8 (§5.0).
#### Process (SOP)
As carried: compile the walk input and the blind brief; author; seal; walk; classify; RP8; route each finding (fix upstream, or put to decision).
#### Role card
Situation Author (`[ORG]CELL-PSA`) and Situation Walker (`[ORG]CELL-PSW`), in the Walkthrough Pod (`[ORG]POD-PW`); as carried, with their own tests.
#### Fixed test
TEST-PPD-PW v3, TEST-PPD-PSA v3, TEST-PPD-PSW v3 · result `NOT_RUN`

### 5.9 Independent Review

#### Definition
The Review Panel rule of the TOM blueprint `v0.5.0` §5.8, carried whole: three to five engines from two or more families review each locked output, alone first, then in a short debate held to quotes; code settles; the PPD Design Lead rules only on what stays contested; at the `full` level no engine is of an author's family (its rule 4); the Chief of Staff never rules, dismisses, downgrades or lowers. This AIOC's review points: RP0 (P0), RP1 (release-reading record and return drafts), RP2 (architecture), RP3 (critical-process choice), RP4 (each process record), RP5 (positions and generated parts), RP6 (structure), RP7 (workload), RP8 (walk findings), RP9 (the release, before filing), and RPa (each needs pass). Done when: as carried.
#### Process (SOP)
As carried.
#### Role card
Blind Reviewers A to E (`[ORG]CELL-PBRA` to `[ORG]CELL-PBRE`), in the Review Pod (`[ORG]POD-PR`); as carried.
#### Fixed test
TEST-PPD-PR v3 and the tests of its Cells · result `NOT_RUN`

### 5.10 Decision Package and Release

#### Definition
| Field | Content |
|---|---|
| Name | Decision Package and Release |
| Purpose | put every element to the organisation's decision, then freeze, file and hand over the decided design |
| Trigger | T8 passed |
| Inputs | every reviewed part of S1 to S8, by hash; the settled review records |
| Outputs | the quality checks; the Decision Package (Annex A.10); the PPD Release manifest and its parts; the filing receipt; the release notice to `[ORG]AIOC-DI` (`contracts/release-notice.schema.json`) |
| Performed by | the Chief of Staff, by code steps; the PPD Design Lead attests the method |
| Done when | T9 and T10 (§5.0) |
| Rules | 1. **Every element is decided.** The Decision Package puts each element to the Requesting Authority: `ACCEPT`, `CORRECT` or `REJECT`; then the final status. Silence, or approval of a whole pass, decides nothing (TOM blueprint `v0.5.0`, `docs/CARRIED-RULES.md` §5, carried). 2. **Plain words.** The Decision Package states the unknowns, the assumptions and the open returns in plain words. 3. **Frozen and content-addressed.** The manifest lists every part by hash, every pack version, the TOM release it was designed from (ID and manifest hash) and every return sent. 4. **The release lint.** The release holds processes and positions only: no person's name, no pay, nothing on what fills a position, no text of a policy. 5. **Filed and handed over.** The release is filed into Source Lifecycle as a source of origin kind `process and position design` and read back by hash. Then a release notice goes to `[ORG]AIOC-DI` (Protocol §20, item 9): the PPD Release ID, version and manifest hash, the TOM Release it rests on, the filed reference, the final-status decision reference, the release it supersedes and the returns it answers; never release text. It is sent once, after the read-back. Where the connection is not signed, it waits on the Panel and nothing of the run waits for it. 6. **Returned to us.** `[ORG]AIOC-DI` returns defects to this AIOC under the same contract, and each ends by §5.11. A change is a new run whose release supersedes this one. 7. **Approval and re-approval.** Each decided process carries its owner position, the decision that approved it, and its re-approval date, set from `re_approval_period`. The release lists every process with its date; the stage that runs the organisation raises the review when it falls due. 8. **Set-aside returns are visible.** Every element carried forward on a set-aside return (Annex B.1, rule 5) is listed in the Decision Package in plain words and in the manifest, with its basis and the decision. 9. **Priority carried** (**New** in v0.5.0; TOM Annex H.7). Each process and each position carries the highest decided priority of the release elements it carries; the Decision Package orders its rows by it, and the release states it, so that the stage after this one rolls out in that order. |

#### Process (SOP)
1. **Chief of Staff**: generate the quality checks and the Decision Package; obtain the Design Lead's attestation of T0 to T8 → *Decision Package* (evidence: hashes).
2. **Chief of Staff**: run RP9; send the element rows and the final status for decision → *decided rows* (evidence: decision references).
3. **Chief of Staff**: freeze the manifest, run the release lint, file into `[ORG]AIOC-SL`, read back, send the release notice to `[ORG]AIOC-DI` → *filed PPD Release; release notice* (evidence: the filing receipt, the read-back hash, and the notice's hash).

#### Role card
Performed by the Chief of Staff (§4.2); the attestation by the PPD Design Lead (§13, H-12).

#### Fixed test
TEST-PPD-COSPPD v3 (cases 64 to 67, 99 and 100) · result `NOT_RUN`

### 5.11 Returns from Delivery and Implementation

**New** in v0.4.0 (`decisions/DR-0004`). The receiving end of the Library's design return contract for the stage after this one, as the TOM blueprint `v0.5.0` §5.10 is for the stage before (carried, Annex E).

#### Definition
| Field | Content |
|---|---|
| Name | Returns from Delivery and Implementation |
| Purpose | no defect DI finds in a PPD Release is lost, and none is left open: each ends, so that DI can deliver |
| Trigger | a return arrives on the connection of `[ORG]AIOC-DI`; a round's deadline passes; a decision on a return row is recorded; a PPD Release that answers a return is filed |
| Inputs | a return (Library design return contract, pinned in `contracts/PINS.json`); its filed copy in Source Lifecycle, by reference; the PPD Release it names |
| Outputs | the returns log (as TOM Annex E.21, with `sender` `[ORG]AIOC-DI`); the return brief and its rows (as TOM Annex E.22); the return at each next version (the return answer); the PPD Design Lead's classification |
| Performed by | the Chief of Staff, by code steps; the PPD Design Lead classifies |
| Done when | the return has ended (`answered by release`, `answered by decision`, `set aside by decision` with its `carried_forward_on`, or `withdrawn` by DI); the ended return is sent back to DI; the PPD Design Lead has classified it |
| Rules | 1. **Admission.** Admitted only if it validates against the pinned contract, names a PPD Release this AIOC filed with the same manifest hash, has a filed copy that reads back with the same hash, and came on DI's connection; otherwise refused back with the reason, never edited. 2. **Never a change to the release.** A filed PPD Release is never edited; a return is answered only by a new decided PPD Release (a new run that cites the filed return) or by a decision of the Requesting Authority. 3. **`accepted` asks nothing.** It is recorded and ends at once, `answered by release`, by the release it names. 4. **A brief made by code; one decision per row.** Three rows, each decided alone: open a new run naming the processes, positions or units to change; answer by decision; or set aside and carry forward as a `known defect` or a `decided assumption`. No row names a person; silence decides nothing. 5. **Rounds.** Round 1 opens on receipt, with the deadline `return_round_deadline`; an answer by release opens the next round when DI returns the same elements again. 6. **Escalation.** Past a deadline, or at `return_rounds_max`, the return goes to the Requesting Authority with two rows only (answer by decision, or set aside), is raised to the Cell carrying `[ORG]HOAC-TM`, and is red on both Panels until decided. 7. **A defect of TOM is passed on, never answered here.** Where the defect lies in the TOM Release that the PPD Release rests on, DI returns it to TOM itself (Protocol §20, item 3); this AIOC answers only for its own release. 8. **Classified, never self-graded.** Each ended return is classified by the PPD Design Lead, never by the Chief of Staff, as a defect of this AIOC or normal discovery; a defect becomes a lesson in §12 and a proposed test case. |

#### Process (SOP)
1. **Chief of Staff**: admit or refuse the return by rule 1; record it; show it on the Panel with its age; end an `accepted` return at once → *recorded return* (evidence: the returns log, with the return's hash).
2. **Chief of Staff (runs the return-brief code step)**: generate the brief and its rows → *return brief* (evidence: hash).
3. **Chief of Staff**: send the rows as decision needs requests through `[ORG]AIOC-SL` (§5.2) → *decision rows* (evidence: the needs log).
4. **Requesting Authority** (in Source Lifecycle): decide one row → *decision reference*.
5. **Chief of Staff**: record the decision on the return as its next version; on a new PPD Release that answers it, mark it `answered by release`; send the answer back to DI on its connection → *return answer* (evidence: the return's version, valid against the pinned contract).
6. **Chief of Staff**: on DI's next round, repeat 1 to 5; past a deadline, or at `return_rounds_max`, escalate by rule 6 → *escalated return* (evidence: the returns log).
7. **PPD Design Lead**: classify each ended return by rule 8 → *classification record* (evidence: run record, live sign-in).

#### Role card
Performed by the Chief of Staff (§4.2); the classification by the PPD Design Lead (§13, H-19).

#### Fixed test
TEST-PPD-COSPPD v3 (cases 101 to 104) and TEST-PPD-PDL v3 (PDL-6) · result `NOT_RUN`

---

## 6. Coordination and routes

- **`[ORG]AIOC-TOM`.** The operating model source, linked directly (Protocol §17, items 2 and 3).
  - **Routes.** Release notices arrive through the Input socket. Returns leave as Work Items through the output port, each also filed into Source Lifecycle.
  - **The connection.** Signed by the `[ORG]HOAC-ACS` position over `[ORG]AIOC-TOM` as `connect-external-port`, with two scopes: read its decided releases; send returns. A wider scope is `grant-or-widen-access`. A revocation cuts it at the gateway at once and holds the run.
  - **Loops.** A return is a Work Item to TOM. TOM answers it on that Work Item (and, for an answer by release, with a new release notice); it never opens a new item back to this AIOC, so the chain never loops (Protocol §4.6, item 2). Every return ends (Annex B.1).
- **`[ORG]AIOC-SL`.** The source of record, and the only route to any person in the organisation.
  - **The connection.** Signed by the `[ORG]HOAC-ACS` position over `[ORG]AIOC-SL` as `connect-external-port` (Protocol §13, item 5), with three scopes: read; needs requests; write only this AIOC's own releases and design reports (its returns).
  - **Needs requests** are sub-items of the run, with chain depth 1.
- **`[ORG]AIOC-DI`, the next stage, linked directly** (Protocol §20, item 9). **New** in v0.4.0.
  - **Routes.** On every filing of a decided PPD Release, a release notice leaves through the output port (§5.10, rule 5). DI reads the release from Source Lifecycle, by the reference in the notice. DI's returns arrive at the Chief of Staff's port and end by §5.11.
  - **The connection.** One connection with two scopes: release notices to DI; returns from DI and their answers. Signed by the `[ORG]HOAC-ACS` position over this AIOC, the PPD Design Lead's, as `connect-external-port` (H-16). A revocation cuts it at the gateway at once; notices and answers wait, shown on the Panel. This AIOC stands alone without it.
  - **Loops.** A return is a Work Item from DI; this AIOC answers it on that Work Item and never opens a new item back.
- **Work Items.**
  - **The run.** One Work Item, opened by the Requesting Authority's Cell through the HU input port. Requested output: a PPD Release (Annex A). Acceptance test: the Requesting Authority's (T9 decided; the manifest valid; the filed reference reads back). Sources: the TOM Release reference and, optionally, the children in scope.
- **`[ORG]AIOC-OCO`.** It installs, fixes and upgrades this AIOC through the front door. Every proposal, correction or critique of this AIOC's AIs is a `design-proposal` Work Item to OCO.
- **Routing rows this AIOC contributes.** `return → [ORG]AIOC-TOM`; `return filing → [ORG]AIOC-SL`; `needs request → [ORG]AIOC-SL`; `missing report → [ORG]AIOC-SL`; `PPD Release filing → [ORG]AIOC-SL`; `release notice → [ORG]AIOC-DI`; `return answer → [ORG]AIOC-DI`.

## 7. Records and where things live

| Record | Home | Source rule |
|---|---|---|
| This blueprint, its contracts, tests, decisions and cards | the writing repository `<org>aioc-ppd` | one home for each thing |
| The code steps of this blueprint and the PRD | the code project `<org>aioc-ppd` | one home for each thing |
| An organisation's run records: Input Pack versions, drafts, difference registers, review records, ruling sheets, traces | `<org>aioc-ppd-records`; `-records-restricted` for any run record that touches a Strictly confidential source | append-only; referenced from the release manifest by hash |
| The organisation's sources, the needs answers, the decisions, the filed PPD Release and the filed returns | `[ORG]AIOC-SL` | Source Lifecycle is the only home of a source |
| The TOM Release | `[ORG]AIOC-TOM`, filed in `[ORG]AIOC-SL` | read by reference and hash, never copied |
| The link between positions and whoever occupies them | not here: top management's own mechanism (Standard §1.1, item 9) | never in this AIOC |
| Work Items | the shared queue | Protocol §2 |

- **References, not copies.** Atom text and release text are held only in the run workspace. Records store IDs and hashes.
- **Revocation or reclassification.** On a notice from Source Lifecycle or TOM, the run is held and its workspace copies are sealed.
- **Engine ceilings.** No atom or release part is sent to an engine whose confidentiality ceiling is below its level (TOM blueprint `v0.5.0` §5.8, rule 17, carried).

## 8. Tools and the shared AI gateway

| Tool | Existing shared tool, or new | If new: asked of the builder as |
|---|---|---|
| The TOM connection (release notice in, returns out, answers in) | made on the TOM side in the TOM blueprint `v0.5.0` | — |
| The DI connection (release notice out, returns in, answers out) | new on this side; DI's side is in its blueprint (`upstream/PROPOSALS.md` of `<org>aioc-di`, item 1) | build items in the code project |
| The Source Lifecycle connection (output socket, needs requests, filing) | existing in `[ORG]AIOC-SL`, with the proposed additions already asked by `[ORG]AIOC-TOM`; the origin kind `process and position design` is new | a change to `[ORG]AIOC-SL` proposed through OCO (`upstream/PROPOSALS.md`, item 2) |
| The code steps: the socket and the release check; the release-reading check; process checks; draft compare; policy-register compile; placement checks; job-description, decision-rights and authority-matrix generators; line checks, span and layer report, chart generator; workload compute; walk-input compile and blind-brief extract; review code steps (carried); quality checks; release lint | new in this AIOC's code project, one build item per step, each with its tests | build items in the code project |
| The schemas of Annex A, the release notice and the return contract | the release notice is in `contracts/`; the return contract is the Library's, pinned in `contracts/PINS.json`; the others are field lists in Annex A, made into schemas before the first run | build items in the code project |
| Engine calls | through the tool gateway, bound per call from the engine register | — |

- **Metering.** Every engine call goes through the tool gateway of the `[ORG]AION`, metered for this AIOC (Standard §4.4, item 11).
- **Null default.** Every AI Cell runs with no tools, no outside access, no memory and a fresh context for each dispatch.
- **Tests stay hidden from the runners.** No Cell under test sees TEST-PPD, its fixtures or §9.

| Tool role | Connector | Access managed in | Part card version |
|---|---|---|---|
| operating model source | `[ORG]AIOC-TOM` release port | Panel; the grant is signed at the tool gateway as `connect-external-port` | 49GAION Target Operating Model, v1 |
| source of record | `[ORG]AIOC-SL` output socket | Panel; as above | 49GAION Source Lifecycle, v1 |
| next design stage | `[ORG]AIOC-DI` input port: release notices out, returns in | Panel; signed by the `[ORG]HOAC-ACS` position over this AIOC (H-16) | 49GAION Delivery and Implementation, v1 |

**Mechanism register.** Read on 15 October 2026. A row is never deleted.

| ID | Mechanism | What it does | Where it lives | Today | Target |
|---|---|---|---|---|---|
| M-01 | Release check | admits only a decided release whose hash matches its filed copy | — | decided, not built | build |
| M-02 | Return path to TOM | sends returns, holds touched elements, re-opens on a new release | — | decided, not built | build (with the TOM change) |
| M-03 | Process checks | one accountable role per step; one decider per decision; matched hand-offs | — | decided, not built | build |
| M-04 | Generators | job descriptions, decision-rights register, authority matrix, charts, workload | — | decided, not built | build |
| M-05 | Release lint | keeps the release to processes and positions | — | decided, not built | build |
| M-06 | Review Panel rule | as carried from `[ORG]AIOC-TOM` | `[ORG]AIOC-TOM` code project, when built | decided, not built | reuse |
| M-07 | Release notice to DI | announces each filed PPD Release by reference | — | decided, not built | build |
| M-08 | Returns from DI | admission, brief, rounds, escalation and the answer, as TOM's §5.10 | `[ORG]AIOC-TOM` code project, when built | decided, not built | reuse |

**Reserve.**

| ID | Idea | Why held | Reconsider when |
|---|---|---|---|
| R-01 | Job families and levels in the position register | taken up on 15 October 2026 (§13, H-07); kept here as a record | — |
| R-02 | A shared review service for every design stage, instead of each stage carrying the TOM rule | one more part to build before the first run | a third design stage needs the same rule |

## 9. Fixed tests: index, triggers and scores

The cases are written in `tests/TEST-PPD.md` (v3). Cases 1 to 22 are the Library's TEST-PROCESS-AND-POSITION-DESIGN v1, cases 1 to 22, unchanged. Cases 23 to 111 are this AIOC's own; case 27 is struck in v2 and replaced by case 98. The Design Lead's seat test is PDL-1 to PDL-6. The Library's TEST-PROCESS-AND-POSITION-DESIGN v2 numbers its added cases 23 to 34 in its own series; they are covered here as follows: 23 → 78 to 81; 24 → 82; 25 → 83, 84; 26 → 95, 96; 27 → 97; 28 → 86; 29 → 87; 30 → 88; 31 → 89, 90; 32 → 85, 94; 33 → 93; 34 → 98, 104. The owner of every part's test is the PPD Design Lead; the owner of the AIOC's whole test, and of the Design Lead's own seat test, is the Cell carrying `[ORG]HOAC-TM`.

| Part | Test ID and version | Cases of TEST-PPD v3 | Evidence level | Last run | Result |
|---|---|---|---|---|---|
| `[ORG]AIOC-PPD` (whole) | TEST-PPD v3 | all (1–111; 27 struck) | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PDL` PPD Design Lead | TEST-PPD-PDL v3 | PDL-1 to PDL-6 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-COSPPD` Chief of Staff (with Office, Input socket, Needs Requests, Decision Package and Release) | TEST-PPD-COSPPD v3 | 1–4, 8, 13, 18, 19, 21–26, 29–34, 48, 51, 62, 64–67, 73–75, 83, 84, 86, 87, 90, 92, 94, 96, 98–105, 108, 110 | MEASURED | — | `NOT_RUN` |
| Panel | default Panel test | — | MEASURED | — | `NOT_RUN` |
| `[ORG]POD-PRI` Release Intake | TEST-PPD-PRI v3 | 3, 5, 6, 7, 28, 30, 47, 111 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PRR` Release Reader | TEST-PPD-PRR v3 | 3, 5, 28, 30, 47, 111 | MEASURED | — | `NOT_RUN` |
| `[ORG]POD-PA` Architecture | TEST-PPD-PA v3 | 9, 10, 35–38, 93, 106–109 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PPA` Process Architect | TEST-PPD-PPA v3 | 9, 10, 35–37, 93, 106, 107 | MEASURED | — | `NOT_RUN` |
| `[ORG]POD-PPW` Process Writing | TEST-PPD-PPW v3 | 11, 16, 39–45, 78–82, 86, 91 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PFPA` First Process Author | TEST-PPD-PFPA v3 | 11, 16, 40–45, 78–82, 86, 91 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PSPA` Second Process Author | TEST-PPD-PSPA v3 | 11, 16, 39–45, 78–82, 86, 91 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PPR` Process Reconciler | TEST-PPD-PPR v3 | 39, 41 | MEASURED | — | `NOT_RUN` |
| `[ORG]POD-PPS` Position Shaping | TEST-PPD-PPS v3 | 12, 13, 20, 46–52, 77, 84, 85, 105 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PPB` Position Builder | TEST-PPD-PPB v3 | 12, 20, 46, 47, 52, 77, 85 | MEASURED | — | `NOT_RUN` |
| `[ORG]POD-PS` Structure | TEST-PPD-PS v3 | 14, 15, 53–58, 87–90, 95–97, 110 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PSD` Structure Designer | TEST-PPD-PSD v3 | 14, 53–56, 87, 88, 95, 97 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PWA` Workload Analyst | TEST-PPD-PWA v3 | 15, 16, 57, 58, 89, 90, 110 | MEASURED | — | `NOT_RUN` |
| `[ORG]POD-PW` Walkthrough | TEST-PPD-PW v3 | 17, 59, 60 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PSA` Situation Author | TEST-PPD-PSA v3 | 59 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PSW` Situation Walker | TEST-PPD-PSW v3 | 17, 60 | MEASURED | — | `NOT_RUN` |
| `[ORG]POD-PR` Review | TEST-PPD-PR v3 | 22, 61–63 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PBRA` to `[ORG]CELL-PBRE` Blind Reviewers | TEST-PPD-PBRA v3 to TEST-PPD-PBRE v3 | 22, 61, 63 | MEASURED | — | `NOT_RUN` |
| Type (Specialised) | TEST-PPD v3, case 76 | 76 | MEASURED | — | `NOT_RUN` |

- **Re-run triggers.** The template defaults, plus any change to the pin of the Library's design return contract, to the release notice contract, to the TOM release or notice format, to the Source Lifecycle output socket, or to the release lint's word list.
- **Complete** only when every part's test has a visible result. `NOT_RUN` is never PASS.

**Checks that are not fixed tests.**

| Check | Placement | Budget per item | Degradation order | Blocks only for |
|---|---|---|---|---|
| Outbound name check: no person's name in any return, needs request or release part | router | each outbound message | none | the message |
| Release lint | as evidence on the verdict record of RP9 | each release | none | the filing |
| Re-generation check: every generated part re-generates byte-identical | inside the producer's loop, at most 2 fix rounds | each generated part | none | the stage's gate |
| Return reconciliation: every return sent has a filed copy with the same hash | after completion | daily | none; a failure opens a defect | nothing; it flags |
| Return clock: every open return, both ways, shows its round and deadline; a return past its deadline is escalated | the router | each return | none | nothing; it raises |

## 10. Build: what is generated from this file

| Built thing | Generated from | Recorded where |
|---|---|---|
| Panel profile | §0, §1, §3, §4.4, §5 role cards | the panel profile names this file's commit |
| Back office | §4.2 role card and SOP (instruction); §4 to §5 (knowledge) | the back office records the commit it was built from |
| Card in the protocol AIOC's map | §1 | the register links this file |
| Cards of the Pods and Cells, and the bot identity cards | §17 | `cards/`, by `tools/make_cards.py` |
| The validators of the release notice and of this AIOC's return examples | `contracts/release-notice.schema.json`; the Library's design return contract at the commit pinned in `contracts/PINS.json` | `tools/check_contracts.py` |

**Delivery path:** definition change → tests → Panel and Back office update → one-click rollback to the previous commit.

## 11. Exceptions

1. **The Chief of Staff never asks the organisation's people anything.** It reaches the organisation only through the Chief of Staff of `[ORG]AIOC-SL`. Reason: as for `[ORG]AIOC-TOM` (its §11, item 1); a design rests on recorded sources, never on words spoken to the designer.
2. **The Back office does not converse with humans** (`converses_with_humans: false`). Reason: as in item 1.
3. **Two operating sources.** The template's Input socket takes sources. This one also takes a design release directly from another AIOC, by reference and hash, and returns defects to it. Reason: the direction of the governing seat that this AIOC is linked to the TOM itself (`decisions/DR-0001`; Protocol §17, items 2 and 3).
4. **Rules carried by reference.** The Review Panel rule, the two-author rule, labels, decision rules and the receiving end of returns are carried from the TOM blueprint `v0.5.0` by section, not restated. A change there reaches this AIOC only when this blueprint pins the new version (Annex E).

## 12. Lessons and proposals to the mother

One dated line per lesson, each written without any organisation's details. Nothing is proposed upstream without the governing seat's word; the drafts are in `upstream/PROPOSALS.md`.

1. 2026-10-15 · The stage after the operating model was first framed as positions alone. Leading design practice designs processes and decision rights with the roles, processes first. Test question added: case 12 (no position without a step or decision). This text is the mother.
2. 2026-10-15 · A stage that reads a design release must be able to send defects back to the stage that made it, without a person relaying them. Test question added: cases 5 to 7. Proposed: the TOM changes in `upstream/PROPOSALS.md`, item 1.
3. 2026-10-15 · Fifteen products that design, launch or run organisations were taken apart from public material, and each useful feature was placed in the stage where it truly belongs. Those that belong here: the facts of each step, controls and segregation of duties, the objectives cascade, measures of three kinds, structure scenarios, peak load, variants, modelling conventions, forum tiers, end-to-end time and re-approval. Anything that rates or watches a person was not taken. Test questions added: cases 78 to 94 (`decisions/DR-0002`). Proposed: `upstream/PROPOSALS.md`, item 5.
4. 2026-10-15 · A review of what launching an organisation needs after this stage found three small additions that belong here: a competence profile in each job description; risk, control and record per step; measure definitions and the review calendar beside the forums. Test questions added: cases 82, 85 and 87 (`decisions/DR-0002`).
5. 2026-10-15 · Positions alone do not make an organisation that can launch: they must be grouped into units, each with a head and a mandate, and that grouping belongs in the same stage as the positions. Test questions added: cases 95 to 97 (`decisions/DR-0003`).
6. 2026-10-16 · A return that can only wait does not end, and a stage that is never told of a release learns of it late. Returns, both ways, now follow the Library's contract and always end; the stage after this one is told of each release directly. Test questions added: cases 98 to 104 (`decisions/DR-0004`; `49GAION/DR-0016`, `DR-0018`).
7. 2026-10-16 · The stage before this one now states what this stage needs to start: the strategy, how each capability is delivered, which streams are critical, each outside party's journey, a priority per element, and how the work runs today. This stage reads them and never fills them. Test questions added: cases 105 to 111 (`decisions/DR-0005`).

## 13. For the `[ORG]HOAC-ACS` seat, and every decision only a human seat can take

Every decision that only a human seat can take is listed here once. Silence decides nothing; a general approval decides no row.

| ID | Decision | Seat | Default |
|---|---|---|---|
| H-01 | Name the Requesting Authority's Cell: the GOV Cell itself, or a human Cell to which it delegates the design decisions (`delegate-authority`) | GOV | none: T0 fails |
| H-02 | **Top management's own mechanism.** Arrange the PPD Design Lead position and any HOAC position added to this AIOC. Nothing of who occupies them enters this blueprint | the Cell carrying `[ORG]HOAC-TM` | the position is vacant: the AIOC does not join |
| H-03 | Install `[ORG]AIOC-PPD` (`create-or-install-unit`); its `change-parent`; its `restart-stopped-unit` | the Cell carrying `[ORG]HOAC-TM` | none |
| H-04 | Accept the TOM changes that let this AIOC read releases directly and send returns (`upstream/PROPOSALS.md`, item 1; made in the TOM blueprint `v0.5.0`) | the Cell carrying `[ORG]HOAC-TM`, made through OCO | required before joining |
| H-05 | Accept the Source Lifecycle origin kind `process and position design` and this AIOC's filing scope (`upstream/PROPOSALS.md`, item 2) | the Cell carrying `[ORG]HOAC-TM`, made through OCO | required before joining |
| H-06 | The connection grants to TOM and to Source Lifecycle (`connect-external-port`), their widening and revocation | the `[ORG]HOAC-ACS` positions over `[ORG]AIOC-TOM` and `[ORG]AIOC-SL` | none: T0 fails |
| H-07 | **People.** Job families and levels in the position register. **Decided by GOV, 15 October 2026** (`decisions/DR-0001`, item 8): carried, from a source or a decision of the Requesting Authority; `not given` when neither gives them; never invented. Pay stays outside this AIOC in every case | GOV (decided); the Requesting Authority for each value with no source | carried |
| H-08 | `review_budget_per_run`, `reduced_review_permitted` and the AIOC's `budget_cap` | the Cell carrying `[ORG]HOAC-TM` | none: must be set; reduced review `no` |
| H-09 | `span_range`, `layers_max`, `workload_period`, `re_approval_period` and `structure_scenarios` | the Cell carrying `[ORG]HOAC-TM` | none: must be set; `structure_scenarios` 1 |
| H-10 | Open the run; name the children in scope | Requesting Authority | none: no run |
| H-11 | The rows of S1 to S9: architecture; critical choice and order; assumptions; contradictions; control gaps; measure targets; positions; units and their heads; decision limits; job families and levels with no source; segregation rules with no source; separation breaches; reporting lines; forums; span and layer findings; result lines with no source; the structure scenario; crosswalk rows marked `retired`; time available; peak findings; walk notices; each element and the final status | Requesting Authority | undecided |
| H-12 | Inside a run: rule on contested `MATERIAL` findings; accept a reduced level within H-08; approve a second run; attest T0 to T8 | the PPD Design Lead | none taken; the step waits |
| H-13 | Create `<org>aioc-ppd-records` and `-records-restricted`, recorded first (Naming Standard R9) | the Cell carrying `[ORG]HOAC-TM` | before the first run |
| H-14 | Send the drafts of `upstream/` to 49GAION or to the parts they concern | GOV | after this blueprint is approved |
| H-15 | Approve this blueprint `v0.5.1` as the design of `[ORG]AIOC-PPD` | the human hub | it stays a draft; nothing is installed |
| H-16 | The connection with `[ORG]AIOC-DI` (release notices out; returns in, and their answers) (`connect-external-port`), its widening (`grant-or-widen-access`) and its revocation | the `[ORG]HOAC-ACS` position over this AIOC (the PPD Design Lead's) | none: no notice is sent and no return is received; this AIOC stands alone |
| H-17 | `return_round_deadline` and `return_rounds_max` (§15) | the Cell carrying `[ORG]HOAC-TM` | none: must be set; until set, every admitted return from DI goes straight to the Requesting Authority with two rows |
| H-18 | Each row on a return, both ways: for a return from DI (§5.11), open a new run, answer by decision, or set aside on a stated basis; for a return this AIOC sent to TOM, the same rows reach the Requesting Authority through TOM | Requesting Authority | undecided; past its deadline, escalated |
| H-19 | Classify each ended return from DI: a defect of this AIOC, or normal discovery (§5.11, rule 8) | the PPD Design Lead | none taken; the classification waits, shown on the Panel |

**Money:** the budget cap and the review budget (H-08). **People:** H-07 (decided); this AIOC designs positions, never who fills them. **Legal:** none decided here.

## 14. Change log

| Blueprint version | Date | Change | Template version | Commit |
|---|---|---|---|---|
| v0.1.0 | 2026-10-15 | First blueprint of `[ORG]AIOC-PPD`, the mother text of the Library part 49GAION Process and Position Design (Protocol §17, proposed): ten stages, processes first; the direct link to `[ORG]AIOC-TOM`, with returns; positions only; TEST-PPD v1 | v1.5.0 at `e89ed1d` | this commit |
| v0.2.0 | 2026-10-15 | The additions of `decisions/DR-0002`, from the study of fifteen rival products and the launch-readiness review: the facts of each step; risk, control and record per step, the controls catalogue and segregation of duties; competence profiles; the objectives cascade and measures of three kinds; forum tiers and the review calendar; structure scenarios; the peak-load check and end-to-end times; variants; modelling conventions; reference models as methods; approval and re-approval. Release parts A.11 to A.14; TEST-PPD v1, cases 78 to 94. Supersedes `v0.1.0` | v1.5.0 at `e89ed1d` | `65403ae` (pull request #2) |
| v0.3.0 | 2026-10-15 | Units in this stage (`decisions/DR-0003`): positions grouped into units, each with its head position and a charter generated by code; reporting lines follow the units unless decided otherwise; release part A.15; TEST-PPD v1, cases 95 to 97. Supersedes `v0.2.0` | v1.5.0 at `e89ed1d` | this pull request |
| v0.4.0 | 2026-10-16 | Connects the chain on both sides (`decisions/DR-0004`; `49GAION/DR-0016`, `DR-0017`, `DR-0018`): returns to TOM follow the Library's design return contract, pinned in `contracts/PINS.json`, count their rounds and always end, and an element of a return set aside goes forward on its stated basis, listed in the release (§5.1; Annex B.1); this AIOC's own `release-return` contract is superseded by the Library's; each decided PPD Release is announced to `[ORG]AIOC-DI` by a release notice (`contracts/release-notice.schema.json`); DI's returns are received and carried to an end (§5.11, new); slots `return_round_deadline` and `return_rounds_max`; H-16 to H-19; the mother is part card `v2`; the TOM rules are carried from the TOM blueprint `v0.5.0`. TEST-PPD v2: cases 98 to 104 and PDL-6, case 27 struck; the Library's v2 cases mapped (§9). Supersedes `v0.3.0` | v1.5.0 at `e89ed1d` | this pull request |
| v0.5.0 | 2026-10-16 | Reads what the TOM release now also states (`decisions/DR-0005`; TOM blueprint `v0.6.0`, Annex H); removes nothing. The release-reading record covers the strategy frame, journeys, value case and activity profile (§5.1 rule 2); critical value streams join the critical-process proposal and priority orders it (§5.3 rule 5); a capability delivered outside becomes a hand-off with oversight steps (§5.3 rule 8); journeys and maturity checked (§5.3 rules 9, 10); the objectives cascade starts from the strategy frame (§5.5 rule 11; A.12); today's activity profile beside the designed workload (§5.7 rule 7; A.9); priority carried into the release (§5.10 rule 9; A.2); Annex D items 20 and 21; Annex E pins TOM `v0.6.0`. TEST-PPD v3 (cases 105–111) | v1.5.0 | this pull request |
| v0.5.1 | 2026-10-19 | The Chief of Staff takes its COS code: `[ORG]CELL-PCS` → `[ORG]CELL-COSPPD` (Naming Standard R16, `49GAION/DR-0028`; `decisions/DR-0006`). The old code is retired and kept in the card's lineage; the part test is renamed; nothing else changes | v1.5.0 | this repository's pull request for this version |

---

## 15. Configuration

The template's slots, all `none: must be set` until the organisation sets them (Protocol §11), plus these slots of this AIOC:

| Slot | Card key | Default offered | Allowed values | Set by |
|---|---|---|---|---|
| Requesting Authority Cell | `requesting_authority_cell` | none: must be set | the Cell carrying `[ORG]HOAC-GOV`, or a human Cell it delegated the design decisions to | the Cell carrying `[ORG]HOAC-GOV` |
| Rows per needs pass | `rows_per_pass` | 12 | 1–12 | PPD Design Lead |
| Passes past their deadline before a non-response stop | `non_response_passes` | none: must be set | ≥ 1 | the Cell carrying `[ORG]HOAC-TM` |
| Engines per review point | `review_engines` | 3 | 3–5 | PPD Design Lead, within the review budget |
| Families per review | `review_families_min` | 2 | 2–3 | PPD Design Lead |
| Reduced review permitted | `reduced_review_permitted` | `no` | `yes`, `no` | the Cell carrying `[ORG]HOAC-TM` (never this AIOC's own `[ORG]HOAC-ACS` position) |
| Review budget per run | `review_budget_per_run` | none: must be set | within `budget_cap` | the Cell carrying `[ORG]HOAC-TM` |
| Span range | `span_range` | none: must be set | a lower and an upper bound | the Cell carrying `[ORG]HOAC-TM` |
| Most layers | `layers_max` | none: must be set | ≥ 1 | the Cell carrying `[ORG]HOAC-TM` |
| Return round deadline | `return_round_deadline` | none: must be set | a period | the Cell carrying `[ORG]HOAC-TM` |
| Most rounds of a return | `return_rounds_max` | none: must be set | ≥ 1 | the Cell carrying `[ORG]HOAC-TM` |
| Workload period | `workload_period` | none: must be set | a week, a month or a year | PPD Design Lead |
| Re-approval period | `re_approval_period` | none: must be set | a period, for example twelve months | the Cell carrying `[ORG]HOAC-TM` |
| Structure scenarios | `structure_scenarios` | 1 | 1–3 | the Cell carrying `[ORG]HOAC-TM` |
| Modelling conventions | `modelling_conventions` | the base set: §5.4 rules 1 to 5 and 11 as `error`; naming and layout rules as `warning` | the base set plus the organisation's own rules, each `error` or `warning`; the base set is never lowered | PPD Design Lead |
| Template slots | `office_accountable_human`, `central_head`, `discussion_limits`, `waiting_deadlines`, `bounce_limit`, `chain_depth` (at least 1), `halt_request_priority` (immediate), `budget_cap`, `unattended_action` (`read-record-triage`), and the `v1.6.0` rows | as the template | — | as the template |

---

## 16. Type

- **Type:** Specialised.
- **Why this AIOC exists:** an organisation needs its processes and positions designed from its decided operating model, traced to it and decided by its own authority.
- **Type-specific test:** TEST-PPD v3, case 76 · result `NOT_RUN`.

---

## 17. Cells and Pods

The parts inside this AIOC (`docs/CELLS-AND-PODS.md` of `49GAION-aioc`). The role and nature of this AIOC are read from the type of its top Cell, the PPD Design Lead. Every field that points to a human takes a position code only.

| Code | Kind | Type | Filler kind | HOAC label | Parent | Fixed test (owner) | External ports |
|---|---|---|---|---|---|---|---|
| `[ORG]CELL-PDL` | CELL | Human Seat | human | `[ORG]HOAC-ACS` | `[ORG]AIOC-PPD` | TEST-PPD-PDL v3 (the Cell carrying `[ORG]HOAC-TM`) | none |
| `[ORG]CELL-COSPPD` | CELL | AI Chief of Staff | ai | none | `[ORG]AIOC-PPD` | TEST-PPD-COSPPD v3 (`[ORG]CELL-PDL`) | `tom-in`, `tom-out`, `sl-in`, `sl-out`, `di-in`, `di-out` |
| `[ORG]POD-PRI` | POD | AI Pod | — | none | `[ORG]AIOC-PPD` | TEST-PPD-PRI v3 (`[ORG]CELL-PDL`) | — |
| `[ORG]CELL-PRR` | CELL | AI Agent | ai | none | `[ORG]POD-PRI` | TEST-PPD-PRR v3 (`[ORG]CELL-PDL`) | none |
| `[ORG]POD-PA` | POD | AI Pod | — | none | `[ORG]AIOC-PPD` | TEST-PPD-PA v3 (`[ORG]CELL-PDL`) | — |
| `[ORG]CELL-PPA` | CELL | AI Agent | ai | none | `[ORG]POD-PA` | TEST-PPD-PPA v3 (`[ORG]CELL-PDL`) | none |
| `[ORG]POD-PPW` | POD | AI Pod | — | none | `[ORG]AIOC-PPD` | TEST-PPD-PPW v3 (`[ORG]CELL-PDL`) | — |
| `[ORG]CELL-PFPA` | CELL | AI Agent | ai | none | `[ORG]POD-PPW` | TEST-PPD-PFPA v3 (`[ORG]CELL-PDL`) | none |
| `[ORG]CELL-PSPA` | CELL | AI Agent | ai | none | `[ORG]POD-PPW` | TEST-PPD-PSPA v3 (`[ORG]CELL-PDL`) | none |
| `[ORG]CELL-PPR` | CELL | AI Agent | ai | none | `[ORG]POD-PPW` | TEST-PPD-PPR v3 (`[ORG]CELL-PDL`) | none |
| `[ORG]POD-PPS` | POD | AI Pod | — | none | `[ORG]AIOC-PPD` | TEST-PPD-PPS v3 (`[ORG]CELL-PDL`) | — |
| `[ORG]CELL-PPB` | CELL | AI Agent | ai | none | `[ORG]POD-PPS` | TEST-PPD-PPB v3 (`[ORG]CELL-PDL`) | none |
| `[ORG]POD-PS` | POD | AI Pod | — | none | `[ORG]AIOC-PPD` | TEST-PPD-PS v3 (`[ORG]CELL-PDL`) | — |
| `[ORG]CELL-PSD` | CELL | AI Agent | ai | none | `[ORG]POD-PS` | TEST-PPD-PSD v3 (`[ORG]CELL-PDL`) | none |
| `[ORG]CELL-PWA` | CELL | AI Agent | ai | none | `[ORG]POD-PS` | TEST-PPD-PWA v3 (`[ORG]CELL-PDL`) | none |
| `[ORG]POD-PW` | POD | AI Pod | — | none | `[ORG]AIOC-PPD` | TEST-PPD-PW v3 (`[ORG]CELL-PDL`) | — |
| `[ORG]CELL-PSA` | CELL | AI Agent | ai | none | `[ORG]POD-PW` | TEST-PPD-PSA v3 (`[ORG]CELL-PDL`) | none |
| `[ORG]CELL-PSW` | CELL | AI Agent | ai | none | `[ORG]POD-PW` | TEST-PPD-PSW v3 (`[ORG]CELL-PDL`) | none |
| `[ORG]POD-PR` | POD | AI Pod | — | none | `[ORG]AIOC-PPD` | TEST-PPD-PR v3 (`[ORG]CELL-PDL`) | — |
| `[ORG]CELL-PBRA` … `[ORG]CELL-PBRE` | CELL | AI Agent | ai | none | `[ORG]POD-PR` | TEST-PPD-PBRA v3 … TEST-PPD-PBRE v3 (`[ORG]CELL-PDL`) | none |

**The card data (the blueprint governs).** `tools/make_cards.py` expands the block below into the complete unit cards and bot identity cards, writes them into `cards/`, and checks them against the schemas of `49GAION-protocol`, the code rules of its `tests/cards/check_cards.py`, Naming Standard R15 and R16, and this blueprint.

```yaml
parts:
  defaults:
    accountable_to: "[ORG]CELL-PDL"
    card_version: "v0.5.1"
    version: "0.3.0"
    lifecycle_state: "designed"
    test_version: "v3"
    test_owner: "[ORG]CELL-PDL"
    audit_trail: "the run record of [ORG]AIOC-PPD"
    hu_in: ["run control and configuration from the PPD Design Lead (never a source)"]
    hu_out: ["run report to the PPD Design Lead"]
  cells:
    - code: "[ORG]CELL-PDL"
      full_name: "PPD Design Lead"
      parent: "[ORG]AIOC-PPD"
      type: "Human Seat"
      filler_kind: "human"
      hoac: "[ORG]HOAC-ACS"
      accountable_to: "[ORG]CELL-TMS"       # example code of the Cell carrying [ORG]HOAC-TM
      entity: "<entity>"
      authority_scope:
        decision_types: ["change-fixed-test-or-threshold", "create-or-install-unit", "change-filler", "retire-unit", "restart-stopped-unit", "appoint-acting-filler"]
        entity: "<entity>"
        expires: "2027-10-15"                # placeholder; each organisation sets it
        authority: "delegated"
      test: { id: "TEST-PPD-PDL", cases: "PDL-1 to PDL-6", owner: "[ORG]CELL-TMS" }
      ai_in: ["run brief", "ruling sheets for contested MATERIAL findings", "release notice", "ended returns from DI to classify"]
      ai_out: ["run control and configuration"]
      hu_in: ["direction from the Cell carrying [ORG]HOAC-TM"]
      hu_out: ["rulings, attestations, reduced-level acceptances and the classification of ended returns, under live sign-in", "report to the Cell carrying [ORG]HOAC-TM"]
    - code: "[ORG]CELL-COSPPD"
      code_rule: "R16"                     # 49GAION/DR-0028; replaces [ORG]CELL-PCS (retired, R5)
      lineage: { id: "[ORG]CELL-PCS", version: "0.3.0", relation: "derived" }
      full_name: "PPD Chief of Staff"
      role: "Chief of Staff"
      parent: "[ORG]AIOC-PPD"
      type: "AI Chief of Staff"
      filler_kind: "ai"
      cell_kind: "chief-of-staff-cell"
      test: { id: "TEST-PPD-COSPPD", cases: "1-4, 8, 13, 18, 19, 21-26, 29-34, 48, 51, 62, 64-67, 73-75, 83, 84, 86, 87, 90, 92, 94, 96, 98-104" }
      ai_in: ["release notice", "return answer", "return", "source reference", "needs answer", "needs status", "needs candidate", "return draft", "locked outputs of the Pods", "settled review records"]
      ai_out: ["Input Pack version", "dispatch to a Pod", "review packet", "return", "needs request", "missing report", "generated parts", "PPD Release filing", "release notice", "return brief", "return answer"]
      hu_out: ["run brief to the PPD Design Lead", "ruling sheets to the PPD Design Lead", "release notice to the Requesting Authority's Cell"]
      external_ports:
        - { port: "tom-in", direction: "input", accepted_content: ["release notice", "return answer"], authority_limit: "the read scope signed under connect-external-port over [ORG]AIOC-TOM", audit_trail: "unit register connected and disconnected events; serve log of [ORG]AIOC-TOM" }
        - { port: "tom-out", direction: "output", accepted_content: ["return"], authority_limit: "returns only, under the scope signed over [ORG]AIOC-TOM", audit_trail: "unit register; the Work Item record" }
        - { port: "sl-in", direction: "input", accepted_content: ["source reference", "needs answer", "needs status"], authority_limit: "the read scope signed under connect-external-port over [ORG]AIOC-SL", audit_trail: "unit register; serve log of [ORG]AIOC-SL" }
        - { port: "sl-out", direction: "output", accepted_content: ["needs request", "missing report", "return filing", "PPD Release filing"], authority_limit: "the request and write scope signed over [ORG]AIOC-SL: this AIOC's own releases and design reports only", audit_trail: "unit register; serve log of [ORG]AIOC-SL" }
        - { port: "di-out", direction: "output", accepted_content: ["release notice", "return answer"], authority_limit: "notices and answers by reference only, under the scope signed under connect-external-port over this AIOC", audit_trail: "unit register; the Work Item record" }
        - { port: "di-in", direction: "input", accepted_content: ["return"], authority_limit: "returns only, under the scope signed under connect-external-port over this AIOC", audit_trail: "unit register; the Work Item record" }
      bot:
        allowed_actions: ["dispatch Cells of this AIOC", "build Input Pack versions through the code steps", "lock outputs and run code steps", "draw review engines and run the review code steps", "write the run record", "send reviewed returns to [ORG]AIOC-TOM and file them in [ORG]AIOC-SL", "send needs requests and Missing Reports to [ORG]AIOC-SL", "generate job descriptions, registers, charts and workload through the code steps", "file a release whose elements are decided", "send release notices to [ORG]AIOC-DI after filing", "admit or refuse a return from [ORG]AIOC-DI by the pinned contract and record it", "generate return briefs through the code step and send their rows to [ORG]AIOC-SL", "send return answers to [ORG]AIOC-DI"]
        ask_first_actions: ["a second run in parallel", "a budget above the cap", "a reduced review level", "any change to configuration", "anything outside its role card"]
    - { code: "[ORG]CELL-PRR", full_name: "PPD Release Reader", role: "Release Reader", parent: "[ORG]POD-PRI", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PRR", cases: "3, 5, 28, 30, 47" }, ai_in: ["Input Pack version", "the TOM release, role register first"], ai_out: ["release-reading record", "return draft"], bot: { allowed_actions: ["read and account for every element of the release", "draft returns with their evidence"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PPA", full_name: "PPD Process Architect", role: "Process Architect", parent: "[ORG]POD-PA", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PPA", cases: "9, 10, 35-37, 93" }, ai_in: ["release-reading record", "Input Pack version"], ai_out: ["process architecture draft", "critical-process proposal", "return draft", "needs candidate"], bot: { allowed_actions: ["draft the process architecture with its trace", "propose the critical processes and their order"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PFPA", full_name: "PPD First Process Author", role: "First Process Author", parent: "[ORG]POD-PPW", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PFPA", cases: "11, 16, 40-45, 78-82, 86, 91" }, ai_in: ["architecture entry", "release elements", "Input Pack atoms"], ai_out: ["process record draft", "return draft", "needs candidate"], bot: { allowed_actions: ["write a process record, blind to the other author"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PSPA", full_name: "PPD Second Process Author", role: "Second Process Author", parent: "[ORG]POD-PPW", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PSPA", cases: "11, 16, 39-45, 78-82, 86, 91" }, ai_in: ["architecture entry", "release elements", "Input Pack atoms"], ai_out: ["process record draft", "return draft", "needs candidate"], bot: { allowed_actions: ["write a process record, blind to the other author"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PPR", full_name: "PPD Process Reconciler", role: "Process Reconciler", parent: "[ORG]POD-PPW", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PPR", cases: "39, 41" }, ai_in: ["two locked drafts", "difference register", "the atoms and elements the drafts cite"], ai_out: ["reconciled process record", "the dispositions of the difference register"], bot: { allowed_actions: ["reconcile two locked drafts, disposing each difference with its reason"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PPB", full_name: "PPD Position Builder", role: "Position Builder", parent: "[ORG]POD-PPS", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PPB", cases: "12, 20, 46, 47, 52, 77, 85" }, ai_in: ["written processes", "role register"], ai_out: ["position register draft", "return draft"], bot: { allowed_actions: ["group steps and decisions into positions, with reasons"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PSD", full_name: "PPD Structure Designer", role: "Structure Designer", parent: "[ORG]POD-PS", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PSD", cases: "14, 53-56, 87, 88, 95, 97" }, ai_in: ["position register", "release parts and governance", "Input Pack atoms"], ai_out: ["unit register", "reporting lines", "forum register", "crosswalk"], bot: { allowed_actions: ["propose units, reporting lines and forums", "draft the crosswalk"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PWA", full_name: "PPD Workload Analyst", role: "Workload Analyst", parent: "[ORG]POD-PS", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PWA", cases: "15, 16, 57, 58, 89, 90" }, ai_in: ["written processes", "position register"], ai_out: ["workload input check", "needs candidate"], bot: { allowed_actions: ["check each workload input's source or assumption", "raise needs candidates for gaps"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PSA", full_name: "PPD Situation Author", role: "Situation Author", parent: "[ORG]POD-PW", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PSA", cases: "59" }, ai_in: ["blind brief"], ai_out: ["blind situation pack"], bot: { allowed_actions: ["write the blind situation pack"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PSW", full_name: "PPD Situation Walker", role: "Situation Walker", parent: "[ORG]POD-PW", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PSW", cases: "17, 60" }, ai_in: ["sealed situation set", "walk input"], ai_out: ["trace", "finding register"], bot: { allowed_actions: ["walk sealed situations", "classify findings"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PBRA", full_name: "PPD Blind Reviewer A", role: "Blind Reviewer A", parent: "[ORG]POD-PR", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PBRA", cases: "22, 61, 63" }, ai_in: ["review packet", "collated findings of its review"], ai_out: ["review card", "positions on findings"], bot: { allowed_actions: ["write its own review card", "state its own positions on the findings of its review"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PBRB", full_name: "PPD Blind Reviewer B", role: "Blind Reviewer B", parent: "[ORG]POD-PR", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PBRB", cases: "22, 61, 63" }, ai_in: ["review packet", "collated findings of its review"], ai_out: ["review card", "positions on findings"], bot: { allowed_actions: ["write its own review card", "state its own positions on the findings of its review"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PBRC", full_name: "PPD Blind Reviewer C", role: "Blind Reviewer C", parent: "[ORG]POD-PR", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PBRC", cases: "22, 61, 63" }, ai_in: ["review packet", "collated findings of its review"], ai_out: ["review card", "positions on findings"], bot: { allowed_actions: ["write its own review card", "state its own positions on the findings of its review"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PBRD", full_name: "PPD Blind Reviewer D", role: "Blind Reviewer D", parent: "[ORG]POD-PR", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PBRD", cases: "22, 61, 63" }, ai_in: ["review packet", "collated findings of its review"], ai_out: ["review card", "positions on findings"], bot: { allowed_actions: ["write its own review card", "state its own positions on the findings of its review"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PBRE", full_name: "PPD Blind Reviewer E", role: "Blind Reviewer E", parent: "[ORG]POD-PR", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PBRE", cases: "22, 61, 63" }, ai_in: ["review packet", "collated findings of its review"], ai_out: ["review card", "positions on findings"], bot: { allowed_actions: ["write its own review card", "state its own positions on the findings of its review"], ask_first_actions: ["anything outside its role card"] } }
  pods:
    - { code: "[ORG]POD-PRI", full_name: "PPD Release Intake", type: "AI Pod", inner_units: ["[ORG]CELL-PRR"], top_cell: "[ORG]CELL-PRR", test: { id: "TEST-PPD-PRI", cases: "3, 5-7, 28, 30, 47" }, ai_in: ["Input Pack version", "release notice"], ai_out: ["release-reading record", "return draft"] }
    - { code: "[ORG]POD-PA", full_name: "PPD Architecture", type: "AI Pod", inner_units: ["[ORG]CELL-PPA"], top_cell: "[ORG]CELL-PPA", test: { id: "TEST-PPD-PA", cases: "9, 10, 35-38, 93" }, ai_in: ["release-reading record"], ai_out: ["process architecture", "critical-process proposal"] }
    - { code: "[ORG]POD-PPW", full_name: "PPD Process Writing", type: "AI Pod", inner_units: ["[ORG]CELL-PFPA", "[ORG]CELL-PSPA", "[ORG]CELL-PPR"], top_cell: "[ORG]CELL-PFPA", test: { id: "TEST-PPD-PPW", cases: "11, 16, 39-45, 78-82, 86, 91" }, ai_in: ["decided architecture", "Input Pack atoms"], ai_out: ["process records"] }
    - { code: "[ORG]POD-PPS", full_name: "PPD Position Shaping", type: "AI Pod", inner_units: ["[ORG]CELL-PPB"], top_cell: "[ORG]CELL-PPB", test: { id: "TEST-PPD-PPS", cases: "12, 13, 20, 46-52, 77, 84, 85" }, ai_in: ["written processes", "role register"], ai_out: ["position register"] }
    - { code: "[ORG]POD-PS", full_name: "PPD Structure", type: "AI Pod", inner_units: ["[ORG]CELL-PSD", "[ORG]CELL-PWA"], top_cell: "[ORG]CELL-PSD", test: { id: "TEST-PPD-PS", cases: "14, 15, 53-58, 87-90, 95-97" }, ai_in: ["position register", "written processes"], ai_out: ["unit register", "reporting lines", "forum register", "crosswalk", "workload input check"] }
    - { code: "[ORG]POD-PW", full_name: "PPD Walkthrough", type: "AI Pod", inner_units: ["[ORG]CELL-PSA", "[ORG]CELL-PSW"], top_cell: "[ORG]CELL-PSW", test: { id: "TEST-PPD-PW", cases: "17, 59, 60" }, ai_in: ["walk input", "blind brief"], ai_out: ["walkthrough report"] }
    - { code: "[ORG]POD-PR", full_name: "PPD Review", type: "AI Pod", inner_units: ["[ORG]CELL-PBRA", "[ORG]CELL-PBRB", "[ORG]CELL-PBRC", "[ORG]CELL-PBRD", "[ORG]CELL-PBRE"], top_cell: "[ORG]CELL-PBRA", test: { id: "TEST-PPD-PR", cases: "22, 61-63" }, ai_in: ["review packet"], ai_out: ["review cards and positions"] }
```

- **Accountability.** Every Pod and Cell of this AIOC is `accountable_to` `[ORG]CELL-PDL`. The AIOC itself and the Design Lead are `accountable_to` the Cell carrying `[ORG]HOAC-TM`.
- **Adding a HOAC position.** The organisation may add HOAC positions to this AIOC in its own design, each a human Cell with a HOAC label and its own fixed test, through OCO (`create-or-install-unit`).
- **Bots.** Each AI Cell's bot (sixteen) has its own identity card, its own credential, `never_signs: true`, and its memory sealed on a change of filler (Protocol §10, item 3). The credential IDs in `cards/bots/` are placeholders.
- The Requesting Authority, the Chief of Staff of `[ORG]AIOC-SL` and the Cells of `[ORG]AIOC-TOM` are not Cells of this AIOC.

**Code checks** (Naming Standard R15, R16 and §5), recorded on 15 October 2026; the Chief of Staff's COS code on 19 October 2026. Each organisation repeats the check of §5.2 against its own register before first use.

| Code | Initials of the full name (R15) | §5.1 | §5.2: no match among this blueprint's codes, nor with `[ORG]AIOC-PPD` | §5.3 |
|---|---|---|---|---|
| `[ORG]CELL-PDL` | **P**PD **D**esign **L**ead | pass | pass | pass |
| `[ORG]CELL-COSPPD` | R16, item 2 (`49GAION/DR-0028`): COS and the initials of `[ORG]AIOC-PPD` → COSPPD. It replaces `[ORG]CELL-PCS`, retired at v0.5.1 (R5) and kept in the card's lineage | pass | pass (distinct from the COS codes of the other mothers: `COSSL`, `COSOER`, `COSPC`, `COSDI`, `COSTOM`, `COSCH`) | pass |
| `[ORG]POD-PRI` / `[ORG]CELL-PRR` | PPD Release Intake / PPD Release Reader | pass | pass | pass |
| `[ORG]POD-PA` / `[ORG]CELL-PPA` | PPD Architecture / PPD Process Architect | pass | pass | pass |
| `[ORG]POD-PPW` / `[ORG]CELL-PFPA`, `-PSPA`, `-PPR` | PPD Process Writing / First Process Author, Second Process Author, Process Reconciler | pass | pass | pass |
| `[ORG]POD-PPS` / `[ORG]CELL-PPB` | PPD Position Shaping / PPD Position Builder | pass | pass | pass |
| `[ORG]POD-PS` / `[ORG]CELL-PSD`, `-PWA` | PPD Structure / Structure Designer, Workload Analyst | pass | pass | pass |
| `[ORG]POD-PW` / `[ORG]CELL-PSA`, `-PSW` | PPD Walkthrough / Situation Author, Situation Walker | pass | pass | pass |
| `[ORG]POD-PR` / `[ORG]CELL-PBRA` to `-PBRE` | PPD Review / Blind Reviewer A to E | pass | pass | pass |

No code of this blueprint uses the suffix `PPD`, so no part can be read as the AIOC itself.

---
## Annex A. The PPD Release: its parts and their field lists

Every part is a versioned, content-addressed object. Every element carries an ID, its provenance (`stated`, `inferred`, `unresolved` or `assumed`, as in TOM Annex B, carried), its basis (release element IDs and source atom IDs, at least one) and, after T9, its decision reference. JSON Schemas are made from these lists before the first run and may add nothing.

**A.1 Release-reading record** (run record). One row per element of the release in scope: `element_id` (`ROLE-n`, `HO-n`, `CPR-n`, `JNY-n`, `VC-n`, a capability, a value-stream phase, a decision domain, an element of the strategy frame, or the activity profile), `part`, `child`, `state` (`used`, `returned`, `out of scope`), `used_by` (process IDs, after S2), `return_id` (when returned), `reason` (when out of scope).

**A.2 Process architecture** (release part). Per entry: `id` (`L1-n`, `L2-n` or `PRC-n`), `level` (1, 2, 3), `name`, `parent`, `traces_to` (release element IDs; at least one for level 1), `owner_role` (`ROLE-n`, level 3), `owner_position` (`POS-n`, level 3, after S5), `carries` (`HO-n` and `CPR-n`), `critical` (yes or no, with `reason`, among them `critical value stream`), `priority` (the highest decided priority of the release elements it carries), `delivery` (the delivery model of the capability it serves: `in-house`, `shared service`, `outsourced`, `partner` or `not decided`), `order`, `current` (the current processes from the sources it replaces, for the crosswalk).

**A.3 Process record** (one per process; release part "process book"). `process_id`; `purpose`; `trigger`; `end`; `lanes` (roles); `steps[]`: {`step_id`, `lane`, `action`, `input`, `output`, `accountable_role`, `decision_id` (or none), `volume` {value, unit, per, basis, `peak` {value, period, basis} or none}, `step_time` {value, unit, basis}, `wait_before` {value, unit, basis}, `done_when`, `worst_error` {description, `reversible` (`yes`, `partly`, `no`), basis}, `act_kinds` (from the fixed list of §5.4, rule 11), `input_source` {kind, `trust` (`verified`, `unverified`), basis}, `confidentiality` (a class of the organisation's classification), `risks` (risk IDs), `controls` (control IDs), `record` {name, basis}}; `decisions[]`: {`decision_id`, `question`, `decides` (one role), `recommends`, `must_agree`, `gives_input`, `carries_out`, `limit` {value, basis}}; `exceptions[]`: {`trigger`, `handling`, `escalates_to` (role)}; `risks[]`: {`risk_id`, `what`, `at_steps`, basis}; `measures[]`: {`name`, `kind` (`quality`, `time`, `cost`, `volume`), `definition`, `unit`, `basis`, `target` (a decision reference, or `not set`), `reviewed_by` (forum ID, after S6)}; `variants[]`: {`variant_id`, `applies_to` (an entity, a site or a product), `differs_at` (step IDs), `reason`}; `end_to_end_time` {value, unit, path (step IDs), complete}; `conventions` (the modelling conventions in force and their results); `method_refs` (reference models used as methods, never as evidence); `policies[]` (policy IDs); `hand_offs` (`HO-n`, `CPR-n`, and the lane hand-offs inside the process); `authors` (one, or two with the difference register's ID); after T9: `owner_position`, `approved_by` (decision reference), `re_approval_due`.

**A.4 Policy register** (release part; compiled by code). Per policy: `policy_id`, `name`, `applied_at` (step IDs), `owner_role`, `basis` (source atom), `state` (`held`, or `needed` when no source holds it). No policy text.

**A.5 Position register** (release part). Per position: `position_id` (`POS-n`), `title`, `role` (one `ROLE-n`), `part` and `child`, `holds_steps`, `holds_decisions`, `grouping_reason` (same expertise, same counterpart, same location, same decision chain, or the release's own grouping), `job_family` and `level` (each with its basis, or `not given`), `reports_to` (`POS-n`, after S6), `forums` (after S6). Never: a person, a pay amount, or what fills the position.

**A.6 Job descriptions** (release part; generated by code, one per position). `position_id`; `title`; `job_family` and `level` (as in A.5); `purpose` (from its processes' purposes); `accountabilities` (from its steps); `decisions` (with their limits); `works_with` (positions at its lane hand-offs); `measures` (from its processes' measures for its steps); `competences` (each a knowledge or skill, with the steps and decisions it serves); `reports_to`; `trace` (every line to a step or decision). The release lint fails any field that does not trace.

**A.7 Decision-rights register and authority matrix** (release parts; generated by code). Register: one row per decision: `decision_id`, `process_id`, `decider` (`POS-n`), the other parts by position, `limit`, `basis`. Matrix: positions by decision class, each cell the part the position plays, generated from the register.

**A.8 Structure** (release parts). **Reporting lines**: `position_id`, `reports_to`. **Organisation charts**: generated from the units and the lines, one per part of the release. **Span and layer report**: per manager position, its span; per part, its layers; each value against the configured range, with findings. **Forum register**: per forum, `forum_id`, `purpose`, `decides` and `advises` (decision IDs), `members` and `chair` (`POS-n`), `tier`, `cadence`, `reviews` (measure names), `inputs`, `outputs`. **Review calendar** (generated): per forum and period, the measures it reviews. **Result lines**: per part, `result_line`, with its basis. **Crosswalk**: per current unit, position or process named in the sources: `current_ref` (source atom), `maps_to` (target IDs), or `state` `retired` or `not mapped`, with `reason`.

**A.9 Workload register** (release part; generated by code). Per position: `position_id`, `period`, `time_needed` (sum of volume × step time over its steps), `time_available` (with its basis), `steps` (the terms of the sum), `complete` (no when any term is a gap), `gaps`. Per process (**New** in v0.5.0): `today` (the activity-profile lines of the processes it replaces, with their atoms and date, or `no observation`) beside its designed volume and time.

**A.10 Decision Package** (release part). A plain summary; the elements for decision, each with its row; the unknowns, the assumptions and the open returns, in plain words; the control gaps and the separation breaches; the span and layer findings; the structure scenarios side by side, when there are any; the peak findings; the walk's findings and their choices; the quality checks.

**A.11 Controls catalogue and segregation-of-duties rules** (release part; compiled by code). Per control: `control_id`, `objective` (the risk IDs it answers), `kind` (`preventive`, `detective`), `at_steps`, `performed_by` (`POS-n`, after S5), `evidence` (the record it leaves), `frequency`, `basis`. Per rule: `rule_id`, `conflict` (two classes of step or decision one position may not hold together, for example start and approve, keep and record, record and reconcile), `basis` (a source or a decision). Check, after S5: per position, each rule it breaks, with any compensating control and the decision reference.

**A.12 Objectives cascade** (release part; generated by code). Per goal: `goal` (a one-year goal or a critical number of the release's strategy frame, by its reference; for a release with no strategy frame, a goal a source gives), `value_stream_measures`, `process_measures`, `position_measures` (by `POS-n`), each link traced. Findings: a goal with nothing under it; a measure that serves no goal.

**A.13 Structure scenarios** (release part, when `structure_scenarios` is above one). Per scenario: `scenario_id`, its reporting lines, and side by side: positions, management positions, spans, layers, `cost` (`not given` without the organisation's cost rates); `chosen` (the decision reference of the one chosen).

**A.14 Peak-load check and value-stream times** (release part; generated by code). Per position: `peak_period`, `time_needed_at_peak`, `time_available`, `terms`, `complete`, findings. Per value stream: `end_to_end_time`, `processes`, `complete`.

**A.15 Unit register and unit charters** (release parts; charters generated by code). Per unit: `unit_id` (`UNIT-n`), `name`, `kind` (the organisation's own word: team, section, department), `part` (the release part), `parent_unit`, `head_position` (`POS-n`, one of its positions), `positions`, `grouping_reason`, `forums`, `measures`, `result_line`. Charter, one per unit: `mandate` (its processes and decisions, from its positions' steps and decisions), `head_position`, `positions`, `works_with` (units at its hand-offs), `forums`, `measures`, `result_line`, `trace` (every line to a step, decision or forum). Never a person.

**The manifest.** `release_id` (`PPDREL-` + SHA-256 of the manifest body); `run_id`; `tom_release` {`release_id`, `manifest_sha256`}; `parts[]` {name, sha256}; `input_packs[]`; `returns[]` (return IDs with their states, both ways); `set_aside[]` (per element carried forward on a set-aside return: `return_id`, `element_id`, `carried_forward_on`, `decision`); `decided_at`; `final_status`.

## Annex B. Returns, both ways

Returns follow the Library's design return contract, `library/contracts/design-return.schema.json` of `49GAION-protocol` (Standard §3.1, item 6; Protocol §17, item 11; `49GAION/DR-0018`), pinned by commit and hash in `contracts/PINS.json`. This AIOC keeps no copy of it. *(v0.4.0: supersedes this AIOC's own `contracts/release-return.schema.json` v0.1, which had no rounds and no set-aside end.)*

| Field | Meaning here |
|---|---|
| `return_id` | `PPDR-` and a number, for a return this AIOC sends; the sender's prefix for a return it receives (`DIR-` from DI) |
| `run_id` | the sending stage's run |
| `release` | the release ID and its manifest hash: a TOM Release for `PPDR`; a PPD Release (`PPDREL-`) for `DIR` |
| `kind` | `accepted`, `cannot use`, `contradiction found`, `assumption invalid`, `request kind unsupported` |
| `missing` | for `cannot use`: what is missing, as a fact-type or an element, never a person |
| `elements` | the release parts and element IDs the return concerns; for `accepted`, the whole release |
| `evidence` | release element IDs and source atom IDs, with span hashes; never text |
| `held_here` | the sender's elements held until the return ends |
| `round` | the round of the loop; each answer that does not end the return opens the next |
| `filed_ref` | the reference of its filed copy in `[ORG]AIOC-SL` |
| `status` | `open`, `answered by release`, `answered by decision`, `set aside by decision`, `withdrawn` |
| `answered_by` | the answering release ID, or the decision reference |
| `carried_forward_on` | for `set aside by decision`: `known defect` or `decided assumption` |

**B.1 Returns this AIOC sends to `[ORG]AIOC-TOM`.**
1. A return goes to `[ORG]AIOC-TOM` directly, through the gateway, and its copy is filed into Source Lifecycle as a design report with the same hash.
2. A return never changes the release. It asks TOM to answer.
3. TOM answers with a new decided release (a continuation run), or the Requesting Authority answers by decision. If a new release still does not answer it, the same return is sent again, under the same `return_id`, in its next round. TOM counts the rounds, holds the deadlines and escalates (TOM blueprint `v0.5.0`, §5.10). Silence answers nothing.
4. When the whole release is used without defect, the run sends one `accepted` return; TOM ends it at once.
5. **Set aside.** A return set aside by the Requesting Authority's decision lets its touched elements go forward on the stated basis. Each is marked in this AIOC's work and in the PPD Release as a `known defect` or a `decided assumption`, with the decision reference; it is listed in the Decision Package in plain words and in the manifest (`set_aside[]`).
6. A return for something TOM should have obtained is a defect of TOM; a return for something only this stage could find is normal (TOM blueprint `v0.5.0`, `docs/CARRIED-RULES.md` §4.4, items 2 and 3). TOM's Design Lead classifies it.

**B.2 Returns this AIOC receives from `[ORG]AIOC-DI`.** Under the same contract, ended by §5.11. A defect DI finds in the TOM Release that a PPD Release rests on is DI's to return to TOM (§5.11, rule 7).

**Done when.** Each return validates against the pinned contract; it is sent and filed with one hash; its touched elements show `held: return open` until it ends; it ends in a status other than `open`.

## Annex C. Run states and gates

**C.1 Run states.** As §5.0. Endings other than a release: `closed: not admitted` (T0 failed, with each failed condition named); `closed: non-response`; `closed: rejected`; `closed: withdrawn by the Requesting Authority`. Flags on any state, each with its age: `waiting`; `waiting: ruling`; `held: return open` (on the touched elements only); `held: material finding`; `held: connection revoked`; `held: no reviewers`; `held: review budget`. No flag releases the run slot; every ending releases it. A return from DI is not a run state: it lives on its own Work Item, with the states of the contract (§5.11), and holds no run.

**C.2 The gates.** T0 to T10 as in §5.0. A gate passes only on its settled review (§5.9) and its done-test. T0 has these conditions: (a) the run request carries references only; (b) the release check passes (§4.3, part 3); (c) the TOM connection is signed and in scope; (d) the Source Lifecycle connection is signed and in scope; (e) the engine register holds eligible engines for the highest confidentiality level in scope, and two author families; (f) `requesting_authority_cell` is set; (g) RP0 is settled.

## Annex D. What this AIOC never does

1. Change, merge, split or drop an element of the TOM release.
2. Ask any person anything about the organisation, or send a request that names a person.
3. Name a person, or read who occupies a position.
4. Say what fills a position.
5. Set pay.
6. Write the text of a policy.
7. Invent a measure, a volume, a time or a limit.
8. Write a job description by hand.
9. Add a role that the role register does not hold.
10. Change a reporting line, span or layer to fit a range.
11. Decide anything for the organisation, or take silence as a decision.
12. Grade its own work: no Cell reviews its own output, and the Chief of Staff rules on nothing.
13. Set or propose a cost rate, or choose a structure scenario.
14. Use a reference model, a taxonomy or a measure library as evidence.
15. Claim that the organisation complies with a law or a standard.
16. Edit a filed PPD Release in answer to a return; decide, answer or classify a return in the Chief of Staff; or write a return brief by hand.
17. Leave a return, either way, without its round and its deadline, count silence as its answer, or let it end other than in one of the contract's four ends.
18. Carry an element forward on a set-aside return without marking its basis in the release.
19. Send a release notice before the filing reads back, or put release text into a notice.
20. Fill what the release states as `not given`, `not decided`, `not set`, `unknown` or `no observation`; or write a goal of its own (TOM Annex H).
21. Design an in-house process for work the release delivers outside, or use today's activity profile to say anything about a person.

## Annex E. What is carried from the Target Operating Model blueprint

This AIOC carries these rules from the blueprint of `[ORG]AIOC-TOM` `v0.6.0` (its writing repository, `<org>aioc-tom`), by section, not by copy. A change there reaches this AIOC only when this annex pins the new version.

| Rule | TOM section | Read here with |
|---|---|---|
| Labels and the honesty ceiling | Annex B | atoms of the organisation's sources; release elements keep their own provenance |
| Patterns are methods, never evidence | Annex B.5 | — |
| The Input Pack, its versions and its trace | §4.3, parts 1 to 3 and 6 to 8 | §4.3 of this blueprint |
| Needs requests, passes and the Missing Report | §5.2 | §5.2 of this blueprint |
| Decision rules: one decision per row; global assent is never approval; "don't know"; the weak-approval signal; delegated, not decided | `docs/CARRIED-RULES.md` §5 | — |
| The return vocabulary | `docs/CARRIED-RULES.md` §4.4 | Annex B of this blueprint |
| The receiving end of returns: admission, the brief made by code, rounds, escalation, ends, classification | §5.10; Annex E.21 and E.22 | §5.11 of this blueprint; "PPD Design Lead" for "TOM Design Lead"; "PPD Release" for "release" |
| The release notice | §5.9 step 8a; Annex E.20 | `contracts/release-notice.schema.json` of this AIOC, with the TOM Release it rests on |
| The operational walkthrough | §5.7 | "processes, positions and decisions" for "operating model" |
| The Review Panel rule | §5.8, rules 1 to 20 | the review points of §5.9 of this blueprint; "PPD Design Lead" for "TOM Design Lead" |
| Two authors | Annex G | "process" for "child"; "process record" for "design ledger" |
| The engine register | Annex E.12 | — |
| What the release also states: the strategy frame, delivery model and maturity, critical streams, journeys, value case, priority, activity profile; the values `not given`, `not decided`, `not set`, `unknown`, `no observation` | Annex H | §5.1 rule 2; §5.3 rules 5, 8 to 10; §5.5 rule 11; §5.7 rule 7; §5.10 rule 9 of this blueprint |

*Powered by 49GAION*
