# resolve_weapon_attack_from_equipped

> 65 nodes · cohesion 0.05

## Key Concepts

- **websocket_handler.py** (73 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (29 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_correlation_context.py** (12 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **get_message_validator()** (5 connections) — `server/realtime/message_validator.py`
- **test_connection_binds_context_fields_before_message_loop()** (5 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **test_websocket_handler_disconnect.py** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **_clear_context_around_test()** (4 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **test_message_loop_assigns_fresh_correlation_id_per_message()** (4 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **test_message_loop_ignores_client_supplied_correlation_id()** (4 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **test_websocket_handler_helpers.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **test_websocket_handler_json_error.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- **Exception** (3 connections)
- **asyncio** (3 connections)
- *... and 40 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (12 shared connections)
- [verify_enhanced_logging_compliance.py](verify_enhanced_logging_compliance.py.md) (11 shared connections)
- [test_game.py](test_game.py.md) (11 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (9 shared connections)
- [useAsciiMapState.ts](useAsciiMapState.ts.md) (7 shared connections)
- [test_corpse_lifecycle_decay.py](test_corpse_lifecycle_decay.py.md) (6 shared connections)
- [look_container.py](look_container.py.md) (4 shared connections)
- [Room](Room.md) (4 shared connections)
- [test_room_subscription_manager_drops.py](test_room_subscription_manager_drops.py.md) (4 shared connections)
- [NATSService](NATSService.md) (4 shared connections)
- [ContainerCreateParams](ContainerCreateParams.md) (3 shared connections)
- [.publish_with_pool](publish_with_pool.md) (2 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_correlation_context.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_json_error.py`

## Audit Trail

- EXTRACTED: 174 (91%)
- INFERRED: 18 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*