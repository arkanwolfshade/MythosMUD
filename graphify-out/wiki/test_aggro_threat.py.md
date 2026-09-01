# test_aggro_threat.py

> 92 nodes

## Key Concepts

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
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **UUID** (11 connections)
- **_make_participant()** (9 connections) — `server/tests/integration/test_aggro_flow.py`
- **get_npc_current_target()** (8 connections) — `server/services/aggro_threat.py`
- **_make_combat()** (8 connections) — `server/tests/integration/test_aggro_flow.py`
- **apply_stealth_wipe()** (7 connections) — `server/services/aggro_threat.py`
- **_get_aggro_config()** (7 connections) — `server/services/aggro_threat.py`
- **on_player_entered_stealth()** (7 connections) — `server/services/aggro_threat.py`
- **test_aggro_healer_overpull_switches_target()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_nightgaunt_like_damage_and_heal_threat()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_passive_mob_no_damage_threat_taunt_switches()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_stealth_wipe_switches_to_next()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_taunt_from_next_room_no_effect()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_tank_swap_taunt_sequence()** (6 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_on_player_entered_stealth_wipes_from_all_npcs()** (6 connections) — `server/tests/unit/services/test_aggro_threat.py`
- *... and 67 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (27 shared connections)
- [CombatInstance](CombatInstance.md) (14 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (5 shared connections)
- [TargetMatch](TargetMatch.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (3 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/services/test_aggro_threat.py`

## Audit Trail

- EXTRACTED: 262 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*