# PostgreSQL Adapter Tests

> 38 nodes · cohesion 0.07

## Key Concepts

- **test_postgres_adapter.py** (14 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **TestPostgresConnectionPool** (13 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **TestUtilityFunctions** (11 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **postgres_adapter.py** (11 connections) — `server/postgres_adapter.py`
- **PostgresConnectionPool** (10 connections) — `server/postgres_adapter.py`
- **connect_postgres()** (6 connections) — `server/postgres_adapter.py`
- **convert_sqlite_to_postgres_query()** (6 connections) — `server/postgres_adapter.py`
- **is_postgres_url()** (5 connections) — `server/postgres_adapter.py`
- **.test_is_postgres_url_false()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_is_postgres_url_true()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_connect_postgres()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_connect_postgres_with_driver_prefix()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_basic()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_insert_replace()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_no_params()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test is_postgres_url() with PostgreSQL URL.** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_get_connection_context_manager()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_get_connection_context_manager_exception()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_get_pool_creates_new_pool()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_get_pool_normalizes_url()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_get_pool_reuses_existing_pool()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Unit tests for PostgreSQL adapter.  Tests PostgresRow, PostgresConnection, Postg** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test get_pool() creates new pool.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test get_pool() reuses existing pool.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test get_pool() normalizes database URL.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- *... and 13 more nodes in this community*

## Relationships

- [[Postgres Adapter Infrastructure]] (12 shared connections)
- [[Postgres Connection Tests]] (8 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Postgres Adapter]] (2 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 113 (90%)
- INFERRED: 13 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
