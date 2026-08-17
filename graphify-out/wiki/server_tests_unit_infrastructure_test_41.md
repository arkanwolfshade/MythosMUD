# server tests unit infrastructure test

> 60 nodes

## Key Concepts

- **test_async_persistence_core.py** (41 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **asyncio** (23 connections)
- **test_get_active_players_by_user_id_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_player_by_id_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_player_by_name_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_players_by_user_id_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_players_in_room_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_profession_by_id_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_database_error()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_os_error()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_success()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_user_by_username_case_insensitive_database_error()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_user_by_username_case_insensitive_success()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_list_players_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_save_player_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_save_players_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_async_list_rooms_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_async_persistence_layer_init_deprecated_params()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_async_persistence_layer_init_skip_room_cache()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_async_persistence_layer_init_with_room_cache()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_close()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_delete_player_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_player_by_name_not_found()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_profession_by_id_not_found()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_empty()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- *... and 35 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (13 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (4 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (4 shared connections)
- [server models profession profession](server_models_profession_profession.md) (3 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (3 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_core.py`

## Audit Trail

- EXTRACTED: 93 (85%)
- INFERRED: 17 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*