# manager subject services

> 24 nodes

## Key Concepts

- **get_async_session()** (13 connections) — `server/database_helpers.py`
- **get_session_maker()** (9 connections) — `server/database_helpers.py`
- **test_get_session_maker_raises_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **AsyncSession** (4 connections)
- **test_get_session_maker()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_success()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_http_exception_propagates()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_on_error()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_failure()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_http_exception_passthrough()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_finally_block_executes()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_success()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Dependency to get NPC database session.      Yields:         AsyncSession: Datab** (2 connections) — `server/npc_database.py`
- **Get the async session maker, initializing if necessary.      Returns:         as** (1 connections) — `server/database_helpers.py`
- **Dependency to get database session.      Yields:         AsyncSession: Database** (1 connections) — `server/database_helpers.py`
- **Test get_session_maker returns session maker from DatabaseManager.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_session_maker raises ValidationError when database cannot be initialize** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_async_session yields session and handles cleanup.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_async_session re-raises HTTPException without rollback.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_async_session rolls back on exception.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_async_session handles rollback failure.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_async_session re-raises HTTPException without logging as database error** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_async_session finally block executes even on success.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test get_async_session successfully rolls back on exception.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`

## Relationships

- [lucidity npc combat](lucidity_npc_combat.md) (11 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (4 shared connections)
- [command inventory models](command_inventory_models.md) (4 shared connections)
- [command commands talk](command_commands_talk.md) (2 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 67 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*