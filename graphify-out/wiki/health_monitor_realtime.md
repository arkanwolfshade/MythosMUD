# health monitor realtime

> 19 nodes

## Key Concepts

- **get_npc_lifecycle_manager_from_connection_manager()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **Protocol** (7 connections)
- **_AppWithState** (7 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateForEventHandler** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcLifecycleManagerForOccupants** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateWithNpcLifecycle** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_RealTimeHandlerContainer** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcOccupantDisplay** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_ContainerWithNpcLifecycle** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_get_event_handler_from_app_host()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state.container shape for resolving the real-time event handler.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal FastAPI/Starlette app shape for reading ``state``.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state shape for resolving the real-time event handler.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal NPC instance shape for room occupant name display.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal lifecycle manager shape for listing NPC names in a room.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state.container shape for resolving the NPC lifecycle manager.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state shape for resolving the NPC lifecycle manager.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Resolve NPC lifecycle manager from connection manager app state.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Resolve real-time event handler from a connection manager or websocket app.** (1 connections) — `server/realtime/websocket_initial_state.py`

## Relationships

- [realtime websocket initial](realtime_websocket_initial.md) (11 shared connections)
- [NATS Messaging](NATS_Messaging.md) (9 shared connections)
- [Room Broadcast](Room_Broadcast.md) (7 shared connections)

## Source Files

- `server/realtime/websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 47 (68%)
- INFERRED: 22 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*