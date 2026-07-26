# test_alias_storage.py

> 109 nodes · cohesion 0.02

## Key Concepts

- **test_alias_storage.py** (65 connections) — `server/tests/unit/test_alias_storage.py`
- **alias.py** (6 connections) — `server/models/alias.py`
- **alias_storage()** (6 connections) — `server/tests/unit/test_alias_storage.py`
- **Path** (6 connections)
- **temp_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_creates_directory()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_without_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_custom_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
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
- **test_get_alias_case_insensitive()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- *... and 84 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (9 shared connections)
- [Alias](Alias.md) (7 shared connections)
- [SchemaValidator](SchemaValidator.md) (4 shared connections)
- [__init__.py](__init__.py.md) (2 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (1 shared connections)

## Source Files

- `server/models/alias.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 244 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*