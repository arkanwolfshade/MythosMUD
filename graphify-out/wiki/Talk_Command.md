# Talk Command

> 36 nodes

## Key Concepts

- **talk_command.py** (28 connections) — `server/commands/talk_command.py`
- **test_talk_command.py** (15 connections) — `server/tests/unit/commands/test_talk_command.py`
- **handle_talk_command()** (12 connections) — `server/commands/talk_command.py`
- **_emit_prompt()** (10 connections) — `server/commands/talk_command.py`
- **_talk_with_npc()** (9 connections) — `server/commands/talk_command.py`
- **get_dialogue_service()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **game/dialogue/__init__.py** (9 connections) — `server/game/dialogue/__init__.py`
- **_resolve_player_id()** (7 connections) — `server/commands/talk_command.py`
- **_talk_by_option_index()** (7 connections) — `server/commands/talk_command.py`
- **format_dialogue_prompt()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **_remainder_from_command_data()** (5 connections) — `server/commands/talk_command.py`
- **UUID** (5 connections)
- **test_talk_with_npc_success()** (4 connections) — `server/tests/unit/commands/test_talk_command.py`
- **asyncio** (4 connections)
- **test_emit_prompt_ended()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_emit_prompt_with_options()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_handle_talk_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_handle_talk_command_usage()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_talk_by_option_index_error_string()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_format_dialogue_prompt_numbers_options()** (3 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_remainder_from_command_data_list()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_remainder_from_command_data_string()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_resolve_player_id_invalid()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_resolve_player_id_uuid()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **talk / talk <n> command for NPC dialogue trees (#583).** (1 connections) — `server/commands/talk_command.py`
- *... and 11 more nodes in this community*

## Relationships

- [Dialogue Service](Dialogue_Service.md) (16 shared connections)
- [Test Communication Commands Flows](Test_Communication_Commands_Flows.md) (7 shared connections)
- [Quest Commands](Quest_Commands.md) (5 shared connections)
- [Test Chat Npc System](Test_Chat_Npc_System.md) (3 shared connections)
- [Test Go Command](Test_Go_Command.md) (3 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Test Rescue Commands](Test_Rescue_Commands.md) (1 shared connections)
- [Test Position Commands](Test_Position_Commands.md) (1 shared connections)
- [Test Command Parser](Test_Command_Parser.md) (1 shared connections)
- [Alias Storage](Alias_Storage.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/commands/talk_command.py`
- `server/game/dialogue/__init__.py`
- `server/game/dialogue/dialogue_service.py`
- `server/tests/unit/commands/test_talk_command.py`
- `server/tests/unit/game/test_dialogue_service.py`

## Audit Trail

- EXTRACTED: 104 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*