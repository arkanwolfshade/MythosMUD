# Admin Setstat Support

> 81 nodes

## Key Concepts

- **admin_setstat_command.py** (35 connections) — `server/commands/admin_setstat_command.py`
- **admin_setstat_support.py** (33 connections) — `server/commands/admin_setstat_support.py`
- **SetStatTargetPlayer** (12 connections) — `server/commands/admin_setstat_support.py`
- **test_admin_setstat_command_context.py** (12 connections) — `server/tests/unit/commands/test_admin_setstat_command_context.py`
- **_apply_stat_change_and_build_result()** (10 connections) — `server/commands/admin_setstat_command.py`
- **_notify_player_stat_change()** (9 connections) — `server/commands/admin_setstat_command.py`
- **Protocol** (9 connections)
- **_execute_admin_set_stat()** (8 connections) — `server/commands/admin_setstat_command.py`
- **parse_set_stat_args()** (8 connections) — `server/commands/admin_setstat_support.py`
- **SetStatApp** (7 connections) — `server/commands/admin_setstat_support.py`
- **SetStatRequest** (7 connections) — `server/commands/admin_setstat_support.py`
- **_maybe_attach_dp_posture_message()** (7 connections) — `server/commands/admin_setstat_command.py`
- **build_set_stat_error_response()** (7 connections) — `server/commands/admin_setstat_support.py`
- **get_app_or_error()** (7 connections) — `server/commands/admin_setstat_support.py`
- **resolve_admin_services_and_permissions()** (7 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatApplyContext** (6 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatLogContext** (6 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatNotifyContext** (6 connections) — `server/commands/admin_setstat_support.py`
- **SetStatConnectionManager** (6 connections) — `server/commands/admin_setstat_support.py`
- **SetStatPersistence** (6 connections) — `server/commands/admin_setstat_support.py`
- **calculate_stat_warnings()** (6 connections) — `server/commands/admin_setstat_support.py`
- **log_admin_set_stat()** (6 connections) — `server/commands/admin_setstat_support.py`
- **target_player_uuid()** (6 connections) — `server/commands/admin_setstat_support.py`
- **test_notify_player_stat_change_dp_attaches_posture_message()** (6 connections) — `server/tests/unit/commands/test_admin_setstat_command_context.py`
- **_mutate_player_stat()** (5 connections) — `server/commands/admin_setstat_command.py`
- *... and 56 more nodes in this community*

## Relationships

- [Test Admin Setstat Command](Test_Admin_Setstat_Command.md) (16 shared connections)
- [Posture Notify](Posture_Notify.md) (3 shared connections)
- [Player Event Handlers State](Player_Event_Handlers_State.md) (3 shared connections)
- [Player Event Handlers Respawn Room](Player_Event_Handlers_Respawn_Room.md) (2 shared connections)
- [Player Effect Repository](Player_Effect_Repository.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Subject Controller](Subject_Controller.md) (1 shared connections)
- [Test Logout Commands Helpers](Test_Logout_Commands_Helpers.md) (1 shared connections)
- [Test Admin Commands](Test_Admin_Commands.md) (1 shared connections)
- [Alias Storage](Alias_Storage.md) (1 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (1 shared connections)
- [Test Envelope](Test_Envelope.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/commands/admin_setstat_support.py`
- `server/tests/unit/commands/test_admin_setstat_command_context.py`
- `server/tests/unit/persistence/test_player_effect_repository.py`

## Audit Trail

- EXTRACTED: 173 (94%)
- INFERRED: 12 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*