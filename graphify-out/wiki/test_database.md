# test database

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

- [look npc](look_npc.md) (4 shared connections)
- [ChatHistoryToggle()](ChatHistoryToggle%28%29.md) (4 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [Tests for handle special command](Tests_for_handle_special_command.md) (2 shared connections)
- [.get room by id()](get_room_by_id%28%29.md) (1 shared connections)

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