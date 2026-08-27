# test_error_logging.py

> 59 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (27 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **websocket_handler_app_state.py** (11 connections) — `server/realtime/websocket_handler_app_state.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_client_disconnected_exception()** (9 connections) — `server/realtime/websocket_helpers.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_runtime_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **resolve_and_setup_app_state_services()** (5 connections) — `server/realtime/websocket_handler_app_state.py`
- **cleanup_websocket_connection()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **send_welcome_event()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **UUID** (5 connections)
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_handler_disconnect.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_websocket_handler_helpers.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **_mirror_service_to_app_state()** (3 connections) — `server/realtime/websocket_handler_app_state.py`
- **_services_from_container()** (3 connections) — `server/realtime/websocket_handler_app_state.py`
- *... and 34 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (17 shared connections)
- [canonical_room_id_impl](canonical_room_id_impl.md) (8 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (7 shared connections)
- [test_goto_helpers.py](test_goto_helpers.py.md) (7 shared connections)
- [CombatAuditLogger](CombatAuditLogger.md) (6 shared connections)
- [test_admin_setstat_command.py](test_admin_setstat_command.py.md) (4 shared connections)
- [test_room_subscription_manager_drops.py](test_room_subscription_manager_drops.py.md) (4 shared connections)
- [App.tsx](App.tsx.md) (4 shared connections)
- [test_logging_processors.py](test_logging_processors.py.md) (4 shared connections)
- [field_validator](field_validator.md) (4 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_app_state.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`

## Audit Trail

- EXTRACTED: 159 (89%)
- INFERRED: 19 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*