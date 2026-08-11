# PostgreSQL Adapter Tests

> 22 nodes

## Key Concepts

- **test_postgres_adapter.py** (14 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **postgres_adapter.py** (12 connections) — `server/postgres_adapter.py`
- **TestUtilityFunctions** (11 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **PostgresConnectionPool** (10 connections) — `server/postgres_adapter.py`
- **connect_postgres()** (6 connections) — `server/postgres_adapter.py`
- **convert_sqlite_to_postgres_query()** (6 connections) — `server/postgres_adapter.py`
- **.test_connect_postgres()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_connect_postgres_with_driver_prefix()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_basic()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_no_params()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_insert_replace()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **PostgreSQL adapter for persistence layer.  Provides a PostgreSQL connection inte** (1 connections) — `server/postgres_adapter.py`
- **Thread-safe PostgreSQL connection pool.** (1 connections) — `server/postgres_adapter.py`
- **Create a PostgreSQL connection.      Args:         database_url: PostgreSQL conn** (1 connections) — `server/postgres_adapter.py`
- **Convert legacy SQLite query syntax to PostgreSQL syntax.      Note: This functio** (1 connections) — `server/postgres_adapter.py`
- **Unit tests for PostgreSQL adapter.  Tests PostgresRow, PostgresConnection, Postg** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test utility functions.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test connect_postgres().** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test connect_postgres() with driver prefix.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test convert_sqlite_to_postgres_query() basic conversion.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test convert_sqlite_to_postgres_query() with no parameters.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test convert_sqlite_to_postgres_query() with INSERT OR REPLACE.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Relationships

- [Postgres Adapter Infrastructure](Postgres_Adapter_Infrastructure.md) (10 shared connections)
- [Postgres Connection Tests](Postgres_Connection_Tests.md) (8 shared connections)
- [Postgres Adapter](Postgres_Adapter.md) (6 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 76 (87%)
- INFERRED: 11 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*