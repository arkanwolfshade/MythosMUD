# server postgres adapter postgresrow

> 24 nodes

## Key Concepts

- **PostgresRow** (23 connections) — `server/postgres_adapter.py`
- **TestPostgresRow** (12 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_contains()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_getitem_int_key()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_getitem_int_key_out_of_range()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_getitem_string_key()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_initialization()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_iter()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_keys()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_len()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_repr()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__getitem__ with integer index.** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.__contains__()** (1 connections) — `server/postgres_adapter.py`
- **.__len__()** (1 connections) — `server/postgres_adapter.py`
- **.__repr__()** (1 connections) — `server/postgres_adapter.py`
- **Row-like object for PostgreSQL query results.** (1 connections) — `server/postgres_adapter.py`
- **Test PostgresRow class.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow initialization.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__getitem__ with string key.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__iter__.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.keys().** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__contains__.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__len__.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__repr__.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Relationships

- [server postgres adapter postgresconnection cursor](server_postgres_adapter_postgresconnection_cursor.md) (4 shared connections)
- [server postgres adapter postgrescursor](server_postgres_adapter_postgrescursor.md) (3 shared connections)
- [server postgres adapter connect postgres](server_postgres_adapter_connect_postgres.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 41 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*