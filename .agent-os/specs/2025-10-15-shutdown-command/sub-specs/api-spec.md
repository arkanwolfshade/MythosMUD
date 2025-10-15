# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-10-15-shutdown-command/spec.md

## Command Interface

### Command: `/shutdown [seconds]`

**Purpose:** Initiate graceful server shutdown with countdown notification

**Parameters:**

- `seconds` (optional integer): Countdown duration in seconds
  - Default: 10 seconds
  - Range: Any positive integer (no enforced maximum)
  - Validation: Must be numeric and positive

**Authorization:** Requires `is_admin` flag set to `true` in player database record

**Response (Admin - Success):**

```json
{
  "result": "Server shutdown initiated. Shutting down in <seconds> seconds..."
}
```

**Response (Admin - Superseding Previous Shutdown):**

```json
{
  "result": "Previous shutdown cancelled. Server will now shut down in <seconds> seconds..."
}
```

**Response (Non-Admin - Denied):**

```json
{
  "result": "You lack the proper authorization to invoke such rituals. Only those with the appropriate clearances may command these mechanisms."
}
```

**Side Effects:**

- Sets `app.state.server_shutdown_pending = True`
- Creates `app.state.shutdown_data` with countdown info
- Spawns countdown notification task
- Blocks new logins and character progression
- Logs to admin audit trail

---

### Command: `/shutdown cancel`

**Purpose:** Cancel ongoing server shutdown countdown

**Parameters:**

- `cancel` (literal string): Exact match required

**Authorization:** Requires `is_admin` flag set to `true`

**Response (Admin - Success):**

```json
{
  "result": "Shutdown cancelled. Server will continue normal operation."
}
```

**Response (Admin - No Active Shutdown):**

```json
{
  "result": "There is no active shutdown to cancel."
}
```

**Response (Non-Admin - Denied):**

```json
{
  "result": "You lack the proper authorization to invoke such rituals. Only those with the appropriate clearances may command these mechanisms."
}
```

**Side Effects:**

- Cancels countdown task
- Clears `app.state.server_shutdown_pending` flag
- Clears `app.state.shutdown_data`
- Re-enables logins and character progression
- Sends cancellation notification to all players
- Logs to admin audit trail

---

## Notification Messages

### Countdown Notifications

**Channel:** Announcements (unignorable)

**Format:**

```
"The server will be shutting down in <time>"
```

**Time Format:**

- Single second: "1 second"
- Multiple seconds: "<n> seconds"

**Frequency:**

- Notifications at: countdown start, then every 10 seconds while > 10, then every second for final 10

**Example Sequence (30-second countdown):**

```
"The server will be shutting down in 30 seconds"
"The server will be shutting down in 20 seconds"
"The server will be shutting down in 10 seconds"
"The server will be shutting down in 9 seconds"
...
"The server will be shutting down in 1 second"
```

### Cancellation Notification

**Channel:** Announcements (unignorable)

**Message:**

```
"The scheduled server shutdown has been cancelled. The stars are right once more."
```

---

## State Management API

### Application State Extensions

**New State Variables:**

```python
app.state.server_shutdown_pending: bool
# Indicates whether server shutdown is in progress
# Default: False
# Set to True when shutdown initiated
# Set to False when cancelled or shutdown completes

app.state.shutdown_data: dict | None
# Contains shutdown countdown information
# Structure:
# {
#   "countdown_seconds": int,
#   "start_time": float,  # time.time() when initiated
#   "end_time": float,    # calculated shutdown time
#   "admin_username": str,
#   "task": asyncio.Task  # reference to countdown task
# }
# Default: None
# Created on shutdown initiation
# Cleared on cancellation or completion
```

**State Access Pattern:**

```python
# Check if shutdown is pending
if getattr(app.state, 'server_shutdown_pending', False):
    # Shutdown is active
    return error_response("Server is shutting down")

# Get shutdown data
shutdown_data = getattr(app.state, 'shutdown_data', None)
if shutdown_data:
    remaining = shutdown_data['end_time'] - time.time()
```

---

## Integration Points

### Authentication Endpoints

**Affected Endpoints:**

- `POST /auth/login`
- `POST /auth/jwt/login`

**Required Change:**

```python
if getattr(app.state, 'server_shutdown_pending', False):
    raise HTTPException(
        status_code=503,
        detail="Server is shutting down, please try again later"
    )
```

### Character Creation Endpoints

**Affected Endpoints:**

- `POST /api/player/create`
- `POST /api/player/roll-stats`

**Required Change:**

```python
if getattr(app.state, 'server_shutdown_pending', False):
    return {"error": "Server is shutting down. Character creation unavailable."}
```

### WebSocket Connection Handler

**Location:** `server/realtime/websocket_handler.py`

**Required Change:**

```python
# In handle_websocket_connection, before allowing MOTD progression:
if getattr(request.app.state, 'server_shutdown_pending', False):
    await websocket.send_json({
        "type": "error",
        "message": "Server is shutting down. Please reconnect later."
    })
    await websocket.close()
    return
```

---

## Command Handler Registration

**Location:** `server/commands/command_service.py`

**Registration:**

```python
# In CommandService.__init__
self.command_handlers = {
    # ... existing handlers ...
    "shutdown": handle_shutdown_command,
}
```

**Handler Import:**

```python
from server.commands.admin_shutdown_command import handle_shutdown_command
```

---

## Error Handling

### Command Execution Errors

**Scenario:** Exception during shutdown initiation
**Response:**

```json
{
  "result": "Error initiating shutdown: <error_message>"
}
```

**Logging:** Error logged with full traceback

### Countdown Task Errors

**Scenario:** Exception during countdown notification
**Behavior:**

- Log error
- Continue countdown if possible
- If fatal, log failure and continue to shutdown

### Service Shutdown Errors

**Scenario:** Exception during NATS/connection cleanup
**Behavior:**

- Log error with context
- Continue to next shutdown phase
- Don't block server exit
