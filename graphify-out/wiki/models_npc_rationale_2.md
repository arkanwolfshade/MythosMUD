# models npc rationale

> 501 nodes

## Key Concepts

- **NPCDefinition** (121 connections) — `server/models/npc.py`
- **time.py** (96 connections) — `server/container/bundles/time.py`
- **NPCBase** (83 connections) — `server/npc/npc_base.py`
- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **NPCSpawnRule** (55 connections) — `server/models/npc.py`
- **npc_base.py** (44 connections) — `server/npc/npc_base.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **PopulationStats** (42 connections) — `server/npc/population_stats.py`
- **npc.py** (38 connections) — `server/models/npc.py`
- **spawning_service.py** (38 connections) — `server/npc/spawning_service.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **NPCEventReactionSystem** (27 connections) — `server/npc/event_reaction_system.py`
- **combat_integration.py** (26 connections) — `server/npc/combat_integration.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_population_stats.py** (23 connections) — `server/tests/unit/npc/test_population_stats.py`
- **should_spawn_npc()** (22 connections) — `server/npc/spawn_validator.py`
- **ShopkeeperNPC** (20 connections) — `server/npc/shopkeeper_npc.py`
- **spawning_request_execution.py** (20 connections) — `server/npc/spawning_request_execution.py`
- **lifecycle_periodic.py** (19 connections) — `server/npc/lifecycle_periodic.py`
- **passive_mob_npc.py** (19 connections) — `server/npc/passive_mob_npc.py`
- **aggressive_mob_npc.py** (18 connections) — `server/npc/aggressive_mob_npc.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **SimpleNPCDefinition** (17 connections) — `server/npc/spawning_models.py`
- **NPCSpawnRequest** (17 connections) — `server/npc/spawning_models.py`
- *... and 476 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (141 shared connections)
- [Loot Generation](Loot_Generation.md) (50 shared connections)
- [command parser rationale](command_parser_rationale.md) (37 shared connections)
- [spell game magic](spell_game_magic.md) (23 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (19 shared connections)
- [npc lifecycle config](npc_lifecycle_config.md) (14 shared connections)
- [channel broadcasting strategies](channel_broadcasting_strategies.md) (13 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (12 shared connections)
- [combat services rationale](combat_services_rationale.md) (11 shared connections)
- [command input commands](command_input_commands.md) (11 shared connections)
- [lucidity event services](lucidity_event_services.md) (9 shared connections)
- [room conftest toolkit](room_conftest_toolkit.md) (9 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/models/npc.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/event_reaction_system.py`
- `server/npc/lifecycle_periodic.py`
- `server/npc/npc_base.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`

## Audit Trail

- EXTRACTED: 1942 (94%)
- INFERRED: 124 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*