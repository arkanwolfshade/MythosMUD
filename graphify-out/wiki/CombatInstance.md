# CombatInstance

> 425 nodes

## Key Concepts

- **CombatInstance** (176 connections) — `server/models/combat.py`
- **models/combat.py** (60 connections) — `server/models/combat.py`
- **combat_turn_participant_actions.py** (47 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatParticipantType** (45 connections) — `server/models/combat.py`
- **test_combat_attack_handler.py** (38 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **combat_taunt.py** (34 connections) — `server/commands/combat_taunt.py`
- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (31 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **test_damage_grace_period.py** (28 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **TauntCommandHandler** (27 connections) — `server/commands/combat_taunt.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **_make_combat()** (23 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_combat_taunt.py** (22 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **add_damage_threat()** (20 connections) — `server/services/aggro_threat.py`
- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **test_combat_cleanup_handler.py** (19 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
- *... and 400 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (109 shared connections)
- [CombatService](CombatService.md) (83 shared connections)
- [NATSError](NATSError.md) (44 shared connections)
- [TargetMatch](TargetMatch.md) (27 shared connections)
- [get_logger](get_logger.md) (23 shared connections)
- [test_combat_flee_handler.py](test_combat_flee_handler.py.md) (20 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (14 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (10 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (10 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (10 shared connections)
- [pytest.md](pytest.md.md) (8 shared connections)
- [.create_combat_instance](create_combat_instance.md) (7 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/models/combat.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_initialization.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_types.py`
- `server/services/player_position_service.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/services/test_aggro_threat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 1172 (95%)
- INFERRED: 57 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*