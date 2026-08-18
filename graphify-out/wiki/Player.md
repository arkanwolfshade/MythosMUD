# Player

> 159 nodes

## Key Concepts

- **Player** (231 connections) — `server/models/player.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository.py** (20 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **health_repository.py** (18 connections) — `server/persistence/repositories/health_repository.py`
- **asyncio** (9 connections)
- **test_health_repository_cold_resistance.py** (8 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **_stats_int()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **.damage_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._update_player_health_inner()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **test_cold_damage_resistance_reduces_damage()** (5 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **test_damage_defaults_current_dp_to_20_when_missing()** (5 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **Player** (5 connections)
- **_convert_legacy_stats_string()** (4 connections) — `server/models/player.py`
- **.heal_player()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **test_damage_player_logs_and_reraises_on_unexpected_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_damage_player_rejects_negative()** (4 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_heal_player_logs_and_reraises_on_unexpected_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_heal_player_max_dp_fallback_when_zero()** (4 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_heal_player_no_op_when_already_full()** (4 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_heal_player_rejects_negative()** (4 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- *... and 134 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (29 shared connections)
- [DatabaseError](DatabaseError.md) (22 shared connections)
- [LucidityService](LucidityService.md) (21 shared connections)
- [models/player.py](models-player.py.md) (18 shared connections)
- [command_result_text](command_result_text.md) (13 shared connections)
- [coerce_int](coerce_int.md) (11 shared connections)
- [inventory_get_command.py](inventory_get_command.py.md) (10 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (7 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (6 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (6 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (5 shared connections)
- [test_player_repository_room.py](test_player_repository_room.py.md) (4 shared connections)

## Source Files

- `server/models/player.py`
- `server/persistence/repositories/health_repository.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`

## Audit Trail

- EXTRACTED: 341 (76%)
- INFERRED: 107 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*