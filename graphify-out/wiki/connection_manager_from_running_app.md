# connection_manager_from_running_app

> 6 nodes

## Key Concepts

- **connection_manager_from_running_app()** (8 connections) — `server/realtime/running_app.py`
- **running_app.py** (5 connections) — `server/realtime/running_app.py`
- **_MainModule** (2 connections) — `server/realtime/running_app.py`
- **Protocol** (1 connections)
- **Read the running FastAPI app without a static import of server.main. A static…** (1 connections) — `server/realtime/running_app.py`
- **Return app.state.container.connection_manager, or None if unavailable.** (1 connections) — `server/realtime/running_app.py`

## Relationships

- [websocket_handler.py](websocket_handler.py.md) (3 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (3 shared connections)
- [.state](state.md) (1 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)

## Source Files

- `server/realtime/running_app.py`

## Audit Trail

- EXTRACTED: 11 (85%)
- INFERRED: 2 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*