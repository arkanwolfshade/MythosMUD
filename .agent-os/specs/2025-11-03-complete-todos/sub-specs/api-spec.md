# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-11-03-complete-todos/spec.md

## Modified Endpoints

### POST /api/game/broadcast

**Purpose**: Broadcast administrative message to all connected players (SECURITY UPDATE)

**Current Behavior**: Allows any authenticated user to broadcast

**New Behavior**: Requires admin role for access

**Parameters**:
- `message` (string, required): Message to broadcast to all players
- Headers: `Authorization: Bearer <jwt_token>` (required)

**Authentication**: JWT token required

**Authorization**: **NEW** - Requires admin role in user profile

**Response Success (200)**:
```json
{
  "message": "Broadcast message: <message content>"
}
```

**Response Error (403 Forbidden)** - NEW:
```json
{
  "detail": "Admin role required for broadcast operations"
}
```

**Response Error (401 Unauthorized)**:
```json
{
  "detail": "Not authenticated"
}
```

**Implementation Changes**:
```python
# server/api/game.py
from server.auth.dependencies import require_admin_role

@router.post("/broadcast")
async def broadcast_message(
    message: str,
    request: Request = None,
    current_user: dict = Depends(require_admin_role),  # Changed from get_current_user
) -> dict[str, str]:
    """Broadcast a message to all connected players (admin only)."""
    logger.info("Broadcast message requested", user=current_user.get("username"), message=message)

    # Admin role already verified by dependency
    # ... rest of implementation
```

**Errors**:
- 401: User not authenticated
- 403: User authenticated but lacks admin role
- 400: Invalid message format

**Testing Requirements**:
- Test with admin user (expect 200)
- Test with non-admin user (expect 403)
- Test with no auth token (expect 401)
- Test with empty message (expect 400)

## New WebSocket Message Validation

### WebSocket CSRF Token Validation

**Purpose**: Validate CSRF tokens on sensitive WebSocket operations

**Connection Handshake Enhancement**:

**Server Sends on Connection**:
```json
{
  "type": "connection_established",
  "csrf_token": "randomly_generated_secure_token",
  "player_id": "player_uuid",
  "session_id": "session_uuid"
}
```

**Client Includes in Messages**:
```json
{
  "type": "command",
  "command": "attack",
  "csrf_token": "token_from_handshake",
  "args": ["npc_123"]
}
```

**Server Validation**:
- Extract `csrf_token` from message
- Compare with stored token for connection
- Reject message if token missing or invalid
- Log CSRF validation failures

**Response for Invalid Token**:
```json
{
  "type": "error",
  "error": "CSRF token validation failed",
  "code": "INVALID_CSRF_TOKEN"
}
```

**Exemptions** (No CSRF Required):
- Read-only operations: `look`, `who`, `inventory` (when implemented)
- System messages
- Connection management messages

**Configuration**:
- `WEBSOCKET_CSRF_ENABLED`: boolean (default: true)
- `CSRF_TOKEN_LENGTH`: integer (default: 32 bytes)

**Implementation Location**:
- `server/realtime/websocket_handler.py:284` - validation logic
- `server/realtime/connection_manager.py` - token generation and storage

## New Service Methods

### NPCInstanceService Enhancements

**Purpose**: Provide admin control over NPC behaviors and reactions

#### Method: set_npc_behavior

**Endpoint**: Called via admin command `npc behavior <npc_id> <behavior_type>`

**Signature**:
```python
async def set_npc_behavior(self, npc_id: str, behavior_type: str) -> bool:
    """Set NPC behavior pattern."""
```

**Parameters**:
- `npc_id`: Unique identifier for NPC instance
- `behavior_type`: One of [patrol, guard, wander, aggressive, passive, flee]

**Returns**: `True` if behavior set successfully, `False` if NPC not found

**Side Effects**:
- Updates NPC instance behavior state
- Publishes `npc.behavior.changed` NATS event
- Logs behavior change

