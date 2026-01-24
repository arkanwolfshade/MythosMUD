# 🚀 MythosMUD Real-Time Architecture

This document describes the real-time architecture implemented for MythosMUD, combining RESTful authentication with
WebSocket-based real-time gameplay updates.

## Rationale

### Recommended Architecture

**Frontend**: React + TypeScript

**Real-Time Communication**: WebSocket-only architecture

### Why WebSocket-Only?

**Simplified Architecture**: Single connection type reduces complexity

**Bidirectional Communication**: WebSocket handles both commands and game state updates

**Better Performance**: Lower overhead than maintaining dual connections

**Easier Debugging**: Single connection simplifies troubleshooting

- **Battle-Tested**: WebSocket is mature and well-supported
- **Unified Message Delivery**: All real-time communication through one protocol

## Architecture Overview

### **Three-Tier Design**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React Client  │    │   FastAPI       │    │   PostgreSQL    │
│   (Frontend)    │◄──►│   (Backend)     │◄──►│   (Database)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### **Communication Flow**

1. **Authentication**: REST API with JWT tokens
2. **Game State Updates**: WebSocket connections
3. **Interactive Commands**: WebSocket connections
4. **Data Persistence**: PostgreSQL database

## Technology Stack

### **Frontend (React + TypeScript)**

**Framework**: React 18+ with TypeScript

**State Management**: React hooks (useState, useReducer) and Zustand

**Real-time**: Native WebSocket API

**Styling**: CSS modules with terminal theme

### **Backend (Python + FastAPI)**

**Framework**: FastAPI with async/await

**Real-time**: WebSocket support only

**Authentication**: JWT tokens with Bearer scheme

**Database**: PostgreSQL with SQLAlchemy ORM

### **Real-time Protocols**

**WebSocket**: Bidirectional communication for all real-time features

**Message Format**: JSON with sequence numbers

## Implementation Details

### **1. Authentication Flow**

```typescript
// Client-side authentication
const response = await fetch('/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ username, password })
});

const { access_token } = await response.json();
// Store token for real-time connections
```

### **2. WebSocket Connections**

**Purpose**: Interactive commands, chat, and game state updates

**Server Endpoint**:

```python
@app.websocket("/ws/{player_id}")
async def websocket_endpoint_route(websocket: WebSocket, player_id: str):
    await websocket_endpoint(websocket, player_id)
```

**Client Connection (updated)**:

```typescript
// Use relative URL behind dev proxy; authenticate via subprotocols
const websocket = new WebSocket('/api/ws?session_id=' + sessionId, ['bearer', accessToken]);

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  handleCommandResponse(response);
};

// Send command
websocket.send(JSON.stringify({
  command: 'look',
  args: [],
  timestamp: new Date().toISOString()
}));
```

### **4. Message Format**

All real-time messages follow this structure:

```json
{
  "event_type": "game_state|room_update|combat_event|chat_message|game_tick",
  "timestamp": "2024-01-15T10:30:00Z",
  "sequence_number": 12345,
  "player_id": "optional-player-id",
  "room_id": "optional-room-id",
  "data": {
    // Event-specific data
  }
}
```

## Connection Management

### **Modular Architecture (Refactored December 2025)**

The ConnectionManager has been refactored into a modular architecture following the Facade pattern. This improves
maintainability, testability, and code organization:

**Component Groups**:

```
server/realtime/
├── connection_manager.py (Facade - coordinates components)
├── monitoring/
│   ├── performance_tracker.py (Performance metrics)
│   ├── statistics_aggregator.py (Statistics reporting)
│   └── health_monitor.py (Connection health checks)
├── errors/
│   └── error_handler.py (Error detection & recovery)
├── maintenance/
│   └── connection_cleaner.py (Cleanup & ghost player removal)
├── messaging/
│   ├── personal_message_sender.py (Direct messages)
│   └── message_broadcaster.py (Room/global broadcasts)
└── integration/
    ├── game_state_provider.py (Initial state delivery)
    └── room_event_handler.py (Room entry/exit events)
```

**Benefits**:

- Each component has a single, focused responsibility
- Components can be tested independently
- Changes are localized to specific modules
- Clear separation of concerns improves maintainability
- Dependency injection enables flexible configuration

**Core Responsibilities Retained**:

- WebSocket lifecycle management (connect/disconnect)
- Player presence tracking (online players, last seen)
- Connection metadata management
- Component coordination via facade pattern

**Refactoring Metrics**:

- Original: 3,653 lines (monolithic)
- Current: 2,382 lines (modular facade)
- Reduction: 35% (1,271 lines extracted)
- Components: 7 specialized modules
- Test Coverage: 99.8% maintained

See `REFACTORING_SUMMARY.md` for complete details.

### **Connection States**

1. **Connecting**: Initial connection attempt
2. **Connected**: Active real-time connection
3. **Reconnecting**: Automatic reconnection after disconnect
4. **Disconnected**: No active connection

