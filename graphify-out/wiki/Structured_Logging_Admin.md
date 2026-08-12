# Structured Logging Admin

> 28 nodes

## Key Concepts

- **AdminActionsLogger** (15 connections) — `server/structured_logging/admin_actions_logger.py`
- **Any** (8 connections)
- **._log_entry()** (8 connections) — `server/structured_logging/admin_actions_logger.py`
- **._read_actions_from_file()** (6 connections) — `server/structured_logging/admin_actions_logger.py`
- **.__init__()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **._get_log_file_path()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_teleport_action()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **.get_recent_actions()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **TeleportActionInput** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **._action_entry_matches_filters()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_admin_command()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_permission_check()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.get_teleport_statistics()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **Path** (3 connections)
- **._ensure_log_file_exists()** (3 connections) — `server/structured_logging/admin_actions_logger.py`
- **datetime** (3 connections)
- **TypedDict** (1 connections)
- **Optional fields for teleport action logging.** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Logger for admin actions with structured logging and file persistence.      Prov** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Initialize the admin actions logger.          Args:             log_directory: D** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Get the log file path for the current date.** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Ensure the current log file exists and create if necessary.** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Log a teleport action with comprehensive details.** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Log a general admin command action.** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Log permission check attempts.          Args:             player_name: Name of t** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- *... and 3 more nodes in this community*

## Relationships

- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (4 shared connections)
- [Room Drop Renderer](Room_Drop_Renderer.md) (1 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (1 shared connections)

## Source Files

- `server/structured_logging/admin_actions_logger.py`

## Audit Trail

- EXTRACTED: 98 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*