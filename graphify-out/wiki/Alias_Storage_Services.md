# Alias Storage Services

> 117 nodes

## Key Concepts

- **test_alias_storage.py** (65 connections) — `server/tests/unit/test_alias_storage.py`
- **_get_alias_validator()** (8 connections) — `server/alias_storage.py`
- **Path** (6 connections)
- **alias_storage()** (6 connections) — `server/tests/unit/test_alias_storage.py`
- **.get_alias_storage()** (4 connections) — `server/realtime/request_context.py`
- **temp_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_without_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_creates_directory()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_custom_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_no_validator()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_with_validator()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_validator_caching()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_validator_import_failure()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_validator_creation_failure()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_file_path()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_load_alias_data_nonexistent_file()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_load_alias_data_existing_file()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_load_alias_data_invalid_json()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_load_alias_data_io_error()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_save_alias_data_success()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_save_alias_data_io_error()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_player_aliases_empty()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_player_aliases_with_aliases()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- *... and 92 more nodes in this community*

## Relationships

- [Player Schema Converter](Player_Schema_Converter.md) (7 shared connections)
- [Alias Expansion Logic](Alias_Expansion_Logic.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [WebSocket Auth Integration](WebSocket_Auth_Integration.md) (2 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (1 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/realtime/request_context.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 262 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*