### **Reconnection Strategy**

**Exponential backoff**: 1s, 2s, 4s, 8s, 16s, 30s max

**Maximum attempts**: 5 reconnection attempts

**Automatic**: Enabled by default, configurable

**State preservation**: Pending messages stored for delivery

### **Error Handling**

```typescript
// Client-side error handling
const handleError = (error: string) => {
  console.error('Connection error:', error);
  // Show user-friendly error message
  // Attempt reconnection if appropriate
};
```

## Game Event Types

### **Core Events**

| Event Type         | Purpose               | Data Structure                    |
| ------------------ | --------------------- | --------------------------------- |
| `game_state`       | Initial game state    | `{player, room}`                  |
| `room_update`      | Room changes          | `{room, entities}`                |
| `player_entered`   | Player joins room     | `{player_name, player_id}`        |
| `player_left`      | Player leaves room    | `{player_name, player_id}`        |
| `combat_event`     | Combat updates        | `{message, damage, target}`       |
| `chat_message`     | Chat messages         | `{channel, player_name, message}` |
| `game_tick`        | Periodic updates      | `{tick_number, timestamp}`        |
| `command_response` | Command results       | `{command, result, success}`      |
| `heartbeat`        | Connection keep-alive | `{}`                              |

### **Event Processing**

```typescript
function handleGameEvent(event: GameEvent) {
  switch (event.event_type) {
    case 'game_state':
      setGameState(event.data);
      break;
    case 'room_update':
      updateRoom(event.data);
      break;
    case 'combat_event':
      displayCombatMessage(event.data);
      break;
    // ... handle other events
  }
}
```

## Performance Considerations

### **Message Ordering**

**Sequence numbers**: All messages include sequence numbers

**Out-of-order handling**: Client can reorder messages if needed

**Duplicate detection**: Sequence numbers prevent duplicate processing

### **Scalability**

**Connection pooling**: Efficient WebSocket management

**Room subscriptions**: Only send updates to relevant players

**Message batching**: Combine multiple updates when possible

**Heartbeat optimization**: Minimal overhead for connection health

### **Memory Management**

**Message history**: Limited to last 100 messages

**Connection cleanup**: Automatic cleanup on disconnect

**Event garbage collection**: Old events automatically removed

## Security Considerations

### **Authentication**

**JWT tokens**: Required for all real-time connections

**Token validation**: Server validates tokens on connection

**Session management**: Tokens expire and require renewal

### **Input Validation**

**Command sanitization**: All commands validated server-side

**Rate limiting**: Prevent command spam

**Injection prevention**: SQL and command injection protection

### **Data Privacy**

**Room-based updates**: Players only see their room's events

**Personal data**: Sensitive data filtered from broadcasts

**Admin controls**: Separate admin-only events

## Development Workflow

### **Local Development**

1. **Start server**:

   ```bash
   cd server
   uv run uvicorn main:app --reload
   ```

2. **Start client**:

   ```bash
   cd client
   npm run dev
   ```

3. **Test connections**:

   - Visit `http://localhost:54731/docs` for API documentation
   - Use browser dev tools to monitor WebSocket connections
   - Check server logs for connection events

### **Testing Real-time Features**

```typescript
// Test WebSocket connection
const ws = new WebSocket('ws://localhost:54731/api/ws?token=test-token');
ws.onmessage = (event) => {
  console.log('WS message:', JSON.parse(event.data));
};
```

## Future Enhancements

### **Planned Features**

1. **Redis Integration**: For guaranteed message delivery
2. **Message Queuing**: Handle high-traffic scenarios
3. **Binary Protocols**: Optimize for performance
4. **Compression**: Reduce bandwidth usage
5. **Metrics**: Connection and performance monitoring

### **Scalability Improvements**

1. **Load Balancing**: Multiple server instances
2. **Database Sharding**: Distribute data across servers
3. **CDN Integration**: Static asset delivery
4. **Caching**: Redis for frequently accessed data

## Troubleshooting

### **Common Issues**

1. **Connection refused**: Check server is running
2. **Authentication failed**: Verify JWT token is valid
3. **Messages not received**: Check event type handling
4. **Reconnection loops**: Verify network connectivity

### **Debug Tools**

**Browser DevTools**: Network tab for connection monitoring

**Server Logs**: Connection and error logging

**WebSocket Inspector**: Browser extension for WS debugging

**Postman**: Test REST endpoints

## Conclusion

This real-time architecture provides a robust foundation for MythosMUD's multiplayer gameplay while maintaining
simplicity for development and debugging. The WebSocket-only approach offers reliable state updates and responsive
interactive commands through a single, unified connection.

The implementation is designed to be beginner-friendly while supporting the performance and scalability requirements of
a multiplayer game. Future enhancements can be added incrementally without disrupting the core architecture.
