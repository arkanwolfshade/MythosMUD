# test_player_combat_service.py

> 74 nodes

## Key Concepts

- **test_player_combat_service.py** (38 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **asyncio** (22 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **player_combat_service()** (7 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_cleanup_stale_combat_states()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state_not_found()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_end_clears_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_start_tracks_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.get_player_combat_state()** (4 connections) — `server/services/player_combat_service.py`
- **test_award_xp_on_npc_death_delegates_to_rewards_when_available()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_error()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_no_player_combat_service()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_player_not_found()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_success()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_calculate_xp_reward_default()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_calculate_xp_reward_from_database()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_calculate_xp_reward_from_mapping()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_clear_player_combat_state()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_combat_stats()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_combat_stats_multiple_combats()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_players_in_combat()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_end()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_start()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_npc_death_error()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- *... and 49 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (30 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [PlayerXPAwardEvent](PlayerXPAwardEvent.md) (2 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (1 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (1 shared connections)
- [test_go_command.py](test_go_command.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/player_combat_service.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 110 (77%)
- INFERRED: 33 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*