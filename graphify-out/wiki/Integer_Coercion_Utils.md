# Integer Coercion Utils

> 41 nodes · cohesion 0.08

## Key Concepts

- **coerce_int()** (37 connections) — `server/utils/int_coercion.py`
- **_stats_int()** (16 connections) — `server/models/player.py`
- **.get_stats()** (12 connections) — `server/models/player.py`
- **test_inventory_command_coercion.py** (11 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **int_coercion.py** (11 connections) — `server/utils/int_coercion.py`
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
- **_int_from_float_safe()** (2 connections) — `server/utils/int_coercion.py`
- *... and 16 more nodes in this community*

## Relationships

- [[Player Domain Model]] (11 shared connections)
- [[Admin Summon Command]] (7 shared connections)
- [[Player Respawn Events]] (6 shared connections)
- [[Lucidity Rescue Helpers]] (5 shared connections)
- [[SQLAlchemy Model Base]] (3 shared connections)
- [[Persistence Container Extended]] (3 shared connections)
- [[WebSocket Initial State]] (3 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Player Respawn Service]] (2 shared connections)
- [[Game Tick Processing]] (1 shared connections)
- [[App Game Tick]] (1 shared connections)
- [[Lucidity State Models]] (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 163 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
