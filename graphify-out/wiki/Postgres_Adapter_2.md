# Postgres Adapter

> 5 nodes · cohesion 0.40

## Key Concepts

- **.get_connection()** (4 connections) — `server/postgres_adapter.py`
- **.get_pool()** (4 connections) — `server/postgres_adapter.py`
- **Get or create a connection pool for the given database URL.** (1 connections) — `server/postgres_adapter.py`
- **Get a connection from the pool.** (1 connections) — `server/postgres_adapter.py`
- **ThreadedConnectionPool** (1 connections) — `server/postgres_adapter.py`

## Relationships

- [[PostgreSQL Adapter Tests]] (2 shared connections)
- [[Postgres Connection Tests]] (1 shared connections)

## Source Files

- `server/postgres_adapter.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
