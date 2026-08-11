# Magic Lifespan Initialization

> 15 nodes

## Key Concepts

- **coerce_int()** (37 connections) — `server/utils/int_coercion.py`
- **int_coercion.py** (13 connections) — `server/utils/int_coercion.py`
- **test_inventory_command_coercion.py** (12 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_string_parsing()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_bool_before_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_plain_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float_nan_falls_back_to_default()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float_inf_falls_back_to_default()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_unknown_type()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **_int_from_decimal_string()** (2 connections) — `server/utils/int_coercion.py`
- **_int_from_float_safe()** (2 connections) — `server/utils/int_coercion.py`
- **Unit tests for server.utils.int_coercion.coerce_int.** (1 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **Coerce object-shaped JSON/JSONB values to int (commands, models, stats).** (1 connections) — `server/utils/int_coercion.py`
- **Parse integer fields from object-typed JSON/JSONB payloads.      Non-numeric str** (1 connections) — `server/utils/int_coercion.py`

## Relationships

- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (6 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (6 shared connections)
- [FastAPI Auth Integration](FastAPI_Auth_Integration.md) (4 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (4 shared connections)
- [Connection Room Presence Utils](Connection_Room_Presence_Utils.md) (3 shared connections)
- [Maps API Endpoints](Maps_API_Endpoints.md) (3 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (3 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Panel Layout Libraries Spec](Panel_Layout_Libraries_Spec.md) (2 shared connections)

## Source Files

- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 77 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*