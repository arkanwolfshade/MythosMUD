# postgres adapter infrastructure

> 38 nodes

## Key Concepts

- **PostgresConnection** (31 connections) — `server/postgres_adapter.py`
- **TestPostgresConnection** (18 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
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
- **.mock_cursor()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **connection** (1 connections)
- **.__enter__()** (1 connections) — `server/postgres_adapter.py`
- **PostgreSQL connection wrapper for persistence layer operations.** (1 connections) — `server/postgres_adapter.py`
- **Commit the current transaction.** (1 connections) — `server/postgres_adapter.py`
- **Rollback the current transaction.** (1 connections) — `server/postgres_adapter.py`
- **Close the connection.** (1 connections) — `server/postgres_adapter.py`
- *... and 13 more nodes in this community*

## Relationships

- [postgres adapter infrastructure](postgres_adapter_infrastructure.md) (16 shared connections)
- [postgres adapter rationale](postgres_adapter_rationale.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 104 (87%)
- INFERRED: 16 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*