# Archive Bug Fix

> 14 nodes

## Key Concepts

- **_get_lifecycle_manager()** (11 connections) — `server/commands/look_npc.py`
- **_get_npcs_in_room()** (7 connections) — `server/commands/look_npc.py`
- **_resolve_npc_in_player_room()** (7 connections) — `server/commands/quest_commands.py`
- **_active_npc_ids_in_room()** (6 connections) — `server/commands/quest_commands.py`
- **test_get_lifecycle_manager_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_lifecycle_manager_no_service()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_lifecycle_manager_no_lifecycle_manager()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Get the lifecycle manager from the NPC instance service.** (1 connections) — `server/commands/look_npc.py`
- **Get list of NPC names in a room from lifecycle manager.** (1 connections) — `server/commands/look_npc.py`
- **Return active, includable NPC ids currently in room_id.** (1 connections) — `server/commands/quest_commands.py`
- **Find a single matching NPC in the player's current room.      Returns (npc_insta** (1 connections) — `server/commands/quest_commands.py`
- **Test getting lifecycle manager successfully.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting lifecycle manager when service not available.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting lifecycle manager when lifecycle_manager not available.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`

## Relationships

- [Combat Death Handling](Combat_Death_Handling.md) (6 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (4 shared connections)
- [Look NPC Command](Look_NPC_Command.md) (4 shared connections)
- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (2 shared connections)
- [Logging System Planning](Logging_System_Planning.md) (2 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (2 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/commands/quest_commands.py`
- `server/tests/unit/commands/test_look_npc.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*