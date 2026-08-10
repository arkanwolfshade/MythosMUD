# Graceful Degradation Plan

> 5 nodes

## Key Concepts

- **.__call__()** (5 connections) — `server/middleware/security_headers.py`
- **Scope** (1 connections)
- **Receive** (1 connections)
- **Send** (1 connections)
- **ASGI application interface.          Args:             scope: ASGI connection sc** (1 connections) — `server/middleware/security_headers.py`

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)

## Source Files

- `server/middleware/security_headers.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*