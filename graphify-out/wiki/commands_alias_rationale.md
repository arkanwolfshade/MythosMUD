# commands alias rationale

> 83 nodes

## Key Concepts

- **test_alias_commands.py** (30 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **__init__.py** (29 connections) — `server/commands/__init__.py`
- **handle_alias_command()** (24 connections) — `server/commands/alias_commands.py`
- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
- **handle_unalias_command()** (12 connections) — `server/commands/alias_commands.py`
- **handle_aliases_command()** (11 connections) — `server/commands/alias_commands.py`
- **handle_help_command()** (11 connections) — `server/commands/system_commands.py`
- **_create_alias()** (5 connections) — `server/commands/alias_commands.py`
- **test_help_commands.py** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **_extract_alias_params()** (4 connections) — `server/commands/alias_commands.py`
- **Any** (4 connections)
- **_view_alias()** (4 connections) — `server/commands/alias_commands.py`
- **help_commands.py** (4 connections) — `server/commands/help_commands.py`
- **_validate_alias_params()** (3 connections) — `server/commands/alias_commands.py`
- **test_handle_alias_command_no_storage()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_no_args()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_view_existing()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_view_nonexistent()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_create_from_args()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_create_from_structured_data()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_invalid_name_too_long()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_invalid_command_too_long()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_circular_reference()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_create_error()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_aliases_command_no_storage()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- *... and 58 more nodes in this community*

## Relationships

- [commands admin mute](commands_admin_mute.md) (7 shared connections)
- [commands party examples](commands_party_examples.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [position player service](position_player_service.md) (4 shared connections)
- [message nats handler](message_nats_handler.md) (3 shared connections)
- [eventLog projectorRoom roomMergeUtils](eventLog_projectorRoom_roomMergeUtils.md) (2 shared connections)
- [commands inventory put](commands_inventory_put.md) (2 shared connections)
- [command helpers functions](command_helpers_functions.md) (2 shared connections)
- [combat services initialization](combat_services_initialization.md) (1 shared connections)
- [commands communication flows](commands_communication_flows.md) (1 shared connections)
- [commands command rationale](commands_command_rationale.md) (1 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (1 shared connections)

## Source Files

- `server/commands/__init__.py`
- `server/commands/alias_commands.py`
- `server/commands/help_commands.py`
- `server/commands/system_commands.py`
- `server/tests/unit/commands/test_alias_commands.py`
- `server/tests/unit/commands/test_help_commands.py`

## Audit Trail

- EXTRACTED: 278 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*