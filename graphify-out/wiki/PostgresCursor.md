# PostgresCursor

> 20 nodes

## Key Concepts

- **PostgresCursor** (19 connections) — `server/postgres_adapter.py`
- **TestPostgresCursor** (13 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_fetchall_empty()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_fetchall_with_rows()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_fetchone_none()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_fetchone_with_row()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_initialization()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_cursor_rowcount()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.fetchall()** (2 connections) — `server/postgres_adapter.py`
- **.fetchone()** (2 connections) — `server/postgres_adapter.py`
- **.__init__()** (2 connections) — `server/postgres_adapter.py`
- **cursor** (1 connections)
- **PostgreSQL cursor wrapper for query result access.** (1 connections) — `server/postgres_adapter.py`
- **Test PostgresCursor class.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor initialization.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchone() with row.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchone() with None.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchall() with rows.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchall() with empty result.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.rowcount().** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Relationships

- [PostgresRow](PostgresRow.md) (5 shared connections)
- [test_postgres_adapter.py](test_postgres_adapter.py.md) (3 shared connections)
- [PostgresConnection](PostgresConnection.md) (2 shared connections)
- [TestPostgresConnectionPool](TestPostgresConnectionPool.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [LucidityRepository](LucidityRepository.md) (1 shared connections)
- [fixture](fixture.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 32 (80%)
- INFERRED: 8 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*