# WebSocket Initial State

> 88 nodes · cohesion 0.04

## Key Concepts

- **websocket_initial_state.py** (44 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_initial_state.py** (41 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (8 connections) — `server/realtime/websocket_initial_state.py`
- **WebSocket** (7 connections) — `server/realtime/websocket_initial_state.py`
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_initial_room_data()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **test_send_game_state_event_safely_close_message_sent()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **_get_death_location_name()** (4 connections) — `server/realtime/websocket_initial_state.py`
- **test_add_npc_occupants_to_list_filters_dead_npcs()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_add_npc_occupants_to_list_no_app()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_add_npc_occupants_to_list_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_in_limbo()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_alive()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_dead()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_get_event_handler_for_initial_state_from_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- *... and 63 more nodes in this community*

## Relationships

- [[WebSocket Helper Utilities]] (14 shared connections)
- [[Realtime Event Delegation]] (10 shared connections)
- [[WebSocket Player Helpers]] (7 shared connections)
- [[Room Occupant Events]] (6 shared connections)
- [[Combat Player Broadcasts]] (5 shared connections)
- [[WebSocket Message Validation]] (4 shared connections)
- [[Respawn Occupant Enrichment]] (4 shared connections)
- [[Realtime WebSocket Auth]] (3 shared connections)
- [[Integer Coercion Utils]] (3 shared connections)
- [[Player Domain Model]] (2 shared connections)
- [[Room Occupancy Class]] (2 shared connections)
- [[Look Command Helpers]] (2 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 350 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
