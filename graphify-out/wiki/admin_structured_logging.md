# admin structured logging

> 48 nodes

## Key Concepts

- **AdminActionsLogger** (29 connections) — `server/structured_logging/admin_actions_logger.py`
- **get_admin_actions_logger()** (27 connections) — `server/structured_logging/admin_actions_logger.py`
- **test_admin_actions_logger.py** (21 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **admin_actions_logger.py** (16 connections) — `server/structured_logging/admin_actions_logger.py`
- **admin_permission_utils.py** (9 connections) — `server/commands/admin_permission_utils.py`
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
- *... and 23 more nodes in this community*

## Relationships

- [npc service services](npc_service_services.md) (7 shared connections)
- [npc rewards combat](npc_rewards_combat.md) (5 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (4 shared connections)
- [shutdown command commands](shutdown_command_commands.md) (4 shared connections)
- [container schemas containers](container_schemas_containers.md) (4 shared connections)
- [security sessionManager SessionManager](security_sessionManager_SessionManager.md) (3 shared connections)
- [commands admin mute](commands_admin_mute.md) (3 shared connections)
- [command models admin](command_models_admin.md) (3 shared connections)
- [realtime game state](realtime_game_state.md) (3 shared connections)
- [eventLog projectorRoom roomMergeUtils](eventLog_projectorRoom_roomMergeUtils.md) (2 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (2 shared connections)

## Source Files

- `server/commands/admin_permission_utils.py`
- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/structured_logging/test_admin_actions_logger.py`

## Audit Trail

- EXTRACTED: 220 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*