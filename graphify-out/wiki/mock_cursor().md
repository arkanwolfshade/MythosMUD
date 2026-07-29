# .mock cursor()

> 21 nodes

## Key Concepts

- **PostgresCursor** (21 connections) — `server/postgres_adapter.py`
- **TestPostgresCursor** (13 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.rowcount()** (4 connections) — `server/postgres_adapter.py`
- **.test_postgres_cursor_fetchone_with_row()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_fetchall_with_rows()** (4 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_initialization()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_fetchone_none()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_fetchall_empty()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_rowcount()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchone() with row.** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.fetchone()** (2 connections) — `server/postgres_adapter.py`
- **.fetchall()** (2 connections) — `server/postgres_adapter.py`
- **.mock_cursor()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.mock_cursor()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Create a mock psycopg2 cursor.** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **PostgreSQL cursor wrapper for query result access.** (1 connections) — `server/postgres_adapter.py`
- **Get the number of rows affected.** (1 connections) — `server/postgres_adapter.py`
- **Test PostgresCursor class.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor initialization.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchall() with empty result.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.rowcount().** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Relationships

- [postgres adapter](postgres_adapter.md) (6 shared connections)
- [PostgresRow](PostgresRow.md) (6 shared connections)
- [PostgresConnection](PostgresConnection.md) (5 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [player respawn](player_respawn.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 62 (81%)
- INFERRED: 15 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*