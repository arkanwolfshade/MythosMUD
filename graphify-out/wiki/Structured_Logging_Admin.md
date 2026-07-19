# Structured Logging Admin

> 22 nodes · cohesion 0.15

## Key Concepts

- **AdminActionsLogger** (13 connections) — `server/structured_logging/admin_actions_logger.py`
- **._log_entry()** (8 connections) — `server/structured_logging/admin_actions_logger.py`
- **Any** (6 connections) — `server/structured_logging/admin_actions_logger.py`
- **._get_log_file_path()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **.__init__()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **.get_recent_actions()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.get_teleport_statistics()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_admin_command()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_permission_check()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_teleport_action()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **._ensure_log_file_exists()** (3 connections) — `server/structured_logging/admin_actions_logger.py`
- **Path** (2 connections) — `server/structured_logging/admin_actions_logger.py`
- **Log a general admin command action.          Args:             admin_name: Name** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Log permission check attempts.          Args:             player_name: Name of t** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Write a log entry to the current log file.          Args:             log_entry:** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Logger for admin actions with structured logging and file persistence.      Prov** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Retrieve recent admin actions from the log files.          Args:             hou** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Get statistics about teleport actions.          Args:             hours: Number** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Initialize the admin actions logger.          Args:             log_directory: D** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Get the log file path for the current date.** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Ensure the current log file exists and create if necessary.** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Log a teleport action with comprehensive details.          Args:             adm** (1 connections) — `server/structured_logging/admin_actions_logger.py`

## Relationships

- [[NPC Admin API]] (2 shared connections)
- [[Admin Shutdown Commands]] (1 shared connections)
- [[Admin Teleport Commands]] (1 shared connections)

## Source Files

- `server/structured_logging/admin_actions_logger.py`

## Audit Trail

- EXTRACTED: 72 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
