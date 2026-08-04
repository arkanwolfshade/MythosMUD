# alias storage rationale

> 115 nodes

## Key Concepts

- **test_alias_storage.py** (66 connections) — `server/tests/unit/test_alias_storage.py`
- **Path** (6 connections)
- **temp_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **sample_alias2()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_without_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_creates_directory()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_file_path()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_custom_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_no_validator()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_with_validator()** (3 connections) — `server/tests/unit/test_alias_storage.py`
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
- *... and 90 more nodes in this community*

## Relationships

- [alias models rationale](alias_models_rationale.md) (6 shared connections)
- [commands party examples](commands_party_examples.md) (5 shared connections)
- [commands recovery lucidity](commands_recovery_lucidity.md) (4 shared connections)
- [request context realtime](request_context_realtime.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 254 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*