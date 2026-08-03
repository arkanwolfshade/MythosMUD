# models player rationale

> 19 nodes

## Key Concepts

- **coerce_int()** (37 connections) — `server/utils/int_coercion.py`
- **_stats_int()** (16 connections) — `server/models/player.py`
- **int_coercion.py** (13 connections) — `server/utils/int_coercion.py`
- **test_inventory_command_coercion.py** (12 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
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
- **Coerce a JSONB stat value to int for DP and combat helpers.** (1 connections) — `server/models/player.py`
- **Unit tests for server.utils.int_coercion.coerce_int.** (1 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **JSONB stats use the same coercion as inventory command payloads.** (1 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **Coerce object-shaped JSON/JSONB values to int (commands, models, stats).** (1 connections) — `server/utils/int_coercion.py`
- **Parse integer fields from object-typed JSON/JSONB payloads.      Non-numeric str** (1 connections) — `server/utils/int_coercion.py`

## Relationships

- [combat models rationale](combat_models_rationale.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (6 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (4 shared connections)
- [commands inventory command](commands_inventory_command.md) (4 shared connections)
- [world models rationale](world_models_rationale.md) (3 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (3 shared connections)
- [tick game processing](tick_game_processing.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (2 shared connections)

## Source Files

- `server/models/player.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 98 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*