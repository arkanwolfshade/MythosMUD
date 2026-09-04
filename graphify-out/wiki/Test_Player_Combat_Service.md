# Test Player Combat Service

> 89 nodes

## Key Concepts

- **PlayerCombatService** (74 connections) — `server/services/player_combat_service.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **asyncio** (22 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **player_combat_service()** (7 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.track_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **test_cleanup_stale_combat_states()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state_not_found()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_end_clears_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_start_tracks_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.get_player_combat_state()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_start()** (4 connections) — `server/services/player_combat_service.py`
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
- *... and 64 more nodes in this community*

## Relationships

- [Player Combat Service](Player_Combat_Service.md) (15 shared connections)
- [Test Movement Service](Test_Movement_Service.md) (6 shared connections)
- [Npc Combat Integration Service](Npc_Combat_Integration_Service.md) (3 shared connections)
- [Lifespan Magic](Lifespan_Magic.md) (3 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (2 shared connections)
- [Combat Loader](Combat_Loader.md) (2 shared connections)
- [Combat Events](Combat_Events.md) (2 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (2 shared connections)
- [Test Player Event Handlers State](Test_Player_Event_Handlers_State.md) (2 shared connections)
- [Test Catatonia Registry](Test_Catatonia_Registry.md) (1 shared connections)
- [Test Combat Handler](Test_Combat_Handler.md) (1 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/services/combat_service.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 160 (80%)
- INFERRED: 40 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*