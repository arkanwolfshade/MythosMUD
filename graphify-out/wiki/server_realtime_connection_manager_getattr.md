# server realtime connection manager getattr

> 5 nodes

## Key Concepts

- **resolve_lazy_attr()** (4 connections) — `server/realtime/connection_manager_lazy.py`
- **__getattr__()** (2 connections) — `server/realtime/connection_manager.py`
- **connection_manager_lazy.py** (2 connections) — `server/realtime/connection_manager_lazy.py`
- **Lazy attribute resolution for connection_manager module exports. Kept separate…** (1 connections) — `server/realtime/connection_manager_lazy.py`
- **Resolve lazy API helpers (broadcast_game_event, send_*, etc.).** (1 connections) — `server/realtime/connection_manager_lazy.py`

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_lazy.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*