# Audit Coverage Boundary — 2026-08 Design Audit

**Version 1.0.0** · MythosMUD · 2026-08-19

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Purpose

**[NOTE]**
The 2026-08-18 design↔implementation drift audit (record:
`data/MythosMUD-Obsidian/Design Audit 2026-08-18/`, a submodule checkout, 21 notes, 2,406 lines)
produced 24 issues, a security advisory, and corrections across roughly 40 documents. Those
**findings** are tracked as GitHub issues because they are concrete. The audit's **blind spots** are
not, because there is nothing to file. This document exists to correct that asymmetry: it is a
checkable scope ledger, not a narrative restatement of [issue #639](
https://github.com/arkanwolfshade/MythosMUD/issues/639).

This is Phase 0, item 1 of the ranked implementation order for issues 618–639. Phase 0, item 2 —
adversarially verify #625–#628 — is this document's first consumer; see §2.

## 2. Scope for the immediate next step: verifying #625–#628

**[SPEC]**

Four open, actionable issues rest on **single-agent evidence, never adversarially verified**:

| Issue | Title | Type |
|---|---|---|
| #625 | Phantom hostiles spawn but cannot be fought | bug |
| #626 | Reversed compass directions for Deranged tier never implemented | enhancement |
| #627 | Room editor backend APIs are missing — map editor edge editing is dead UI | enhancement |
| #628 | Gladiator arena has no entry point — 121 rooms nothing routes to | enhancement |

**Base rate.** The comparable adversarial pass over the 12 reopened issues from this audit found a
**1-in-12** error rate (corrected on #86). Across four items, that is roughly a 1-in-3 chance at
least one of #625–#628 is false.

**[BUG]**

**Symptom:** verifying against a stale index produces false negatives, not just false positives.
**Fix / mandatory precondition:** reindex before verifying. The party-integration-hooks claim in the
FRD sweep was marked `UNVERIFIABLE`, was re-run later, and turned out to be a **false negative**
caused by a stale jCodemunch index (`P4-Intent-FRD-Specs.md:129-131`). Known-stale at audit time:
`server/api/real_time.py`, `server/game/chat_service.py`. A clean re-check against an unrefreshed
index is not evidence — see the close rule in §5.

**Consequence.** Per the locked ranking (`issue_ranking_618-639_466453ee.plan.md:41`): *"#625–#628
stay provisional until the verification pass; a false finding reshuffles only those four."*

## 3. Enumeration method

**[SPEC]**

```text
Enumerated on branch main at commit 34ef2ed38 via:
  git ls-files 'docs/**/*.md' 'docs/*.md' | grep -v '^docs/archive/' | sort -u
```

Yields **103** live Markdown files under `docs/` (excluding `docs/archive/`). This document is
excluded from its own enumeration — a coverage ledger that lists itself as an unexamined design doc
would be self-contradicting; once committed, `git ls-files` returns 104.

The audit recorded the corpus size as **102**. It has already drifted by one since 2026-08-18, which
is why the command and commit are pinned rather than the count alone. This guards the exact failure
that produced the audit's five withdrawn findings: the original corpus decision was made from
`ls docs | head -60`, `docs/subsystems/` sorted below that cut, and the truncation went unnoticed
because the command itself was never recorded (`CORRECTIONS-Corpus-Gap.md:14-16`). Re-run the command
above against the current `HEAD` before trusting any count in this document.

**Directory tallies at `34ef2ed38`:**

| Directory | Files |
|---|---|
| `docs/` (root) | 60 |
| `docs/architecture/decisions/` | 20 |
| `docs/subsystems/` | 16 |
| `docs/architecture/` | 3 |
| `docs/runbooks/` | 2 |
| `docs/testing/` | 1 |
| `docs/examples/logging/` | 1 |

**[?]**
`docs/subsystems/` is 16 tracked files, but the audit and issue #639 both say "15 documents". The
delta is `README.md`, which describes the directory rather than a subsystem. Stated here so it reads
as reconciled, not as further uncounted drift.

## 4. Coverage ledger

**[SPEC]**

Columns: **Surface** · **Size** · **Excluded because** · **Risk if wrong** · **Status** · **Closed
by**. `Status` values are plain words (`EXAMINED`, `NOT EXAMINED`, `UNKNOWN`, `UNRESOLVED`) — never a
bracketed tag — so this table does not itself trip HADS's loose-tag scan. `Closed by` is a citation
(vault note, issue, or commit); see the close rule in §5 for what is allowed to fill it.

### 4.1 Documents — the audited 29, recovered from the audit's own claim registers

**[NOTE]**
The audited corpus was never published as a list, only as a count. It is nonetheless fully
recoverable: `P2-ADR-Claims.md` (frontmatter `artifact_group: ADR-001..018`, `docs: 18`, `lines:
2182`, `claims_total: 64`) and `P2-Structural-Claims.md` (frontmatter `docs: 11`, `lines: 3806`,
`claims_total: 47`) together enumerate exactly 18 + 11 = **29** documents, reconciling with the
corpus count the audit reported. These 29 are marked `EXAMINED` below, cited to their register.

| Surface | Size | Excluded because | Risk if wrong | Status | Closed by |
|---|---|---|---|---|---|
| 18 ADRs (`ADR-001`–`ADR-018`) | 2,182 ln | — audited | `provenance: post-hoc` per the register — a `CONFORMS` verdict here is weak evidence, since these ADRs were largely written to describe code already in place | EXAMINED | `P2-ADR-Claims.md` |
| `BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md`, `CONTAINER_SYSTEM_ARCHITECTURE.md`, `PERSISTENCE_REPOSITORY_ARCHITECTURE.md`, `DATABASE_ACCESS_PATTERNS.md`, `EVENT_OWNERSHIP_MATRIX.md`, `NATS_SUBJECT_PATTERNS.md`, `REAL_TIME_ARCHITECTURE.md`, `CONNECTION_MANAGER_ARCHITECTURE.md` | part of 3,806 ln (11 docs) | — audited | `provenance: pre-hoc` per the register — a `DEVIATED` verdict here is a genuine finding, not a documentation artifact | EXAMINED | `P2-Structural-Claims.md` |
| `DISTRIBUTED_EVENTBUS_NATS.md`, `API_OPENAPI_SPECIFICATION.md`, `aggro-threat-system.md` | part of 3,806 ln (11 docs) | — audited | same pre-hoc weighting as above | EXAMINED | `P2-Structural-Claims.md` |

### 4.2 Documents — the residual 74, conservative default

**[NOTE]**
The two error types here are asymmetric: marking an audited doc `NOT EXAMINED` costs one wasted
re-check; marking an unaudited doc `EXAMINED` hides a gap, which is precisely the failure this
document exists to prevent. Every document below therefore defaults to `NOT EXAMINED` unless the
vault gives direct evidence otherwise — none currently does for this residual set.

Arithmetic: 103 total − 29 examined (§4.1) = 74 residual = 16 (`docs/subsystems/`) + 1
(`decisions/README.md`) + 57 (below). Issue #639's "roughly 70 further live documents" used a
different denominator (102 − 29, before `docs/subsystems/` was broken out as its own row); once
subsystems is counted separately, carrying that figure forward would double-count it.

| Surface | Size | Excluded because | Risk if wrong | Status | Closed by |
|---|---|---|---|---|---|
| `docs/subsystems/` — 15 design docs (Movement, Follow, Rest, Rescue, Emote/Pose, Who, Party, Combat, Status effects, Magic, Skills/Level, Lucidity, Respawn, NPC, Admin commands) + `README.md` | 16 files, ~2,497 ln | not in the ADR-plus-architecture corpus; used only to *withdraw* false-gap findings, never read for conformance | see §4.4 — these are reverse-engineered from code, so absence of findings does not mean alignment | NOT EXAMINED | — |
| `docs/architecture/decisions/README.md` | — | not a claim-bearing document, not covered by the 18-ADR register | low — index-only | NOT EXAMINED | — |
| **57** further live documents — how-to guides, runbooks (`docs/runbooks/`, 2), testing docs (`docs/testing/`, 1), examples (`docs/examples/logging/`, 1), and the remainder of `docs/` root not named in §4.1 | remainder of 103 | outside the ADR-plus-architecture corpus by original scoping choice | unknown — never sampled at all | NOT EXAMINED | — |

### 4.3 Code — method fact, not a directory checklist

**[SPEC]**
**No code directory has swept status.** Verification throughout the audit was **claim-driven symbol
lookup**: an agent read a design claim, then used jCodemunch to check the specific symbol the claim
named (`who_commands.py:190`, `server/models/game.py:67`, `chat_service.py`, etc.). No directory of
code was ever walked top to bottom. Because the audit's own headline finding is that the design
record was substantially reverse-engineered *from* the code, this sampling method is structurally
biased toward code that already has documentation — which means the code most likely to be
*undocumented* is the code least likely to have been visited. Issue #639 names five trees as
unexamined; that phrasing implies the complement (`server/`, `client/`) was covered by a sweep. It
was not — it was covered by whatever a design claim happened to point at.

| Surface | Excluded because | Risk if wrong | Status | Closed by |
|---|---|---|---|---|
| `server/tests/` | never opened at all | test suites may encode a wrong contract undetected | NOT EXAMINED | — |
| `e2e-tests/` | never opened at all | same | NOT EXAMINED | — |
| `scripts/` | never opened at all | operational scripts unverified against current schema/config | NOT EXAMINED | — |
| `tools/` | never opened at all | same | NOT EXAMINED | — |
| `db/` (most of) | never opened at all | procedures unverified against ADR-015's stored-procedure contract | NOT EXAMINED | — |
| `server/` (remainder), `client/` (remainder) | sampled only where a design claim pointed | claim-driven sampling is biased toward already-documented code — undocumented code is systematically under-sampled | NOT EXAMINED (no sweep — see §4.6) | — |

### 4.4 `docs/subsystems/` — staleness, not conformance

**[SPEC]**
`docs/subsystems/README.md` states outright: *"This directory contains **reverse-engineered** design
documents… Code is the source of truth; these docs are derived from it."* All 15 are dated
2026-07-30. Auditing them for design↔code conformance would mostly re-confirm that code matches
documents that were themselves derived from that code
(`CORRECTIONS-Corpus-Gap.md:82-84`: *"Auditing 2,497 further lines of admittedly reverse-engineered
prose for conformance would mostly re-confirm that code matches documents derived from code. Using
the directory to suppress false gap findings captures nearly all the value at a fraction of the
cost."*). Issue #639 ranks a subsystems conformance check as its top suggested next pass; this
document deliberately overrides that ordering — see §6 — because the audit's own closing
recommendation on the same evidence says the opposite. The pass with real signal is **staleness**:
has the code moved since 2026-07-30 in ways the derived docs no longer reflect?

### 4.5 Security — a boundary issue #639 does not mention

**[SPEC]**
No systematic security review was performed at any point in this audit. The one Critical finding —
a WebSocket authentication bypass at `server/api/real_time.py:231-247`, where a missing/invalid JWT
falls back to trusting an unauthenticated `player_id` query parameter — was found **incidentally**,
while verifying an unrelated design claim during the P4 intent sweep (`CRITICAL-WebSocket-Auth.md`,
`phase: P4`, `verified_by: main-agent-direct`). Nobody was looking for it. [#632](
https://github.com/arkanwolfshade/MythosMUD/issues/632) merged the fix for that one instance. The
**defect class** — a test-only affordance shipped with no enforcing gate, where *"the comment says
'only for tests' — nothing enforces that"* (`CRITICAL-WebSocket-Auth.md:40`) — was never swept for
anywhere else. #632's closure is a fix, not coverage.

| Surface | Excluded because | Risk if wrong | Status | Closed by |
|---|---|---|---|---|
| Systematic security review (auth, authz, injection, secrets handling) | never scoped as a dimension of this audit | unknown — the one incidental finding was Critical | NOT EXAMINED | — |
| Test-only-affordance defect class (comment-gated bypasses with no enforcing flag) | only the one instance was found, and only by accident | other instances of the same pattern may exist unflagged | NOT EXAMINED | — |

### 4.6 Questions never asked

**[SPEC]**

| Surface | Excluded because | Risk if wrong | Status | Closed by |
|---|---|---|---|---|
| Code-to-documentation coverage sweep (enumerate the codebase, ask "what has no design record") | never run — undocumented systems surfaced only when an intent artifact happened to point at one | the undocumented-systems list is a sample, not an inventory | NOT EXAMINED | — |
| Systematic pairwise document contradiction sweep | never run — the four contradictions found were noticed incidentally while verifying other claims | unknown further contradictions | NOT EXAMINED | — |

### 4.7 Verification debt — irrecoverable, must be re-run wholesale

**[BUG]**

**Symptom:** roughly 19 `UNVERIFIABLE` findings across the FRD and plan-document sweeps were never
resolved, and cannot be resolved individually. They exist only as counts in prose —
`P4-Intent-FRD-Specs.md:128`: *"15 claims marked UNVERIFIABLE rather than guessed — partly turn
budget, partly the jCodemunch index reporting itself stale."* No claim IDs were recorded, no list, no
per-item citation. The one item that *was* re-verified (party-integration hooks) turned out to be a
**false negative** caused by the stale index — so the remaining ~19 should be treated as unresolved,
not as negative findings.

**Fix:** because the individual claims are unrecoverable, the FRD sweep and the plan-document sweep
must be **re-run wholesale**, not resolved item by item. This is materially more expensive than
"resolve 19 things" and should be budgeted as a full re-sweep. Attach a method rule to any future
sweep: enumerate `UNVERIFIABLE` claims as individually citable work items (claim text + location),
never collapse them into a count. The debt is unrecoverable specifically because it was recorded as
a number — the same asymmetry this whole document exists to correct.

| Surface | Excluded because | Risk if wrong | Status | Closed by |
|---|---|---|---|---|
| ~15 `UNVERIFIABLE` claims, FRD sweep | recorded as a count only, no claim IDs | unknown — one re-verified instance was a false negative | UNRESOLVED | — |
| ~4 `UNVERIFIABLE` claims, plan-document sweep | same | unknown | UNRESOLVED | — |
| `server_authority_remediation` | unverifiable on a stale index; needs a dedicated client-side pass | unknown | UNRESOLVED | — |
| `generate-authoritative-database-schema` phases 3–4 | schema-application step moved somewhere the sweep did not cover | unknown | UNRESOLVED | — |

### 4.8 Unmerged remediation — the audit's own output was never verified against `main`

**[BUG]**

**Symptom:** the vault's `P8-Applied.md` reports the audit's own remediation work as **Done**. It is
done *on a branch*. Commit `d7627813f` ("Refactor ADRs and related code for player effects system and
WebSocket authentication") lives on `origin/design-impl-audit` and is **not an ancestor of `main`**
(`git merge-base --is-ancestor d7627813f HEAD` returns false on `34ef2ed38`). Concretely, on `main`:

- `ADR-019` (Player Effects System) **does not exist** — zero references anywhere in the tree.
- The **16 `ADR-009` → `ADR-019` citation repoints P8 reports as applied never landed.**
  `server/models/game.py`, `server/models/player.py`, `server/async_persistence.py`,
  `server/alembic/versions/2026_02_09_add_player_effects_table.py`, `player_effect.py`,
  `player_effect_repository.py`, `login_grace_period.py`, and their tests all still cite `ADR-009`
  for the effects system — the exact mistake `CORRECTIONS-Corpus-Gap.md:53` identified.
- `ADR-020` **is** present on `main`, but arrived separately via #632, not from this branch.

**Fix:** merge or re-apply `origin/design-impl-audit`, then re-verify the citation repoint count
against `main` rather than trusting the vault's "Applied" status. See §6, item 1.

| Surface | Excluded because | Risk if wrong | Status | Closed by |
|---|---|---|---|---|
| P8 remediation (`d7627813f`, `ADR-019`, 16 citation repoints) | reported Done in the vault; verification against `main` was never performed | a reader trusts the vault and believes the citations are already fixed | UNRESOLVED | — |

## 5. Close rule

**[SPEC]**
**A row in this ledger is never closed by a clean result alone.** "I looked at X and found nothing"
closes nothing — that inference is exactly the one this document exists to forbid, per issue #639's
own premise. Closing a row requires **both**:

1. A cited artifact proving the sweep actually ran — a vault note, a GitHub issue, or a commit —
   recorded in the row's `Closed by` column, **and**
2. A recorded index-freshness check for any tooling-assisted verification.

Both are required together because the audit's only re-verified "clean" result *was* a false
negative produced by a stale index (§2). A clean result from an unverified tool is indistinguishable
from a clean result from a healthy one — the check is what makes the two distinguishable.

## 6. Deferred register — no phase in the 618–639 ranking

**[SPEC]**
The ranked implementation order for issues 618–639 (`issue_ranking_618-639_466453ee.plan.md`, phases
0–7) ends at #638. **None of the following are scheduled anywhere in that plan.** They are recorded
here so they read as acknowledged, prioritized debt rather than either a competing queue or silence.

Priority — **the audit's own closing recommendation overrides issue #639's stated ordering** where
the two conflict (see §4.4):

1. **Merge or re-apply `origin/design-impl-audit`** (§4.8). Finished work sitting unmerged and
   currently misreported as applied. Cheaper than any sweep below, and until it lands the codebase
   carries 16 citations the audit already proved wrong.
2. **Code-to-documentation coverage sweep** (§4.6). Never run; result is not predetermined; converts
   the undocumented-systems list from a sample into an inventory.
3. **Re-run the FRD and plan-document sweeps wholesale** (§4.7), reindexing
   `server/api/real_time.py` and `server/game/chat_service.py` first.
4. **Security defect-class sweep** (§4.5): grep for test-only fallbacks and comment-gated bypasses
   with no enforcing config flag, the pattern that produced the one Critical finding.
5. **`docs/subsystems/` staleness check** (§4.4) — explicitly *not* a conformance audit. Demoted
   below the four passes above per the audit's own recommendation, contrary to issue #639's ranking.

## 7. Explicitly out of scope

**[NOTE]**

- **`.cursor/rules/`** (272 files, ~77k lines of normative agent-binding rules) — considered and
  excluded. The audit's subject was design↔implementation drift for the game system; agent
  instruction files are tooling configuration, not system architecture.
- **Running any of the verification in §4 or §6.** This document is a charter. Zero rows are closed
  by writing it.
- **Re-opening or re-litigating findings already ruled on** in `P7-Rulings.md`.

## 8. Follow-up

**[NOTE]**
Issue #639's stated job is *recording* this boundary; that job completes when this document merges,
so #639 should close on merge rather than stay open as a standing tracker. Because the deferred
register in §6 has no other owner, one follow-up issue should be filed to own it, linked from this
document — otherwise the register would sit untracked in a merged file, restoring the exact
asymmetry between tracked findings and untracked blind spots that #639 exists to correct.
