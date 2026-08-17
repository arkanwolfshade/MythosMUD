# coerce_int

> 44 nodes

## Key Concepts

- **coerce_int()** (51 connections) — `server/utils/int_coercion.py`
- **int_coercion.py** (17 connections) — `server/utils/int_coercion.py`
- **_stats_int()** (14 connections) — `server/models/player.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **test_inventory_command_coercion.py** (13 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
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

- [DatabaseError](DatabaseError.md) (16 shared connections)
- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (8 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (7 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (6 shared connections)
- [test_look_container_helpers.py](test_look_container_helpers.py.md) (5 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (3 shared connections)
- [inventory_get_command.py](inventory_get_command.py.md) (3 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)
- [Protocol](Protocol.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/models/player.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 125 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*