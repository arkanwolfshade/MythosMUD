# Chat NATS Publisher

> 135 nodes

## Key Concepts

- **command_service.py** (92 connections) — `server/commands/command_service.py`
- **.__init__()** (71 connections) — `server/commands/command_service.py`
- **command_parser.py** (45 connections) — `server/utils/command_parser.py`
- **__init__.py** (29 connections) — `server/commands/__init__.py`
- **request_with_app_container()** (28 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- **test_communication_commands_say_me_pose.py** (22 connections) — `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- **position_commands.py** (21 connections) — `server/commands/position_commands.py`
- **test_communication_commands_channels.py** (20 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **handle_say_command()** (17 connections) — `server/commands/communication_commands.py`
- **handle_pose_command()** (14 connections) — `server/commands/communication_commands.py`
- **handle_unalias_command()** (13 connections) — `server/commands/alias_commands.py`
- **handle_aliases_command()** (12 connections) — `server/commands/alias_commands.py`
- **handle_global_command()** (12 connections) — `server/commands/communication_commands.py`
- **_handle_position_change()** (12 connections) — `server/commands/position_commands.py`
- **handle_help_command()** (12 connections) — `server/commands/system_commands.py`
- **handle_local_command()** (11 connections) — `server/commands/communication_commands.py`
- **test_position_commands.py** (11 connections) — `server/tests/unit/commands/test_position_commands.py`
- **_format_room_posture_message()** (10 connections) — `server/commands/position_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_lie_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_sit_command()** (9 connections) — `server/commands/position_commands.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **handle_me_command()** (8 connections) — `server/commands/communication_commands.py`
- **Any** (6 connections)
- **communication_commands_mocks.py** (5 connections) — `server/tests/unit/commands/communication_commands_mocks.py`
- *... and 110 more nodes in this community*

## Relationships

- [Quest Journal Commands](Quest_Journal_Commands.md) (24 shared connections)
- [Character Creation API](Character_Creation_API.md) (20 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (18 shared connections)
- [Client Event Store](Client_Event_Store.md) (18 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (17 shared connections)
- [NPC Admin Commands](NPC_Admin_Commands.md) (11 shared connections)
- [Deprecated Logging Patterns](Deprecated_Logging_Patterns.md) (10 shared connections)
- [Memory Threshold Monitor](Memory_Threshold_Monitor.md) (10 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (9 shared connections)
- [Player Event Handler Tests](Player_Event_Handler_Tests.md) (8 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (7 shared connections)
- [Command Parser](Command_Parser.md) (6 shared connections)

## Source Files

- `server/commands/__init__.py`
- `server/commands/alias_commands.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands.py`
- `server/commands/help_commands.py`
- `server/commands/position_commands.py`
- `server/commands/system_commands.py`
- `server/tests/unit/commands/communication_commands_mocks.py`
- `server/tests/unit/commands/test_communication_commands_channels.py`
- `server/tests/unit/commands/test_communication_commands_say_me_pose.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 642 (88%)
- INFERRED: 88 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*