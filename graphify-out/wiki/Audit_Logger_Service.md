# Audit Logger Service

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
- **.__init__()** (4 connections) — `server/utils/audit_logger.py`
- **._get_log_file_path()** (4 connections) — `server/utils/audit_logger.py`
- **.log_command()** (4 connections) — `server/utils/audit_logger.py`
- **.log_container_interaction()** (4 connections) — `server/utils/audit_logger.py`
- **._entry_matches_filters()** (4 connections) — `server/utils/audit_logger.py`
- **.log_security_event()** (4 connections) — `server/utils/audit_logger.py`
- **.get_statistics()** (4 connections) — `server/utils/audit_logger.py`
- **test_audit_logger_init()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_command()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_permission_change()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_player_action()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_get_recent_entries()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **Path** (3 connections)
- **.log_permission_change()** (3 connections) — `server/utils/audit_logger.py`
- **datetime** (3 connections)
- **.log_player_action()** (3 connections) — `server/utils/audit_logger.py`
- **.log_alias_expansion()** (3 connections) — `server/utils/audit_logger.py`
- *... and 21 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Command Parser](Command_Parser.md) (2 shared connections)
- [Container Open Events](Container_Open_Events.md) (1 shared connections)
- [Persistence Container Extended](Persistence_Container_Extended.md) (1 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (1 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_audit_logger.py`
- `server/utils/audit_logger.py`

## Audit Trail

- EXTRACTED: 154 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*