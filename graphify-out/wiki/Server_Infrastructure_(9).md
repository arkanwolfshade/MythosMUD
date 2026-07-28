# Server Infrastructure (9)

> 31 nodes

## Key Concepts

- **PostgresConnection** (31 connections) — `server/postgres_adapter.py`
- **TestPostgresConnection** (18 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresConnection class.** (6 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.__exit__()** (5 connections) — `server/postgres_adapter.py`
- **.test_postgres_connection_execute()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_execute_no_params()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.commit()** (3 connections) — `server/postgres_adapter.py`
- **.rollback()** (3 connections) — `server/postgres_adapter.py`
- **.close()** (3 connections) — `server/postgres_adapter.py`
- **.test_postgres_connection_initialization()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_cursor()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_cursor_with_factory()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_commit()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_rollback()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_close()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_context_manager_success()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_connection_context_manager_exception()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.__init__()** (2 connections) — `server/postgres_adapter.py`
- **.mock_connection()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresConnection as context manager (success).** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **connection** (1 connections)
- **.__enter__()** (1 connections) — `server/postgres_adapter.py`
- **PostgreSQL connection wrapper for persistence layer operations.** (1 connections) — `server/postgres_adapter.py`
- **Commit the current transaction.** (1 connections) — `server/postgres_adapter.py`
- **Rollback the current transaction.** (1 connections) — `server/postgres_adapter.py`
- *... and 6 more nodes in this community*

## Relationships

- [Server Infrastructure (10)](Server_Infrastructure_%2810%29.md) (10 shared connections)
- [Server Infrastructure (14)](Server_Infrastructure_%2814%29.md) (5 shared connections)
- [Server (13)](Server_%2813%29.md) (3 shared connections)
- [Server Infrastructure (17)](Server_Infrastructure_%2817%29.md) (2 shared connections)
- [Server Infrastructure (11)](Server_Infrastructure_%2811%29.md) (2 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 102 (86%)
- INFERRED: 16 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*