**Errors**:
- Raises `ValueError` if behavior_type invalid
- Raises `NPCNotFoundError` if npc_id not found

#### Method: trigger_npc_reaction

**Endpoint**: Called via admin command `npc react <npc_id> <reaction_type>`

**Signature**:
```python
async def trigger_npc_reaction(self, npc_id: str, reaction_type: str) -> bool:
    """Trigger immediate NPC reaction."""
```

**Parameters**:
- `npc_id`: Unique identifier for NPC instance
- `reaction_type`: One of [greet, attack, flee, investigate, alert, calm, excited, suspicious]

**Returns**: `True` if reaction triggered, `False` if NPC not found

**Side Effects**:
- Executes immediate reaction animation/emote
- Publishes `npc.reacted` NATS event
- Broadcasts reaction to players in room

**Errors**:
- Raises `ValueError` if reaction_type invalid
- Raises `NPCNotFoundError` if npc_id not found

#### Method: stop_npc_behavior

**Endpoint**: Called via admin command `npc stop <npc_id>`

**Signature**:
```python
async def stop_npc_behavior(self, npc_id: str) -> bool:
    """Stop NPC behavior and set to idle."""
```

**Parameters**:
- `npc_id`: Unique identifier for NPC instance

**Returns**: `True` if behavior stopped, `False` if NPC not found or already idle

**Side Effects**:
- Halts current behavior loop
- Sets NPC to idle state
- Publishes `npc.behavior.stopped` NATS event
- Clears behavior timers

**Errors**:
- Raises `NPCNotFoundError` if npc_id not found

## API Integration Points

### NATS Event Publishing

**New Events**:
1. `npc.behavior.changed` - Published when NPC behavior is modified
2. `npc.reacted` - Published when NPC performs reaction
3. `npc.behavior.stopped` - Published when NPC behavior is stopped
4. `room.sync.request` - Published to request fresh room data

**Event Format**:
```python
{
    "event_type": "npc.behavior.changed",
    "npc_id": "npc_uuid",
    "behavior_type": "aggressive",
    "changed_by": "admin_player_id",
    "timestamp": "2025-11-03T19:45:00Z"
}
```

### Configuration API

**New Configuration Values**:
- `JWT_SECRET`: Environment variable (required in production)
- `JWT_TOKEN_LIFETIME`: Integer seconds (default: 3600)
- `WEBSOCKET_CSRF_ENABLED`: Boolean (default: true)
- `CSRF_TOKEN_LENGTH`: Integer (default: 32)
- `IMMEDIATE_DEATH_HANDLING`: Boolean (default: true)
- `SQL_ECHO`: Boolean (default: false)
- `SQL_ECHO_POOL`: Boolean (default: false)
- `ALLOW_ROOM_MODIFICATIONS`: Boolean (default: false)
- `REQUIRE_TELEPORT_CONFIRMATION`: Boolean (default: false)

**Configuration Access**:
```python
from server.config import get_config

config = get_config()
jwt_secret = config.jwt_secret  # Raises error if not set
csrf_enabled = config.websocket_csrf_enabled
```

## Backward Compatibility

**Breaking Changes**: None - all changes are additive or security-enhancing

**Deprecations**:
- Legacy chat subscription patterns (`chat.local.*`) - will be removed after verification

**Migration Path**:
- Existing code continues to work
- New security features enforced on next deployment
- Invite tracking applies to new character creations only (existing characters unaffected)

## Performance Impact Assessment

- **JWT Secret**: No performance impact (config read at startup)
- **Admin Role Check**: +2-5ms per admin endpoint call (acceptable for infrequent admin operations)
- **CSRF Validation**: +1-3ms per WebSocket message (minimal impact)
- **NPC Methods**: +5-10ms per admin command (acceptable for admin operations)
- **Damage Calculation**: +2-5ms per combat action (significant improvement over basic damage)
- **Name Resolution**: +1-2ms per event with caching (acceptable)
