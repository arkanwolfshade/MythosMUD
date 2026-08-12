# send_game_event

> 62 nodes

## Key Concepts

- **send_game_event()** (28 connections) — `server/realtime/connection_manager_api.py`
- **message_handler_factory.py** (23 connections) — `server/realtime/message_handler_factory.py`
- **connection_manager_api.py** (16 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (15 connections) — `server/realtime/connection_manager_utils.py`
- **resolve_connection_manager()** (14 connections) — `server/realtime/connection_manager_utils.py`
- **message_handlers.py** (14 connections) — `server/realtime/message_handlers.py`
- **test_message_handlers.py** (12 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **lazy_import_api_function()** (11 connections) — `server/realtime/connection_manager_utils.py`
- **handle_command_message()** (11 connections) — `server/realtime/message_handlers.py`
- **broadcast_game_event()** (10 connections) — `server/realtime/connection_manager_api.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_ping_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_follow_response_message()** (9 connections) — `server/realtime/message_handlers.py`
- **handle_party_invite_response_message()** (8 connections) — `server/realtime/message_handlers.py`
- **asyncio** (7 connections)
- **send_player_status_update()** (6 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (6 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (6 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (6 connections) — `server/realtime/connection_manager_api.py`
- **handle_client_error_report_message()** (6 connections) — `server/realtime/message_handlers.py`
- **Any** (6 connections)
- **WebSocket** (6 connections)
- **UUID** (5 connections)
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **test_handle_chat_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- *... and 37 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [test_message_handler_factory.py](test_message_handler_factory.py.md) (10 shared connections)
- [build_event](build_event.md) (8 shared connections)
- [Any](Any.md) (6 shared connections)
- [magic_service.py](magic_service.py.md) (5 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (3 shared connections)
- [FollowService](FollowService.md) (3 shared connections)
- [bundles/game.py](bundles-game.py.md) (3 shared connections)
- [ErrorType](ErrorType.md) (3 shared connections)
- [MagicServiceHealingMixin](MagicServiceHealingMixin.md) (2 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (2 shared connections)

## Source Files

- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`
- `server/realtime/message_handler_factory.py`
- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 287 (92%)
- INFERRED: 25 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*