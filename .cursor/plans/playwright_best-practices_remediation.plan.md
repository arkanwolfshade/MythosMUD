---
name: "Playwright Best-Practices Remediation "
overview: "Remediate MythosMUD client E2E tests and config against .cursor/rules/playwright.mdc: replace waitForTimeout with web-first waits, adopt robust locators, introduce a minimal Page Object layer, align config with CI/debugging guidance, add E2E README documenting auth state, and optionally add ESLint Playwright plugin. "
todos:
  - id: PW-1
    content: "Add screenshot and video to client/playwright.config.ts; optional reporter list "
    status: completed
  - id: PW-2
    content: "Set video to on-first-retry in playwright.runtime.config.ts; optional reporter "
    status: completed
  - id: PW-3
    content: "Add eslint-plugin-playwright for E2E test files in client "
    status: completed
  - id: PW-4
    content: "Create client/tests/e2e/README.md with auth-state note (di-migration only, not multiplayer) "
    status: completed
  - id: PW-5
    content: "Auth fixture and di-migration - use getByTestId for login (username, password, button) "
    status: completed
  - id: PW-6
    content: "Auth fixture and di-migration - use getByTestId/getByRole for MOTD and character selection "
    status: completed
  - id: PW-7
    content: "player.ts - use getByText or data-testid for posture; avoid brittle div:has-text "
    status: completed
  - id: PW-8
    content: "Replace waitForTimeout in auth.ts with web-first waits "
    status: completed
  - id: PW-9
    content: "Replace waitForTimeout and setTimeout in player.ts with web-first waits "
    status: completed
  - id: PW-10
    content: "Replace waitForTimeout in runtime specs (combat, connection, commands, error-handling, etc.) "
    status: completed
  - id: PW-11
    content: "Replace waitForTimeout in di-migration-validation.spec.ts "
    status: completed
  - id: PW-12
    content: "Add pages/ - LoginPage, CharacterSelectionPage, MotdPage (or equivalent) "
    status: completed
  - id: PW-13
    content: "Refactor auth.ts to use page objects "
    status: completed
  - id: PW-14
    content: "Refactor di-migration-validation.spec.ts to use page objects "
    status: cancelled
  - id: PW-15
    content: "Verification - run test:e2e:runtime and root Playwright test; check artifacts "
    status: completed
isProject: false
---

# Playwright Best-Practices Remediation Plan

## Scope

Analysis used [.cursor/rules/playwright.mdc](.cursor/rules/playwright.mdc). All E2E code lives under
[client/tests/e2e](client/tests/e2e); configs are [client/playwright.config.ts](client/playwright.config.ts)
and [client/tests/e2e/playwright.runtime.config.ts](client/tests/e2e/playwright.runtime.config.ts). The project
already uses `@playwright/test` throughout (Rule 1 satisfied). Assertions are mostly web-first
`expect(...).toBeVisible()` etc.; no `assert.equal`/`page.title()` anti-patterns found.

---

## 1. Eliminate `waitForTimeout` (Rule 3)

**Finding:** Many specs and fixtures use `page.waitForTimeout(ms)`, which is flaky and disallowed.

**Locations:** [client/tests/e2e/runtime/fixtures/auth.ts](client/tests/e2e/runtime/fixtures/auth.ts),
[client/tests/e2e/runtime/fixtures/player.ts](client/tests/e2e/runtime/fixtures/player.ts), and multiple
runtime specs (combat, connection, commands, error-handling, lucidity, muting, character, etc.),
plus [client/tests/e2e/di-migration-validation.spec.ts](client/tests/e2e/di-migration-validation.spec.ts).

**Action:** Replace each `waitForTimeout`/delay with a web-first wait (e.g. `expect(locator).toBeVisible({ timeout })`,
`locator.waitFor({ state: 'visible', timeout })`). Where no observable state exists, document the exception
or introduce a test-only signal.

---

## 2. Robust Locators (Rule 2)

**Finding:** Login and character flows use brittle CSS/placeholder locators. The app already exposes
`data-testid="username-input"`, `"password-input"`, `"login-button"` in [client/src/App.tsx](client/src/App.tsx),
and `data-testid="motd-enter-realm"`, `"command-input"` elsewhere.

