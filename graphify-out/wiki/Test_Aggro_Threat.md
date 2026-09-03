# Test Aggro Threat

> 88 nodes

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
- **UUID** (11 connections)
- **_make_participant()** (9 connections) — `server/tests/integration/test_aggro_flow.py`
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
- **test_update_aggro_excludes_dead_from_candidate()** (6 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_update_aggro_one_entity_sets_target()** (6 connections) — `server/tests/unit/services/test_aggro_threat.py`
- *... and 63 more nodes in this community*

## Relationships

- [Test Combat Flee Handler](Test_Combat_Flee_Handler.md) (12 shared connections)
- [Test Combat Cleanup Handler](Test_Combat_Cleanup_Handler.md) (11 shared connections)
- [Combat Turn Processing](Combat_Turn_Processing.md) (10 shared connections)
- [Combat Turn Participant Actions](Combat_Turn_Participant_Actions.md) (7 shared connections)
- [Combat Taunt](Combat_Taunt.md) (5 shared connections)
- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (4 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (3 shared connections)
- [Test Config Init](Test_Config_Init.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/services/test_aggro_threat.py`

## Audit Trail

- EXTRACTED: 250 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*