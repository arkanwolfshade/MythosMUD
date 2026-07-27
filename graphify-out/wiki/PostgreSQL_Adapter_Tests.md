# PostgreSQL Adapter Tests

> 4 nodes · cohesion 0.14

## Key Concepts

- **connect_postgres()** (6 connections) — `server/postgres_adapter.py`
- **convert_sqlite_to_postgres_query()** (6 connections) — `server/postgres_adapter.py`
- **Create a PostgreSQL connection.      Args:         database_url: PostgreSQL conn** (1 connections) — `server/postgres_adapter.py`
- **Convert legacy SQLite query syntax to PostgreSQL syntax.      Note: This functio** (1 connections) — `server/postgres_adapter.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Postgres Connection Tests](Postgres_Connection_Tests.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*