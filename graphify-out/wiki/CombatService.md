# CombatService

> 438 nodes

## Key Concepts

- **CombatService** (212 connections) — `server/services/combat_service.py`
- **get_config()** (126 connections) — `server/config/__init__.py`
- **combat_service.py** (116 connections) — `server/services/combat_service.py`
- **models/combat.py** (83 connections) — `server/models/combat.py`
- **CombatParticipantType** (82 connections) — `server/models/combat.py`
- **npc_combat_integration_service.py** (60 connections) — `server/services/npc_combat_integration_service.py`
- **combat_turn_participant_actions.py** (49 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatParticipantData** (46 connections) — `server/services/combat_types.py`
- **combat_service_start.py** (34 connections) — `server/services/combat_service_start.py`
- **combat_service_npc.py** (32 connections) — `server/services/combat_service_npc.py`
- **PlayerDiedEvent** (31 connections) — `server/events/event_types.py`
- **test_idle_movement_combat_gate.py** (31 connections) — `server/tests/unit/npc/test_idle_movement_combat_gate.py`
- **combat_death_handler.py** (30 connections) — `server/services/combat_death_handler.py`
- **test_combat_service_npc_helpers.py** (30 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **combat_taunt_action.py** (27 connections) — `server/services/combat_taunt_action.py`
- **CombatDeathHandler** (26 connections) — `server/services/combat_death_handler.py`
- **combat_turn_processor.py** (26 connections) — `server/services/combat_turn_processor.py`
- **npc_combat_data_provider.py** (24 connections) — `server/services/npc_combat_data_provider.py`
- **UUID** (23 connections)
- **combat_attack_handler.py** (22 connections) — `server/services/combat_attack_handler.py`
- **npc_combat_integration_validation_mixin.py** (22 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **npc_combat_integration_combat_mixin.py** (21 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.create_combat_instance()** (19 connections) — `server/services/combat_initialization.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **TestCombatInitializer** (17 connections) — `server/tests/unit/services/test_combat_initialization.py`
- *... and 413 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (83 shared connections)
- [CombatInstance](CombatInstance.md) (74 shared connections)
- [CombatParticipant](CombatParticipant.md) (66 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (59 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (59 shared connections)
- [SuccessLevel](SuccessLevel.md) (27 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (26 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (26 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (25 shared connections)
- [TargetMatch](TargetMatch.md) (22 shared connections)
- [test_n_player_combat.py](test_n_player_combat.py.md) (21 shared connections)
- [NpcDisposition](NpcDisposition.md) (20 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/container/bundles/combat.py`
- `server/events/event_types.py`
- `server/game/magic/spell_effects_threat.py`
- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_initialization.py`
- `server/services/combat_messaging_integration.py`
- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/services/combat_taunt_action.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/services/corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 1522 (90%)
- INFERRED: 163 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*