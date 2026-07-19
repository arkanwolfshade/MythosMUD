# Postgres Adapter Infrastructure

> 25 nodes · cohesion 0.12

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
- **Test PostgresRow.__getitem__ with integer index.** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__iter__.** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.fetchall()** (2 connections) — `server/postgres_adapter.py`
- **.fetchone()** (2 connections) — `server/postgres_adapter.py`
- **Test PostgresRow class.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow initialization.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__getitem__ with string key.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__contains__.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__len__.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test PostgresRow.__repr__.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.__contains__()** (1 connections) — `server/postgres_adapter.py`
- **.__len__()** (1 connections) — `server/postgres_adapter.py`
- **.__repr__()** (1 connections) — `server/postgres_adapter.py`
- **Row-like object for PostgreSQL query results.** (1 connections) — `server/postgres_adapter.py`

## Relationships

- [[PostgreSQL Adapter Tests]] (6 shared connections)
- [[Postgres Adapter Infrastructure]] (4 shared connections)
- [[Postgres Adapter]] (4 shared connections)
- [[Postgres Connection Tests]] (2 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 77 (90%)
- INFERRED: 9 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
