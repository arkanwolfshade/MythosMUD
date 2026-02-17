# E2E Tests (Playwright)

End-to-end tests for the MythosMUD client run under this directory using
[Playwright](https://playwright.dev/) and `@playwright/test`.

## Running tests

- **Root config** (from `client/`): `npm run test` or `playwright test` — uses
  [playwright.config.ts](../../playwright.config.ts), runs `tests/**/*.spec.ts`.
- **Runtime E2E** (multiplayer, server-dependent): `npm run test:e2e:runtime` —
  uses [playwright.runtime.config.ts](playwright.runtime.config.ts), runs
  [runtime/](runtime/) specs. Requires server and client to be running (or
  started by the config in non-CI).

## Auth state

**Auth state is reused only in the di-migration validation suite**, via
`storageState`, to avoid repeating login in that single-session flow. **Runtime
multiplayer tests do not reuse auth state**; each player uses a fresh browser
context so that sessions are isolated and cross-player leakage is avoided. See
[runtime/fixtures/multiplayer.ts](runtime/fixtures/multiplayer.ts) and
[di-migration-validation.spec.ts](di-migration-validation.spec.ts).

## Fixtures and structure

- **Fixtures:** [runtime/fixtures/](runtime/fixtures/) — auth helpers
  (`auth.ts`), player helpers (`player.ts`), multiplayer context setup
  (`multiplayer.ts`), and test data.
- **Specs:** [runtime/](runtime/) is organized by feature (e.g. connection,
  combat, communication, character).
