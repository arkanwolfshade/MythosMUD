# PostgresRow

> 35 nodes

## Key Concepts

- **PostgresRow** (26 connections) — `server/postgres_adapter.py`
- **TestPostgresRow** (15 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Any** (7 connections)
- **.execute()** (4 connections) — `server/postgres_adapter.py`
- **.cursor()** (3 connections) — `server/postgres_adapter.py`
- **.keys()** (3 connections) — `server/postgres_adapter.py`
- **.test_postgres_row_contains()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_getitem_int_key()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_getitem_int_key_out_of_range()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_getitem_string_key()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_initialization()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_iter()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_keys()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_len()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_postgres_row_repr()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.__getitem__()** (2 connections) — `server/postgres_adapter.py`
- **.__init__()** (2 connections) — `server/postgres_adapter.py`
- **.__iter__()** (2 connections) — `server/postgres_adapter.py`
- **.__contains__()** (1 connections) — `server/postgres_adapter.py`
- **.__len__()** (1 connections) — `server/postgres_adapter.py`
- **.__repr__()** (1 connections) — `server/postgres_adapter.py`
- **Row-like object for PostgreSQL query results.** (1 connections) — `server/postgres_adapter.py`
- **Return the keys of the row dictionary. Returns: dict_keys: The keys of the row…** (1 connections) — `server/postgres_adapter.py`
- **Execute a query and return a cursor. Args: query: SQL query with PostgreSQL %s…** (1 connections) — `server/postgres_adapter.py`
- **Get a cursor from the underlying connection. This method provides direct access…** (1 connections) — `server/postgres_adapter.py`
- *... and 10 more nodes in this community*

## Relationships

- [PostgresCursor](PostgresCursor.md) (5 shared connections)
- [PostgresConnection](PostgresConnection.md) (5 shared connections)
- [test_postgres_adapter.py](test_postgres_adapter.py.md) (3 shared connections)
- [TestPostgresConnectionPool](TestPostgresConnectionPool.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 99 (92%)
- INFERRED: 9 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*