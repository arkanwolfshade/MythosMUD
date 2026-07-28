# Server Infrastructure (8)

> 43 nodes

## Key Concepts

- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
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
- **Test get_player_by_name delegates to PlayerRepository.** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **Test get_user_by_username_case_insensitive with successful lookup.** (2 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- *... and 18 more nodes in this community*

## Relationships

- [Server Services](Server_Services.md) (10 shared connections)
- [Server Admin](Server_Admin.md) (6 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (4 shared connections)
- [Server Persistence](Server_Persistence.md) (4 shared connections)
- [Server Models (28)](Server_Models_%2828%29.md) (3 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_async_persistence_core.py`

## Audit Trail

- EXTRACTED: 108 (92%)
- INFERRED: 9 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*