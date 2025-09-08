# Dual Connection System Specification

## Overview

This specification defines the enhancement of the MythosMUD connection handler system to support players having both an active WebSocket and an active SSE connection simultaneously. The system must maintain both connections without disconnecting either, except under specific conditions outlined in this document.

## Current System Analysis

### Existing Architecture

The current connection management system in `server/realtime/connection_manager.py` has the following characteristics:

1. **Single Connection Per Type**: Currently, only one WebSocket and one SSE connection per player is supported
2. **Connection Replacement**: New connections of the same type terminate existing connections
3. **Player Presence Tracking**: Uses `online_players` dictionary to track player presence
4. **Room Subscriptions**: Manages room subscriptions through `RoomSubscriptionManager`
5. **Message Queuing**: Handles pending messages through `MessageQueue`

### Current Limitations

1. **Connection Termination**: Lines 197-225 in `connect_websocket()` terminate existing WebSocket connections
2. **SSE Replacement**: Lines 351-354 in `connect_sse()` terminate existing SSE connections
3. **Single Connection Tracking**: Data structures assume one connection per type per player
4. **Message Delivery**: `send_personal_message()` only attempts WebSocket first, then falls back to pending messages

## Requirements

### Functional Requirements

1. **Dual Connection Support**: Players must be able to maintain both WebSocket and SSE connections simultaneously
2. **Connection Persistence**: Neither connection should be terminated when the other is established
3. **Message Delivery**: Messages should be delivered to all active connections for a player
4. **Presence Tracking**: Player presence should be maintained as long as any connection is active
5. **Room Subscriptions**: Room subscriptions should persist across all connections

### Disconnection Rules

Connections should only be disconnected under these specific conditions:

1. **Player Leaves Game**: When player explicitly logs out or leaves the game
2. **Fatal Error**: When a fatal error is detected in the connection (e.g., authentication failure, critical protocol error)
3. **New Game Client Session**: When a user logs in through a new game client session (replaces all existing connections)

### Non-Disconnection Scenarios

The following scenarios should NOT result in connection termination:

1. **Simultaneous Connection**: Establishing a second connection type while the first is active
2. **Connection Health Checks**: Routine health checks and ping operations
3. **Temporary Network Issues**: Brief network interruptions or latency spikes
4. **Client Reconnection**: Client attempting to reconnect while existing connections are healthy

## Technical Design

### Data Structure Changes

#### Connection Tracking

```python
# Current structure
self.active_websockets: dict[str, WebSocket] = {}  # connection_id -> websocket
self.player_websockets: dict[str, str] = {}        # player_id -> connection_id
self.active_sse_connections: dict[str, str] = {}   # player_id -> connection_id

# New structure
self.active_websockets: dict[str, WebSocket] = {}  # connection_id -> websocket
self.player_websockets: dict[str, list[str]] = {}  # player_id -> [connection_ids]
self.active_sse_connections: dict[str, list[str]] = {}  # player_id -> [connection_ids]
self.connection_metadata: dict[str, dict] = {}     # connection_id -> metadata
```

#### Connection Metadata

```python
@dataclass
class ConnectionMetadata:
    connection_id: str
    player_id: str
    connection_type: str  # "websocket" or "sse"
    established_at: float
    last_seen: float
    is_healthy: bool
    session_id: str  # For tracking new game client sessions
```

### API Changes

#### Connection Manager Methods

```python
async def connect_websocket(self, websocket: WebSocket, player_id: str, session_id: str = None) -> bool:
    """
    Connect a WebSocket for a player.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        session_id: Optional session identifier for new game client sessions

    Returns:
        bool: True if connection was successful, False otherwise
    """

async def connect_sse(self, player_id: str, session_id: str = None) -> str:
    """
    Connect an SSE connection for a player.

    Args:
        player_id: The player's ID
        session_id: Optional session identifier for new game client sessions

    Returns:
        str: The connection ID
    """

async def send_personal_message(self, player_id: str, event: dict[str, Any]) -> bool:
    """
    Send a personal message to a player via all active connections.

    Args:
        player_id: The player's ID
        event: The event data to send

    Returns:
        bool: True if sent successfully to at least one connection, False otherwise
    """

async def handle_new_game_session(self, player_id: str, session_id: str):
    """
    Handle a new game client session by terminating all existing connections.

    Args:
        player_id: The player's ID
        session_id: The new session identifier
    """
```

### Connection Health Management

#### Health Check System

```python
async def check_connection_health(self, player_id: str) -> dict[str, bool]:
    """
    Check health of all connections for a player.

    Returns:
        dict: Health status for each connection type
    """

async def cleanup_dead_connections(self, player_id: str):
    """
    Clean up dead connections for a player.
    """

def get_active_connections(self, player_id: str) -> dict[str, list[str]]:
    """
    Get all active connections for a player.

    Returns:
        dict: Connection IDs by type
    """
```

### Message Delivery Strategy

#### Multi-Connection Message Delivery

```python
async def send_personal_message(self, player_id: str, event: dict[str, Any]) -> bool:
    """
    Enhanced message delivery to all active connections.
    """
    success_count = 0
    total_connections = 0

    # Try WebSocket connections
    if player_id in self.player_websockets:
        for connection_id in self.player_websockets[player_id]:
            total_connections += 1
            if connection_id in self.active_websockets:
                websocket = self.active_websockets[connection_id]
                try:
                    await websocket.send_json(event)
                    success_count += 1
                except Exception as e:
                    logger.warning(f"WebSocket send failed for {player_id}: {e}")
                    await self._cleanup_dead_websocket(player_id, connection_id)

    # Try SSE connections (via pending messages)
    if player_id in self.active_sse_connections:
        for connection_id in self.active_sse_connections[player_id]:
            total_connections += 1
            # Add to pending messages for SSE delivery
            if player_id not in self.message_queue.pending_messages:
                self.message_queue.pending_messages[player_id] = []
            self.message_queue.pending_messages[player_id].append(event)
            success_count += 1

    return success_count > 0
```

