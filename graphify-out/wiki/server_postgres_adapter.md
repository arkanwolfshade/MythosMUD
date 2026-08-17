# server postgres adapter

> 28 nodes

## Key Concepts

- **test_postgres_adapter.py** (15 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **postgres_adapter.py** (12 connections) — `server/postgres_adapter.py`
- **TestPostgresConnectionPool** (11 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **TestUtilityFunctions** (8 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **PostgresConnectionPool** (6 connections) — `server/postgres_adapter.py`
- **connect_postgres()** (6 connections) — `server/postgres_adapter.py`
- **convert_sqlite_to_postgres_query()** (6 connections) — `server/postgres_adapter.py`
- **is_postgres_url()** (5 connections) — `server/postgres_adapter.py`
- **.test_connect_postgres()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_connect_postgres_with_driver_prefix()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_is_postgres_url_false()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_is_postgres_url_true()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_basic()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_insert_replace()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_no_params()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test is_postgres_url() with PostgreSQL URL.** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **PostgreSQL adapter for persistence layer. Provides a PostgreSQL connection…** (1 connections) — `server/postgres_adapter.py`
- **Thread-safe PostgreSQL connection pool.** (1 connections) — `server/postgres_adapter.py`
- **Check if the database URL is PostgreSQL.** (1 connections) — `server/postgres_adapter.py`
- **Create a PostgreSQL connection. Args: database_url: PostgreSQL connection URL…** (1 connections) — `server/postgres_adapter.py`
- **Convert legacy SQLite query syntax to PostgreSQL syntax. Note: This function is…** (1 connections) — `server/postgres_adapter.py`
- **Unit tests for PostgreSQL adapter. Tests PostgresRow, PostgresConnection,…** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test utility functions.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test connect_postgres().** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test connect_postgres() with driver prefix.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- *... and 3 more nodes in this community*

## Relationships

- [server postgres adapter postgresconnectionpool get](server_postgres_adapter_postgresconnectionpool_get.md) (9 shared connections)
- [server postgres adapter postgresconnection](server_postgres_adapter_postgresconnection.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server postgres adapter postgrescursor](server_postgres_adapter_postgrescursor.md) (3 shared connections)
- [server postgres adapter postgresrow](server_postgres_adapter_postgresrow.md) (3 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 63 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*