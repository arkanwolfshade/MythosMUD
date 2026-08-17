# test_auth

> 6 nodes

## Key Concepts

- **test_auth()** (4 connections) — `server/main.py`
- **read_root()** (3 connections) — `server/main.py`
- **get** (2 connections)
- **Any** (1 connections)
- **Root endpoint providing basic server information.** (1 connections) — `server/main.py`
- **Test endpoint to verify JWT authentication is working.** (1 connections) — `server/main.py`

## Relationships

- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/main.py`

## Audit Trail

- EXTRACTED: 7 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*