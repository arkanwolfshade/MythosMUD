# Realtime Event Delegation

> 84 nodes · cohesion 0.03

## Key Concepts

- **RealTimeEventHandler** (49 connections) — `server/realtime/event_handler.py`
- **test_event_handler.py** (38 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **Test RealTimeEventHandler._handle_player_entered() delegates to player_handler.** (8 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **_AppStateForEventHandler** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateWithNpcLifecycle** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_AppWithState** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_ContainerWithNpcLifecycle** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcOccupantDisplay** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_RealTimeHandlerContainer** (5 connections) — `server/realtime/websocket_initial_state.py`
- **Delegate player entered event to specialized handler.** (3 connections) — `server/realtime/event_handler.py`
- **._get_room_occupants()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_npc_entered()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_npc_left()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_delirium_respawned()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_died()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_dp_decay()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_dp_updated()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_entered()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_left()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_respawned()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_xp_awarded()** (3 connections) — `server/realtime/event_handler.py`
- **._send_occupants_snapshot_to_player()** (3 connections) — `server/realtime/event_handler.py`
- **.send_room_occupants_update()** (3 connections) — `server/realtime/event_handler.py`
- **._send_room_occupants_update_internal()** (3 connections) — `server/realtime/event_handler.py`
- **._subscribe_to_events()** (3 connections) — `server/realtime/event_handler.py`
- *... and 59 more nodes in this community*

## Relationships

- [[Player Respawn Events]] (25 shared connections)
- [[WebSocket Initial State]] (10 shared connections)
- [[Room Occupant Events]] (7 shared connections)
- [[Player Combat XP]] (7 shared connections)
- [[Realtime Service Bundle]] (5 shared connections)
- [[Distributed Event Bus]] (2 shared connections)
- [[NPC Services Bundle]] (2 shared connections)
- [[Player Event Handler Tests]] (2 shared connections)
- [[Player Death Service]] (2 shared connections)
- [[Respawn Occupant Enrichment]] (1 shared connections)
- [[Movement Service Tests]] (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_event_handler.py`

## Audit Trail

- EXTRACTED: 235 (88%)
- INFERRED: 31 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
