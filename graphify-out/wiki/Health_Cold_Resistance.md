# Health Cold Resistance

> 31 nodes · cohesion 0.10

## Key Concepts

- **HealthRepository** (20 connections) — `server/persistence/repositories/health_repository.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **Player** (7 connections) — `server/persistence/repositories/health_repository.py`
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository_cold_resistance.py** (5 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **.damage_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._update_player_health_inner()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **UUID** (5 connections) — `server/persistence/repositories/health_repository.py`
- **.heal_player()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **_stats_int()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **test_cold_damage_resistance_reduces_damage()** (3 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **test_damage_defaults_current_dp_to_20_when_missing()** (3 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **._calculate_effective_damage()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **Exception** (3 connections) — `server/persistence/repositories/health_repository.py`
- **Tests for cold damage resistance in HealthRepository.** (1 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **Cold resistance should reduce incoming cold-type damage before persistence.** (1 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **Missing current_dp should use base investigator fallback to avoid inflated healt** (1 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **Log critical damage persistence failure.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Execute atomic health update via update_player_health procedure.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Damage a player and persist health changes atomically.          Args:** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Heal a player and persist health changes atomically.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Core heal logic without error handling wrapper.** (1 connections) — `server/persistence/repositories/health_repository.py`
- *... and 6 more nodes in this community*

## Relationships

- [[NPC Admin API]] (13 shared connections)
- [[Player Domain Model]] (5 shared connections)
- [[Persistence Item Instance]] (1 shared connections)

## Source Files

- `server/persistence/repositories/health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`

## Audit Trail

- EXTRACTED: 101 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
