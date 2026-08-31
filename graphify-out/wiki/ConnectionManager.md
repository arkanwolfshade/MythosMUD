# ConnectionManager

> 168 nodes

## Key Concepts

- **ConnectionManager** (169 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **test_connection_manager_class.py** (16 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **ConnectionManager** (11 connections)
- **._track_player_disconnected()** (7 connections) — `server/realtime/connection_manager.py`
- **.broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (5 connections) — `server/realtime/connection_manager.py`
- **.track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **.canonical_room_id()** (4 connections) — `server/realtime/connection_manager.py`
- **._check_and_process_disconnect()** (4 connections) — `server/realtime/connection_manager.py`
- **.check_connection_health()** (4 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (4 connections) — `server/realtime/connection_manager.py`
- **._cleanup_dead_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **.force_disconnect_player()** (4 connections) — `server/realtime/connection_manager.py`
- **._get_players_batch()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_authentication_error()** (4 connections) — `server/realtime/connection_manager.py`
- **._is_websocket_open()** (4 connections) — `server/realtime/connection_manager.py`
- **._prune_player_from_all_rooms()** (4 connections) — `server/realtime/connection_manager.py`
- **.recover_from_error()** (4 connections) — `server/realtime/connection_manager.py`
- **._safe_close_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (4 connections) — `server/realtime/connection_manager.py`
- **._validate_token()** (4 connections) — `server/realtime/connection_manager.py`
- *... and 143 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (12 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (8 shared connections)
- [test_connection_error_methods.py](test_connection_error_methods.py.md) (8 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (7 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (6 shared connections)
- [event_types.py](event_types.py.md) (5 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (4 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [emit_posture_change](emit_posture_change.md) (3 shared connections)
- [LootAllRequest](LootAllRequest.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 303 (87%)
- INFERRED: 44 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*