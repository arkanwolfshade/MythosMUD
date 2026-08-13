# CombatService

> 752 nodes

## Key Concepts

- **CombatService** (181 connections) — `server/services/combat_service.py`
- **CombatParticipant** (167 connections) — `server/models/combat.py`
- **CombatInstance** (155 connections) — `server/models/combat.py`
- **combat_service.py** (100 connections) — `server/services/combat_service.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **models/combat.py** (50 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatParticipantType** (35 connections) — `server/models/combat.py`
- **combat_service_npc.py** (30 connections) — `server/services/combat_service_npc.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **combat_service_attack.py** (26 connections) — `server/services/combat_service_attack.py`
- **combat_flee_handler.py** (23 connections) — `server/services/combat_flee_handler.py`
- **CombatAction** (21 connections) — `server/models/combat.py`
- **CombatResult** (20 connections) — `server/models/combat.py`
- **UUID** (20 connections)
- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **CombatDeathHandler** (18 connections) — `server/services/combat_death_handler.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_combat_service.py** (18 connections) — `server/tests/unit/services/test_combat_service.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **test_combat_flee_handler.py** (17 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- *... and 727 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (59 shared connections)
- [TargetMatch](TargetMatch.md) (44 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (37 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (27 shared connections)
- [get_logger](get_logger.md) (25 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (23 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (19 shared connections)
- [PlayerService](PlayerService.md) (18 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (17 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (16 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (16 shared connections)
- [get_config](get_config.md) (14 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/game/magic/spell_effects_internal.py`
- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/services/lucidity_command_disruption.py`

## Audit Trail

- EXTRACTED: 1787 (96%)
- INFERRED: 72 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*