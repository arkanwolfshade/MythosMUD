# CombatParticipant

> 364 nodes

## Key Concepts

- **CombatParticipant** (167 connections) — `server/models/combat.py`
- **CombatInstance** (155 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **combat_service_attack.py** (26 connections) — `server/services/combat_service_attack.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **_make_combat()** (23 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **CombatResult** (20 connections) — `server/models/combat.py`
- **add_damage_threat()** (20 connections) — `server/services/aggro_threat.py`
- **UUID** (20 connections)
- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **CombatDeathHandler** (18 connections) — `server/services/combat_death_handler.py`
- **asyncio** (17 connections)
- **get_current_tick()** (15 connections) — `server/app/game_tick_processing.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- **_make_participant()** (13 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **apply_taunt()** (12 connections) — `server/services/aggro_threat.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **._execute_spell_action()** (11 connections) — `server/services/combat_turn_processor.py`
- *... and 339 more nodes in this community*

## Relationships

- [combat_service.py](combat_service.py.md) (134 shared connections)
- [CombatService](CombatService.md) (73 shared connections)
- [get_logger](get_logger.md) (21 shared connections)
- [test_combat_flee_handler.py](test_combat_flee_handler.py.md) (13 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (13 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (8 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (7 shared connections)
- [_NPCCombatIntegrationDeps](_NPCCombatIntegrationDeps.md) (7 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (6 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (6 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (5 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (4 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_aggro_threat.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 1798 (99%)
- INFERRED: 16 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*