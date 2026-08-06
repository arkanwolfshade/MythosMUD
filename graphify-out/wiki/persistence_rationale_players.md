# persistence rationale players

> 309 nodes

## Key Concepts

- **Player** (240 connections) — `server/models/player.py`
- **test_player_respawn_service.py** (54 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **test_async_persistence_delegates.py** (35 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **test_health_repository.py** (19 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **.update_player_health()** (8 connections) — `server/persistence/repositories/health_repository.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **reset_async_persistence()** (6 connections) — `server/async_persistence.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **_stats_int()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **Player** (6 connections)
- **._heal_player_inner()** (6 connections) — `server/persistence/repositories/health_repository.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **._log_damage_error()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **._update_player_health_inner()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **.damage_player()** (5 connections) — `server/persistence/repositories/health_repository.py`
- **quest_seed_data()** (5 connections) — `server/tests/integration/test_quest_flow.py`
- **.is_alive()** (4 connections) — `server/models/player.py`
- *... and 284 more nodes in this community*

## Relationships

- [player room realtime](player_room_realtime.md) (54 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (53 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (29 shared connections)
- [player event handlers](player_event_handlers.md) (22 shared connections)
- [player service game](player_service_game.md) (13 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (9 shared connections)
- [player cache rationale](player_cache_rationale.md) (8 shared connections)
- [add used user](add_used_user.md) (7 shared connections)
- [profession models rationale](profession_models_rationale.md) (6 shared connections)
- [task registry app](task_registry_app.md) (5 shared connections)
- [combat npc service](combat_npc_service.md) (5 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (4 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/models/player.py`
- `server/persistence/repositories/health_repository.py`
- `server/services/player_respawn_service.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- `server/tests/unit/services/test_player_death_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 952 (86%)
- INFERRED: 156 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*