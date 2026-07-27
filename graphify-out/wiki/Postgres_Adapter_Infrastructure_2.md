# Postgres Adapter Infrastructure

> 6 nodes · cohesion 0.12

## Key Concepts

- **PostgresCursor** (19 connections) — `server/postgres_adapter.py`
- **.fetchall()** (2 connections) — `server/postgres_adapter.py`
- **.fetchone()** (2 connections) — `server/postgres_adapter.py`
- **.rowcount()** (2 connections) — `server/postgres_adapter.py`
- **PostgreSQL cursor wrapper for query result access.** (1 connections) — `server/postgres_adapter.py`
- **Get the number of rows affected.** (1 connections) — `server/postgres_adapter.py`

## Relationships

- [Postgres Adapter](Postgres_Adapter.md) (2 shared connections)
- [Postgres Adapter Infrastructure](Postgres_Adapter_Infrastructure.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`

## Audit Trail

- EXTRACTED: 22 (81%)
- INFERRED: 5 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*