# pyrightconfig.json

> 10 nodes

## Key Concepts

- **asyncio** (33 connections)
- **test_handle_player_entered_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_broadcast_player_entered_message_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_log_player_movement_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_send_occupants_snapshot_to_player_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_send_occupants_snapshot_to_player_string_id()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test send_occupants_snapshot_to_player() handles string player_id.** (2 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test broadcast_player_entered_message() skips when room_id is None.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test handle_player_entered() skips when connection manager not available.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test log_player_movement() handles errors.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`

## Relationships

- [](unnamed.md) (15 shared connections)
- [Dialogue Content Tools (Content Creators)](Dialogue_Content_Tools_Content_Creators.md) (9 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [test_create_add_admin_command](test_create_add_admin_command.md) (1 shared connections)
- [test_create_admin_command](test_create_admin_command.md) (1 shared connections)
- [test_create_status_command](test_create_status_command.md) (1 shared connections)
- [test_create_mutes_command](test_create_mutes_command.md) (1 shared connections)
- [test_create_unmute_global_command](test_create_unmute_global_command.md) (1 shared connections)
- [test_create_mute_global_command](test_create_mute_global_command.md) (1 shared connections)
- [test_create_time_command](test_create_time_command.md) (1 shared connections)
- [test_command_factory_init](test_command_factory_init.md) (1 shared connections)
- [unit/services/nats_subject_manager/__init__.py](unit-services-nats_subject_manager-__init__.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_player_event_handlers_room.py`

## Audit Trail

- EXTRACTED: 43 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*