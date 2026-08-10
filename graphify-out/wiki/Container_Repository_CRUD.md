# Container Repository CRUD

> 23 nodes

## Key Concepts

- **look_npc.py** (25 connections) — `server/commands/look_npc.py`
- **Any** (14 connections)
- **_format_npc_stats_for_admin()** (12 connections) — `server/commands/look_npc.py`
- **_try_lookup_npc_implicit()** (12 connections) — `server/commands/look_npc.py`
- **_find_matching_npcs()** (11 connections) — `server/commands/look_npc.py`
- **_format_lifecycle_info()** (11 connections) — `server/commands/look_npc.py`
- **_format_core_attributes()** (10 connections) — `server/commands/look_npc.py`
- **_format_other_stats()** (10 connections) — `server/commands/look_npc.py`
- **_format_single_npc_result()** (10 connections) — `server/commands/look_npc.py`
- **_format_multiple_npcs_result()** (6 connections) — `server/commands/look_npc.py`
- **test_format_core_attributes_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_single_npc_result_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **NPC look functionality for MythosMUD.  This module handles looking at NPCs, incl** (1 connections) — `server/commands/look_npc.py`
- **Find NPCs matching the target name.** (1 connections) — `server/commands/look_npc.py`
- **Format core attributes section.** (1 connections) — `server/commands/look_npc.py`
- **Format other stats section (excluding core attributes).** (1 connections) — `server/commands/look_npc.py`
- **Format lifecycle information section.** (1 connections) — `server/commands/look_npc.py`
- **Format NPC stats for admin display.** (1 connections) — `server/commands/look_npc.py`
- **Format result for a single matching NPC.** (1 connections) — `server/commands/look_npc.py`
- **Format result for multiple matching NPCs.** (1 connections) — `server/commands/look_npc.py`
- **Try to find and display an NPC in implicit lookup.** (1 connections) — `server/commands/look_npc.py`
- **Test formatting core attributes.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test formatting single NPC result successfully.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`

## Relationships

- [Look NPC Command](Look_NPC_Command.md) (26 shared connections)
- [Player State Command Factory](Player_State_Command_Factory.md) (13 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (4 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (4 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (3 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (3 shared connections)
- [Ground and Rescue Commands](Ground_and_Rescue_Commands.md) (3 shared connections)
- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (2 shared connections)
- [Logging System Planning](Logging_System_Planning.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (2 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`

## Audit Trail

- EXTRACTED: 137 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*