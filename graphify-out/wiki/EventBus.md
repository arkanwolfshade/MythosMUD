# EventBus

> 300 nodes

## Key Concepts

- **EventBus** (225 connections) — `server/events/event_bus.py`
- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **event_types.py** (102 connections) — `server/events/event_types.py`
- **NPCBase** (79 connections) — `server/npc/npc_base.py`
- **NPCSpawningService** (69 connections) — `server/npc/spawning_service.py`
- **NPCEnteredRoom** (53 connections) — `server/events/event_types.py`
- **NPCEventReactionSystem** (47 connections) — `server/npc/event_reaction_system.py`
- **test_spawning_modules.py** (47 connections) — `server/tests/unit/npc/test_spawning_modules.py`
- **NPCLeftRoom** (46 connections) — `server/events/event_types.py`
- **npc_base.py** (46 connections) — `server/npc/npc_base.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **event_bus.py** (40 connections) — `server/events/event_bus.py`
- **spawning_service.py** (40 connections) — `server/npc/spawning_service.py`
- **models/npc.py** (39 connections) — `server/models/npc.py`
- **event_reaction_system.py** (36 connections) — `server/npc/event_reaction_system.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **combat_integration.py** (27 connections) — `server/npc/combat_integration.py`
- **spawning_instance_factory.py** (27 connections) — `server/npc/spawning_instance_factory.py`
- **server/events/__init__.py** (26 connections) — `server/events/__init__.py`
- **spawning_request_execution.py** (21 connections) — `server/npc/spawning_request_execution.py`
- **bundles/npc.py** (20 connections) — `server/container/bundles/npc.py`
- **aggressive_mob_npc.py** (20 connections) — `server/npc/aggressive_mob_npc.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **SimpleNPCDefinition** (19 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (19 connections) — `server/npc/spawning_instance_factory.py`
- *... and 275 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (105 shared connections)
- [BaseEvent](BaseEvent.md) (75 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (75 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (68 shared connections)
- [NPCPopulationController](NPCPopulationController.md) (39 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (30 shared connections)
- [test_event_bus_lifecycle.py](test_event_bus_lifecycle.py.md) (22 shared connections)
- [event_handler.py](event_handler.py.md) (18 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (18 shared connections)
- [FollowService](FollowService.md) (17 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (17 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (16 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/models/npc.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behavior_engine.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/communication_integration.py`
- `server/npc/corruption_reactions.py`
- `server/npc/event_reaction_system.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`

## Audit Trail

- EXTRACTED: 1290 (87%)
- INFERRED: 186 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*