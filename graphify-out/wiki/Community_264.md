# Community 264

> 58 nodes

## Key Concepts

- **combat_turn_participant_actions.py** (40 connections) — `server/services/combat_turn_participant_actions.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **process_npc_turn()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_weapon_damage_from_equipped_player()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **get_npc_current_target()** (8 connections) — `server/services/aggro_threat.py`
- **_get_combat_container_services()** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_player_attack_damage()** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatService** (7 connections)
- **_execute_npc_attack()** (6 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_player_attack()** (6 connections) — `server/services/combat_turn_participant_actions.py`
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
- *... and 33 more nodes in this community*

## Relationships

- [Combat Instance Turn Management](Combat_Instance_Turn_Management.md) (29 shared connections)
- [Community 97](Community_97.md) (7 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (4 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (3 shared connections)
- [Community 275](Community_275.md) (3 shared connections)
- [Community 261](Community_261.md) (2 shared connections)
- [Community 80](Community_80.md) (2 shared connections)
- [Community 93](Community_93.md) (2 shared connections)
- [Community 46](Community_46.md) (2 shared connections)
- [Community 514](Community_514.md) (1 shared connections)
- [Community 117](Community_117.md) (1 shared connections)
- [Community 355](Community_355.md) (1 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/corruption_service.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 148 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*