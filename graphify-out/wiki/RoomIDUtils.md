# RoomIDUtils

> 43 nodes

## Key Concepts

- **RoomIDUtils** (30 connections) — `server/realtime/room_id_utils.py`
- **test_room_id_utils.py** (15 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **.normalize_room_id_for_comparison()** (7 connections) — `server/realtime/room_id_utils.py`
- **.check_normalized_ids_match()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_normalized_room_matches()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_npc_room_match()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_fallback_room_matches()** (4 connections) — `server/realtime/room_id_utils.py`
- **test_check_fallback_room_matches()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_normalized_ids_match()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_normalized_ids_match_none()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_normalized_room_matches()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_empty()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_none()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_string()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_whitespace()** (4 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **.__init__()** (3 connections) — `server/realtime/room_id_utils.py`
- **test_check_npc_room_match()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_get_canonical_room_id()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_get_canonical_room_id_no_manager()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_room_id_utils_init()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **.get_canonical_room_id()** (2 connections) — `server/realtime/room_id_utils.py`
- **Any** (1 connections)
- **Check if NPC room IDs match target room IDs using fallback comparison. Args:…** (1 connections) — `server/realtime/room_id_utils.py`
- **Check if NPC room matches target room using normalized comparison. Args:…** (1 connections) — `server/realtime/room_id_utils.py`
- **Utilities for room ID normalization and comparison.** (1 connections) — `server/realtime/room_id_utils.py`
- *... and 18 more nodes in this community*

## Relationships

- [NPCOccupantProcessor](NPCOccupantProcessor.md) (7 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (2 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/realtime/room_id_utils.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 61 (80%)
- INFERRED: 15 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*