# Combat Turn Participant Actions

> 56 nodes

## Key Concepts

- **combat_turn_participant_actions.py** (47 connections) — `server/services/combat_turn_participant_actions.py`
- **test_combat_turn_participant_actions.py** (13 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **_get_combat_container_services()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **get_npc_current_target()** (8 connections) — `server/services/aggro_threat.py`
- **_execute_player_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_npc_attack()** (6 connections) — `server/services/combat_turn_participant_actions.py`
- **test_process_npc_turn_calls_process_attack_when_target_resolved()** (6 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_apply_physical_strength_bonus()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_get_target_stats_for_damage()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_player_target()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_continue_npc_turn()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_continue_player_turn()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_skip_for_casting()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **test_resolve_npc_target_broadcasts_when_aggro_switches()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_resolve_npc_target_uses_aggro_current_target()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_attacker_stats_dict_from_full_player()** (4 connections) — `server/services/combat_turn_participant_actions.py`
- **_strength_modifier_from_attacker_stats()** (4 connections) — `server/services/combat_turn_participant_actions.py`
- **test_select_npc_target_prefers_mortally_wounded_player_over_skipping()** (4 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **.get_stats()** (3 connections) — `server/services/player_position_service.py`
- *... and 31 more nodes in this community*

## Relationships

- [Combat Turn Processing](Combat_Turn_Processing.md) (19 shared connections)
- [Test Combat Flee Handler](Test_Combat_Flee_Handler.md) (10 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (8 shared connections)
- [Test Aggro Threat](Test_Aggro_Threat.md) (7 shared connections)
- [Async Persistence](Async_Persistence.md) (5 shared connections)
- [Test Combat Cleanup Handler](Test_Combat_Cleanup_Handler.md) (5 shared connections)
- [NATS Messaging Config](NATS_Messaging_Config.md) (4 shared connections)
- [Test Config Init](Test_Config_Init.md) (3 shared connections)
- [Cors](Cors.md) (3 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (3 shared connections)
- [Test Prototype Registry](Test_Prototype_Registry.md) (3 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (3 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/player_position_service.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 148 (89%)
- INFERRED: 19 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*