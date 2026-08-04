# connection realtime manager

> 80 nodes

## Key Concepts

- **get_username_from_user()** (53 connections) — `server/utils/command_helpers.py`
- **test_command_helpers.py** (27 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **command_helpers.py** (18 connections) — `server/utils/command_helpers.py`
- **test_command_helpers_functions.py** (17 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **validate_command_safety()** (17 connections) — `server/utils/command_helpers.py`
- **get_command_help()** (12 connections) — `server/utils/command_helpers.py`
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
- **test_get_username_from_user_dict_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_name()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_invalid()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_empty_dict()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_none()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_priority_player_over_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- *... and 55 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (11 shared connections)
- [commands admin mute](commands_admin_mute.md) (3 shared connections)
- [commands position system](commands_position_system.md) (3 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [command factories create](command_factories_create.md) (2 shared connections)
- [command commands handler](command_commands_handler.md) (2 shared connections)
- [commands logout rationale](commands_logout_rationale.md) (2 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (2 shared connections)
- [command helpers functions](command_helpers_functions.md) (2 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (1 shared connections)
- [rest grace period](rest_grace_period.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 253 (87%)
- INFERRED: 37 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*