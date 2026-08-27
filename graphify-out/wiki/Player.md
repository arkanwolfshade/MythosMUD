# Player

> 226 nodes

## Key Concepts

- **Player** (232 connections) — `server/models/player.py`
- **coerce_int()** (51 connections) — `server/utils/int_coercion.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository.py** (20 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **int_coercion.py** (17 connections) — `server/utils/int_coercion.py`
- **test_player_repository_room.py** (15 connections) — `server/tests/unit/persistence/test_player_repository_room.py`
- **_stats_int()** (14 connections) — `server/models/player.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **validate_and_fix_player_room()** (13 connections) — `server/persistence/repositories/player_repository_room.py`
- **test_inventory_command_coercion.py** (13 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_inventory_commands_persistence_helpers.py** (13 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **should_skip_room_validation()** (10 connections) — `server/persistence/repositories/player_repository_room.py`
- **validate_and_fix_player_room_with_persistence()** (10 connections) — `server/persistence/repositories/player_repository_room.py`
- **_player()** (9 connections) — `server/tests/unit/persistence/test_player_repository_room.py`
- **player_repository_room.py** (9 connections) — `server/persistence/repositories/player_repository_room.py`
- **asyncio** (9 connections)
- **test_health_repository_cold_resistance.py** (8 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **_stats_int()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- *... and 201 more nodes in this community*

## Relationships

- [models/player.py](models-player.py.md) (51 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (23 shared connections)
- [DatabaseError](DatabaseError.md) (22 shared connections)
- [inventory_pickup_command.py](inventory_pickup_command.py.md) (20 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (13 shared connections)
- [command_result_text](command_result_text.md) (13 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (9 shared connections)
- [pytest.md](pytest.md.md) (7 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (7 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (5 shared connections)
- [test_look_container_helpers.py](test_look_container_helpers.py.md) (5 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)

## Source Files

- `server/models/player.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/player_repository_room.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- `server/tests/unit/persistence/test_player_repository_room.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 506 (81%)
- INFERRED: 115 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*