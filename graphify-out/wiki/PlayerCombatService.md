# PlayerCombatService

> 117 nodes

## Key Concepts

- **PlayerCombatService** (76 connections) — `server/services/player_combat_service.py`
- **test_player_combat_service.py** (38 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **asyncio** (22 connections)
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **._award_xp_via_persistence_fallback()** (7 connections) — `server/services/player_combat_service.py`
- **player_combat_service()** (7 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_targeting.py`
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
- *... and 92 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [CombatInstance](CombatInstance.md) (5 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (4 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (4 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [TargetMatch](TargetMatch.md) (3 shared connections)
- [combat_loader.py](combat_loader.py.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [test_lifespan_startup.py](test_lifespan_startup.py.md) (1 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/realtime/connection_manager.py`
- `server/services/combat_service.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 192 (80%)
- INFERRED: 49 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*