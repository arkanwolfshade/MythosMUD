# Dual Connection Troubleshooting

> 21 nodes

## Key Concepts

- **get_npc_lifecycle_manager_from_connection_manager()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **Protocol** (7 connections)
- **_NpcLifecycleManagerForOccupants** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateWithNpcLifecycle** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_RealTimeHandlerContainer** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcOccupantDisplay** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_ContainerWithNpcLifecycle** (5 connections) — `server/realtime/websocket_initial_state.py`
- **test_add_npc_occupants_to_list_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_add_npc_occupants_to_list_no_app()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_add_npc_occupants_to_list_filters_dead_npcs()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Minimal app.state.container shape for resolving the real-time event handler.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal NPC instance shape for room occupant name display.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal lifecycle manager shape for listing NPC names in a room.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state.container shape for resolving the NPC lifecycle manager.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Minimal app.state shape for resolving the NPC lifecycle manager.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Resolve NPC lifecycle manager from connection manager app state.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Add NPC occupants to the occupant names list.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Test add_npc_occupants_to_list() adds NPC names to list.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test add_npc_occupants_to_list() does nothing when no app.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test add_npc_occupants_to_list() includes all NPCs (code doesn't filter dead).** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`

## Relationships

- [WebSocket Initial State](WebSocket_Initial_State.md) (15 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (5 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 56 (81%)
- INFERRED: 13 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*