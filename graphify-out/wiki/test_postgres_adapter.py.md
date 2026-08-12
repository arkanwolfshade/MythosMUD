# test_postgres_adapter.py

> 18 nodes

## Key Concepts

- **test_postgres_adapter.py** (14 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **TestUtilityFunctions** (11 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
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

- [TestPostgresConnectionPool](TestPostgresConnectionPool.md) (6 shared connections)
- [PostgresConnection](PostgresConnection.md) (4 shared connections)
- [PostgresCursor](PostgresCursor.md) (3 shared connections)
- [PostgresRow](PostgresRow.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 59 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*