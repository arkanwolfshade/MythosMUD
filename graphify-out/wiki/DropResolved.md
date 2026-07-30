# DropResolved

> 120 nodes

## Key Concepts

- **command_service.py** (92 connections) — `server/commands/command_service.py`
- **admin_summon_command.py** (34 connections) — `server/commands/admin_summon_command.py`
- **test_inventory_helpers_extended.py** (26 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_inventory_commands_more_helpers.py** (23 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **resolve_state()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_player()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **broadcast_room_event()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **get_help_content()** (14 connections) — `server/help/help_content.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **handle_help_command()** (12 connections) — `server/commands/system_commands.py`
- **help_content.py** (12 connections) — `server/help/help_content.py`
- **_resolve_summon_context()** (11 connections) — `server/commands/admin_summon_command.py`
- **Any** (10 connections)
- **handle_summon_command()** (10 connections) — `server/commands/admin_summon_command.py`
- **_broadcast_and_log_summon_success()** (7 connections) — `server/commands/admin_summon_command.py`
- **_complete_summon()** (7 connections) — `server/commands/admin_summon_command.py`
- **_persist_summoned_item()** (6 connections) — `server/commands/admin_summon_command.py`
- **test_inventory_commands_state_helpers.py** (6 connections) — `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- **_parse_summon_command_data()** (5 connections) — `server/commands/admin_summon_command.py`
- **test_help_commands.py** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_websocket_handler_help.py** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **_validate_summon_prerequisites()** (4 connections) — `server/commands/admin_summon_command.py`
- **_summon_npc_stub_response()** (4 connections) — `server/commands/admin_summon_command.py`
- **_create_summon_item_instance()** (4 connections) — `server/commands/admin_summon_command.py`
- **_log_summon_success()** (4 connections) — `server/commands/admin_summon_command.py`
- *... and 95 more nodes in this community*

## Relationships

- [Any](Any.md) (26 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (12 shared connections)
- [test magic commands](test_magic_commands.md) (11 shared connections)
- [test command factories inventory](test_command_factories_inventory.md) (10 shared connections)
- [Player Position Service](Player_Position_Service.md) (10 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (9 shared connections)
- [CommandHandler](CommandHandler.md) (6 shared connections)
- [real time](real_time.md) (5 shared connections)
- [AuthSlice](AuthSlice.md) (4 shared connections)
- [.initialize()](initialize%28%29.md) (4 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (4 shared connections)
- [.get instance()](get_instance%28%29.md) (4 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`
- `server/commands/command_service.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/system_commands.py`
- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 519 (97%)
- INFERRED: 15 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*