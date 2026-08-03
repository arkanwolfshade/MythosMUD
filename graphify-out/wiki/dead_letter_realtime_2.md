# dead letter realtime

> 10 nodes

## Key Concepts

- **.check_normalized_room_matches()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_npc_room_match()** (5 connections) — `server/realtime/room_id_utils.py`
- **.check_fallback_room_matches()** (4 connections) — `server/realtime/room_id_utils.py`
- **test_check_normalized_room_matches()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_fallback_room_matches()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Check if normalized NPC room IDs match normalized target room IDs.          Args** (1 connections) — `server/realtime/room_id_utils.py`
- **Check if NPC room IDs match target room IDs using fallback comparison.** (1 connections) — `server/realtime/room_id_utils.py`
- **Check if NPC room matches target room using normalized comparison.          Args** (1 connections) — `server/realtime/room_id_utils.py`
- **Test check_normalized_room_matches checks all combinations.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test check_fallback_room_matches checks fallback matches.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`

## Relationships

- [time service rationale](time_service_rationale.md) (4 shared connections)
- [magic healing game](magic_healing_game.md) (3 shared connections)

## Source Files

- `server/realtime/room_id_utils.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*