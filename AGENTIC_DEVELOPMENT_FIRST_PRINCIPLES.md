# First Principles for Reliable Agentic Development

A domain-agnostic set of tenets for building software with autonomous or
semi-autonomous coding agents, where an orchestrating agent plans,
implements, and reviews work across long sessions with minimal human
input. These principles are the distilled, transferable core of a
workflow that survived contact with real failure modes. They assume
nothing about the project's purpose, language, or domain.

The document is organized as numbered tenets grouped into themes. Each
tenet states the principle, the reasoning, and — where the principle
exists because something broke without it — the failure it prevents.

---

## Theme A — Where truth lives

**A1. Enforce in the pipeline what cannot afford to be "mostly followed."**
A rule expressed only as prose instruction to an agent is a suggestion the
model may interpret loosely. A rule expressed as a deterministic check
(a script, a test, a git hook, a CI gate) is enforced. Decide for every
rule: if violating it should block progress, it belongs in the pipeline;
if violating it should merely raise an eyebrow, it belongs in prose.
Never use prose as a substitute for automated enforcement of a
non-negotiable.

**A2. Decisive truth lives in artifacts, not in code shape — and never in
the agent's own claim of completion.**
When you must guarantee a semantic property ("X is always true of the
output"), verify it on the actual emitted artifact, not by inspecting the
source that produces it. The artifact is finite and decidable; the space
of source code that could produce it is not. A check that reads the
produced file and asserts the property is total and evasion-proof; a
check that tries to prove the property from the code can always be
evaded by a construction it didn't anticipate. The agent's explanation of
why its work is complete is never evidence — evidence is an external check
the agent cannot talk its way around. This is the boundary of trust:
everything the agent asserts is a claim until a verifier it does not
control confirms it.

**A3. The evidence trail is the shared memory.**
Every plan, review, verdict, and decision is written to a durable,
version-controlled location, not held in conversation. This is what lets
a session be resumed, audited, handed to a different agent or runner, and
reasoned about after the fact. If it isn't written down in the repo, it
didn't happen. Conversation is ephemeral; the repo is the system of
record.

**A4. Instructions an agent must always honor must reload after
compaction.**
Long sessions compact or truncate context. Any rule the agent must obey
throughout must be re-injected from disk after compaction, not given once
in conversation. Put durable rules in the files the runtime guarantees to
re-read; never rely on a rule stated only in an early message surviving to
a late one.

The same boundary degrades _state_, not just rules. Every task-state claim
carried across a compaction — a task list, a summary, a remembered
"already done" — is a hypothesis until re-grounded against the artifact.
This matters most precisely when it is hardest: under context pressure, the
carried list becomes the only apparent truth at exactly the moment it is
least trustworthy.

**A5. Separate storage from presentation; the live artifact is the
control surface.**
Durable evidence — logs, plans, verdicts, metrics, decisions — lives in a
structured store the agent can search (markdown, a vault, version
control). A separate presentation layer renders that state into a live,
human-readable artifact (a dashboard of progress, costs, recent
decisions, and check results). The split matters because the two
consumers differ: the agent reads the store, the human watches the
artifact. The rendered artifact is not a report written after the fact —
it is the control surface from which a human decides _when to intervene_
in a long autonomous run. Terminal transcripts do not scale to several
sessions in parallel; a rendered state surface does. Build the surface so
supervision is a glance, not an archaeology.

**A6. Every projection of state is a claim with a timestamp; only the
system of record is truth.**
A2 says the agent's explanation is not evidence. The harder version is that
the agent's own _bookkeeping_ is not evidence either: the task list, the
rendered dashboard, a status label from the control plane, a subagent's
summary, a prior session's note, even the operator's recollection that
something was implemented. Each is a projection that was true when written
and may not be now. The rule that makes this operational: a state may be
recorded as done only with an inline citation of the ground truth read —
the exact path plus the value, line, revision, or count observed. No
citation, no closure. And never collapse the three states of delegated
work: _dispatched_, _returned_, and _verified-done_ are different facts, and
a completion notification advances only the second. The first action on any
completion is to read the named artifact, not to believe the summary that
announced it.

**A7. Verified where it is cheap is not verified where it matters.**
A check that passes in the repository does not establish that the thing
works in the environment it must work in. Rather than let that gap hide
inside a binary pass/fail, give it a name — the honest verdict is
"repository-green, deployment-pending," and it is not acceptance. Any
contract whose value depends on a deployed target must draw its evidence
from that target. The vocabulary matters: a verdict that cannot express
"proven in the wrong place" will be reported as proven. Give the ladder
explicit rungs — built, installed, activated, observed working — because
each is a distinct state and a single pass/fail flattens all four into the
most flattering one. What must match is the real thing: the operating
system, the process model, the loaded path, the configuration generation
actually in effect. Committed source is not deployed behavior.

**A8. A negative claim requires a baseline recorded before the change.**
"Nothing outside scope was touched" cannot be established after the fact. A
manifest captured post-change proves only a future baseline; it says nothing
about history. Capture the pre-change state of every protected surface the
work declares it will not touch, then compare. This applies to
configuration, schedulers, allowlists, and reviewer material — not just the
directory that was edited. Evidence of absence is the one kind of evidence
that cannot be produced retroactively.

**A9. Verification must not write to what it measures.**
A test that exercises a metering path, a budget counter, an alerting spool,
or an observability signal must be bound to an isolated state root, and the
production signal asserted byte-identical before and after. Otherwise the
act of verifying corrupts the record that verification depends on — and the
corruption is invisible, because the fixture's own rows look exactly like
real ones. When residue is found, treat it as an integrity defect in the
live signal: purge only positively identified fixture rows, record counts
and checksums, and recompute anything derived from the cleaned source.

**A10. Final state does not establish history.**
A check that reads only the end state cannot distinguish work that was done
correctly from work that was done wrongly and then tidied — staged and
reverted, written and overwritten, run twice with the first result
discarded. Where the honest sequence matters, verify the sequence: bind
evidence to the specific execution that produced it, to a digest of the
artifact as it stood, and to the generation of the system it ran against.
Evidence that floats free of when and where it was produced can be
re-presented later against a different artifact entirely.

**A11. When reconstructing what happened, preserve the unknowns.**
Reconstruction under pressure tends to resolve every gap into a confident
narrative, because a matching count or a plausible name feels like an
identification. It is not one: a count proves cardinality, not identity, and
a heuristic match proves resemblance. Carry gaps forward as gaps. A
reconstruction that reports no unknowns is usually a reconstruction that
overwrote them, and it will be trusted more than the direct evidence it
replaced.

---

## Theme B — Separation of powers

**B1. The author of a check is not the implementer of the thing checked.**
If the same agent writes both the implementation and the test that
validates it, the test degrades into a description of whatever the code
happens to do. Separate the roles: one agent (or pass) authors the
acceptance checks against the specification; another satisfies them. The
implementer must not be able to edit the checks.

**B2. Tests-first inverts, but does not remove, the tautology risk — so
defend both directions.**
Writing tests before implementation prevents tests-fit-to-code, but
introduces code-fit-to-tests: an implementer can hardcode the test
inputs' expected outputs. Neither sequencing is safe alone. Defend with
layers: prefer invariant/property/cross-path tests over specific-value
tests (they cannot be satisfied by hardcoding a finite input set); have
an adversarial pass attack the implementation with inputs outside the
test distribution; have an independent reviewer ask "would a competent
practitioner have written this, or is it fitted?"; and re-run
verification against real data, not the test corpus. The goal is not to
make cheating impossible but to make honest implementation cheaper than
cheating.

**B3. Tests bind; reviewers certify; the specification is the truth.**
Passing tests is necessary, not sufficient. Truth-establishment comes
from reviewers certifying the work against the specification, not from a
green test suite. Tests are a regression floor and an implementation
contract; they are never the spec. An implementation that satisfies every
test but fails review has failed.

**B4. Disputes route through an arbiter with the burden of proof on the
challenger.**
When the implementer believes a check is wrong, it does not edit the
check. It files a dispute that an arbiter rules on, and the default
ruling is "the check stands." Without a compelling, specification-grounded
argument, the check holds. This keeps the separation of powers from
collapsing the first time it's inconvenient.

**B5. A consolidating judge decides; reviewers find.**
Multiple specialized reviewers attack the work from independent angles;
a single judge consolidates their findings into one verdict. The judge
adds no findings of its own (anything reviewers missed becomes a note for
the next cycle), and the reviewers do not each get a veto. This prevents
both the diffusion of responsibility and the deadlock of equal voices.

**B6. Independence is a runtime property, and infrastructure can revoke it
silently.**
Two roles declared independent in a design document can collapse into one at
execution time: a provider fallback routes both to the same model, a resume
reuses the implementer's session, a retry inherits custody of the checks.
Nothing announces this. So record the _actual_ identity on every committed
piece of evidence — which profile, which session, which model and provider
authored it and which reviewed it — and fail closed when that attribution is
unknown. What must stay distinct is structural: separate sessions, separate
custody of the checks, held-out material the implementer cannot reach.
Unknown attribution is a defect; a shared but declared and controlled route
is not.

**B7. The apparatus that grades the work is not self-actuable — even when
the change is plainly a strengthening.**
An implementer may improve the thing it is measured by only through the
party that owns the measurement. This holds for a fix that is obviously in
the tightening direction, because "obviously correct" is exactly the
judgment the separation exists to remove. It also holds for the _inputs_ of
a protected check: migrating a fixture is editing the spec you are graded
by, not housekeeping. The boundary is clean — a strengthening guard on the
_work_ can be self-applied; a change to the instrument that _grades_ the
work routes to the grader, who verifies both directions: that it now
catches what it claims, and that it does not newly block valid work.

**B8. Never shape the reviewer's question to obtain the verdict you want.**
Framing is a way of rigging. Telling a judge to treat a disputed behavior as
"pending governance," scoping a review so the contested surface falls
outside it, or handing over only the evidence that supports the claim
corrupts the seam more thoroughly than a bad verdict would, because the
result looks clean. Relatedly: the absence of a prior verdict is not
permission to write the favorable one. An acceptor that finds no record
proceeds to verify; it does not record a pass.

**B9. Role separation must be structural, not verbal.**
A worker that boots with the supervisor's identity will supervise: it
clarifies, re-frames, and re-delegates instead of doing the work, and no
amount of stronger task wording overrides the inherited disposition. If a
unit needs implementation, dispatch it to something whose identity is an
implementer's — a focused leaf that cannot escalate or re-delegate, or a
dedicated executor. Never dispatch a supervisor to itself: it manufactures
no independence and produces a twin, not a worker.

**B10. A degraded path is a different product and cannot satisfy the real
path's acceptance.**
When the required dependency is missing, the tempting move is a fallback: a
stub, a synthetic mode, a native substitute, a path that skips the hard
integration. That fallback may be a legitimate product decision, but it is
never evidence for the primary path, and a suite that only ever exercises it
proves nothing about the thing being accepted. So state which path acceptance
requires, require it end to end, and make the executor install what it needs
rather than silently succeeding in a reduced mode. Work that passed only
through the degraded path is reverted, not patched — remediating it starts
from the false premise that it was nearly right.

**B11. After a fabrication, revoke trust by provenance class, not
wholesale.**
Discovering that one claim was invented poisons a category of evidence, not
the entire record, and the two overcorrections are equally costly: keep
trusting everything from that source, or discard independently reproduced
facts along with the fiction. Draw the line at provenance — void what rests
on the actor's own self-attestation, retain what an independent check
confirmed. Then re-derive the voided set rather than assuming it was
probably fine.

---

## Theme C — Bounded review and convergence

These are the tenets whose absence caused a multi-agent review loop to run
without converging. They are the most important and most counter-intuitive
in the document.

**C1. A semantic property of program behavior cannot be decided by static
inspection — so never assign that job to a static checker.**
Whether a program computes or persists some value is, in general,
undecidable from its source (Rice's theorem is the formal statement; the
practical statement is that a determined constructor can always write
another evading shape). A reviewer mandate of "any construction that
evades this static check is a defect" therefore has no fixed point and
diverges: every fix creates fresh surface for the next evasion. Semantic
properties are enforced at the artifact layer (A2) or the type layer
(make the bad state unrepresentable); static checks are diagnostic
tripwires only.

**C2. A checker has a closure contract, and its obligation ends there.**
Define explicitly, in advance, the finite set of shapes a check must
catch: the shapes named in the plan, plus any shape actually present in
the codebase or named in prior findings. Once a check rejects its
contract shapes and passes its offender suite, it is CLOSED. Constructible
shapes beyond the contract are notes for future work, never blocking
findings, and are never answered by extending the checker. A checker that
grows past a small size ceiling to chase evasions is itself a defect — the
invariant it strains to prove belongs at a different layer.

A verifier fails in two opposite directions, and the closure contract is
what holds it between them. A _vague_ verifier lets the agent satisfy the
easiest interpretation of the task — it under-specifies, so plausible-
looking work passes. A _too-narrow_ verifier invites the agent to overfit
to it and miss the broader intent — it over-specifies one shape, so work
that games that shape passes. Layered verification (C-theme plus B3)
addresses both: cheap deterministic checks set a precise floor, and a
higher-level judgment review guards the broad intent the floor cannot
express.

**C3. Severity is graded by reality, not by hypothesis.**

- A defect present in the actual artifact/tree, or a failing committed
  check, or an unmet contract: blocking.
- A synthetic construction that evades a check but is absent from the
  tree: non-blocking follow-up at most, and consolidated to one finding
  per check (not one per construction).
- A construction no honest implementer would realistically write:
  a note at most, never a gate.
  Reviewers propose severity; the judge normalizes it against this law.
  A reviewer's label is an input, not a verdict.

**C4. Remediation is regression gating of named findings, not re-attack.**
When a cycle fails and remediation begins, the gate for the next cycle is
exactly "the named findings are closed and nothing regressed" — not "no
reviewer can find anything new." Each cycle's open set must be a subset of
the prior cycle's named set. Newly discovered issues are filed as future
work (the way a new ticket would be), not folded into the current loop.
Regression gating and exploratory testing are different activities;
conflating them makes loops non-terminating.

**C5. Detect divergence by finding-class, not finding-identity.**
A loop where each cycle produces a _novel instance_ of the _same kind_ of
finding is diverging, even though no single finding repeats. Detect this
by class ("another evasion of the same checker," "another instance of the
same category") not by exact identity. The naive "same finding twice"
trigger never fires on a creative adversary.

**C6. Adjudicate a recurring class once, and bind the ruling forward.**
The second time a finding-class recurs, the judge rules on the _class_
(its severity, its correct enforcement layer, its disposition) rather than
processing another instance. The ruling binds all later cycles: further
instances of an adjudicated class are recorded under the ruling and do not
re-gate. This is the structural mechanism that converts a potential
infinite loop into a bounded one — apply it at the second occurrence, not
the thirteenth.

**C7. Convergence guarantees must survive a human override.**
If an operator removes a cycle cap to "let it finish," that must not
remove the convergence contract. Unlimited cycles never means unlimited
re-attack. The class-adjudication and regression-gating rules hold
regardless of caps; the cap is a safety limit, not the thing keeping the
loop bounded.

**C8. The system must not depend on any single agent behaving perfectly.**
Reliability comes from structural backstops (closure contracts, class
rulings, block counters, artifact-layer enforcement), not from trusting
that the adversarial reviewer will show restraint or the judge will
normalize correctly every time. Design so that a miscalibrated agent
costs you bounded extra cycles, never an unbounded loop or a silent
escape. This is also what makes the workflow portable across models: you
are relying on the structure, not on a specific model's disposition.

**C9. Bind every fix to the declared property, never to the failing
instance.**
The characteristic remediation defect is the same bug one level up: shown a
failing case, the implementer satisfies _that case_ rather than the property
the case was an instance of. It is most damaging on a two-sided property —
a guard that must both reject the unsafe input and admit the valid one, a
filter that must both block and pass. Over-tightening to close the failure
breaks the other side and produces a fresh failure that looks new and is
not. So state both obligations explicitly in the remediation instruction,
say plainly that satisfying one by breaking the other is not a fix, and
forbid weakening the check. Pre-empting this costs a sentence; discovering
it costs a cycle.

**C10. A finding fixable only outside the unit's editable surface is a
specification escalation, not a remediation cycle.**
When the only real fix reaches a protected check, another component, or an
architectural convention, no cycle inside the unit can close it, and
spending one buys a foregone failure. Instruct every remediation to stop and
write a short note — the evidence that no in-scope fix exists, the options, a
recommendation — instead of reaching out of scope. An implementer that
correctly declines has succeeded. The escalated finding returns as a
specification change authored by the check's owner, and that opens a _new_
budget epoch rather than continuing the exhausted one; a re-framed spec is
not a continuation of the loop that failed against the old one.

**C11. When two reviews of the same work disagree, reconcile by cause before
trusting either.**
The newer or cleaner verdict is not automatically right. There are three
separable causes and they have different resolutions: _temporal_ — one read a
stale snapshot, so the later verdict governs; _method_ — one graded the
deliverable's completeness and the other the live capability, so both are
valid and the gaps carry forward as debt, not as capability failures; and
_depth_ — a fan of independent per-unit reviews is more adversarial than one
consolidated multi-lens pass and finds defects the single pass cannot. Depth
is asymmetric: a shallow pass's clean verdict does not retire a deep pass's
finding until you re-probe the claim yourself.

**C12. The class of evidence must match the class of defect.**
A concurrency finding is closed by a real interleaving probe against the
shared target, not by reading the source for a lock. An ordering finding is
closed by injecting the bad state and reading back every store afterward.
A green fixture is evidence only if it actually drives the mechanism the
finding implicated. Otherwise the remediation is verified against a proxy
and the defect survives its own fix.

---

## Theme D — Anti-bloat and anti-drift

**D1. Prefer, in order: delete > replace > refine > add.**
The cheapest correct change is removing something. The most expensive and
riskiest is adding. When fixing a problem, exhaust deletion and
replacement before reaching for new code. Bloat is not a cosmetic concern;
it is accumulated future surface for drift and evasion.

**D2. Localize the cure to the disease.**
When a defect is concentrated in a few files, fix those files; do not
reset or rewrite the surrounding verified work to feel thorough.
Discarding good, independently-verified work to cure a localized problem
trades a small known cost for a large one. Identify the minimal surface
that actually carries the defect and operate only there.

**D3. Every design choice traces to a failure pattern or a principle.**
If you cannot say which concrete failure a piece of process prevents or
which principle it expresses, it is probably ceremony. Process that exists
"to be safe" without a named threat is bloat in the workflow itself.

**D4. Specify exhaustively up front, including negative constraints.**
State not only what to build but what not to do, where the scope ends, and
which adjacent changes are forbidden. Ambiguity is resolved by the agent
guessing, and the guess is drift. The cost of a long, precise
specification is paid once; the cost of an under-specified one is paid
every cycle.

**D5. Scope is declared and enforced.**
Each unit of work declares the files it will touch and the bounds of each
change. A reviewer flags anything in the diff outside that declaration.
"While I was in there" is how unrelated risk enters a change set.

**D6. Make the bad state unrepresentable before you make it detectable.**
The strongest enforcement is a type or structure that cannot express the
defect at all. The next strongest is a decisive check on the artifact.
The weakest is a lint-style tripwire. Spend effort at the highest layer
that can carry the invariant, not the most familiar one.

**D7. Ceremony is proportional to governed materiality.**
The machinery in this document is expensive, and applying all of it to
everything is its own failure. Reserve the full contract-and-review apparatus
for work that genuinely needs governing: new behavior or architecture, an
irreversible change, unresolved decisions reserved for the human, a
cross-runner build unit. Routine cleanup, a bounded restart, deletion of
data already proven disposable, or reconciling a settled fact stays direct.
"A contract _could_ govern this" is not "this _warrants_ a contract," and the
existence of lifecycle machinery does not make an unnecessary invocation of
it appropriate.

**D8. Procedural correctness on the wrong-sized unit is the subtlest drift.**
The most expensive drift is not sloppiness; it is following the process
faithfully while solving something adjacent to the objective. It has a
recognizable signature: an operational blocker gets promoted to the mission,
each review finding grows the unit instead of constraining it, and activity
volume — delegations dispatched, evidence files written, lanes running — is
counted as progress. Stop when the active task no longer begins with the
stated objective, when two units govern the same bounded cleanup, or when
process artifacts multiply without a new decision or acceptance result.
Findings constrain the existing unit; they do not authorize recursively
building a larger program.

**D9. After repeated failures of the same class, revert and re-architect
rather than attempt the next fix.**
There is a point where remediation is more expensive than replacement, and
the accumulated repairs are themselves the liability. Repeated failures of
the same class against the same structure are evidence about the structure.
Discard the work and re-approach; sunk effort is not a reason to keep
refining something that has already told you its shape is wrong. (This is not
in tension with D2 — localize the cure when the defect is localized; reset
when the defect _is_ the arrangement.)

**D10. Context is a budgeted resource, and the supervisor's is the scarcest.**
An orchestrator that spends its own window on source archaeology, bulk edits,
or log reading has less left for the judgment only it can perform, and it
degrades exactly when the work gets hard. Push token-expensive work into
isolated children, keep the supervisor to framing, deciding, and reading the
few decisive artifacts. Relatedly, size a unit so it fits its budget rather
than chopping it into ceiling-shaped fragments or serializing independent
work: raise the bound deliberately, and treat a pathological tail as a
job-shape defect rather than a delivery problem. Treat the window as a data
plane with a capacity, not as an unbounded log: cap what a tool is allowed to
return, put large intermediate results on disk, and pass pointers rather than
replaying payloads. An unbounded result from one careless read can consume
the budget that the rest of the work needed.

---

## Theme E — Phasing and gates

**E0. The goal is a contract, not a prompt.**
Before planning begins, define the unit of work as a contract with four
parts: the desired end state, the evidence required to prove success, the
constraints that must not be violated, and the budget (turn, time, and/or
cost). A prompt invites the agent to do something; a contract gives it a
target it can repeatedly measure itself against and gives you the standing
to reject work that misses. A weak goal leaves room to stop early, take
shortcuts, or redefine success into something that looks plausible in the
transcript but fails in the real system. The budget term is co-equal with
the correctness terms: an unbounded run is as much a failure as an
incorrect one, and cost-runaway is a distinct failure from cycle-runaway
(E4) — name both. The contract is also where domain expertise enters that
the model would otherwise guess: the specific target, the held-out check,
the baseline the result must beat, the reference the output must match.
The model executes; the contract defines what "done" actually means.

**E1. Plan before code, and review the plan before implementing it.**
A reviewed plan is the cheapest place to catch a wrong approach. The
sequence is: produce an explicit plan artifact → independent review of
the plan → only on approval, write checks → implement → review code →
judge. A failure caught at the plan gate costs a paragraph; the same
failure caught after implementation costs a cycle. Planning is where
expertise enters: a generated plan is a draft to be inspected,
challenged, and sharpened — its assumptions surfaced and its success
criteria made concrete — before it is handed to an autonomous loop.

**E2. Every phase transition is a gate with explicit, checkable
conditions.**
Do not advance on vibes. Each phase has machine-checkable exit
conditions, and the session cannot proceed (or cannot terminate) until
they are met. The termination gate in particular should be a small set of
deterministic conditions verified mechanically, not the agent's
self-assessment that it is "done."

**E3. The completion gate makes required outputs structurally
unskippable.**
If a deliverable must always accompany completion (a summary, a matrix, a
provenance record), make the termination gate check for it so the session
literally cannot exit success without it. Anything merely requested in
prose will eventually be skipped under pressure.

**E4. Cap cycles; surface to a human at the cap.**
Bounded remediation cycles with a hard cap, after which the session stops
and writes a structured hand-off rather than grinding. The cap is a
backstop behind the convergence contract (C4–C7), not a substitute for it.

**E5. Surfacing to a human is a first-class, structured exit — not a
failure.**
When the agent hits a condition it should not resolve autonomously (a
genuine ambiguity, a contract conflict, a decision reserved for an owner),
it writes a structured disposition: what state it reached, what's blocking,
what it recommends. This is a normal outcome, designed for, not an error
path.

**E6. De-risk on a cheap subset before the full autonomous run.**
Before committing a long-running loop to the full task, run a small, cheap
slice of it: a single representative case, a reduced dataset, a one-file
version. The cheap run surfaces wrong approaches, missing constraints, and
verifier gaps for a fraction of the cost of discovering them mid-loop. The
full run is launched only once the subset confirms the goal contract and
verifiers behave as intended.

**E7. The outer loop is a first-class control component, and it carries
the convergence guarantees.**
A goal gives direction; a loop keeps the work alive. Models stop before
the task is finished — they hit a turn limit, lose confidence, exhaust
context, or judge a partial solution sufficient. The outer loop is the
control system that prevents silent victory: it wakes, inspects progress,
runs the verifiers, compares the result to the goal contract, and
re-dispatches the agent with the next instruction when the goal is unmet.
Long-running autonomy is repeated effort under a control layer, not one
continuous act of intelligence. Treat the loop as the thing you trust and
the agent as the thing the loop supervises. Critically, the loop is not a
license to re-attack: it carries the Theme C guarantees verbatim —
regression gating of named findings (C4), class-keyed divergence detection
(C5), adjudicate-once (C6), and convergence-survives-override (C7). A loop
without those guarantees is the common blind spot and the source of the
non-terminating failure the C-theme exists to prevent.

**E8. Sequence by reversibility, not by caution.**
Waiting is a cost, and it buys nothing on work that can be undone. Drive
reversible work now — that is how you earn the evidence a real gate needs,
and deferring it merely postpones the discovery. Reserve delay, soak time,
and staged rollout for genuinely irreversible acts: deletions, published
artifacts, migrations that cannot be walked back. The corollary is that a
high-impact but reversible change is legitimate when its verification comes
first, while a small irreversible one deserves the full pause.

**E9. Order the work so a decision precedes the expensive verification it
constrains.**
Before spending a costly review cycle, ask whether its verdict could actually
advance the state. If an unresolved decision would still block completion, or
if the implementation still embodies the disputed behavior, the review will
return contested or become invalid the moment the decision lands. The correct
order is: frame the decision, capture the ruling, implement what the ruling
determines, verify the decisive artifacts, then run one independent cycle
against the resulting tree. When this ordering defect is discovered
mid-flight, cancel the cycle — setup already spent is not a reason to buy a
verdict that cannot be used.

**E10. Budget the amplified cost, not the visible one.**
The intuition that cost tracks output is wrong by orders of magnitude. What
is billed is the accumulated context re-sent on every step, multiplied by the
steps a unit takes, multiplied again by concurrent children and by everything
retried. A run that produces one paragraph can cost more than one that
produces a thousand lines. So express the budget in the terms that actually
bill, make the drivers explicit when authoring, and treat context-multiplying
choices — fanning out wide, resuming a long history, disabling reuse of a
cached prefix — as budget decisions rather than mechanics. Cost runaway is a
distinct failure from cycle runaway (E0), and it is the one that arrives
without warning.

---

## Theme F — Specialized review competence

**F1. At least one reviewer must hold domain/practitioner judgment, not
just rule-conformance.**
Mechanical gates catch mechanical violations. They cannot catch work that
satisfies every rule and is still wrong by the standards of someone who
actually does this work. One reviewer must be equipped with that
domain-expert judgment and must ask "is this how a competent practitioner
would build it?" — independent of whether it passes the checks. (The
domain knowledge here is project-specific; the requirement that such a
reviewer exist is universal.)

**F2. An adversarial reviewer must actively try to break the work, with
reproducible evidence.**
Distinct from the reviewer who checks conformance, one role assumes the
implementer cut corners and tries to prove it: attack the claims, run the
code on hostile inputs, attempt the evasions. Every finding it raises is
backed by a reproduction, not speculation. Its mandate is bounded by the
severity law (C2–C3) so it attacks toward convergence, not toward an
arms race.

**F3. Reviewers run with independent context.**
The value of multiple reviewers comes from their independence. Running
them in parallel with separate context windows preserves it; piping one's
output into another's input collapses three opinions into one. Independent
isolation is the point, and it is also why specialized review scales.

**F4. Novel failure modes are absorbed by the review layer, not by piling
onto the durable rules.**
When a new kind of failure appears, the response is to teach the relevant
reviewer or judge to catch it (and, if it recurs across units of work, to
give it a named gate). The response is not to reflexively append another
line to the always-loaded rules file, which grows without bound and
dilutes adherence. Workflow discipline lives in the review prompts;
durable runtime rules stay small. (The routing of a recurring failure to
its correct home — which sometimes _is_ the durable rules file — is
governed by F6.)

**F5. Match the evaluator type to the crispness of success.**
Choose how to verify by how cleanly success can be expressed, and decide
this before building the verifier. When success is crisp — a property that
can be stated as an assertion — use deterministic checks: type checks,
unit tests, lint rules, integration tests, benchmark scripts. They are
cheaper, faster, and not subject to the evaluator's own judgment errors.
When success is genuinely fuzzy — coherence, faithful adherence to an
intent, a match to a design that resists assertion — only then reach for
an agent or judgment-based evaluator, which brings language, reasoning,
and sometimes vision. The standing pattern is deterministic checks as the
floor and judgment evaluation as the higher layer; do not promote a fuzzy
evaluator to do a job a deterministic check could express, and do not
force a crisp assertion onto a problem that genuinely needs judgment.

**F6. Mine past sessions for recurring failures and promote each to its
correct enforcement home.**
Past session transcripts are workflow data, not exhaust. As a standing
operational practice, periodically scan recent sessions for recurring
failure modes — the same check forgotten, the same wrong path taken, the
same command retried, the same tool misused — and promote each recurring
pattern into a durable improvement so it cannot recur silently. This is
how a harness gets smarter without retraining a model: targeted, specific,
project-local improvements are what move the needle, not generic advice.
The orchestrator itself may drive this mining-and-improvement step on a
standing basis; the discipline is identical whether a human or the
orchestrator performs it.

The promotion must be _routed to the right home_, which is what reconciles
this practice with F4 and A1. Diagnose the failure's nature, then route:

- **Expressible as a check** → a deterministic check or a reviewer rule
  (enforced, scoped, no dilution). This is the default route and the one
  that most reliably moves the needle.
- **A failure of recall or context** → a memory/instruction improvement:
  a sharpened always-loaded rules file (the durable project/agent
  instructions), a clarified skill or tool-usage instruction, or a recall
  fix. Use this route only when the failure must shape behavior pervasively
  and cannot be expressed as a check, and even then keep it within a size
  budget (F4, A4).
- **A failure of orchestration** → a fix to the harness itself: tool-call
  conventions, tool or MCP tool definitions, sub-agent routing, or the
  orchestrator's own configuration.
  The aim across all three routes is the same: identify the recurring
  pattern, move it to the layer that can enforce or prevent it, and keep the
  always-loaded surface small while making the local environment measurably
  smarter.

---

## Theme G — Portability and the human seam

**G1. Separate contracts from orchestration.**
The durable assets — specifications, review prompts, checks, gates, the
evidence format — are runner-neutral. The mechanics of launching,
spawning sub-agents, and enforcing termination are runner-specific. Keep
them apart so the contracts move to a new tool, model, or environment
unchanged, and only a thin adapter is rewritten.

**G2. Single source of truth; adapters are pointers.**
When the same prompt or rule must be referenced from multiple places, the
references point at one canonical file; they do not copy it. Duplication
is drift waiting to happen — two copies will diverge, and then which is
authoritative is undefined.

**G3. Cross-model/cross-runner behavioral identity is earned by one
supervised run, never asserted.**
Contracts transfer mechanically; behavioral calibration of judgment-bearing
prompts does not transfer by assumption. The first run on a new model or
runner is supervised against explicit signals (does it apply the severity
law, does the gate loop produce progress, is orchestration faithful). Two
clean supervised runs earn "trusted"; before that, "it should work" is a
prior, and the workflow's own epistemics demand the posterior. For a
judgment-bearing role specifically, require more: a candidate must clear
non-regression against a seeded library of the failures its predecessor
caught before it inherits the role. A reviewer has to out-judge the work it
grades, and that is a measurable claim, not an assumption about capability.

**G4. Role is an architecture decision; route each role to the model that
is best at it.**
Stop treating "the model" as a single choice. Planning, execution, and
evaluation are distinct roles with distinct demands: some models plan and
reason about constraints better, some execute and generate code better,
some evaluate or review more cheaply or with vision. A good orchestrator
lets you assign each role to the model suited to it and swap them
independently. Role-to-model routing is a deliberate architecture decision,
expressed in configuration and changeable without touching the contracts
(G1).

**G5. The human's standing role is decisions, not labor.**
Design so the human's recurring involvement is approving, choosing between
genuine alternatives, and ruling on reserved decisions — never manual
mechanical work the pipeline should do. Per unit of work the human should
have a small, fixed number of decision points, with everything between
them automated. If the human is doing rote work, that work belongs in the
pipeline.

**G6. Reserve genuinely-owner decisions for the human, explicitly.**
Some decisions (irreversible choices, definitional/policy calls, anything
where being wrong is expensive and judgment is required) are not the
agent's to make. Mark these as surface-to-human triggers up front. The
agent's job there is to frame the decision well, not to make it.

**G7. One unit of work, one runner, start to finish.**
Do not switch the executing tool mid-unit. If a session is handed off or
resumed, treat the resume as reading the committed evidence trail (A3)
and continuing from there — the evidence is the shared state precisely so
hand-offs are clean.

**G8. Absence of an answer is not an answer.**
A timed-out question, a default, or a wrapper replying "use your best
judgment" does not transfer decision authority. Do not choose a branch, do
not record a provisional ruling (persisting it makes an unauthorized choice
look settled to every later session), and do not author work whose validity
depends on the unchosen branch. Record the decision surface, hold, and
continue only what is valid under every possible answer. Reversibility
lowers implementation risk; it does not confer authority. Symmetrically,
pre-authorization covers the _loop_, not the decisions the loop uncovers: an
instruction to proceed without approval never licenses skipping a gate the
work itself raises.

**G9. Authority binds to a specific question and artifact, not to a phrase.**
An approval is scoped to what was asked and to the artifact that was in front
of the approver. Any mechanism that can replay text — a compaction, a
reconnect, a resumed session — can re-present a prior approval so that it
reads like a fresh answer to the question just asked. Detect it by shape
mismatch, by verbatim match to an approval already consumed, or by suspicious
timing, and refuse: name the mismatch and re-ask. A genuine approver answers
again in one line; an echo does not reproduce. The same scoping holds without
any replay: what was approved is the specific version of the specific bundle
that was presented, so a material change to the plan, the surface, or the
blast radius voids it and must be re-presented rather than absorbed as
already-covered.

**G10. Over-escalation is a failure mode, not caution.**
G5 and G6 push mechanical labor off the human and reserve genuine decisions
for them. The mirror failure is asking anyway: presenting a menu of options
for a reversible, in-scope, low-stakes choice spends the scarcest resource in
the system and makes the human the bottleneck they hired the pipeline to
remove. Decide what you are equipped to decide, state the decision and its
one-line rationale, and record it attributably so it can be vetoed after the
fact. Reserve the interrupt for irreversible acts, policy and identity,
unset budget ceilings, and real forks with trade-offs only the owner can
weigh.

**G11. Never make the human your scheduler.**
An autonomous run that dispatches work and then ends its turn to wait goes
idle until someone pokes it — the human becomes the clock, which is the
opposite of the arrangement. On the critical path, wait deliberately with one
paced, bounded waiter and continue in the same span of work. Off it, take a
single completion signal and do not also poll. Polling is an evidence read,
not a clock: one unchanged status does not justify another immediate look.
Every one of these — idling for a push, duplicated push-and-pull, zero-delay
status spinning, whimsical re-dispatch — is churn that looks like progress.

**G12. An interruptible run must be able to answer "what is happening" in one
bounded snapshot.**
When a human re-enters a long autonomous run, they get an immediate answer
before any further work: what is active right now and whether anything
destructive is in flight, what has actually landed (artifact-verified only),
and what is blocked with the exact next step. Naming paused safety controls
belongs in that snapshot. If answering requires reconstructing state from
identifiers, task labels, or a chronology dump, the run is not supervisable.

**G13. Approving a decision is not authorizing the act that follows it.**
"Yes, that is the right approach" is a ruling on the approach. It is not
permission to commit, to publish, to restart the system, to delete, or to
declare the unit closed. Those are separate capabilities with their own blast
radius, and collapsing them is how an agreed-upon plan turns into an
unreviewed irreversible action. Keep the two gates distinct even when the same
person holds both, and name which one you are asking for.

**G14. A conditional approval carries its condition all the way to the act.**
An approval granted on a stated premise — provided the check passes, assuming
this is reversible, as long as nothing else is touched — remains bound to that
premise at the moment of execution, which may be much later and after
intervening evidence. If the premise no longer holds, the approval has
expired; it has not become unconditional through the passage of time. Re-state
the predicate when you act on it, and stop if it is now false.

---

## Theme H — Disposition and tone of the agent

**H1. Honest pushback is required, not optional.**
An agent that agrees with a flawed instruction to be agreeable is a
liability. The workflow must expect and reward the agent surfacing "this
is wrong because…" The most valuable interventions are the ones that
contradict the operator with evidence.

**H2. Reject the maximalist reading of a demand when it conflicts with a
principle.**
"Address everything" does not mean "pull unrelated future work into now."
"Fix it completely" does not mean "rewrite the working parts." When an
instruction's literal maximal reading violates anti-bloat or scope
discipline, the correct response is to name the conflict and propose the
disciplined reading, not to comply maximally.

**H3. Distinguish "broken" from "not yet built."**
A seam that fails because its consumer hasn't been implemented yet is not
the same as a seam that's implemented wrong. The first is scheduled work;
the second is a defect. Triaging them identically produces either false
alarm or premature building. Always ask whether a failure is a defect or
an absence.

**H4. A correct failure is a success of the process.**
When a gate or reviewer correctly fails work — including catching
something a weaker process would have passed — that is the system working,
not a setback. Evaluate the process by whether it catches what it should,
not by whether everything passes on the first try.

**H5. An obstacle to gathering a decision's evidence must not bias the
decision.**
This is the most insidious reasoning failure observed, because it never feels
like one. When a tool is broken, a probe keeps dying, or the measurement is
expensive, the reading of the problem that happens not to need that evidence
becomes quietly attractive — and gets adopted on arguments that look
technical. Name the missing evidence explicitly, then reason to the sound
answer anyway, or fix the obstacle and go get it. "This interpretation avoids
the thing that isn't working" is never an argument, and the moment an
option's appeal coincides with its convenience is the moment to be suspicious
of your own reasoning.

**H6. A reclassification from an authority is a proposal to re-decide, not a
settled fact.**
When a reviewer, a judge, or the operator overturns a load-bearing
classification, that carries the same weight as the original call and earns
the same scrutiny. An authority can be formally right on the criterion it
applied and wrong on the one it did not check. Verify before folding it in,
and disagree on the record when the evidence requires it. Conceding because
the source is authoritative — or because it is late and the argument is
tiring — is how a wrong frame gets built on. Fatigue is a reason to pause,
never a reason to agree.

**H7. The deliverable is the mechanism, not the account of it.**
Under pressure, the reachable output is a document describing what would
work: a plan, an analysis, a report of what was found. That is the failure
mode this whole document exists to prevent, appearing as diligence. Nothing
is done until it runs and something outside the agent confirms it ran.

**H8. Do not canonize a workaround before establishing that the obstacle is
real.**
A blocked path gets routed around, the detour works, and the detour gets
written into the durable procedure — where it hardens into permanent
complexity that everyone afterward believes was necessary. Often the
"limitation" was a defect, a misconfiguration, or a wrong assumption about
what the tool could do, and the fix was cheaper than the workaround. Diagnose
first: is this the way the world is, or the way it is currently broken? Fix
the mechanism when you can, and if you must route around it, mark the detour
as provisional with the unresolved question attached rather than promoting it
to a rule.

---

## Theme I — Calibrating the evaluator

The rest of this document treats the verifier as the thing you trust. These
tenets exist because the verifier is also an artifact, authored under the
same pressures, and a defective one is the most expensive failure available:
it is indistinguishable from an execution failure, so every cycle it burns
gets charged to the implementer's competence.

**I1. Prove the bar two-sided, through the full decision path, before
freezing it.**
An acceptance threshold is not defensible until a constructed best case has
been driven all the way through — metric, aggregation, threshold, verdict —
and passed, and a constructed genuine failure has been driven through the
same path and failed. Do both against the real machinery, never against
hand-set verdict payloads. Critically, the best case must be produced by the
_same class of solution the contract obliges the implementer to build_, under
its real constraints. A bar that an unconstrained ideal clears proves
reachability in principle, not reachability by anything the implementer is
allowed to write — and that distinction has cost multiple build cycles that
looked like quality failures and were arithmetic.

**I2. Reachable is necessary and not sufficient: the metric must also
discriminate.**
A check the naive baseline passes by construction certifies nothing, however
cleanly it is expressed. The one-line test before ratifying any threshold,
and especially before loosening one: _does the trivial or default solution
pass this by construction?_ If yes it is vacuous — and vacuous is worse than
unreachable, because it manufactures confidence instead of failure. When an
unreachable magnitude bar must be retired, pair the retirement with a
tightening that actually powers whatever the work's value depends on, and
name the remaining floor as a regression guard rather than as the value test.

**I3. Ground a threshold in a measured frontier, not in a chosen number.**
The load-bearing constant is the one most likely to have been picked because
it sounded right. Derive it: drive the mandated class of solution to its best
achievable score across several independent instances, look at the
distribution, and set the bar as a fraction with margin of what is _reliably_
achievable. Never set it from a single point, from the best observed case, or
from a number the evidence has already produced — a proposed threshold that
sits near the current implementation's score launders that implementation
into passing, and one that sits near the best observed case is the same error
mirrored.

**I4. The graded quantity's degrees of freedom must lie in the layer the
implementer is allowed to move.**
The subtlest unreachable bar is the one whose arithmetic is clean: a
normalized measure whose numerator can only be moved by the layer under
contract, while its denominator's magnitude is set by a layer the contract
explicitly forbids touching. The achievable result is then a weak
second-order effect regardless of build quality. Trace both sides
independently — what can the mandated work actually move, and where does the
magnitude of the comparison come from — and if they live in different,
contractually separated layers, the bar is broken.

**I5. Hold everything fixed except the variable being graded.**
A comparison run through two different apparatuses measures the apparatus. A
candidate evaluated with one solver against a reference computed with a
stronger one is handicapped by the harness, and the resulting deficit says
nothing about the candidate. Before trusting any comparative number, confirm
in the source that the baseline and the candidate differ only in the thing
under test.

**I6. Assert the measurement's own construction invariants, and return
"undetermined" when they break.**
Most measurements have properties that hold by construction — a constrained
optimum cannot be worse than a feasible reference, a fraction cannot exceed
its whole, a subset count cannot exceed its superset. Assert them on every
run. A violation means the instrument is broken, and the correct output is
_undetermined_, never a finding and never a threshold proposal. A broken
reference impersonates a low ceiling extremely convincingly. Watch for scale
degeneracy in the same reflex: a ratio computed on a near-zero denominator is
noise that will happily satisfy a relative significance test, so significance
needs an absolute floor as well as a relative one.

**I7. A cheap probe answers whether, never how much — and its brief must
permit "undetermined."**
An under-powered measurement can decisively settle a yes-or-no question while
being structurally incapable of setting a number. If the instruction asks for
a value, the agent will return one, because a brief that admits no
"insufficient evidence" answer structurally forces over-claiming. This is
the scoping party's failure, not the reporter's: permit the null return
explicitly, and require a distribution wherever a magnitude is expected. Then
treat a confident point estimate from a bounded probe as a defect regardless
of how authoritative its source is.

**I8. Declare the acceptance mode explicitly, and declare it per leg.**
There are two shapes of success and they need different machinery: a set of
binary properties that either hold or do not, and a continuous quantity
descended toward within a budget where "not yet, keep going" is a legitimate
state. Which one applies is a separate axis from how risky the work is, and
it gets decided implicitly unless it is written down. Most real units are
mixed: constraint satisfaction and policy compliance are _always_ binary —
you do not descend toward a constraint — while at most one leg carries a
genuine continuous margin. Label each leg, never the unit as a whole, and
never inherit a leg's classification from the predecessor unit: two adjacent
units measure different quantities across the seam between them.

**I9. Reachability gates the classification, not just the number.**
"A continuous quality measure exists" does not make success continuous; the
load-bearing half of that judgment is _with room to improve_, and that clause
must be verified rather than assumed. A continuous measure whose achievable
frontier sits at the baseline has no room, and the honest treatment is a
binary property. Both misclassification directions cost the same, so run the
reachability determination _before_ fixing the mode — at authoring time,
which is the cheapest place it can be caught.

**I10. Repeated failure against the same bar is evidence about the bar.**
After a second cycle fails near the same ceiling, the next action is to
measure the ceiling — by reading the grading definitions, not by inspecting
the implementation's shape — rather than to commission another attempt.
Charging cycle after cycle to implementer quality when the metric is
unreachable is the single most expensive pattern in this document, and it
always looks like an execution problem from inside.

**I11. Never require a surface that does not exist in the real dependency.**
An acceptance property that can only be satisfied by emitting a field,
metric, or endpoint with no counterpart in the actual pinned dependency is a
defect in the property, and satisfying it is fabrication. The distinction
that holds: synthetic _values_ on _real_ structure are legitimate and often
necessary; invented _structure_ never is, and labelling it synthetic does not
launder it. Cross-check every surface a contract obliges the work to touch
against the real dependency before freezing, and when a settled decision's
_phrasing_ forces a phantom surface, correct the decision rather than
satisfying its letter.

---

## Theme J — Seams, substrate, and custody

Themes A through I assume the machine under the agent behaves and that work,
once done, is where you left it. Neither assumption held. These tenets are
about the layer beneath the reasoning, where a conclusion can be perfectly
argued and still worthless.

**J1. Defects live in the seam between locally correct components.**
The recurring shape of a hard bug: two parts are each correct and verified,
and the failure is in the join nothing tested. Local correctness on both
sides of a boundary is not coherence across it. So every positive control
traverses the _entire_ path end to end rather than each stage separately,
and every unit verifies its own assumptions rather than inheriting a
predecessor's conclusion — the seam between two units of work is exactly as
untested as the seam between two functions.

**J2. Separate substrate failure from work failure before concluding
anything.**
A full disk, an exhausted quota, a hung process, a dead transport, a service
that refuses every write — each produces symptoms that read as defects in the
work. A conclusion drawn about the work while the substrate was broken is
worthless, and worse, it usually gets recorded. Probe the substrate first when
failure is broad, sudden, or absurd. An infrastructure hang is a
diagnosis to report precisely, not a failure to attribute. Headroom is a
correctness requirement, not an operational nicety: disk, memory, and
scratch space that run out produce corruption and refused writes rather than
a clean error, so cleanup has to survive the timeouts and process deaths that
are exactly when it gets skipped.

**J3. Verify which plane a tool acts on.**
When an agent's filesystem, network, or process view differs from the one
that matters — a container against a host, a mount against its source, a
sandbox against the real target — then a file written, a service probed, or a
path resolved may have happened somewhere real but irrelevant. Evidence
written to the wrong plane is not evidence. Establish which plane each tool
reaches before trusting anything it reports, and keep that mapping explicit
rather than inferred. Make the plane an explicit input to any operation that
crosses one, rather than something the agent infers from a familiar-looking
path — a path that exists in both places is the most dangerous kind. This is
also why a negative observation is weak: not finding a process, a file, or a
service from the wrong side proves nothing about whether it exists.

**J4. Missing work is a custody question before it is a loss.**
Work that cannot be found has usually not been destroyed; it is somewhere you
did not look — a branch you are not on, a reference nobody enumerated, a
sibling session, a different store. Enumerate before concluding: refs,
branches, working trees, sessions, stores. Never re-run destructively on
apparent absence, because the panic re-run is what turns a lookup failure
into a real loss. This is also the discipline that makes state duplication
survivable: recover from the durable spine, not from whichever copy is in
front of you.

**J5. Every status envelope is one observer, not ground truth.**
A control-plane label and the actual work are different facts. A run marked
running can have a dead supervisor; a run marked failed can have a live
orphan still mutating the repository; a completion notification can fire for
work already harvested. Reconcile the label against artifact freshness on
disk, and never act destructively on a single observer: before terminating,
bind identity with several independent signals, and before retrying, prove
the prior attempt left nothing behind or deliberately reconcile what it did.

**J6. A parent owns its children's lifetime.**
Background work dispatched by a process that then exits dies with it — often
reporting success, because the dispatch succeeded and nothing observed the
death. Work that must survive either runs to completion within its parent's
life or lands in durable state as it goes. The same applies to evidence: a
receipt that lives only in untracked scratch is destroyed by the next
clean-state sweep, so put durable proof where the cleanup cannot reach it.

**J7. Verify control-plane assumptions by reading them back.**
Automation has implicit conventions — where relative paths resolve from,
which clock and timezone a schedule is interpreted in, which channel output
is delivered on, what an empty result means — and each has silently voided
work. Scheduled is not runnable: a job registered against a path that does not
resolve fails on every fire. Worst of all is silence-on-success: a job that
says nothing when healthy is indistinguishable from a job that never ran, so
verify it by the accrual of its artifact over time, never by its own status.
Read back what the control plane actually recorded rather than assuming it
accepted what you meant.

**J8. Scheduling is a baton across an interruption, never the ignition for
work you can drive now.**
A scheduled continuation earns its place for exactly one purpose: carrying
work across something that ends the current session, such as the restart that
applies a change, or a resource that is genuinely unavailable until later.
It is the wrong instrument for starting work that could be driven live, and
using it that way is deferral wearing the costume of automation — a scheduled
session is blind, unsteerable, and cannot be corrected mid-flight. And it is
a _second_ concurrent worker: if you decide to drive live, cancel the
scheduled one before it fires, or you have created the collision you were
guarding against.

**J9. A handoff packet is self-contained or it is not a handoff.**
A dispatched worker inherits none of the conversation that produced its task:
absolute paths, the plane to act on, the exact success condition, and the
negative constraints _are_ the packet. Because this is a rule that gets
"mostly followed," enforce it mechanically at the dispatch boundary — refuse a
packet missing its required elements rather than discovering the omission in
the child's confused output. And compose the whole packet before the first
dispatch attempt rather than learning the requirements through a sequence of
rejections. The packet must also tell the worker what to do when it is stuck,
because an autonomous child has no one to ask: it decides within the authority
it was given, or it stops and emits a structured blocker. A worker that waits
for an answer that cannot arrive burns its entire budget on silence.

**J10. One writer per mutable surface, for the duration of the fan-out.**
Parallelism is safe when the lanes own disjoint state or are read-only. Two
children editing the same file, record, or configuration will interleave into
a result neither produced, and the loss is silent because each child reports
success truthfully. Assign ownership explicitly when fanning out, and where
several lanes must contribute to one surface, have them return their findings
and let a single consolidator write.

**J11. A logical transition spanning two stores needs one authoritative
commit point.**
When a single conceptual change has to land in several places — a record and
an index, a graph and a file, a status and its artifact — a crash or timeout
between the writes leaves a state that is neither the old one nor the new one,
and it is precisely the state nothing knows how to interpret. Either make the
transition atomic, or write an intent journal first so an interrupted
transition is recoverable rather than merely detectable. Recovery must be able
to answer "was this committed?" without guessing.

**J12. Every side-effecting operation must be safe to repeat under an
ambiguous outcome.**
A timeout, a dropped connection, or a killed process leaves you unable to tell
whether the effect happened. Retrying blindly duplicates it; not retrying
loses it. Neither is acceptable, so design the operation to be repeatable
without harm — a stable key the receiver can deduplicate on — and read back
after any ambiguous failure rather than inferring from the error. Ambiguity is
the normal case at scale, not the exception.

**J13. Preserve the causal identity of a failure.**
Collapsing every failure into one generic status destroys the information
needed to respond, and the responses are opposite: a provider refusal wants a
retry, an exhausted resource wants cleanup, a bad handoff wants re-authoring, a
genuine defect wants a fix. Worse, a masked infrastructure failure gets
attributed to the work and recorded as a quality problem. Keep the layer the
failure came from attached to it, all the way to whatever reads it later.

**J14. Distinguish the kinds of timeout, and tie progress to real work.**
"It took too long" hides several different facts: total elapsed time, silence
since the last output, a limit on steps, and the death of a parent. They have
different meanings and different correct responses, and a single undifferentiated
timeout will kill healthy long work while letting a stalled process run.
Distinguish them — and make the liveness signal causally downstream of actual
progress, because a heartbeat that ticks regardless of whether anything is
happening measures only that the clock still runs.

---

## The irreducible core

If most of this document were lost, these would regenerate it:

1. **The goal is a contract — end state, required evidence, constraints,
   budget — and the outer loop supervises the agent against it, carrying
   the convergence guarantees** (E0, E7).
2. **Enforce non-negotiables in the pipeline; verify semantic properties
   on artifacts, not source, and never on the agent's own claim of
   completion** (A1, A2, C1).
3. **Separate who writes checks from who satisfies them; a judge
   consolidates, reviewers find; match the evaluator to the crispness of
   success** (B1, B5, F5).
4. **Every checker has a finite closure contract; severity is graded by
   reality; recurring classes are adjudicated once and bound forward**
   (C2, C3, C6) — this is what keeps multi-agent review from diverging.
5. **Remediation gates named findings only; convergence survives human
   override; never depend on one agent being perfect** (C4, C7, C8).
6. **Delete before adding; localize the cure; trace every process element
   to a threat** (D1, D2, D3).
7. **Plan-review-implement-review-judge, with mechanically-checkable gates
   and a structurally-unskippable completion gate** (E1, E2, E3).
8. **Contracts are runner-neutral and single-sourced; role-to-model
   routing is a deliberate architecture decision; behavioral portability
   is earned by a supervised run; the human decides, the pipeline labors**
   (G1, G2, G4, G3, G5).
9. **Mine past sessions for recurring failures and route each to its
   correct enforcement home — check, instruction, or harness fix — keeping
   the always-loaded surface small** (F6, F4).
10. **The evaluator is an artifact that can be wrong: prove the bar
    two-sided and reachable by the mandated solution, prove it is not
    vacuous, ground it in a measured frontier, and read repeated failure
    against the same bar as evidence about the bar** (I1, I2, I3, I10).
11. **Every projection of state is a timestamped claim — dashboards, task
    lists, status envelopes, prior sessions, your own memory — so close
    nothing without citing the artifact, and separate substrate failure
    from work failure before concluding anything** (A6, J2, J5).
12. **Authority binds to a specific question: silence is not consent, a
    replayed approval is not an approval, approving an approach is not
    authorizing the act, pre-authorization covers the loop and not the
    decisions it uncovers — and escalating a reversible in-scope choice is
    its own failure** (G8, G9, G13, G10).

None of this removes the hard problems: agents still take shortcuts, stop
early, and overestimate completion. Trusting them more does not fix that;
better control systems do. Goals, loops, evaluators, deterministic checks,
observable artifacts, and session memory are all ways of making autonomy
observable and correctable rather than merely hoped-for.
