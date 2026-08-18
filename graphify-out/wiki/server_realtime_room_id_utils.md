# server realtime room id utils

> 40 nodes

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
- **test_check_npc_room_match()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_get_canonical_room_id()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_get_canonical_room_id_no_manager()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_room_id_utils_init()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **.get_canonical_room_id()** (2 connections) — `server/realtime/room_id_utils.py`
- **Check if NPC room IDs match target room IDs using fallback comparison. Args:…** (1 connections) — `server/realtime/room_id_utils.py`
- **Check if NPC room matches target room using normalized comparison. Args:…** (1 connections) — `server/realtime/room_id_utils.py`
- **Utilities for room ID normalization and comparison.** (1 connections) — `server/realtime/room_id_utils.py`
- **Get canonical room ID for consistent comparison. Args: room_id: The room ID…** (1 connections) — `server/realtime/room_id_utils.py`
- **Normalize room ID for comparison. Args: rid: Room ID to normalize Returns:…** (1 connections) — `server/realtime/room_id_utils.py`
- *... and 15 more nodes in this community*

## Relationships

- [server realtime npc occupant processor](server_realtime_npc_occupant_processor.md) (8 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)
- [server realtime room id utils](server_realtime_room_id_utils.md) (1 shared connections)

## Source Files

- `server/realtime/room_id_utils.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 63 (85%)
- INFERRED: 11 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*