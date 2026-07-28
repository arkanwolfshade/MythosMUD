# Logging Migration Examples

> 43 nodes · cohesion 0.07

## Key Concepts

- **coerce_int()** (37 connections) — `server/utils/int_coercion.py`
- **_stats_int()** (16 connections) — `server/models/player.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **int_coercion.py** (13 connections) — `server/utils/int_coercion.py`
- **test_inventory_command_coercion.py** (12 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **inventory_command_coercion.py** (6 connections) — `server/commands/inventory_command_coercion.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- **.get_combat_stats()** (4 connections) — `server/models/player.py`
- **.get_health_percentage()** (4 connections) — `server/models/player.py`
- **.get_health_state()** (4 connections) — `server/models/player.py`
- **.is_alive()** (4 connections) — `server/models/player.py`
- **.is_dead()** (4 connections) — `server/models/player.py`
- **.is_mortally_wounded()** (4 connections) — `server/models/player.py`
- **test_stats_int_delegates_to_coerce_int()** (3 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_bool_before_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float_inf_falls_back_to_default()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float_nan_falls_back_to_default()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_plain_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_string_parsing()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_unknown_type()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **_int_from_decimal_string()** (2 connections) — `server/utils/int_coercion.py`
- *... and 18 more nodes in this community*

## Relationships

- [Event Bus Serialization](Event_Bus_Serialization.md) (18 shared connections)
- [Deprecated Logging Patterns](Deprecated_Logging_Patterns.md) (5 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (5 shared connections)
- [Admin Summon Command](Admin_Summon_Command.md) (4 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (4 shared connections)
- [Container Persistence Queries](Container_Persistence_Queries.md) (3 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [WebSocket Player Helpers](WebSocket_Player_Helpers.md) (1 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (1 shared connections)
- [Fresh Session Test Guide](Fresh_Session_Test_Guide.md) (1 shared connections)
- [Player Death Service Tests](Player_Death_Service_Tests.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/models/player.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 173 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*