# Alias Storage Services

> 10 nodes · cohesion 0.20

## Key Concepts

- **Path** (7 connections) — `server/tests/unit/test_alias_storage.py`
- **temp_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_backup_aliases_custom_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_no_validator()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_payload_with_validator()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **temp_log_dir()** (2 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Create a temporary directory for alias storage.** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **Test backup_aliases uses custom backup directory.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _validate_alias_payload returns empty list when validator unavailable.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test _validate_alias_payload uses validator when available.** (1 connections) — `server/tests/unit/test_alias_storage.py`

## Relationships

- [[Alias Storage Layer]] (5 shared connections)
- [[Alias Expansion Logic]] (1 shared connections)
- [[Command Alias Model]] (1 shared connections)
- [[Chat Logger Service Tests]] (1 shared connections)

## Source Files

- `server/tests/unit/services/test_chat_logger.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 24 (92%)
- INFERRED: 2 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
