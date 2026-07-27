# Postgres Adapter Infrastructure

> 5 nodes · cohesion 0.11

## Key Concepts

- **PostgresRow** (26 connections) — `server/postgres_adapter.py`
- **.__contains__()** (1 connections) — `server/postgres_adapter.py`
- **.__len__()** (1 connections) — `server/postgres_adapter.py`
- **.__repr__()** (1 connections) — `server/postgres_adapter.py`
- **Row-like object for PostgreSQL query results.** (1 connections) — `server/postgres_adapter.py`

## Relationships

- [Postgres Adapter](Postgres_Adapter.md) (4 shared connections)
- [Postgres Adapter Infrastructure](Postgres_Adapter_Infrastructure.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`

## Audit Trail

- EXTRACTED: 25 (83%)
- INFERRED: 5 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*