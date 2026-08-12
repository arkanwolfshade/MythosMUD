# Postgres Adapter Infrastructure

> 25 nodes

## Key Concepts

- **PostgresRow** (26 connections) — `server/postgres_adapter.py`
- **TestPostgresRow** (15 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_contains()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_getitem_int_key()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_getitem_int_key_out_of_range()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_getitem_string_key()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_initialization()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_iter()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_keys()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_len()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_repr()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.__contains__()** (1 connections) — `server/postgres_adapter.py`
- **.__len__()** (1 connections) — `server/postgres_adapter.py`
- **.__repr__()** (1 connections) — `server/postgres_adapter.py`
- **Row-like object for PostgreSQL query results.** (1 connections) — `server/postgres_adapter.py`
- **Test PostgresRow class.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow initialization.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__getitem__ with string key.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__getitem__ with integer index.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__getitem__ with out-of-range integer index.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__iter__.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.keys().** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__contains__.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__len__.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__repr__.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Relationships

- [PostgresCursor](PostgresCursor.md) (4 shared connections)
- [test_postgres_adapter.py](test_postgres_adapter.py.md) (4 shared connections)
- [Any](Any.md) (4 shared connections)
- [PostgresConnection](PostgresConnection.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [TestUtilityFunctions](TestUtilityFunctions.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 73 (89%)
- INFERRED: 9 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*