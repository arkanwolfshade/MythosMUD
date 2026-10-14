# command_error

> 236 nodes

## Key Concepts

- **command_error()** (227 connections) — `server/commands/command_results.py`
- **admin_teleport_commands.py** (37 connections) — `server/commands/admin_teleport_commands.py`
- **admin_hallucinate_command.py** (34 connections) — `server/commands/admin_hallucinate_command.py`
- **test_goto_helpers.py** (32 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_teleport_helpers.py** (31 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **admin_confirm_teleport_commands.py** (28 connections) — `server/commands/admin_confirm_teleport_commands.py`
- **teleport_helpers.py** (28 connections) — `server/commands/teleport_helpers.py`
- **get_admin_actions_logger()** (27 connections) — `server/structured_logging/admin_actions_logger.py`
- **goto_helpers.py** (26 connections) — `server/commands/goto_helpers.py`
- **admin_teleport_utils.py** (24 connections) — `server/commands/admin_teleport_utils.py`
- **validate_admin_permission()** (22 connections) — `server/commands/admin_permission_utils.py`
- **handle_goto_command()** (21 connections) — `server/commands/admin_teleport_commands.py`
- **broadcast_teleport_effects()** (21 connections) — `server/commands/admin_teleport_utils.py`
- **notify_player_of_teleport()** (21 connections) — `server/commands/admin_teleport_utils.py`
- **asyncio** (21 connections)
- **admin_actions_logger.py** (20 connections) — `server/structured_logging/admin_actions_logger.py`
- **test_admin_commands_helpers.py** (20 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_admin_teleport_utils.py** (18 connections) — `server/tests/unit/commands/test_admin_teleport_utils.py`
- **create_teleport_effect_message()** (16 connections) — `server/commands/admin_teleport_utils.py`
- **patch** (16 connections)
- **get_online_player_by_display_name()** (15 connections) — `server/commands/admin_teleport_utils.py`
- **validate_goto_context()** (14 connections) — `server/commands/goto_helpers.py`
- **log_failed_admin_move()** (13 connections) — `server/commands/admin_teleport_utils.py`
- **execute_confirm_goto()** (12 connections) — `server/commands/goto_helpers.py`
- **execute_goto_teleport()** (12 connections) — `server/commands/goto_helpers.py`
- *... and 211 more nodes in this community*

## Relationships

- [alias_storage.py](alias_storage.py.md) (44 shared connections)
- [test_admin_teleport_commands.py](test_admin_teleport_commands.py.md) (36 shared connections)
- [command_service.py](command_service.py.md) (36 shared connections)
- [AliasStorage](AliasStorage.md) (33 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (24 shared connections)
- [get_logger](get_logger.md) (24 shared connections)
- [_handle_admin_hallucinate_command](_handle_admin_hallucinate_command.md) (15 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (12 shared connections)
- [test_admin_summon_command.py](test_admin_summon_command.py.md) (8 shared connections)
- [communication_commands_flows.py](communication_commands_flows.py.md) (8 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (7 shared connections)
- [test_room_system_message_categories.py](test_room_system_message_categories.py.md) (7 shared connections)

## Source Files

- `server/commands/admin_confirm_teleport_commands.py`
- `server/commands/admin_hallucinate_command.py`
- `server/commands/admin_permission_utils.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/admin_teleport_utils.py`
- `server/commands/command_results.py`
- `server/commands/goto_helpers.py`
- `server/commands/teleport_helpers.py`
- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/commands/test_admin_commands_helpers.py`
- `server/tests/unit/commands/test_admin_permission_utils.py`
- `server/tests/unit/commands/test_admin_teleport_utils.py`
- `server/tests/unit/commands/test_goto_helpers.py`
- `server/tests/unit/commands/test_teleport_helpers.py`
- `server/tests/unit/realtime/test_message_category_invariants.py`
- `server/tests/unit/realtime/test_room_system_message_categories.py`

## Audit Trail

- EXTRACTED: 901 (99%)
- INFERRED: 7 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*