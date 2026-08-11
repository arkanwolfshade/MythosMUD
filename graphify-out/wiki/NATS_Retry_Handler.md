# NATS Retry Handler

> 15 nodes

## Key Concepts

- **RoomIDUtils** (20 connections) — `server/realtime/room_id_utils.py`
- **.__init__()** (3 connections) — `server/realtime/room_id_utils.py`
- **test_room_id_utils_init()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_get_canonical_room_id()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_get_canonical_room_id_no_manager()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_npc_room_match()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **.get_canonical_room_id()** (2 connections) — `server/realtime/room_id_utils.py`
- **Any** (1 connections)
- **Utilities for room ID normalization and comparison.** (1 connections) — `server/realtime/room_id_utils.py`
- **Initialize room ID utilities.          Args:             connection_manager: Con** (1 connections) — `server/realtime/room_id_utils.py`
- **Get canonical room ID for consistent comparison.          Args:             room** (1 connections) — `server/realtime/room_id_utils.py`
- **Test RoomIDUtils initialization.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test get_canonical_room_id returns canonical ID.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test get_canonical_room_id returns original when no manager.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test check_npc_room_match checks NPC room match.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`

## Relationships

- [Archive Effects System](Archive_Effects_System.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Admin Shutdown Commands](Admin_Shutdown_Commands.md) (2 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [Realtime Npc Event](Realtime_Npc_Event.md) (2 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (2 shared connections)

## Source Files

- `server/realtime/room_id_utils.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 43 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*