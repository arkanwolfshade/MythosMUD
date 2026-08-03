# admin structured logging

> 42 nodes

## Key Concepts

- **AdminActionsLogger** (29 connections) — `server/structured_logging/admin_actions_logger.py`
- **test_admin_actions_logger.py** (21 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **._log_entry()** (8 connections) — `server/structured_logging/admin_actions_logger.py`
- **_read_log_entries()** (7 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **Any** (6 connections)
- **Path** (6 connections)
- **.__init__()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **._get_log_file_path()** (5 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_teleport_action()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_admin_command()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.log_permission_check()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.get_recent_actions()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **.get_teleport_statistics()** (4 connections) — `server/structured_logging/admin_actions_logger.py`
- **test_log_teleport_action_success()** (4 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_get_admin_actions_logger_singleton()** (4 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **._ensure_log_file_exists()** (3 connections) — `server/structured_logging/admin_actions_logger.py`
- **admin_logger()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_log_teleport_action_failure()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_log_admin_command()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_log_admin_command_failure()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_log_permission_check_denied()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_admin_logger_init_from_config()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **Path** (2 connections)
- **log_dir()** (2 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_get_recent_actions_filters()** (2 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- *... and 17 more nodes in this community*

## Relationships

- [npc service services](npc_service_services.md) (5 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/structured_logging/test_admin_actions_logger.py`

## Audit Trail

- EXTRACTED: 165 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*