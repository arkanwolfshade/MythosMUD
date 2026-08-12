# alias_storage

> 18 nodes

## Key Concepts

- **alias_storage()** (7 connections) — `server/tests/unit/test_alias_storage.py`
- **Path** (5 connections)
- **.get_alias_storage()** (4 connections) — `server/realtime/request_context.py`
- **sample_alias()** (4 connections) — `server/tests/unit/test_alias_storage.py`
- **sample_alias2()** (4 connections) — `server/tests/unit/test_alias_storage.py`
- **temp_storage_dir()** (4 connections) — `server/tests/unit/test_alias_storage.py`
- **fixture** (4 connections)
- **test_backup_aliases_custom_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_no_validator()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_with_validator()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **Get the alias storage from the request context.** (1 connections) — `server/realtime/request_context.py`
- **Create a temporary directory for alias storage.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Create an AliasStorage instance with temporary directory.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Create a sample alias for testing.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Create another sample alias for testing.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test backup_aliases uses custom backup directory.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _validate_alias_payload returns empty list when validator unavailable.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _validate_alias_payload uses validator when available.** (1 connections) — `server/tests/unit/test_alias_storage.py`

## Relationships

- [test_alias_storage.py](test_alias_storage.py.md) (7 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (2 shared connections)
- [Alias](Alias.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [GameBundle](GameBundle.md) (1 shared connections)

## Source Files

- `server/realtime/request_context.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 46 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*