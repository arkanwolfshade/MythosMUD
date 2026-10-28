# NATSConnectionStateMachine

> 116 nodes · cohesion 0.04

## Key Concepts

- **test_connection_session_management.py** (49 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **ConnectionMetadata** (30 connections) — `server/realtime/connection_models.py`
- **connection_session_management.py** (26 connections) — `server/realtime/connection_session_management.py`
- **_as_mgr()** (21 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_make_manager()** (20 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **handle_new_game_session_impl()** (15 connections) — `server/realtime/connection_session_management.py`
- **_SessionConnectionManager** (15 connections) — `server/realtime/connection_session_management.py`
- **_as_ws()** (14 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_disconnect_connection_for_session()** (13 connections) — `server/realtime/connection_session_management.py`
- **_FakeWebSocket** (13 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **asyncio** (13 connections)
- **_disconnect_all_connections_for_session()** (10 connections) — `server/realtime/connection_session_management.py`
- **_cleanup_old_session_tracking()** (9 connections) — `server/realtime/connection_session_management.py`
- **_is_websocket_connected()** (9 connections) — `server/realtime/connection_session_management.py`
- **_migrate_player_to_new_session()** (9 connections) — `server/realtime/connection_session_management.py`
- **test_connection_models.py** (9 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **test_disconnect_all_connections_for_session()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_all_connections_for_session_partial_success()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_close_error()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_key_error()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_handle_new_game_session_impl_same_session_is_noop()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_handle_new_game_session_impl_success()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_cleanup_player_data_for_session()** (8 connections) — `server/realtime/connection_session_management.py`
- **NewGameSessionResult** (8 connections) — `server/realtime/connection_session_management.py`
- **test_disconnect_connection_for_session_not_connected()** (8 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- *... and 91 more nodes in this community*

## Relationships

- [test_npc_utils.py](test_npc_utils.py.md) (9 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (9 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (8 shared connections)
- [ChatService](ChatService.md) (4 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (4 shared connections)
- [SpellEffects](SpellEffects.md) (3 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (3 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_models.py`
- `server/realtime/connection_session_management.py`
- `server/tests/unit/realtime/test_connection_models.py`
- `server/tests/unit/realtime/test_connection_session_management.py`

## Audit Trail

- EXTRACTED: 294 (95%)
- INFERRED: 14 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*