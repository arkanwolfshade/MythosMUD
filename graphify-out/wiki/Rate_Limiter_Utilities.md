# Rate Limiter Utilities

> 26 nodes

## Key Concepts

- **DatabaseManager** (29 connections) — `server/database.py`
- **._initialize_database()** (19 connections) — `server/database.py`
- **test_database.py** (7 connections) — `server/tests/unit/infrastructure/test_database.py`
- **.get_session_maker()** (6 connections) — `server/database.py`
- **.get_engine()** (5 connections) — `server/database.py`
- **async_sessionmaker** (5 connections)
- **_normalize_connect_args_search_path()** (4 connections) — `server/database.py`
- **.__init__()** (4 connections) — `server/database.py`
- **test_database_manager_singleton()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_reset_instance()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_direct_init_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_initial_state()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **.get_database_url()** (3 connections) — `server/database.py`
- **Any** (2 connections)
- **Ensure PostgreSQL search_path matches the target database schema name.** (2 connections) — `server/database.py`
- **Thread-safe singleton for database management.      Manages database engine, ses** (1 connections) — `server/database.py`
- **Initialize the database manager.** (1 connections) — `server/database.py`
- **Initialize database engine and session maker from configuration.          CRITIC** (1 connections) — `server/database.py`
- **Get the database engine, initializing if necessary.          Returns:** (1 connections) — `server/database.py`
- **Get the async session maker, initializing if necessary.          Returns:** (1 connections) — `server/database.py`
- **Get the database URL, initializing if necessary.          Returns:             s** (1 connections) — `server/database.py`
- **Unit tests for database initialization.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test that DatabaseManager is a singleton.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test resetting the singleton instance.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test that direct initialization raises RuntimeError when instance exists.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- *... and 1 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (12 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (12 shared connections)
- [Container Loot Helpers](Container_Loot_Helpers.md) (6 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (5 shared connections)
- [Holiday Persistence Models](Holiday_Persistence_Models.md) (4 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (4 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (4 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (3 shared connections)
- [Container Persistence Layer](Container_Persistence_Layer.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database.py`

## Audit Trail

- EXTRACTED: 99 (88%)
- INFERRED: 14 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*