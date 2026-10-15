```yaml
# ── Blueprint metadata (machine-readable; the panel generator and the back-office builder read this block) ──
blueprint:
  aioc: "[ORG]AIOC-PPD"
  parent: "[ORG]AIOC-CH"                  # example code of the Charter; each organisation writes its own Charter's code (Standard §1.7, item 13)
  full_name: "Process and Position Design"
  organisation: "<organisation>"          # filled in each organisation's own copy
  type: "specialised"
  org_aion: "[ORG]AION"
  blueprint_version: "v0.1.0"
  status: "draft"
  template:
    name: "49GAION AIOC Blueprint Template"
    version: "v1.5.0, with the unreleased v1.6.0 additions on main"
    source: "github.com/49g-holding/49GAION-aioc, template/AIOC-BLUEPRINT-TEMPLATE.md @ e89ed1d"
  mother:
    name: "49GAION Process and Position Design"
    version: "part card v1 (DRAFT), proposed"
    source: "github.com/49g-holding/49GAION-protocol, library/cards/process-and-position-design.part-card.json and Protocol §17 (pull request #33); Standard §3.1, item 3 (49GAION pull request #66, DR-0014)"
  writing_repository: "<org>aioc-ppd"
  code_project: "<org>aioc-ppd, on the organisation's code platform"
  panel_register_id: "none yet"
  capabilities:
    standard: ["Chief of Staff", "Office", "Input socket", "Panel"]
    functional: ["Release Intake and Returns", "Needs Requests", "Process Architecture", "Process Writing", "Position Shaping", "Structure", "Workload", "Operational Walkthrough", "Independent Review", "Decision Package and Release"]
```

# Blueprint · `[ORG]AIOC-PPD` · Process and Position Design · `v0.1.0`

**Draft, 15 October 2026.** Written by `[ORG]AIOC-OCO` on the directions recorded in `decisions/DR-0001`. This is the first blueprint of Process and Position Design, written for any organisation as the mother text of the Library part 49GAION Process and Position Design (Protocol §17, proposed). Every rule rests on a 49GAION text, on the blueprint of `[ORG]AIOC-TOM` (cited by section and version), or is new here and marked **New**. Nothing here has run. Every fixed test reads `NOT_RUN`.

> **Process and Position Design in one page**
>
> Process and Position Design (PPD) takes an organisation's decided target operating model and designs how its work runs and the positions that carry it. It is the stage after the Target Operating Model (TOM), and a part of its own.
>
> **What goes in**
> 1. The decided TOM release, handed over directly by `[ORG]AIOC-TOM`, by reference and hash. PPD reads its role register first, then its value streams, capabilities, decision domains and hand-offs.
> 2. The organisation's other sources, only from Source Lifecycle: the processes, procedures, policies, volumes and times it already has.
> 3. Answers to what the release and the sources do not say. PPD never asks a person. It asks the Chief of Staff of Source Lifecycle, who gets the answer approved and recorded.
>
> **The link with TOM goes both ways.** PPD never changes the TOM release. When it finds a defect, it sends a return straight back to TOM, naming the part and the reason: cannot use, missing what; contradiction found; assumption invalid; request kind unsupported. The elements the return touches wait; the rest of the work goes on. TOM answers with a new decided release, and the two go back and forth until the release holds.
>
> **What PPD does, in ten stages, processes first**
> 1. Admit: check the request, the release and the connections.
> 2. Read the release: account for every role, phase, capability, decision domain and hand-off, or return it.
> 3. Architecture: the processes under each part of the model, in three levels, each with one owner.
> 4. Critical processes: choose the processes that cross parts, and design them first.
> 5. Write each process: purpose, trigger, steps in role lanes, what goes in and out of each step, the decision at each step and who decides it, exceptions and escalation, measures, volumes and step times. Each step also says when it is done, its worst error and whether it can be undone, what kind of act it is, where its input comes from and how far it is trusted, how confidential it is, and its risk, control and record.
> 6. Shape the positions: group the steps and decisions of each role into positions, and generate each job description from what the position holds. No job description is written by hand.
> 7. Structure: reporting lines, spans and layers, standing forums with charters, and the crosswalk from the organisation as it is today.
> 8. Workload: the work each position carries, from the volumes and step times of its processes.
> 9. Walk: test the design against realistic situations.
> 10. Decide and release: the organisation decides each element; the release is frozen, filed in Source Lifecycle, and handed to the next stage.
>
> Each stage has one input, one output and one test that says when it is done. Critical processes are written twice, separately, by two authors of two engine families. Every stage is checked by three or more other engines before the next starts. A person, the PPD Design Lead, rules on what they still dispute.
>
> **What comes out: the PPD Release**
> - the process architecture and the process book;
> - the decision-rights register and the authority matrix;
> - the policy register;
> - the controls catalogue and the segregation-of-duties check;
> - the position register, with a job description and a competence profile for every position;
> - the objectives cascade, from the decided goals down to each position's measures;
> - organisation charts, standing forums with their charters and tiers, and the review calendar;
> - structure scenarios side by side, when the organisation asks for them;
> - the workload of each position, its peak-load check, and the end-to-end time of each process and value stream;
> - the crosswalk from today's organisation;
> - the walkthrough report and the quality checks;
> - the Decision Package.
>
> **Who decides.** The organisation's Requesting Authority decides each element: accept, correct or reject. Silence decides nothing. PPD designs positions only (Standard §1.1, item 9). It makes no choice of what fills a position; that belongs to a later stage.

**Where this blueprint stands.** First draft. The stages, their inputs, outputs and done-tests are set (§5.0). The engine rules it shares with `[ORG]AIOC-TOM` (the Review Panel rule, two authors, labels, decision rules) are carried from the TOM blueprint `v0.4.1` by section, not copied (§5.9; Annex E). The decisions only a human seat can take are listed once, in §13.

---

## 0. Identity and lineage

