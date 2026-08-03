# time service rationale

> 18 nodes

## Key Concepts

- **test_room_id_utils.py** (15 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **.normalize_room_id_for_comparison()** (7 connections) — `server/realtime/room_id_utils.py`
- **.check_normalized_ids_match()** (5 connections) — `server/realtime/room_id_utils.py`
- **test_normalize_room_id_for_comparison_none()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_string()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_whitespace()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_empty()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_normalized_ids_match()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_normalized_ids_match_none()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Normalize room ID for comparison.          Args:             rid: Room ID to nor** (1 connections) — `server/realtime/room_id_utils.py`
- **Check if two normalized room IDs match.          Args:             id1: First no** (1 connections) — `server/realtime/room_id_utils.py`
- **Unit tests for room ID utilities.  Tests the RoomIDUtils class for room ID norma** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test normalize_room_id_for_comparison with None.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test normalize_room_id_for_comparison with string.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test normalize_room_id_for_comparison strips whitespace.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test normalize_room_id_for_comparison returns None for empty string.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test check_normalized_ids_match returns True for matching IDs.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test check_normalized_ids_match returns False when either ID is None.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`

## Relationships

- [magic healing game](magic_healing_game.md) (8 shared connections)
- [dead letter realtime](dead_letter_realtime.md) (4 shared connections)

## Source Files

- `server/realtime/room_id_utils.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*