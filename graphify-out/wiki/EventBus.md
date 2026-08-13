# EventBus

> 1033 nodes

## Key Concepts

- **EventBus** (127 connections) — `server/events/event_bus.py`
- **NPCDefinition** (108 connections) — `server/models/npc.py`
- **NPCBase** (81 connections) — `server/npc/npc_base.py`
- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **NPCLifecycleManager** (73 connections) — `server/npc/lifecycle_manager.py`
- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **NPCCombatIntegration** (63 connections) — `server/npc/combat_integration.py`
- **NPCPopulationController** (62 connections) — `server/npc/population_control.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **ZoneConfiguration** (52 connections) — `server/npc/zone_configuration.py`
- **NPCSpawningService** (48 connections) — `server/npc/spawning_service.py`
- **lifecycle_manager.py** (48 connections) — `server/npc/lifecycle_manager.py`
- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **PopulationStats** (42 connections) — `server/npc/population_stats.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **npc_base.py** (41 connections) — `server/npc/npc_base.py`
- **models/npc.py** (37 connections) — `server/models/npc.py`
- **spawning_service.py** (37 connections) — `server/npc/spawning_service.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **AggressiveMobNPC** (32 connections) — `server/npc/aggressive_mob_npc.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **test_npc_utils.py** (30 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **PassiveMobNPC** (29 connections) — `server/npc/passive_mob_npc.py`
- **event_bus.py** (29 connections) — `server/events/event_bus.py`
- **NPCThreadManager** (25 connections) — `server/npc/threading.py`
- *... and 1008 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (102 shared connections)
- [get_logger](get_logger.md) (92 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (41 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (34 shared connections)
- [Any](Any.md) (33 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (29 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (19 shared connections)
- [test_npc_combat_integration_class.py](test_npc_combat_integration_class.py.md) (19 shared connections)
- [_JSONDict](_JSONDict.md) (18 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (18 shared connections)
- [AliasStorage](AliasStorage.md) (17 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (16 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/events/event_bus.py`
- `server/game/follow_service.py`
- `server/game/party_service.py`
- `server/models/npc.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behavior_engine.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/idle_movement.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/movement_integration.py`
- `server/npc/npc_base.py`
- `server/npc/npc_utils.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`

## Audit Trail

- EXTRACTED: 2307 (94%)
- INFERRED: 147 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*