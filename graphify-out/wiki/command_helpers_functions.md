# command helpers functions

> 88 nodes

## Key Concepts

- **get_username_from_user()** (51 connections) — `server/utils/command_helpers.py`
- **test_command_helpers.py** (27 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_command_helpers_functions.py** (17 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **validate_command_safety()** (17 connections) — `server/utils/command_helpers.py`
- **command_helpers.py** (15 connections) — `server/utils/command_helpers.py`
- **handle_teach_command()** (12 connections) — `server/commands/teach_command.py`
- **get_command_help()** (12 connections) — `server/utils/command_helpers.py`
- **test_teach_command.py** (6 connections) — `server/tests/unit/commands/test_teach_command.py`
- **_username_from_dict()** (4 connections) — `server/utils/command_helpers.py`
- **test_handle_teach_command()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_target()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_validate_command_safety_safe_commands()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_shell_metacharacters()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_sql_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_python_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_format_string_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_xss_attempts()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_no_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_specific_commands()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_unknown_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_case_insensitive()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_player_object()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_username_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_name_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- *... and 63 more nodes in this community*

## Relationships

- [commands alias rationale](commands_alias_rationale.md) (13 shared connections)
- [command inventory factories](command_inventory_factories.md) (7 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [commands admin mute](commands_admin_mute.md) (3 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (3 shared connections)
- [commands rescue rationale](commands_rescue_rationale.md) (3 shared connections)
- [command utility models](command_utility_models.md) (2 shared connections)
- [command handler unified](command_handler_unified.md) (2 shared connections)
- [commands logout rationale](commands_logout_rationale.md) (2 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (2 shared connections)
- [target resolution service](target_resolution_service.md) (1 shared connections)
- [rest grace period](rest_grace_period.md) (1 shared connections)

## Source Files

- `server/commands/teach_command.py`
- `server/tests/unit/commands/test_teach_command.py`
- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 276 (89%)
- INFERRED: 34 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*