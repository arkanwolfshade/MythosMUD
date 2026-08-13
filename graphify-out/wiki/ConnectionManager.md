# ConnectionManager

> 174 nodes

## Key Concepts

- **ConnectionManager** (162 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **Any** (40 connections)
- **.check_connection_health()** (6 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (6 connections) — `server/realtime/connection_manager.py`
- **._track_player_disconnected()** (6 connections) — `server/realtime/connection_manager.py`
- **._broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.broadcast_to_room()** (5 connections) — `server/realtime/connection_manager.py`
- **.cleanup_dead_connections()** (5 connections) — `server/realtime/connection_manager.py`
- **.connect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.detect_and_handle_error_state()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_message_delivery_stats()** (5 connections) — `server/realtime/connection_manager.py`
- **.get_player_presence_info()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_players_batch()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_authentication_error()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_new_game_session()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_security_violation()** (5 connections) — `server/realtime/connection_manager.py`
- **.handle_websocket_error()** (5 connections) — `server/realtime/connection_manager.py`
- **.recover_from_error()** (5 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (5 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message_old()** (5 connections) — `server/realtime/connection_manager.py`
- **._track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **.validate_player_presence()** (5 connections) — `server/realtime/connection_manager.py`
- *... and 149 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (51 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (12 shared connections)
- [build_event](build_event.md) (10 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (9 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (6 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (5 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (4 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [websocket_handler_connection.py](websocket_handler_connection.py.md) (3 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (3 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 378 (94%)
- INFERRED: 25 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*