# models profession rationale

> 15 nodes

## Key Concepts

- **close_db()** (9 connections) — `server/database.py`
- **get_engine()** (8 connections) — `server/database.py`
- **.get_engine()** (5 connections) — `server/database.py`
- **test_get_engine_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **AsyncEngine** (4 connections)
- **.close()** (3 connections) — `server/database.py`
- **test_close_db_success()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_close_db_error()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Get the database engine, initializing if necessary.          Returns:** (1 connections) — `server/database.py`
- **Close database connections.** (1 connections) — `server/database.py`
- **Close database connections.      This closes the database manager's engine and c** (1 connections) — `server/database.py`
- **Get the database engine from DatabaseManager.      Returns:         AsyncEngine:** (1 connections) — `server/database.py`
- **Test get_engine initializes database if not already initialized.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test close_db closes database successfully.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test close_db raises RuntimeError on error.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`

## Relationships

- [command player state](command_player_state.md) (6 shared connections)
- [aggro threat services](aggro_threat_services.md) (3 shared connections)
- [game models enums](game_models_enums.md) (3 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 42 (89%)
- INFERRED: 5 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*