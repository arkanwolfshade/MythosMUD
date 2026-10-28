# test_shopkeeper_npc.py

> 71 nodes · cohesion 0.06

## Key Concepts

- **AdminActionsLogger** (31 connections) — `server/structured_logging/admin_actions_logger.py`
- **get_admin_actions_logger()** (27 connections) — `server/structured_logging/admin_actions_logger.py`
- **validate_admin_permission()** (22 connections) — `server/commands/admin_permission_utils.py`
- **test_admin_actions_logger.py** (21 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **admin_actions_logger.py** (20 connections) — `server/structured_logging/admin_actions_logger.py`
- **test_admin_permission_utils.py** (11 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **admin_permission_utils.py** (10 connections) — `server/commands/admin_permission_utils.py`
- **._log_entry()** (8 connections) — `server/structured_logging/admin_actions_logger.py`
- **Any** (8 connections)
- **_read_log_entries()** (7 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **._read_actions_from_file()** (6 connections) — `server/structured_logging/admin_actions_logger.py`
- **asyncio** (6 connections)
- **Path** (6 connections)
- **._get_log_file_path()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **.get_recent_actions()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **.__init__()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_teleport_action()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **._action_entry_matches_filters()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.get_teleport_statistics()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_admin_command()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_permission_check()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **TeleportActionInput** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **_BrokenAdminPlayer** (4 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_attribute_error()** (4 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_logs_secondary_failure()** (4 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- *... and 46 more nodes in this community*

## Relationships

- [ErrorContext](ErrorContext.md) (11 shared connections)
- [Async Code Review - Post Phase 2 Migration](Async_Code_Review_-_Post_Phase_2_Migration.md) (8 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (7 shared connections)
- [command_parser.py](command_parser.py.md) (6 shared connections)
- [npc_database.py](npc_database.py.md) (6 shared connections)
- [Room](Room.md) (5 shared connections)
- [test_command_communication.py](test_command_communication.py.md) (3 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (2 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (1 shared connections)
- [security.ts](security.ts.md) (1 shared connections)
- [inventory_item_matching.py](inventory_item_matching.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_permission_utils.py`
- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/commands/test_admin_permission_utils.py`
- `server/tests/unit/structured_logging/test_admin_actions_logger.py`

## Audit Trail

- EXTRACTED: 176 (93%)
- INFERRED: 14 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*