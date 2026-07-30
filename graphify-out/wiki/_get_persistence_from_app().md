# . get persistence from app()

> 69 nodes

## Key Concepts

- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **test_command_helpers_functions.py** (17 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **validate_command_safety()** (17 connections) — `server/utils/command_helpers.py`
- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **AppWithState** (5 connections)
- **._get_persistence_from_app()** (5 connections) — `server/commands/combat_handler.py`
- **_username_from_dict()** (4 connections) — `server/utils/command_helpers.py`
- **test_validate_command_safety_safe_commands()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_shell_metacharacters()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_sql_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_python_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_format_string_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_xss_attempts()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_player_object()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_username_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_name_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_name()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_invalid()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_empty_dict()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_none()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_priority_player_over_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_safe()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_validate_command_safety_shell_metacharacters()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_validate_command_safety_sql_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- *... and 44 more nodes in this community*

## Relationships

- [lifespan shutdown](lifespan_shutdown.md) (21 shared connections)
- [Spell Targeting](Spell_Targeting.md) (7 shared connections)
- [Player Position Service](Player_Position_Service.md) (3 shared connections)
- [test command service](test_command_service.md) (3 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (2 shared connections)
- [.check and interrupt rest()](check_and_interrupt_rest%28%29.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (2 shared connections)
- [disconnect player connections()](disconnect_player_connections%28%29.md) (2 shared connections)
- [ContainerData](ContainerData.md) (2 shared connections)
- [.get room by id()](get_room_by_id%28%29.md) (2 shared connections)
- [Send a system message to](Send_a_system_message_to.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 188 (85%)
- INFERRED: 33 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*