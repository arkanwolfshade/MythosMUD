# shutdown admin command

> 121 nodes

## Key Concepts

- **test_admin_shutdown_command.py** (57 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **admin_shutdown_command.py** (35 connections) — `server/commands/admin_shutdown_command.py`
- **Any** (20 connections)
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **_await_shutdown_result()** (14 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
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
- **test_initiate_shutdown_countdown_success()** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- *... and 96 more nodes in this community*

## Relationships

- [commands position system](commands_position_system.md) (6 shared connections)
- [models profession rationale](models_profession_rationale.md) (5 shared connections)
- [commands npc admin](commands_npc_admin.md) (4 shared connections)
- [models npc rationale](models_npc_rationale.md) (4 shared connections)
- [shutdown commands sequence](shutdown_commands_sequence.md) (3 shared connections)
- [profession game service](profession_game_service.md) (2 shared connections)
- [npc service services](npc_service_services.md) (1 shared connections)
- [admin structured logging](admin_structured_logging.md) (1 shared connections)
- [game models stats](game_models_stats.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (1 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 465 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*