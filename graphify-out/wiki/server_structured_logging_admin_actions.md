# server structured logging admin actions

> 53 nodes

## Key Concepts

- **AdminActionsLogger** (31 connections) — `server/structured_logging/admin_actions_logger.py`
- **get_admin_actions_logger()** (27 connections) — `server/structured_logging/admin_actions_logger.py`
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

- [server commands admin teleport commands](server_commands_admin_teleport_commands.md) (10 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (4 shared connections)
- [server commands admin teleport utils](server_commands_admin_teleport_utils.md) (4 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (3 shared connections)
- [server commands admin permission utils](server_commands_admin_permission_utils.md) (3 shared connections)
- [server commands admin setstat command](server_commands_admin_setstat_command.md) (3 shared connections)
- [server commands admin shutdown command](server_commands_admin_shutdown_command.md) (2 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (2 shared connections)
- [server commands admin summon command](server_commands_admin_summon_command.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/structured_logging/test_admin_actions_logger.py`

## Audit Trail

- EXTRACTED: 126 (89%)
- INFERRED: 15 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*