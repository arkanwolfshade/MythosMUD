# skill game service

> 13 nodes

## Key Concepts

- **verify_npc_occupants.py** (8 connections) — `server/scripts/verify_npc_occupants.py`
- **verify_npcs_in_lifecycle_manager()** (6 connections) — `server/scripts/verify_npc_occupants.py`
- **_check_service_availability()** (5 connections) — `server/scripts/verify_npc_occupants.py`
- **_collect_npcs_by_room()** (4 connections) — `server/scripts/verify_npc_occupants.py`
- **_test_query_for_room()** (4 connections) — `server/scripts/verify_npc_occupants.py`
- **Any** (3 connections)
- **_print_summary()** (3 connections) — `server/scripts/verify_npc_occupants.py`
- **Verification script to check NPCs in lifecycle manager and test occupant query l** (1 connections) — `server/scripts/verify_npc_occupants.py`
- **Check if NPC service, lifecycle manager, and active_npcs are available.      Ret** (1 connections) — `server/scripts/verify_npc_occupants.py`
- **Collect NPCs grouped by room ID.      Args:         active_npcs: Dictionary of a** (1 connections) — `server/scripts/verify_npc_occupants.py`
- **Test query logic for a specific room.      Args:         active_npcs: Dictionary** (1 connections) — `server/scripts/verify_npc_occupants.py`
- **Print verification summary.      Args:         npc_count: Total number of active** (1 connections) — `server/scripts/verify_npc_occupants.py`
- **Verify NPCs exist in lifecycle manager and test query logic.** (1 connections) — `server/scripts/verify_npc_occupants.py`

## Relationships

- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/scripts/verify_npc_occupants.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*