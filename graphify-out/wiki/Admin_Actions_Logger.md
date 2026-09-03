# Admin Actions Logger

> 53 nodes

## Key Concepts

- **AdminActionsLogger** (31 connections) — `server/structured_logging/admin_actions_logger.py`
- **get_admin_actions_logger()** (25 connections) — `server/structured_logging/admin_actions_logger.py`
- **test_admin_actions_logger.py** (22 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **admin_actions_logger.py** (19 connections) — `server/structured_logging/admin_actions_logger.py`
- **._log_entry()** (8 connections) — `server/structured_logging/admin_actions_logger.py`
- **Any** (8 connections)
- **_read_log_entries()** (7 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **._read_actions_from_file()** (6 connections) — `server/structured_logging/admin_actions_logger.py`
- **Path** (6 connections)
- **._get_log_file_path()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **.get_recent_actions()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **.__init__()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_teleport_action()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **TeleportActionInput** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **._action_entry_matches_filters()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.get_teleport_statistics()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_admin_command()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_permission_check()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **admin_logger()** (4 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_get_admin_actions_logger_singleton()** (4 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_log_teleport_action_success()** (4 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **._ensure_log_file_exists()** (3 connections) — `server/structured_logging/admin_actions_logger.py`
- **log_dir()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_admin_logger_init_from_config()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_log_admin_command()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- *... and 28 more nodes in this community*

## Relationships

- [Test Teleport Helpers](Test_Teleport_Helpers.md) (6 shared connections)
- [Test Goto Helpers](Test_Goto_Helpers.md) (5 shared connections)
- [Test Admin Setlucidity Command](Test_Admin_Setlucidity_Command.md) (4 shared connections)
- [Test Admin Commands](Test_Admin_Commands.md) (3 shared connections)
- [Test Admin Permission Utils](Test_Admin_Permission_Utils.md) (3 shared connections)
- [Test Admin Summon Command](Test_Admin_Summon_Command.md) (3 shared connections)
- [Test Admin Teleport Commands](Test_Admin_Teleport_Commands.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Admin Shutdown Command](Admin_Shutdown_Command.md) (2 shared connections)
- [Test Config Init](Test_Config_Init.md) (2 shared connections)
- [Admin Setstat Support](Admin_Setstat_Support.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/structured_logging/test_admin_actions_logger.py`

## Audit Trail

- EXTRACTED: 127 (91%)
- INFERRED: 12 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*