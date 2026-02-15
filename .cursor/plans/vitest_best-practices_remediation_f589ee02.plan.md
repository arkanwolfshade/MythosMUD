---
name: Vitest Best-Practices Remediation
overview: "Remediate client Vitest tests and config against .cursor/rules/vitest.mdc: fix file naming and exclusions, replace arbitrary setTimeout waits with vi.waitFor where applicable, fix manual global fetch assignment, optionally add mock cleanup audits and .concurrent for independent tests."
todos:
  - id: VIT-1
    content: Rename all 7 *.spec.tsx to *.test.tsx; fix mock/import paths; remove **/*.spec.* from vitest.config.ts
    status: completed
  - id: VIT-2
    content: "useWebSocketConnection.test.ts: replace setTimeout(0) with vi.waitFor or waitFor(condition)"
    status: completed
  - id: VIT-3
    content: "LogoutFlow.integration (src/__tests__): replace 100ms wait with waitFor(observable condition)"
    status: completed
  - id: VIT-4
    content: "StatRollingWithProfessionRequirements: use vi.spyOn(global,'fetch') or vi.stubGlobal + restore"
    status: completed
  - id: VIT-5
    content: Audit vi.mock/vi.spyOn files for afterEach cleanup (clearAllMocks or mockRestore)
    status: completed
  - id: VIT-6
    content: "Optional: vi.useFakeTimers/advanceTimersByTime in App.test.tsx and LogoutFlow mocks"
    status: completed
  - id: VIT-7
    content: "Optional: add describe.concurrent / it.concurrent for independent suites; destructure expect"
    status: completed
  - id: VIT-8
    content: "Verification: npm run test and vitest run --coverage in client; fix any .spec inclusion failures"
    status: completed
isProject: false
---

# Vitest Best-Practices Remediation Plan

## Scope

Analysis used [.cursor/rules/vitest.mdc](.cursor/rules/vitest.mdc). All Vitest usage is in the **client** ([client/vitest.config.ts](client/vitest.config.ts)); config already has `environment: 'happy-dom'`, `globals: true`, V8 coverage, and sensible thresholds (Rule 5, 7 satisfied). No `test(` usage found; suites use `it(` (Rule 2). Below are the findings and recommended fixes.

---

## 1. File Naming and Exclusions (Rule 1)

**Finding:** Rule requires `*.test.{ts,tsx}`. The project has **7 files** named `*.spec.tsx`:

- [client/src/components/panels/**tests**/game-log-panel.spec.tsx](client/src/components/panels/__tests__/game-log-panel.spec.tsx)
- [client/src/components/panels/**tests**/command-panel.spec.tsx](client/src/components/panels/__tests__/command-panel.spec.tsx)
- [client/src/components/panels/**tests**/chat-panel.spec.tsx](client/src/components/panels/__tests__/chat-panel.spec.tsx)
- [client/src/components/**tests**/performance.spec.tsx](client/src/components/__tests__/performance.spec.tsx)
- [client/src/components/**tests**/game-terminal-integration.spec.tsx](client/src/components/__tests__/game-terminal-integration.spec.tsx)
- [client/src/components/**tests**/game-log-panel.spec.tsx](client/src/components/__tests__/game-log-panel.spec.tsx)
- [client/src/components/**tests**/command-panel.spec.tsx](client/src/components/__tests__/command-panel.spec.tsx)

[client/vitest.config.ts](client/vitest.config.ts) **excludes** `**/*.spec.ts` and `**/*.spec.tsx`, so these specs are never run by Vitest. At least one has a broken mock path (e.g. `vi.mock('../src/components/ui/EldritchIcon', ...)` from inside `panels/__tests__/`), which would resolve incorrectly.

**Action (Option A):** Rename all `*.spec.tsx` to `*.test.tsx`, fix any mock/import paths (e.g. correct `vi.mock` paths from inside `panels/__tests__/` and `components/__tests__/`), and remove the `**/*.spec.ts` and `**/*.spec.tsx` entries from [client/vitest.config.ts](client/vitest.config.ts) so these tests run under Vitest.

---

## 2. Async Testing: Replace Arbitrary Waits with vi.waitFor (Rule 3)

**Finding:** Rule says to use `vi.waitFor` for polling conditions and avoid `await new Promise(resolve => setTimeout(resolve, N))` before assertions.

| Location                                                                                                                                           | Current pattern                                                                           | Recommendation                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [client/src/hooks/**tests**/useWebSocketConnection.test.ts](client/src/hooks/__tests__/useWebSocketConnection.test.ts) ~L1500                      | `await new Promise(resolve => setTimeout(resolve, 0));` to "flush effects" after rerender | Replace with `vi.waitFor` (or RTL `waitFor`) on an observable condition (e.g. ref/callback updated) if possible; otherwise document as intentional yield. |
| [client/src/components/**tests**/LogoutFlow.integration.test.tsx](client/src/components/__tests__/LogoutFlow.integration.test.tsx) L57, L275, L424 | `setTimeout(resolve, 10)` / 100ms inside **mock** implementation                          | Mock is simulating async behavior; acceptable. Optional: use `vi.useFakeTimers()` and `vi.advanceTimersByTime()` to avoid real delay.                     |
| [client/src/**tests**/LogoutFlow.integration.test.tsx](client/src/__tests__/LogoutFlow.integration.test.tsx) L116–118                              | Comment says "simulate server logout command delay"; 100ms wait in test                   | Prefer asserting on observable state with `vi.waitFor` (or RTL `waitFor`) instead of fixed 100ms.                                                         |
| [client/src/App.test.tsx](client/src/App.test.tsx) L1196–1205, L1251–1265                                                                          | `setTimeout` inside **fetch mock** to simulate network delay                              | Acceptable (mock behavior). Optional: fake timers to avoid real 100ms.                                                                                    |
| [client/src/utils/**tests**/performanceTester.test.ts](client/src/utils/__tests__/performanceTester.test.ts) L49, L80                              | `setTimeout` inside the **function under test** (async test function)                     | Acceptable; not "wait then assert."                                                                                                                       |

