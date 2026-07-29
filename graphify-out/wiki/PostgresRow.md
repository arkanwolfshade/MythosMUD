# PostgresRow

> 23 nodes

## Key Concepts

- **PostgresRow** (28 connections) — `server/postgres_adapter.py`
- **TestPostgresRow** (15 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_initialization()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_getitem_string_key()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_getitem_int_key()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_getitem_int_key_out_of_range()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_iter()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_keys()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_contains()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_len()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_repr()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__getitem__ with integer index.** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__iter__.** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.__contains__()** (1 connections) — `server/postgres_adapter.py`
- **.__len__()** (1 connections) — `server/postgres_adapter.py`
- **.__repr__()** (1 connections) — `server/postgres_adapter.py`
- **Row-like object for PostgreSQL query results.** (1 connections) — `server/postgres_adapter.py`
- **Test PostgresRow class.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow initialization.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__getitem__ with string key.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__contains__.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__len__.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__repr__.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Relationships

- [postgres adapter](postgres_adapter.md) (6 shared connections)
- [.mock cursor()](mock_cursor%28%29.md) (6 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [PostgresConnection](PostgresConnection.md) (2 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 73 (87%)
- INFERRED: 11 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*