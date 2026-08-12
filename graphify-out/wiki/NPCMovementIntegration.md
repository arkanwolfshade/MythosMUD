# NPCMovementIntegration

> 61 nodes

## Key Concepts

- **NPCMovementIntegration** (24 connections) — `server/npc/movement_integration.py`
- **quest_events.py** (14 connections) — `server/game/quest/quest_events.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **subscribe_quest_events()** (10 connections) — `server/game/quest/quest_events.py`
- **.move_npc_to_room()** (7 connections) — `server/npc/movement_integration.py`
- **_make_on_player_entered()** (5 connections) — `server/game/quest/quest_events.py`
- **.__init__()** (5 connections) — `server/npc/idle_movement.py`
- **.__init__()** (5 connections) — `server/npc/movement_integration.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **._move_with_integration()** (5 connections) — `server/npc/npc_base.py`
- **_make_on_npc_died()** (4 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_left()** (4 connections) — `server/game/quest/quest_events.py`
- **._get_destination_subzone()** (4 connections) — `server/npc/movement_integration.py`
- **._get_room_objects()** (4 connections) — `server/npc/movement_integration.py`
- **._update_npc_instance_room_tracking()** (4 connections) — `server/npc/movement_integration.py`
- **._update_room_occupancy()** (4 connections) — `server/npc/movement_integration.py`
- **Any** (4 connections)
- **_parse_player_id()** (3 connections) — `server/game/quest/quest_events.py`
- **._is_npc_in_combat()** (3 connections) — `server/npc/movement_integration.py`
- **._validate_room_ids()** (3 connections) — `server/npc/movement_integration.py`
- **.validate_subzone_boundary()** (3 connections) — `server/npc/movement_integration.py`
- **._is_npc_in_combat()** (3 connections) — `server/npc/npc_base.py`
- **._move_simple()** (3 connections) — `server/npc/npc_base.py`
- **_entity_id_for_quest_offer()** (2 connections) — `server/game/quest/quest_events.py`
- *... and 36 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (9 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (7 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [threading.py](threading.py.md) (1 shared connections)
- [quest_commands.py](quest_commands.py.md) (1 shared connections)
- [test_room_utils.py](test_room_utils.py.md) (1 shared connections)
- [MovementService](MovementService.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/game/quest/quest_events.py`
- `server/npc/idle_movement.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 101 (89%)
- INFERRED: 13 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*