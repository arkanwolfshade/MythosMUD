# coerce_int

> 20 nodes

## Key Concepts

- **coerce_int()** (51 connections) — `server/utils/int_coercion.py`
- **int_coercion.py** (17 connections) — `server/utils/int_coercion.py`
- **_stats_int()** (14 connections) — `server/models/player.py`
- **test_inventory_command_coercion.py** (13 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_string_parsing()** (3 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_stats_int_delegates_to_coerce_int()** (3 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_bool_before_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float_inf_falls_back_to_default()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float_nan_falls_back_to_default()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_plain_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_unknown_type()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **_int_from_decimal_string()** (2 connections) — `server/utils/int_coercion.py`
- **_int_from_float_safe()** (2 connections) — `server/utils/int_coercion.py`
- **parametrize** (1 connections)
- **Coerce a JSONB stat value to int for DP and combat helpers.** (1 connections) — `server/models/player.py`
- **Unit tests for server.utils.int_coercion.coerce_int.** (1 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **JSONB stats use the same coercion as inventory command payloads.** (1 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **Coerce object-shaped JSON/JSONB values to int (commands, models, stats).** (1 connections) — `server/utils/int_coercion.py`
- **Parse integer fields from object-typed JSON/JSONB payloads. Non-numeric strings…** (1 connections) — `server/utils/int_coercion.py`

## Relationships

- [Player](Player.md) (9 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (7 shared connections)
- [LucidityService](LucidityService.md) (6 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (5 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (5 shared connections)
- [test_look_container.py](test_look_container.py.md) (5 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (4 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (3 shared connections)
- [log_and_raise](log_and_raise.md) (3 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (3 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/models/player.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 86 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*