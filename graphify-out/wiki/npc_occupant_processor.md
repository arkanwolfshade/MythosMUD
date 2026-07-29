# npc occupant processor

> 48 nodes

## Key Concepts

- **RoomIDUtils** (20 connections) — `server/realtime/room_id_utils.py`
- **room_occupant_manager.py** (19 connections) — `server/realtime/room_occupant_manager.py`
- **test_room_id_utils.py** (15 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **npc_occupant_processor.py** (8 connections) — `server/realtime/npc_occupant_processor.py`
- **.normalize_room_id_for_comparison()** (7 connections) — `server/realtime/room_id_utils.py`
- **room_id_utils.py** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_normalized_ids_match()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_normalized_room_matches()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_npc_room_match()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_fallback_room_matches()** (4 connections) — `server/realtime/room_id_utils.py`
- **.__init__()** (3 connections) — `server/realtime/room_id_utils.py`
- **test_room_id_utils_init()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_get_canonical_room_id()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_get_canonical_room_id_no_manager()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_none()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_string()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_whitespace()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_empty()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_normalized_ids_match()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_normalized_ids_match_none()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_normalized_room_matches()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_fallback_room_matches()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_npc_room_match()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **.get_canonical_room_id()** (2 connections) — `server/realtime/room_id_utils.py`
- **Test normalize_room_id_for_comparison with None.** (2 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- *... and 23 more nodes in this community*

## Relationships

- [Any](Any.md) (8 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (4 shared connections)
- [main()](main%28%29.md) (4 shared connections)
- [occupant formatter](occupant_formatter.md) (2 shared connections)
- [disconnect grace period](disconnect_grace_period.md) (2 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (1 shared connections)
- [PlayerOccupantProcessor](PlayerOccupantProcessor.md) (1 shared connections)
- [test room occupant manager](test_room_occupant_manager.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/room_id_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 157 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*