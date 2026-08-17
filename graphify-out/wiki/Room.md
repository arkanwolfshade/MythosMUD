# room

> 105 nodes

## Key Concepts

- **test_websocket_initial_state.py** (47 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **websocket_initial_state.py** (34 connections) — `server/realtime/websocket_initial_state.py`
- **asyncio** (21 connections)
- **send_initial_room_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **check_and_send_death_notification()** (12 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (11 connections) — `server/realtime/websocket_initial_state.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **get_npc_lifecycle_manager_from_connection_manager()** (7 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (7 connections) — `server/realtime/websocket_initial_state.py`
- **Protocol** (7 connections)
- **UUID** (6 connections)
- **prepare_initial_room_data()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **mock_connection_manager()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_in_limbo()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_alive()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_dead()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_game_state_success()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **WebSocket** (5 connections)
- **_NpcLifecycleManagerForOccupants** (4 connections) — `server/realtime/websocket_initial_state.py`
- **_get_death_location_name()** (4 connections) — `server/realtime/websocket_initial_state.py`
- **_get_event_handler_from_app_host()** (4 connections) — `server/realtime/websocket_initial_state.py`
- **_get_player_for_death_check()** (4 connections) — `server/realtime/websocket_initial_state.py`
- *... and 80 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (18 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (4 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (3 shared connections)
- [playercombatservice](playercombatservice.md) (3 shared connections)
- [server realtime player event handlers](server_realtime_player_event_handlers.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (2 shared connections)
- [server commands inventory command coercion](server_commands_inventory_command_coercion.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 213 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*