# logoutHandler logger App

> 62 nodes

## Key Concepts

- **player_effect_repository.py** (21 connections) — `server/persistence/repositories/player_effect_repository.py`
- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **test_player_effect_repository.py** (17 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **.get_active_effects_for_player()** (10 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_row_to_player_effect()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **UUID** (8 connections)
- **.add_effect()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Any** (7 connections)
- **AddEffectInput** (7 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_add_effect_params()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.delete_effect()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_effects_expiring_this_tick()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.expire_effects_for_tick()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_make_effect()** (6 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **._execute_add_effect()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_effect_remaining_ticks()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_row_from_effect()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **_str_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_int_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_opt_str()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.has_effect()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **test_get_active_effects_for_player_filters_by_remaining()** (4 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_has_effect_true()** (4 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_effect_remaining_ticks()** (4 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **._remaining_ticks()** (3 connections) — `server/persistence/repositories/player_effect_repository.py`
- *... and 37 more nodes in this community*

## Relationships

- [endpoints auth rationale](endpoints_auth_rationale.md) (10 shared connections)
- [player room realtime](player_room_realtime.md) (9 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (8 shared connections)
- [add used user](add_used_user.md) (7 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (2 shared connections)
- [useWebSocketConnectionTestFixtures useWe](useWebSocketConnectionTestFixtures_useWe.md) (1 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_effect_repository.py`
- `server/tests/unit/persistence/test_player_effect_repository.py`

## Audit Trail

- EXTRACTED: 212 (95%)
- INFERRED: 12 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*