# Server Services (36)

> 51 nodes

## Key Concepts

- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_get_combat_container_services()** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_npc_target()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_player_attack()** (7 connections) — `server/services/combat_turn_participant_actions.py`
- **_execute_npc_attack()** (6 connections) — `server/services/combat_turn_participant_actions.py`
- **test_process_npc_turn_calls_process_attack_when_target_resolved()** (6 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_get_target_stats_for_damage()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_apply_physical_strength_bonus()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_continue_npc_turn()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_continue_player_turn()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_select_player_target()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_should_skip_for_casting()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **test_select_npc_target_prefers_mortally_wounded_player_over_skipping()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_resolve_npc_target_uses_aggro_current_target()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_resolve_npc_target_broadcasts_when_aggro_switches()** (5 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **_strength_modifier_from_attacker_stats()** (4 connections) — `server/services/combat_turn_participant_actions.py`
- **.get_equipped_items()** (3 connections) — `server/models/player.py`
- **UUID** (3 connections)
- **_attacker_stats_dict_from_full_player()** (3 connections) — `server/services/combat_turn_participant_actions.py`
- **test_strength_modifier_from_attacker_stats_defaults()** (3 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- *... and 26 more nodes in this community*

## Relationships

- [Server Models (2)](Server_Models_%282%29.md) (18 shared connections)
- [Server Services (28)](Server_Services_%2828%29.md) (12 shared connections)
- [Server Services (7)](Server_Services_%287%29.md) (10 shared connections)
- [Server Game](Server_Game.md) (8 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (8 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (6 shared connections)
- [Server Services (13)](Server_Services_%2813%29.md) (5 shared connections)
- [Server Services (5)](Server_Services_%285%29.md) (4 shared connections)
- [Server Config (2)](Server_Config_%282%29.md) (3 shared connections)
- [Server Config](Server_Config.md) (3 shared connections)
- [Server App](Server_App.md) (2 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (2 shared connections)

## Source Files

- `server/models/player.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 210 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*