# test_command_communication.py

> 136 nodes · cohesion 0.03

## Key Concepts

- **admin_setstat_command.py** (62 connections) — `server/commands/admin_setstat_command.py`
- **admin_setstat_support.py** (38 connections) — `server/commands/admin_setstat_support.py`
- **_handle_admin_set_stat_command()** (33 connections) — `server/commands/admin_setstat_command.py`
- **test_admin_setstat_command.py** (20 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **SetStatTargetPlayer** (14 connections) — `server/commands/admin_setstat_support.py`
- **asyncio** (14 connections)
- **_apply_lucidity_via_service()** (13 connections) — `server/commands/admin_setstat_command.py`
- **_apply_stat_change_and_build_result()** (12 connections) — `server/commands/admin_setstat_command.py`
- **_apply_corruption_via_service()** (11 connections) — `server/commands/admin_setstat_command.py`
- **_notify_player_stat_change()** (11 connections) — `server/commands/admin_setstat_command.py`
- **test_admin_setstat_command_context.py** (11 connections) — `server/tests/unit/commands/test_admin_setstat_command_context.py`
- **AdminSetStatApplyContext** (10 connections) — `server/commands/admin_setstat_support.py`
- **_finish_occult_stat_change()** (9 connections) — `server/commands/admin_setstat_command.py`
- **Protocol** (9 connections)
- **_execute_admin_set_stat()** (8 connections) — `server/commands/admin_setstat_command.py`
- **build_set_stat_error_response()** (8 connections) — `server/commands/admin_setstat_support.py`
- **calculate_stat_warnings()** (8 connections) — `server/commands/admin_setstat_support.py`
- **get_app_or_error()** (8 connections) — `server/commands/admin_setstat_support.py`
- **log_admin_set_stat()** (8 connections) — `server/commands/admin_setstat_support.py`
- **parse_set_stat_args()** (8 connections) — `server/commands/admin_setstat_support.py`
- **resolve_admin_services_and_permissions()** (8 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatLogContext** (7 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatNotifyContext** (7 connections) — `server/commands/admin_setstat_support.py`
- **SetStatApp** (7 connections) — `server/commands/admin_setstat_support.py`
- **SetStatRequest** (7 connections) — `server/commands/admin_setstat_support.py`
- *... and 111 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (17 shared connections)
- [WearableContainerServiceError](WearableContainerServiceError.md) (14 shared connections)
- [PopulationStats](PopulationStats.md) (6 shared connections)
- [Room](Room.md) (4 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (4 shared connections)
- [.publish_with_pool](publish_with_pool.md) (3 shared connections)
- [reset_database](reset_database.md) (3 shared connections)
- [FollowService](FollowService.md) (3 shared connections)
- [look_container.py](look_container.py.md) (3 shared connections)
- [test_shopkeeper_npc.py](test_shopkeeper_npc.py.md) (3 shared connections)
- [ItemFactory](ItemFactory.md) (2 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/commands/admin_setstat_support.py`
- `server/tests/unit/commands/test_admin_setstat_command.py`
- `server/tests/unit/commands/test_admin_setstat_command_context.py`

## Audit Trail

- EXTRACTED: 324 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*