# event bus events

> 68 nodes

## Key Concepts

- **NPCOccupantProcessor** (31 connections) — `server/realtime/npc_occupant_processor.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **RoomIDUtils** (22 connections) — `server/realtime/room_id_utils.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **room_occupant_manager.py** (19 connections) — `server/realtime/room_occupant_manager.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **test_npc_occupant_processor.py** (17 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **Any** (11 connections)
- **npc_occupant_processor.py** (9 connections) — `server/realtime/npc_occupant_processor.py`
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **.query_npcs_for_room()** (6 connections) — `server/realtime/npc_occupant_processor.py`
- **room_id_utils.py** (6 connections) — `server/realtime/room_id_utils.py`
- **.__init__()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._validate_npc_room_tracking()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._should_include_npc_in_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._scan_active_npcs_for_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_lifecycle_manager_for_filtering()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._filter_fallback_npcs()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_fallback_npcs()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_npc_room_id()** (4 connections) — `server/realtime/npc_occupant_processor.py`
- **._filter_single_fallback_npc()** (4 connections) — `server/realtime/npc_occupant_processor.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/room_occupant_manager.py`
- **.process_npcs_for_occupants()** (3 connections) — `server/realtime/npc_occupant_processor.py`
- **.__init__()** (3 connections) — `server/realtime/room_id_utils.py`
- *... and 43 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (12 shared connections)
- [time service rationale](time_service_rationale.md) (11 shared connections)
- [NPC Combat](NPC_Combat.md) (10 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (8 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (5 shared connections)
- [player_event_handler_utils](player_event_handler_utils.md) (4 shared connections)
- [combat services turn](combat_services_turn.md) (4 shared connections)
- [player occupant processor](player_occupant_processor.md) (4 shared connections)
- [logging setup structured](logging_setup_structured.md) (3 shared connections)
- [schedule services service](schedule_services_service.md) (3 shared connections)
- [container sql injection](container_sql_injection.md) (3 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (2 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/room_id_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_npc_occupant_processor.py`

## Audit Trail

- EXTRACTED: 303 (96%)
- INFERRED: 12 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*