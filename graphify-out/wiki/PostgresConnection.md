# PostgresConnection

> 78 nodes

## Key Concepts

- **PostgresConnection** (26 connections) — `server/postgres_adapter.py`
- **TestPostgresConnection** (16 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **test_postgres_adapter.py** (15 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **TestPostgresConnectionPool** (11 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **TestUtilityFunctions** (8 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.get_pool()** (7 connections) — `server/postgres_adapter.py`
- **patch** (7 connections)
- **PostgresConnectionPool** (6 connections) — `server/postgres_adapter.py`
- **connect_postgres()** (6 connections) — `server/postgres_adapter.py`
- **convert_sqlite_to_postgres_query()** (6 connections) — `server/postgres_adapter.py`
- **.get_connection()** (6 connections) — `server/postgres_adapter.py`
- **is_postgres_url()** (5 connections) — `server/postgres_adapter.py`
- **.__exit__()** (5 connections) — `server/postgres_adapter.py`
- **.test_get_connection_context_manager()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_get_connection_context_manager_exception()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_get_pool_creates_new_pool()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_get_pool_normalizes_url()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_get_pool_reuses_existing_pool()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_connect_postgres()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_connect_postgres_with_driver_prefix()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.close()** (3 connections) — `server/postgres_adapter.py`
- **.commit()** (3 connections) — `server/postgres_adapter.py`
- **.rollback()** (3 connections) — `server/postgres_adapter.py`
- **.test_postgres_connection_close()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_commit()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- *... and 53 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [Any](Any.md) (3 shared connections)
- [PostgresCursor](PostgresCursor.md) (3 shared connections)
- [fixture](fixture.md) (2 shared connections)
- [PostgresRow](PostgresRow.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 127 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*