# .get connection()

> 15 nodes

## Key Concepts

- **.get_pool()** (7 connections) — `server/postgres_adapter.py`
- **.get_connection()** (6 connections) — `server/postgres_adapter.py`
- **.test_get_connection_context_manager()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_get_pool_creates_new_pool()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_get_pool_reuses_existing_pool()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_get_pool_normalizes_url()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_get_connection_context_manager_exception()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **ThreadedConnectionPool** (1 connections)
- **Get or create a connection pool for the given database URL.** (1 connections) — `server/postgres_adapter.py`
- **Get a connection from the pool.** (1 connections) — `server/postgres_adapter.py`
- **Test get_pool() creates new pool.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test get_pool() reuses existing pool.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test get_pool() normalizes database URL.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test get_connection() context manager.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test get_connection() context manager with exception.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Relationships

- [postgres adapter](postgres_adapter.md) (7 shared connections)
- [PostgresConnection](PostgresConnection.md) (2 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 36 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*