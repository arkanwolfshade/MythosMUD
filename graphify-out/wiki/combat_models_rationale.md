# combat models rationale

> 183 nodes

## Key Concepts

- **Player** (236 connections) — `server/models/player.py`
- **player.py** (89 connections) — `server/models/player.py`
- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository.py** (19 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **test_inventory_commands_persistence_helpers.py** (12 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **test_procedures_return_shape.py** (11 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **test_add_player_effect_generates_id()** (7 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **_stats_int()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **Player** (6 connections)
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **.damage_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **.heal_player()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **test_cold_damage_resistance_reduces_damage()** (4 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **test_damage_defaults_current_dp_to_20_when_missing()** (4 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **_convert_legacy_stats_string()** (3 connections) — `server/models/player.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **._calculate_effective_damage()** (3 connections) — `server/persistence/repositories/health_repository.py`
- **mock_player()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **test_clone_inventory()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **test_persist_player_success()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **test_get_player_by_name_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_player_by_id_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- *... and 158 more nodes in this community*

## Relationships

- [command factories communication](command_factories_communication.md) (47 shared connections)
- [Database Config](Database_Config.md) (31 shared connections)
- [Loot Generation](Loot_Generation.md) (17 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (15 shared connections)
- [models player rationale](models_player_rationale.md) (14 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (12 shared connections)
- [inventory commands command](inventory_commands_command.md) (11 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (11 shared connections)
- [schemas invite user](schemas_invite_user.md) (11 shared connections)
- [player death service](player_death_service.md) (10 shared connections)
- [profession models rationale](profession_models_rationale.md) (10 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (10 shared connections)

## Source Files

- `server/models/player.py`
- `server/persistence/repositories/health_repository.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- `server/tests/unit/persistence/test_player_repository.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 644 (83%)
- INFERRED: 130 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*