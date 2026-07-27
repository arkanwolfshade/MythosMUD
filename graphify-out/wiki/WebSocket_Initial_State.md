# WebSocket Initial State

> 6 nodes · cohesion 0.02

## Key Concepts

- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **UUID** (8 connections) — `server/realtime/event_handler.py`
- **UUID** (8 connections) — `server/realtime/websocket_initial_state.py`
- **WebSocket** (7 connections) — `server/realtime/websocket_initial_state.py`
- **Room** (3 connections) — `server/realtime/websocket_initial_state.py`
- **Get the global async persistence instance.      DEPRECATED: Use ApplicationConta** (1 connections) — `server/async_persistence.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/realtime/event_handler.py`
- `server/realtime/websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 34 (74%)
- INFERRED: 12 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*