**Action:** Focus on useWebSocketConnection (replace `setTimeout(0)` with a condition-based wait where feasible) and the LogoutFlow 100ms wait (replace with `waitFor` on an observable condition). Leave mock-internal delays and performanceTester SUT behavior as-is unless adopting fake timers project-wide.

---

## 3. Mocking: Manual Global Overwrite (Rule 4)

**Finding:** Rule says use `vi.fn()` / `vi.spyOn()` / `vi.mock()` and avoid manual assignment without cleanup.

- **[client/src/tests/StatRollingWithProfessionRequirements.test.tsx](client/src/__tests__/StatRollingWithProfessionRequirements.test.tsx)** (currently excluded in vitest.config): Uses `global.fetch = fetchSpy` (L6–7) and in `afterEach` calls `fetchSpy.mockRestore()`. For a plain `vi.fn()` assigned to `global.fetch`, `mockRestore()` does **not** restore `global.fetch`, so this leaks the mock and is a semantic error.

**Action:** In StatRollingWithProfessionRequirements.test.tsx, replace with `vi.spyOn(global, 'fetch')` (or `vi.stubGlobal('fetch', fetchSpy)` and restore the original in `afterEach`). Then the existing afterEach cleanup will correctly restore `global.fetch`. Apply when/if the file is re-enabled in the config.

---

## 4. Mock Cleanup Audit (Rule 4)

**Finding:** Rule: "Always clean up mocks after each test." Many files already use `beforeEach(vi.clearAllMocks())` or `afterEach(mockRestore)` (e.g. roomHandlers, memoryLeakDetector). A subset of the ~70+ files that use `vi.mock` may lack consistent cleanup.

**Action:** Audit test files that use `vi.mock` or `vi.spyOn` to ensure either (1) `afterEach(() => { vi.clearAllMocks(); })` or (2) `afterEach(() => { spy.mockRestore(); })` (for global spies) so mocks do not leak between tests. Prioritize files that mock globals or shared modules.

---

## 5. Optional: Fake Timers for Delays

**Finding:** Several tests use real `setTimeout` inside mocks (App.test.tsx, LogoutFlow.integration) to simulate delays. Rule discourages arbitrary waits; it does not forbid delays inside mocks but suggests reliable synchronization.

**Action:** Optionally introduce `vi.useFakeTimers()` / `vi.advanceTimersByTime()` in those tests to avoid real wall-clock waits and make timing deterministic. Lower priority than items 1–4.

---

## 6. Optional: .concurrent (Rule 6)

**Finding:** No `describe.concurrent` or `it.concurrent` in the codebase. Rule recommends using `.concurrent` for independent tests to speed up the suite.

**Action:** Identify suites that are side-effect-free and independent (e.g. pure util or handler tests), and add `describe.concurrent` or `it.concurrent` where appropriate. When using `.concurrent`, destructure `expect` from the test context: `it.concurrent('...', async ({ expect }) => { ... })`. Low priority; validate no shared state or order dependence first.

---

## 7. Co-location (Rule 1)

**Finding:** Rule says place test files "directly next to" the component or module. The project uses `__tests__/` subdirs next to a module (e.g. `components/Button/__tests__/Button.test.tsx`) and a few at `src/__tests__/` for app-level flows. This is a common pattern and is considered "next to" the module/feature.

**Action:** No change required unless you want to move every test to a strict `ComponentName.test.tsx` beside the single source file; that would be a large refactor and is optional.

---

## Implementation Order and Risk

| Priority | Item                                                                                        | Risk                |
| -------- | ------------------------------------------------------------------------------------------- | ------------------- |
| 1        | Fix StatRollingWithProfessionRequirements global.fetch (when re-enabling)                   | Low                 |
| 2        | .spec → .test naming (option A); fix mock/import paths; remove _/_.spec. from vitest.config | Medium (path fixes) |
| 3        | useWebSocketConnection: replace setTimeout(0) with vi.waitFor / waitFor on condition        | Low                 |
| 4        | LogoutFlow 100ms: replace with waitFor(condition)                                           | Low                 |
| 5        | Audit vi.mock/vi.spyOn cleanup across client test files                                     | Low                 |
| 6        | Optional: fake timers for mock delays; .concurrent for independent suites                   | Low                 |

---

## Verification

- Run `npm run test` (or client Vitest script) from project root after changes; ensure no regressions.
- Run `vitest run --coverage` in client and confirm coverage thresholds still pass.
- If .spec files are re-included, run the full suite and fix any path/mock errors until green.
