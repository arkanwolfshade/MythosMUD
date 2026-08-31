# test_auth_utils.py

> 130 nodes

## Key Concepts

- **test_auth_utils.py** (53 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **AttributeError** (46 connections)
- **create_access_token()** (32 connections) — `server/auth_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **hash_password()** (18 connections) — `server/auth_utils.py`
- **test_connection_event_helpers.py** (14 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **subscribe_to_room_events_impl()** (10 connections) — `server/realtime/connection_event_helpers.py`
- **unsubscribe_from_room_events_impl()** (10 connections) — `server/realtime/connection_event_helpers.py`
- **verify_password()** (9 connections) — `server/auth_utils.py`
- **asyncio** (8 connections)
- **test_create_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_subscribe_to_room_events_impl_attribute_error()** (5 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_database_error()** (5 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_attribute_error()** (5 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_database_error()** (5 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **setup_jwt_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_jwt_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_audience()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_expired()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 105 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (31 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (6 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (3 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [real_time.py](real_time.py.md) (2 shared connections)
- [test_real_time_helpers.py](test_real_time_helpers.py.md) (2 shared connections)
- [test_argon2_utils.py](test_argon2_utils.py.md) (2 shared connections)
- [test_command_parser.py](test_command_parser.py.md) (2 shared connections)
- [test_status_commands.py](test_status_commands.py.md) (2 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (2 shared connections)
- [test_combat_persistence_handler_persistence.py](test_combat_persistence_handler_persistence.py.md) (2 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/realtime/connection_event_helpers.py`
- `server/tests/unit/auth/test_auth_utils.py`
- `server/tests/unit/realtime/test_connection_event_helpers.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 232 (79%)
- INFERRED: 61 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*