# ApplicationContainer

> 1107 nodes

## Key Concepts

- **ApplicationContainer** (145 connections) — `server/container/main.py`
- **EventBus** (127 connections) — `server/events/event_bus.py`
- **NPCDefinition** (108 connections) — `server/models/npc.py`
- **time.py** (89 connections) — `server/container/bundles/time.py`
- **NPCBase** (81 connections) — `server/npc/npc_base.py`
- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **NPCLifecycleManager** (73 connections) — `server/npc/lifecycle_manager.py`
- **NPCCombatIntegration** (63 connections) — `server/npc/combat_integration.py`
- **NPCPopulationController** (62 connections) — `server/npc/population_control.py`
- **lifespan_startup.py** (60 connections) — `server/app/lifespan_startup.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCSpawningService** (48 connections) — `server/npc/spawning_service.py`
- **lifecycle_manager.py** (48 connections) — `server/npc/lifecycle_manager.py`
- **threading.py** (45 connections) — `server/npc/threading.py`
- **PopulationStats** (42 connections) — `server/npc/population_stats.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **npc_base.py** (41 connections) — `server/npc/npc_base.py`
- **NPCLeftRoom** (40 connections) — `server/events/event_types.py`
- **models/npc.py** (37 connections) — `server/models/npc.py`
- **spawning_service.py** (37 connections) — `server/npc/spawning_service.py`
- **.get_instance()** (34 connections) — `server/container/main.py`
- **container/main.py** (33 connections) — `server/container/main.py`
- **AggressiveMobNPC** (32 connections) — `server/npc/aggressive_mob_npc.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **test_npc_utils.py** (30 connections) — `server/tests/unit/npc/test_npc_utils.py`
- *... and 1082 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (200 shared connections)
- [event_types.py](event_types.py.md) (70 shared connections)
- [DatabaseError](DatabaseError.md) (55 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (53 shared connections)
- [PlayerService](PlayerService.md) (47 shared connections)
- [test_population_control.py](test_population_control.py.md) (42 shared connections)
- [Any](Any.md) (33 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (30 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (25 shared connections)
- [TaskRegistry](TaskRegistry.md) (24 shared connections)
- [test_npc_combat_integration_class.py](test_npc_combat_integration_class.py.md) (20 shared connections)
- [lifespan.py](lifespan.py.md) (19 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/caching/lru_cache.py`
- `server/commands/combat_handler.py`
- `server/commands/shutdown_process_termination.py`
- `server/commands/time_commands.py`
- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/models/npc.py`

## Audit Trail

- EXTRACTED: 2916 (93%)
- INFERRED: 211 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*