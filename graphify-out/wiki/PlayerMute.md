# PlayerMute

> 51 nodes

## Key Concepts

- **PlayerMute** (26 connections) — `server/persistence/repositories/player_mute_repository.py`
- **PlayerMuteRepository** (19 connections) — `server/persistence/repositories/player_mute_repository.py`
- **test_player_aliases_and_mutes_db.py** (14 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **test_game_bundle_mute_load.py** (14 connections) — `server/tests/unit/container/test_game_bundle_mute_load.py`
- **test_player_mute_repository.py** (14 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **_Players** (12 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **_Session** (11 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **_Repo** (8 connections) — `server/tests/unit/container/test_game_bundle_mute_load.py`
- **test_database_errors_raise_database_error()** (7 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **test_delete_reports_whether_a_row_was_removed()** (7 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **test_load_active_maps_rows()** (7 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **test_upsert_binds_stringified_ids_and_commits()** (7 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **_Result** (6 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **test_load_player_mutes_fills_user_manager_index()** (6 connections) — `server/tests/unit/container/test_game_bundle_mute_load.py`
- **_use_session()** (6 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **test_global_mute_survives_restart_without_muter_online()** (5 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **test_mute_repository_upsert_replaces_and_filters_expired()** (5 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **test_load_player_mutes_database_error_starts_with_no_mutes()** (5 connections) — `server/tests/unit/container/test_game_bundle_mute_load.py`
- **asyncio** (5 connections)
- **MonkeyPatch** (5 connections)
- **test_alias_crud_round_trip()** (4 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **test_alias_rejected_for_unknown_player_and_over_limit()** (4 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **test_aliases_are_per_player_and_deleted_by_id()** (4 connections) — `server/tests/integration/test_player_aliases_and_mutes_db.py`
- **asyncio** (4 connections)
- **.load_active()** (3 connections) — `server/tests/unit/container/test_game_bundle_mute_load.py`
- *... and 26 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (24 shared connections)
- [UserManager](UserManager.md) (8 shared connections)
- [test_user_manager.py](test_user_manager.py.md) (8 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (1 shared connections)
- [session_factory](session_factory.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_mute_repository.py`
- `server/tests/integration/test_player_aliases_and_mutes_db.py`
- `server/tests/unit/container/test_game_bundle_mute_load.py`
- `server/tests/unit/persistence/repositories/test_player_mute_repository.py`

## Audit Trail

- EXTRACTED: 125 (85%)
- INFERRED: 22 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*