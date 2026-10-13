# Community 385

> 46 nodes

## Key Concepts

- **HealthRepository** (30 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository.py** (19 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **asyncio** (9 connections)
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **.damage_player()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **_stats_int()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **.heal_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._update_player_health_inner()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **test_cold_damage_resistance_reduces_damage()** (5 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **test_damage_defaults_current_dp_to_20_when_missing()** (5 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **Player** (5 connections)
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

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (16 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (11 shared connections)
- [Community 226](Community_226.md) (2 shared connections)
- [Community 78](Community_78.md) (2 shared connections)
- [Community 51](Community_51.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/health_repository.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`

## Audit Trail

- EXTRACTED: 85 (75%)
- INFERRED: 28 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*