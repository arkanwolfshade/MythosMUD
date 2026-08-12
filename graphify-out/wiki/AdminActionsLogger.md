# AdminActionsLogger

> 28 nodes

## Key Concepts

- **AdminActionsLogger** (15 connections) — `server/structured_logging/admin_actions_logger.py`
- **._log_entry()** (8 connections) — `server/structured_logging/admin_actions_logger.py`
- **Any** (8 connections)
- **._read_actions_from_file()** (6 connections) — `server/structured_logging/admin_actions_logger.py`
- **._get_log_file_path()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **.get_recent_actions()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **.__init__()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_teleport_action()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **TeleportActionInput** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **._action_entry_matches_filters()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.get_teleport_statistics()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_admin_command()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_permission_check()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **._ensure_log_file_exists()** (3 connections) — `server/structured_logging/admin_actions_logger.py`
- **datetime** (3 connections)
- **Path** (3 connections)
- **TypedDict** (1 connections)
- **Log a general admin command action.** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Log permission check attempts. Args: player_name: Name of the player attempting…** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Optional fields for teleport action logging.** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Write a log entry to the current log file. Args: log_entry: Dictionary…** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Retrieve recent admin actions from the log files. Args: hours: Number of hours…** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Get statistics about teleport actions. Args: hours: Number of hours to analyze…** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Logger for admin actions with structured logging and file persistence. Provides…** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Initialize the admin actions logger. Args: log_directory: Directory to store…** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- *... and 3 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [admin_shutdown_command.py](admin_shutdown_command.py.md) (1 shared connections)

## Source Files

- `server/structured_logging/admin_actions_logger.py`

## Audit Trail

- EXTRACTED: 98 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*