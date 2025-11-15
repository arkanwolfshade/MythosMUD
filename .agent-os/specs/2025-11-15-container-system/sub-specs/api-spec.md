# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-11-15-container-system/spec.md

## Endpoints

### POST /api/containers/open

**Purpose:** Initiate interaction with a container in the player’s current room or inventory.
**Parameters:** `{ "container_id": "string" }`
**Response:** `{ "container": { ...ContainerComponent... }, "mutation_token": "string" }`
**Errors:** `404 container_not_found`, `403 access_denied`, `409 already_open`, `423 locked`

### POST /api/containers/transfer

**Purpose:** Move items between container and player inventory (bidirectional).
**Parameters:** `{ "mutation_token": "string", "container_id": "string", "direction": "to_container|to_player", "stack": {...}, "quantity": int }`
**Response:** `{ "container": {...}, "player_inventory": [...] }`
**Errors:** `400 invalid_stack`, `403 access_denied`, `409 capacity_exceeded`, `412 stale_mutation`

### POST /api/containers/close

**Purpose:** Release the mutation guard and close the container UI.
**Parameters:** `{ "container_id": "string", "mutation_token": "string" }`
**Response:** `{ "status": "closed" }`
**Errors:** `400 invalid_token`, `404 container_not_found`

### POST /api/containers/loot-all

**Purpose:** Convenience action to move all eligible stacks from container to player inventory (subject to capacity).
**Parameters:** `{ "container_id": "string", "mutation_token": "string" }`
**Response:** `{ "container": {...}, "player_inventory": [...] }`
**Errors:** `403 access_denied`, `409 capacity_exceeded`, `423 lock_active`

## WebSocket Events

- **container.opened**: `{ "container": {...}, "owner_id": "string", "expires_at": "timestamp" }`
- **container.updated**: `{ "container_id": "string", "diff": {...}, "actor_id": "string" }`
- **container.closed**: `{ "container_id": "string" }`
- **container.decayed**: `{ "container_id": "string", "room_id": "string" }`

## Controllers & Business Logic

- **ContainerController**: validates proximity, ACLs, and lock/key requirements before delegating to `ContainerService`.
- **ContainerService**: wraps `InventoryService` stack operations, applies grace-period logic for corpses, and records telemetry via enhanced logging.
- **Rate Limiting**: apply per-player plus per-container throttles (existing rate limiter middleware) to avoid spam interactions.
- **Error Handling**: map domain exceptions (`InventoryCapacityError`, `ContainerLockedError`, `MutationConflictError`) to HTTP/WS error payloads with actionable codes/messages.
