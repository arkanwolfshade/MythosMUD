# Server (8)

> 21 nodes

## Key Concepts

- **test_alias_storage.py** (65 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_without_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_file_path_rejects_traversal()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_remove_alias_existing()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_nonexistent()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_name_too_long()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_name_reserved()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_command_reserved()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_create_alias_invalid_name()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_create_alias_invalid_command()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_list_alias_files_empty()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **Test AliasStorage initialization with ALIASES_DIR environment variable.** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **Test validate_alias_name rejects reserved commands.** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **Test create_alias returns None for invalid name.** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **Unit tests for alias storage utilities.  Tests the AliasStorage class for managi** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Path-injection: traversal and separators must not escape storage_dir.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test remove_alias removes existing alias.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test get_alias returns None for nonexistent alias.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test validate_alias_name rejects names longer than 20 characters.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test list_alias_files returns empty list when no files exist.** (1 connections) — `server/tests/unit/test_alias_storage.py`

## Relationships

- [Server (11)](Server_%2811%29.md) (6 shared connections)
- [Server Commands](Server_Commands.md) (4 shared connections)
- [Server (15)](Server_%2815%29.md) (4 shared connections)
- [Server (14)](Server_%2814%29.md) (4 shared connections)
- [Server Models (11)](Server_Models_%2811%29.md) (1 shared connections)
- [Server (30)](Server_%2830%29.md) (1 shared connections)
- [Server (54)](Server_%2854%29.md) (1 shared connections)
- [Server (51)](Server_%2851%29.md) (1 shared connections)
- [Server (53)](Server_%2853%29.md) (1 shared connections)
- [Server (52)](Server_%2852%29.md) (1 shared connections)
- [Server (50)](Server_%2850%29.md) (1 shared connections)
- [Server (35)](Server_%2835%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 101 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*