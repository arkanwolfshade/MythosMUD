# dialogue definitions admin

> 45 nodes

## Key Concepts

- **__init__.py** (30 connections) — `server/persistence/repositories/__init__.py`
- **HealthRepository** (20 connections) — `server/persistence/repositories/health_repository.py`
- **health_repository.py** (16 connections) — `server/persistence/repositories/health_repository.py`
- **RoomRepository** (12 connections) — `server/persistence/repositories/room_repository.py`
- **.update_player_health()** (8 connections) — `server/persistence/repositories/health_repository.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **Player** (6 connections)
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._update_player_health_inner()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **.damage_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **_stats_int()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **UUID** (4 connections)
- **.heal_player()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **test_cold_damage_resistance_reduces_damage()** (4 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **test_damage_defaults_current_dp_to_20_when_missing()** (4 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **._calculate_effective_damage()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **Exception** (2 connections)
- **.get_room_by_id()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.list_rooms()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.save_room()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.save_rooms()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **Repository modules for async persistence layer.** (1 connections) — `server/persistence/repositories/__init__.py`
- *... and 20 more nodes in this community*

## Relationships

- [npc populate databases](npc_populate_databases.md) (14 shared connections)
- [NATS Messaging](NATS_Messaging.md) (8 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (5 shared connections)
- [persistence container item](persistence_container_item.md) (3 shared connections)
- [player model models](player_model_models.md) (3 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (3 shared connections)
- [persistence container extended](persistence_container_extended.md) (2 shared connections)
- [dialogue definition persistence](dialogue_definition_persistence.md) (2 shared connections)
- [task registry app](task_registry_app.md) (2 shared connections)
- [effect player repository](effect_player_repository.md) (2 shared connections)
- [player room persistence](player_room_persistence.md) (2 shared connections)

## Source Files

- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/room_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`

## Audit Trail

- EXTRACTED: 175 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*