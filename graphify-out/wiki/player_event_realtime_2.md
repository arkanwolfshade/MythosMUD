# player event realtime

> 13 nodes

## Key Concepts

- **Path** (6 connections)
- **alias_storage()** (6 connections) — `server/tests/unit/test_alias_storage.py`
- **temp_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_file_path()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_custom_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_no_validator()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_with_validator()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **Create a temporary directory for alias storage.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Create an AliasStorage instance with temporary directory.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _get_alias_file_path returns correct path.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test backup_aliases uses custom backup directory.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _validate_alias_payload returns empty list when validator unavailable.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _validate_alias_payload uses validator when available.** (1 connections) — `server/tests/unit/test_alias_storage.py`

## Relationships

- [alias storage rationale](alias_storage_rationale.md) (6 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [request context realtime](request_context_realtime.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 31 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*