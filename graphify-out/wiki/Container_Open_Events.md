# Container Open Events

> 161 nodes

## Key Concepts

- **command_service.py** (92 connections) — `server/commands/command_service.py`
- **.__init__()** (71 connections) — `server/commands/command_service.py`
- **__init__.py** (29 connections) — `server/commands/__init__.py`
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **position_commands.py** (21 connections) — `server/commands/position_commands.py`
- **handle_mute_command()** (20 connections) — `server/commands/admin_mute_commands.py`
- **Any** (16 connections)
- **get_help_content()** (14 connections) — `server/help/help_content.py`
- **handle_unmute_command()** (13 connections) — `server/commands/admin_mute_commands.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **handle_add_admin_command()** (12 connections) — `server/commands/admin_mute_commands.py`
- **handle_mutes_command()** (12 connections) — `server/commands/admin_mute_commands.py`
- **_handle_position_change()** (12 connections) — `server/commands/position_commands.py`
- **handle_help_command()** (12 connections) — `server/commands/system_commands.py`
- **test_position_commands.py** (11 connections) — `server/tests/unit/commands/test_position_commands.py`
- **handle_mute_global_command()** (10 connections) — `server/commands/admin_mute_commands.py`
- **handle_unmute_global_command()** (10 connections) — `server/commands/admin_mute_commands.py`
- **_format_room_posture_message()** (10 connections) — `server/commands/position_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_lie_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_system_command()** (10 connections) — `server/commands/system_commands.py`
- **handle_sit_command()** (9 connections) — `server/commands/position_commands.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **handle_me_command()** (8 connections) — `server/commands/communication_commands.py`
- **_perform_mutes_list()** (7 connections) — `server/commands/admin_mute_commands.py`
- *... and 136 more nodes in this community*

## Relationships

- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (39 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (24 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (16 shared connections)
- [Client Event Store](Client_Event_Store.md) (13 shared connections)
- [Communication Command Handlers](Communication_Command_Handlers.md) (11 shared connections)
- [Character Creation API](Character_Creation_API.md) (11 shared connections)
- [NPC Admin Commands](NPC_Admin_Commands.md) (11 shared connections)
- [Game Client Container](Game_Client_Container.md) (8 shared connections)
- [Player Event Handler Tests](Player_Event_Handler_Tests.md) (7 shared connections)
- [Health Check Service](Health_Check_Service.md) (6 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (6 shared connections)
- [Room Drop Renderer](Room_Drop_Renderer.md) (5 shared connections)

## Source Files

- `server/commands/__init__.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands.py`
- `server/commands/help_commands.py`
- `server/commands/position_commands.py`
- `server/commands/system_commands.py`
- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/tests/unit/commands/test_admin_commands.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/tests/unit/commands/test_system_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 613 (82%)
- INFERRED: 138 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*