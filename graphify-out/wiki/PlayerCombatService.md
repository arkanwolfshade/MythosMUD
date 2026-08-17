# PlayerCombatService

> 214 nodes

## Key Concepts

- **PlayerCombatService** (76 connections) — `server/services/player_combat_service.py`
- **test_movement_service.py** (52 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_player_combat_service.py** (38 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **movement_service.py** (35 connections) — `server/game/movement_service.py`
- **asyncio** (22 connections)
- **asyncio** (20 connections)
- **movement_helpers.py** (17 connections) — `server/game/movement_helpers.py`
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **validate_exit()** (11 connections) — `server/game/movement_helpers.py`
- **validate_player_room_membership()** (11 connections) — `server/game/movement_helpers.py`
- **check_combat_state()** (10 connections) — `server/game/movement_helpers.py`
- **check_player_posture()** (8 connections) — `server/game/movement_helpers.py`
- **._award_xp_via_persistence_fallback()** (7 connections) — `server/services/player_combat_service.py`
- **player_combat_service()** (7 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **.clear_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **._get_xp_from_lifecycle_manager()** (5 connections) — `server/services/player_combat_service.py`
- **.track_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **test_cleanup_stale_combat_states()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_get_player_combat_state_not_found()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_end_clears_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **test_handle_combat_start_tracks_state()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- *... and 189 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (20 shared connections)
- [log_and_raise](log_and_raise.md) (12 shared connections)
- [pytest.md](pytest.md.md) (8 shared connections)
- [ValidationError](ValidationError.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [NPCCombatIntegrationReadApi](NPCCombatIntegrationReadApi.md) (3 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [combat_loader.py](combat_loader.py.md) (2 shared connections)

## Source Files

- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/services/player_combat_service.py`
- `server/services/player_position_service.py`
- `server/tests/unit/game/test_movement_service.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 380 (88%)
- INFERRED: 54 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*