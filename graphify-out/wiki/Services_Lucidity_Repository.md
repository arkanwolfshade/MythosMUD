# Services Lucidity Repository

> 29 nodes

## Key Concepts

- **test_admin_shutdown_command.py** (57 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
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
- **test_get_shutdown_blocking_message_login()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_character_creation()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_get_shutdown_blocking_message_default()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Check if server shutdown is currently pending.      Args:         app: FastAPI a** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Cancel active shutdown countdown.      Args:         app: FastAPI application in** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Unit tests for admin shutdown command handler.  Tests the shutdown command funct** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **App double with no state attribute (is_shutdown_pending must return False).** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test is_shutdown_pending() returns True when shutdown is pending.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test is_shutdown_pending() returns False when shutdown is not pending.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test is_shutdown_pending() returns False when app has no state.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test get_shutdown_blocking_message() returns login message.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- *... and 4 more nodes in this community*

## Relationships

- [Room Drop Renderer](Room_Drop_Renderer.md) (12 shared connections)
- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (11 shared connections)
- [Status Effect Model](Status_Effect_Model.md) (7 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (6 shared connections)
- [Commands System Help](Commands_System_Help.md) (4 shared connections)
- [Chat Archive Advanced](Chat_Archive_Advanced.md) (4 shared connections)
- [Logging Structured Setup](Logging_Structured_Setup.md) (4 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (3 shared connections)
- [E 2 E Cleanup Troubleshooting](E_2_E_Cleanup_Troubleshooting.md) (3 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (1 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 151 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*