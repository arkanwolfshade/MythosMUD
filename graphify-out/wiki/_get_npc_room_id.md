# _get_npc_room_id

> 16 nodes

## Key Concepts

- **_get_npc_room_id()** (14 connections) — `server/commands/look_npc.py`
- **_get_npcs_in_room()** (7 connections) — `server/commands/look_npc.py`
- **test_get_npc_room_id_from_current_room()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_get_npc_room_id_from_current_room_id()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_get_npc_room_id_none()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_get_npc_room_id_from_current_room()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_npc_room_id_from_current_room_id()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_npc_room_id_none()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Get the room ID from an NPC instance, checking both current_room and…** (1 connections) — `server/commands/look_npc.py`
- **Get list of NPC names in a room from lifecycle manager.** (1 connections) — `server/commands/look_npc.py`
- **Test _get_npc_room_id() returns current_room_id when available.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _get_npc_room_id() returns current_room when current_room_id is None.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _get_npc_room_id() returns None when both are None.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test getting NPC room ID from current_room_id.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting NPC room ID from current_room when current_room_id is None.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting NPC room ID when both are None.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`

## Relationships

- [test_look_npc.py](test_look_npc.py.md) (8 shared connections)
- [test_look_npc_helpers.py](test_look_npc_helpers.py.md) (4 shared connections)
- [quest_commands.py](quest_commands.py.md) (2 shared connections)
- [test_look_room.py](test_look_room.py.md) (2 shared connections)
- [_should_include_npc](_should_include_npc.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*