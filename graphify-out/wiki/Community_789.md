# Community 789

> 21 nodes

## Key Concepts

- **Protocol** (9 connections)
- **get_npc_lifecycle_manager_from_connection_manager()** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcLifecycleManagerForOccupants** (4 connections) — `server/realtime/websocket_initial_state.py`
- **_PlayerHandlerForOccupantsSnapshot** (4 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateForEventHandler** (3 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateWithNpcLifecycle** (3 connections) — `server/realtime/websocket_initial_state.py`
- **_AppWithState** (3 connections) — `server/realtime/websocket_initial_state.py`
- **_ContainerWithNpcLifecycle** (3 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcOccupantDisplay** (3 connections) — `server/realtime/websocket_initial_state.py`
- **_RealTimeHandlerContainer** (3 connections) — `server/realtime/websocket_initial_state.py`
- **.send_occupants_snapshot_to_player()** (3 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal player handler surface for sending occupants snapshots on connect.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Resolve NPC lifecycle manager from connection manager app state.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Send a room occupants snapshot to one connected player.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state.container shape for resolving the real-time event handler.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal FastAPI/Starlette app shape for reading ``state``.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state shape for resolving the real-time event handler.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal NPC instance shape for room occupant name display.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal lifecycle manager shape for listing NPC names in a room.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state.container shape for resolving the NPC lifecycle manager.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state shape for resolving the NPC lifecycle manager.** (1 connections) — `server/realtime/websocket_initial_state.py`

## Relationships

- [Community 57](Community_57.md) (12 shared connections)
- [Community 553](Community_553.md) (1 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*