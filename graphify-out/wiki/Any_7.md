# Any

> 127 nodes

## Key Concepts

- **test_admin_shutdown_command.py** (57 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **admin_shutdown_command.py** (35 connections) — `server/commands/admin_shutdown_command.py`
- **Any** (20 connections)
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **handle_shutdown_command()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **_await_shutdown_result()** (14 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **initiate_shutdown_countdown()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **cancel_shutdown_countdown()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **parse_shutdown_parameters()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **validate_shutdown_admin_permission()** (9 connections) — `server/commands/admin_shutdown_command.py`
- **calculate_notification_times()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **broadcast_shutdown_notification()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **countdown_loop()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **test_is_shutdown_pending_true()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_false()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_no_active()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_success()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_create_countdown_task()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_store_shutdown_data()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_clear_shutdown_state()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_validate_shutdown_context()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_handle_shutdown_cancel()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_handle_shutdown_initiate()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_ShutdownContainerStub** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_success()** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- *... and 102 more nodes in this community*

## Relationships

- [Any](Any.md) (6 shared connections)
- [. init ()](_init_%28%29.md) (6 shared connections)
- [Schedule a best effort graceful](Schedule_a_best_effort_graceful.md) (3 shared connections)
- [Player Position Service](Player_Position_Service.md) (3 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (3 shared connections)
- [handle global command()](handle_global_command%28%29.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [get current tick()](get_current_tick%28%29.md) (2 shared connections)
- [Connection Manager](Connection_Manager.md) (2 shared connections)
- [test command factories inventory](test_command_factories_inventory.md) (1 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (1 shared connections)
- [message formatters](message_formatters.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 477 (100%)
- INFERRED: 2 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*