## Implementation Plan

### Phase 1: Data Structure Updates

1. **Update Connection Tracking**
   - Modify `player_websockets` to support multiple connections
   - Modify `active_sse_connections` to support multiple connections
   - Add `connection_metadata` tracking

2. **Update Connection Methods**
   - Modify `connect_websocket()` to support multiple connections
   - Modify `connect_sse()` to support multiple connections
   - Add session tracking for new game client sessions

### Phase 2: Message Delivery Enhancement

1. **Multi-Connection Message Delivery**
   - Update `send_personal_message()` to deliver to all connections
   - Implement connection health checking
   - Add dead connection cleanup

2. **Connection Health Management**
   - Implement health check system
   - Add automatic dead connection cleanup
   - Update presence tracking logic

### Phase 3: Disconnection Logic

1. **New Game Session Handling**
   - Implement `handle_new_game_session()` method
   - Add session-based connection termination
   - Update API endpoints to pass session information

2. **Fatal Error Handling**
   - Enhance error detection and handling
   - Implement connection-specific error handling
   - Add error logging and monitoring

### Phase 4: Testing and Validation

1. **Unit Tests**
   - Test dual connection establishment
   - Test message delivery to multiple connections
   - Test disconnection scenarios

2. **Integration Tests**
   - Test client-side dual connection handling
   - Test server-side connection management
   - Test error scenarios and recovery

## Client-Side Considerations

### Connection Management

The client-side `useGameConnection` hook already supports tracking both WebSocket and SSE connections separately. The following enhancements may be needed:

1. **Connection State Management**
   - Ensure both connections can be active simultaneously
   - Handle connection-specific error states
   - Implement proper reconnection logic

2. **Message Handling**
   - Handle duplicate messages from multiple connections
   - Implement message deduplication if needed
   - Ensure proper event handling across connections

### API Integration

1. **Session Management**
   - Pass session identifiers to connection endpoints
   - Handle new game session notifications
   - Implement proper session cleanup

## Security Considerations

### Authentication and Authorization

1. **Connection Validation**
   - Ensure all connections are properly authenticated
   - Validate session identifiers
   - Implement connection-specific security checks

2. **Rate Limiting**
   - Apply rate limiting per connection type
   - Implement per-player rate limiting across all connections
   - Add connection-specific rate limiting

### Data Protection

1. **Message Security**
   - Ensure messages are only delivered to authenticated connections
   - Implement connection-specific message filtering
   - Add message integrity checks

## Monitoring and Logging

### Connection Monitoring

1. **Connection Metrics**
   - Track active connections per player
   - Monitor connection health
   - Log connection establishment and termination

2. **Performance Monitoring**
   - Monitor message delivery performance
   - Track connection error rates
   - Monitor resource usage

### Logging Enhancements

1. **Connection Events**
   - Log all connection establishment events
   - Log connection termination events
   - Log connection health check results

2. **Error Tracking**
   - Log connection-specific errors
   - Track fatal error occurrences
   - Monitor error recovery attempts

## Migration Strategy

### Backward Compatibility

1. **API Compatibility**
   - Maintain existing API endpoints
   - Add optional session parameters
   - Ensure existing clients continue to work

2. **Data Migration**
   - Migrate existing connection data structures
   - Update connection tracking logic
   - Ensure smooth transition

### Rollout Plan

1. **Development Environment**
   - Implement and test in development
   - Validate all functionality
   - Perform comprehensive testing

2. **Staging Environment**
   - Deploy to staging environment
   - Perform integration testing
   - Validate client compatibility

3. **Production Deployment**
   - Deploy with feature flags
   - Monitor system performance
   - Gradual rollout to users

## Success Criteria

### Functional Success

1. **Dual Connection Support**
   - Players can maintain both WebSocket and SSE connections
   - Messages are delivered to all active connections
   - Connections persist as specified

2. **Disconnection Rules**
   - Connections are only terminated under specified conditions
   - New game sessions properly terminate existing connections
   - Fatal errors are handled appropriately

### Performance Success

1. **Message Delivery**
   - Messages are delivered efficiently to all connections
   - No significant performance degradation
   - Proper error handling and recovery

2. **Resource Usage**
   - Memory usage remains within acceptable limits
   - Connection overhead is minimized
   - System remains stable under load

## Risk Assessment

### Technical Risks

1. **Connection Management Complexity**
   - Risk: Increased complexity in connection management
   - Mitigation: Comprehensive testing and monitoring

2. **Message Delivery Issues**
   - Risk: Duplicate or lost messages
   - Mitigation: Implement message deduplication and delivery confirmation

3. **Resource Usage**
   - Risk: Increased memory and CPU usage
   - Mitigation: Implement connection limits and monitoring

### Operational Risks

1. **Client Compatibility**
   - Risk: Existing clients may not work properly
   - Mitigation: Maintain backward compatibility and gradual rollout

2. **System Stability**
   - Risk: System instability due to increased complexity
   - Mitigation: Comprehensive testing and monitoring

## Conclusion

This specification provides a comprehensive plan for enhancing the MythosMUD connection handler system to support dual WebSocket and SSE connections. The implementation will maintain backward compatibility while providing the enhanced functionality required for modern client applications.

The phased implementation approach ensures that each component is thoroughly tested before proceeding to the next phase, minimizing risk and ensuring system stability throughout the development process.
