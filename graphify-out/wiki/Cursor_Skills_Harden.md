# Cursor Skills Harden

> 51 nodes

## Key Concepts

- **player_service()** (23 connections) — `docs/examples/logging/fastapi_integration.py`
- **party_commands.py** (19 connections) — `server/commands/party_commands.py`
- **teach_command.py** (15 connections) — `server/commands/teach_command.py`
- **handle_teach_command()** (14 connections) — `server/commands/teach_command.py`
- **handle_party_command()** (12 connections) — `server/commands/party_commands.py`
- **handle_system_command()** (10 connections) — `server/commands/system_commands.py`
- **Any** (9 connections)
- **chat_service** (6 connections) — `docs/examples/logging/websocket_integration.py`
- **_get_party_command_context()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_invite()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_kick()** (6 connections) — `server/commands/party_commands.py`
- **test_system_commands.py** (6 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_teach_command.py** (6 connections) — `server/tests/unit/commands/test_teach_command.py`
- **_handle_party_chat()** (5 connections) — `server/commands/party_commands.py`
- **_handle_party_list()** (5 connections) — `server/commands/party_commands.py`
- **Any** (5 connections)
- **_get_container()** (4 connections) — `server/commands/party_commands.py`
- **_get_member_display()** (4 connections) — `server/commands/party_commands.py`
- **_get_teach_services()** (4 connections) — `server/commands/teach_command.py`
- **_resolve_npc_teacher()** (4 connections) — `server/commands/teach_command.py`
- **_handle_party_leave()** (3 connections) — `server/commands/party_commands.py`
- **_format_teach_result()** (3 connections) — `server/commands/teach_command.py`
- **test_handle_system_command()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_message()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- **test_handle_system_command_no_chat_service()** (3 connections) — `server/tests/unit/commands/test_system_commands.py`
- *... and 26 more nodes in this community*

## Relationships

- [Container Open Events](Container_Open_Events.md) (21 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (9 shared connections)
- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (6 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (2 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (2 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (2 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (2 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (2 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (1 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (1 shared connections)
- [Combat Messaging Tests](Combat_Messaging_Tests.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/websocket_integration.py`
- `server/commands/party_commands.py`
- `server/commands/system_commands.py`
- `server/commands/teach_command.py`
- `server/tests/unit/commands/test_system_commands.py`
- `server/tests/unit/commands/test_teach_command.py`

## Audit Trail

- EXTRACTED: 187 (86%)
- INFERRED: 31 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*