# command_service.py

> 120 nodes

## Key Concepts

- **command_service.py** (108 connections) — `server/commands/command_service.py`
- **test_alias_commands.py** (31 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **server/commands/__init__.py** (29 connections) — `server/commands/__init__.py`
- **handle_alias_command()** (24 connections) — `server/commands/alias_commands.py`
- **asyncio** (23 connections)
- **handle_say_command()** (16 connections) — `server/commands/communication_commands.py`
- **get_help_content()** (15 connections) — `server/help/help_content.py`
- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
- **handle_pose_command()** (14 connections) — `server/commands/communication_commands.py`
- **handle_inventory_command()** (13 connections) — `server/commands/inventory_commands.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **handle_unalias_command()** (12 connections) — `server/commands/alias_commands.py`
- **help_content.py** (12 connections) — `server/help/help_content.py`
- **handle_aliases_command()** (11 connections) — `server/commands/alias_commands.py`
- **handle_help_command()** (11 connections) — `server/commands/system_commands.py`
- **exploration_commands.py** (11 connections) — `server/commands/exploration_commands.py`
- **test_help_commands.py** (6 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_websocket_handler_help.py** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **_create_alias()** (5 connections) — `server/commands/alias_commands.py`
- **_extract_alias_params()** (4 connections) — `server/commands/alias_commands.py`
- **_view_alias()** (4 connections) — `server/commands/alias_commands.py`
- **test_handle_alias_command_circular_reference()** (4 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_create_error()** (4 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_create_from_args()** (4 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_create_from_structured_data()** (4 connections) — `server/tests/unit/commands/test_alias_commands.py`
- *... and 95 more nodes in this community*

## Relationships

- [request_with_app_container](request_with_app_container.md) (19 shared connections)
- [AliasStorage](AliasStorage.md) (13 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (11 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (10 shared connections)
- [position_commands.py](position_commands.py.md) (8 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (6 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (6 shared connections)
- [get_username_from_user](get_username_from_user.md) (5 shared connections)
- [ValidationError](ValidationError.md) (5 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (4 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (4 shared connections)

## Source Files

- `server/commands/__init__.py`
- `server/commands/alias_commands.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands.py`
- `server/commands/exploration_commands.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/system_commands.py`
- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/tests/unit/commands/test_alias_commands.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 318 (83%)
- INFERRED: 67 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*