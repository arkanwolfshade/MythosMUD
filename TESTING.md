# MythosMUD Testing Strategy (Greenfield Suite)

**Note**: This is the new greenfield test suite. The previous test suite has
been moved to `server/tests_backup_original/` for reference.

## Tiers and commands

Unit (fast, no real DB/files, pure logic): `pytest -m "unit and not slow" server/tests`

- Integration (real Postgres, minimal mocks): `pytest -m "integration and not

  slow" server/tests`

- E2E / Playwright: follow `e2e-tests/` playbooks; typically sequential.
- Slow/perf: run explicitly (`-m slow`) outside the fast lanes.

See `server/tests/README.md` for detailed documentation on the test suite structure.

## Isolation rules

No server startups inside tests. Never run tests from `/server/`; run from
  repo root.

- Env vars are process-global: tests that mutate env must be

  `@pytest.mark.serial` + `@pytest.mark.xdist_group`.

- Unit tier: forbid real network/DB/filesystem writes; use fakes/mocks;

  deterministic seeds.

- Integration tier: use ephemeral Postgres per run; truncate/rollback between

  tests; no cross-worker shared mutable state.

## Markers

`unit`, `integration`, `e2e`, `slow`, `serial`, `xdist_group(name=...)`.

- Default parallel only for tests proven side-effect free; serial+group for

  env or global singletons.

- Auto-marking by path: `server/tests/unit/*` -> unit,

  `server/tests/integration/*` -> integration,
  `server/tests/e2e/*` -> e2e.

## Coverage policy

Critical codepaths (auth/security, commands/validators, services/persistence,
  runtime config, events/realtime, API surface, security utilities) must reach
  **≥90%** coverage.

- All other code must reach **≥70%** coverage (global floor enforced).

- Critical set is defined by path patterns (enforced in CI); see

  `.coveragerc` notes and CI checks.

- Draft critical patterns (update in CI when finalized):

  - `server/auth/**`, `server/auth_utils.py`

  - `server/config/__init__.py`, `server/config/models.py`

  - `server/commands/**`, `server/validators/**`, `server/utils/command_*`,

    `server/command_handler_unified.py`, `server/utils/command_processor.py`

  - `server/services/**`, `server/persistence/**`,

    `server/async_persistence.py`, `server/database.py`, `server/models/**`

  - `server/events/**`, `server/realtime/**`
  - `server/api/**`, `server/routes/**`, `server/security_utils.py`, `server/exceptions.py`

## Fixtures/layout

Tiered fixtures: `tests/fixtures/unit/` (pure fakes),
  `tests/fixtures/integration/` (real DB/session factory), shared builders in
  `tests/fixtures/shared/`.

- Avoid module-level mutable globals in fixtures; prefer factories returning

  fresh instances.

- Use `pytest-timeout` defaults; keep test-specific timeouts minimal.

- Ephemeral Postgres for integration: enable via `integration_db_url` fixture

  (uses `PYTEST_EPHEMERAL_DB=1` by default).

## Mocking standards

Unit: allow mocks/fakes; prefer `autospec=True`; patch narrow surfaces.

- Integration: prefer real collaborators; only mock external services.

- Never mock model classes that SQLAlchemy selects against.

- Use `strict_mocker` fixture (`tests/fixtures/unit/mock_helpers.py`) for

  autospec-by-default patching.

## What to run when

PR/CI fast lane: unit subset (`-m "unit and not slow"`) + critical
  integration smoke.

- Nightly/merge gate: full integration + coverage + selected E2E.
- Local troubleshooting: smallest reproducer with markers, then widen scope.

## Logging and diagnostics

Use structured logging (`get_logger`) if asserting logs; no print debugging
  in committed tests.

- Keep per-test data under `server/tests/data/` only; do not create DB files elsewhere.
