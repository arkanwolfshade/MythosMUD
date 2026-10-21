# WearableContainerServiceError

> 84 nodes · cohesion 0.04

## Key Concepts

- **test_room_system_message_categories.py** (35 connections) — `server/tests/unit/realtime/test_room_system_message_categories.py`
- **emit_posture_change()** (31 connections) — `server/realtime/posture_notify.py`
- **posture_notify.py** (27 connections) — `server/realtime/posture_notify.py`
- **test_posture_notify.py** (16 connections) — `server/tests/unit/realtime/test_posture_notify.py`
- **format_room_posture_message()** (13 connections) — `server/realtime/posture_notify.py`
- **attach_posture_self_message()** (12 connections) — `server/realtime/posture_notify.py`
- **normalize_posture()** (12 connections) — `server/realtime/posture_notify.py`
- **_ConnectionRecorder** (11 connections) — `server/tests/unit/realtime/test_room_system_message_categories.py`
- **_maybe_attach_dp_posture_message()** (10 connections) — `server/commands/admin_setstat_command.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **SetStatConnectionManager** (8 connections) — `server/commands/admin_setstat_support.py`
- **test_admin_broadcast_event_is_system_info()** (8 connections) — `server/tests/unit/realtime/test_room_system_message_categories.py`
- **_PostureConnectionManager** (7 connections) — `server/realtime/posture_notify.py`
- **_drive_setstat_posture()** (7 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **test_send_room_message_tags_every_npc_room_message_as_room_movement()** (7 connections) — `server/tests/unit/realtime/test_room_system_message_categories.py`
- **test_send_system_message_maps_message_type_to_category()** (7 connections) — `server/tests/unit/realtime/test_room_system_message_categories.py`
- **_send_personal_posture_message()** (6 connections) — `server/realtime/posture_notify.py`
- **_data()** (6 connections) — `server/tests/unit/realtime/test_room_system_message_categories.py`
- **asyncio** (6 connections)
- **test_teleport_system_events_are_system_info()** (6 connections) — `server/tests/unit/realtime/test_room_system_message_categories.py`
- **_as()** (5 connections) — `server/tests/unit/realtime/test_room_system_message_categories.py`
- **_SocketRecorder** (5 connections) — `server/tests/unit/realtime/test_room_system_message_categories.py`
- **test_posture_change_room_event_is_room_movement()** (5 connections) — `server/tests/unit/realtime/test_room_system_message_categories.py`
- **_broadcast_room_posture_change()** (4 connections) — `server/realtime/posture_notify.py`
- **UUID** (4 connections)
- *... and 59 more nodes in this community*

## Relationships

- [look_container.py](look_container.py.md) (19 shared connections)
- [test_command_communication.py](test_command_communication.py.md) (14 shared connections)
- [ConnectionManager](ConnectionManager.md) (10 shared connections)
- [ErrorContext](ErrorContext.md) (5 shared connections)
- [.publish_with_pool](publish_with_pool.md) (4 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (4 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (4 shared connections)
- [BaseEvent](BaseEvent.md) (4 shared connections)
- [PlayerCombatState](PlayerCombatState.md) (3 shared connections)
- [.initialize](initialize.md) (3 shared connections)
- [schema.sql](schema.sql.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/commands/admin_setstat_support.py`
- `server/realtime/posture_notify.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/tests/unit/realtime/test_message_category_invariants.py`
- `server/tests/unit/realtime/test_posture_notify.py`
- `server/tests/unit/realtime/test_room_system_message_categories.py`

## Audit Trail

- EXTRACTED: 219 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*