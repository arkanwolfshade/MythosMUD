# Alias Storage Layer

> 66 nodes · cohesion 0.02

## Key Concepts

- **test_alias_storage.py** (66 connections) — `server/tests/unit/test_alias_storage.py`
- **Path** (7 connections)
- **alias.py** (6 connections) — `server/models/alias.py`
- **alias_storage()** (6 connections) — `server/tests/unit/test_alias_storage.py`
- **temp_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_creates_directory()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_without_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_custom_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_file_path()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_no_validator()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_with_validator()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_add_alias_new()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_io_error()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_nonexistent_file()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_success()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_clear_aliases()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_create_alias_invalid_command()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_create_alias_invalid_name()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_create_alias_limit_reached()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_create_alias_success()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_delete_player_aliases_existing()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_delete_player_aliases_io_error()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_delete_player_aliases_nonexistent()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- *... and 41 more nodes in this community*

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (9 shared connections)
- [UI Panel Manager](UI_Panel_Manager.md) (7 shared connections)
- [Server Config Loading](Server_Config_Loading.md) (4 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (2 shared connections)
- [WebSocket Request Context](WebSocket_Request_Context.md) (1 shared connections)

## Source Files

- `server/models/alias.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 204 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*