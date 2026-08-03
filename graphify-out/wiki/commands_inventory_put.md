# commands inventory put

> 8 nodes

## Key Concepts

- **close_db()** (9 connections) — `server/database_helpers.py`
- **test_close_db_engine_initialization_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_success()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_raises_runtime_error_on_failure()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Close database connections.** (1 connections) — `server/database_helpers.py`
- **Test close_db successfully closes database connections.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test close_db raises RuntimeError when closing fails.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test close_db handles failure when engine initialization fails.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`

## Relationships

- [lucidity npc combat](lucidity_npc_combat.md) (4 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)
- [command commands talk](command_commands_talk.md) (1 shared connections)
- [npc idle movement](npc_idle_movement.md) (1 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)
- [command inventory models](command_inventory_models.md) (1 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 22 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*