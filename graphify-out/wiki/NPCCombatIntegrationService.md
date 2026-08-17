# NPCCombatIntegrationService

> 129 nodes

## Key Concepts

- **NPCCombatIntegrationService** (86 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service.py** (47 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **asyncio** (25 connections)
- **SimpleNPCDefinition** (16 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (16 connections) — `server/npc/spawning_instance_factory.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_build_aggressive()** (8 connections) — `server/npc/spawning_instance_factory.py`
- **integration_service()** (7 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **_build_passive()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_build_shopkeeper()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **_StubConfigRoot** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **_coerce_simple_definition()** (5 connections) — `server/npc/spawning_instance_factory.py`
- **._generate_npc_id()** (5 connections) — `server/npc/spawning_service.py`
- **.handle_npc_attack_on_player()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **._init_persistence_and_event_bus()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **test_validate_combat_location_limbo_cross_room_uses_debug()** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **.is_alive()** (4 connections) — `server/models/combat.py`
- **._complete_player_attack_on_npc_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_player_attack_on_npc()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **test_end_combat_if_participant_in_combat_ends_combat()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- *... and 104 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (21 shared connections)
- [EventBus](EventBus.md) (21 shared connections)
- [test_npc_combat_integration_service_player_attacks.py](test_npc_combat_integration_service_player_attacks.py.md) (11 shared connections)
- [NPCDefinition](NPCDefinition.md) (8 shared connections)
- [NPCBase](NPCBase.md) (7 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_npc_combat_handlers.py](test_npc_combat_handlers.py.md) (4 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [NPCCombatLifecycle](NPCCombatLifecycle.md) (3 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_service.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/npc/test_spawning_modules.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 251 (76%)
- INFERRED: 78 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*