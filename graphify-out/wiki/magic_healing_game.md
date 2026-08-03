# magic healing game

> 19 nodes

## Key Concepts

- **RoomIDUtils** (22 connections) — `server/realtime/room_id_utils.py`
- **npc_occupant_processor.py** (9 connections) — `server/realtime/npc_occupant_processor.py`
- **room_id_utils.py** (6 connections) — `server/realtime/room_id_utils.py`
- **.__init__()** (3 connections) — `server/realtime/room_id_utils.py`
- **test_room_id_utils_init()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_get_canonical_room_id()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_get_canonical_room_id_no_manager()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **test_check_npc_room_match()** (3 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **.get_canonical_room_id()** (2 connections) — `server/realtime/room_id_utils.py`
- **NPC occupant processing utilities.  This module handles querying and processing** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Any** (1 connections)
- **Room ID normalization and comparison utilities.  This module provides utilities** (1 connections) — `server/realtime/room_id_utils.py`
- **Utilities for room ID normalization and comparison.** (1 connections) — `server/realtime/room_id_utils.py`
- **Initialize room ID utilities.          Args:             connection_manager: Con** (1 connections) — `server/realtime/room_id_utils.py`
- **Get canonical room ID for consistent comparison.          Args:             room** (1 connections) — `server/realtime/room_id_utils.py`
- **Test RoomIDUtils initialization.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test get_canonical_room_id returns canonical ID.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test get_canonical_room_id returns original when no manager.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`
- **Test check_npc_room_match checks NPC room match.** (1 connections) — `server/tests/unit/realtime/test_room_id_utils.py`

## Relationships

- [time service rationale](time_service_rationale.md) (8 shared connections)
- [event bus events](event_bus_events.md) (6 shared connections)
- [look helpers commands](look_helpers_commands.md) (4 shared connections)
- [dead letter realtime](dead_letter_realtime.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [AppRouter main AppRouter()](AppRouter_main_AppRouter%28%29.md) (1 shared connections)
- [message realtime messaging](message_realtime_messaging.md) (1 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/room_id_utils.py`
- `server/tests/unit/realtime/test_room_id_utils.py`

## Audit Trail

- EXTRACTED: 62 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*