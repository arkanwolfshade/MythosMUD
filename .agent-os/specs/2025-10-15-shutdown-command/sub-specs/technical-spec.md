# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-10-15-shutdown-command/spec.md

## Technical Requirements

### Command Handler Implementation

- **Location:** `server/commands/admin_shutdown_command.py` (new file)
- **Integration:** Register handler in `CommandService.command_handlers` dictionary
- **Command Format:** `/shutdown [seconds|cancel]`
- **Parameter Validation:**
  - Seconds parameter: positive integer, no maximum enforced
  - Default: 10 seconds if not provided
  - Cancel: exact string match "cancel"

### Authorization

- **Permission Check:** Query `is_admin` flag from player's database record
- **Implementation:** Use existing `validate_admin_permission()` from `server/services/admin_auth_service.py`
- **Denial Message:** Thematic message for non-admin attempts (e.g., "You lack the proper authorization to invoke such rituals...")
- **No Logging:** Permission denials not logged to avoid log clutter

### Shutdown State Management

- **Global Flag:** `app.state.server_shutdown_pending` (boolean)
- **Shutdown Data:** `app.state.shutdown_data` (dict containing countdown time, start time, admin username)
- **State Access:** All authentication and character creation endpoints must check shutdown flag
- **Superseding Shutdowns:** New shutdown command overwrites existing shutdown_data

### Countdown Notification System

- **Implementation:** Async background task using `asyncio.create_task()`
- **Task Registration:** Register with `app.state.task_registry` for proper lifecycle management
- **Notification Frequency:**
  - Countdown > 10 seconds: notifications every 10 seconds
  - Final 10 seconds: notifications every 1 second
  - Example for 30 seconds: messages at 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
- **Message Channel:** Announcements channel (unignorable)
- **Message Format:** "The server will be shutting down in <time>"
- **Cancellation:** Task must be cancellable via `task.cancel()` when `/shutdown cancel` is issued

### Cancellation Implementation

- **Cancel Detection:** Check if `app.state.shutdown_data` exists
- **Task Cancellation:** Cancel countdown task via `task.cancel()` and await with `asyncio.CancelledError` handling
- **State Cleanup:** Clear `app.state.server_shutdown_pending` flag and `app.state.shutdown_data`
- **Notification:** Send cancellation message to Announcements channel (thematic message)
- **Login Restoration:** Immediately allow new logins/character creation after cancellation

### Shutdown Sequence (After Countdown Reaches Zero)

**Phase 1: Player Persistence**

- Iterate through all connected player IDs via `connection_manager.get_all_connected_player_ids()`
- Persist each player via `await persistence.save_player(player_id)`
- Log any persistence failures but continue shutdown

**Phase 2: NPC Cleanup**

- Iterate through `app.state.npc_spawning_service.active_npc_instances.keys()`
- Despawn each NPC via `app.state.npc_lifecycle_manager.despawn_npc(npc_id, reason="server_shutdown")`
- This stops NPC AI and removes instances from the game world

**Phase 3: Player Disconnection**

- Iterate through all connected player IDs
- Force disconnect via `await connection_manager.force_disconnect_player(player_id)`
- This closes both WebSocket and SSE connections gracefully

**Phase 4: Message System Shutdown**

- Stop NATS message handler: `await app.state.nats_message_handler.stop()`
- Disconnect NATS service: `await app.state.nats_service.disconnect()`
- Handle exceptions gracefully with logging

**Phase 5: Service Cleanup**

- Clean up connection manager: `await connection_manager.force_cleanup()`
- Shutdown task registry: `await task_registry.shutdown_all(timeout=5.0)`
- Log cleanup completion

**Phase 6: Server Exit**

- Call `sys.exit(0)` or raise `SystemExit(0)` to trigger FastAPI/uvicorn shutdown
- The lifespan context manager will handle final cleanup

### Login/Progression Blocking

**Authentication Endpoint** (`server/auth/endpoints.py`):

- Check `app.state.server_shutdown_pending` before issuing JWT
- Return HTTP 503 with message: "Server is shutting down, please try again later"

**Character Creation/Stats Rolling** (`server/api/player.py`):

- Check `app.state.server_shutdown_pending` before processing creation/stats
- Return error response with shutdown message

**MOTD Progression** (WebSocket connection handler):

- Check `app.state.server_shutdown_pending` before allowing MOTD completion
- Send error message and disconnect

### Audit Logging

- **Implementation:** Use `AdminActionsLogger` from `server/logging/admin_actions_logger.py`
- **Method:** `log_admin_command(admin_name, command, success, additional_data)`
- **Shutdown Initiation Data:**
  - `command`: "/shutdown"
  - `additional_data`: `{"countdown_seconds": <seconds>, "scheduled_time": <timestamp>}`
- **Cancellation Data:**
  - `command`: "/shutdown cancel"
  - `additional_data`: `{"remaining_seconds": <remaining>, "cancelled_at": <timestamp>}`
- **Log Location:** `logs/<environment>/commands.log`

### Error Handling

- **Countdown Task Errors:** Wrap countdown loop in try-except, log errors and attempt graceful degradation
- **Persistence Failures:** Log but don't halt shutdown sequence
- **Disconnection Failures:** Log but continue with remaining disconnections
- **Service Shutdown Errors:** Log and continue to next service
- **All Errors:** Log via structured logging with full context

### Performance Considerations

- **Countdown Task:** Minimal CPU impact, uses `asyncio.sleep()` between notifications
- **Player Persistence:** Sequential persistence acceptable for MVP, parallel optimization if needed
- **Graceful Timeouts:** Use `asyncio.wait_for()` with 5-second timeouts for service shutdowns
- **Memory Cleanup:** Ensure all references cleared to allow garbage collection

### Testing Requirements

- **Unit Tests:** Command parsing, authorization, state management, countdown logic
- **Integration Tests:** Full shutdown sequence with mock connections and services
- **Manual Testing:** Real server shutdown with multiple connected players
- **Test Coverage:** Minimum 80% code coverage for new shutdown module
