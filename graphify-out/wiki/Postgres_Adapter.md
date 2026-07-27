# Postgres Adapter

> 12 nodes · cohesion 0.20

## Key Concepts

- **Any** (7 connections) — `server/postgres_adapter.py`
- **.execute()** (5 connections) — `server/postgres_adapter.py`
- **.cursor()** (4 connections) — `server/postgres_adapter.py`
- **.keys()** (4 connections) — `server/postgres_adapter.py`
- **.__getitem__()** (3 connections) — `server/postgres_adapter.py`
- **cursor** (3 connections) — `server/postgres_adapter.py`
- **.__init__()** (2 connections) — `server/postgres_adapter.py`
- **.__init__()** (2 connections) — `server/postgres_adapter.py`
- **.__iter__()** (2 connections) — `server/postgres_adapter.py`
- **Return the keys of the row dictionary.          Returns:             dict_keys:** (1 connections) — `server/postgres_adapter.py`
- **Execute a query and return a cursor.          Args:             query: SQL query** (1 connections) — `server/postgres_adapter.py`
- **Get a cursor from the underlying connection.          This method provides direc** (1 connections) — `server/postgres_adapter.py`

## Relationships

- [[Postgres Adapter Infrastructure]] (6 shared connections)
- [[Postgres Connection Tests]] (3 shared connections)

## Source Files

- `server/postgres_adapter.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
