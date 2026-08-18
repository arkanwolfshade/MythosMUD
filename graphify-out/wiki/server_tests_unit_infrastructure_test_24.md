# server tests unit infrastructure test

> 6 nodes

## Key Concepts

- **.mock_connection()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.mock_cursor()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **.mock_cursor()** (3 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **fixture** (3 connections)
- **Create a mock psycopg2 cursor.** (2 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`
- **Create a mock psycopg2 connection.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Relationships

- [server postgres adapter postgresconnection](server_postgres_adapter_postgresconnection.md) (2 shared connections)
- [server postgres adapter postgrescursor](server_postgres_adapter_postgrescursor.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_postgres_adapter.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*