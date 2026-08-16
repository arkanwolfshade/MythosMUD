# admin_shutdown_command.py

> 44 nodes

## Key Concepts

- **admin_shutdown_command.py** (36 connections) — `server/commands/admin_shutdown_command.py`
- **Any** (20 connections)
- **handle_shutdown_command()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **initiate_shutdown_countdown()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **cancel_shutdown_countdown()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **parse_shutdown_parameters()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **validate_shutdown_admin_permission()** (9 connections) — `server/commands/admin_shutdown_command.py`
- **broadcast_shutdown_notification()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **calculate_notification_times()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **countdown_loop()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **_clear_shutdown_state()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_create_countdown_task()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_handle_shutdown_cancel()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_handle_shutdown_initiate()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_store_shutdown_data()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_validate_shutdown_context()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_broadcast_shutdown_cancellation()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_cancel_countdown_task()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_cancel_existing_shutdown_task()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_get_shutdown_services()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_get_shutdown_state()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_set_shutdown_pending_flag()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **Task** (2 connections)
- **Admin shutdown command for MythosMUD. This module provides the /shutdown…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Calculate notification times for countdown. Notifications occur: - Every 10…** (1 connections) — `server/commands/admin_shutdown_command.py`
- *... and 19 more nodes in this community*

## Relationships

- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (27 shared connections)
- [test_shutdown_sequence.py](test_shutdown_sequence.py.md) (3 shared connections)
- [command_service.py](command_service.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (3 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 127 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*