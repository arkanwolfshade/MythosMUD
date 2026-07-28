# Postgres Adapter Infrastructure

> 22 nodes · cohesion 0.12

## Key Concepts

- **PostgresCursor** (21 connections) — `server/postgres_adapter.py`
- **TestPostgresCursor** (13 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.rowcount()** (4 connections) — `server/postgres_adapter.py`
- **.test_postgres_cursor_fetchall_with_rows()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_fetchone_with_row()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_fetchall_empty()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_fetchone_none()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_initialization()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_rowcount()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.fetchall()** (2 connections) — `server/postgres_adapter.py`
- **.fetchone()** (2 connections) — `server/postgres_adapter.py`
- **.mock_cursor()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **PostgreSQL cursor wrapper for query result access.** (1 connections) — `server/postgres_adapter.py`
- **Get the number of rows affected.** (1 connections) — `server/postgres_adapter.py`
- **Test PostgresCursor class.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Create a mock psycopg2 cursor.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor initialization.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchone() with row.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchone() with None.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchall() with rows.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchall() with empty result.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.rowcount().** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Relationships

- [Postgres Adapter Infrastructure](Postgres_Adapter_Infrastructure.md) (6 shared connections)
- [Postgres Adapter](Postgres_Adapter.md) (4 shared connections)
- [Postgres Connection Tests](Postgres_Connection_Tests.md) (4 shared connections)
- [PostgreSQL Adapter Tests](PostgreSQL_Adapter_Tests.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Room Exploration API](Room_Exploration_API.md) (1 shared connections)
- [Services Lucidity Repository](Services_Lucidity_Repository.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 59 (80%)
- INFERRED: 15 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*