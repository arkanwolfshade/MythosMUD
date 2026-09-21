# Player

> 240 nodes

## Key Concepts

- **Player** (238 connections) — `server/models/player.py`
- **coerce_int()** (67 connections) — `server/utils/int_coercion.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **inventory_get_command.py** (30 connections) — `server/commands/inventory_get_command.py`
- **test_inventory_get_command.py** (25 connections) — `server/tests/unit/commands/test_inventory_get_command.py`
- **int_coercion.py** (24 connections) — `server/utils/int_coercion.py`
- **test_health_repository.py** (19 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **health_repository.py** (17 connections) — `server/persistence/repositories/health_repository.py`
- **handle_get_command()** (16 connections) — `server/commands/inventory_get_command.py`
- **_handle_get_from_room()** (16 connections) — `server/commands/inventory_get_command.py`
- **_get_from_container_path()** (15 connections) — `server/commands/inventory_get_command.py`
- **_stats_int()** (14 connections) — `server/models/player.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **test_inventory_command_coercion.py** (12 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **_get_transfer_out_of_container()** (11 connections) — `server/commands/inventory_get_command.py`
- **asyncio** (10 connections)
- **asyncio** (9 connections)
- **GetCommandRuntime** (8 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (8 connections) — `server/commands/inventory_get_command.py`
- **quest_seed_data()** (8 connections) — `server/tests/integration/test_quest_flow.py`
- **_get_route_after_validation()** (7 connections) — `server/commands/inventory_get_command.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- *... and 215 more nodes in this community*

## Relationships

- [models/player.py](models-player.py.md) (35 shared connections)
- [inventory_pickup_command.py](inventory_pickup_command.py.md) (27 shared connections)
- [command_result_text](command_result_text.md) (21 shared connections)
- [DatabaseError](DatabaseError.md) (20 shared connections)
- [get_logger](get_logger.md) (15 shared connections)
- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) (11 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (9 shared connections)
- [LucidityService](LucidityService.md) (9 shared connections)
- [Profession](Profession.md) (9 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (7 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (6 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (6 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_get_command.py`
- `server/models/player.py`
- `server/persistence/repositories/health_repository.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/tests/unit/commands/test_inventory_get_command.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 589 (81%)
- INFERRED: 134 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*