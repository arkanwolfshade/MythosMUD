# E 2 E Ai Execution

> 8 nodes

## Key Concepts

- **_get_alias_validator()** (8 connections) — `server/alias_storage.py`
- **test_get_alias_validator_caching()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_validator_import_failure()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_validator_creation_failure()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **Lazily instantiate and cache the alias schema validator.** (1 connections) — `server/alias_storage.py`
- **Test _get_alias_validator caches the validator.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _get_alias_validator returns None when import has previously failed.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _get_alias_validator handles validator creation failure.** (1 connections) — `server/tests/unit/test_alias_storage.py`

## Relationships

- [Alias Storage Services](Alias_Storage_Services.md) (4 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Fastapi Code Review](Fastapi_Code_Review.md) (1 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*