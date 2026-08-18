# NPCDefinition

> 601 nodes

## Key Concepts

- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **event_types.py** (87 connections) — `server/events/event_types.py`
- **NPCBase** (79 connections) — `server/npc/npc_base.py`
- **PlayerEnteredRoom** (76 connections) — `server/events/event_types.py`
- **NPCLifecycleManager** (70 connections) — `server/npc/lifecycle_manager.py`
- **test_population_control.py** (66 connections) — `server/tests/unit/npc/test_population_control.py`
- **NPCPopulationController** (60 connections) — `server/npc/population_control.py`
- **test_npc_instance_service.py** (54 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **NPCEnteredRoom** (46 connections) — `server/events/event_types.py`
- **npc_base.py** (45 connections) — `server/npc/npc_base.py`
- **NPCLeftRoom** (43 connections) — `server/events/event_types.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **PopulationStats** (40 connections) — `server/npc/population_stats.py`
- **models/npc.py** (39 connections) — `server/models/npc.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **event_bus.py** (35 connections) — `server/events/event_bus.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **event_reaction_system.py** (30 connections) — `server/npc/event_reaction_system.py`
- **combat_integration.py** (27 connections) — `server/npc/combat_integration.py`
- **server/events/__init__.py** (25 connections) — `server/events/__init__.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **time_event_consumer.py** (25 connections) — `server/time/time_event_consumer.py`
- **NPCEventReactionSystem** (24 connections) — `server/npc/event_reaction_system.py`
- **NPCInstanceService** (23 connections) — `server/services/npc_instance_service.py`
- *... and 576 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (95 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (62 shared connections)
- [EventBus](EventBus.md) (57 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (49 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (33 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (30 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (30 shared connections)
- [test_event_handler.py](test_event_handler.py.md) (28 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (25 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (24 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (21 shared connections)
- [npc_service/__init__.py](npc_service-__init__.py.md) (18 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/bundles/npc.py`
- `server/events/__init__.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/npc/npc_combat_schedule.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/population_control.py`

## Audit Trail

- EXTRACTED: 1681 (93%)
- INFERRED: 132 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*