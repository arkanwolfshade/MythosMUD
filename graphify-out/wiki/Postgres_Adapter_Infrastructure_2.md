# Postgres Adapter Infrastructure

> 19 nodes · cohesion 0.15

## Key Concepts

- **PostgresCursor** (19 connections) — `server/postgres_adapter.py`
- **TestPostgresCursor** (13 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchone() with row.** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_fetchall_empty()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_fetchall_with_rows()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_fetchone_none()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_fetchone_with_row()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_initialization()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_rowcount()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Create a mock psycopg2 cursor.** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.mock_cursor()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.mock_cursor()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.rowcount()** (2 connections) — `server/postgres_adapter.py`
- **Test PostgresCursor class.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor initialization.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchall() with empty result.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.rowcount().** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **PostgreSQL cursor wrapper for query result access.** (1 connections) — `server/postgres_adapter.py`
- **Get the number of rows affected.** (1 connections) — `server/postgres_adapter.py`

## Relationships

- [[PostgreSQL Adapter Tests]] (6 shared connections)
- [[Postgres Adapter Infrastructure]] (4 shared connections)
- [[Postgres Connection Tests]] (3 shared connections)
- [[Postgres Adapter]] (2 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 58 (87%)
- INFERRED: 9 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
