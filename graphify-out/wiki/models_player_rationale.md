# models player rationale

> 41 nodes

## Key Concepts

- **coerce_int()** (37 connections) — `server/utils/int_coercion.py`
- **_stats_int()** (16 connections) — `server/models/player.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **int_coercion.py** (13 connections) — `server/utils/int_coercion.py`
- **test_inventory_command_coercion.py** (12 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.is_alive()** (4 connections) — `server/models/player.py`
- **.is_mortally_wounded()** (4 connections) — `server/models/player.py`
- **.is_dead()** (4 connections) — `server/models/player.py`
- **.get_health_state()** (4 connections) — `server/models/player.py`
- **.get_combat_stats()** (4 connections) — `server/models/player.py`
- **.get_health_percentage()** (4 connections) — `server/models/player.py`
- **test_stats_int_delegates_to_coerce_int()** (3 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_string_parsing()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_bool_before_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_plain_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float_nan_falls_back_to_default()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float_inf_falls_back_to_default()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_unknown_type()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **_int_from_decimal_string()** (2 connections) — `server/utils/int_coercion.py`
- **_int_from_float_safe()** (2 connections) — `server/utils/int_coercion.py`
- *... and 16 more nodes in this community*

## Relationships

- [world models rationale](world_models_rationale.md) (14 shared connections)
- [inventory commands command](inventory_commands_command.md) (7 shared connections)
- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (5 shared connections)
- [persistence container item](persistence_container_item.md) (3 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (3 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (2 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (1 shared connections)
- [player persistence repository](player_persistence_repository.md) (1 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 166 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*