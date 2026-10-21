# .load_room_data

> 62 nodes · cohesion 0.05

## Key Concepts

- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **test_command_helpers.py** (21 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **validate_command_safety()** (17 connections) — `server/utils/command_helpers.py`
- **command_helpers.py** (16 connections) — `server/utils/command_helpers.py`
- **test_command_helpers_functions.py** (13 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_username_from_user_empty_dict()** (4 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_invalid()** (4 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_none()** (4 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_username_from_user_with_name()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_username_from_user_with_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_validate_command_safety_format_string()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_validate_command_safety_python_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_validate_command_safety_safe()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_validate_command_safety_shell_metacharacters()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_validate_command_safety_sql_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_validate_command_safety_xss()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_username_from_user_dict_name()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_name_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_player_object()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_priority_player_over_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_username_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_format_string_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_python_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- *... and 37 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [CommandFactory](CommandFactory.md) (3 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (2 shared connections)
- [QuestService](QuestService.md) (2 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (2 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (2 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (2 shared connections)
- [command_parser.py](command_parser.py.md) (1 shared connections)
- [properties](properties.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 106 (76%)
- INFERRED: 34 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*