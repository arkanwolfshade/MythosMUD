# server postgres adapter postgresconnection cursor

> 10 nodes

## Key Concepts

- **Any** (7 connections)
- **.execute()** (4 connections) — `server/postgres_adapter.py`
- **.cursor()** (3 connections) — `server/postgres_adapter.py`
- **.keys()** (3 connections) — `server/postgres_adapter.py`
- **.__getitem__()** (2 connections) — `server/postgres_adapter.py`
- **.__init__()** (2 connections) — `server/postgres_adapter.py`
- **.__iter__()** (2 connections) — `server/postgres_adapter.py`
- **Return the keys of the row dictionary. Returns: dict_keys: The keys of the row…** (1 connections) — `server/postgres_adapter.py`
- **Execute a query and return a cursor. Args: query: SQL query with PostgreSQL %s…** (1 connections) — `server/postgres_adapter.py`
- **Get a cursor from the underlying connection. This method provides direct access…** (1 connections) — `server/postgres_adapter.py`

## Relationships

- [server postgres adapter postgresrow](server_postgres_adapter_postgresrow.md) (4 shared connections)
- [server postgres adapter postgresconnection](server_postgres_adapter_postgresconnection.md) (3 shared connections)
- [server postgres adapter postgrescursor](server_postgres_adapter_postgrescursor.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*