# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-09-13-logout-button/spec.md

## Endpoints

### POST /commands/logout

**Purpose:** Process player logout command to terminate server-side session and cleanup game state
**Parameters:**
- `command`: "logout" (string)
- `args`: [] (empty array)
- `player_id`: Current player ID from session
- `auth_token`: Current authentication token

**Response:**
```json
{
  "success": true,
  "message": "Logged out successfully",
  "session_terminated": true,
  "connections_closed": true
}
```

**Errors:**
- `401 Unauthorized`: Invalid or expired authentication token
- `400 Bad Request`: Invalid logout command format
- `500 Internal Server Error`: Server-side logout processing error

### Server-Side Logout Processing

**Purpose:** Handle logout command processing on server side with proper session cleanup
**Implementation Requirements:**
- Persist player data to storage before logout
- Remove player from active gameplay memory
- Close all active connections (WebSocket and SSE)
- Terminate session and invalidate tokens
- Clean up connection pools and resources

**Error Handling:**
- Graceful handling of client disconnection during logout
- Ensure server-side cleanup completes even if client disconnects first
- Log logout events for debugging and monitoring

### Client-Side API Integration

**Purpose:** Integrate logout functionality with existing client architecture
**Implementation Details:**
- Utilize existing `sendCommand` function from `useGameConnection` hook
- Implement Promise-based timeout handling (5 seconds)
- Handle both successful and failed server responses
- Ensure client-side cleanup proceeds regardless of server response

**Timeout Behavior:**
- Wait maximum 5 seconds for server response
- If timeout occurs, proceed with client-side logout
- Provide user feedback during timeout period
- Always ensure user can return to login screen
