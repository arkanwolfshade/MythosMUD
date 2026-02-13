# MythosMUD Server

The backend server for MythosMUD, a Lovecraftian horror MUD game.

## Features

### Core Systems

**World Loading**: Loads room data from JSON files organized by zones (now
in `data/local/rooms/`)

**Player Management**: Complete player character system with stats and persistence

**Real-time Game Loop**: Tick-based game loop for processing game events

**Status Effects**: Dynamic status effect system for horror mechanics

### Player Data Storage (NEW)

Player data is stored as individual files in `data/local/players/player_<GUID>.json`.

- There is no longer a single `players.json` file.
- The server dynamically loads player data from these files after authentication.
- Example: `data/local/players/player_3ff4b997-1bed-42b9-a96e-0892c9e25357.json`
- A sample player file for tests is provided as `data/local/players/player_test-id-123.json`.

### Player Stats System

The game features a comprehensive stats system with Lovecraftian horror elements:

#### Core Attributes (1-20 scale)

**Physical**: Strength, Dexterity, Constitution

**Mental**: Intelligence, Wisdom, Charisma

#### Horror-Specific Attributes (0-100 scale)

**Lucidity**: Mental stability (0 = complete madness)

**Occult Knowledge**: Forbidden lore knowledge (causes lucidity loss)

**Fear**: Susceptibility to terror and panic

**Corruption**: Taint from dark forces

- **Cult Affiliation**: Ties to cults and secret societies

#### Status Effects

**Stunned**: Unable to act

**Poisoned**: Damage over time

**Hallucinating**: Visual/auditory disturbances

**Paranoid**: Mental instability

- **Trembling**: Reduced dexterity
- **Corrupted**: Physical/mental changes
- **Delirious**: Complete mental breakdown

## API Endpoints

### System Health & Monitoring

`GET /v1/monitoring/health` - Get comprehensive system health status

- Returns server status, uptime, memory usage, database connectivity, and

  active connections

- HTTP 200: System is healthy or degraded (with status in response body)
- HTTP 503: System is unhealthy
- HTTP 500: Health check itself failed

#### Health Endpoint Response Examples

**Healthy System Response (200 OK):**

```json
{
  "status": "healthy",
  "timestamp": "2025-08-27T15:30:45.123456Z",
  "uptime_seconds": 12345.67,
  "version": "0.1.0",
  "components": {
    "server": {
      "status": "healthy",
      "uptime_seconds": 12345.67,
      "memory_usage_mb": 256.5,
      "cpu_usage_percent": 15.2
    },
    "database": {
      "status": "healthy",
      "connection_count": 5,
      "last_query_time_ms": 12.5
    },
    "connections": {
      "status": "healthy",
      "active_connections": 3,
      "max_connections": 100,
      "connection_rate_per_minute": 45.2
    }
  },
  "alerts": []
}
```

**Degraded System Response (200 OK):**

```json
{
  "status": "degraded",
  "timestamp": "2025-08-27T15:30:45.123456Z",
  "uptime_seconds": 12345.67,
  "version": "0.1.0",
  "components": {
    "server": {
      "status": "healthy",
      "uptime_seconds": 12345.67,
      "memory_usage_mb": 512.8,
      "cpu_usage_percent": 85.2
    },
    "database": {
      "status": "degraded",
      "connection_count": 15,
      "last_query_time_ms": 250.5
    },
    "connections": {
      "status": "healthy",
      "active_connections": 3,
      "max_connections": 100,
      "connection_rate_per_minute": 45.2
    }
  },
  "alerts": ["High memory usage: 512.8MB", "Database response time elevated"]
}
```

**Unhealthy System Response (503 Service Unavailable):**

```json
{
  "status": "unhealthy",
  "timestamp": "2025-08-27T15:30:45.123456Z",
  "uptime_seconds": 12345.67,
  "version": "0.1.0",
  "components": {
    "server": {
      "status": "unhealthy",
      "uptime_seconds": 12345.67,
      "memory_usage_mb": 2048.5,
      "cpu_usage_percent": 95.2
    },
    "database": {
      "status": "unhealthy",
      "connection_count": 0,
      "last_query_time_ms": null
    },
    "connections": {
      "status": "healthy",
      "active_connections": 3,
      "max_connections": 100,
      "connection_rate_per_minute": 45.2
    }
  },
  "alerts": [
    "Server performance critical",
    "High memory usage: 2048.5MB",
    "High CPU usage: 95.2%",
    "Database connection issues detected"
  ]
}
```

