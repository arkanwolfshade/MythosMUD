# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-08-27-health-endpoint/spec.md

## Endpoints

### GET /health

**Purpose:** Provides comprehensive system health status including server availability, database connectivity, memory usage, and active connections.

**Parameters:** None

**Response:** JSON object containing health status and component metrics

**Success Response (200 OK):**

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

**Degraded Response (503 Service Unavailable):**

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
  "alerts": [
    "High memory usage detected",
    "Database response time elevated"
  ]
}
```

**Unhealthy Response (503 Service Unavailable):**

```json
{
  "status": "unhealthy",
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
    "Database connection failed",
    "Critical system component unavailable"
  ]
}

```

**Errors:**

- **500 Internal Server Error**: Health check itself failed

  ```json
  {
    "error": "Health check failed",
    "detail": "Unable to retrieve system metrics",
    "timestamp": "2025-08-27T15:30:45.123456Z"
  }

  ```

## Response Models

### HealthResponse

- `status` (string): Overall health status ("healthy", "degraded", "unhealthy")
- `timestamp` (string): ISO-8601 timestamp of health check

- `uptime_seconds` (float): Server uptime in seconds
- `version` (string): Server version
- `components` (object): Individual component health status
- `alerts` (array): List of active alerts

### ComponentStatus

- `status` (string): Component health status
- Additional fields vary by component type

### ServerComponent

- `status` (string): Server health status
- `uptime_seconds` (float): Server uptime
- `memory_usage_mb` (float): Memory usage in MB

- `cpu_usage_percent` (float): CPU usage percentage

### DatabaseComponent

- `status` (string): Database health status
- `connection_count` (integer): Active database connections
- `last_query_time_ms` (float): Last query response time

### ConnectionsComponent

- `status` (string): Connection manager health status
- `active_connections` (integer): Current active connections
- `max_connections` (integer): Maximum allowed connections
- `connection_rate_per_minute` (float): Connection rate

## Integration Notes

- Endpoint will be added to the existing monitoring router
- Leverages existing connection manager and memory monitoring systems
- Uses existing database connection pool for health checks
- Integrates with existing logging and error handling systems
