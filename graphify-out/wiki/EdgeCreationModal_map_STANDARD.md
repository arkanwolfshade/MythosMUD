# EdgeCreationModal map STANDARD

> 52 nodes

## Key Concepts

- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **process_player_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **resolve_player_attack_damage()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **get_npc_current_target()** (8 connections) — `server/services/aggro_threat.py`
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
- **UUID** (3 connections)
- **_attacker_stats_dict_from_full_player()** (3 connections) — `server/services/combat_turn_participant_actions.py`
- **test_strength_modifier_from_attacker_stats_defaults()** (3 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- *... and 27 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (19 shared connections)
- [command factories exploration](command_factories_exploration.md) (13 shared connections)
- [models npc rationale](models_npc_rationale.md) (9 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (8 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (7 shared connections)
- [player event handlers](player_event_handlers.md) (6 shared connections)
- [tools generate invite](tools_generate_invite.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [combat npc mixin](combat_npc_mixin.md) (3 shared connections)
- [MapView GameClientV2ContainerView Tabbed](MapView_GameClientV2ContainerView_Tabbed.md) (3 shared connections)
- [game chat service](game_chat_service.md) (3 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 216 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*