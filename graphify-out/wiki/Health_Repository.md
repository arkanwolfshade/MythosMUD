# Health Repository

> 19 nodes

## Key Concepts

- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **.damage_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._update_player_health_inner()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **Player** (5 connections)
- **.heal_player()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **._calculate_effective_damage()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **UUID** (3 connections)
- **Exception** (1 connections)
- **Log critical damage persistence failure.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Execute atomic health update via update_player_health procedure.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Damage a player and persist health changes atomically. Args: player: Player to…** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Heal a player and persist health changes atomically.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Core heal logic without error handling wrapper.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Update player current_dp field atomically. Args: player_id: Player UUID or…** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Calculate effective damage after applying simple resistance rules. Currently…** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Core damage logic without error handling wrapper.** (1 connections) — `server/persistence/repositories/health_repository.py`

## Relationships

- [Player Model & Migrations](Player_Model_&_Migrations.md) (11 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (2 shared connections)

## Source Files

- `server/persistence/repositories/health_repository.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*