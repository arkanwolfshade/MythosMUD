# Player

> 185 nodes

## Key Concepts

- **Player** (231 connections) — `server/models/player.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository.py** (20 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **health_repository.py** (18 connections) — `server/persistence/repositories/health_repository.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **asyncio** (9 connections)
- **test_health_repository_cold_resistance.py** (8 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **_stats_int()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- **.damage_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._update_player_health_inner()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **test_cold_damage_resistance_reduces_damage()** (5 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **test_damage_defaults_current_dp_to_20_when_missing()** (5 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **Player** (5 connections)
- **_convert_legacy_stats_string()** (4 connections) — `server/models/player.py`
- **.get_combat_stats()** (4 connections) — `server/models/player.py`
- **.get_health_percentage()** (4 connections) — `server/models/player.py`
- *... and 160 more nodes in this community*

## Relationships

- [sqlalchemy.md](sqlalchemy.md.md) (16 shared connections)
- [pytest.md](pytest.md.md) (14 shared connections)
- [command_result_text](command_result_text.md) (13 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (12 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (11 shared connections)
- [inventory_get_command.py](inventory_get_command.py.md) (10 shared connections)
- [coerce_int](coerce_int.md) (9 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (7 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (6 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (5 shared connections)
- [repositories/__init__.py](repositories-__init__.py.md) (5 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (5 shared connections)

## Source Files

- `server/models/player.py`
- `server/persistence/repositories/health_repository.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`

## Audit Trail

- EXTRACTED: 375 (77%)
- INFERRED: 111 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*