# persistence core infrastructure

> 60 nodes

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
- **test_get_user_by_username_case_insensitive_database_error()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_save_player_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_list_players_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_players_in_room_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_save_players_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_success()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_database_error()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_os_error()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_profession_by_id_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_close()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_player_by_name_not_found()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_user_by_username_case_insensitive_not_found()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_room_by_id_delegates()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_room_by_id_not_found()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_list_rooms_delegates()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_async_list_rooms_delegates()** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- *... and 35 more nodes in this community*

## Relationships

- [world models rationale](world_models_rationale.md) (11 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [profession models rationale](profession_models_rationale.md) (3 shared connections)
- [Exception Containers](Exception_Containers.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [admin auth service](admin_auth_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_core.py`

## Audit Trail

- EXTRACTED: 132 (91%)
- INFERRED: 13 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*