**Action:** In auth fixture and di-migration, switch to `getByTestId('username-input')`, `getByTestId('password-input')`,
`getByTestId('login-button')`, and `getByTestId('motd-enter-realm')`. Replace character-selection locators with
`getByRole('heading', { name: /Select Your Character/i })` and `getByRole('button', { name: /Select Character/i })`;
add data-testids in the character selection UI if needed. In player.ts, use getByText or a stable test id for posture.

---

## 3. Page Object Model (Rule 4)

**Finding:** No dedicated Page Object classes; login/character/MOTD logic duplicated between auth.ts and
di-migration-validation.spec.ts.

**Action:** Introduce a small POM under `client/tests/e2e/runtime/pages/` (or shared `client/tests/e2e/pages/`):
**LoginPage**, **CharacterSelectionPage**, **MotdPage** (or equivalent). Refactor auth.ts and
di-migration-validation.spec.ts to use these page objects.

---

## 4. CI/CD Config: Trace, Screenshot, Video (Rule 7)

**Finding:** Root [client/playwright.config.ts](client/playwright.config.ts) has only `trace: 'on-first-retry'`;
no screenshot or video. Runtime config has screenshot and video but could align with rule.

**Action:** In root config, add `screenshot: 'only-on-failure'` and `video: 'on-first-retry'`. In runtime config,
optionally set `video: 'on-first-retry'`. Add `reporter: [['html'], ['list']]` in both if desired.

---

## 5. ESLint and Playwright Plugin (Rule 8)

**Finding:** [client/eslint.config.js](client/eslint.config.js) does not use `eslint-plugin-playwright`.

**Action:** Add `eslint-plugin-playwright` to devDependencies and a config block for E2E test files with
`plugin:playwright` and recommended rules. Keep existing overrides for Playwright config files.

---

## 6. E2E README and Auth State (Rule 5)

**Finding:** Runtime multiplayer tests intentionally use a fresh context per player (see
[client/tests/e2e/runtime/fixtures/multiplayer.ts](client/tests/e2e/runtime/fixtures/multiplayer.ts));
[client/tests/e2e/di-migration-validation.spec.ts](client/tests/e2e/di-migration-validation.spec.ts) reuses
auth via `storageState`. There is no short E2E README documenting this.

**Action:** Add a short E2E README (e.g. [client/tests/e2e/README.md](client/tests/e2e/README.md)) that documents:
auth state is reused only in di-migration (storageState) and not in multiplayer tests, to avoid cross-player
leakage; and any other concise E2E conventions (how to run runtime vs root config, where fixtures live).

---

## 7. Optional

- **Route blocking (Rule 5):** Optional: use `context.route('**/*.{png,jpg,...}', route => route.abort())` behind
  a flag or in a “fast” project for tests that do not need static assets.
- **Mock APIs (Rule 6):** E2E is full-stack; no change. Consider `page.route` for API mocking if adding UI-only flows.

---

## 8. Implementation Order and Risk

- **Low risk:** Config (trace/screenshot/video, reporter); ESLint Playwright plugin; getByTestId for login/MOTD;
  E2E README.
- **Medium risk:** Replacing all waitForTimeout with web-first waits.
- **Larger refactor:** Page objects and refactoring auth + di-migration.

Recommended order: (1) Config and ESLint; (2) E2E README; (3) Robust locators; (4) Replace waitForTimeout;
(5) POM and refactor auth/di-migration; (6) Optional route blocking.

---

## 9. Detailed Todos

- **PW-1** Add screenshot and video to [client/playwright.config.ts](client/playwright.config.ts): e.g.
  `screenshot: 'only-on-failure'`, `video: 'on-first-retry'`. Optionally add `reporter: [['html'], ['list']]`.
- **PW-2** In [client/tests/e2e/playwright.runtime.config.ts](client/tests/e2e/playwright.runtime.config.ts),
  set `video: 'on-first-retry'` to align with rule; optionally add list reporter.
