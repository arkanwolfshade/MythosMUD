# test alias storage

> 121 nodes

## Key Concepts

- **test_alias_storage.py** (66 connections) — `server/tests/unit/test_alias_storage.py`
- **Path** (6 connections)
- **alias_storage()** (6 connections) — `server/tests/unit/test_alias_storage.py`
- **.get_alias_storage()** (4 connections) — `server/realtime/request_context.py`
- **temp_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **sample_alias()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_without_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_creates_directory()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_file_path()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_add_alias_updates_existing()** (3 connections) — `server/tests/unit/test_alias_storage.py`
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
- *... and 96 more nodes in this community*

## Relationships

- [test magic commands](test_magic_commands.md) (6 shared connections)
- [test npc instance service](test_npc_instance_service.md) (6 shared connections)
- [AuthSlice](AuthSlice.md) (5 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/request_context.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 267 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*