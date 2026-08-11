# Archive Effects System

> 12 nodes

## Key Concepts

- **test_room_id_utils.py** (15 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **.normalize_room_id_for_comparison()** (7 connections) — `server/realtime/room_id_utils.py`
- **test_normalize_room_id_for_comparison_none()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_string()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_whitespace()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_normalize_room_id_for_comparison_empty()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Normalize room ID for comparison.          Args:             rid: Room ID to nor** (1 connections) — `server/realtime/room_id_utils.py`
- **Unit tests for room ID utilities.  Tests the RoomIDUtils class for room ID norma** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test normalize_room_id_for_comparison with None.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test normalize_room_id_for_comparison with string.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test normalize_room_id_for_comparison strips whitespace.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test normalize_room_id_for_comparison returns None for empty string.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`

## Relationships

- [NATS Retry Handler](NATS_Retry_Handler.md) (6 shared connections)
- [Realtime Npc Event](Realtime_Npc_Event.md) (3 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/realtime/room_id_utils.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 40 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*