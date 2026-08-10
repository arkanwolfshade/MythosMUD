# Playwright Remediation Plan

> 47 nodes

## Key Concepts

- **test_admin_shutdown_command.py** (57 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_true()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_false()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_no_active()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_cancel_shutdown_countdown_success()** (6 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownContainerStub** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_success()** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_supersedes()** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_is_shutdown_pending_no_state()** (4 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_PendingCheckAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_AppWithoutState** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownCancelStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_ShutdownCancelAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_InitiateStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_InitiateAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_login()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_character_creation()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_default()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_broadcast_shutdown_notification_success()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_broadcast_shutdown_notification_failure()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_no_args()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_cancel()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_seconds()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_invalid_negative()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- *... and 22 more nodes in this community*

## Relationships

- [Room Drop Renderer](Room_Drop_Renderer.md) (18 shared connections)
- [Connection Room Presence Utils](Connection_Room_Presence_Utils.md) (11 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (8 shared connections)
- [Realtime Message Builders](Realtime_Message_Builders.md) (4 shared connections)
- [Chat Archive Advanced](Chat_Archive_Advanced.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 174 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*