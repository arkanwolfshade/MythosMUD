# coerce_int

> 44 nodes

## Key Concepts

- **coerce_int()** (62 connections) — `server/utils/int_coercion.py`
- **int_coercion.py** (22 connections) — `server/utils/int_coercion.py`
- **_stats_int()** (14 connections) — `server/models/player.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **test_inventory_command_coercion.py** (12 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **inventory_command_coercion.py** (6 connections) — `server/commands/inventory_command_coercion.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- **.get_combat_stats()** (4 connections) — `server/models/player.py`
- **.get_health_percentage()** (4 connections) — `server/models/player.py`
- **.get_health_state()** (4 connections) — `server/models/player.py`
- **.is_alive()** (4 connections) — `server/models/player.py`
- **.is_dead()** (4 connections) — `server/models/player.py`
- **.is_mortally_wounded()** (4 connections) — `server/models/player.py`
- **test_coerce_int_string_parsing()** (3 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_stats_int_delegates_to_coerce_int()** (3 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_bool_before_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float_inf_falls_back_to_default()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float_nan_falls_back_to_default()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_plain_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_unknown_type()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **_int_from_decimal_string()** (2 connections) — `server/utils/int_coercion.py`
- *... and 19 more nodes in this community*

## Relationships

- [Player](Player.md) (23 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (7 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (6 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (5 shared connections)
- [game_tick_status_effects.py](game_tick_status_effects.py.md) (5 shared connections)
- [look_container.py](look_container.py.md) (4 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (4 shared connections)
- [NPCBase](NPCBase.md) (3 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (3 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (3 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (3 shared connections)
- [magic_service.py](magic_service.py.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/models/player.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 140 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*