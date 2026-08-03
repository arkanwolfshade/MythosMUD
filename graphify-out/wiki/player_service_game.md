# player service game

> 68 nodes

## Key Concepts

- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **test_is_player_in_combat_sync_true()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_cleanup_stale_combat_states()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_player_combat_service_init()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_track_player_combat_state()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state_not_found()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_clear_player_combat_state()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_is_player_in_combat_sync_false()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_is_player_in_combat()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_players_in_combat()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_start()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_end()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_success()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_player_not_found()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_error()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_calculate_xp_reward_from_mapping()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_calculate_xp_reward_from_database()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_calculate_xp_reward_default()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_combat_stats()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_combat_stats_multiple_combats()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_npc_death_error()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_delegates_to_rewards_when_available()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_no_player_combat_service()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- *... and 43 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (27 shared connections)
- [item models rationale](item_models_rationale.md) (6 shared connections)
- [command input commands](command_input_commands.md) (2 shared connections)
- [combat attack handler](combat_attack_handler.md) (2 shared connections)

## Source Files

- `server/services/player_combat_service.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 175 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*