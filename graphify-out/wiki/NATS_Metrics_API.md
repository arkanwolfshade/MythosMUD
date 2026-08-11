# NATS Metrics API

> 50 nodes

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
- **UUID** (3 connections)
- **_attacker_stats_dict_from_full_player()** (3 connections) — `server/services/combat_turn_participant_actions.py`
- **test_strength_modifier_from_attacker_stats_defaults()** (3 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **test_apply_physical_strength_bonus_adds_for_physical_only()** (3 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- *... and 25 more nodes in this community*

## Relationships

- [Rest Command Flow](Rest_Command_Flow.md) (18 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (12 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (10 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (8 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (6 shared connections)
- [Command Parser](Command_Parser.md) (6 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (5 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (4 shared connections)
- [NATS Subject Admin API](NATS_Subject_Admin_API.md) (3 shared connections)
- [NATS Retry Handler](NATS_Retry_Handler.md) (3 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (2 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (2 shared connections)

## Source Files

- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 207 (95%)
- INFERRED: 10 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*