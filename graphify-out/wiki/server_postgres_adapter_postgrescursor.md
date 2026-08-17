# server postgres adapter postgrescursor

> 22 nodes

## Key Concepts

- **PostgresCursor** (16 connections) — `server/postgres_adapter.py`
- **TestPostgresCursor** (11 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.rowcount()** (4 connections) — `server/postgres_adapter.py`
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
- **Get the number of rows affected.** (1 connections) — `server/postgres_adapter.py`
- **Test PostgresCursor class.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor initialization.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchone() with row.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchone() with None.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchall() with rows.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.fetchall() with empty result.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresCursor.rowcount().** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Relationships

- [server postgres adapter](server_postgres_adapter.md) (3 shared connections)
- [server postgres adapter postgresrow](server_postgres_adapter_postgresrow.md) (3 shared connections)
- [server postgres adapter postgresconnection cursor](server_postgres_adapter_postgresconnection_cursor.md) (1 shared connections)
- [server postgres adapter postgresconnection](server_postgres_adapter_postgresconnection.md) (1 shared connections)
- [server tests unit infrastructure test](server_tests_unit_infrastructure_test.md) (1 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (1 shared connections)
- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 33 (87%)
- INFERRED: 5 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*