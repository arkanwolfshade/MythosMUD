# HealthRepository

> 44 nodes

## Key Concepts

- **HealthRepository** (20 connections) — `server/persistence/repositories/health_repository.py`
- **.__init__()** (13 connections) — `server/async_persistence.py`
- **RoomRepository** (12 connections) — `server/persistence/repositories/room_repository.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **.damage_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._update_player_health_inner()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **Player** (5 connections)
- **.heal_player()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **_stats_int()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **test_cold_damage_resistance_reduces_damage()** (4 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **test_damage_defaults_current_dp_to_20_when_missing()** (4 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **._calculate_effective_damage()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/room_repository.py`
- **UUID** (3 connections)
- **.get_room_by_id()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.list_rooms()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.save_room()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.save_rooms()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **asyncio** (2 connections)
- **Exception** (1 connections)
- **Initialize the async persistence layer. This facade delegates to focused async…** (1 connections) — `server/async_persistence.py`
- *... and 19 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [log_and_raise](log_and_raise.md) (8 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (3 shared connections)
- [Room](Room.md) (1 shared connections)
- [item_instance_persistence.py](item_instance_persistence.py.md) (1 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (1 shared connections)
- [Profession](Profession.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/room_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`

## Audit Trail

- EXTRACTED: 84 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*