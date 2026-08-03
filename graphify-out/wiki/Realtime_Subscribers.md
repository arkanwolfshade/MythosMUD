# Realtime Subscribers

> 1045 nodes

## Key Concepts

- **NPCDefinition** (119 connections) — `server/models/npc.py`
- **NPCBase** (83 connections) — `server/npc/npc_base.py`
- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **NPCLifecycleManager** (76 connections) — `server/npc/lifecycle_manager.py`
- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **NPCCombatIntegration** (63 connections) — `server/npc/combat_integration.py`
- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **NPCSpawnRule** (55 connections) — `server/models/npc.py`
- **ZoneConfiguration** (53 connections) — `server/npc/zone_configuration.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCSpawningService** (50 connections) — `server/npc/spawning_service.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **PopulationStats** (42 connections) — `server/npc/population_stats.py`
- **npc.py** (37 connections) — `server/models/npc.py`
- **spawning_service.py** (37 connections) — `server/npc/spawning_service.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **AggressiveMobNPC** (32 connections) — `server/npc/aggressive_mob_npc.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **test_npc_utils.py** (30 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **combat_integration.py** (25 connections) — `server/npc/combat_integration.py`
- **spawning_instance_factory.py** (24 connections) — `server/npc/spawning_instance_factory.py`
- **NPCInstanceService** (24 connections) — `server/services/npc_instance_service.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_npc_combat_integration_class.py** (23 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- *... and 1020 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (241 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (30 shared connections)
- [models npc rationale](models_npc_rationale.md) (22 shared connections)
- [spawn npc services](spawn_npc_services.md) (22 shared connections)
- [Item Instances](Item_Instances.md) (20 shared connections)
- [admin auth service](admin_auth_service.md) (20 shared connections)
- [zone npc config](zone_npc_config.md) (19 shared connections)
- [NPC Combat](NPC_Combat.md) (14 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (13 shared connections)
- [attack combat commands](attack_combat_commands.md) (10 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (9 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (9 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/commands/combat_attack.py`
- `server/commands/npc_admin/definition.py`
- `server/container/bundles/npc.py`
- `server/events/event_types.py`
- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/npc_utils.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`

## Audit Trail

- EXTRACTED: 3804 (94%)
- INFERRED: 243 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*