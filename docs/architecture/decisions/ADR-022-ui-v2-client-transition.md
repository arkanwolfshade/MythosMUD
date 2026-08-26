# ADR-022: ui-v2 Client Transition and Legacy Retirement

**Version 1.0.0** · MythosMUD · 2026-08-26

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted
**Date:** 2026-08-26

`client/src/components/ui-v2/` (`GameClientV2Container` / `PanelSystem`, 95 modules) is the
client architecture. This ADR records that decision — which had never been written down — and
the retirement plan for the legacy surface that still sits alongside it. It closes #637.

## 2. Context

**[NOTE]**
Issue #637 asked to replace "ADR-021 section 6." No ADR named
`ADR-021-ui-v2-client-transition.md` exists; `ADR-021` is
[Character Display Name Validation](ADR-021-character-display-name-validation.md), dated
2026-08-23. No ADR anywhere records the ui-v2 transition. A contributor reading
`client/src/components/` sees two plausible client architectures — `ui-v2/` (95 modules) and the
remainder (155 modules) — with nothing indicating which one ships.

**[BUG]**
The 2026-08 design audit that filed #637 both cited a document that never existed and
undercounted the legacy surface by roughly 6x (~26 claimed vs. 155 actual `.ts`/`.tsx` files
outside `ui-v2/`, tests excluded). This is the fourth ranked item in the 618-639 campaign with a
materially false premise, and the first citing a nonexistent document.

## 3. Decision

**[SPEC]**

- `client/src/components/ui-v2/` is the client architecture. It is what `appLazyScreens.tsx` and
  `AppRouter.tsx` route into for gameplay.
- The onboarding/character-creation flow (`CharacterNameScreen`, `CharacterSelectionScreen`,
  `SkillAssignmentScreen`, `ProfessionSelectionScreen`, `StatsRollingScreen`,
  `MotdInterstitialScreen`) is **not** superseded — `ui-v2` has no character-creation flow of its
  own, and these six screens are lazily routed from `src/mythosApp/appLazyScreens.tsx`. They stay.
- Everything else under `client/src/components/` outside `ui-v2/` that is not transitively
  reachable from the production entry is retired per the plan in §6.

## 4. Alternatives Considered

**[SPEC]**

1. **Retirement plan only, no transition decision** — Rejected: a removal sequence with no
   statement of which tree is live doesn't close the ambiguity #637 exists to resolve.
2. **Two ADRs (transition, then retirement)** — Rejected: the retirement plan is meaningless
   without the transition decision it depends on; splitting doubles review surface for no benefit.
3. **Number this `ADR-021`, matching the issue's stale link** — Rejected: `ADR-021` is taken.
   Reusing it would misdate a 2026-08-26 decision behind one accepted 2026-08-23.

## 5. Consequences

**[SPEC]**

- Positive: the live architecture is on record; the orphaned surface has an inventory and named
  owners (§6); a CI gate (§6) prevents silent re-accumulation once the sequence completes.
- Negative: 82 of 155 legacy modules are confirmed orphaned but not yet deleted — this ADR is a
  plan, not a cleanup. The bundle does not shrink until the cluster issues land.
- Neutral: no runtime behavior changes in the PR that introduces this ADR.

## 6. Retirement Plan

**[SPEC]**

**Definition of "live":** transitively reachable via a static or `import()` reference — including
extension-inclusive imports (`from '../components/X.tsx'`) — from the production entry
(`index.html` → `main.tsx`), following imports to closure. A module reachable only from its own
test file, or only from another module that is itself only test-reachable, is **orphaned**, not
live.

**Stub exemption:** a module kept alive by tests alone is not orphaned if it carries an explicit
comment naming it a stub for future implementation *and* references a GitHub Issue tracking that
work. No candidate module in this inventory carries such a comment — the exemption found zero
matches.

**Inventory method:** `client/knip.json` `files` rule enabled (`"error"`, was `"off"`); a
script-driven import closure over `client/src` (not knip's own file-unused report, which — even
with `files: error` — reports only directly-unreferenced files and does not, by itself, resolve
the transitive case above) computed reachability from every module under
`client/src/components/` excluding `ui-v2/`. Two known false-negative sources were found and
corrected before trusting the result: import strings with an explicit `.tsx`/`.ts` extension, and
one-hop-only reachability (a module counts as live only if traced to something outside the
candidate set, not merely to any importer). **82 of 155** legacy modules are orphaned under this
definition; **73** remain live, including the six onboarding screens named in §3.

**Removal clusters** (one issue each, filed alongside this ADR):

| Cluster | Files | Contents | Issue |
| --- | --- | --- | --- |
| Top-level demo/test + legacy GameTerminal | 27 | `*Test.tsx`/`*.helper` demo components, `CommandPanelTest.*` family, `DraggablePanel*` family, `GameTerminal`/`GameTerminalContainer`/`GameTerminalPresentation` | [#690](https://github.com/arkanwolfshade/MythosMUD/issues/690) |
| `panels/` chat & game-log family | 35 | `ChatPanel*`, `GameLogPanel*`, `PlayerPanel`, `RoomPanel`, `ConnectionPanel`, `MonitoringPanel`, `panels/chat/*` | [#691](https://github.com/arkanwolfshade/MythosMUD/issues/691) |
| `containers/` | 6 | `BackpackTab`, `ContainerSplitPane*`, `CorpseOverlay*` | [#692](https://github.com/arkanwolfshade/MythosMUD/issues/692) |
| `ui/` misc + stray singletons | 14 | `ui/` leftovers (`StyleGuide*`, `FeedbackForm`, `RoomInfo`, …), `map/AsciiMapEditor.tsx`, `layout/GridLayoutManager.tsx`, `health/IncapacitatedBanner.tsx`, `lucidity/*` | [#693](https://github.com/arkanwolfshade/MythosMUD/issues/693) |

Each cluster issue carries its own per-file list, an export-signature comparison against its
apparent `ui-v2` counterpart (flagging suspected behaviour gaps — not claiming equivalence, which
a signature comparison cannot establish), and is removed in one reviewable PR. Deep behavioural
verification happens inside that PR, not here.

**Gate condition — the sequence's completion test:** `.github/workflows/ci.yml`'s knip step
carries `continue-on-error: true` (comment: *"Baseline has many findings; reduce over time, then
remove this"*), so even the enabled knip rules cannot fail CI today. The **final** follow-up issue
([#694](https://github.com/arkanwolfshade/MythosMUD/issues/694), explicitly last, depends on all
four cluster issues) removes that line. `npm run knip` returning clean with the gate enforcing is
what proves the retirement finished — not this ADR.

## 7. Related ADRs

**[SPEC]**

- ADR-008: React + TypeScript Client
- ADR-021: Character Display Name Validation (the onboarding flow this ADR keeps live)

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-08-26 | Initial version. Records the ui-v2 transition decision and the legacy retirement plan for #637. |
