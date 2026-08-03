# persistence core infrastructure

> 50 nodes

## Key Concepts

- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_async_persistence_layer_init_skip_room_cache()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_async_persistence_layer_init_with_room_cache()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_async_persistence_layer_init_deprecated_params()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_player_by_name_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_player_by_id_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_players_by_user_id_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_active_players_by_user_id_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_user_by_username_case_insensitive_success()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_save_player_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_list_players_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_players_in_room_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_save_players_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_close()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_player_by_name_not_found()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_user_by_username_case_insensitive_not_found()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_room_by_id_delegates()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_room_by_id_not_found()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_list_rooms_delegates()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_async_list_rooms_delegates()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_delete_player_delegates()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_update_player_last_active_delegates()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_update_player_last_active_none()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_empty()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_profession_by_id_not_found()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- *... and 25 more nodes in this community*

## Relationships

- [Async Query Helpers](Async_Query_Helpers.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (5 shared connections)
- [npc populate databases](npc_populate_databases.md) (4 shared connections)
- [models profession available](models_profession_available.md) (3 shared connections)
- [auth users rationale](auth_users_rationale.md) (3 shared connections)
- [world models rationale](world_models_rationale.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_core.py`

## Audit Trail

- EXTRACTED: 117 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*