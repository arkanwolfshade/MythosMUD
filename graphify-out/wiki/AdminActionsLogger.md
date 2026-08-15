# AdminActionsLogger

> 51 nodes

## Key Concepts

- **AdminActionsLogger** (31 connections) — `server/structured_logging/admin_actions_logger.py`
- **test_admin_actions_logger.py** (21 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
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
- **test_log_admin_command_failure()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- *... and 26 more nodes in this community*

## Relationships

- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [admin_shutdown_command.py](admin_shutdown_command.py.md) (2 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (2 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (1 shared connections)
- [validate_admin_permission](validate_admin_permission.md) (1 shared connections)
- [_handle_admin_set_stat_command](_handle_admin_set_stat_command.md) (1 shared connections)
- [admin_summon_command.py](admin_summon_command.py.md) (1 shared connections)
- [test_goto_helpers.py](test_goto_helpers.py.md) (1 shared connections)

## Source Files

- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/structured_logging/test_admin_actions_logger.py`

## Audit Trail

- EXTRACTED: 102 (87%)
- INFERRED: 15 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*