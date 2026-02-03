---
name: mythosmud-test-writing
description: Write and run MythosMUD tests: server tests under server/tests/unit|integration, client under client; use make test or make test-comprehensive from project root only. Use when adding tests, interpreting test failures, or when the user asks about test layout or coverage.
---

# MythosMUD Test Writing

## Where Tests Live

| Area | Location | Notes |
|------|----------|--------|
| Server unit | `server/tests/unit/` | By module, e.g. `server/tests/unit/events/` |
| Server integration | `server/tests/integration/` | Cross-component tests |
| Client | `client/` | Per project structure (e.g. `__tests__` next to source) |
| Fixtures/utilities | `server/tests/fixtures/` | Mixins, helpers only — not test classes |

## How to Run Tests

- **Always from project root.** Never run tests from `server/` or `client/` as the sole working directory.
- **Never** use `python -m pytest` from `server/`; use the Makefile from project root.

| Goal | Command |
|------|--------|
| Fast suite (unit + critical integration) | `make test` |
| Full suite (all tests, including slow) | `make test-comprehensive` or `make test-ci` |
| Server only | `make test-server` |
| Server with coverage | `make test-server-coverage` |
| Client only | `make test-client` |
| Client with coverage | `make test-client-coverage` |
| All with coverage | `make test-coverage` |

## Coverage

- **Minimum:** 70% overall for new code.
- **Critical code:** 90% (security, core features, user-facing code).

## Rules

- Tests must **test server/client code**, not test infrastructure or Python built-ins.
- When a bug is fixed, add or extend a test that would have caught it.
- Exclude `test_player_stats.py` from coverage as per project config.

## Reference

- Full rules: [CLAUDE.md](../../CLAUDE.md) "TESTING REQUIREMENTS"
- Server remediation: [.cursor/commands/server-test-remediation.md](../../commands/server-test-remediation.md)
- Client remediation: [.cursor/commands/client-test-remediation.md](../../commands/client-test-remediation.md)
- Makefile: [Makefile](../../Makefile) (test, test-server, test-client, test-coverage, test-comprehensive)
