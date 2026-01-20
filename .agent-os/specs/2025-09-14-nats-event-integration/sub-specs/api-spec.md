# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-09-14-nats-event-integration/spec.md

## Endpoints

### WebSocket /ws

**Purpose:** WebSocket endpoint for real-time game communication (unchanged interface)
**Parameters:** token (query param), session_id (query param)
**Response:** JSON messages with event_type, data, timestamp, sequence_number
**Errors:** 401 (Invalid token), 404 (Player not found)

### WebSocket /ws/{player_id}

**Purpose:** Backward-compatible WebSocket endpoint (unchanged interface)
**Parameters:** player_id (path param), token (query param), session_id (query param)
**Response:** JSON messages with event_type, data, timestamp, sequence_number
**Errors:** 401 (Invalid token), 404 (Player not found)

### GET /api/events

**Purpose:** Server-Sent Events stream for real-time game updates (unchanged interface)
**Parameters:** token (query param), session_id (query param)
**Response:** text/event-stream with SSE-formatted events
**Errors:** 401 (Invalid token), 404 (Player not found)

### GET /api/events/{player_id}

**Purpose:** Server-Sent Events stream for specific player (unchanged interface)
**Parameters:** player_id (path param), session_id (query param)
**Response:** text/event-stream with SSE-formatted events
**Errors:** 401 (Invalid token), 404 (Player not found)

## Event Message Format

All real-time events follow this standardized format:

```json
{
  "event_type": "player_entered|player_left|game_tick|room_occupants|game_state",
  "timestamp": "2024-01-15T10:30:00Z",
  "sequence_number": 12345,
  "player_id": "optional-player-id",
  "room_id": "optional-room-id",
  "data": {
    // Event-specific data
  }
}
```

## NATS Subject Patterns

`events.player_entered.{room_id}` - Player enters a room

- `events.player_left.{room_id}` - Player leaves a room
- `events.game_tick` - Global game heartbeat (10 second intervals)

## Integration Points

**EventPublisher**: Publishes events to NATS subjects

**NATSMessageHandler**: Subscribes to NATS subjects and routes to WebSocket clients

**ConnectionManager**: Manages WebSocket connections and room subscriptions
- **Game Tick Loop**: Publishes periodic game state updates
