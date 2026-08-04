# combat models rationale

> 251 nodes

## Key Concepts

- **Player** (236 connections) — `server/models/player.py`
- **player.py** (89 connections) — `server/models/player.py`
- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **PositionState** (20 connections) — `server/models/game.py`
- **test_health_repository.py** (19 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **test_procedures_return_shape.py** (11 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_lucidity_round_trip.py** (10 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **test_lucidity_adjustment_round_trip()** (7 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **test_add_player_effect_generates_id()** (7 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **_stats_int()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **Player** (6 connections)
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **.damage_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **.heal_player()** (4 connections) — `server/persistence/repositories/health_repository.py`
- **InventoryPayload** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **test_cold_damage_resistance_reduces_damage()** (4 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **test_damage_defaults_current_dp_to_20_when_missing()** (4 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **_convert_legacy_stats_string()** (3 connections) — `server/models/player.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/health_repository.py`
- *... and 226 more nodes in this community*

## Relationships

- [commands inventory command](commands_inventory_command.md) (18 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (17 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (14 shared connections)
- [npc population stats](npc_population_stats.md) (13 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (13 shared connections)
- [nats services service](nats_services_service.md) (12 shared connections)
- [models player rationale](models_player_rationale.md) (12 shared connections)
- [shutdown command commands](shutdown_command_commands.md) (12 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (11 shared connections)
- [world models rationale](world_models_rationale.md) (11 shared connections)
- [schemas invite user](schemas_invite_user.md) (11 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (10 shared connections)

## Source Files

- `server/models/game.py`
- `server/models/player.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 866 (87%)
- INFERRED: 129 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*