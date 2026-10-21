# Persistence Layer Refactoring - COMPLETE ✅

> 55 nodes · cohesion 0.07

## Key Concepts

- **talk_command.py** (30 connections) — `server/commands/talk_command.py`
- **dialogue_service.py** (17 connections) — `server/game/dialogue/dialogue_service.py`
- **handle_talk_command()** (14 connections) — `server/commands/talk_command.py`
- **test_talk_command.py** (14 connections) — `server/tests/unit/commands/test_talk_command.py`
- **DialoguePrompt** (12 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service.py** (12 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **_emit_prompt()** (10 connections) — `server/commands/talk_command.py`
- **_talk_with_npc()** (9 connections) — `server/commands/talk_command.py`
- **get_dialogue_service()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **game/dialogue/__init__.py** (9 connections) — `server/game/dialogue/__init__.py`
- **_resolve_player_id()** (7 connections) — `server/commands/talk_command.py`
- **_talk_by_option_index()** (7 connections) — `server/commands/talk_command.py`
- **format_dialogue_prompt()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **reset_dialogue_service_for_tests()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **UUID** (5 connections)
- **_remainder_from_command_data()** (5 connections) — `server/commands/talk_command.py`
- **test_dialogue_service_start_and_choose()** (5 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **asyncio** (4 connections)
- **test_talk_with_npc_success()** (4 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_dialogue_service_choose_without_cursor()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_emit_prompt_ended()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_emit_prompt_with_options()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_handle_talk_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_handle_talk_command_usage()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_talk_by_option_index_error_string()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- *... and 30 more nodes in this community*

## Relationships

- [test_shutdown_sequence.py](test_shutdown_sequence.py.md) (14 shared connections)
- [command_parser.py](command_parser.py.md) (8 shared connections)
- [BaseCommand](BaseCommand.md) (7 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (5 shared connections)
- [Room](Room.md) (4 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (3 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (3 shared connections)
- [endpoints.py](endpoints.py.md) (2 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [.load_room_data](load_room_data.md) (1 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (1 shared connections)

## Source Files

- `server/commands/talk_command.py`
- `server/game/dialogue/__init__.py`
- `server/game/dialogue/dialogue_service.py`
- `server/tests/unit/commands/test_talk_command.py`
- `server/tests/unit/game/test_dialogue_service.py`

## Audit Trail

- EXTRACTED: 142 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*