# shutdown admin command

> 130 nodes

## Key Concepts

- **test_admin_shutdown_command.py** (57 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **admin_shutdown_command.py** (35 connections) — `server/commands/admin_shutdown_command.py`
- **Any** (20 connections)
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **_await_shutdown_result()** (14 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **initiate_shutdown_countdown()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **handle_shutdown_command()** (13 connections) — `server/commands/admin_shutdown_command.py`
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
- *... and 105 more nodes in this community*

## Relationships

- [commands admin mute](commands_admin_mute.md) (12 shared connections)
- [profession game service](profession_game_service.md) (6 shared connections)
- [auth users rationale](auth_users_rationale.md) (4 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (4 shared connections)
- [shutdown commands sequence](shutdown_commands_sequence.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (2 shared connections)
- [admin structured logging](admin_structured_logging.md) (1 shared connections)
- [npc commands admin](npc_commands_admin.md) (1 shared connections)
- [npc look commands](npc_look_commands.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 492 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*