# AuditLogger

> 46 nodes

## Key Concepts

- **AuditLogger** (21 connections) — `server/utils/audit_logger.py`
- **audit_logger.py** (14 connections) — `server/utils/audit_logger.py`
- **._write_entry()** (10 connections) — `server/utils/audit_logger.py`
- **test_audit_logger.py** (8 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **Any** (7 connections)
- **._read_entries_from_file()** (6 connections) — `server/utils/audit_logger.py`
- **.get_recent_entries()** (5 connections) — `server/utils/audit_logger.py`
- **ContainerInteractionAuditInput** (4 connections) — `server/utils/audit_logger.py`
- **._entry_matches_filters()** (4 connections) — `server/utils/audit_logger.py`
- **._get_log_file_path()** (4 connections) — `server/utils/audit_logger.py`
- **.get_statistics()** (4 connections) — `server/utils/audit_logger.py`
- **.__init__()** (4 connections) — `server/utils/audit_logger.py`
- **.log_command()** (4 connections) — `server/utils/audit_logger.py`
- **.log_container_interaction()** (4 connections) — `server/utils/audit_logger.py`
- **.log_security_event()** (4 connections) — `server/utils/audit_logger.py`
- **test_audit_logger_get_recent_entries()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_init()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_command()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_permission_change()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_player_action()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **.log_alias_expansion()** (3 connections) — `server/utils/audit_logger.py`
- **.log_permission_change()** (3 connections) — `server/utils/audit_logger.py`
- **.log_player_action()** (3 connections) — `server/utils/audit_logger.py`
- **datetime** (3 connections)
- **Path** (3 connections)
- *... and 21 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [processing.py](processing.py.md) (2 shared connections)
- [LootAllRequest](LootAllRequest.md) (1 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_audit_logger.py`
- `server/utils/audit_logger.py`

## Audit Trail

- EXTRACTED: 154 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*