# .initialize

> 23 nodes

## Key Concepts

- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **asyncio** (12 connections)
- **init_db()** (10 connections) — `server/database.py`
- **test_get_async_session_rollback_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_on_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_close_db_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_close_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_http_exception_re_raised()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_init_db_connection_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_init_db_import_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_init_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Initialize core services. No dependencies.** (1 connections) — `server/container/bundles/core.py`
- **Initialize the database (deprecated - kept for backward compatibility). This…** (1 connections) — `server/database.py`
- **Test get_async_session creates and yields session successfully.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test get_async_session re-raises HTTPException.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test get_async_session rolls back on error.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test get_async_session handles rollback errors.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test init_db initializes database successfully.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test init_db handles import errors.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test init_db handles connection errors.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test close_db closes database successfully.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **Test close_db raises RuntimeError on error.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`

## Relationships

- [test_database_extended.py](test_database_extended.py.md) (13 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [DatabaseManager](DatabaseManager.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [ValueError](ValueError.md) (2 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (1 shared connections)
- [npc_database.py](npc_database.py.md) (1 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)
- [TrackedTaskManager](TrackedTaskManager.md) (1 shared connections)
- [DistributedEventBus](DistributedEventBus.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)

## Source Files

- `server/container/bundles/core.py`
- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 57 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*