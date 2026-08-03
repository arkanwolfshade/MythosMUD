# room persistence loader

> 10 nodes

## Key Concepts

- **init_db()** (8 connections) — `server/database_helpers.py`
- **test_init_db_success()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_init_db_raises_on_error()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_init_db_configure_mappers_failure()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_init_db_connection_verification_failure()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Initialize database connection and verify configuration.      NOTE: DDL (table c** (1 connections) — `server/database_helpers.py`
- **Test init_db successfully initializes database.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test init_db raises exception on initialization failure.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test init_db raises exception when configure_mappers fails.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test init_db raises exception when connection verification fails.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`

## Relationships

- [lucidity npc combat](lucidity_npc_combat.md) (5 shared connections)
- [command commands talk](command_commands_talk.md) (1 shared connections)
- [npc idle movement](npc_idle_movement.md) (1 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*