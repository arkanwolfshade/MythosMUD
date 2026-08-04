# event bus events

> 28 nodes

## Key Concepts

- **NPCOccupantProcessor** (31 connections) — `server/realtime/npc_occupant_processor.py`
- **RoomIDUtils** (22 connections) — `server/realtime/room_id_utils.py`
- **room_occupant_manager.py** (19 connections) — `server/realtime/room_occupant_manager.py`
- **test_npc_occupant_processor.py** (17 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **npc_occupant_processor.py** (9 connections) — `server/realtime/npc_occupant_processor.py`
- **room_id_utils.py** (6 connections) — `server/realtime/room_id_utils.py`
- **.__init__()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **processor()** (3 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **.get_canonical_room_id()** (2 connections) — `server/realtime/room_id_utils.py`
- **test_get_npc_room_id_prefers_current_room()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_should_include_npc_dead()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_should_include_npc_matching_room()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_scan_active_npcs_for_room()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_query_npcs_for_room_uses_lifecycle_manager()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_query_npcs_fallback_to_room()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_process_npcs_for_occupants()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_filter_fallback_npcs_dead()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_get_npc_lifecycle_manager_unavailable()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_get_npc_lifecycle_manager_no_active_npcs()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_query_npcs_handles_exception()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **NPC occupant processing utilities.  This module handles querying and processing** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Processes NPC occupants for rooms.** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Initialize NPC occupant processor.          Args:             connection_manager** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Room ID normalization and comparison utilities.  This module provides utilities** (1 connections) — `server/realtime/room_id_utils.py`
- **Utilities for room ID normalization and comparison.** (1 connections) — `server/realtime/room_id_utils.py`
- *... and 3 more nodes in this community*

## Relationships

- [message realtime messaging](message_realtime_messaging.md) (12 shared connections)
- [time service rationale](time_service_rationale.md) (11 shared connections)
- [player occupant processor](player_occupant_processor.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (2 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (2 shared connections)
- [logging processors structured](logging_processors_structured.md) (2 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)
- [magic healing game](magic_healing_game.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/room_id_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_npc_occupant_processor.py`

## Audit Trail

- EXTRACTED: 140 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*