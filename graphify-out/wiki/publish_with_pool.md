# .publish_with_pool

> 77 nodes · cohesion 0.04

## Key Concepts

- **build_event()** (123 connections) — `server/realtime/envelope.py`
- **envelope.py** (35 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (33 connections) — `server/tests/unit/realtime/test_envelope.py`
- **rest_countdown_task.py** (18 connections) — `server/commands/rest_countdown_task.py`
- **create_rest_countdown_task()** (9 connections) — `server/commands/rest_countdown_task.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **_handle_countdown_loop()** (7 connections) — `server/commands/rest_countdown_task.py`
- **UUID** (6 connections)
- **_send_countdown_message()** (6 connections) — `server/commands/rest_countdown_task.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **_disconnect_player_after_rest()** (5 connections) — `server/commands/rest_countdown_task.py`
- **_is_rest_interrupted()** (5 connections) — `server/commands/rest_countdown_task.py`
- **Any** (5 connections)
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **_broadcast_command_room_if_needed()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **test_build_event_defaults_command_response_to_command_output()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_json_serializable()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_sequence_priority()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_handles_other_types()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **_get_next_global_sequence()** (3 connections) — `server/realtime/envelope.py`
- **test_build_event_all_parameters()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_basic()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_empty_data()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_keeps_an_explicit_command_response_category()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- *... and 52 more nodes in this community*

## Relationships

- [look_container.py](look_container.py.md) (26 shared connections)
- [security.ts](security.ts.md) (9 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (8 shared connections)
- [Room](Room.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (5 shared connections)
- [RoomNodeData](RoomNodeData.md) (5 shared connections)
- [ErrorContext](ErrorContext.md) (4 shared connections)
- [authenticated.ts](authenticated.ts.md) (4 shared connections)
- [WearableContainerServiceError](WearableContainerServiceError.md) (4 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (4 shared connections)
- [asyncio](asyncio.md) (4 shared connections)

## Source Files

- `server/commands/rest_countdown_task.py`
- `server/realtime/envelope.py`
- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 261 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*