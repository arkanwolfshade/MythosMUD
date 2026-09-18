# Player Creation Service

> 276 nodes

## Key Concepts

- **Player** (286 connections) — `server/models/player.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **asyncio** (23 connections)
- **test_health_repository.py** (19 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **_stats_int()** (13 connections) — `server/models/player.py`
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **row_to_player()** (10 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **test_procedures_return_shape.py** (10 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **asyncio** (9 connections)
- **.create_player_with_stats()** (8 connections) — `server/game/player_creation_service.py`
- **.create_player()** (7 connections) — `server/game/player_creation_service.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.update_player_health()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **test_add_player_effect_generates_id()** (7 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **PlayerCreationService** (6 connections) — `server/game/player_creation_service.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **_stats_int()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **._resolve_tutorial_start_room()** (5 connections) — `server/game/player_creation_service.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- *... and 251 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (54 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (15 shared connections)
- [Community 302](Community_302.md) (14 shared connections)
- [Community 101](Community_101.md) (13 shared connections)
- [Community 289](Community_289.md) (10 shared connections)
- [Community 528](Community_528.md) (10 shared connections)
- [Community 157](Community_157.md) (9 shared connections)
- [Catatonia Status Checks](Catatonia_Status_Checks.md) (8 shared connections)
- [Community 290](Community_290.md) (7 shared connections)
- [Community 1142](Community_1142.md) (7 shared connections)
- [Community 70](Community_70.md) (6 shared connections)
- [Community 136](Community_136.md) (5 shared connections)

## Source Files

- `server/game/player_creation_service.py`
- `server/models/player.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`

## Audit Trail

- EXTRACTED: 580 (84%)
- INFERRED: 112 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*