# test_aggression.py

> 51 nodes · cohesion 0.07

## Key Concepts

- **PlayerMute** (26 connections) — `server/persistence/repositories/player_mute_repository.py`
- **player_mute_repository.py** (21 connections) — `server/persistence/repositories/player_mute_repository.py`
- **PlayerMuteRepository** (19 connections) — `server/persistence/repositories/player_mute_repository.py`
- **test_game_bundle_mute_load.py** (14 connections) — `server/tests/unit/container/test_game_bundle_mute_load.py`
- **test_player_mute_repository.py** (14 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **_Session** (11 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **_Repo** (8 connections) — `server/tests/unit/container/test_game_bundle_mute_load.py`
- **.delete()** (7 connections) — `server/persistence/repositories/player_mute_repository.py`
- **test_database_errors_raise_database_error()** (7 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **test_delete_reports_whether_a_row_was_removed()** (7 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **test_load_active_maps_rows()** (7 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **test_upsert_binds_stringified_ids_and_commits()** (7 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **test_load_player_mutes_fills_user_manager_index()** (6 connections) — `server/tests/unit/container/test_game_bundle_mute_load.py`
- **_Result** (6 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **_use_session()** (6 connections) — `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- **test_load_player_mutes_database_error_starts_with_no_mutes()** (5 connections) — `server/tests/unit/container/test_game_bundle_mute_load.py`
- **MonkeyPatch** (5 connections)
- **_opt_str()** (4 connections) — `server/persistence/repositories/player_mute_repository.py`
- **UUID** (4 connections)
- **_row_to_mute()** (4 connections) — `server/persistence/repositories/player_mute_repository.py`
- **asyncio** (4 connections)
- **_as_uuid()** (3 connections) — `server/persistence/repositories/player_mute_repository.py`
- **_MuteRow** (3 connections) — `server/persistence/repositories/player_mute_repository.py`
- **asyncio** (3 connections)
- **.load_active()** (3 connections) — `server/tests/unit/container/test_game_bundle_mute_load.py`
- *... and 26 more nodes in this community*

## Relationships

- [endpoints.py](endpoints.py.md) (10 shared connections)
- [asyncio](asyncio.md) (10 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (8 shared connections)
- [Room](Room.md) (6 shared connections)
- [MythosMUD Database Placement](MythosMUD_Database_Placement.md) (5 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (5 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (5 shared connections)
- [AttributeError](AttributeError.md) (4 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)
- [test_party_service.py](test_party_service.py.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_mute_repository.py`
- `server/tests/unit/container/test_game_bundle_mute_load.py`
- `server/tests/unit/persistence/repositories/test_player_mute_repository.py`
- `server/tests/unit/services/test_user_manager.py`

## Audit Trail

- EXTRACTED: 131 (89%)
- INFERRED: 17 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*