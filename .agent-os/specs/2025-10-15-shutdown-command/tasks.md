# Spec Tasks

## Tasks

[x] 1. Implement Command Handler and Authorization

- [x] 1.1 Write tests for shutdown command parsing and authorization checks
- [x] 1.2 Create `server/commands/admin_shutdown_command.py` with command handler function
- [x] 1.3 Implement permission checking using `validate_admin_permission()` from admin_auth_service
- [x] 1.4 Add thematic denial message for non-admin players
- [x] 1.5 Register `shutdown` command handler in `CommandService.command_handlers` dictionary
- [x] 1.6 Implement basic parameter parsing for seconds (integer) and "cancel" (string)
- [x] 1.7 Add parameter validation with default value of 10 seconds
- [x] 1.8 Verify all tests pass for command parsing and authorization

- [x] 2. Implement Shutdown State Management and Countdown System
  - [x] 2.1 Write tests for state management and countdown notification frequency
  - [x] 2.2 Add `server_shutdown_pending` flag and `shutdown_data` dict to app.state
  - [x] 2.3 Implement countdown notification task with proper frequency (every 10s above 10s, every 1s for final 10s)
  - [x] 2.4 Register countdown task with `app.state.task_registry` for lifecycle management
  - [x] 2.5 Implement notification broadcasting via Announcements channel
  - [x] 2.6 Implement shutdown superseding logic (new shutdown cancels previous)
  - [x] 2.7 Implement `/shutdown cancel` command with task cancellation
  - [x] 2.8 Add cancellation notification message to Announcements channel
  - [x] 2.9 Verify all tests pass for state management and countdown logic

- [x] 3. Implement Login and Character Progression Blocking
  - [x] 3.1 Write tests for login blocking during shutdown
  - [x] 3.2 Add shutdown check to authentication endpoints (`/auth/login`, `/auth/register`)
  - [x] 3.3 Return HTTP 503 with appropriate message when shutdown is pending
  - [x] 3.4 Add shutdown check to character creation endpoint (`/players/create-character`)
  - [x] 3.5 Add shutdown check to stats rolling endpoint (`/players/roll-stats`)
  - [x] 3.6 Add shutdown check to WebSocket MOTD progression in `websocket_handler.py`
  - [x] 3.7 Send error message and disconnect WebSocket if shutdown is pending
  - [x] 3.8 Verify all tests pass for login and progression blocking

- [x] 4. Implement Graceful Shutdown Sequence
  - [x] 4.1 Write tests for shutdown sequence phases (mocked services)
  - [x] 4.2 Implement Phase 1: Player persistence loop with error handling
  - [x] 4.3 Implement Phase 2: NPC despawning via lifecycle_manager with "server_shutdown" reason
  - [x] 4.4 Implement Phase 3: Player disconnection via connection_manager force_disconnect_player
  - [x] 4.5 Implement Phase 4: NATS message handler stop and service disconnect
  - [x] 4.6 Implement Phase 5: Connection manager cleanup and task registry shutdown
  - [x] 4.7 Implement complete execute_shutdown_sequence function with all 7 phases
  - [x] 4.8 Add comprehensive error handling and logging for each phase
  - [x] 4.9 Verify all tests pass for shutdown sequence

- [x] 5. Implement Audit Logging and Testing
  - [x] 5.1 Write tests for audit logging verification
  - [x] 5.2 Verify audit logging using AdminActionsLogger.log_admin_command()
  - [x] 5.3 Verify shutdown initiation logged with countdown_seconds and scheduled_time
  - [x] 5.4 Verify shutdown cancellation logged with remaining_seconds and cancelled_at
  - [x] 5.5 Verify unauthorized attempts are not logged to audit trail
  - [x] 5.6 Test countdown notifications at correct intervals
  - [x] 5.7 Test cancellation flow and normal operation resumption
  - [x] 5.8 Verify minimum 80% code coverage achieved (81.04%)
  - [x] 5.9 Verify all 4,093 tests pass
