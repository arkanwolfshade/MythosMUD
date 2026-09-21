# get_config

> 246 nodes

## Key Concepts

- **get_config()** (113 connections) — `server/config/__init__.py`
- **models/combat.py** (61 connections) — `server/models/combat.py`
- **CombatParticipantType** (47 connections) — `server/models/combat.py`
- **combat_turn_participant_actions.py** (47 connections) — `server/services/combat_turn_participant_actions.py`
- **test_aggro_threat.py** (33 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **aggro_threat.py** (30 connections) — `server/services/aggro_threat.py`
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **_make_combat()** (24 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **add_damage_threat()** (22 connections) — `server/services/aggro_threat.py`
- **combat_attack_handler.py** (22 connections) — `server/services/combat_attack_handler.py`
- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **_make_participant()** (17 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **add_heal_threat()** (15 connections) — `server/services/aggro_threat.py`
- **CombatStatus** (14 connections) — `server/models/combat.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- **apply_taunt()** (12 connections) — `server/services/aggro_threat.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_player_attack_damage()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- *... and 221 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (61 shared connections)
- [CombatInstance](CombatInstance.md) (41 shared connections)
- [combat_service.py](combat_service.py.md) (25 shared connections)
- [get_logger](get_logger.md) (24 shared connections)
- [CombatService](CombatService.md) (21 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (20 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (19 shared connections)
- [AppConfig](AppConfig.md) (19 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (15 shared connections)
- [TargetMatch](TargetMatch.md) (9 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (8 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (8 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/game/magic/spell_targeting.py`
- `server/game/player_service.py`
- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/services/test_aggro_threat.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_types.py`
- `server/tests/unit/services/test_damage_grace_period.py`
- `server/tests/unit/test_config_smoke.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 858 (98%)
- INFERRED: 22 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*