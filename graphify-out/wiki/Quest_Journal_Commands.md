# Quest Journal Commands

> 57 nodes · cohesion 0.05

## Key Concepts

- **quest_commands.py** (38 connections) — `server/commands/quest_commands.py`
- **handle_quest_command()** (21 connections) — `server/commands/quest_commands.py`
- **test_quest_commands.py** (20 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **Any** (18 connections)
- **handle_journal_command()** (15 connections) — `server/commands/quest_commands.py`
- **_get_lifecycle_manager()** (11 connections) — `server/commands/look_npc.py`
- **_resolve_quest_command_context()** (10 connections) — `server/commands/quest_commands.py`
- **_get_quest_service()** (7 connections) — `server/commands/quest_commands.py`
- **_resolve_npc_in_player_room()** (7 connections) — `server/commands/quest_commands.py`
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
- *... and 32 more nodes in this community*

## Relationships

- [Look NPC Command](Look_NPC_Command.md) (10 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (9 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Quest Service Core](Quest_Service_Core.md) (3 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (2 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (1 shared connections)
- [Logging Implementation Summary](Logging_Implementation_Summary.md) (1 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (1 shared connections)
- [Player Service Tests](Player_Service_Tests.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/commands/quest_commands.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_quest_commands.py`

## Audit Trail

- EXTRACTED: 276 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*