# Player

> 388 nodes

## Key Concepts

- **Player** (238 connections) — `server/models/player.py`
- **AsyncPersistenceLayer** (177 connections) — `server/async_persistence.py`
- **models/player.py** (105 connections) — `server/models/player.py`
- **models/user.py** (67 connections) — `server/models/user.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **test_async_persistence_delegates.py** (34 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **player_event_handlers_respawn.py** (30 connections) — `server/realtime/player_event_handlers_respawn.py`
- **asyncio** (22 connections)
- **Player** (20 connections)
- **test_health_repository.py** (19 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_player_effect_repository.py** (17 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **PlayerEffect** (15 connections) — `server/models/player_effect.py`
- **UUID** (15 connections)
- **.get_stats()** (13 connections) — `server/models/player.py`
- **protocols.py** (13 connections) — `server/persistence/protocols.py`
- **test_inventory_commands_persistence_helpers.py** (12 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **test_procedures_return_shape.py** (11 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **player_effect.py** (10 connections) — `server/models/player_effect.py`
- **asyncio** (9 connections)
- **test_add_player_effect_generates_id()** (8 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **asyncio** (8 connections)
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- *... and 363 more nodes in this community*

## Relationships

- [async_persistence.py](async_persistence.py.md) (32 shared connections)
- [get_logger](get_logger.md) (20 shared connections)
- [get_session_maker](get_session_maker.md) (20 shared connections)
- [User](User.md) (19 shared connections)
- [server/models/__init__.py](server-models-__init__.py.md) (16 shared connections)
- [inventory_pickup_command.py](inventory_pickup_command.py.md) (16 shared connections)
- [test_async_persistence_core.py](test_async_persistence_core.py.md) (15 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (15 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (15 shared connections)
- [command_result_text](command_result_text.md) (15 shared connections)
- [coerce_int](coerce_int.md) (14 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (13 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/models/player.py`
- `server/models/player_effect.py`
- `server/models/user.py`
- `server/persistence/protocols.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- `server/tests/unit/persistence/test_player_effect_repository.py`

## Audit Trail

- EXTRACTED: 970 (85%)
- INFERRED: 170 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*