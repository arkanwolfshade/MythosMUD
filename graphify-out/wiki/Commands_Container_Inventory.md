# Commands Container Inventory

> 11 nodes

## Key Concepts

- **Path** (6 connections)
- **alias_storage()** (6 connections) — `server/tests/unit/test_alias_storage.py`
- **temp_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_custom_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_no_validator()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_with_validator()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **Create a temporary directory for alias storage.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Create an AliasStorage instance with temporary directory.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test backup_aliases uses custom backup directory.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _validate_alias_payload returns empty list when validator unavailable.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _validate_alias_payload uses validator when available.** (1 connections) — `server/tests/unit/test_alias_storage.py`

## Relationships

- [Alias Storage Services](Alias_Storage_Services.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Status Effect Model](Status_Effect_Model.md) (1 shared connections)
- [WebSocket Auth Integration](WebSocket_Auth_Integration.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 26 (90%)
- INFERRED: 3 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*