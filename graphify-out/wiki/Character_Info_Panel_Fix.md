# Character Info Panel Fix

> 14 nodes

## Key Concepts

- **_get_npc_room_id()** (14 connections) — `server/commands/look_npc.py`
- **test_get_npc_room_id_from_current_room_id()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_npc_room_id_from_current_room()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_npc_room_id_none()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_npc_room_id_from_current_room_id()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_get_npc_room_id_from_current_room()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_get_npc_room_id_none()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Get the room ID from an NPC instance, checking both current_room and current_roo** (1 connections) — `server/commands/look_npc.py`
- **Test getting NPC room ID from current_room_id.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting NPC room ID from current_room when current_room_id is None.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting NPC room ID when both are None.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test _get_npc_room_id() returns current_room_id when available.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _get_npc_room_id() returns current_room when current_room_id is None.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _get_npc_room_id() returns None when both are None.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`

## Relationships

- [Look NPC Command](Look_NPC_Command.md) (4 shared connections)
- [Player State Command Factory](Player_State_Command_Factory.md) (4 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (2 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (2 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*