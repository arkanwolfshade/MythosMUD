# Health Cold Resistance

> 27 nodes · cohesion 0.12

## Key Concepts

- **HealthRepository** (20 connections) — `server/persistence/repositories/health_repository.py`
- **health_repository.py** (16 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (8 connections) — `server/persistence/repositories/health_repository.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **Player** (6 connections)
- **.damage_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._update_player_health_inner()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **.heal_player()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **UUID** (4 connections)
- **_stats_int()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **._calculate_effective_damage()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **Exception** (2 connections)
- **Health repository for async persistence operations.  This module provides asyn** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Log critical damage persistence failure.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Execute atomic health update via update_player_health procedure.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Damage a player and persist health changes atomically.          Args:** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Heal a player and persist health changes atomically.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Core heal logic without error handling wrapper.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Update player current_dp field atomically.          Args:             player_** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Convert stat values to int with a safe fallback.** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Repository for player health persistence operations.      Handles damage, heal** (1 connections) — `server/persistence/repositories/health_repository.py`
- **Initialize the health repository.          Args:             event_bus: Optio** (1 connections) — `server/persistence/repositories/health_repository.py`
- *... and 2 more nodes in this community*

## Relationships

- [Realtime Connection Impl](Realtime_Connection_Impl.md) (13 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (7 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (1 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/health_repository.py`

## Audit Trail

- EXTRACTED: 104 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*