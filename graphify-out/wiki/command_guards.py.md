# command_guards.py

> 65 nodes · cohesion 0.05

## Key Concepts

- **player_effect_repository.py** (22 connections) — `server/persistence/repositories/player_effect_repository.py`
- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **test_player_effect_repository.py** (17 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **PlayerEffect** (15 connections) — `server/models/player_effect.py`
- **player_effect.py** (10 connections) — `server/models/player_effect.py`
- **.get_active_effects_for_player()** (9 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_row_to_player_effect()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **asyncio** (8 connections)
- **.add_effect()** (7 connections) — `server/persistence/repositories/player_effect_repository.py`
- **UUID** (7 connections)
- **_add_effect_params()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **AddEffectInput** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Any** (6 connections)
- **_make_effect()** (6 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **.delete_effect()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **._execute_add_effect()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_effect_remaining_ticks()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_row_from_effect()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_active_effects_for_player_filters_by_remaining()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_effect_remaining_ticks()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_has_effect_true()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **_int_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_opt_str()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.has_effect()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_str_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- *... and 40 more nodes in this community*

## Relationships

- [endpoints.py](endpoints.py.md) (12 shared connections)
- [Room](Room.md) (7 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (3 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (2 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (2 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (2 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [whisper-movement.spec.ts](whisper-movement.spec.ts.md) (1 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)
- [test_inventory_item_matching.py](test_inventory_item_matching.py.md) (1 shared connections)

## Source Files

- `server/models/player_effect.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/tests/unit/persistence/test_player_effect_repository.py`

## Audit Trail

- EXTRACTED: 138 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*