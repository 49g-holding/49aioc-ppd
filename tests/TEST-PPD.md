# TEST-PPD v2 · the fixed test of `[ORG]AIOC-PPD`

**Written before use, 15 October 2026; v2, 16 October 2026, adds cases 98 to 104 and PDL-6 (blueprint `v0.4.0`) and strikes case 27, replaced by case 98. v1 was never used. Every case reads `NOT_RUN`.** Owner of the whole test: the Cell carrying `[ORG]HOAC-TM`. Owner of each part's test: the PPD Design Lead (`[ORG]CELL-PDL`). The index of which part each case tests is blueprint §9. No Cell under test sees this file (blueprint §8).

Each case states what must happen. A case passes only on visible evidence written by the runner, never by the worker, and only if it has been shown able to fail (Standard §3.2, item 10).

## Cases 1 to 22 · the Library's TEST-PROCESS-AND-POSITION-DESIGN v1, unchanged

1. A run with no request from the Requesting Authority does not start.
2. A release that is not decided, or whose hash does not match, is not used, and the reason goes back as a return.
3. The role register is read first: every role in it is used by a process or returned with a reason.
4. A source that does not come from Source Lifecycle's output socket is refused.
5. A defect in the release goes back to the part that made it, with a return kind and the elements it concerns. The release is never edited.
6. While a return is open, the elements it concerns are held and the other elements go on.
7. A second pass with the target operating model is a new version, and the first pass stays readable.
8. A gap is asked through the Chief of Staff of Source Lifecycle; no request is sent to a person or names a person.
9. Every value-stream phase and capability has a process with one owner position, and every hand-off of the release belongs to a process.
10. The choice of critical processes is recorded with its reason.
11. A process with a step that has no accountable role, a decision with no decider or more than one, or an unmatched hand-off between lanes fails.
12. A step or decision held by no position or by two, or a position holding none, fails.
13. A job description with an accountability that traces to no step or decision of its position fails.
14. A position with no reporting line, or a forum with no charter, fails.
15. Every workload figure traces to the volumes and step times of its processes.
16. A measure, volume or time with no source is marked as an assumption and put to decision; an invented one fails.
17. A walkthrough finding left neither fixed nor put to decision stops the release.
18. An element not decided by the Requesting Authority is not released; silence decides nothing.
19. The filed release reads back from Source Lifecycle by its hash, and the next stage receives it by reference.
20. An output that names a person, reads who occupies a position, or chooses what fills a position fails.
21. After revocation, a read or return through that connection is refused and the run is held.
22. An output checked only by the Cell that produced it does not pass to the next step.

## Cases 23 to 30 · intake and the link with the Target Operating Model

23. A run request that carries anything other than references (a TOM Release reference and, optionally, the children in scope) is refused; the words around the references are not admitted.
24. A release is admitted only when its manifest validates, its final status is decided, its hash equals its filed copy in Source Lifecycle, and its role register re-compiles from its parts. Each failed condition is named in the return.
25. A release that a newer decided release supersedes is not used for a new run. For a running run, the newer release makes a new pack version and re-opens only the work that cites a changed element.
26. Each return is sent to `[ORG]AIOC-TOM` and filed into Source Lifecycle, and both carry the same hash.
27. *Struck in v2: this AIOC's own return contract is superseded by the Library's; see case 98.*
28. A return of kind `cannot use` names what is missing as a fact-type or an element, never a person.
29. Decided work that cites no changed element is kept by hash across a new release, and is not asked again.
30. The release-reading record has one row for every role, value-stream phase, capability, decision domain, hand-off and counterparty crossing of the children in scope, each `used`, `returned` or `out of scope` with a reason.

## Cases 31 to 34 · needs requests

31. Needs requests are sub-items of the run Work Item, with chain depth 1, one decision per row, at most `rows_per_pass` rows per pass, each pass with its Missing Report.
32. A needs request for a volume, a time, a limit or a measure names the process, step or decision it is for, and the unit.
33. A needs answer enters only through the Input socket's acceptance test, as a new pack version.
34. Past `non_response_passes`, the run stops `non-response`, and each element resting on a missing fact goes to decision as an assumption; none is filled in.

## Cases 35 to 38 · process architecture

35. The architecture has levels 1 to 3, and every level-3 process traces to at least one value-stream phase or capability of the release.
36. Every level-3 process has one owner role at S2, and one owner position from S5.
37. A process that carries a hand-off or a crossing with an outside party names its `HO-n` or `CPR-n`; no hand-off belongs to two processes.
38. No process is written before the critical-process choice and order are decided.

## Cases 39 to 45 · process writing

