# extract_room_id_from_npc

> 16 nodes

## Key Concepts

- **extract_room_id_from_npc()** (15 connections) — `server/npc/npc_utils.py`
- **test_extract_room_id_from_npc_current_room()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_current_room_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_non_string()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_not_found()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_room_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_skips_unknown_sentinel()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_extract_room_id_from_npc_spawn_room_id()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Extract room ID from NPC instance with fallback logic. Args: npc_instance: The…** (1 connections) — `server/npc/npc_utils.py`
- **Test extract_room_id_from_npc() extracts from current_room.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_room_id_from_npc() extracts from current_room_id.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_room_id_from_npc() extracts from room_id.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_room_id_from_npc() falls back to spawn_room_id.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Literal 'unknown' on current_room must fall through to a real attr.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_room_id_from_npc() returns 'unknown' when not found.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Test extract_room_id_from_npc() returns 'unknown' for non-string value.** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`

## Relationships

- [test_npc_utils.py](test_npc_utils.py.md) (8 shared connections)
- [NPCDied](NPCDied.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [npc_utils.py](npc_utils.py.md) (2 shared connections)

## Source Files

- `server/npc/npc_utils.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 29 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*