**Health Check Failure Response (500 Internal Server Error):**

```json
{
  "error": "Health check failed",
  "detail": "Database connection timeout",
  "timestamp": "2025-08-27T15:30:45.123456Z"
}
```

#### Health Endpoint Usage Guidelines

**Monitoring**: Use this endpoint for load balancer health checks and
monitoring systems

**Performance**: Response time is optimized to be under 100ms for healthy
systems

**Rate Limiting**: No rate limiting applied - designed for frequent health checks

**Authentication**: No authentication required - public endpoint for monitoring

- **Alert Thresholds**:
  - Memory usage: Warning at 1GB, critical at 1.5GB
  - CPU usage: Warning at 80%, critical at 96%
  - Database response time: Warning at 100ms, critical at 1s
  - Connection pool: Warning at 50%, critical at 80%

### World

`GET /rooms/{room_id}` - Get room information

### Player Management

`POST /players` - Create a new player

- `GET /players` - List all players
- `GET /players/{player_id}` - Get player by ID
- `GET /players/name/{player_name}` - Get player by name
- `DELETE /players/{player_id}` - Delete a player

### Memory Leak Monitoring Endpoints

The server provides comprehensive memory leak monitoring endpoints for detecting and tracking resource leaks:

#### Memory Leak Metrics Endpoints

`GET /v1/monitoring/memory-leaks` - Get comprehensive memory leak metrics from all sources

- Returns aggregated metrics from connections, events, caches, tasks, and NATS
- Includes growth rates, alerts, and trend data
- Response includes: connection metrics, event metrics, cache metrics, task metrics, NATS metrics, growth rates, and alerts

- `GET /v1/monitoring/eventbus` - Get EventBus subscriber and task metrics
  - Returns subscriber counts by event type, active task count, subscription churn rate
  - Useful for detecting event subscription leaks

- `GET /v1/monitoring/caches` - Get cache metrics with expiration tracking
  - Returns cache sizes, hit rates, expired entry counts, expiration rates, capacity utilization
  - Helps identify cache-related memory leaks

- `GET /v1/monitoring/tasks` - Get TaskRegistry metrics
  - Returns active task counts, task lifecycle metrics, service-level breakdown
  - Tracks orphaned tasks and task growth rates

#### Memory Leak Metrics Documentation

**Connection Metrics:**

- `active_websockets_count`: Number of active WebSocket connections
- `connection_metadata_count`: Number of connection metadata entries
- `player_websockets_count`: Number of players with WebSocket connections
- `closed_websockets_count`: Number of closed WebSocket IDs being tracked (potential leak indicator)
- `active_to_player_ratio`: Ratio of active connections to active players (normal: ~1.0, high indicates leaks)
- `orphaned_connections`: Connections without associated active players (indicates cleanup issues)

**Normal vs Abnormal Values:**

- `closed_websockets_count`: Normal < 1000, Warning > 5000, Critical > 10000
- `active_to_player_ratio`: Normal 0.8-1.2, Abnormal > 2.0 (multiple connections per player)
- `orphaned_connections`: Normal 0, Warning > 10

**Event Metrics:**

- `total_subscribers`: Total number of event subscribers across all event types
- `active_task_count`: Number of active async tasks in EventBus
- `subscription_churn_rate`: Rate of unsubscriptions vs subscriptions (normal: < 0.1, high indicates leaks)

**Normal vs Abnormal Values:**

- `subscription_churn_rate`: Normal < 0.1 (10%), Abnormal > 0.2 (20% growth per period)
- `active_task_count`: Should remain relatively stable, growing count indicates leaks

**Cache Metrics:**

- `cache_sizes`: Current size of each cache
- `capacity_utilization`: Percentage of max_size used (normal: < 100%, warning: > 110%)
- `expired_entry_counts`: Number of entries expired due to TTL
- `expiration_rates`: Rate of expiration vs total operations

**Normal vs Abnormal Values:**

- `capacity_utilization`: Normal < 100%, Warning > 110% (cache exceeded max_size)
- `expiration_rates`: High rates indicate TTL working correctly, low rates with high sizes indicate leaks

**Task Metrics:**