| Field | Value |
|---|---|
| Code | `[ORG]AIOC-PPD`. Collision check (Naming Standard §5 and R6): the initials do not recreate `AIOC`, `AION` or `49GAION`, and do not read as a version suffix. The code is the one Protocol §17 gives the Library part in an `[ORG]AION`. Each organisation records it in its register before the repository is created (Naming Standard R9) |
| Full name | Process and Position Design |
| Description | "`[ORG]AIOC-PPD` is `<organisation>`'s Process and Position Design core, built from 49GAION Process and Position Design" |
| Kind | AIOC |
| Parent | `<code of the Charter of this [ORG]AION>`; the cards use the example code `[ORG]AIOC-CH`. A top-level AIOC (Standard §1.7, item 13). A change of parent is the listed type `change-parent` |
| Inner units | `[ORG]CELL-PDL`, `[ORG]CELL-PCS`, `[ORG]POD-PRI`, `[ORG]POD-PA`, `[ORG]POD-PPW`, `[ORG]POD-PPS`, `[ORG]POD-PS`, `[ORG]POD-PW`, `[ORG]POD-PR`: seven Pods with their fifteen Cells, and two Cells directly under the AIOC (§17). No inner AIOC |
| HOAC label | `[ORG]HOAC-ACS`, held by its top Cell, the PPD Design Lead `[ORG]CELL-PDL` (`label_holder`) |
| Accountable to | `<code of the Cell carrying [ORG]HOAC-TM>`; the cards use the example code `[ORG]CELL-TMS` (Naming Standard R15). That Cell signs this AIOC's install, its `change-parent` and its `restart-stopped-unit` (Standard §5.3, item 4; §4.4, item 3) |
| Type | Specialised: the organisation needs its processes and positions designed from its decided operating model (§16) |
| `[ORG]AION` | `[ORG]AION`, based on 49GAION Standard `v1.5.0`, with the unreleased `v1.6.0` texts on main |
| Versioned Definition | this file; the Panel and the Back office are built from it |
| Organisation | `<organisation>` |
| Made from | the Library part 49GAION Process and Position Design, part card `v1` (DRAFT), and Protocol §17, both proposed on 15 October 2026 (`decisions/DR-0001`) |
| Template | 49GAION AIOC Blueprint Template `v1.5.0` at `e89ed1d` (with the `v1.6.0` additions: mechanism register and Reserve, checks that are not fixed tests, the added Configuration rows, position codes only) |
| Mother | 49GAION Process and Position Design, part card `v1`. This text is its mother blueprint |
| Blueprint version and status | `v0.1.0` · draft |
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
  inner_units: ["[ORG]CELL-PDL", "[ORG]CELL-PCS", "[ORG]POD-PRI", "[ORG]POD-PA", "[ORG]POD-PPW", "[ORG]POD-PPS", "[ORG]POD-PS", "[ORG]POD-PW", "[ORG]POD-PR"]
  type: "specialised"
  org_aion: "[ORG]AION"
  card_version: "v0.1.0"
  input_door: "Chief of Staff"
  wake: { method: "queue", verified: false }
  receives:
    - kind: "run request"                 # a Work Item from the Requesting Authority's Cell, through the HU input port; references only
      format: "Work Item (Protocol §4.1) whose sources field holds one TOM Release reference and, optionally, the children in scope"
      acceptance_test: "TEST-PPD v1, cases 1, 23"
      decision_needed: false
    - kind: "release notice"              # from [ORG]AIOC-TOM, directly, through the tool gateway
      format: "release notice (contracts/README.md, release notice): TOM Release ID, manifest hash, the reference of its filed copy in [ORG]AIOC-SL"
      acceptance_test: "TEST-PPD v1, cases 2, 3, 24, 25"
      decision_needed: false
    - kind: "source reference"            # the organisation's other sources, from the output socket of [ORG]AIOC-SL
      format: "source reference (ID + version + hash; held or not held)"
      acceptance_test: "TEST-PPD v1, cases 4, 30"
      decision_needed: false
    - kind: "needs answer"                # the output of a needs request sub-item
      format: "needs answer, by reference only"
      acceptance_test: "TEST-PPD v1, cases 8, 33"
      decision_needed: false
    - kind: "needs status"                # accepted, returned or asked, from [ORG]AIOC-SL
      format: "needs status"
      acceptance_test: "TEST-PPD v1, case 31"
      decision_needed: false
  delivers:
    - kind: "return"                      # to [ORG]AIOC-TOM, directly; also filed into [ORG]AIOC-SL as a design report
      format: "release return (contracts/release-return.schema.json)"
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
    - kind: "release notice"              # to the next stage, by reference
      format: "release notice: PPD Release ID, manifest hash, the reference of its filed copy"
      usual_receivers: ["the next design stage"]
  anatomy:
    panel: { health: { tests: true, metrics: ["stuck", "returned", "late", "run state", "returns open", "returns answered", "needs open", "needs past deadline", "processes by state", "positions by state", "assumptions open", "reviews held", "review budget used"] } }
    back_office: { converses_with_humans: false, hosts: ["Chief of Staff", "Office"], protocol_traffic: true }
    definition: { location: "<org>aioc-ppd, blueprint/PPD-BLUEPRINT.md", version: "v0.1.0" }
    delivery: { rollback: "one-click" }
    connectors:
      - { role: "operating model source", connector: "[ORG]AIOC-TOM release port", access_managed_in: "panel" }   # the grant is signed at the tool gateway as connect-external-port (Protocol §17, item 8)
      - { role: "source of record", connector: "[ORG]AIOC-SL output socket", access_managed_in: "panel" }      # as above (Protocol §13, item 5)
    gateway: { metering_id: "<per-AIOC metering id>" }
  full_name: "Process and Position Design"
  version: "0.1.0"
  lineage: { id: "[ORG]AIOC-PPD", version: "0.1.0", relation: "original" }
  lifecycle_state: "designed"
  blueprint_version: "v0.1.0"
  template_version: "v1.5.0"
  accountable_to: "[ORG]CELL-TMS"         # example code of the Cell carrying [ORG]HOAC-TM (Naming Standard R15); never a Cell inside this AIOC
  top_cell: "[ORG]CELL-PDL"
  hoac: "[ORG]HOAC-ACS"
  label_holder: "[ORG]CELL-PDL"
  fixed_test: { id: "TEST-PPD", version: "v1", owner: "[ORG]CELL-TMS" }
  skills:
    - { id: "ppd-release-intake", name: "Reading a decided operating model, and returning its defects", tags: ["design", "intake"] }
    - { id: "ppd-process-design", name: "Process architecture and process design", tags: ["design"] }
    - { id: "ppd-position-design", name: "Positions and generated job descriptions", tags: ["design"] }
    - { id: "ppd-structure", name: "Reporting lines, forums and crosswalk", tags: ["design"] }
    - { id: "ppd-walkthrough", name: "Operational walkthrough of processes and positions", tags: ["assurance"] }
  ports:
    - { unit: "[ORG]AIOC-PPD", port: "ai-in", direction: "input", type: "AI", identification: "technical-key", accepted_content: ["release notice", "source reference", "needs answer", "needs status"], authority_limit: "read only, within the scopes signed for the TOM and Source Lifecycle connections", audit_trail: "unit register; the serve logs of [ORG]AIOC-TOM and [ORG]AIOC-SL", required_tests: ["TEST-PPD v1"], enforcement: "shared-gateway-outside-unit" }
    - { unit: "[ORG]AIOC-PPD", port: "ai-out", direction: "output", type: "AI", identification: "technical-key", accepted_content: ["return", "needs request", "missing report", "needs status", "PPD Release filing", "release notice"], authority_limit: "returns, requests, reports and filings only; files only its own releases and design reports; never an instruction to a person", audit_trail: "Work Item record and the unit register", required_tests: ["TEST-PPD v1"], enforcement: "shared-gateway-outside-unit" }
    - { unit: "[ORG]AIOC-PPD", port: "hu-in", direction: "input", type: "HU", identification: "live-human-sign-in-at-gateway", accepted_content: ["run request from the Requesting Authority's Cell (references only)", "run control and configuration from the PPD Design Lead (never a source)"], authority_limit: "the signer's authority_scope; nothing received here is a source", audit_trail: "Office record", required_tests: ["TEST-PPD v1"], enforcement: "shared-gateway-outside-unit" }
    - { unit: "[ORG]AIOC-PPD", port: "hu-out", direction: "output", type: "HU", identification: "live-human-sign-in-at-gateway", accepted_content: ["run brief to the PPD Design Lead", "ruling sheets to the PPD Design Lead", "release notice to the Requesting Authority's Cell"], authority_limit: "information only; never a question about the organisation", audit_trail: "Office record", required_tests: ["TEST-PPD v1"], enforcement: "shared-gateway-outside-unit" }
    - { unit: "[ORG]AIOC-PPD", port: "stop", direction: "input", type: "HU", identification: "live-human-sign-in-at-gateway", accepted_content: ["stop"], authority_limit: "stop only", audit_trail: "unit register", required_tests: ["TEST-PPD v1"], enforcement: "shared-gateway-outside-unit", stop_door: true }
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
```

**Joining the protocol.** This AIOC joins only after every input and output on this card passes fixed samples (the joining test, Protocol §11, item 1; Standard §3.2, item 4). It also needs `[ORG]AIOC-TOM` to send release notices and accept returns (the TOM changes in `upstream/PROPOSALS.md`, item 1), and Source Lifecycle to accept filings of origin kind `process and position design`. Until then its `lifecycle_state` stays `designed` and no Work Item is routed to it. The cards of its Pods and Cells are set in §17 and generated into `cards/`.

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
| The Library blueprint this core is made from | 49GAION Process and Position Design, part card `v1` (proposed); Protocol §17 (proposed) |
| **The Requesting Authority**: the position that asks for the design and decides it | `<code of the human Cell carrying [ORG]HOAC-GOV>`, or of a human Cell carrying a HOAC label whose `authority_scope`, delegated by that Cell under `delegate-authority`, covers the design decisions of this AIOC (Standard §4.2, items 5 and 8; §4.4, item 8). It is a position, never this AIOC's Design Lead position |
| **The PPD Design Lead position** | a HOAC position (`[ORG]HOAC-ACS`), a legal persona. Who occupies it is top management's own mechanism; this AIOC never sees it |
| **The operating model source** | `[ORG]AIOC-TOM`: it hands over its decided release directly, and receives this AIOC's returns |
| **The source of record** | `[ORG]AIOC-SL`: every other source, every question to the organisation, and every filing |
| **The engine register** | held at the tool gateway, in the Charter (Standard §4.4, item 11); read by this AIOC as `[ORG]AIOC-TOM` reads it (TOM blueprint `v0.4.1`, Annex E.12) |

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
  - **The next design stage** receives the PPD Release by reference and returns its defects to this AIOC in the same way.
  - **`[ORG]AIOC-OCO`** installs, fixes and upgrades this AIOC; it never grades it (Standard §2.3, item 9).
- **Overlap.** None known. Where an organisation already holds process maps or job descriptions, they are sources, read through Source Lifecycle and mapped in the crosswalk (§5.6).

---

## 3. Positions

| Position (standard title) | Purpose | Reports to | Run today by | Deputy |
|---|---|---|---|---|
| PPD Design Lead | the accountable position of this AIOC and the owner of its path: owns the fixed tests of its parts; rules on contested review findings; accepts a reduced review level within the TM Cell's permission; attests the method. Answers for the method, never for the organisation's choices | the Cell carrying `[ORG]HOAC-TM` | a HOAC position (`[ORG]HOAC-ACS`); who occupies it is top management's own mechanism, never seen by this AIOC | as top management arranges (`appoint-acting-filler`, Standard §4.1, item 12) |
| Chief of Staff | keep each run moving, honest and traced; the only door to `[ORG]AIOC-TOM` and to Source Lifecycle | PPD Design Lead | an agent (`[ORG]CELL-PCS`) | none; the run halts |
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
TEST-PPD-PCS v1 (TEST-PPD v1, case 73) · result `NOT_RUN`

### 4.2 Chief of Staff
#### Definition
Default, **managing** kind, with these additions:
- **The only door.** It is the only Cell of this AIOC that sends anything outside it: returns to `[ORG]AIOC-TOM`, an `accepted` return included; needs requests, Missing Reports and filings to `[ORG]AIOC-SL`; the release notice to the next stage. The four external ports sit on its card (§17).
- **No question to a person.** It never asks any person anything about the organisation. Every question for the organisation goes to the Chief of Staff of `[ORG]AIOC-SL` as a needs request (§5.2). Its only human contact is its own HOAC position, the PPD Design Lead, about the run.
- **An orchestrator that never judges itself.** It runs the gates of each run (Annex C), dispatches the Cells, locks outputs, runs the code steps, draws the Review Panel and writes the run record. It never rules on a finding, never dismisses or downgrades one, and never lowers a review (TOM blueprint `v0.4.1`, §5.8, carried).
#### Process (SOP)
Default, plus:
1. **Admission (S0).** On a run request: open the run record; check that the request carries references only; receive or fetch the release notice; have the Input socket build Input Pack P0 (§4.3); check gate T0 (Annex C.2) → *P0 and the T0 record* (evidence: the T0 record, with P0's ID).
2. **One run at a time.** One run per organisation. A second run in parallel needs the Design Lead's approval, recorded in the run record → *run slot* (evidence: run record).
3. **Returns.** Collect the return drafts of the Pods; have each reviewed at its review point; send each to `[ORG]AIOC-TOM` and file it into `[ORG]AIOC-SL` as a design report, with the same hash; mark the elements it touches `held: return open` → *return sent* (evidence: the return and its filing receipt).
4. **Passes.** Batch the Pods' needs candidates into passes of at most `rows_per_pass` rows, one decision per row; send each pass with its Missing Report → *pass sent* (evidence: Work Item IDs in the needs log).
5. **Waiting.** Overdue requests and returns follow the waiting deadlines and escalation (Protocol §4.6, item 1). Past `non_response_passes`, the run stops as `non-response`, and every element resting on a missing fact goes to decision as an assumption → *ageing record* (evidence: the needs log).
6. **Answers.** Hand each needs answer and each new release notice to the Input socket, which makes a new pack version; re-open only the work that cites what changed → *re-opened items* (evidence: the pack's increment).
7. **Code steps.** Run the code steps of §5.5 and §5.6 (job descriptions, decision-rights register, authority matrix, charts) and of §5.7 (workload) → *generated parts* (evidence: the step's output hash, re-generated byte-identical).
8. **Stops and revocation.** A stop takes effect at the gateway on every part; the Chief of Staff is itself stopped. A revoked or narrowed connection holds the run as `held: connection revoked`; no restart is needed when a new connection is signed → *held run* (evidence: unit register).
#### Role card
| Field | Content |
|---|---|
| Name | Chief of Staff |
| Position and seat | the position Chief of Staff; accountable seat: the PPD Design Lead (`[ORG]HOAC-ACS`) |
| Performed by | an agent (`[ORG]CELL-PCS`, full name PPD Chief of Staff) |
| Purpose | keep each run moving, honest and traced; be this AIOC's voice to the Design Lead and its only door to TOM, Source Lifecycle and the next stage |
| Authority limits | alone: dispatch, lock, record, run code steps, send returns and needs requests that passed their review, file a release whose elements are decided; needs the Design Lead: a second run in parallel, a budget above the cap, any change to configuration, a ruling on a finding, a reduced review level; never: ask a person anything about the organisation, change the TOM release, answer a needs request itself, take anything from the Design Lead as a source, decide for the Requesting Authority, rule on or dismiss a finding, sign, close a Work Item this AIOC performed, write a job description by hand |
| Write location | the run record and this AIOC's Work Items |
| Reports to | the PPD Design Lead |
| Escalation | to the Design Lead in one line, with evidence linked; a stop goes to the stop door, never through this Cell |
| Tools and access | the TOM and Source Lifecycle connections through the tool gateway, within their signed scopes; the code steps of the code project; no credential in any instruction |
| Deputy and cover | none; on failure the run halts and the Design Lead is told |
| Fixed test and score | TEST-PPD-PCS v1 (§9), plus the default Chief of Staff test |
| Card version and status | v0.1.0 · draft |
#### Fixed test
TEST-PPD-PCS v1 · result `NOT_RUN`

### 4.3 Input socket
#### Definition
Default, with this AIOC's standard format, the **Input Pack**, as in the TOM blueprint `v0.4.1` §4.3, parts 1 to 3 and 6 to 8, read with these changes:
1. **Two kinds of input.** The **release**: the decided TOM Release, by manifest and parts, each by hash, from the release notice. The **sources**: the organisation's other sources, by reference from Source Lifecycle's output socket, cut into atoms and labelled once (TOM Annex B, carried).
2. **The release is read, never atomised as a source.** Its elements keep their own IDs (`ROLE-n`, `HO-n`, `CPR-n`, `CHILD-…` and the ledger entry IDs). Every element of this AIOC's output traces to a release element or a source atom.
3. **The release check.** A release is admitted only when: its manifest validates; its final status is decided; its hash equals the copy filed in Source Lifecycle; and its role register re-compiles from its parts (TOM Annex E.17, rule 6). Otherwise nothing of it is used, and a return goes back with the failed condition (Annex B).
4. **A new release** from `[ORG]AIOC-TOM` makes a new pack version. The elements that changed re-open the work that cites them; decided work that cites nothing changed is kept by hash.
5. **Nothing that arrives through a human port is a source.** A run request is admitted only if it carries references; the words around them are not admitted.
6. The pack's ID is `PPDI-` followed by the SHA-256 of its body.
#### Process (SOP)
Default (receive, identify, normalise, check, deliver), run by the Chief of Staff through the socket's code steps. A refused item comes back with its reason and never enters.
#### Role card
Default; performed by the Chief of Staff (`[ORG]CELL-PCS`) through the socket's code steps.
#### Fixed test
TEST-PPD v1, cases 2, 3, 4, 23, 24, 25, 30, 33 · result `NOT_RUN`

### 4.4 Panel
#### Definition
Default. The Panel also shows, for each run: the run state and its flags with their ages; the TOM release in use and any newer one; every return, with its state and age; every needs request; each gate with its result; per review, its point, verdict and findings; the assumptions waiting for decision; the decision state of each element.
#### Process (SOP)
Default.
#### Role card
Default.
#### Fixed test
Default Panel test · result `NOT_RUN`

---
## 5. Functional capabilities

Ten stages (§5.0) are performed by the Input socket (§4.3: S0) and these capabilities: Release Intake and Returns (S1); Process Architecture (S2, S3); Process Writing (S4); Position Shaping (S5); Structure (S6); Workload (S7); Operational Walkthrough (S8); Decision Package and Release (S9). Needs Requests (§5.2) is a service every stage uses. Independent Review (§5.9) is the rule that closes every stage. Each capability is written in the four-part form (Annex A of the template), with one added row, **Done when**, which names its gate. Each step reads: **position**: action → *output* (evidence). Rules that apply to every capability are in Annex A (release parts and field lists), Annex B (returns), Annex C (run states and gates), Annex D (what this AIOC never does) and Annex E (what is carried from the TOM blueprint).

**One word per meaning.**
- **Release**, unqualified, is the TOM Release this run reads. **PPD Release** is this AIOC's output.
- **Role**: a role-type of the TOM release's role register (`ROLE-n`). **Position**: a position this AIOC designs (`POS-n`). A role may give rise to several positions; a position belongs to exactly one role.
- **Process** (`PRC-n`): a level-3 entry of the process architecture. **Step** (`STP-n`): one step of a process, in one role lane. **Decision** (`DEC-n`): a decision taken at a step.
- **Return** (`PPDR-n`): this AIOC's notice to `[ORG]AIOC-TOM` about its release (Annex B).
- **Assumption**: a value no source gives (a volume, a time, a limit, a measure), marked as such and put to decision. It is never a fact.

### 5.0 The stages: input, output, done-test

| ID | Plain name | Run state | Gate | Exact input | Exact output | Done-test | Human decision |
|---|---|---|---|---|---|---|---|
| S0 | **Admit** | `admitting` | T0 | The run Work Item (references only). The release notice from `[ORG]AIOC-TOM`. The connection grants to TOM and Source Lifecycle. The engine register. | Input Pack `P0`; the run record, opened; the RP0 review record. | **T0** (Annex C.2): the request carries references only; the release check passes (§4.3, part 3); both connections are signed and in scope; the engine register holds eligible engines; `requesting_authority_cell` is set. | Requesting Authority: opens the run. Seats over TOM and Source Lifecycle: sign the connections. |
| S1 | **Read the release** | `reading` | T1 | P0 (or later); the release, role register first. | The **release-reading record** (Annex A.1); return drafts (Annex B). | **T1**: every role, value-stream phase, capability, decision domain and hand-off of the release in scope is `used`, `returned` or `out of scope` with a reason; every return draft passed RP1 and was sent. | Requesting Authority: the children in scope, if the request did not name them. |
| S2 | **Architecture** | `architecting` | T2 | The release-reading record; the release; the pack's sources of current processes. | The **process architecture** (Annex A.2): levels 1 to 3, each level-3 process with one owner role. | **T2**: every phase and capability in scope has at least one process; every hand-off in scope belongs to one process; no process traces to nothing; RP2 settled clear. | Requesting Authority: the architecture rows. |
| S3 | **Critical processes** | `choosing` | T3 | The decided architecture. | The **critical-process choice**, with its reasons; the order in which processes are written. | **T3**: every process that crosses two parts of the release is either chosen or set aside with a reason; RP3 settled clear; the choice decided. | Requesting Authority: the choice and the order. |
| S4 | **Write the processes** | `writing` | T4 | Per process: its architecture entry; the release elements it carries; the pack's atoms for it. | Per process: its **process record** (Annex A.3). For a critical process: two locked drafts, the difference register and the reconciled record (Annex E, two authors). The **policy register** (Annex A.4) and the **controls catalogue** (Annex A.11), compiled by code from the process records. | **T4**, per process: each step has one accountable role and an input and output; each decision has exactly one decider; each lane hand-off is matched at both ends; each exception names its escalation; each measure, volume and time has a source or is an assumption; each step carries its done-when, worst error and reversibility, act kinds, input source and trust, confidentiality, risks, controls and record (§5.4, rules 11 and 12); the modelling conventions report no `error`; the end-to-end time is computed; RP4 settled with no unresolved `MATERIAL` finding. | Requesting Authority: assumptions; contradictions touching the process; control gaps; measure targets. PPD Design Lead: rulings. |
| S5 | **Shape the positions** | `shaping` | T5 | The written processes; the role register. | The **position register** (Annex A.5); the **job descriptions** (Annex A.6), generated by code; the **decision-rights register** and the **authority matrix** (Annex A.7), generated by code; the **objectives cascade** (Annex A.12), generated by code. | **T5**: every step and decision sits in exactly one position; every position holds at least one; every position belongs to one role; every position passes the segregation-of-duties rules or its breach is put to decision; every competence traces to a step or decision; the generated parts re-generate byte-identical; RP5 settled with no unresolved `MATERIAL` finding. | Requesting Authority: positions; decision limits with no source; job families and levels with no source; segregation rules with no source; separation breaches. |
| S6 | **Structure** | `structuring` | T6 | The position register; the release's parts and governance; the pack's sources of the current organisation. | **Reporting lines**, the **organisation charts** (generated by code), the **forum register** with charters and tiers, the **review calendar** (generated by code), the **result lines**, and the **crosswalk** (Annex A.8); the **structure scenarios** (Annex A.13) when `structure_scenarios` is above one. | **T6**: every position has one reporting line and no line forms a loop; spans and layers reported against the configured ranges; every forum has a charter and a tier; every measure has a forum that reviews it; every current unit, position and process in the sources is mapped or marked with a reason; with scenarios, each is shown on the same measures and one is decided; RP6 settled with no unresolved `MATERIAL` finding. | Requesting Authority: reporting lines; forums; span and layer findings; result lines with no source; the structure scenario; crosswalk rows marked `retired`. |
| S7 | **Workload** | `loading` | T7 | The written processes (volumes, step times); the position register; the time available per position, from a source or a decision. | The **workload register** (Annex A.9) and the **peak-load check and value-stream times** (Annex A.14), generated by code. | **T7**: every figure traces to the steps it sums; every input is a source or a decided assumption; every peak figure traces to its peak volumes and step times; RP7 settled clear. | Requesting Authority: the time available; assumptions; peak findings. |
| S8 | **Walk** | `walking` | T8 | The walk input, compiled by code from S2 to S7; a blind brief for the Situation Author. | The sealed situation set; the trace; the finding register; the **walkthrough report**. | **T8**: situations sealed before the walk; every situation traced to its end or to a finding; every finding fixed or put to decision; RP8 settled with no unresolved `MATERIAL` finding. | Requesting Authority: notice choices. PPD Design Lead: rulings. |
| S9 | **Decide and release** | `deciding`; end states `released`, then `filed` | T9, then T10 | Every reviewed part of S1 to S8, by hash; every pack version; the settled review records. | The **quality checks**; the Design Lead's attestation of T0 to T8; the **Decision Package** (Annex A.10); then the **PPD Release** manifest and its parts; the filing receipt; the release notice to the next stage. | **T9**: every element decided (`ACCEPT`, `CORRECT`, `REJECT`) and the final status decided; every process carries its owner position and its re-approval date; silence decided nothing. **T10**: the manifest is content-addressed; every element traces to a release element or a source atom; the release lint passes; the release is filed and reads back by hash; the release notice is sent. | Requesting Authority: each element and the final status. PPD Design Lead: the attestation. |

**Not stages: services and rules used by every stage.**

| Name | What it is | Output | Done-test |
|---|---|---|---|
| **Returns** (§5.1) | Every stage may find a defect in the release. It drafts a return; the Chief of Staff sends it to TOM after review | a return (Annex B) | Annex B, Done when |
| **Asking** (§5.2) | Every stage raises needs candidates; the Chief of Staff asks the Chief of Staff of `[ORG]AIOC-SL` | needs requests; one Missing Report per pass | each request ends answered by reference or with another outcome of the needs-answer contract |
| **Review Panel rule** (§5.9) | The rule that closes every stage | a review record and a verdict | §5.9, Done when |
| **Two authors** (Annex E) | Each critical process is written twice, blind, by two authors of two families, then reconciled | two locked drafts; the difference register; one reconciled record | TOM blueprint `v0.4.1`, Annex G, Done when, read with "process" for "child" |

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
| Rules | 1. **Role register first.** The Release Reader reads every entry of the role register before any other part, and records for each: `used` (the processes that will carry it), `returned` (with the return) or `out of scope` (with the reason). 2. **Then the rest.** Every value-stream phase, capability, decision domain, hand-off (`HO-n`) and counterparty crossing (`CPR-n`) of the children in scope is accounted the same way. 3. **Never changed.** The release is read as decided. No element of it is edited, merged, split or dropped by this AIOC. A role register entry that no process uses is returned, never deleted. 4. **Returns, not fixes.** A defect becomes a return of one kind (Annex B): `cannot use` (with what is missing), `contradiction found`, `assumption invalid` or `request kind unsupported`. When the whole release is used without defect, the run sends one `accepted` return. 5. **The touched elements wait.** The elements a return touches, and only those, are held as `held: return open` until a new decided release or a decision of the Requesting Authority answers it. The rest of the work goes on. 6. **Back and forth.** TOM's answer arrives as a new release notice. It makes a new pack version; the work that cites a changed element re-opens; decided work that cites nothing changed is kept by hash. Each pass is a new version; nothing is overwritten. 7. **Filed too.** Each return is also filed into Source Lifecycle as a design report, with the same hash, so that a revised TOM request can cite it (TOM blueprint `v0.4.1`, `docs/CARRIED-RULES.md` §4.4, item 5). 8. **Not a person.** A return names release parts, elements and fact-types, never a person. |

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
| Fixed test and score | TEST-PPD-PRR v1 (§9) |
| Card version and status | v0.1.0 · draft |

#### Fixed test
TEST-PPD-PRI v1 and TEST-PPD-PRR v1 · result `NOT_RUN`

### 5.2 Needs Requests

#### Definition
As in the TOM blueprint `v0.4.1` §5.2, carried, with these changes. What this AIOC typically asks for: the organisation's current process documents and procedures; volumes per period; step times; decision limits (for example spending thresholds); measures already in use; the time available per position per period; the policies a process applies. Each request names the process, step or decision it is for, and the unit of a figure. One decision per row; at most `rows_per_pass` rows per pass. A request never names a person. Done when: each request ends answered by reference, or with another outcome of the needs-answer contract, and its sub-item is `done` only when the Input socket's acceptance test passes.
#### Process (SOP)
As carried: the Pods raise needs candidates; the Chief of Staff batches, reviews (RPa), sends, waits, and admits each answer through the Input socket as a new pack version.
#### Role card
Performed by the Chief of Staff (§4.2).
#### Fixed test
TEST-PPD v1, cases 8, 31, 32, 33, 34 · result `NOT_RUN`

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
| Rules | 1. **Three levels.** Level 1 is a value-stream phase or a capability of the release; level 2 groups processes; level 3 is a process with a trigger and an end. Every level-3 process traces to at least one level-1 entry. 2. **One owner.** Each level-3 process has one owner role from the role register; from S5 the owner is a position of that role. 3. **Hand-offs belong somewhere.** Every hand-off in scope (`HO-n`) and every crossing with an outside party (`CPR-n`) belongs to exactly one process, which names it. 4. **Today's processes are evidence.** A current process named in the sources is mapped to the architecture or marked `not carried` with its reason; the crosswalk (§5.6) uses this. 5. **Critical first.** The processes that cross two or more parts of the release are proposed as critical. The Process Architect proposes an order with its reasons; the Requesting Authority decides the choice and the order. 6. **A general pattern is a method, never evidence** (TOM Annex B.5, carried). 7. **Reference models as methods.** A reference process taxonomy, a leading-practice flow or a measure library may be used to check the architecture for completeness. Each is recorded in `method_refs` and is never evidence: what it suggests becomes a needs request or a finding, never a process on its own. |

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
| Fixed test and score | TEST-PPD-PPA v1 (§9) |
| Card version and status | v0.1.0 · draft |

#### Fixed test
TEST-PPD-PA v1 and TEST-PPD-PPA v1 · result `NOT_RUN`

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
| Fixed test and score | TEST-PPD-PFPA v1, TEST-PPD-PSPA v1, TEST-PPD-PPR v1 (§9) |
| Card version and status | v0.1.0 · draft |

#### Fixed test
TEST-PPD-PPW v1 and the tests of its Cells · result `NOT_RUN`

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
| Rules | 1. **From the steps.** The Position Builder groups the steps and decisions of each role into positions. Every step and decision sits in exactly one position; every position holds at least one. 2. **One role.** Every position belongs to exactly one role of the role register. Work that fits no role is a return (`cannot use`), never a new role. 3. **Why this grouping.** Each grouping records its reason: the same expertise, the same counterpart, the same location, the same decision chain, or the release's own grouping. 4. **Separation.** A position that both takes a decision and checks that same decision fails, unless the Requesting Authority accepts it as a known defect. 5. **Generated, never written.** Each job description is generated by code from what the position holds: its purpose (from its processes' purposes), its accountabilities (its steps), its decisions and their limits, the positions it works with (its lane hand-offs), its measures and its reporting line (after S6). A field that does not trace to the position's steps and decisions fails the lint. 6. **Decision rights.** The decision-rights register lists every decision with its decider position, the others' parts and its limit. A limit with no source is a decision row. The authority matrix is generated from it. 7. **Positions only.** A job description names positions by code and title. It never names a person or a pay amount, and never says what fills the position. 8. **Job families and levels.** Each position carries its job family and its level when a source gives them or the Requesting Authority decides them. With neither, each field reads `not given` and the position goes on without it. They are never invented. Pay stays outside this AIOC (H-07). 9. **Segregation of duties.** Code checks every position against the segregation-of-duties rules of the controls catalogue (Annex A.11), for example one position both starting and approving the same payment, or both keeping an asset and recording it. Rule 4 is one of these rules. Each breach is listed with any compensating control and put to decision. A rule with no source is a decision row. 10. **Competence profile.** For each step and decision a position holds, the Position Builder states the knowledge and skill it needs, from the organisation's competence framework when a source gives one. The job description lists them as the position's competence profile. A competence that traces to no step or decision fails the lint. It never names a course, a provider or a person. 11. **The objectives cascade.** Code links each decided goal the release carries (until it carries them, each goal a source gives) to the measures of its value streams, then of its processes, then of the steps each position holds (Annex A.12). A goal with no measure under it, or a measure that serves no goal, is a finding. |

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
| Fixed test and score | TEST-PPD-PPB v1 (§9) |
| Card version and status | v0.1.0 · draft |

#### Fixed test
TEST-PPD-PPS v1 and TEST-PPD-PPB v1 · result `NOT_RUN`

### 5.6 Structure

#### Definition
| Field | Content |
|---|---|
| Name | Structure |
| Purpose | set who each position reports to, where positions meet, and how today's organisation maps to the target |
| Trigger | T5 passed |
| Inputs | the position register; the release's parts and governance skeleton; the pack's sources of the current organisation |
| Outputs | reporting lines; organisation charts (generated by code); the forum register with charters; the crosswalk (Annex A.8) |
| Performed by | the Structure Designer (`[ORG]CELL-PSD`) in the Structure Pod (`[ORG]POD-PS`) |
| Done when | T6 (§5.0) |
| Rules | 1. **One line.** Every position has one reporting line, within its part of the release, unless the release's governance places it elsewhere. No line forms a loop. 2. **Spans and layers are checks.** They are reported against `span_range` and `layers_max`. A value outside the range is a finding for decision, never an automatic change. 3. **Forums.** Each standing forum the processes need (a committee, a board, a review meeting) has a charter: its purpose, the decisions it takes or advises on, its member positions, its chair position, its cadence, its inputs and its outputs. A forum takes only decisions the decision-rights register gives it. 4. **The crosswalk.** Every current unit, position and process named in the sources is mapped to a target element, or marked `retired` or `not mapped`, each with its reason. A `retired` row is a decision row. 5. **Charts are generated** from the reporting lines, never drawn by hand. 6. **Tiers and the review calendar.** Each forum carries its tier: `daily`, `weekly`, `monthly`, `quarterly` or `annual`. Code generates the review calendar from the forum register and the measures each forum reviews. A measure that no forum reviews, or a tier the processes need that no forum holds, is a finding for decision. 7. **The result line.** Each part of the release names the line of the organisation's results it moves most (for example revenue, cost, cash or risk), from a source or a decision. 8. **Structure scenarios.** When `structure_scenarios` is above one, the Structure Designer proposes that many structures. Code shows them side by side on the same measures: positions, management positions, spans, layers and cost. Cost appears only where the organisation gives cost rates per job family and level as a source; with none, it reads `not given`. The Requesting Authority chooses one; this AIOC never chooses. |

#### Process (SOP)
1. **Structure Designer**: propose reporting lines and forums, and draft the crosswalk → *structure draft* (evidence: one row per position, forum and current element).
2. **Chief of Staff**: run the line checks, the span and layer report, and generate the charts, the review calendar and, with scenarios, the side-by-side view → *check record; charts; review calendar; scenario view* (evidence: re-generated byte-identical).
3. **Chief of Staff**: run RP6, then send the rows for decision → *decided rows* (evidence: decision references).

#### Role card
| Field | Content |
|---|---|
| Name | Structure Designer |
| Position and seat | Structure Designer; accountable seat: the PPD Design Lead |
| Performed by | an agent (`[ORG]CELL-PSD`, full name PPD Structure Designer) |
| Purpose | reporting lines, forums and the crosswalk |
| Authority limits | alone: propose; never: change a position's steps, change a span or layer to fit a range, retire a current element without a decision, ask a person |
| Write location | the run record |
| Reports to | Chief of Staff |
| Escalation | to the Chief of Staff |
| Tools and access | the position register, the release and the pack; a fresh context per dispatch |
| Fixed test and score | TEST-PPD-PSD v1 (§9) |
| Card version and status | v0.1.0 · draft |

#### Fixed test
TEST-PPD-PS v1 and TEST-PPD-PSD v1 · result `NOT_RUN`

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
| Rules | 1. **The sum.** A position's workload for the period is the sum, over the steps it holds, of volume times step time. 2. **Traced.** Every figure names the steps it sums and the source or decided assumption of each input. 3. **Time, not anything else.** The register shows time per period against the time available. It draws no other conclusion. 4. **Gaps stay visible.** A step with no volume or no time is listed as a gap, and its position's figure is marked incomplete. 5. **Peak load.** Where a source gives a peak period and its volume, code computes each position's time needed in that period against its time available (Annex A.14). A peak above the time available is a finding for decision, never a change to a position. 6. **End-to-end time of a value stream.** Code adds the end-to-end times of the processes along each value stream (§5.4, rule 16). A missing term marks it incomplete. |

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
| Fixed test and score | TEST-PPD-PWA v1 (§9) |
| Card version and status | v0.1.0 · draft |

#### Fixed test
TEST-PPD-PWA v1 · result `NOT_RUN`

### 5.8 Operational Walkthrough

#### Definition
As in the TOM blueprint `v0.4.1` §5.7, carried, read with "processes, positions and decisions" for "operating model". The Situation Author writes situations blind to the design, from a blind brief compiled by code (the parts of the release in scope, the roles, the hand-offs; never the process records). The set is sealed before the walk. The Situation Walker walks each situation through the processes, positions, decisions and forums, and records where it holds and where it breaks: a step with no position, a decision with no decider, a hand-off that ends nowhere, an exception with no escalation, a forum asked to decide what it may not. Done when: T8 (§5.0).
#### Process (SOP)
As carried: compile the walk input and the blind brief; author; seal; walk; classify; RP8; route each finding (fix upstream, or put to decision).
#### Role card
Situation Author (`[ORG]CELL-PSA`) and Situation Walker (`[ORG]CELL-PSW`), in the Walkthrough Pod (`[ORG]POD-PW`); as carried, with their own tests.
#### Fixed test
TEST-PPD-PW v1, TEST-PPD-PSA v1, TEST-PPD-PSW v1 · result `NOT_RUN`

### 5.9 Independent Review

#### Definition
The Review Panel rule of the TOM blueprint `v0.4.1` §5.8, carried whole: three to five engines from two or more families review each locked output, alone first, then in a short debate held to quotes; code settles; the PPD Design Lead rules only on what stays contested; at the `full` level no engine is of an author's family (its rule 4); the Chief of Staff never rules, dismisses, downgrades or lowers. This AIOC's review points: RP0 (P0), RP1 (release-reading record and return drafts), RP2 (architecture), RP3 (critical-process choice), RP4 (each process record), RP5 (positions and generated parts), RP6 (structure), RP7 (workload), RP8 (walk findings), RP9 (the release, before filing), and RPa (each needs pass). Done when: as carried.
#### Process (SOP)
As carried.
#### Role card
Blind Reviewers A to E (`[ORG]CELL-PBRA` to `[ORG]CELL-PBRE`), in the Review Pod (`[ORG]POD-PR`); as carried.
#### Fixed test
TEST-PPD-PR v1 and the tests of its Cells · result `NOT_RUN`

### 5.10 Decision Package and Release

#### Definition
| Field | Content |
|---|---|
| Name | Decision Package and Release |
| Purpose | put every element to the organisation's decision, then freeze, file and hand over the decided design |
| Trigger | T8 passed |
| Inputs | every reviewed part of S1 to S8, by hash; the settled review records |
| Outputs | the quality checks; the Decision Package (Annex A.10); the PPD Release manifest and its parts; the filing receipt; the release notice to the next stage |
| Performed by | the Chief of Staff, by code steps; the PPD Design Lead attests the method |
| Done when | T9 and T10 (§5.0) |
| Rules | 1. **Every element is decided.** The Decision Package puts each element to the Requesting Authority: `ACCEPT`, `CORRECT` or `REJECT`; then the final status. Silence, or approval of a whole pass, decides nothing (TOM blueprint `v0.4.1`, `docs/CARRIED-RULES.md` §5, carried). 2. **Plain words.** The Decision Package states the unknowns, the assumptions and the open returns in plain words. 3. **Frozen and content-addressed.** The manifest lists every part by hash, every pack version, the TOM release it was designed from (ID and manifest hash) and every return sent. 4. **The release lint.** The release holds processes and positions only: no person's name, no pay, nothing on what fills a position, no text of a policy. 5. **Filed and handed over.** The release is filed into Source Lifecycle as a source of origin kind `process and position design`, read back by hash, and announced to the next stage by a release notice. 6. **Returned to us.** The next stage returns defects to this AIOC with the same return kinds (Annex B). A change is a new run whose release supersedes this one. 7. **Approval and re-approval.** Each decided process carries its owner position, the decision that approved it, and its re-approval date, set from `re_approval_period`. The release lists every process with its date; the stage that runs the organisation raises the review when it falls due. |

#### Process (SOP)
1. **Chief of Staff**: generate the quality checks and the Decision Package; obtain the Design Lead's attestation of T0 to T8 → *Decision Package* (evidence: hashes).
2. **Chief of Staff**: run RP9; send the element rows and the final status for decision → *decided rows* (evidence: decision references).
3. **Chief of Staff**: freeze the manifest, run the release lint, file into `[ORG]AIOC-SL`, read back, send the release notice → *filed PPD Release* (evidence: the filing receipt and the read-back hash).

#### Role card
Performed by the Chief of Staff (§4.2); the attestation by the PPD Design Lead (§13, H-12).

#### Fixed test
TEST-PPD-PCS v1 (cases 64 to 67) · result `NOT_RUN`

---

## 6. Coordination and routes

- **`[ORG]AIOC-TOM`.** The operating model source, linked directly (Protocol §17, items 2 and 3).
  - **Routes.** Release notices arrive through the Input socket. Returns leave as Work Items through the output port, each also filed into Source Lifecycle.
  - **The connection.** Signed by the `[ORG]HOAC-ACS` position over `[ORG]AIOC-TOM` as `connect-external-port`, with two scopes: read its decided releases; send returns. A wider scope is `grant-or-widen-access`. A revocation cuts it at the gateway at once and holds the run.
  - **Loops.** A return is a Work Item to TOM. TOM answers it with a new release notice; it never opens a new item back to this AIOC, so the chain never loops (Protocol §4.6, item 2).
- **`[ORG]AIOC-SL`.** The source of record, and the only route to any person in the organisation.
  - **The connection.** Signed by the `[ORG]HOAC-ACS` position over `[ORG]AIOC-SL` as `connect-external-port` (Protocol §13, item 5), with three scopes: read; needs requests; write only this AIOC's own releases and design reports (its returns).
  - **Needs requests** are sub-items of the run, with chain depth 1.
- **The next design stage.** It receives the PPD Release by a release notice and returns defects with the same return kinds (Annex B).
- **Work Items.**
  - **The run.** One Work Item, opened by the Requesting Authority's Cell through the HU input port. Requested output: a PPD Release (Annex A). Acceptance test: the Requesting Authority's (T9 decided; the manifest valid; the filed reference reads back). Sources: the TOM Release reference and, optionally, the children in scope.
- **`[ORG]AIOC-OCO`.** It installs, fixes and upgrades this AIOC through the front door. Every proposal, correction or critique of this AIOC's AIs is a `design-proposal` Work Item to OCO.
- **Routing rows this AIOC contributes.** `return → [ORG]AIOC-TOM`; `return filing → [ORG]AIOC-SL`; `needs request → [ORG]AIOC-SL`; `missing report → [ORG]AIOC-SL`; `PPD Release filing → [ORG]AIOC-SL`; `release notice → the next design stage`.

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
- **Engine ceilings.** No atom or release part is sent to an engine whose confidentiality ceiling is below its level (TOM blueprint `v0.4.1` §5.8, rule 17, carried).

## 8. Tools and the shared AI gateway

| Tool | Existing shared tool, or new | If new: asked of the builder as |
|---|---|---|
| The TOM connection (release notice in, returns out) | new on both sides | a change to `[ORG]AIOC-TOM` proposed through OCO (`upstream/PROPOSALS.md`, item 1) |
| The Source Lifecycle connection (output socket, needs requests, filing) | existing in `[ORG]AIOC-SL`, with the proposed additions already asked by `[ORG]AIOC-TOM`; the origin kind `process and position design` is new | a change to `[ORG]AIOC-SL` proposed through OCO (`upstream/PROPOSALS.md`, item 2) |
| The code steps: the socket and the release check; the release-reading check; process checks; draft compare; policy-register compile; placement checks; job-description, decision-rights and authority-matrix generators; line checks, span and layer report, chart generator; workload compute; walk-input compile and blind-brief extract; review code steps (carried); quality checks; release lint | new in this AIOC's code project, one build item per step, each with its tests | build items in the code project |
| The schemas of Annex A and the return contract | the return contract is in `contracts/`; the others are field lists in Annex A, made into schemas before the first run | build items in the code project |
| Engine calls | through the tool gateway, bound per call from the engine register | — |

- **Metering.** Every engine call goes through the tool gateway of the `[ORG]AION`, metered for this AIOC (Standard §4.4, item 11).
- **Null default.** Every AI Cell runs with no tools, no outside access, no memory and a fresh context for each dispatch.
- **Tests stay hidden from the runners.** No Cell under test sees TEST-PPD, its fixtures or §9.

| Tool role | Connector | Access managed in | Part card version |
|---|---|---|---|
| operating model source | `[ORG]AIOC-TOM` release port | Panel; the grant is signed at the tool gateway as `connect-external-port` | 49GAION Target Operating Model (proposed) |
| source of record | `[ORG]AIOC-SL` output socket | Panel; as above | 49GAION Source Lifecycle, v1 |

**Mechanism register.** Read on 15 October 2026. A row is never deleted.

| ID | Mechanism | What it does | Where it lives | Today | Target |
|---|---|---|---|---|---|
| M-01 | Release check | admits only a decided release whose hash matches its filed copy | — | decided, not built | build |
| M-02 | Return path to TOM | sends returns, holds touched elements, re-opens on a new release | — | decided, not built | build (with the TOM change) |
| M-03 | Process checks | one accountable role per step; one decider per decision; matched hand-offs | — | decided, not built | build |
| M-04 | Generators | job descriptions, decision-rights register, authority matrix, charts, workload | — | decided, not built | build |
| M-05 | Release lint | keeps the release to processes and positions | — | decided, not built | build |
| M-06 | Review Panel rule | as carried from `[ORG]AIOC-TOM` | `[ORG]AIOC-TOM` code project, when built | decided, not built | reuse |

**Reserve.**

| ID | Idea | Why held | Reconsider when |
|---|---|---|---|
| R-01 | Job families and levels in the position register | taken up on 15 October 2026 (§13, H-07); kept here as a record | — |
| R-02 | A shared review service for every design stage, instead of each stage carrying the TOM rule | one more part to build before the first run | a third design stage needs the same rule |

## 9. Fixed tests: index, triggers and scores

The cases are written in `tests/TEST-PPD.md`. Cases 1 to 22 are the Library's TEST-PROCESS-AND-POSITION-DESIGN v1, cases 1 to 22, unchanged. Cases 23 to 94 are this AIOC's own. The Design Lead's seat test is PDL-1 to PDL-5. The owner of every part's test is the PPD Design Lead; the owner of the AIOC's whole test, and of the Design Lead's own seat test, is the Cell carrying `[ORG]HOAC-TM`.

| Part | Test ID and version | Cases of TEST-PPD v1 | Evidence level | Last run | Result |
|---|---|---|---|---|---|
| `[ORG]AIOC-PPD` (whole) | TEST-PPD v1 | all (1–94) | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PDL` PPD Design Lead | TEST-PPD-PDL v1 | PDL-1 to PDL-5 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PCS` Chief of Staff (with Office, Input socket, Needs Requests, Decision Package and Release) | TEST-PPD-PCS v1 | 1–4, 8, 13, 18, 19, 21–27, 29–34, 48, 51, 62, 64–67, 73–75, 83, 84, 86, 87, 90, 92, 94 | MEASURED | — | `NOT_RUN` |
| Panel | default Panel test | — | MEASURED | — | `NOT_RUN` |
| `[ORG]POD-PRI` Release Intake | TEST-PPD-PRI v1 | 3, 5, 6, 7, 28, 30, 47 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PRR` Release Reader | TEST-PPD-PRR v1 | 3, 5, 28, 30, 47 | MEASURED | — | `NOT_RUN` |
| `[ORG]POD-PA` Architecture | TEST-PPD-PA v1 | 9, 10, 35–38, 93 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PPA` Process Architect | TEST-PPD-PPA v1 | 9, 10, 35–37, 93 | MEASURED | — | `NOT_RUN` |
| `[ORG]POD-PPW` Process Writing | TEST-PPD-PPW v1 | 11, 16, 39–45, 78–82, 86, 91 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PFPA` First Process Author | TEST-PPD-PFPA v1 | 11, 16, 40–45, 78–82, 86, 91 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PSPA` Second Process Author | TEST-PPD-PSPA v1 | 11, 16, 39–45, 78–82, 86, 91 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PPR` Process Reconciler | TEST-PPD-PPR v1 | 39, 41 | MEASURED | — | `NOT_RUN` |
| `[ORG]POD-PPS` Position Shaping | TEST-PPD-PPS v1 | 12, 13, 20, 46–52, 77, 84, 85 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PPB` Position Builder | TEST-PPD-PPB v1 | 12, 20, 46, 47, 52, 77, 85 | MEASURED | — | `NOT_RUN` |
| `[ORG]POD-PS` Structure | TEST-PPD-PS v1 | 14, 15, 53–58, 87–90 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PSD` Structure Designer | TEST-PPD-PSD v1 | 14, 53–56, 87, 88 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PWA` Workload Analyst | TEST-PPD-PWA v1 | 15, 16, 57, 58, 89, 90 | MEASURED | — | `NOT_RUN` |
| `[ORG]POD-PW` Walkthrough | TEST-PPD-PW v1 | 17, 59, 60 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PSA` Situation Author | TEST-PPD-PSA v1 | 59 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PSW` Situation Walker | TEST-PPD-PSW v1 | 17, 60 | MEASURED | — | `NOT_RUN` |
| `[ORG]POD-PR` Review | TEST-PPD-PR v1 | 22, 61–63 | MEASURED | — | `NOT_RUN` |
| `[ORG]CELL-PBRA` to `[ORG]CELL-PBRE` Blind Reviewers | TEST-PPD-PBRA v1 to TEST-PPD-PBRE v1 | 22, 61, 63 | MEASURED | — | `NOT_RUN` |
| Type (Specialised) | TEST-PPD v1, case 76 | 76 | MEASURED | — | `NOT_RUN` |

- **Re-run triggers.** The template defaults, plus any change to the return contract, to the TOM release format, to the Source Lifecycle output socket, or to the release lint's word list.
- **Complete** only when every part's test has a visible result. `NOT_RUN` is never PASS.

**Checks that are not fixed tests.**

| Check | Placement | Budget per item | Degradation order | Blocks only for |
|---|---|---|---|---|
| Outbound name check: no person's name in any return, needs request or release part | router | each outbound message | none | the message |
| Release lint | as evidence on the verdict record of RP9 | each release | none | the filing |
| Re-generation check: every generated part re-generates byte-identical | inside the producer's loop, at most 2 fix rounds | each generated part | none | the stage's gate |
| Return reconciliation: every return sent has a filed copy with the same hash | after completion | daily | none; a failure opens a defect | nothing; it flags |

## 10. Build: what is generated from this file

| Built thing | Generated from | Recorded where |
|---|---|---|
| Panel profile | §0, §1, §3, §4.4, §5 role cards | the panel profile names this file's commit |
| Back office | §4.2 role card and SOP (instruction); §4 to §5 (knowledge) | the back office records the commit it was built from |
| Card in the protocol AIOC's map | §1 | the register links this file |
| Cards of the Pods and Cells, and the bot identity cards | §17 | `cards/`, by `tools/make_cards.py` |
| The return contract's validator | `contracts/release-return.schema.json` | `tools/check_contracts.py` |

**Delivery path:** definition change → tests → Panel and Back office update → one-click rollback to the previous commit.

## 11. Exceptions

1. **The Chief of Staff never asks the organisation's people anything.** It reaches the organisation only through the Chief of Staff of `[ORG]AIOC-SL`. Reason: as for `[ORG]AIOC-TOM` (its §11, item 1); a design rests on recorded sources, never on words spoken to the designer.
2. **The Back office does not converse with humans** (`converses_with_humans: false`). Reason: as in item 1.
3. **Two operating sources.** The template's Input socket takes sources. This one also takes a design release directly from another AIOC, by reference and hash, and returns defects to it. Reason: the direction of the governing seat that this AIOC is linked to the TOM itself (`decisions/DR-0001`; Protocol §17, items 2 and 3).
4. **Rules carried by reference.** The Review Panel rule, the two-author rule, labels and decision rules are carried from the TOM blueprint `v0.4.1` by section, not restated. A change there reaches this AIOC only when this blueprint pins the new version (Annex E).

## 12. Lessons and proposals to the mother

One dated line per lesson, each written without any organisation's details. Nothing is proposed upstream without the governing seat's word; the drafts are in `upstream/PROPOSALS.md`.

1. 2026-10-15 · The stage after the operating model was first framed as positions alone. Leading design practice designs processes and decision rights with the roles, processes first. Test question added: case 12 (no position without a step or decision). This text is the mother.
2. 2026-10-15 · A stage that reads a design release must be able to send defects back to the stage that made it, without a person relaying them. Test question added: cases 5 to 7. Proposed: the TOM changes in `upstream/PROPOSALS.md`, item 1.
3. 2026-10-15 · Fifteen products that design, launch or run organisations were taken apart from public material, and each useful feature was placed in the stage where it truly belongs. Those that belong here: the facts of each step, controls and segregation of duties, the objectives cascade, measures of three kinds, structure scenarios, peak load, variants, modelling conventions, forum tiers, end-to-end time and re-approval. Anything that rates or watches a person was not taken. Test questions added: cases 78 to 94 (`decisions/DR-0002`). Proposed: `upstream/PROPOSALS.md`, item 5.
4. 2026-10-15 · A review of what launching an organisation needs after this stage found three small additions that belong here: a competence profile in each job description; risk, control and record per step; measure definitions and the review calendar beside the forums. Test questions added: cases 82, 85 and 87 (`decisions/DR-0002`).

## 13. For the `[ORG]HOAC-ACS` seat, and every decision only a human seat can take

Every decision that only a human seat can take is listed here once. Silence decides nothing; a general approval decides no row.

| ID | Decision | Seat | Default |
|---|---|---|---|
| H-01 | Name the Requesting Authority's Cell: the GOV Cell itself, or a human Cell to which it delegates the design decisions (`delegate-authority`) | GOV | none: T0 fails |
| H-02 | **Top management's own mechanism.** Arrange the PPD Design Lead position and any HOAC position added to this AIOC. Nothing of who occupies them enters this blueprint | the Cell carrying `[ORG]HOAC-TM` | the position is vacant: the AIOC does not join |
| H-03 | Install `[ORG]AIOC-PPD` (`create-or-install-unit`); its `change-parent`; its `restart-stopped-unit` | the Cell carrying `[ORG]HOAC-TM` | none |
| H-04 | Accept the TOM changes that let this AIOC read releases directly and send returns (`upstream/PROPOSALS.md`, item 1) | the Cell carrying `[ORG]HOAC-TM`, made through OCO | required before joining |
| H-05 | Accept the Source Lifecycle origin kind `process and position design` and this AIOC's filing scope (`upstream/PROPOSALS.md`, item 2) | the Cell carrying `[ORG]HOAC-TM`, made through OCO | required before joining |
| H-06 | The connection grants to TOM and to Source Lifecycle (`connect-external-port`), their widening and revocation | the `[ORG]HOAC-ACS` positions over `[ORG]AIOC-TOM` and `[ORG]AIOC-SL` | none: T0 fails |
| H-07 | **People.** Job families and levels in the position register. **Decided by GOV, 15 October 2026** (`decisions/DR-0001`, item 8): carried, from a source or a decision of the Requesting Authority; `not given` when neither gives them; never invented. Pay stays outside this AIOC in every case | GOV (decided); the Requesting Authority for each value with no source | carried |
| H-08 | `review_budget_per_run`, `reduced_review_permitted` and the AIOC's `budget_cap` | the Cell carrying `[ORG]HOAC-TM` | none: must be set; reduced review `no` |
| H-09 | `span_range`, `layers_max`, `workload_period`, `re_approval_period` and `structure_scenarios` | the Cell carrying `[ORG]HOAC-TM` | none: must be set; `structure_scenarios` 1 |
| H-10 | Open the run; name the children in scope | Requesting Authority | none: no run |
| H-11 | The rows of S1 to S9: architecture; critical choice and order; assumptions; contradictions; control gaps; measure targets; positions; decision limits; job families and levels with no source; segregation rules with no source; separation breaches; reporting lines; forums; span and layer findings; result lines with no source; the structure scenario; crosswalk rows marked `retired`; time available; peak findings; walk notices; each element and the final status | Requesting Authority | undecided |
| H-12 | Inside a run: rule on contested `MATERIAL` findings; accept a reduced level within H-08; approve a second run; attest T0 to T8 | the PPD Design Lead | none taken; the step waits |
| H-13 | Create `<org>aioc-ppd-records` and `-records-restricted`, recorded first (Naming Standard R9) | the Cell carrying `[ORG]HOAC-TM` | before the first run |
| H-14 | Send the drafts of `upstream/` to 49GAION or to the parts they concern | GOV | after this blueprint is approved |
| H-15 | Approve this blueprint `v0.1.0` as the design of `[ORG]AIOC-PPD` | the human hub | it stays a draft; nothing is installed |

**Money:** the budget cap and the review budget (H-08). **People:** H-07 (decided); this AIOC designs positions, never who fills them. **Legal:** none decided here.

## 14. Change log

| Blueprint version | Date | Change | Template version | Commit |
|---|---|---|---|---|
| v0.1.0 | 2026-10-15 | First blueprint of `[ORG]AIOC-PPD`, the mother text of the Library part 49GAION Process and Position Design (Protocol §17, proposed): ten stages, processes first; the direct link to `[ORG]AIOC-TOM`, with returns; positions only; job families and levels (`decisions/DR-0001`, item 8); the step facts, controls and segregation of duties, competence profiles, the objectives cascade, measures of three kinds, forum tiers and the review calendar, structure scenarios, peak load, variants, modelling conventions, end-to-end time and re-approval (`decisions/DR-0002`); TEST-PPD v1, 94 cases | v1.5.0 at `e89ed1d` | this pull request |

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
| Workload period | `workload_period` | none: must be set | a week, a month or a year | PPD Design Lead |
| Re-approval period | `re_approval_period` | none: must be set | a period, for example twelve months | the Cell carrying `[ORG]HOAC-TM` |
| Structure scenarios | `structure_scenarios` | 1 | 1–3 | the Cell carrying `[ORG]HOAC-TM` |
| Modelling conventions | `modelling_conventions` | the base set: §5.4 rules 1 to 5 and 11 as `error`; naming and layout rules as `warning` | the base set plus the organisation's own rules, each `error` or `warning`; the base set is never lowered | PPD Design Lead |
| Template slots | `office_accountable_human`, `central_head`, `discussion_limits`, `waiting_deadlines`, `bounce_limit`, `chain_depth` (at least 1), `halt_request_priority` (immediate), `budget_cap`, `unattended_action` (`read-record-triage`), and the `v1.6.0` rows | as the template | — | as the template |

---

## 16. Type

- **Type:** Specialised.
- **Why this AIOC exists:** an organisation needs its processes and positions designed from its decided operating model, traced to it and decided by its own authority.
- **Type-specific test:** TEST-PPD v1, case 76 · result `NOT_RUN`.

---

## 17. Cells and Pods

The parts inside this AIOC (`docs/CELLS-AND-PODS.md` of `49GAION-aioc`). The role and nature of this AIOC are read from the type of its top Cell, the PPD Design Lead. Every field that points to a human takes a position code only.

| Code | Kind | Type | Filler kind | HOAC label | Parent | Fixed test (owner) | External ports |
|---|---|---|---|---|---|---|---|
| `[ORG]CELL-PDL` | CELL | Human Seat | human | `[ORG]HOAC-ACS` | `[ORG]AIOC-PPD` | TEST-PPD-PDL v1 (the Cell carrying `[ORG]HOAC-TM`) | none |
| `[ORG]CELL-PCS` | CELL | AI Chief of Staff | ai | none | `[ORG]AIOC-PPD` | TEST-PPD-PCS v1 (`[ORG]CELL-PDL`) | `tom-in`, `tom-out`, `sl-in`, `sl-out` |
| `[ORG]POD-PRI` | POD | AI Pod | — | none | `[ORG]AIOC-PPD` | TEST-PPD-PRI v1 (`[ORG]CELL-PDL`) | — |
| `[ORG]CELL-PRR` | CELL | AI Agent | ai | none | `[ORG]POD-PRI` | TEST-PPD-PRR v1 (`[ORG]CELL-PDL`) | none |
| `[ORG]POD-PA` | POD | AI Pod | — | none | `[ORG]AIOC-PPD` | TEST-PPD-PA v1 (`[ORG]CELL-PDL`) | — |
| `[ORG]CELL-PPA` | CELL | AI Agent | ai | none | `[ORG]POD-PA` | TEST-PPD-PPA v1 (`[ORG]CELL-PDL`) | none |
| `[ORG]POD-PPW` | POD | AI Pod | — | none | `[ORG]AIOC-PPD` | TEST-PPD-PPW v1 (`[ORG]CELL-PDL`) | — |
| `[ORG]CELL-PFPA` | CELL | AI Agent | ai | none | `[ORG]POD-PPW` | TEST-PPD-PFPA v1 (`[ORG]CELL-PDL`) | none |
| `[ORG]CELL-PSPA` | CELL | AI Agent | ai | none | `[ORG]POD-PPW` | TEST-PPD-PSPA v1 (`[ORG]CELL-PDL`) | none |
| `[ORG]CELL-PPR` | CELL | AI Agent | ai | none | `[ORG]POD-PPW` | TEST-PPD-PPR v1 (`[ORG]CELL-PDL`) | none |
| `[ORG]POD-PPS` | POD | AI Pod | — | none | `[ORG]AIOC-PPD` | TEST-PPD-PPS v1 (`[ORG]CELL-PDL`) | — |
| `[ORG]CELL-PPB` | CELL | AI Agent | ai | none | `[ORG]POD-PPS` | TEST-PPD-PPB v1 (`[ORG]CELL-PDL`) | none |
| `[ORG]POD-PS` | POD | AI Pod | — | none | `[ORG]AIOC-PPD` | TEST-PPD-PS v1 (`[ORG]CELL-PDL`) | — |
| `[ORG]CELL-PSD` | CELL | AI Agent | ai | none | `[ORG]POD-PS` | TEST-PPD-PSD v1 (`[ORG]CELL-PDL`) | none |
| `[ORG]CELL-PWA` | CELL | AI Agent | ai | none | `[ORG]POD-PS` | TEST-PPD-PWA v1 (`[ORG]CELL-PDL`) | none |
| `[ORG]POD-PW` | POD | AI Pod | — | none | `[ORG]AIOC-PPD` | TEST-PPD-PW v1 (`[ORG]CELL-PDL`) | — |
| `[ORG]CELL-PSA` | CELL | AI Agent | ai | none | `[ORG]POD-PW` | TEST-PPD-PSA v1 (`[ORG]CELL-PDL`) | none |
| `[ORG]CELL-PSW` | CELL | AI Agent | ai | none | `[ORG]POD-PW` | TEST-PPD-PSW v1 (`[ORG]CELL-PDL`) | none |
| `[ORG]POD-PR` | POD | AI Pod | — | none | `[ORG]AIOC-PPD` | TEST-PPD-PR v1 (`[ORG]CELL-PDL`) | — |
| `[ORG]CELL-PBRA` … `[ORG]CELL-PBRE` | CELL | AI Agent | ai | none | `[ORG]POD-PR` | TEST-PPD-PBRA v1 … TEST-PPD-PBRE v1 (`[ORG]CELL-PDL`) | none |

**The card data (the blueprint governs).** `tools/make_cards.py` expands the block below into the complete unit cards and bot identity cards, writes them into `cards/`, and checks them against the schemas of `49GAION-protocol`, the code rules of its `tests/cards/check_cards.py`, Naming Standard R15, and this blueprint.

```yaml
parts:
  defaults:
    accountable_to: "[ORG]CELL-PDL"
    card_version: "v0.1.0"
    version: "0.1.0"
    lifecycle_state: "designed"
    test_version: "v1"
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
      test: { id: "TEST-PPD-PDL", cases: "PDL-1 to PDL-5", owner: "[ORG]CELL-TMS" }
      ai_in: ["run brief", "ruling sheets for contested MATERIAL findings", "release notice"]
      ai_out: ["run control and configuration"]
      hu_in: ["direction from the Cell carrying [ORG]HOAC-TM"]
      hu_out: ["rulings, attestations and reduced-level acceptances, under live sign-in", "report to the Cell carrying [ORG]HOAC-TM"]
    - code: "[ORG]CELL-PCS"
      full_name: "PPD Chief of Staff"
      role: "Chief of Staff"
      parent: "[ORG]AIOC-PPD"
      type: "AI Chief of Staff"
      filler_kind: "ai"
      cell_kind: "chief-of-staff-cell"
      test: { id: "TEST-PPD-PCS", cases: "1-4, 8, 13, 18, 19, 21-27, 29-34, 48, 51, 62, 64-67, 73-75, 83, 84, 86, 87, 90, 92, 94" }
      ai_in: ["release notice", "source reference", "needs answer", "needs status", "needs candidate", "return draft", "locked outputs of the Pods", "settled review records"]
      ai_out: ["Input Pack version", "dispatch to a Pod", "review packet", "return", "needs request", "missing report", "generated parts", "PPD Release filing", "release notice"]
      hu_out: ["run brief to the PPD Design Lead", "ruling sheets to the PPD Design Lead", "release notice to the Requesting Authority's Cell"]
      external_ports:
        - { port: "tom-in", direction: "input", accepted_content: ["release notice"], authority_limit: "the read scope signed under connect-external-port over [ORG]AIOC-TOM", audit_trail: "unit register connected and disconnected events; serve log of [ORG]AIOC-TOM" }
        - { port: "tom-out", direction: "output", accepted_content: ["return"], authority_limit: "returns only, under the scope signed over [ORG]AIOC-TOM", audit_trail: "unit register; the Work Item record" }
        - { port: "sl-in", direction: "input", accepted_content: ["source reference", "needs answer", "needs status"], authority_limit: "the read scope signed under connect-external-port over [ORG]AIOC-SL", audit_trail: "unit register; serve log of [ORG]AIOC-SL" }
        - { port: "sl-out", direction: "output", accepted_content: ["needs request", "missing report", "return filing", "PPD Release filing"], authority_limit: "the request and write scope signed over [ORG]AIOC-SL: this AIOC's own releases and design reports only", audit_trail: "unit register; serve log of [ORG]AIOC-SL" }
      bot:
        allowed_actions: ["dispatch Cells of this AIOC", "build Input Pack versions through the code steps", "lock outputs and run code steps", "draw review engines and run the review code steps", "write the run record", "send reviewed returns to [ORG]AIOC-TOM and file them in [ORG]AIOC-SL", "send needs requests and Missing Reports to [ORG]AIOC-SL", "generate job descriptions, registers, charts and workload through the code steps", "file a release whose elements are decided", "send release notices"]
        ask_first_actions: ["a second run in parallel", "a budget above the cap", "a reduced review level", "any change to configuration", "anything outside its role card"]
    - { code: "[ORG]CELL-PRR", full_name: "PPD Release Reader", role: "Release Reader", parent: "[ORG]POD-PRI", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PRR", cases: "3, 5, 28, 30, 47" }, ai_in: ["Input Pack version", "the TOM release, role register first"], ai_out: ["release-reading record", "return draft"], bot: { allowed_actions: ["read and account for every element of the release", "draft returns with their evidence"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PPA", full_name: "PPD Process Architect", role: "Process Architect", parent: "[ORG]POD-PA", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PPA", cases: "9, 10, 35-37, 93" }, ai_in: ["release-reading record", "Input Pack version"], ai_out: ["process architecture draft", "critical-process proposal", "return draft", "needs candidate"], bot: { allowed_actions: ["draft the process architecture with its trace", "propose the critical processes and their order"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PFPA", full_name: "PPD First Process Author", role: "First Process Author", parent: "[ORG]POD-PPW", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PFPA", cases: "11, 16, 40-45, 78-82, 86, 91" }, ai_in: ["architecture entry", "release elements", "Input Pack atoms"], ai_out: ["process record draft", "return draft", "needs candidate"], bot: { allowed_actions: ["write a process record, blind to the other author"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PSPA", full_name: "PPD Second Process Author", role: "Second Process Author", parent: "[ORG]POD-PPW", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PSPA", cases: "11, 16, 39-45, 78-82, 86, 91" }, ai_in: ["architecture entry", "release elements", "Input Pack atoms"], ai_out: ["process record draft", "return draft", "needs candidate"], bot: { allowed_actions: ["write a process record, blind to the other author"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PPR", full_name: "PPD Process Reconciler", role: "Process Reconciler", parent: "[ORG]POD-PPW", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PPR", cases: "39, 41" }, ai_in: ["two locked drafts", "difference register", "the atoms and elements the drafts cite"], ai_out: ["reconciled process record", "the dispositions of the difference register"], bot: { allowed_actions: ["reconcile two locked drafts, disposing each difference with its reason"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PPB", full_name: "PPD Position Builder", role: "Position Builder", parent: "[ORG]POD-PPS", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PPB", cases: "12, 20, 46, 47, 52, 77, 85" }, ai_in: ["written processes", "role register"], ai_out: ["position register draft", "return draft"], bot: { allowed_actions: ["group steps and decisions into positions, with reasons"], ask_first_actions: ["anything outside its role card"] } }
    - { code: "[ORG]CELL-PSD", full_name: "PPD Structure Designer", role: "Structure Designer", parent: "[ORG]POD-PS", type: "AI Agent", filler_kind: "ai", test: { id: "TEST-PPD-PSD", cases: "14, 53-56, 87, 88" }, ai_in: ["position register", "release parts and governance", "Input Pack atoms"], ai_out: ["reporting lines", "forum register", "crosswalk"], bot: { allowed_actions: ["propose reporting lines and forums", "draft the crosswalk"], ask_first_actions: ["anything outside its role card"] } }
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
    - { code: "[ORG]POD-PS", full_name: "PPD Structure", type: "AI Pod", inner_units: ["[ORG]CELL-PSD", "[ORG]CELL-PWA"], top_cell: "[ORG]CELL-PSD", test: { id: "TEST-PPD-PS", cases: "14, 15, 53-58, 87-90" }, ai_in: ["position register", "written processes"], ai_out: ["reporting lines", "forum register", "crosswalk", "workload input check"] }
    - { code: "[ORG]POD-PW", full_name: "PPD Walkthrough", type: "AI Pod", inner_units: ["[ORG]CELL-PSA", "[ORG]CELL-PSW"], top_cell: "[ORG]CELL-PSW", test: { id: "TEST-PPD-PW", cases: "17, 59, 60" }, ai_in: ["walk input", "blind brief"], ai_out: ["walkthrough report"] }
    - { code: "[ORG]POD-PR", full_name: "PPD Review", type: "AI Pod", inner_units: ["[ORG]CELL-PBRA", "[ORG]CELL-PBRB", "[ORG]CELL-PBRC", "[ORG]CELL-PBRD", "[ORG]CELL-PBRE"], top_cell: "[ORG]CELL-PBRA", test: { id: "TEST-PPD-PR", cases: "22, 61-63" }, ai_in: ["review packet"], ai_out: ["review cards and positions"] }
```

- **Accountability.** Every Pod and Cell of this AIOC is `accountable_to` `[ORG]CELL-PDL`. The AIOC itself and the Design Lead are `accountable_to` the Cell carrying `[ORG]HOAC-TM`.
- **Adding a HOAC position.** The organisation may add HOAC positions to this AIOC in its own design, each a human Cell with a HOAC label and its own fixed test, through OCO (`create-or-install-unit`).
- **Bots.** Each AI Cell's bot (sixteen) has its own identity card, its own credential, `never_signs: true`, and its memory sealed on a change of filler (Protocol §10, item 3). The credential IDs in `cards/bots/` are placeholders.
- The Requesting Authority, the Chief of Staff of `[ORG]AIOC-SL` and the Cells of `[ORG]AIOC-TOM` are not Cells of this AIOC.

**Code checks** (Naming Standard R15 and §5), recorded on 15 October 2026. Each organisation repeats the check of §5.2 against its own register before first use.

| Code | Initials of the full name (R15) | §5.1 | §5.2: no match among this blueprint's codes, nor with `[ORG]AIOC-PPD` | §5.3 |
|---|---|---|---|---|
| `[ORG]CELL-PDL` | **P**PD **D**esign **L**ead | pass | pass | pass |
| `[ORG]CELL-PCS` | **P**PD **C**hief of **S**taff ("of" skipped) | pass | pass (distinct from `[ORG]CELL-TCS` and `[ORG]CELL-SLCS` of other AIOCs) | pass |
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

**A.1 Release-reading record** (run record). One row per element of the release in scope: `element_id` (`ROLE-n`, `HO-n`, `CPR-n`, a capability, a value-stream phase or a decision domain), `part`, `child`, `state` (`used`, `returned`, `out of scope`), `used_by` (process IDs, after S2), `return_id` (when returned), `reason` (when out of scope).

**A.2 Process architecture** (release part). Per entry: `id` (`L1-n`, `L2-n` or `PRC-n`), `level` (1, 2, 3), `name`, `parent`, `traces_to` (release element IDs; at least one for level 1), `owner_role` (`ROLE-n`, level 3), `owner_position` (`POS-n`, level 3, after S5), `carries` (`HO-n` and `CPR-n`), `critical` (yes or no, with `reason`), `order`, `current` (the current processes from the sources it replaces, for the crosswalk).

**A.3 Process record** (one per process; release part "process book"). `process_id`; `purpose`; `trigger`; `end`; `lanes` (roles); `steps[]`: {`step_id`, `lane`, `action`, `input`, `output`, `accountable_role`, `decision_id` (or none), `volume` {value, unit, per, basis, `peak` {value, period, basis} or none}, `step_time` {value, unit, basis}, `wait_before` {value, unit, basis}, `done_when`, `worst_error` {description, `reversible` (`yes`, `partly`, `no`), basis}, `act_kinds` (from the fixed list of §5.4, rule 11), `input_source` {kind, `trust` (`verified`, `unverified`), basis}, `confidentiality` (a class of the organisation's classification), `risks` (risk IDs), `controls` (control IDs), `record` {name, basis}}; `decisions[]`: {`decision_id`, `question`, `decides` (one role), `recommends`, `must_agree`, `gives_input`, `carries_out`, `limit` {value, basis}}; `exceptions[]`: {`trigger`, `handling`, `escalates_to` (role)}; `risks[]`: {`risk_id`, `what`, `at_steps`, basis}; `measures[]`: {`name`, `kind` (`quality`, `time`, `cost`, `volume`), `definition`, `unit`, `basis`, `target` (a decision reference, or `not set`), `reviewed_by` (forum ID, after S6)}; `variants[]`: {`variant_id`, `applies_to` (an entity, a site or a product), `differs_at` (step IDs), `reason`}; `end_to_end_time` {value, unit, path (step IDs), complete}; `conventions` (the modelling conventions in force and their results); `method_refs` (reference models used as methods, never as evidence); `policies[]` (policy IDs); `hand_offs` (`HO-n`, `CPR-n`, and the lane hand-offs inside the process); `authors` (one, or two with the difference register's ID); after T9: `owner_position`, `approved_by` (decision reference), `re_approval_due`.

**A.4 Policy register** (release part; compiled by code). Per policy: `policy_id`, `name`, `applied_at` (step IDs), `owner_role`, `basis` (source atom), `state` (`held`, or `needed` when no source holds it). No policy text.

**A.5 Position register** (release part). Per position: `position_id` (`POS-n`), `title`, `role` (one `ROLE-n`), `part` and `child`, `holds_steps`, `holds_decisions`, `grouping_reason` (same expertise, same counterpart, same location, same decision chain, or the release's own grouping), `job_family` and `level` (each with its basis, or `not given`), `reports_to` (`POS-n`, after S6), `forums` (after S6). Never: a person, a pay amount, or what fills the position.

**A.6 Job descriptions** (release part; generated by code, one per position). `position_id`; `title`; `job_family` and `level` (as in A.5); `purpose` (from its processes' purposes); `accountabilities` (from its steps); `decisions` (with their limits); `works_with` (positions at its lane hand-offs); `measures` (from its processes' measures for its steps); `competences` (each a knowledge or skill, with the steps and decisions it serves); `reports_to`; `trace` (every line to a step or decision). The release lint fails any field that does not trace.

**A.7 Decision-rights register and authority matrix** (release parts; generated by code). Register: one row per decision: `decision_id`, `process_id`, `decider` (`POS-n`), the other parts by position, `limit`, `basis`. Matrix: positions by decision class, each cell the part the position plays, generated from the register.

**A.8 Structure** (release parts). **Reporting lines**: `position_id`, `reports_to`. **Organisation charts**: generated from the lines, one per part of the release. **Span and layer report**: per manager position, its span; per part, its layers; each value against the configured range, with findings. **Forum register**: per forum, `forum_id`, `purpose`, `decides` and `advises` (decision IDs), `members` and `chair` (`POS-n`), `tier`, `cadence`, `reviews` (measure names), `inputs`, `outputs`. **Review calendar** (generated): per forum and period, the measures it reviews. **Result lines**: per part, `result_line`, with its basis. **Crosswalk**: per current unit, position or process named in the sources: `current_ref` (source atom), `maps_to` (target IDs), or `state` `retired` or `not mapped`, with `reason`.

**A.9 Workload register** (release part; generated by code). Per position: `position_id`, `period`, `time_needed` (sum of volume × step time over its steps), `time_available` (with its basis), `steps` (the terms of the sum), `complete` (no when any term is a gap), `gaps`.

**A.10 Decision Package** (release part). A plain summary; the elements for decision, each with its row; the unknowns, the assumptions and the open returns, in plain words; the control gaps and the separation breaches; the span and layer findings; the structure scenarios side by side, when there are any; the peak findings; the walk's findings and their choices; the quality checks.

**A.11 Controls catalogue and segregation-of-duties rules** (release part; compiled by code). Per control: `control_id`, `objective` (the risk IDs it answers), `kind` (`preventive`, `detective`), `at_steps`, `performed_by` (`POS-n`, after S5), `evidence` (the record it leaves), `frequency`, `basis`. Per rule: `rule_id`, `conflict` (two classes of step or decision one position may not hold together, for example start and approve, keep and record, record and reconcile), `basis` (a source or a decision). Check, after S5: per position, each rule it breaks, with any compensating control and the decision reference.

**A.12 Objectives cascade** (release part; generated by code). Per goal: `goal` (a decided goal the release carries, or one a source gives), `value_stream_measures`, `process_measures`, `position_measures` (by `POS-n`), each link traced. Findings: a goal with nothing under it; a measure that serves no goal.

**A.13 Structure scenarios** (release part, when `structure_scenarios` is above one). Per scenario: `scenario_id`, its reporting lines, and side by side: positions, management positions, spans, layers, `cost` (`not given` without the organisation's cost rates); `chosen` (the decision reference of the one chosen).

**A.14 Peak-load check and value-stream times** (release part; generated by code). Per position: `peak_period`, `time_needed_at_peak`, `time_available`, `terms`, `complete`, findings. Per value stream: `end_to_end_time`, `processes`, `complete`.

**The manifest.** `release_id` (`PPDREL-` + SHA-256 of the manifest body); `run_id`; `tom_release` {`release_id`, `manifest_sha256`}; `parts[]` {name, sha256}; `input_packs[]`; `returns[]` (return IDs with their states); `decided_at`; `final_status`.

## Annex B. Returns to the Target Operating Model

The return contract is `contracts/release-return.schema.json`. It is the shared contract between this AIOC and `[ORG]AIOC-TOM`, and between this AIOC and the next stage (where this AIOC is the receiver).

| Field | Meaning |
|---|---|
| `return_id` | `PPDR-` and a number |
| `run_id` | this AIOC's run |
| `release` | the TOM Release ID and its manifest hash |
| `kind` | `accepted`, `cannot use`, `contradiction found`, `assumption invalid`, `request kind unsupported` |
| `missing` | for `cannot use`: what is missing, as a fact-type or an element, never a person |
| `elements` | the release parts and element IDs the return concerns; for `accepted`, the whole release |
| `evidence` | release element IDs and source atom IDs, with span hashes; never text |
| `held_here` | this AIOC's elements held until the return is answered |
| `filed_ref` | the reference of its filed copy in `[ORG]AIOC-SL` |
| `status` | `open`, `answered by release`, `answered by decision`, `withdrawn` |
| `answered_by` | the new TOM Release ID, or the decision reference |

**Rules.**
1. A return goes to `[ORG]AIOC-TOM` directly, through the gateway, and its copy is filed into Source Lifecycle with the same hash.
2. A return never changes the release. It asks TOM to answer.
3. TOM answers with a new decided release (a continuation run), or the Requesting Authority answers by decision. Silence answers nothing; the waiting deadlines apply.
4. A return for something TOM should have obtained is a defect of TOM; a return for something only this stage could find is normal (TOM blueprint `v0.4.1`, `docs/CARRIED-RULES.md` §4.4, items 2 and 3).
5. The next stage returns defects of the PPD Release to this AIOC under the same contract.

**Done when.** The return validates; it is sent and filed with one hash; its touched elements show `held: return open`; it ends in a status other than `open`.

## Annex C. Run states and gates

**C.1 Run states.** As §5.0. Endings other than a release: `closed: not admitted` (T0 failed, with each failed condition named); `closed: non-response`; `closed: rejected`; `closed: withdrawn by the Requesting Authority`. Flags on any state, each with its age: `waiting`; `waiting: ruling`; `held: return open` (on the touched elements only); `held: material finding`; `held: connection revoked`; `held: no reviewers`; `held: review budget`. No flag releases the run slot; every ending releases it.

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

## Annex E. What is carried from the Target Operating Model blueprint

This AIOC carries these rules from the blueprint of `[ORG]AIOC-TOM` `v0.4.1` (its writing repository, `<org>aioc-tom`), by section, not by copy. A change there reaches this AIOC only when this annex pins the new version.

| Rule | TOM section | Read here with |
|---|---|---|
| Labels and the honesty ceiling | Annex B | atoms of the organisation's sources; release elements keep their own provenance |
| Patterns are methods, never evidence | Annex B.5 | — |
| The Input Pack, its versions and its trace | §4.3, parts 1 to 3 and 6 to 8 | §4.3 of this blueprint |
| Needs requests, passes and the Missing Report | §5.2 | §5.2 of this blueprint |
| Decision rules: one decision per row; global assent is never approval; "don't know"; the weak-approval signal; delegated, not decided | `docs/CARRIED-RULES.md` §5 | — |
| The return vocabulary | `docs/CARRIED-RULES.md` §4.4 | Annex B of this blueprint |
| The operational walkthrough | §5.7 | "processes, positions and decisions" for "operating model" |
| The Review Panel rule | §5.8, rules 1 to 20 | the review points of §5.9 of this blueprint; "PPD Design Lead" for "TOM Design Lead" |
| Two authors | Annex G | "process" for "child"; "process record" for "design ledger" |
| The engine register | Annex E.12 | — |

*Powered by 49GAION*
