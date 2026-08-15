# models/combat.py

> 148 nodes

## Key Concepts

- **models/combat.py** (56 connections) — `server/models/combat.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatParticipantType** (44 connections) — `server/models/combat.py`
- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **_make_combat()** (23 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **add_damage_threat()** (20 connections) — `server/services/aggro_threat.py`
- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- **_make_participant()** (13 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **apply_taunt()** (12 connections) — `server/services/aggro_threat.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **UUID** (11 connections)
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_make_participant()** (9 connections) — `server/tests/integration/test_aggro_flow.py`
- **get_npc_current_target()** (8 connections) — `server/services/aggro_threat.py`
- **_get_combat_container_services()** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **_make_combat()** (8 connections) — `server/tests/integration/test_aggro_flow.py`
- **apply_stealth_wipe()** (7 connections) — `server/services/aggro_threat.py`
- *... and 123 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (39 shared connections)
- [CombatInstance](CombatInstance.md) (27 shared connections)
- [CombatService](CombatService.md) (23 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (9 shared connections)
- [get_config](get_config.md) (9 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (8 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (8 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (7 shared connections)
- [TargetMatch](TargetMatch.md) (5 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (5 shared connections)
- [Player](Player.md) (5 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/services/test_aggro_threat.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 474 (96%)
- INFERRED: 18 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*