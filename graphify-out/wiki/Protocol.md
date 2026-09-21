# Protocol

> 19 nodes

## Key Concepts

- **Protocol** (9 connections)
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
- **Send a room occupants snapshot to one connected player.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state.container shape for resolving the real-time event handler.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal FastAPI/Starlette app shape for reading ``state``.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state shape for resolving the real-time event handler.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal NPC instance shape for room occupant name display.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal lifecycle manager shape for listing NPC names in a room.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state.container shape for resolving the NPC lifecycle manager.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state shape for resolving the NPC lifecycle manager.** (1 connections) — `server/realtime/websocket_initial_state.py`

## Relationships

- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (10 shared connections)
- [player_event_handlers_respawn_room.py](player_event_handlers_respawn_room.py.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 29 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*