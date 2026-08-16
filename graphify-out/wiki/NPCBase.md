# NPCBase

> 201 nodes

## Key Concepts

- **NPCBase** (79 connections) — `server/npc/npc_base.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnRequest** (19 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (18 connections) — `server/npc/spawning_request_execution.py`
- **register_default_reactions_for_npc()** (17 connections) — `server/npc/npc_default_reactions.py`
- **SimpleNPCDefinition** (16 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (16 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnResult** (15 connections) — `server/npc/spawning_models.py`
- **npc_config_parsing.py** (14 connections) — `server/npc/npc_config_parsing.py`
- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **test_npc_default_reactions.py** (9 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **CommunicationIntegrationProtocol** (8 connections) — `server/npc/npc_protocols.py`
- **schedule_end_combat_if_npc_died_best_effort()** (8 connections) — `server/npc/npc_combat_schedule.py`
- **_build_aggressive()** (8 connections) — `server/npc/spawning_instance_factory.py`
- **_spawn_success()** (8 connections) — `server/npc/spawning_request_execution.py`
- **get_combat_stats_dict()** (7 connections) — `server/npc/npc_config_parsing.py`
- **to_int_or_default()** (7 connections) — `server/npc/npc_config_parsing.py`
- **register_npc_display_name()** (7 connections) — `server/npc/npc_display_names.py`
- **CombatIntegrationProtocol** (6 connections) — `server/npc/npc_protocols.py`
- **_PopulationLifecycleManager** (6 connections) — `server/npc/population_control.py`
- **_build_passive()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_build_shopkeeper()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_room_from_persistence()** (6 connections) — `server/npc/spawning_request_execution.py`
- *... and 176 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (99 shared connections)
- [NPCDefinition](NPCDefinition.md) (12 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (6 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (5 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [NPCDied](NPCDied.md) (3 shared connections)
- [BehaviorEngine](BehaviorEngine.md) (3 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [AggressiveMobNPC](AggressiveMobNPC.md) (2 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (2 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (2 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_combat_schedule.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/npc_default_reactions.py`
- `server/npc/npc_display_names.py`
- `server/npc/npc_protocols.py`
- `server/npc/population_control.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_npc_combat_schedule.py`
- `server/tests/unit/npc/test_npc_default_reactions.py`
- `server/tests/unit/npc/test_spawning_modules.py`

## Audit Trail

- EXTRACTED: 379 (87%)
- INFERRED: 56 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*