# Postgres Adapter

> 9 nodes · cohesion 0.10

## Key Concepts

- **PostgresConnectionPool** (10 connections) — `server/postgres_adapter.py`
- **is_postgres_url()** (5 connections) — `server/postgres_adapter.py`
- **.get_connection()** (4 connections) — `server/postgres_adapter.py`
- **.get_pool()** (4 connections) — `server/postgres_adapter.py`
- **Thread-safe PostgreSQL connection pool.** (1 connections) — `server/postgres_adapter.py`
- **Get or create a connection pool for the given database URL.** (1 connections) — `server/postgres_adapter.py`
- **Get a connection from the pool.** (1 connections) — `server/postgres_adapter.py`
- **Check if the database URL is PostgreSQL.** (1 connections) — `server/postgres_adapter.py`
- **ThreadedConnectionPool** (1 connections) — `server/postgres_adapter.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Postgres Connection Tests](Postgres_Connection_Tests.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`

## Audit Trail

- EXTRACTED: 23 (82%)
- INFERRED: 5 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*