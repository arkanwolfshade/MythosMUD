# server postgres adapter connect postgres

> 18 nodes

## Key Concepts

- **test_postgres_adapter.py** (15 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **TestUtilityFunctions** (8 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **connect_postgres()** (6 connections) — `server/postgres_adapter.py`
- **convert_sqlite_to_postgres_query()** (6 connections) — `server/postgres_adapter.py`
- **.test_connect_postgres()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_connect_postgres_with_driver_prefix()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_basic()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_insert_replace()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_no_params()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Create a PostgreSQL connection. Args: database_url: PostgreSQL connection URL…** (1 connections) — `server/postgres_adapter.py`
- **Convert legacy SQLite query syntax to PostgreSQL syntax. Note: This function is…** (1 connections) — `server/postgres_adapter.py`
- **Unit tests for PostgreSQL adapter. Tests PostgresRow, PostgresConnection,…** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test utility functions.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test connect_postgres().** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test connect_postgres() with driver prefix.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test convert_sqlite_to_postgres_query() basic conversion.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test convert_sqlite_to_postgres_query() with no parameters.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test convert_sqlite_to_postgres_query() with INSERT OR REPLACE.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Relationships

- [server postgres adapter postgresconnection](server_postgres_adapter_postgresconnection.md) (4 shared connections)
- [server postgres adapter postgresconnectionpool](server_postgres_adapter_postgresconnectionpool.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server postgres adapter postgrescursor](server_postgres_adapter_postgrescursor.md) (2 shared connections)
- [server postgres adapter postgresrow](server_postgres_adapter_postgresrow.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)
- [server postgres adapter is postgres](server_postgres_adapter_is_postgres.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 38 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*