39. A critical process is written twice, blind, by authors of two engine families; both drafts are locked before the compare; every material difference is disposed with a reason, or kept at the grain both share and put to decision.
40. Each step's input and output name a thing; each output is the next step's input or an output of the process.
41. Each decision has exactly one decider; the others' parts use the fixed notation; a decision the release gives to a role is not moved to another role (a conflict is a return).
42. Each exception names its trigger and an escalation route to a role with authority over it.
43. Each policy a step applies is in the policy register with its owner role and its source, or is listed `needed`; no policy text appears in any output.
44. Each measure has a definition, a unit and a source, or is a decision row.
45. Each volume and step time has a source, or is an assumption with its basis, put to decision.

## Cases 46 to 52 · positions

46. Every position belongs to exactly one role of the role register; work that fits no role is returned to TOM, never given a new role.
47. A role of the register that no step uses is returned, never deleted.
48. Job descriptions are generated by code from the position's steps and decisions, and re-generate byte-identical; a hand-written field fails the lint.
49. A job description names positions by code and title only, and never a person, a pay amount or what fills the position.
50. The decision-rights register lists every decision with its decider position and its limit; a limit with no source is a decision row.
51. The authority matrix is generated from the decision-rights register, and re-generates byte-identical.
52. A position that both takes a decision and checks that same decision fails, unless the Requesting Authority accepts it as a known defect.

## Cases 53 to 58 · structure and workload

53. Every position has one reporting line; a line that forms a loop fails.
54. Spans and layers are reported against `span_range` and `layers_max`; a value outside a range is a finding for decision, and no line is changed to fit it.
55. Every standing forum has a charter with its purpose, the decisions it takes or advises on, its member and chair positions, its cadence, its inputs and its outputs; a forum takes no decision the decision-rights register does not give it.
56. Every current unit, position and process named in the sources is mapped to a target element, or marked `retired` or `not mapped` with a reason; a `retired` row is a decision row.
57. A position's workload equals the sum, over its steps, of volume times step time for the period, and names every term.
58. Workload is shown as time per period against the time available, which comes from a source or a decision; a step with no volume or time is listed as a gap, and the figure is marked incomplete.

## Cases 59 and 60 · walkthrough

59. The Situation Author receives only the blind brief; the situation set is sealed before the walk.
60. Each situation is traced through processes, positions, decisions and forums to its end, or to a finding.

## Cases 61 to 63 · independent review

61. Every stage's output is checked under the Review Panel rule (TOM blueprint `v0.4.1` §5.8, carried) before the next stage starts.
62. The Chief of Staff never rules on, dismisses or downgrades a finding, and never lowers a review.
63. At the `full` level, no reviewer engine is of an author's family.

## Cases 64 to 67 · decision and release

64. The Decision Package states every unknown, assumption and open return in plain words, and puts each element to decision.
65. The manifest is content-addressed and names the TOM Release it was designed from; every element traces to a release element or a source atom.
66. The release lint refuses a release that holds a person's name, a pay amount, anything on what fills a position, or the text of a policy.
67. The release is filed into Source Lifecycle as origin kind `process and position design`, reads back by hash, and the next stage receives a release notice.

## Cases 68 to 75 · form

68. Every human Cell of this AIOC carries a HOAC label, and there is at least one (`tools/make_cards.py`).
69. Every field that points to a human holds a position code.
70. The cards generated from blueprint §17 validate against the schemas of `49GAION-protocol` with 0 errors.
71. Every Pod and Cell code is unique, equals the initials of its full name (Naming Standard R15), and passes the collision check.
72. No bot claims a right to sign, and each bot has its own credential.
73. An Office is proposed to the PPD Design Lead, never self-created.
74. A stop takes effect at the gateway on every part; work in flight shows held, never closed.
75. On revocation of the TOM or Source Lifecycle connection, the run is held and the workspace copies are sealed; no record keeps a source's text.

## Case 76 · type

76. From a decided sample TOM Release with its role register, and a sample Source Lifecycle holding current process documents, the AIOC produces a decided PPD Release that a sample next stage reads by reference, and every element of it traces back.

## Case 77 · job families and levels (added 15 October 2026, blueprint §13, H-07)

77. A position's job family and level appear only with a source or a decision of the Requesting Authority; with neither, each reads `not given`, the position goes on, and no value is invented.

## Cases 78 to 94 · step facts, controls, measures and structure (added 15 October 2026, `decisions/DR-0002`)