- **PW-3** Add `eslint-plugin-playwright` to client devDependencies; in [client/eslint.config.js](client/eslint.config.js)
  add a block for E2E files (e.g. `tests/e2e/**/*.ts`) with `plugin:playwright` and recommended rules.
- **PW-4** Create [client/tests/e2e/README.md](client/tests/e2e/README.md) with a short note that auth state is
  reused only in di-migration (storageState) and not in multiplayer tests, to avoid cross-player leakage; include
  how to run runtime vs root Playwright config and where fixtures live.
- **PW-5** In [client/tests/e2e/runtime/fixtures/auth.ts](client/tests/e2e/runtime/fixtures/auth.ts) and
  [client/tests/e2e/di-migration-validation.spec.ts](client/tests/e2e/di-migration-validation.spec.ts), switch login
  form to `getByTestId('username-input')`, `getByTestId('password-input')`, and `getByTestId('login-button')`.
- **PW-6** In auth.ts and di-migration-validation.spec.ts, use `getByTestId('motd-enter-realm')` (or getByRole for
  “Enter the Realm”) and replace character-selection locators with getByRole for heading/buttons; add data-testids
  in character selection UI if needed.
- **PW-7** In [client/tests/e2e/runtime/fixtures/player.ts](client/tests/e2e/runtime/fixtures/player.ts), use
  getByText or a stable data-testid for the posture section instead of
  `page.locator('div:has-text("Posture")').filter({ hasText: 'standing' })`.
- **PW-8** Replace all `waitForTimeout` and equivalent delays in [client/tests/e2e/runtime/fixtures/auth.ts](client/tests/e2e/runtime/fixtures/auth.ts)
  with web-first waits (expect(locator).toBeVisible, waitForSelector, etc.).
- **PW-9** Replace `new Promise(r => setTimeout(r, ms))` and any waitForTimeout in
  [client/tests/e2e/runtime/fixtures/player.ts](client/tests/e2e/runtime/fixtures/player.ts) with web-first waits
  where possible.
- **PW-10** Replace `waitForTimeout` in runtime specs: combat-messages-game-info, basic-connection, clean-game-state,
  disconnect-grace-period, logout-errors, whisper-rate-limiting, sanitarium-failover, muting-system-emotes,
  rest-command, logout-accessibility, local-channel-errors, character-selection, character-name-uniqueness,
  multi-character-creation, character-deletion (and any other specs that use it).
- **PW-11** Replace `waitForTimeout(timeout)` in [client/tests/e2e/di-migration-validation.spec.ts](client/tests/e2e/di-migration-validation.spec.ts)
  with a web-first wait.
- **PW-12** Add page objects under `client/tests/e2e/runtime/pages/` (or `client/tests/e2e/pages/`): LoginPage
  (navigate, username/password/submit locators, login(username, password)), CharacterSelectionPage (heading,
  Select Character / Create / Delete buttons, selectFirstCharacter etc.), MotdPage (Enter the Realm, enterRealm()).
- **PW-13** Refactor [client/tests/e2e/runtime/fixtures/auth.ts](client/tests/e2e/runtime/fixtures/auth.ts) to call
  LoginPage, CharacterSelectionPage, and MotdPage instead of inlining selectors and actions.
- **PW-14** Refactor [client/tests/e2e/di-migration-validation.spec.ts](client/tests/e2e/di-migration-validation.spec.ts)
  to use the same page objects for login, character selection, and MOTD where the flow overlaps.
  _(Cancelled: di-migration keeps its own long local login flow with debug listeners and safeWait;
  shared auth fixture and page objects are used for runtime specs only.)_
- **PW-15** Verification: Run `npm run test:e2e:runtime` (and root `npm run test` if it runs Playwright); confirm
  no new flakiness; confirm trace/screenshot/video artifacts on failure/retry; run ESLint on client/tests/e2e and
  fix any new findings.

---

## 10. Verification

- Run `make test-playwright` or `npm run test:e2e:runtime` (and root Playwright if applicable) after changes.
- Confirm no new flakiness; trace/screenshot/video artifacts appear on failure/retry as configured.
- Run ESLint on `client/tests/e2e/**` and fix any new Playwright-plugin findings.
