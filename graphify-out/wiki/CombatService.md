# CombatService

> 298 nodes

## Key Concepts

- **CombatService** (173 connections) — `server/services/combat_service.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **combat_service.py** (104 connections) — `server/services/combat_service.py`
- **models/combat.py** (58 connections) — `server/models/combat.py`
- **npc_combat_integration_service.py** (53 connections) — `server/services/npc_combat_integration_service.py`
- **CombatParticipantType** (44 connections) — `server/models/combat.py`
- **CombatParticipantData** (37 connections) — `server/services/combat_types.py`
- **NPCCombatDataProvider** (36 connections) — `server/services/npc_combat_data_provider.py`
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **CombatResult** (20 connections) — `server/models/combat.py`
- **UUID** (20 connections)
- **npc_combat_integration_validation_mixin.py** (20 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **npc_combat_integration_combat_mixin.py** (18 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **test_npc_combat_data_provider.py** (18 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **.connection_manager()** (16 connections) — `server/services/combat_messaging/base.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **get_current_tick()** (14 connections) — `server/app/game_tick_counter.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- *... and 273 more nodes in this community*

## Relationships

- [NATSError](NATSError.md) (56 shared connections)
- [get_logger](get_logger.md) (41 shared connections)
- [CombatParticipant](CombatParticipant.md) (40 shared connections)
- [CombatInstance](CombatInstance.md) (39 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (37 shared connections)
- [combat_service_npc.py](combat_service_npc.py.md) (27 shared connections)
- [TargetMatch](TargetMatch.md) (23 shared connections)
- [server/config/__init__.py](server-config-__init__.py.md) (23 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (17 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (14 shared connections)
- [_NPCCombatIntegrationValidationDeps](_NPCCombatIntegrationValidationDeps.md) (14 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (13 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/config/__init__.py`
- `server/game/magic/spell_targeting.py`
- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_initialization.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging_integration.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_uuid_mapping.py`
- `server/tests/unit/services/test_combat_initialization.py`

## Audit Trail

- EXTRACTED: 1017 (89%)
- INFERRED: 126 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*