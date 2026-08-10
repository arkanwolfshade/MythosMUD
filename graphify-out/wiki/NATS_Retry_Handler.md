# NATS Retry Handler

> 45 nodes

## Key Concepts

- **RoomIDUtils** (20 connections) — `server/realtime/room_id_utils.py`
- **test_room_id_utils.py** (15 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **.normalize_room_id_for_comparison()** (7 connections) — `server/realtime/room_id_utils.py`
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
- **Any** (1 connections)
- **Utilities for room ID normalization and comparison.** (1 connections) — `server/realtime/room_id_utils.py`
- **Initialize room ID utilities.          Args:             connection_manager: Con** (1 connections) — `server/realtime/room_id_utils.py`
- *... and 20 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (4 shared connections)
- [Admin Shutdown Commands](Admin_Shutdown_Commands.md) (3 shared connections)
- [Contexts Themecontext Hooks](Contexts_Themecontext_Hooks.md) (1 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (1 shared connections)
- [Spell Effects Tests](Spell_Effects_Tests.md) (1 shared connections)

## Source Files

- `server/realtime/room_id_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 132 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*