# Realtime Npc Event

> 10 nodes

## Key Concepts

- **.check_normalized_ids_match()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_normalized_room_matches()** (5 connections) — `server/realtime/room_id_utils.py`
- **test_check_normalized_ids_match()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_normalized_ids_match_none()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_normalized_room_matches()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Check if two normalized room IDs match.          Args:             id1: First no** (1 connections) — `server/realtime/room_id_utils.py`
- **Check if normalized NPC room IDs match normalized target room IDs.          Args** (1 connections) — `server/realtime/room_id_utils.py`
- **Test check_normalized_ids_match returns True for matching IDs.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test check_normalized_ids_match returns False when either ID is None.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test check_normalized_room_matches checks all combinations.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`

## Relationships

- [Archive Effects System](Archive_Effects_System.md) (3 shared connections)
- [NATS Retry Handler](NATS_Retry_Handler.md) (2 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (1 shared connections)

## Source Files

- `server/realtime/room_id_utils.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*