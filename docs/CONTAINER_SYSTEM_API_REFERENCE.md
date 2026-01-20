# Container System API Reference

## Overview

The unified container system provides secure storage for environmental props, wearable gear, and corpse containers. All
container operations are audited for security and compliance, with proper access control, rate limiting, and mutation
guards.

## Table of Contents

1. [Container Endpoints](#container-endpoints)
2. [WebSocket Events](#websocket-events)
3. [Authentication](#authentication)
4. [Rate Limiting](#rate-limiting)
5. [Error Handling](#error-handling)
6. [Examples](#examples)

## Container Endpoints

All container endpoints are prefixed with `/api/containers` and require authentication.

### Open Container

**Endpoint**: `POST /api/containers/open`

**Purpose**: Open a container for interaction. Returns container data and a mutation token required for subsequent
operations.

**Request Body**:

```json
{
  "container_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

**Response** (200 OK):

```json
{
  "container": {
    "container_id": "550e8400-e29b-41d4-a716-446655440000",
    "source_type": "environment",
    "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
    "capacity_slots": 10,
    "lock_state": "unlocked",
    "items": [
      {
        "item_instance_id": "inst_item_001",
        "prototype_id": "test_item",
        "item_id": "test_item",
        "item_name": "Test Item",
        "slot_type": "backpack",
        "quantity": 1
      }
    ],
    "metadata": {
      "key_item_id": "key_001",
      "description": "A locked chest"
    }
  },
  "mutation_token": "abc123-def456-ghi789",
  "expires_at": "2025-01-01T12:00:00Z"
}
```

**Errors**:

- `401 Unauthorized`: Authentication required
- `404 Not Found`: Container not found
- `403 Forbidden`: Access denied (not in same room, wrong role, grace period active)
- `423 Locked`: Container is locked and player doesn't have key
- `429 Too Many Requests`: Rate limit exceeded (20 requests per 60 seconds)
- `500 Internal Server Error`: Server error

**Rate Limiting**: 20 requests per 60 seconds per player

### Transfer Items to Container

**Endpoint**: `POST /api/containers/transfer`

**Purpose**: Transfer items from player inventory to container.

**Request Body**:

```json
{
  "container_id": "550e8400-e29b-41d4-a716-446655440000",
  "mutation_token": "abc123-def456-ghi789",
  "direction": "to_container",
  "item": {
    "item_instance_id": "inst_item_001",
    "prototype_id": "test_item",
    "item_id": "test_item",
    "item_name": "Test Item",
    "slot_type": "backpack",
    "quantity": 1
  },
  "quantity": 1
}
```

**Response** (200 OK):

```json
{
  "container": {
    "container_id": "550e8400-e29b-41d4-a716-446655440000",
    "items": [...]
  },
  "player_inventory": [...]
}
```

**Errors**:

- `401 Unauthorized`: Authentication required
- `404 Not Found`: Container not found or not open
- `400 Bad Request`: Invalid mutation token or container not open
- `409 Conflict`: Container capacity exceeded
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error

**Rate Limiting**: 20 requests per 60 seconds per player

### Transfer Items from Container

**Endpoint**: `POST /api/containers/transfer`

**Purpose**: Transfer items from container to player inventory.

**Request Body**:

```json
{
  "container_id": "550e8400-e29b-41d4-a716-446655440000",
  "mutation_token": "abc123-def456-ghi789",
  "direction": "from_container",
  "item": {
    "item_instance_id": "inst_item_001",
    "prototype_id": "test_item",
    "item_id": "test_item",
    "item_name": "Test Item",
    "slot_type": "backpack",
    "quantity": 1
  },
  "quantity": 1
}
```

**Response** (200 OK):

```json
{
  "container": {
    "container_id": "550e8400-e29b-41d4-a716-446655440000",
    "items": [...]
  },
  "player_inventory": [...]
}
```

**Errors**: Same as "Transfer Items to Container"

**Rate Limiting**: 20 requests per 60 seconds per player

### Close Container

**Endpoint**: `POST /api/containers/close`

**Purpose**: Close a container and release the mutation guard.

**Request Body**:

```json
{
  "container_id": "550e8400-e29b-41d4-a716-446655440000",
  "mutation_token": "abc123-def456-ghi789"
}
```

**Response** (200 OK):

```json
{
  "success": true,
  "message": "Container closed"
}
```

**Errors**:

- `401 Unauthorized`: Authentication required
- `404 Not Found`: Container not found or not open
- `400 Bad Request`: Invalid mutation token
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error

**Rate Limiting**: 20 requests per 60 seconds per player

### Loot All Items

**Endpoint**: `POST /api/containers/loot-all`

**Purpose**: Transfer all eligible items from container to player inventory in a single operation.

**Request Body**:

```json
{
  "container_id": "550e8400-e29b-41d4-a716-446655440000",
  "mutation_token": "abc123-def456-ghi789"
}
```

**Response** (200 OK):

```json
{
  "container": {
    "container_id": "550e8400-e29b-41d4-a716-446655440000",
    "items": []
  },
  "player_inventory": [...]
}
```

**Errors**: Same as "Transfer Items from Container"

**Rate Limiting**: 20 requests per 60 seconds per player

## WebSocket Events

The container system emits real-time WebSocket events for container state changes.

### container.opened

Emitted when a container is opened by a player.

**Event Data**:

```json
{
  "type": "container.opened",
  "data": {
    "container_id": "550e8400-e29b-41d4-a716-446655440000",
    "container": {...},
    "mutation_token": "abc123-def456-ghi789",
    "expires_at": "2025-01-01T12:00:00Z"
  },
  "player_id": "player-uuid",
  "room_id": "earth_arkhamcity_sanitarium_room_foyer_001"
}
```

### container.updated

Emitted when container contents are modified.

**Event Data**:

```json
{
  "type": "container.updated",
  "data": {
    "container_id": "550e8400-e29b-41d4-a716-446655440000",
    "diff": {
      "items": {
        "added": [...],
        "removed": [...]
      }
    }
  },
  "actor_id": "player-uuid",
  "room_id": "earth_arkhamcity_sanitarium_room_foyer_001"
}
```

### container.closed

Emitted when a container is closed.

**Event Data**:

```json
{
  "type": "container.closed",
  "data": {
    "container_id": "550e8400-e29b-41d4-a716-446655440000"
  },
  "player_id": "player-uuid",
  "room_id": "earth_arkhamcity_sanitarium_room_foyer_001"
}
```

### container.decayed

Emitted when a corpse container decays and is cleaned up.

**Event Data**:

```json
{
  "type": "container.decayed",
  "data": {
    "container_id": "550e8400-e29b-41d4-a716-446655440000"
  },
  "room_id": "earth_arkhamcity_sanitarium_room_foyer_001"
}
```

## Authentication

All container endpoints require authentication via JWT token in the `Authorization` header:

```
Authorization: Bearer <JWT_TOKEN>
```

## Rate Limiting

All container endpoints are rate limited to **20 requests per 60 seconds per player**.

When rate limit is exceeded, the API returns:

- Status Code: `429 Too Many Requests`
- Response: `{"detail": "Rate limit exceeded. Retry after <seconds> seconds"}`

## Error Handling

All errors follow the standard error response format:

```json
{
  "detail": "Error message",
  "error_code": "CONTAINER_NOT_FOUND",
  "context": {
    "container_id": "...",
    "player_id": "..."
  }
}
```

### Common Error Codes

`CONTAINER_NOT_FOUND`: Container does not exist

- `CONTAINER_LOCKED`: Container is locked and player doesn't have key
- `CONTAINER_ACCESS_DENIED`: Player doesn't have access (wrong room, role, or grace period)
- `CONTAINER_CAPACITY_EXCEEDED`: Container is full
- `INVALID_MUTATION_TOKEN`: Mutation token is invalid or expired
- `RATE_LIMIT_EXCEEDED`: Too many requests

## Examples

### Complete Workflow: Opening and Looting a Container

```javascript
// 1. Open container
const openResponse = await fetch('/api/containers/open', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    container_id: '550e8400-e29b-41d4-a716-446655440000'
  })
});

const { container, mutation_token } = await openResponse.json();

// 2. Transfer item to container
await fetch('/api/containers/transfer', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    container_id: container.container_id,
    mutation_token: mutation_token,
    direction: 'to_container',
    item: {
      item_instance_id: 'inst_item_001',
      prototype_id: 'test_item',
      item_id: 'test_item',
      item_name: 'Test Item',
      slot_type: 'backpack',
      quantity: 1
    }
  })
});

// 3. Loot all items
await fetch('/api/containers/loot-all', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    container_id: container.container_id,
    mutation_token: mutation_token
  })
});

// 4. Close container
await fetch('/api/containers/close', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    container_id: container.container_id,
    mutation_token: mutation_token
  })
});
```

## Security and Compliance

All container operations are **audit logged** for security and compliance

- Container metadata is validated to ensure **COPPA compliance** (no personal data)
- All operations use **mutation guards** to prevent race conditions
- **Rate limiting** prevents abuse and DoS attacks
- **Access control** enforces proximity, ownership, roles, and grace periods
