# React Best-Practices Remediation Plan

## Scope

Analysis against [.cursor/rules/react.mdc](.cursor/rules/react.mdc). Scope: `client/src` (React/TypeScript).
Excludes test files except where they contain reusable components or patterns.

---

## 1. Critical: Missing onClick (Rule 7 - Semantic HTML)

**Finding:** [ChannelActivityIndicators.tsx](client/src/components/panels/chat/ChannelActivityIndicators.tsx)
renders a `div` with `role="button"`, `tabIndex={0}`, `onKeyDown`, but no `onClick`. Users can activate via
keyboard but not via mouse click.

**Action:** Add `onClick={() => onChannelSelect(channel.id)}` to the channel indicator div. (Done.)

---

## 2. No-op useEffects (Rule 6 - Common Pitfalls)

**Finding:** GameTerminal and GameTerminalPresentation registered window resize listeners that called a no-op.

**Action:** Remove the no-op effect entirely from both files; add comment. (Done.)

---

## 3. Div as Button (Rule 7 - Accessibility)

**Action:** No change. Document: "Div with role=button is acceptable when button cannot contain the required
block/complex content."

---

## 4. Modal role="dialog" Placement (Rule 7 - A11y)

**Action:** Move `role="dialog"`, `aria-modal="true"`, `aria-labelledby` to the inner content div. (Done.)

---

## 5. ESLint Suppressions Audit (Rule 6)

**Action:** Ensure each suppression has a one-line comment justifying it. (Done.)

---

## 6. Code Organization (Rule 2)

**Finding:** The rule recommends a `features/`-based bulletproof-react structure. The project uses
`components/`, `pages/`, `hooks/`, `contexts/` at top level. No `features/` directory exists.

**Action:** Document as out-of-scope for this remediation. Optional future refactor: gradually introduce
`features/` for cohesive domains (e.g. `features/auth/`, `features/game-terminal/`). Not required for
compliance.

---

## 7. Separation of Concerns (Rule 3)

**Finding:** Components like ProfessionSelectionScreen and StatsRollingScreen fetch data and render UI in the
same component. The rule prefers "smart" containers that use hooks and render "dumb" presentational components.

**Action:** Extract `useProfessions(baseUrl, authToken)` and `useStatsRolling(baseUrl, authToken, professionId,
profession, onError)` so that screens consume data and actions from hooks and focus on presentation. Build:
implement the hooks and refactor the screens to use them.

---

## 8. AsciiMapViewer Map Click (Rule 7)

**Action:** Add `role="img"` and `aria-label` to map div. (Done.)

---

## Implementation Order

| Priority | Item |
| -------- | ---- |
| 1 | ChannelActivityIndicators: add onClick (Done) |
| 2 | GameTerminal, GameTerminalPresentation: remove no-op useEffects (Done) |
| 3 | MainMenuModal: move role="dialog" to inner content div (Done) |
| 4 | Audit ESLint suppressions; add justification comments (Done) |
| 5 | AsciiMapViewer: add aria-label (Done) |
| 6 | Document features/ as out-of-scope; optional future refactor |
| 7 | Extract useProfessions(baseUrl, authToken); refactor ProfessionSelectionScreen |
| 8 | Extract useStatsRolling(...); refactor StatsRollingScreen |

---

## Verification

- Run client tests: `make test-client-coverage` (or equivalent)
- Run lint: `npm run lint` in client directory
