# GameClientV2.tsx

> 8 nodes

## Key Concepts

- **AuthRateLimitMiddleware** (5 connections) — `server/middleware/auth_rate_limit.py`
- **.__call__()** (5 connections) — `server/middleware/auth_rate_limit.py`
- **.__init__()** (2 connections) — `server/middleware/auth_rate_limit.py`
- **ASGIApp** (1 connections)
- **Receive** (1 connections)
- **Scope** (1 connections)
- **Send** (1 connections)
- **Pure ASGI middleware; HTTP POST login/register only.** (1 connections) — `server/middleware/auth_rate_limit.py`

## Relationships

- [Execution Steps](Execution_Steps.md) (2 shared connections)
- [useRespawnHandlers.ts](useRespawnHandlers.ts.md) (1 shared connections)

## Source Files

- `server/middleware/auth_rate_limit.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*