# DatabaseManager

> 24 nodes

## Key Concepts

- **DatabaseManager** (24 connections) — `server/database.py`
- **test_database.py** (7 connections) — `server/tests/unit/infrastructure/test_database.py`
- **.get_session_maker()** (5 connections) — `server/database.py`
- **test_database_manager_init_raises_when_instance_exists()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_manager_direct_init_raises()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_initial_state()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_reset_instance()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **test_database_manager_singleton()** (4 connections) — `server/tests/unit/infrastructure/test_database.py`
- **.close()** (3 connections) — `server/database.py`
- **.get_database_url()** (3 connections) — `server/database.py`
- **async_sessionmaker** (3 connections)
- **AsyncSession** (3 connections)
- **.__init__()** (2 connections) — `server/database.py`
- **Thread-safe singleton for database management. Manages database engine, session…** (1 connections) — `server/database.py`
- **Initialize the database manager.** (1 connections) — `server/database.py`
- **Get the async session maker, initializing if necessary. Returns:…** (1 connections) — `server/database.py`
- **Get the database URL, initializing if necessary. Returns: str: The database URL…** (1 connections) — `server/database.py`
- **Close database connections.** (1 connections) — `server/database.py`
- **Test DatabaseManager.__init__ raises when instance already exists.** (1 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Unit tests for database initialization.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test that DatabaseManager is a singleton.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test resetting the singleton instance.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test that direct initialization raises RuntimeError when instance exists.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`
- **Test initial state of database manager.** (1 connections) — `server/tests/unit/infrastructure/test_database.py`

## Relationships

- [DatabaseError](DatabaseError.md) (10 shared connections)
- [.reset_instance](reset_instance.md) (7 shared connections)
- [.get_instance](get_instance.md) (7 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (2 shared connections)
- [get_async_session](get_async_session.md) (2 shared connections)
- [get_session_maker](get_session_maker.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [get_database_path](get_database_path.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`

## Audit Trail

- EXTRACTED: 55 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*