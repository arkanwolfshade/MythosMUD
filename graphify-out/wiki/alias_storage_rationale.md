# alias storage rationale

> 104 nodes

## Key Concepts

- **test_alias_storage.py** (66 connections) — `server/tests/unit/test_alias_storage.py`
- **sample_alias2()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_without_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_creates_directory()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_validator_caching()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_validator_import_failure()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_validator_creation_failure()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_file_path_rejects_traversal()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_load_alias_data_nonexistent_file()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_load_alias_data_existing_file()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_load_alias_data_invalid_json()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_load_alias_data_io_error()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_save_alias_data_success()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_save_alias_data_io_error()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_player_aliases_empty()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_player_aliases_with_aliases()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_player_aliases_with_timestamps()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_player_aliases_invalid_alias_data()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_save_player_aliases()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_add_alias_new()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_remove_alias_existing()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_remove_alias_nonexistent()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_remove_alias_case_insensitive()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- *... and 79 more nodes in this community*

## Relationships

- [commands admin mute](commands_admin_mute.md) (10 shared connections)
- [player event realtime](player_event_realtime.md) (6 shared connections)
- [alias models rationale](alias_models_rationale.md) (5 shared connections)
- [skill game service](skill_game_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 228 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*