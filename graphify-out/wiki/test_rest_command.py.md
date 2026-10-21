# test_rest_command.py

> 128 nodes · cohesion 0.03

## Key Concepts

- **test_admin_shutdown_command.py** (57 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **admin_shutdown_command.py** (40 connections) — `server/commands/admin_shutdown_command.py`
- **Any** (20 connections)
- **_asyncio_mark** (19 connections)
- **handle_shutdown_command()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **_await_shutdown_result()** (14 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **initiate_shutdown_countdown()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **cancel_shutdown_countdown()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **parse_shutdown_parameters()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **broadcast_shutdown_notification()** (9 connections) — `server/commands/admin_shutdown_command.py`
- **validate_shutdown_admin_permission()** (8 connections) — `server/commands/admin_shutdown_command.py`
- **calculate_notification_times()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **countdown_loop()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_no_active()** (7 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_success()** (7 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_broadcast_shutdown_cancellation()** (6 connections) — `server/commands/admin_shutdown_command.py`
- **_handle_shutdown_initiate()** (6 connections) — `server/commands/admin_shutdown_command.py`
- **_validate_shutdown_context()** (6 connections) — `server/commands/admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_success()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_supersedes()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_false()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_true()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_clear_shutdown_state()** (5 connections) — `server/commands/admin_shutdown_command.py`
- *... and 103 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (15 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (6 shared connections)
- [look_container.py](look_container.py.md) (5 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (4 shared connections)
- [test_game.py](test_game.py.md) (4 shared connections)
- [CombatAuditLogger](CombatAuditLogger.md) (3 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (2 shared connections)
- [test_shopkeeper_npc.py](test_shopkeeper_npc.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (2 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 292 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*