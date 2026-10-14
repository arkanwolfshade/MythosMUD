# ConnectionManager

> 163 nodes

## Key Concepts

- **ConnectionManager** (193 connections) — `server/realtime/connection_manager.py`
- **UUID** (42 connections)
- **test_connection_manager_class.py** (15 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **ConnectionManager** (11 connections)
- **._track_player_disconnected()** (7 connections) — `server/realtime/connection_manager.py`
- **.broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (5 connections) — `server/realtime/connection_manager.py`
- **.track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **.canonical_room_id()** (4 connections) — `server/realtime/connection_manager.py`
- **._check_and_process_disconnect()** (4 connections) — `server/realtime/connection_manager.py`
- **.check_connection_health()** (4 connections) — `server/realtime/connection_manager.py`
- **._cleanup_dead_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **.force_disconnect_player()** (4 connections) — `server/realtime/connection_manager.py`
- **._get_players_batch()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_new_login()** (4 connections) — `server/realtime/connection_manager.py`
- **.mark_player_seen()** (4 connections) — `server/realtime/connection_manager.py`
- **._prune_player_from_all_rooms()** (4 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (4 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message_old()** (4 connections) — `server/realtime/connection_manager.py`
- **._validate_token()** (4 connections) — `server/realtime/connection_manager.py`
- **manager()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_broadcast_and_health_delegates()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **test_disconnect_and_session_delegates()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- *... and 138 more nodes in this community*

## Relationships

- [test_connection_error_methods.py](test_connection_error_methods.py.md) (10 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (9 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (7 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (6 shared connections)
- [AttributeError](AttributeError.md) (6 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (6 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (5 shared connections)
- [safe_close_websocket_impl](safe_close_websocket_impl.md) (5 shared connections)
- [FollowService](FollowService.md) (4 shared connections)
- [NpcDisposition](NpcDisposition.md) (4 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (4 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`

## Audit Trail

- EXTRACTED: 304 (84%)
- INFERRED: 59 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*