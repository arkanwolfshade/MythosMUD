# Server Config Loading

> 73 nodes

## Key Concepts

- **quest_commands.py** (32 connections) — `server/commands/quest_commands.py`
- **handle_quest_command()** (21 connections) — `server/commands/quest_commands.py`
- **test_quest_commands.py** (20 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **Any** (17 connections)
- **handle_journal_command()** (15 connections) — `server/commands/quest_commands.py`
- **_resolve_quest_command_context()** (10 connections) — `server/commands/quest_commands.py`
- **_handle_quest_npc_sub()** (8 connections) — `server/commands/quest_commands.py`
- **_get_quest_service()** (7 connections) — `server/commands/quest_commands.py`
- **_resolve_npc_in_player_room()** (7 connections) — `server/commands/quest_commands.py`
- **_enter_quest_command_patches()** (7 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **_resolve_player_id()** (6 connections) — `server/commands/quest_commands.py`
- **UUID** (6 connections)
- **_active_npc_ids_in_room()** (6 connections) — `server/commands/quest_commands.py`
- **_quest_command_ready()** (6 connections) — `server/commands/quest_commands.py`
- **_get_container_and_persistence()** (5 connections) — `server/commands/quest_commands.py`
- **_format_one_quest_entry()** (5 connections) — `server/commands/quest_commands.py`
- **_format_quest_log()** (5 connections) — `server/commands/quest_commands.py`
- **_handle_quest_abandon()** (5 connections) — `server/commands/quest_commands.py`
- **ExitStack** (5 connections)
- **test_quest_ask_success()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_ask_npc_not_in_room()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_turnin_success()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_turnin_npc_not_in_room()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **_parse_quest_subcommand()** (4 connections) — `server/commands/quest_commands.py`
- **_format_goal_line()** (4 connections) — `server/commands/quest_commands.py`
- *... and 48 more nodes in this community*

## Relationships

- [Container Open Events](Container_Open_Events.md) (12 shared connections)
- [Look NPC Command](Look_NPC_Command.md) (9 shared connections)
- [Quest Service Core](Quest_Service_Core.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [3. Systematic Investigation Approach](3._Systematic_Investigation_Approach.md) (1 shared connections)

## Source Files

- `server/commands/quest_commands.py`
- `server/tests/unit/commands/test_quest_commands.py`

## Audit Trail

- EXTRACTED: 290 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*