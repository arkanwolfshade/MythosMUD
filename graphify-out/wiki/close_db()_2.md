# close db()

> 69 nodes

## Key Concepts

- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **get_async_session()** (13 connections) — `server/database_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **get_session_maker()** (9 connections) — `server/database_helpers.py`
- **close_db()** (9 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **get_database_url()** (6 connections) — `server/database_helpers.py`
- **test_get_engine_raises_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker_raises_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **AsyncSession** (4 connections)
- **test_reset_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_engine()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url_returns_none()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_engine_initialization_failure()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **reset_db()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_success()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_http_exception_propagates()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_on_error()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_failure()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_init_db_success()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_init_db_raises_on_error()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_success()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_raises_runtime_error_on_failure()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- *... and 44 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (16 shared connections)
- [main()](main%28%29.md) (14 shared connections)
- [.reset instance()](reset_instance%28%29.md) (6 shared connections)
- [.get instance()](get_instance%28%29.md) (5 shared connections)
- [ensure database directory()](ensure_database_directory%28%29.md) (3 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 228 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*