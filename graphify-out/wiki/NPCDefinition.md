# NPCDefinition

> 485 nodes

## Key Concepts

- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **event_types.py** (87 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (76 connections) — `server/events/event_types.py`
- **test_population_control.py** (66 connections) — `server/tests/unit/npc/test_population_control.py`
- **NPCPopulationController** (60 connections) — `server/npc/population_control.py`
- **ZoneConfiguration** (54 connections) — `server/npc/zone_configuration.py`
- **PlayerLeftRoom** (49 connections) — `server/events/event_types.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **NPCEnteredRoom** (46 connections) — `server/events/event_types.py`
- **npc_base.py** (45 connections) — `server/npc/npc_base.py`
- **NPCLeftRoom** (43 connections) — `server/events/event_types.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **test_event_handler.py** (42 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **PopulationStats** (40 connections) — `server/npc/population_stats.py`
- **models/npc.py** (39 connections) — `server/models/npc.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **event_bus.py** (32 connections) — `server/events/event_bus.py`
- **models/room.py** (32 connections) — `server/models/room.py`
- **event_reaction_system.py** (30 connections) — `server/npc/event_reaction_system.py`
- **server/events/__init__.py** (25 connections) — `server/events/__init__.py`
- **test_spawn_validator.py** (25 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **NPCEventReactionSystem** (24 connections) — `server/npc/event_reaction_system.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- *... and 460 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (131 shared connections)
- [get_logger](get_logger.md) (90 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (66 shared connections)
- [NPCDied](NPCDied.md) (41 shared connections)
- [BaseEvent](BaseEvent.md) (32 shared connections)
- [test_npc_models.py](test_npc_models.py.md) (24 shared connections)
- [test_population_stats.py](test_population_stats.py.md) (21 shared connections)
- [.__post_init__](__post_init__.md) (18 shared connections)
- [_JSONDict](_JSONDict.md) (17 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (16 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (16 shared connections)
- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (14 shared connections)

## Source Files

- `server/events/__init__.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/game/instance_manager.py`
- `server/game/quest/quest_events.py`
- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_service.py`

## Audit Trail

- EXTRACTED: 1394 (87%)
- INFERRED: 200 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*