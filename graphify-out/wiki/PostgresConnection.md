# PostgresConnection

> 34 nodes

## Key Concepts

- **PostgresConnection** (28 connections) — `server/postgres_adapter.py`
- **TestPostgresConnection** (18 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.__exit__()** (5 connections) — `server/postgres_adapter.py`
- **.close()** (3 connections) — `server/postgres_adapter.py`
- **.commit()** (3 connections) — `server/postgres_adapter.py`
- **.rollback()** (3 connections) — `server/postgres_adapter.py`
- **.test_postgres_connection_close()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_commit()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_context_manager_exception()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_context_manager_success()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_cursor()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_cursor_with_factory()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_execute()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_execute_no_params()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_initialization()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_rollback()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.__init__()** (2 connections) — `server/postgres_adapter.py`
- **.__enter__()** (1 connections) — `server/postgres_adapter.py`
- **connection** (1 connections)
- **Commit the current transaction.** (1 connections) — `server/postgres_adapter.py`
- **Rollback the current transaction.** (1 connections) — `server/postgres_adapter.py`
- **Close the connection.** (1 connections) — `server/postgres_adapter.py`
- **PostgreSQL connection wrapper for persistence layer operations.** (1 connections) — `server/postgres_adapter.py`
- **Test PostgresConnection initialization.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresConnection.execute().** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- *... and 9 more nodes in this community*

## Relationships

- [PostgresRow](PostgresRow.md) (5 shared connections)
- [test_postgres_adapter.py](test_postgres_adapter.py.md) (4 shared connections)
- [TestPostgresConnectionPool](TestPostgresConnectionPool.md) (3 shared connections)
- [PostgresCursor](PostgresCursor.md) (2 shared connections)
- [fixture](fixture.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 55 (87%)
- INFERRED: 8 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*