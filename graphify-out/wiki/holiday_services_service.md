# holiday services service

> 10 nodes

## Key Concepts

- **test_database.py** (7 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_singleton()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_reset_instance()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_direct_init_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_initial_state()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Unit tests for database initialization.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test that DatabaseManager is a singleton.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test resetting the singleton instance.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test that direct initialization raises RuntimeError when instance exists.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test initial state of database manager.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`

## Relationships

- [Database Access Layer](Database_Access_Layer.md) (7 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (2 shared connections)
- [combat npc services](combat_npc_services.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_database.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*