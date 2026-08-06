# game weapon player

> 130 nodes

## Key Concepts

- **Player** (240 connections) — `server/models/player.py`
- **HealthRepository** (31 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository.py** (19 connections) — `server/tests/unit/persistence/repositories/test_health_repository.py`
- **health_repository.py** (17 connections) — `server/persistence/repositories/health_repository.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **test_inventory_commands_persistence_helpers.py** (12 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **.update_player_health()** (8 connections) — `server/persistence/repositories/health_repository.py`
- **.respawn_player_from_delirium_by_user_id()** (7 connections) — `server/game/player_respawn_wrapper.py`
- **._damage_player_inner()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
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
- **.is_mortally_wounded()** (4 connections) — `server/models/player.py`
- **.is_dead()** (4 connections) — `server/models/player.py`
- **.get_health_state()** (4 connections) — `server/models/player.py`
- *... and 105 more nodes in this community*

## Relationships

- [player room realtime](player_room_realtime.md) (45 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (43 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (22 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (14 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (13 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (11 shared connections)
- [level curve game](level_curve_game.md) (9 shared connections)
- [add used user](add_used_user.md) (8 shared connections)
- [player service game](player_service_game.md) (8 shared connections)
- [player cache rationale](player_cache_rationale.md) (7 shared connections)
- [room renderer functions](room_renderer_functions.md) (5 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (5 shared connections)

## Source Files

- `server/game/player_respawn_wrapper.py`
- `server/models/player.py`
- `server/persistence/repositories/health_repository.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/persistence/repositories/test_health_repository.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 488 (78%)
- INFERRED: 140 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*