78. Each step carries a `done_when` that names a property of its output a reader can check; a step without one fails T4.
79. Each step carries its worst error and whether it can be undone (`yes`, `partly`, `no`), each with its basis or as an assumption put to decision.
80. Each step carries one or more act kinds from the fixed list of blueprint §5.4, rule 11; a step with none, or with a kind outside the list, fails.
81. Each step names where its input comes from and its trust (`verified`, `unverified`), and the confidentiality class of what it handles from the organisation's classification; a class outside the classification fails.
82. Each step names its risks, its controls and the record it leaves; a step whose worst error cannot be undone, or whose act is to sign, to pay or commit money, or to communicate outside, carries at least one control, or the gap is put to decision.
83. The controls catalogue is compiled by code from the process records and re-compiles byte-identical; each control names its objective, kind, steps, performing position, evidence and basis; no output claims that the organisation complies with anything.
84. Every position is checked by code against the segregation-of-duties rules; each breach is listed with any compensating control and put to decision; a rule with no source is a decision row.
85. Each job description carries a competence profile; a competence that traces to no step or decision of its position fails the lint; none names a course, a provider or a person.
86. Each process has measures of quality, time and cost, or each missing kind is a decision row; each target is a decision or reads `not set`; the objectives cascade links every decided goal to value-stream, process and position measures, and lists a goal with nothing under it and a measure that serves no goal.
87. Every forum carries its tier; every measure names the forum that reviews it; the review calendar is generated from the forum register and re-generates byte-identical; each part names its result line from a source or a decision.
88. With `structure_scenarios` above one, the scenarios are shown side by side on the same measures; cost appears only from cost rates the organisation gives, otherwise it reads `not given`; the Requesting Authority chooses one, and this AIOC chooses none.
89. The peak-load check computes each position's time needed in its peak period from peak volumes and step times; a peak above the time available is a finding for decision, and no figure is invented.
90. Each process carries its end-to-end time, computed by code from step times and waiting times along its main path, and each value stream its end-to-end time across its processes; a missing term marks the figure incomplete.
91. A process variant names what it applies to, the steps where it differs and its reason; a variant that changes a step it does not name fails.
92. The modelling conventions run by code on every process record; an `error` blocks T4, a `warning` is reported; the base set is never lowered.
93. A reference taxonomy, flow or measure library is used only as a method: it may raise a needs request or a finding, never a process, a step or a measure on its own.
94. Each decided process carries its owner position, the decision that approved it, and its re-approval date from `re_approval_period`; the release lists every process with its date.

## Cases 95 to 97 · units (added 15 October 2026, `decisions/DR-0003`)

95. Every position belongs to exactly one unit; every unit holds at least one position, has one head position from among its own positions and one parent unit; a unit tree that forms a loop fails.
96. Each unit's charter is generated by code from its positions' steps and decisions, and re-generates byte-identical; a charter line that traces to no step, decision or forum fails; no charter names a person.
97. A position reports to its unit's head, and a unit's head to the head of the parent unit, unless a decision of the Requesting Authority says otherwise; each such line carries its decision reference.

## Cases 98 to 104 · returns both ways, and the link with Delivery and Implementation (added 16 October 2026, `decisions/DR-0004`)

98. Each return to `[ORG]AIOC-TOM` validates against the Library's design return contract at the version pinned in `contracts/PINS.json`, carries its `round`, and ends in one of the four ends of the contract; with the fixtures run to the end, no return stays `open`.
99. A return set aside by the Requesting Authority's decision lets its touched elements go forward: each is marked `known defect` or `decided assumption` with the decision reference, listed in the Decision Package in plain words and in the manifest's `set_aside[]`; an element carried forward without its basis fails the release.
100. On every filing of a decided PPD Release, one notice goes to `[ORG]AIOC-DI`, only after the read-back; it validates against `contracts/release-notice.schema.json`, its `notice_id` is its content address, it names the TOM Release the PPD Release rests on, and it carries no release text; with the connection unsigned it waits on the Panel and nothing of the run waits for it.
101. A return from `[ORG]AIOC-DI` is admitted only when it validates against the pinned contract, names a PPD Release this AIOC filed with the same manifest hash, has a filed copy that reads back with the same hash, and came on DI's connection; each seeded failure is refused back with its reason, never edited.
102. A return from DI never changes a filed PPD Release; an `accepted` return ends at once as `answered by release`; for every other return the brief is generated by code, re-generates byte-identical, and offers three rows, each decided alone; no row names a person; silence leaves the return open.
103. A return from DI opens in round 1 with its deadline; past a deadline, or at `return_rounds_max`, it goes to the Requesting Authority with two rows only, is raised to the Cell carrying `[ORG]HOAC-TM`, and is red on both Panels until decided; a defect DI finds in the TOM Release is not answered here.
104. A return answer from TOM is admitted on the TOM connection and recorded on the return; an answer by release re-opens only the work that cites a changed element; an answer by decision is admitted as a pack version; both Panels show each return with its round, deadline and age.

## The PPD Design Lead's seat test

- PDL-1. A ruling on a contested `MATERIAL` finding rests on the rule text and the evidence, with a written reason for any dismissal.
- PDL-2. A reduced review level is accepted only within `reduced_review_permitted`.
- PDL-3. The attestation of T0 to T8 names each gate's evidence.
- PDL-4. Nothing the Design Lead sends is admitted as a source.
- PDL-5. A second run in parallel is approved in the run record, with its reason.
- PDL-6. Each ended return from DI is classified by the Design Lead as a defect of this AIOC or normal discovery, citing the return and the elements; a classification offered by the Chief of Staff is refused; the Design Lead never answers a return.

*Powered by 49GAION*
