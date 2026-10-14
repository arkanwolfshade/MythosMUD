# admin_setstat_command.py

> 150 nodes

## Key Concepts

- **admin_setstat_command.py** (62 connections) — `server/commands/admin_setstat_command.py`
- **admin_setstat_support.py** (38 connections) — `server/commands/admin_setstat_support.py`
- **_handle_admin_set_stat_command()** (33 connections) — `server/commands/admin_setstat_command.py`
- **test_admin_setstat_command.py** (20 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **SetStatTargetPlayer** (14 connections) — `server/commands/admin_setstat_support.py`
- **asyncio** (14 connections)
- **_apply_lucidity_via_service()** (13 connections) — `server/commands/admin_setstat_command.py`
- **_apply_stat_change_and_build_result()** (12 connections) — `server/commands/admin_setstat_command.py`
- **normalize_posture()** (12 connections) — `server/realtime/posture_notify.py`
- **_apply_corruption_via_service()** (11 connections) — `server/commands/admin_setstat_command.py`
- **_notify_player_stat_change()** (11 connections) — `server/commands/admin_setstat_command.py`
- **test_admin_setstat_command_context.py** (11 connections) — `server/tests/unit/commands/test_admin_setstat_command_context.py`
- **AdminSetStatApplyContext** (10 connections) — `server/commands/admin_setstat_support.py`
- **_maybe_attach_dp_posture_message()** (10 connections) — `server/commands/admin_setstat_command.py`
- **_finish_occult_stat_change()** (9 connections) — `server/commands/admin_setstat_command.py`
- **Protocol** (9 connections)
- **SetStatConnectionManager** (8 connections) — `server/commands/admin_setstat_support.py`
- **_execute_admin_set_stat()** (8 connections) — `server/commands/admin_setstat_command.py`
- **build_set_stat_error_response()** (8 connections) — `server/commands/admin_setstat_support.py`
- **calculate_stat_warnings()** (8 connections) — `server/commands/admin_setstat_support.py`
- **get_app_or_error()** (8 connections) — `server/commands/admin_setstat_support.py`
- **log_admin_set_stat()** (8 connections) — `server/commands/admin_setstat_support.py`
- **parse_set_stat_args()** (8 connections) — `server/commands/admin_setstat_support.py`
- **resolve_admin_services_and_permissions()** (8 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatLogContext** (7 connections) — `server/commands/admin_setstat_support.py`
- *... and 125 more nodes in this community*

## Relationships

- [build_event](build_event.md) (13 shared connections)
- [command_error](command_error.md) (12 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (10 shared connections)
- [LucidityService](LucidityService.md) (6 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (3 shared connections)
- [command_service.py](command_service.py.md) (3 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (3 shared connections)
- [alias_storage.py](alias_storage.py.md) (3 shared connections)
- [CorruptionService](CorruptionService.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/commands/admin_setstat_support.py`
- `server/realtime/posture_notify.py`
- `server/tests/unit/commands/test_admin_setstat_command.py`
- `server/tests/unit/commands/test_admin_setstat_command_context.py`
- `server/tests/unit/realtime/test_message_category_invariants.py`

## Audit Trail

- EXTRACTED: 352 (95%)
- INFERRED: 18 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*