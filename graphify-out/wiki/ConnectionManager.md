# ConnectionManager

> 180 nodes

## Key Concepts

- **ConnectionManager** (162 connections) — `server/realtime/connection_manager.py`
- **UUID** (41 connections)
- **Any** (40 connections)
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
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
- *... and 155 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (38 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (17 shared connections)
- [build_event](build_event.md) (11 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (9 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (4 shared connections)
- [bundles/game.py](bundles-game.py.md) (3 shared connections)
- [Room](Room.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/event_handlers.py`

## Audit Trail

- EXTRACTED: 648 (95%)
- INFERRED: 35 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*