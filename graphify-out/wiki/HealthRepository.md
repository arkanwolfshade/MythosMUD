# HealthRepository

> 25 nodes

## Key Concepts

- **HealthRepository** (20 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (8 connections) — `server/persistence/repositories/health_repository.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **Player** (6 connections)
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._update_player_health_inner()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **.damage_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **_stats_int()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **UUID** (4 connections)
- **.heal_player()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **._calculate_effective_damage()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **Exception** (2 connections)
- **Convert stat values to int with a safe fallback.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Repository for player health persistence operations.      Handles damage, heal** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Initialize the health repository.          Args:             event_bus: Optio** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Calculate effective damage after applying simple resistance rules.          Cu** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Core damage logic without error handling wrapper.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Log critical damage persistence failure.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Execute atomic health update via update_player_health procedure.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Damage a player and persist health changes atomically.          Args:** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Heal a player and persist health changes atomically.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Core heal logic without error handling wrapper.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Update player current_dp field atomically.          Args:             player_** (1 connections) — `server/persistence/repositories/health_repository.py`

## Relationships

- [real time](real_time.md) (12 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (1 shared connections)
- [spell registry](spell_registry.md) (1 shared connections)
- [world](world.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/health_repository.py`

## Audit Trail

- EXTRACTED: 87 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*