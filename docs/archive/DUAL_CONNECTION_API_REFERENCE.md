# Dual Connection System API Reference

## Overview

This document provides comprehensive API documentation for the dual WebSocket/SSE connection system implemented in MythosMUD. The system allows players to maintain both WebSocket and Server-Sent Events (SSE) connections simultaneously, providing enhanced reliability and performance.

## Table of Contents

1. [Connection Endpoints](#connection-endpoints)
2. [Session Management](#session-management)
3. [Connection Statistics](#connection-statistics)
4. [Monitoring Endpoints](#monitoring-endpoints)
5. [Error Handling](#error-handling)
6. [Client Integration](#client-integration)
7. [Examples](#examples)

## Connection Endpoints

### WebSocket Connection

**Preferred Endpoint**: `/api/ws`

**Authentication (Recommended)**: WebSocket subprotocols

- Send `Sec-WebSocket-Protocol: bearer, <JWT>`

**Query Parameters**:

- `session_id` (optional): Unique session identifier for the game session

**Example**:

```
new WebSocket('/api/ws?session_id=session_123', ['bearer', accessToken])
```

**Backward Compatibility**:
Legacy path param endpoint `/api/ws/{player_id}` is deprecated and will be removed in a future release.

**Connection Behavior**:

- Multiple WebSocket connections per player are supported
- Each connection receives all messages sent to the player
- Connections persist until explicitly disconnected or session changes

### SSE Connection

**Endpoint**: `http://localhost:8000/sse/{player_id}`

**Query Parameters**:

- `session_id` (optional): Unique session identifier for the game session

**Example**:

```
http://localhost:8000/sse/test_player?session_id=session_123
```

**Connection Behavior**:

- Multiple SSE connections per player are supported
- Each connection receives all messages sent to the player
- Connections persist until explicitly disconnected or session changes

## Session Management

### New Game Session

**Endpoint**: `POST /api/connections/{player_id}/session`

**Request Body**:

```json
{
  "session_id": "new_session_456"
}
```

**Response**:

```json
{
  "success": true,
  "message": "New game session established",
  "session_id": "new_session_456",
  "previous_connections_disconnected": 2,
  "timestamp": "2025-01-06T19:55:00Z"
}
```

**Behavior**:

- Disconnects all existing connections for the player
- Establishes new session tracking
- Player must reconnect with new session ID

### Get Player Session

**Endpoint**: `GET /api/connections/{player_id}/session`

**Response**:

```json
{
  "player_id": "test_player",
  "session_id": "session_123",
  "session_created": "2025-01-06T19:50:00Z",
  "active_connections": 2,
  "connection_types": ["websocket", "sse"]
}
```

## Connection Statistics

### Get Connection Information

**Endpoint**: `GET /api/connections/{player_id}`

**Response**:

```json
{
  "player_id": "test_player",
  "session_id": "session_123",
  "connections": {
    "websocket": {
      "count": 1,
      "connection_ids": ["ws_conn_123"],
      "last_activity": "2025-01-06T19:55:00Z"
    },
    "sse": {
      "count": 1,
      "connection_ids": ["sse_conn_456"],
      "last_activity": "2025-01-06T19:55:00Z"
    }
  },
  "presence": {
    "status": "online",
    "last_seen": "2025-01-06T19:55:00Z",
    "total_connections": 2
  },
  "health": {
    "overall_health": "healthy",
    "websocket_health": "healthy",
    "sse_health": "healthy"
  }
}
```

### Get Global Connection Statistics

**Endpoint**: `GET /api/connections/stats`

**Response**:

```json
{
  "total_players": 25,
  "total_connections": 50,
  "connection_distribution": {
    "websocket_only": 5,
    "sse_only": 3,
    "dual_connections": 17
  },
  "session_statistics": {
    "total_sessions": 25,
    "average_connections_per_session": 2.0
  },
  "health_statistics": {
    "healthy_connections": 48,
    "unhealthy_connections": 2,
    "health_percentage": 96.0
  }
}
```

## Monitoring Endpoints

### Dual Connection Statistics

**Endpoint**: `GET /monitoring/dual-connections`

**Response**:

```json
{
  "connection_distribution": {
    "total_players": 25,
    "dual_connection_players": 17,
    "websocket_only_players": 5,
    "sse_only_players": 3,
    "dual_connection_percentage": 68.0
  },
  "connection_health": {
    "total_connections": 50,
    "healthy_connections": 48,
    "unhealthy_connections": 2,
    "health_percentage": 96.0
  },
  "session_analytics": {
    "total_sessions": 25,
    "sessions_with_connections": 25,
    "average_connections_per_session": 2.0
  }
}
```

### Performance Statistics

**Endpoint**: `GET /monitoring/performance`

**Response**:

```json
{
  "connection_establishment": {
    "total_connections": 50,
    "websocket_connections": 25,
    "sse_connections": 25,
    "avg_websocket_establishment_ms": 45.2,
    "avg_sse_establishment_ms": 32.1,
    "max_websocket_establishment_ms": 120.5,
    "max_sse_establishment_ms": 89.3
  },
  "message_delivery": {
    "total_messages_sent": 1250,
    "successful_deliveries": 1245,
    "failed_deliveries": 5,
    "delivery_success_rate": 99.6
  },
  "timestamp": "2025-01-06T19:55:00Z"
}
```

### Connection Health Statistics

**Endpoint**: `GET /monitoring/connection-health`

**Response**:

```json
{
  "overall_health": {
    "total_connections": 50,
    "healthy_connections": 48,
    "unhealthy_connections": 2,
    "health_percentage": 96.0
  },
  "connection_type_health": {
    "websocket": {
      "total": 25,
      "healthy": 24,
      "unhealthy": 1,
      "health_percentage": 96.0
    },
    "sse": {
      "total": 25,
      "healthy": 24,
      "unhealthy": 1,
      "health_percentage": 96.0
    }
  },
  "health_trends": {
    "last_hour_health_percentage": 95.8,
    "last_24_hours_health_percentage": 96.2
  }
}
```

## Error Handling

### Error Response Format

All API endpoints return errors in the following format:

```json
{
  "error": true,
  "error_type": "connection_error",
  "message": "Failed to establish connection",
  "details": {
    "player_id": "test_player",
    "connection_type": "websocket",
    "error_code": "CONNECTION_FAILED"
  },
  "timestamp": "2025-01-06T19:55:00Z"
}
```

### Common Error Types

`connection_error`: Connection establishment or maintenance issues

- `session_error`: Session management problems
- `authentication_error`: Authentication or authorization failures
- `validation_error`: Request validation failures
- `system_error`: Internal system errors

### Error Recovery

The system implements automatic error recovery for:

- Temporary connection failures
- Network interruptions
- Server restarts
- Session conflicts

## Client Integration

### React Hook Usage

```typescript
import { useGameConnection } from './hooks/useGameConnection';

function GameComponent() {
  const {
    isConnected,
    isConnecting,
    sessionId,
    connectionHealth,
    connect,
    disconnect,
    sendCommand,
    createNewSession,
    switchToSession,
    getConnectionInfo
  } = useGameConnection({
    playerId: 'test_player',
    onSessionChange: (newSessionId) => {
      console.log('Session changed to:', newSessionId);
    },
    onConnectionHealthUpdate: (health) => {
      console.log('Connection health:', health);
    }
  });

  // Component implementation
}
```

### Connection State Management

The client automatically manages:

- Dual connection establishment
- Session tracking
- Connection health monitoring
- Automatic reconnection
- Message deduplication

## Examples

### Establishing Dual Connections

```javascript
// WebSocket connection
const ws = new WebSocket('ws://localhost:8000/ws/test_player?session_id=session_123');

// SSE connection
const eventSource = new EventSource('http://localhost:8000/sse/test_player?session_id=session_123');

// Both connections will receive messages sent to test_player
```

### Session Management

```javascript
// Create new session
const response = await fetch('/api/connections/test_player/session', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ session_id: 'new_session_456' })
});

// Get current session
const sessionInfo = await fetch('/api/connections/test_player/session');
```

### Monitoring Connection Health

```javascript
// Get connection health statistics
const healthStats = await fetch('/monitoring/connection-health');
const stats = await healthStats.json();

console.log(`Health percentage: ${stats.overall_health.health_percentage}%`);
```

## Best Practices

### Connection Management

1. **Always include session_id** in connection URLs for proper session tracking
2. **Handle connection failures gracefully** with automatic retry logic
3. **Monitor connection health** using the provided monitoring endpoints
4. **Use dual connections** for enhanced reliability in production

### Session Management

1. **Create new sessions** when starting new game instances
2. **Switch sessions** when changing game contexts
3. **Clean up old sessions** to prevent resource leaks
4. **Validate session state** before critical operations

### Error Handling

1. **Implement retry logic** for temporary failures
2. **Log errors appropriately** for debugging
3. **Provide user feedback** for connection issues
4. **Monitor error rates** using the monitoring endpoints

### Performance Optimization

1. **Limit concurrent connections** per player (recommended: 2-4)
2. **Monitor performance metrics** regularly
3. **Implement connection pooling** for high-traffic scenarios
4. **Use health checks** to identify and resolve issues quickly

## Security Considerations

### Authentication

All connections require valid player authentication

- Session IDs should be cryptographically secure
- Implement rate limiting for connection attempts

### Authorization

Players can only access their own connections

- Session validation prevents unauthorized access
- Connection metadata is protected from external access

### Data Protection

Connection logs exclude sensitive information

- Session data is encrypted in transit
- Implement proper cleanup of connection metadata

## Troubleshooting

### Common Issues

1. **Connection Failures**

   - Check network connectivity
   - Verify server status
   - Validate session ID format

2. **Message Delivery Issues**

   - Check connection health status
   - Verify player authentication
   - Review server logs for errors

3. **Session Management Problems**

   - Ensure session ID uniqueness
   - Check session validation logic
   - Verify connection cleanup

### Debugging Tools

Use monitoring endpoints for system health

- Check connection statistics for patterns
- Review performance metrics for bottlenecks
- Monitor error logs for recurring issues

## Version History

**v1.0.0**: Initial dual connection system implementation

**v1.1.0**: Added comprehensive monitoring and health checks

**v1.2.0**: Enhanced session management and error recovery

- **v1.3.0**: Improved performance monitoring and optimization

## Support

For technical support or questions about the dual connection system:

1. Check the monitoring endpoints for system status
2. Review server logs for error details
3. Consult the troubleshooting section above
4. Contact the development team for advanced issues

---

*This documentation is maintained as part of the MythosMUD dual connection system implementation. Last updated: 2025-01-06*
