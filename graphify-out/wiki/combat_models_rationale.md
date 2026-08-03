# combat models rationale

> 168 nodes

## Key Concepts

- **Player** (203 connections) — `server/models/player.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.is_alive()** (4 connections) — `server/models/player.py`
- **.is_mortally_wounded()** (4 connections) — `server/models/player.py`
- **.is_dead()** (4 connections) — `server/models/player.py`
- **.get_health_state()** (4 connections) — `server/models/player.py`
- **.get_combat_stats()** (4 connections) — `server/models/player.py`
- **.get_health_percentage()** (4 connections) — `server/models/player.py`
- **test_get_player_by_name_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_player_by_id_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_players_by_user_id_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_active_players_by_user_id_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_save_player_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_list_players_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_players_in_room_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_save_players_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_player_creation()** (3 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_defaults()** (3 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_get_stats()** (3 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_get_stats_default()** (3 connections) — `server/tests/unit/models/test_player_model.py`
- *... and 143 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (21 shared connections)
- [world models rationale](world_models_rationale.md) (21 shared connections)
- [command inventory factories](command_inventory_factories.md) (19 shared connections)
- [schemas invite user](schemas_invite_user.md) (10 shared connections)
- [models player rationale](models_player_rationale.md) (9 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (6 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (5 shared connections)
- [alias command models](alias_command_models.md) (5 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (5 shared connections)
- [commands inventory command](commands_inventory_command.md) (4 shared connections)
- [inventory commands command](inventory_commands_command.md) (3 shared connections)
- [target resolution service](target_resolution_service.md) (3 shared connections)

## Source Files

- `server/models/player.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/test_player_repository.py`
- `server/tests/unit/services/test_player_death_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 505 (85%)
- INFERRED: 92 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*