- `active_task_count`: Current number of active tasks
- `task_creation_rate`: Tasks created per hour
- `task_completion_rate`: Tasks completed per hour
- `orphaned_task_count`: Tasks that are done but not cleaned up

**Normal vs Abnormal Values:**

- `task_growth_rate`: Normal < 0.2 (20% per period), Abnormal > 0.3 (30% growth)
- `orphaned_task_count`: Normal 0, Warning > 5

**NATS Metrics:**

- `subscription_count`: Number of active NATS subscriptions
- `last_cleanup_time`: Timestamp of last subscription cleanup
- `active_subscriptions`: List of active subscription subjects

**Normal vs Abnormal Values:**

- `subscription_count`: Should match expected service subscriptions, growing count indicates leaks
- Subscriptions remaining after cleanup: Normal 0, Warning > 0

#### Example Memory Leak Metrics Response

```json
{
  "connection": {
    "active_websockets_count": 45,
    "connection_metadata_count": 45,
    "player_websockets_count": 42,
    "closed_websockets_count": 1234,
    "active_to_player_ratio": 1.07,
    "orphaned_connections": 3
  },
  "event": {
    "subscriber_counts_by_type": {
      "PlayerEnteredRoom": 2,
      "PlayerLeftRoom": 2
    },
    "total_subscribers": 4,
    "active_task_count": 1,
    "subscription_churn_rate": 0.05
  },
  "cache": {
    "cache_sizes": {
      "rooms": 1234,
      "players": 42
    },
    "capacity_utilization": {
      "rooms": 0.25,
      "players": 0.84
    },
    "expired_entry_counts": {
      "players": 156
    }
  },
  "task": {
    "active_task_count": 12,
    "tasks_by_type": {
      "lifecycle": 3,
      "websocket": 5
    },
    "task_creation_rate": 24,
    "task_completion_rate": 22,
    "orphaned_task_count": 0
  },
  "nats": {
    "active_subscriptions": ["chat.global", "chat.local"],
    "subscription_count": 2,
    "last_cleanup_time": 1704067200.0
  },
  "growth_rates": {
    "closed_websockets": 0.02,
    "subscribers": 0.0,
    "tasks": 0.05
  },
  "alerts": [],
  "timestamp": 1704067200.0
}
```

### Player Stats & Effects

`POST /players/{player_id}/lucidity-loss` - Apply lucidity loss

- `POST /players/{player_id}/fear` - Apply fear
- `POST /players/{player_id}/corruption` - Apply corruption
- `POST /players/{player_id}/occult-knowledge` - Gain occult knowledge
- `POST /players/{player_id}/heal` - Heal player
- `POST /players/{player_id}/damage` - Damage player

## Running the Server

1. Install dependencies:

   ```bash
   uv sync
   ```

2. Start the server:

   ```bash
   # Note: Hot reloading is disabled due to client compatibility issues

   uv run uvicorn main:app
   ```

3. The server will be available at `http://localhost:54731`

## Testing

Run the test script to verify the player stats system:

```bash
python test_player_stats.py
```

## Data Storage

Player data is stored as individual files in `data/local/players/player_<GUID>.json`.

- Room data is stored in `data/local/rooms/`.
- The system automatically creates these directories and handles data persistence.

## Game Mechanics

### Lucidity System

Players start with 100 lucidity

- Encountering horrors, reading forbidden texts, or learning occult knowledge

  reduces lucidity

- Low lucidity triggers status effects (paranoia, hallucinations, delirium)
- Lucidity can be recovered through rest, therapy, or certain items

### Fear System

Fear accumulates from terrifying encounters

- High fear levels cause trembling and reduced effectiveness
- Fear can be reduced through courage, experience, or certain items

### Corruption System

Corruption represents taint from dark forces

- High corruption can lead to physical/mental changes
- Corruption is difficult to remove and may be permanent

### Occult Knowledge

Learning forbidden lore increases occult knowledge

- Each point of occult knowledge gained costs 0.5 lucidity
- High occult knowledge provides access to powerful abilities but increases vulnerability

## Development

The server uses:

**FastAPI** for the web framework

**Pydantic** for data validation and serialization

**JSON** for data persistence (can be upgraded to database later)

**Asyncio** for the game loop

## Future Enhancements

Database integration (PostgreSQL/DynamoDB)

- WebSocket support for real-time communication
- Combat system integration
- NPC AI and behavior
- Quest system
- Inventory and item management
