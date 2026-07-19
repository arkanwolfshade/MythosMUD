# Postgres Connection Tests

> 31 nodes · cohesion 0.10

## Key Concepts

- **PostgresConnection** (28 connections) — `server/postgres_adapter.py`
- **TestPostgresConnection** (18 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresConnection class.** (6 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.__exit__()** (5 connections) — `server/postgres_adapter.py`
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
- **.close()** (3 connections) — `server/postgres_adapter.py`
- **.commit()** (3 connections) — `server/postgres_adapter.py`
- **.rollback()** (3 connections) — `server/postgres_adapter.py`
- **Test PostgresConnection as context manager (success).** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.mock_connection()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.__init__()** (2 connections) — `server/postgres_adapter.py`
- **Create a mock psycopg2 connection.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresConnection initialization.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresConnection.execute() without parameters.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresConnection.cursor() with custom factory.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresConnection.rollback().** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- *... and 6 more nodes in this community*

## Relationships

- [[PostgreSQL Adapter Tests]] (8 shared connections)
- [[Postgres Adapter Infrastructure]] (5 shared connections)
- [[Postgres Adapter]] (4 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 104 (92%)
- INFERRED: 9 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
