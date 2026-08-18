# PlayerCombatService

> 111 nodes

## Key Concepts

- **PlayerCombatService** (76 connections) — `server/services/player_combat_service.py`
- **test_player_combat_service.py** (38 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **asyncio** (22 connections)
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **._award_xp_via_persistence_fallback()** (7 connections) — `server/services/player_combat_service.py`
- **player_combat_service()** (7 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **.clear_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **._get_xp_from_lifecycle_manager()** (5 connections) — `server/services/player_combat_service.py`
- **.track_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **test_cleanup_stale_combat_states()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state_not_found()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_end_clears_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_start_tracks_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **._award_xp_via_npc_rewards()** (4 connections) — `server/services/player_combat_service.py`
- **.calculate_xp_reward()** (4 connections) — `server/services/player_combat_service.py`
- **.get_player_combat_state()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_end()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_start()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_npc_death()** (4 connections) — `server/services/player_combat_service.py`
- **test_award_xp_on_npc_death_delegates_to_rewards_when_available()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_error()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_award_xp_on_npc_death_no_player_combat_service()** (4 connections) — `server/tests/unit/services/test_player_combat_service.py`
- *... and 86 more nodes in this community*

## Relationships

- [test_event_handler.py](test_event_handler.py.md) (10 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [combat_loader.py](combat_loader.py.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/services/player_combat_service.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 189 (81%)
- INFERRED: 44 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*