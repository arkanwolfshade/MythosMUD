# UI Primitives Package Design

**Version 1.0.0** · MythosMUD · 2026-09-16

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
`client/src/components/ui-v2/primitives/` is the shared presentational-primitives layer `ui-v2`
is built on: the buttons, inputs, icons, panel chrome, modal shell and channel dropdown used
throughout `HeaderBar`, the panel family, and `GameClientV2ContainerView`. This document is
reverse-engineered from code; code is the source of truth (see
[`docs/subsystems/README.md`](../subsystems/README.md) for the same posture applied to behavioral
subsystems).

Written to close [`#744`](https://github.com/arkanwolfshade/MythosMUD/issues/744). That issue was
filed against the predecessor path `client/src/components/ui/`, deliberately deferring its own
disposition pending a check of whether the directory should be retired instead of documented —
the `#690`–`#694` ui-v2 retirement cluster had just swept it. That cluster is now fully closed,
and every surviving file in the old `ui/` directory turned out to be a live `ui-v2` dependency,
not retirement debris (§4). This document's companion change therefore also **relocated** the
package from `client/src/components/ui/` into `ui-v2/primitives/` — ADR-022 declares `ui-v2/` "is
the client architecture," and a directory of primitives it depends on for its own buttons and
icons has no reason to sit outside it, nor to carry a `(legacy)` label that stopped being true
once `#693` finished. See [ADR-022 §6](../architecture/decisions/ADR-022-ui-v2-client-transition.md#6-retirement-plan)
for the historical record of that cluster and its `[NOTE]` recording this relocation.

## 2. Members

**[SPEC]**

| File                  | Exports                                   | Purpose                                                                                                                                                                       |
| --------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `EldritchIcon.tsx`    | `EldritchIcon`, `MythosIcons` (re-export) | Maps a `MythosIcons` name to a `lucide-react` icon component, themed via one of five `variant` classes (`primary`/`secondary`/`warning`/`error`/`success`).                   |
| `MythosIcons.ts`      | `MythosIcons`                             | A `Record<string, string>` of icon-name string literals (self-mapped, e.g. `chat: 'chat'`) that `EldritchIcon.iconMap` and `ChannelSelector`/`config/channels.ts` key off of. |
| `TerminalButton.tsx`  | `TerminalButton`                          | `forwardRef` button with `variant`/`size` props, terminal styling.                                                                                                            |
| `TerminalInput.tsx`   | `TerminalInput`                           | `forwardRef` text input with terminal styling.                                                                                                                                |
| `ChannelSelector.tsx` | `ChannelSelector`, `Channel` (type)       | Dropdown for chat-channel selection; the `Channel` interface is also the shape `config/channels.ts` builds its channel list against.                                          |
| `LogoutButton.tsx`    | `LogoutButton`                            | Logout control with a global `Ctrl+Q` keyboard shortcut, wraps `EldritchIcon`.                                                                                                |
| `ModalContainer.tsx`  | `ModalContainer`                          | Modal shell with three layout modes (`center`, `center-no-backdrop`, `bottom-right`), Escape-to-close, optional close button and title.                                       |
| `MythosPanel.tsx`     | `MythosPanel`                             | Base bordered/titled panel shell.                                                                                                                                             |
| `index.ts`            | re-exports all of the above               | The only barrel in this directory; every consumer imports from `'./primitives'` / `'../primitives'`, never a component's own file path.                                       |

## 3. Boundary contract

**[SPEC]**

**Exports.** `index.ts` is the sole public surface — `EldritchIcon`, `MythosIcons`,
`TerminalButton`, `TerminalInput`, `ChannelSelector`, `Channel` (type), `LogoutButton`,
`ModalContainer`, `MythosPanel`. No component's own file path should be imported directly by
code outside this directory (tests are the one exception — see §6).

**Dependents.**

- `ui-v2/HeaderBar.tsx` — `EldritchIcon`, `LogoutButton`, `MythosIcons`
- `ui-v2/GameClientV2ContainerView.tsx` — `ModalContainer`
- `ui-v2/panels/{ChatHistoryPanel,CommandHistoryPanel,CommandInputPanel,GameInfoPanel,SettingsPanel}.tsx` — `EldritchIcon`, `MythosIcons`, `TerminalButton`, `TerminalInput`, `ChannelSelector`
- `ui-v2/PanelSystem/{ExpandedPanelHeader,MinimizedPanelHeader}.tsx` — `EldritchIcon`, `MythosIcons`, `TerminalButton`
- `config/channels.ts` — `MythosIcons`, the `Channel` type (channel configuration, outside `ui-v2`)
- `ui-v2/demos/EldritchEffectsDemo.tsx`, `ui-v2/demos/eldritchEffectsDemoData.ts` — all seven
  runtime exports; the only consumer of `MythosPanel` (§4); design showcase, not GameClientV2

**Invariants a caller must not violate:**

- **Presentational only.** No store access, no server calls, no business logic. Every component
  takes its state and callbacks as props; `LogoutButton`'s `Ctrl+Q` listener is the only
  side-effecting code in the directory, and it calls the `onLogout` prop rather than reaching into
  a store itself.
- **Theme exclusively via `mythos-terminal-*` Tailwind tokens** (`bg-mythos-terminal-surface`,
  `text-mythos-terminal-error`, `border-mythos-terminal-border`, etc.) plus the `eldritch-*`
  animation utilities (`animate-eldritch-glow`, `duration-eldritch`). No hardcoded colors.
- **`EldritchIcon`'s `iconMap` must stay total over `MythosIcons`.** `iconMap` is typed
  `Record<keyof typeof MythosIcons, keyof typeof LucideIcons>` — adding a key to `MythosIcons`
  without a matching `iconMap` entry is a compile error, not a runtime gap.
- **`ChannelSelector`'s `Channel` type is shared, not local.** `config/channels.ts` imports it to
  type the channel list it hands back to `ChannelSelector` — the two are one contract split
  across a component and its configuration, not two independent shapes that happen to match.

## 4. Key design decisions

**[SPEC]**

- **Relocated from `client/src/components/ui/` to `ui-v2/primitives/`, not just documented in
  place.** The `#744` investigation found all 8 files were live `ui-v2` imports — the `(legacy)`
  label predated `#693`'s cleanup and had gone stale. Moving the directory inside `ui-v2/` makes
  the dependency direction match the label ADR-022 already uses for the package.
- **`MythosPanel`'s intentional consumer is the design showcase** —
  `ui-v2/demos/EldritchEffectsDemo.tsx`, reached from the login screen's demo button
  (`MythosLoginForm.tsx` → `showDemo` → `AppRootViews` → `AppDemoView`, lazy-loaded via
  `appLazyScreens.tsx`). The demo lives under `ui-v2/demos/` (not `GameClientV2`, not the
  primitives barrel). Keep `MythosPanel` in the barrel while this showcase remains; do not
  treat the panel as an orphan to drop solely because production panels do not import it.
- **Barrel added on relocation.** The predecessor directory had no `index.ts` despite its old
  README instructing contributors to "update the index.ts file" — that file never existed. The
  barrel is new, and every consumer import was rewritten to go through it rather than a component's
  own path.
- **`EldritchIcon` re-exports `MythosIcons`** (`export { MythosIcons }` in `EldritchIcon.tsx`) in
  addition to `MythosIcons.ts` exporting it directly — a backward-compatibility shim from before
  the icon names were split into their own file, called out in-file as deliberate. The barrel
  re-exports `MythosIcons` from `EldritchIcon`, not from `MythosIcons.ts`, to match what existing
  call sites already destructured.

## 5. Constraints

**[SPEC]**

- `TerminalButton` and `TerminalInput` are `React.forwardRef` — callers relying on ref forwarding
  (e.g. focus management) must not wrap them in a way that breaks the ref chain.
- `ModalContainer`'s Escape-key handler is bound on `document` for the lifetime of `isOpen`, via a
  `useEffect` cleanup — nesting two open `ModalContainer`s registers two document-level listeners
  with no z-order awareness of which one Escape should close; the components do not coordinate
  with each other.
- **`exports` and `types` knip rules are `"off"`** in `client/knip.json` (only `files` is
  `"error"`) — an export added to `index.ts` that gains no consumer will **not** be flagged
  automatically. Cross-reference [`#718`](https://github.com/arkanwolfshade/MythosMUD/issues/718),
  which tracks knip's 94 unused-export/unused-type findings across the whole client once those
  rules are enabled.
- `ChannelSelector`'s `icon` field on `Channel` is typed `keyof typeof MythosIcons`, so a channel
  config referencing an icon name that doesn't exist in `MythosIcons` is a compile error, not a
  runtime blank icon.

## 6. Developer guide

**[NOTE]**

- **Adding a new primitive**: add the file, export it from `index.ts`, and add its test to
  `__tests__/`. Do not add a component-level README entry — the stub
  `ui-v2/primitives/README.md` points here rather than duplicating a component list.
- **Adding a new `MythosIcons` entry**: add it to `MythosIcons.ts` and the matching `iconMap` row
  in `EldritchIcon.tsx` in the same change — the type system will refuse to compile one without
  the other, but only once both files exist.
- **Mocking in tests**: `vi.mock()` targets the **concrete file path**
  (e.g. `'../primitives/EldritchIcon'`), never the barrel (`'../primitives'`) — mocking the
  barrel replaces every export it re-exports, not just the one symbol under test. Every existing
  test in this codebase that mocks a primitive follows this rule; keep new ones consistent.
- **Tests**: `client/src/components/ui-v2/primitives/__tests__/` — one file per component,
  Vitest + Testing Library, mirroring the source layout.

## 7. Troubleshooting

**[NOTE]**

- **A consumer's mock of a primitive silently stops taking effect**: check whether the mock
  targets the barrel path (`'../primitives'`) instead of the component's concrete file — barrel
  mocks replace the whole module and can mask or duplicate other symbols from the same import.
- **TypeScript error adding an icon**: `EldritchIcon`'s `iconMap` is `Record`-total over
  `MythosIcons` — a new `MythosIcons` key needs a same-change `iconMap` entry, not a follow-up.
- **An unused export in `index.ts` isn't caught by CI**: knip's `exports`/`types` rules are off
  project-wide (§5); this is a known gap, not a broken check.

## 8. Related docs

**[SPEC]**

- [ADR-022 — UI-v2 client transition](../architecture/decisions/ADR-022-ui-v2-client-transition.md) —
  the retirement-cluster decision record this package's relocation follows on from; its §6 `[NOTE]`
  records the move.
- [`docs/subsystems/README.md`](../subsystems/README.md) — the sibling reverse-engineered-doc
  family, behavioral rather than structural axis.
- [`docs/packages/README.md`](README.md) — the package coverage index this doc is entered into.

## 9. Changelog

**[SPEC]**

| Version | Date       | Change                                                                                                                |
| ------- | ---------- | --------------------------------------------------------------------------------------------------------------------- |
| 1.0.0   | 2026-09-16 | Initial version; relocated from `client/src/components/ui/` to `client/src/components/ui-v2/primitives/`, closes #744 |
