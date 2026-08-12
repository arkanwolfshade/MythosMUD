# DatabaseManager

> 30 nodes

## Key Concepts

- **DatabaseManager** (24 connections) — `server/database.py`
- **._initialize_database()** (15 connections) — `server/database.py`
- **get_test_database_url()** (6 connections) — `server/database_config_helpers.py`
- **_create_engine_or_raise()** (6 connections) — `server/database.py`
- **configure_pool_settings()** (5 connections) — `server/database_config_helpers.py`
- **.get_session_maker()** (5 connections) — `server/database.py`
- **_sync_test_url_state()** (5 connections) — `server/database.py`
- **.get_engine()** (4 connections) — `server/database.py`
- **_dispose_engine_safely()** (4 connections) — `server/database.py`
- **_normalize_connect_args_search_path()** (4 connections) — `server/database.py`
- **AsyncEngine** (4 connections)
- **.close()** (3 connections) — `server/database.py`
- **.get_database_url()** (3 connections) — `server/database.py`
- **async_sessionmaker** (3 connections)
- **AsyncSession** (3 connections)
- **.__init__()** (2 connections) — `server/database.py`
- **Any** (2 connections)
- **Configure pool settings based on database URL and config. When full config is…** (1 connections) — `server/database_config_helpers.py`
- **Get test override database URL.** (1 connections) — `server/database_config_helpers.py`
- **Create async engine or raise a typed configuration/connection error.** (1 connections) — `server/database.py`
- **Dispose database engine with Windows/asyncpg-safe cleanup.** (1 connections) — `server/database.py`
- **Thread-safe singleton for database management. Manages database engine, session…** (1 connections) — `server/database.py`
- **Initialize the database manager.** (1 connections) — `server/database.py`
- **Initialize database engine and session maker from configuration. CRITICAL: This…** (1 connections) — `server/database.py`
- **Get the database engine, initializing if necessary. Returns: AsyncEngine: The…** (1 connections) — `server/database.py`
- *... and 5 more nodes in this community*

## Relationships

- [database.py](database.py.md) (8 shared connections)
- [log_and_raise](log_and_raise.md) (8 shared connections)
- [.get_instance](get_instance.md) (7 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (3 shared connections)
- [bundles/game.py](bundles-game.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (2 shared connections)
- [Invite](Invite.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)
- [get_config](get_config.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`

## Audit Trail

- EXTRACTED: 108 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*