# Server Infrastructure (10)

> 28 nodes

## Key Concepts

- **test_postgres_adapter.py** (14 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **TestPostgresConnectionPool** (13 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **postgres_adapter.py** (12 connections) — `server/postgres_adapter.py`
- **TestUtilityFunctions** (11 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **PostgresConnectionPool** (10 connections) — `server/postgres_adapter.py`
- **connect_postgres()** (6 connections) — `server/postgres_adapter.py`
- **convert_sqlite_to_postgres_query()** (6 connections) — `server/postgres_adapter.py`
- **is_postgres_url()** (5 connections) — `server/postgres_adapter.py`
- **.test_connect_postgres()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_connect_postgres_with_driver_prefix()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_is_postgres_url_true()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_is_postgres_url_false()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_basic()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_no_params()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_convert_sqlite_to_postgres_query_insert_replace()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test is_postgres_url() with PostgreSQL URL.** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **PostgreSQL adapter for persistence layer.  Provides a PostgreSQL connection inte** (1 connections) — `server/postgres_adapter.py`
- **Thread-safe PostgreSQL connection pool.** (1 connections) — `server/postgres_adapter.py`
- **Check if the database URL is PostgreSQL.** (1 connections) — `server/postgres_adapter.py`
- **Create a PostgreSQL connection.      Args:         database_url: PostgreSQL conn** (1 connections) — `server/postgres_adapter.py`
- **Convert legacy SQLite query syntax to PostgreSQL syntax.      Note: This functio** (1 connections) — `server/postgres_adapter.py`
- **Unit tests for PostgreSQL adapter.  Tests PostgresRow, PostgresConnection, Postg** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test utility functions.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test connect_postgres().** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test connect_postgres() with driver prefix.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- *... and 3 more nodes in this community*

## Relationships

- [Server Infrastructure (9)](Server_Infrastructure_%289%29.md) (10 shared connections)
- [Server Infrastructure (17)](Server_Infrastructure_%2817%29.md) (7 shared connections)
- [Server Infrastructure (14)](Server_Infrastructure_%2814%29.md) (6 shared connections)
- [Server Infrastructure (11)](Server_Infrastructure_%2811%29.md) (6 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Npc (6)](Server_Npc_%286%29.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 99 (87%)
- INFERRED: 15 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*