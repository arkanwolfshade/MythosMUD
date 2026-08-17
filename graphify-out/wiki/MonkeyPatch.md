# MonkeyPatch

> 11 nodes

## Key Concepts

- **test_alias_storage_init_with_env_var()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_io_error()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_delete_player_aliases_io_error()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **MonkeyPatch** (5 connections)
- **test_load_alias_data_io_error()** (4 connections) — `server/tests/unit/test_alias_storage.py`
- **test_save_alias_data_io_error()** (4 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _load_alias_data handles IO errors gracefully.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _save_alias_data handles IO errors.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test delete_player_aliases handles IO errors.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test backup_aliases handles IO errors.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test AliasStorage initialization with ALIASES_DIR environment variable.** (1 connections) — `server/tests/unit/test_alias_storage.py`

## Relationships

- [test_alias_storage.py](test_alias_storage.py.md) (5 shared connections)
- [AliasStorage](AliasStorage.md) (5 shared connections)
- [Alias](Alias.md) (2 shared connections)
- [Path](Path.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 16 (70%)
- INFERRED: 7 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*