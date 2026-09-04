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

### Serial suite vs one-off scenarios

[playwright.runtime.config.ts](playwright.runtime.config.ts) sets `workers: 1` and
`fullyParallel: false` by default (shared test accounts, one server DB).

**Opt-in parallel** (separate worker processes; start server and Vite yourself):

```powershell
$env:E2E_RUNTIME_PARALLEL = "1"
$env:E2E_WORKERS = "2"
..\..\scripts\e2e-run-parallel.ps1
```

Parallel mode skips Playwright `webServer` startup.

To run **one file** or **grep** a subset (from `client/`):

```text
npm run test:e2e:runtime -- tests/e2e/runtime/communication/chat-messages.spec.ts
npm run test:e2e:runtime -- --grep "Character Selection"
```

Extra arguments after `--` are passed to the Playwright CLI.

## Local database bootstrap (mythos_e2e)

From the **repository root**, use `e2e.bat` (Windows) or:

```text
powershell -ExecutionPolicy Bypass -File scripts/bootstrap_e2e_database.ps1
```

That force-recreates PostgreSQL `mythos_e2e` (DDL, migrations, procedures) and runs
`scripts/seed_e2e_users.py`. Requires `.env.e2e_test` (copy from `env.e2e_test.example`).

`runtime/global-setup.ts` still runs `seed_e2e_users.py` and `verify_e2e_users_seeded.py`
before specs as an **idempotent** safety net if you skip the full bootstrap. Any bootstrap
failure throws, writes `logs/e2e_test/bootstrap-errors.log`, and exits Playwright with a
non-zero code. `make test-playwright` runs integration pytest **only** when Playwright passes
(`scripts/run_test_playwright.ps1`).

## E2E accounts (mythos_e2e)

On a fresh DB, seeding creates exactly:

- **ArkanWolfshade** / `Cthulhu1` — admin user and admin character (multiplayer / admin commands).
- **Ithaqua** / `Cthulhu1` — regular user and character (also used for character-creation specs).

Both seeded characters start in **DEFAULT_RESPAWN_ROOM** (matches
`server.constants.spawn_defaults`; mirrored as `DEFAULT_RESPAWN_ROOM` in
[runtime/fixtures/test-data.ts](runtime/fixtures/test-data.ts)).

Uses `DATABASE_URL` and `POSTGRES_SEARCH_PATH` from `.env.e2e_test` when present; otherwise defaults to
`mythos_e2e`. Safe to re-run; existing users and character names are skipped.

## Auth state

**Auth state is reused only in the di-migration validation suite**, via
`storageState`, to avoid repeating login in that single-session flow. **Runtime
multiplayer tests do not reuse auth state**; each player uses a fresh browser
context so that sessions are isolated and cross-player leakage is avoided. See
[runtime/fixtures/multiplayer.ts](runtime/fixtures/multiplayer.ts) and
[di-migration/](di-migration/) (`suite-*.spec.ts`).

### DI migration validation (optional)

From `client/`:

```text
npx playwright test tests/e2e/di-migration --timeout=600000
npx playwright test tests/e2e/di-migration -g "Suite 1"
```

## Fixtures and structure

- **Fixtures:** [runtime/fixtures/](runtime/fixtures/) — auth helpers
  (`auth.ts`), player helpers (`player.ts`), multiplayer context setup
  (`multiplayer.ts`), and test data.
- **Specs:** [runtime/](runtime/) is organized by feature (e.g. connection,
  combat, communication, character).
