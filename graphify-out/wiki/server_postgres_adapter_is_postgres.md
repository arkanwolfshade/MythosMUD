# server postgres adapter is postgres

> 5 nodes

## Key Concepts

- **is_postgres_url()** (5 connections) — `server/postgres_adapter.py`
- **.test_is_postgres_url_false()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.test_is_postgres_url_true()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Test is_postgres_url() with PostgreSQL URL.** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Check if the database URL is PostgreSQL.** (1 connections) — `server/postgres_adapter.py`

## Relationships

- [server postgres adapter postgresconnectionpool](server_postgres_adapter_postgresconnectionpool.md) (2 shared connections)
- [server postgres adapter connect postgres](server_postgres_adapter_connect_postgres.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/postgres_adapter.py`
- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*