# Container Repository CRUD

> 45 nodes

## Key Concepts

- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **teach_command.py** (15 connections) — `server/commands/teach_command.py`
- **handle_teach_command()** (14 connections) — `server/commands/teach_command.py`
- **test_teach_command.py** (6 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Any** (5 connections)
- **_get_teach_services()** (4 connections) — `server/commands/teach_command.py`
- **_resolve_npc_teacher()** (4 connections) — `server/commands/teach_command.py`
- **_username_from_dict()** (4 connections) — `server/utils/command_helpers.py`
- **_format_teach_result()** (3 connections) — `server/commands/teach_command.py`
- **test_handle_teach_command()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_target()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_get_username_from_user_player_object()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_username_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_name_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_name()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_invalid()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_empty_dict()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_none()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_priority_player_over_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_with_name()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_username_from_user_with_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_username_from_user_dict()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **Any** (2 connections)
- *... and 20 more nodes in this community*

## Relationships

- [WebSocket Handler Helpers](WebSocket_Handler_Helpers.md) (16 shared connections)
- [Client Event Store](Client_Event_Store.md) (8 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (7 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (3 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (3 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (3 shared connections)
- [Player Event Handler Tests](Player_Event_Handler_Tests.md) (3 shared connections)
- [Logging Migration Examples](Logging_Migration_Examples.md) (2 shared connections)
- [Legacy Error Sanitization](Legacy_Error_Sanitization.md) (2 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (2 shared connections)
- [Plan Modernization Archive](Plan_Modernization_Archive.md) (1 shared connections)
- [Player State Factories](Player_State_Factories.md) (1 shared connections)

## Source Files

- `server/commands/teach_command.py`
- `server/tests/unit/commands/test_teach_command.py`
- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 138 (80%)
- INFERRED: 34 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*