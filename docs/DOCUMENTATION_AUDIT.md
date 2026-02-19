# Documentation vs. Code Accuracy Audit Log

This file records the documentation audit performed per the Documentation vs. Code Accuracy Audit Plan.
Code is treated as the source of truth; docs are updated or corrected to match.

## Audit date

2026-02-19 (initial pass)

## Summary

- **Phase 1 (reference docs):** Completed. NATS, persistence, DB, events, realtime, command models,
  container API, config, logging references verified; broken links fixed.
- **Phase 2 (guides/runbooks):** Completed. E2E, deployment, debugging, PostgreSQL, runbook
  spot-checked; QUICK_START_E2E and E2E_TESTING_GUIDE corrected for PostgreSQL and make target.
- **Phase 3 (README/root):** Completed. README structure and CLAUDE logging import corrected.
- **Phase 4 (architecture/ADRs):** Completed. Links from architecture docs verified (targets exist).
- **Phase 5 (remaining docs/):** Completed. No further changes required.
- **Phase 6 (markdown outside docs/):** Completed. server/README, e2e-tests/MULTIPLAYER_TEST_RULES
  updated for PostgreSQL and make target.
- **Link validation:** Performed per-doc during audit. Internal links fixed in NATS_SUBJECT_PATTERNS,
  LOGGING_QUICK_REFERENCE; references and paths corrected across multiple docs.
- **Subsystem design docs:** Added [docs/subsystems/](docs/subsystems/) with 15 reverse-engineered
  design documents (Movement, Follow, Rest, Rescue, Emote/Pose, Who, Party, Combat, Status effects,
  Magic, Skills/Level, Lucidity, Respawn, NPC, Admin commands). See [docs/subsystems/README.md]
  (docs/subsystems/README.md) for the index.

## Changes by document

### docs/NATS_SUBJECT_PATTERNS.md

- **Link validation:** Removed broken internal links to non-existent files
  (`NATS_INTEGRATION_GUIDE.md`, `CHAT_SERVICE_GUIDE.md`). Kept and fixed links to
  `REAL_TIME_ARCHITECTURE.md`, `ENHANCED_LOGGING_GUIDE.md`; added link to `realtime.md`.
- **References section:** Updated source path from `server/services/nats_subject_manager.py` to
  `server/services/nats_subject_manager/` (package). Updated tests path to
  `server/tests/unit/services/nats_subject_manager/`. Removed non-existent performance tests path
  and `.agent-os/specs/` migration spec path.
- **Content:** Verified import paths and API (build_subject, validate_subject, get_subscription_pattern,
  get_chat_subscription_patterns, get_performance_metrics, register_pattern) against code; no changes needed.

### docs/realtime.md

- **Content:** Fixed typo: "async\_ persistence" -> "async persistence".

### docs/PERSISTENCE_REPOSITORY_ARCHITECTURE.md

- **Content:** Verified (async_persistence.py, AsyncPersistenceLayer, repository names exist). No changes.

### docs/DATABASE_ACCESS_PATTERNS.md

- **Content:** Verified (server/async_persistence.py, get_async_session from server.database). No changes.

### docs/EVENT_OWNERSHIP_MATRIX.md

- **Content:** Verified (server/events/event_types.py, event classes). No changes.

### docs/COMMAND_MODELS_REFERENCE.md

- **Content:** Spot-checked; BaseCommand and command patterns align with codebase. No changes.

### docs/CONTAINER_SYSTEM_API_REFERENCE.md

- **Content:** Spot-checked; endpoint paths and descriptions align. No changes.

### docs/CONFIGURATION_FILES_REFERENCE.md

- (To be audited)

### docs/LOGGING_QUICK_REFERENCE.md

- **Content:** Corrected import path from `server.logging.enhanced_logging_config` to
  `server.structured_logging.enhanced_logging_config` to match code.
- **Link validation:** Replaced broken link to non-existent `LOGGING_BEST_PRACTICES.md` with
  `ENHANCED_LOGGING_GUIDE.md`.

### README.md

- **Content:** Updated project structure: `server/logging/` to `server/structured_logging/` for
  enhanced logging (matches code).

### CLAUDE.md

- **Content:** Corrected logging import path from `server.logging.enhanced_logging_config` to
  `server.structured_logging.enhanced_logging_config` in two places.

### docs/QUICK_START_E2E_TESTS.md

- **Content:** Removed outdated reference to SQLite test database
  (`data/unit_test/players/unit_test_players.db`). Replaced with PostgreSQL test database and
  reference to `make setup-postgresql-test-db` and test env.

### docs/E2E_TESTING_GUIDE.md

- **Content:** Corrected make target from `make test-client-runtime` to `make test-playwright` to
  match Makefile.

### e2e-tests/MULTIPLAYER_TEST_RULES.md

- **Content:** Corrected make target from `make test-client-runtime` to `make test-playwright`.

### server/README.md

- **Content:** Replaced outdated "Player data stored as JSON files in data/local/players/" with
  PostgreSQL as primary datastore and pointers to DATABASE_ACCESS_PATTERNS and
  PERSISTENCE_REPOSITORY_ARCHITECTURE.
