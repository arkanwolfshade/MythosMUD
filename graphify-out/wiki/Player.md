# Player

> 221 nodes

## Key Concepts

- **Player** (281 connections) — `server/models/player.py`
- **test_player_model.py** (47 connections) — `server/tests/unit/models/test_player_model.py`
- **test_async_persistence_core.py** (41 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **asyncio** (24 connections)
- **test_health_repository.py** (19 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **asyncio** (9 connections)
- **quest_seed_data()** (8 connections) — `server/tests/integration/test_quest_flow.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **.damage_player()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **_stats_int()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **.heal_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._update_player_health_inner()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **test_cold_damage_resistance_reduces_damage()** (5 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **test_damage_defaults_current_dp_to_20_when_missing()** (5 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **Player** (5 connections)
- **_convert_legacy_stats_string()** (4 connections) — `server/models/player.py`
- **test_clear_player_inventory_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_active_players_by_user_id_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_player_by_id_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_player_by_name_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- *... and 196 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (54 shared connections)
- [alias_storage.py](alias_storage.py.md) (29 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (18 shared connections)
- [command_result_text](command_result_text.md) (15 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (12 shared connections)
- [coerce_int](coerce_int.md) (11 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (8 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (6 shared connections)
- [session](session.md) (4 shared connections)
- [combat_assist.py](combat_assist.py.md) (4 shared connections)
- [test_player_repository_room.py](test_player_repository_room.py.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)

## Source Files

- `server/models/player.py`
- `server/persistence/repositories/health_repository.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`

## Audit Trail

- EXTRACTED: 451 (76%)
- INFERRED: 143 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*