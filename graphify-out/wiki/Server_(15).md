# Server (15)

> 8 nodes

## Key Concepts

- **_get_alias_validator()** (7 connections) — `server/alias_storage.py`
- **test_get_alias_validator_caching()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_validator_import_failure()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_validator_creation_failure()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **Lazily instantiate and cache the alias schema validator.** (1 connections) — `server/alias_storage.py`
- **Test _get_alias_validator caches the validator.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _get_alias_validator returns None when import has previously failed.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _get_alias_validator handles validator creation failure.** (1 connections) — `server/tests/unit/test_alias_storage.py`

## Relationships

- [Server (8)](Server_%288%29.md) (4 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)
- [Server (3)](Server_%283%29.md) (1 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*