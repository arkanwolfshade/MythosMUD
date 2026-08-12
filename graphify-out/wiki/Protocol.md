# Protocol

> 13 nodes

## Key Concepts

- **Protocol** (7 connections)
- **_AppStateForEventHandler** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateWithNpcLifecycle** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_AppWithState** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_ContainerWithNpcLifecycle** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcOccupantDisplay** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_RealTimeHandlerContainer** (5 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state.container shape for resolving the real-time event handler.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal FastAPI/Starlette app shape for reading ``state``.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state shape for resolving the real-time event handler.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal NPC instance shape for room occupant name display.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state.container shape for resolving the NPC lifecycle manager.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state shape for resolving the NPC lifecycle manager.** (1 connections) — `server/realtime/websocket_initial_state.py`

## Relationships

- [websocket_initial_state.py](websocket_initial_state.py.md) (7 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (6 shared connections)

## Source Files

- `server/realtime/websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 31 (72%)
- INFERRED: 12 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*