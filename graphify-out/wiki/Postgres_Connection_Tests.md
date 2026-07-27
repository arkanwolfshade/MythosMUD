# Postgres Connection Tests

> 12 nodes · cohesion 0.07

## Key Concepts

- **PostgresConnection** (28 connections) — `server/postgres_adapter.py`
- **.__exit__()** (5 connections) — `server/postgres_adapter.py`
- **.close()** (3 connections) — `server/postgres_adapter.py`
- **.commit()** (3 connections) — `server/postgres_adapter.py`
- **.rollback()** (3 connections) — `server/postgres_adapter.py`
- **.__init__()** (2 connections) — `server/postgres_adapter.py`
- **.__enter__()** (1 connections) — `server/postgres_adapter.py`
- **connection** (1 connections) — `server/postgres_adapter.py`
- **Commit the current transaction.** (1 connections) — `server/postgres_adapter.py`
- **Rollback the current transaction.** (1 connections) — `server/postgres_adapter.py`
- **Close the connection.** (1 connections) — `server/postgres_adapter.py`
- **PostgreSQL connection wrapper for persistence layer operations.** (1 connections) — `server/postgres_adapter.py`

## Relationships

- [Postgres Adapter](Postgres_Adapter.md) (4 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [PostgreSQL Adapter Tests](PostgreSQL_Adapter_Tests.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`

## Audit Trail

- EXTRACTED: 45 (90%)
- INFERRED: 5 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*