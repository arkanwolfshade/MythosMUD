# _get_lifecycle_manager

> 10 nodes

## Key Concepts

- **_get_lifecycle_manager()** (11 connections) — `server/commands/look_npc.py`
- **_get_npcs_in_room()** (7 connections) — `server/commands/look_npc.py`
- **test_get_lifecycle_manager_no_lifecycle_manager()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_lifecycle_manager_no_service()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_lifecycle_manager_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Get the lifecycle manager from the NPC instance service.** (1 connections) — `server/commands/look_npc.py`
- **Get list of NPC names in a room from lifecycle manager.** (1 connections) — `server/commands/look_npc.py`
- **Test getting lifecycle manager successfully.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting lifecycle manager when service not available.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting lifecycle manager when lifecycle_manager not available.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`

## Relationships

- [test_look_npc.py](test_look_npc.py.md) (4 shared connections)
- [look_npc.py](look_npc.py.md) (3 shared connections)
- [quest_commands.py](quest_commands.py.md) (2 shared connections)
- [test_look_room.py](test_look_room.py.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [test_look_npc_helpers.py](test_look_npc_helpers.py.md) (1 shared connections)
- [_should_include_npc](_should_include_npc.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*