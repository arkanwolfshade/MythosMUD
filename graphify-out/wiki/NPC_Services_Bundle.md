# NPC Services Bundle

> 263 nodes · cohesion 0.02

## Key Concepts

- **NPCPopulationController** (93 connections) — `server/npc/population_control.py`
- **NPCLeftRoom** (71 connections) — `server/events/event_types.py`
- **NPCCombatIntegration** (68 connections) — `server/npc/combat_integration.py`
- **PopulationStats** (64 connections) — `server/npc/population_stats.py`
- **PlayerLeftRoom** (61 connections) — `server/events/event_types.py`
- **NPCSpawningService** (53 connections) — `server/npc/spawning_service.py`
- **SimpleNPCDefinition** (36 connections) — `server/npc/spawning_models.py`
- **NPCSpawnResult** (32 connections) — `server/npc/spawning_models.py`
- **NPCSpawnRequest** (31 connections) — `server/npc/spawning_models.py`
- **ZoneConfiguration** (28 connections) — `server/npc/population_control.py`
- **spawning_service.py** (25 connections) — `server/npc/spawning_service.py`
- **test_population_stats.py** (21 connections) — `server/tests/unit/npc/test_population_stats.py`
- **combat_integration.py** (20 connections) — `server/npc/combat_integration.py`
- **NPCDefinition** (19 connections) — `server/npc/spawning_service.py`
- **NPCSpawnRequest** (18 connections) — `server/npc/spawning_service.py`
- **NPCSpawnStatistics** (17 connections) — `server/npc/spawning_service.py`
- **NPCSpawnResult** (17 connections) — `server/npc/spawning_service.py`
- **ZoneConfiguration** (17 connections) — `server/npc/spawning_service.py`
- **spawning_instance_factory.py** (16 connections) — `server/npc/spawning_instance_factory.py`
- **PopulationStats** (15 connections) — `server/npc/spawning_service.py`
- **spawning_request_execution.py** (14 connections) — `server/npc/spawning_request_execution.py`
- **EventBus** (14 connections) — `server/npc/spawning_service.py`
- **NPCBase** (14 connections) — `server/npc/spawning_service.py`
- **NPCCombatIntegration** (14 connections) — `server/npc/spawning_service.py`
- **NPCCombatIntegrationService** (14 connections) — `server/npc/spawning_service.py`
- *... and 238 more nodes in this community*

## Relationships

- [[Distributed Event Bus]] (135 shared connections)
- [[NPC Death Lifecycle]] (56 shared connections)
- [[Combat Command Handler]] (26 shared connections)
- [[NPC Admin API]] (18 shared connections)
- [[NPC Population Control]] (14 shared connections)
- [[Lifespan Startup Hooks]] (11 shared connections)
- [[NPC Occupant Verification]] (11 shared connections)
- [[Aggressive Mob NPC]] (10 shared connections)
- [[Room Occupancy Class]] (9 shared connections)
- [[Game Mechanics Service]] (8 shared connections)
- [[NPC Utility Functions]] (8 shared connections)
- [[Application DI Bundles]] (7 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/bundles/npc.py`
- `server/events/event_types.py`
- `server/models/room.py`
- `server/models/spell_db.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/npc/test_population_stats.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 990 (60%)
- INFERRED: 652 (40%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
