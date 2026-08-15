# HealthRepository

> 46 nodes

## Key Concepts

- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository.py** (19 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **asyncio** (9 connections)
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **_stats_int()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **.damage_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._update_player_health_inner()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **test_cold_damage_resistance_reduces_damage()** (5 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **test_damage_defaults_current_dp_to_20_when_missing()** (5 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **Player** (5 connections)
- **.heal_player()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **test_damage_player_logs_and_reraises_on_unexpected_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_damage_player_rejects_negative()** (4 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_heal_player_logs_and_reraises_on_unexpected_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_heal_player_max_dp_fallback_when_zero()** (4 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_heal_player_no_op_when_already_full()** (4 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_heal_player_rejects_negative()** (4 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_heal_player_success_and_capped()** (4 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_update_player_health_raises_database_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **._calculate_effective_damage()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/health_repository.py`
- *... and 21 more nodes in this community*

## Relationships

- [Player](Player.md) (14 shared connections)
- [DatabaseError](DatabaseError.md) (12 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (2 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/health_repository.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`

## Audit Trail

- EXTRACTED: 87 (77%)
- INFERRED: 26 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*