# Path

> 17 nodes

## Key Concepts

- **Path** (11 connections)
- **test_backup_aliases_custom_dir()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_creates_directory()** (4 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_storage_dir()** (4 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_file_path()** (4 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_file_path_rejects_traversal()** (4 connections) — `server/tests/unit/test_alias_storage.py`
- **test_load_and_save_reject_path_injection()** (4 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_no_validator()** (4 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_with_validator()** (4 connections) — `server/tests/unit/test_alias_storage.py`
- **Load/save re-check before open: attack names never open files outside storage.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test backup_aliases uses custom backup directory.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test AliasStorage initialization with storage_dir parameter.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _validate_alias_payload returns empty list when validator unavailable.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _validate_alias_payload uses validator when available.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test that AliasStorage creates the storage directory if it doesn't exist.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test get_alias_file_path returns correct path.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Path-injection: traversal and separators must not escape storage_dir.** (1 connections) — `server/tests/unit/test_alias_storage.py`

## Relationships

- [AliasStorage](AliasStorage.md) (9 shared connections)
- [test_alias_storage.py](test_alias_storage.py.md) (8 shared connections)
- [Alias](Alias.md) (1 shared connections)
- [fixture](fixture.md) (1 shared connections)
- [MonkeyPatch](MonkeyPatch.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 27 (75%)
- INFERRED: 9 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*