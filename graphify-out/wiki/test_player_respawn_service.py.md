# test_player_respawn_service.py

> 124 nodes

## Key Concepts

- **test_player_respawn_service.py** (63 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **PlayerRespawnService** (33 connections) — `server/services/player_respawn_service.py`
- **asyncio** (29 connections)
- **UUID** (14 connections)
- **.respawn_player()** (9 connections) — `server/services/player_respawn_service.py`
- **test_get_respawn_room_redirects_template_to_exit_room()** (9 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **.respawn_player_from_delirium()** (8 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (8 connections) — `server/services/player_respawn_service.py`
- **test_get_respawn_room_keeps_normal_custom_room()** (8 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **._prepare_delirium_respawn()** (7 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (7 connections) — `server/services/player_respawn_service.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **AsyncSession** (7 connections)
- **fixture** (7 connections)
- **._clear_respawn_combat_state()** (6 connections) — `server/services/player_respawn_service.py`
- **.get_respawn_room()** (6 connections) — `server/services/player_respawn_service.py`
- **.move_player_to_limbo()** (6 connections) — `server/services/player_respawn_service.py`
- **._redirect_template_respawn()** (6 connections) — `server/services/player_respawn_service.py`
- **_session_returning()** (6 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **._can_move_to_limbo()** (5 connections) — `server/services/player_respawn_service.py`
- **._publish_delirium_respawn_event()** (5 connections) — `server/services/player_respawn_service.py`
- **_foyer()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_combat_clear_error()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_database_error()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_success()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- *... and 99 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (21 shared connections)
- [LucidityService](LucidityService.md) (17 shared connections)
- [Player](Player.md) (12 shared connections)
- [Stats](Stats.md) (10 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (4 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (3 shared connections)
- [Room](Room.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [_PlayerCombatClearing](_PlayerCombatClearing.md) (2 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)

## Source Files

- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 246 (88%)
- INFERRED: 33 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*