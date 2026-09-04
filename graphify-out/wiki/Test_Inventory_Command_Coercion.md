# Test Inventory Command Coercion

> 16 nodes

## Key Concepts

- **coerce_int()** (42 connections) — `server/utils/int_coercion.py`
- **int_coercion.py** (17 connections) — `server/utils/int_coercion.py`
- **test_inventory_command_coercion.py** (13 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_string_parsing()** (3 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_bool_before_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float_inf_falls_back_to_default()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float_nan_falls_back_to_default()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_plain_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_unknown_type()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **_int_from_decimal_string()** (2 connections) — `server/utils/int_coercion.py`
- **_int_from_float_safe()** (2 connections) — `server/utils/int_coercion.py`
- **parametrize** (1 connections)
- **Unit tests for server.utils.int_coercion.coerce_int.** (1 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **Coerce object-shaped JSON/JSONB values to int (commands, models, stats).** (1 connections) — `server/utils/int_coercion.py`
- **Parse integer fields from object-typed JSON/JSONB payloads. Non-numeric strings…** (1 connections) — `server/utils/int_coercion.py`

## Relationships

- [Lucidity Helpers & Catatonia](Lucidity_Helpers_&_Catatonia.md) (8 shared connections)
- [Inventory Drop Command](Inventory_Drop_Command.md) (8 shared connections)
- [Game Tick Death](Game_Tick_Death.md) (5 shared connections)
- [Test Look Container Helpers](Test_Look_Container_Helpers.md) (4 shared connections)
- [Test Game Tick Processing Async](Test_Game_Tick_Processing_Async.md) (3 shared connections)
- [Container Helpers](Container_Helpers.md) (3 shared connections)
- [Game Tick Status Effects](Game_Tick_Status_Effects.md) (2 shared connections)
- [Test Magic Service](Test_Magic_Service.md) (2 shared connections)
- [Test Player Respawn Service](Test_Player_Respawn_Service.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [Test Look Container](Test_Look_Container.md) (1 shared connections)
- [Magic Service](Magic_Service.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 64 (91%)
- INFERRED: 6 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*