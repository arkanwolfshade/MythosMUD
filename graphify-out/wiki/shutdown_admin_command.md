# shutdown admin command

> 51 nodes

## Key Concepts

- **test_admin_shutdown_command.py** (57 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **_await_shutdown_result()** (14 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **cancel_shutdown_countdown()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **test_is_shutdown_pending_true()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_false()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_no_active()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_success()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownContainerStub** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_no_state()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_AppWithoutState** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownCancelStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownCancelAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_no_player_service()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_no_permission()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_invalid_parameters()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_cancel()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_cancel_no_active()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_superseding()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_no_seconds()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_handle_shutdown_command_initiate_failure()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- *... and 26 more nodes in this community*

## Relationships

- [eventLog projectorRoom roomMergeUtils](eventLog_projectorRoom_roomMergeUtils.md) (13 shared connections)
- [profession game service](profession_game_service.md) (7 shared connections)
- [services service hallucination](services_service_hallucination.md) (7 shared connections)
- [occupant realtime formatter](occupant_realtime_formatter.md) (4 shared connections)
- [lucidity models rationale](lucidity_models_rationale.md) (4 shared connections)
- [connection manager realtime](connection_manager_realtime.md) (4 shared connections)
- [motd loader rationale](motd_loader_rationale.md) (3 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)
- [commands party examples](commands_party_examples.md) (2 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)
- [room websocket updates](room_websocket_updates.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 206 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*