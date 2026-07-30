# test npc combat rewards

> 30 nodes

## Key Concepts

- **TestNPCCombatRewards** (19 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.mock_persistence()** (2 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.mock_game_mechanics()** (2 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.test_calculate_xp_reward_with_npc_definition()** (2 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.test_calculate_xp_reward_no_xp_value()** (2 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.test_calculate_xp_reward_none_npc()** (2 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.test_calculate_xp_reward_non_dict_stats()** (2 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.test_is_valid_uuid_valid()** (2 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.test_is_valid_uuid_invalid()** (2 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.test_check_player_connection_state_with_connection_manager()** (2 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.test_check_player_connection_state_no_container()** (2 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.test_award_xp_to_killer_success()** (2 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.test_award_xp_to_killer_failure()** (2 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.test_award_xp_to_killer_exception()** (2 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.test_award_xp_to_killer_zero_xp()** (2 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Test suite for NPCCombatRewards class.** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Create a mock persistence layer.** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Create a mock game mechanics service.** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Test calculate_xp_reward returns XP from NPC definition.** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Test calculate_xp_reward returns 0 when no xp_value in stats.** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Test calculate_xp_reward returns 0 when NPC is None.** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Test calculate_xp_reward returns 0 when stats is not a dict.** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Test _is_valid_uuid returns True for valid UUID.** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Test _is_valid_uuid returns False for invalid UUID.** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Test check_player_connection_state logs connection state.** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- *... and 5 more nodes in this community*

## Relationships

- [look container](look_container.md) (4 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_rewards.py`

## Audit Trail

- EXTRACTED: 61 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*