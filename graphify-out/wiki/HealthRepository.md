# HealthRepository

> 44 nodes

## Key Concepts

- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository.py** (19 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **asyncio** (9 connections)
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **_stats_int()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **.damage_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._update_player_health_inner()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **Player** (5 connections)
- **.heal_player()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **test_cold_damage_resistance_reduces_damage()** (4 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **test_damage_defaults_current_dp_to_20_when_missing()** (4 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **._calculate_effective_damage()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **test_calculate_effective_damage_zero_and_resistance_edge_cases()** (3 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_damage_player_logs_and_reraises_on_unexpected_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_damage_player_rejects_negative()** (3 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_heal_player_logs_and_reraises_on_unexpected_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_heal_player_max_dp_fallback_when_zero()** (3 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_heal_player_no_op_when_already_full()** (3 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_heal_player_rejects_negative()** (3 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_heal_player_success_and_capped()** (3 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_stats_int_defaults_and_coercion()** (3 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- *... and 19 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [Player](Player.md) (6 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (2 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/health_repository.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`

## Audit Trail

- EXTRACTED: 95 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*