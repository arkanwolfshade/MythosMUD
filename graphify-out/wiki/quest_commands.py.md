# quest_commands.py

> 72 nodes · cohesion 0.05

## Key Concepts

- **quest_commands.py** (31 connections) — `server/commands/quest_commands.py`
- **handle_quest_command()** (21 connections) — `server/commands/quest_commands.py`
- **test_quest_commands.py** (20 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **Any** (16 connections)
- **handle_journal_command()** (15 connections) — `server/commands/quest_commands.py`
- **_get_lifecycle_manager()** (11 connections) — `server/commands/look_npc.py`
- **_resolve_quest_command_context()** (10 connections) — `server/commands/quest_commands.py`
- **_resolve_npc_in_player_room()** (8 connections) — `server/commands/quest_commands.py`
- **_get_quest_service()** (7 connections) — `server/commands/quest_commands.py`
- **_enter_quest_command_patches()** (7 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **UUID** (6 connections)
- **_resolve_player_id()** (6 connections) — `server/commands/quest_commands.py`
- **ExitStack** (5 connections)
- **_format_one_quest_entry()** (5 connections) — `server/commands/quest_commands.py`
- **_format_quest_log()** (5 connections) — `server/commands/quest_commands.py`
- **_get_container_and_persistence()** (5 connections) — `server/commands/quest_commands.py`
- **test_quest_ask_npc_not_in_room()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_ask_success()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_turnin_npc_not_in_room()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_turnin_success()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **_format_goal_line()** (4 connections) — `server/commands/quest_commands.py`
- **_format_quest_action_results()** (4 connections) — `server/commands/quest_commands.py`
- **_npc_definition_id()** (4 connections) — `server/commands/quest_commands.py`
- **_parse_quest_subcommand()** (4 connections) — `server/commands/quest_commands.py`
- **test_get_lifecycle_manager_no_lifecycle_manager()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- *... and 47 more nodes in this community*

## Relationships

- [test_look_npc.py](test_look_npc.py.md) (11 shared connections)
- [AliasStorage](AliasStorage.md) (9 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [QuestService](QuestService.md) (3 shared connections)
- [_should_include_npc](_should_include_npc.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [test_look_room.py](test_look_room.py.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/commands/quest_commands.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_quest_commands.py`

## Audit Trail

- EXTRACTED: 283 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*