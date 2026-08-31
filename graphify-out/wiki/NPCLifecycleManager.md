# NPCLifecycleManager

> 520 nodes

## Key Concepts

- **NPCLifecycleManager** (70 connections) — `server/npc/lifecycle_manager.py`
- **test_population_control.py** (66 connections) — `server/tests/unit/npc/test_population_control.py`
- **NPCPopulationController** (60 connections) — `server/npc/population_control.py`
- **test_npc_instance_service.py** (54 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **PopulationStats** (40 connections) — `server/npc/population_stats.py`
- **event_bus.py** (40 connections) — `server/events/event_bus.py`
- **test_npc_utils.py** (34 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **NPCDied** (29 connections) — `server/events/event_types.py`
- **combat_integration.py** (27 connections) — `server/npc/combat_integration.py`
- **NPCLifecycleState** (24 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **NPCInstanceService** (23 connections) — `server/services/npc_instance_service.py`
- **test_population_stats.py** (23 connections) — `server/tests/unit/npc/test_population_stats.py`
- **asyncio** (23 connections)
- **despawn_npc_impl()** (20 connections) — `server/npc/lifecycle_despawn.py`
- **server/npc/__init__.py** (19 connections) — `server/npc/__init__.py`
- **test_lifecycle_despawn.py** (19 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **EventBusProcessingMixin** (18 connections) — `server/events/event_bus_processing.py`
- **get_zone_key_from_room_id()** (17 connections) — `server/npc/npc_utils.py`
- **NPCLifecycleRecord** (16 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_despawn.py** (16 connections) — `server/npc/lifecycle_despawn.py`
- **lifecycle_types.py** (16 connections) — `server/npc/lifecycle_types.py`
- *... and 495 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (64 shared connections)
- [EventBus](EventBus.md) (34 shared connections)
- [get_logger](get_logger.md) (26 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (26 shared connections)
- [NPCDefinition](NPCDefinition.md) (23 shared connections)
- [NPCBase](NPCBase.md) (20 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (13 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (11 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (10 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (9 shared connections)
- [._handle_event_async](_handle_event_async.md) (8 shared connections)
- [test_lifecycle_manager.py](test_lifecycle_manager.py.md) (8 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/events/event_bus.py`
- `server/events/event_bus_base.py`
- `server/events/event_bus_processing.py`
- `server/events/event_types.py`
- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/__init__.py`
- `server/npc/combat_integration.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/spawning_service.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/npc/test_lifecycle_death.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`

## Audit Trail

- EXTRACTED: 1120 (93%)
- INFERRED: 81 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*