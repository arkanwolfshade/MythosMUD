# Realtime Subscribers

> 357 nodes

## Key Concepts

- **EventBus** (135 connections) — `server/events/event_bus.py`
- **NPCDefinition** (119 connections) — `server/models/npc.py`
- **NPCLifecycleManager** (76 connections) — `server/npc/lifecycle_manager.py`
- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **NPCCombatIntegration** (63 connections) — `server/npc/combat_integration.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCSpawningService** (50 connections) — `server/npc/spawning_service.py`
- **lifecycle_manager.py** (48 connections) — `server/npc/lifecycle_manager.py`
- **npc_base.py** (44 connections) — `server/npc/npc_base.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **npc.py** (37 connections) — `server/models/npc.py`
- **spawning_service.py** (37 connections) — `server/npc/spawning_service.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **event_bus.py** (31 connections) — `server/events/event_bus.py`
- **NPCDied** (25 connections) — `server/events/event_types.py`
- **combat_integration.py** (25 connections) — `server/npc/combat_integration.py`
- **spawning_instance_factory.py** (24 connections) — `server/npc/spawning_instance_factory.py`
- **NPCInstanceService** (24 connections) — `server/services/npc_instance_service.py`
- **lifecycle_death.py** (23 connections) — `server/npc/lifecycle_death.py`
- **spawning_request_execution.py** (19 connections) — `server/npc/spawning_request_execution.py`
- **aggressive_mob_npc.py** (18 connections) — `server/npc/aggressive_mob_npc.py`
- **_SpawnTrackedNPC** (17 connections) — `server/npc/lifecycle_manager.py`
- **NPCLifecycleRecord** (17 connections) — `server/npc/lifecycle_types.py`
- **_LifecycleManagerForDeath** (16 connections) — `server/npc/lifecycle_death.py`
- **_SpawningServiceProtocol** (16 connections) — `server/npc/lifecycle_manager.py`
- *... and 332 more nodes in this community*

## Relationships

- [item models rationale](item_models_rationale.md) (102 shared connections)
- [NPC Combat](NPC_Combat.md) (42 shared connections)
- [command inventory factories](command_inventory_factories.md) (40 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (38 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (35 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (30 shared connections)
- [realtime connection helpers](realtime_connection_helpers.md) (24 shared connections)
- [models npc rationale](models_npc_rationale.md) (22 shared connections)
- [message queue realtime](message_queue_realtime.md) (21 shared connections)
- [time service rationale](time_service_rationale.md) (20 shared connections)
- [Error Conversion](Error_Conversion.md) (19 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (19 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/bundles/npc.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/models/npc.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/combat_integration.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 1749 (89%)
- INFERRED: 213 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*