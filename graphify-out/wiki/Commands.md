# Commands

> 13 nodes · cohesion 0.17

## Key Concepts

- **_get_npc_room_id()** (14 connections) — `server/commands/look_npc.py`
- **test_get_npc_room_id_from_current_room()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_get_npc_room_id_from_current_room_id()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_get_npc_room_id_none()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_get_npc_room_id_from_current_room()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_npc_room_id_from_current_room_id()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_npc_room_id_none()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Get the room ID from an NPC instance, checking both current_room and…** (1 connections) — `server/commands/look_npc.py`
- **Test _get_npc_room_id() returns current_room_id when available.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _get_npc_room_id() returns current_room when current_room_id is None.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _get_npc_room_id() returns None when both are None.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test getting NPC room ID from current_room_id.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting NPC room ID when both are None.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`

## Relationships

- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) (6 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (4 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*