# Container System Architecture

## Overview

The unified container system provides secure storage for environmental props, wearable gear, and corpse containers. This document describes the architecture, design decisions, and implementation details of the container system.

## Table of Contents

1. [System Architecture](#system-architecture)
2. [Data Model](#data-model)
3. [Service Layer](#service-layer)
4. [Persistence Layer](#persistence-layer)
5. [API Layer](#api-layer)
6. [WebSocket Events](#websocket-events)
7. [Security and Compliance](#security-and-compliance)
8. [Lifecycle Management](#lifecycle-management)

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Client (React/TypeScript)                │
│  - Container UI Components                                  │
│  - WebSocket Event Handlers                                 │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP/WebSocket
┌──────────────────────▼──────────────────────────────────────┐
│                    API Layer (FastAPI)                       │
│  - /api/containers/open                                     │
│  - /api/containers/transfer                                 │
│  - /api/containers/close                                    │
│  - /api/containers/loot-all                                 │
│  - Rate Limiting                                            │
│  - Authentication                                           │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                  Service Layer                              │
│  - ContainerService (open/close/transfer)                  │
│  - CorpseLifecycleService (decay/cleanup)                  │
│  - WearableContainerService (equip/unequip)                │
│  - EnvironmentalContainerLoader (room loading)             │
│  - InventoryService (item stacking)                        │
│  - InventoryMutationGuard (concurrency control)            │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                Persistence Layer                            │
│  - ContainerPersistence (CRUD operations)                   │
│  - PostgreSQL Database (containers table)                  │
│  - Room Integration (environmental containers)             │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│              PostgreSQL Database                             │
│  - containers table (UUID, JSONB, indexes)                 │
│  - rooms table (with container references)                  │
└─────────────────────────────────────────────────────────────┘
```

### Component Relationships

```
ContainerService
├── PersistenceLayer (container CRUD)
├── InventoryService (item stacking)
├── InventoryMutationGuard (concurrency)
└── Access Control (proximity, ownership, roles, grace periods)

CorpseLifecycleService
├── PersistenceLayer (container CRUD)
├── TimeService (decay timers)
└── ConnectionManager (WebSocket events)

WearableContainerService
├── PersistenceLayer (container CRUD)
└── EquipmentService (equip/unequip integration)

EnvironmentalContainerLoader
├── PersistenceLayer (container CRUD)
└── Room JSON Schema (container definitions)
```

## Data Model

### ContainerComponent (Pydantic Model)

The `ContainerComponent` model serves as the data contract for all container types:

```python
class ContainerComponent(BaseModel):
    container_id: UUID                    # Unique container instance ID
    source_type: ContainerSourceType      # environment | equipment | corpse
    owner_id: UUID | None                 # Owner UUID (for corpses/equipment)
    room_id: str | None                   # Room ID (for environment/corpse)
    entity_id: UUID | None                # Entity UUID (for equipment)
    lock_state: ContainerLockState        # unlocked | locked | sealed
    capacity_slots: int                   # 1-20 slots
    weight_limit: int | None              # Optional weight limit
    decay_at: datetime | None             # Decay timestamp (corpses)
    allowed_roles: list[str]              # Role-based access control
    items: list[InventoryStack]           # Container contents
    metadata: dict[str, Any]              # Container-specific metadata
```

### Container Source Types

1. **Environment**: Containers in rooms (chests, barrels, etc.)
   - Requires `room_id`
   - Accessible by players in same room
   - Can have role-based restrictions

2. **Equipment**: Wearable containers (backpacks, bandoliers, etc.)
   - Requires `entity_id` (player/NPC UUID)
   - Only accessible by owner
   - Created on equip, preserved on unequip

3. **Corpse**: Containers created on player/NPC death
   - Requires `room_id` and `owner_id`
   - Grace period for owner-only access
   - Automatic decay and cleanup

### Database Schema

```sql
CREATE TABLE containers (
    container_instance_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_type TEXT NOT NULL,
    owner_id UUID NULL,
    room_id TEXT NULL,
    entity_id UUID NULL,
    lock_state TEXT NOT NULL DEFAULT 'unlocked',
    capacity_slots INTEGER NOT NULL CHECK (capacity_slots >= 1 AND capacity_slots <= 20),
    weight_limit INTEGER NULL,
    decay_at TIMESTAMPTZ NULL,
    allowed_roles JSONB NOT NULL DEFAULT '[]'::jsonb,
    items JSONB NOT NULL DEFAULT '[]'::jsonb,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_containers_room ON containers(room_id);
CREATE INDEX idx_containers_entity ON containers(entity_id);
CREATE INDEX idx_containers_owner ON containers(owner_id);
```

## Service Layer

### ContainerService

Orchestrates container operations with mutation guards and access control.

**Key Methods**:
- `open_container()`: Opens container, validates access, returns mutation token
- `close_container()`: Closes container, releases mutation guard
- `transfer_to_container()`: Moves items from player to container
- `transfer_from_container()`: Moves items from container to player
- `loot_all()`: Transfers all items from container to player

**Access Control**:
- Proximity check (environment/corpse containers)
- Ownership check (equipment containers)
- Role-based access control
- Corpse grace period enforcement

### CorpseLifecycleService

Manages corpse container lifecycle from creation to decay.

**Key Methods**:
- `create_corpse_on_death()`: Creates corpse container with grace period
- `can_access_corpse()`: Validates access during grace period
- `is_corpse_decayed()`: Checks if decay timer has expired
- `cleanup_decayed_corpse()`: Removes decayed corpse and redistributes items

**Lifecycle**:
1. Player dies → `create_corpse_on_death()` called
2. Grace period (default 5 minutes) → owner-only access
3. Decay timer (default 1 hour) → automatic cleanup
4. Cleanup → items redistributed, container removed

### WearableContainerService

Manages wearable container integration with equipment system.

**Key Methods**:
- `handle_equip_wearable_container()`: Creates container on equip
- `handle_unequip_wearable_container()`: Preserves container on unequip
- `get_wearable_containers_for_player()`: Retrieves player's wearable containers
- `handle_container_overflow()`: Manages inventory spill rules

**Integration**:
- Hooks into `EquipmentService.equip_from_inventory()`
- Hooks into `EquipmentService.unequip_to_inventory()`
- Updates `inner_container` in item stacks

### EnvironmentalContainerLoader

Loads environmental container definitions from room JSON and migrates to PostgreSQL.

**Key Methods**:
- `load_container_from_room_json()`: Parses container definition from room JSON
- `migrate_room_container_to_postgresql()`: Creates container in database

**Integration**:
- Called during world loading
- Room JSON schema includes optional `container` block
- Containers loaded with room data

## Persistence Layer

### Container Persistence Functions

Located in `server/persistence/container_persistence.py`:

- `create_container()`: Creates new container in database
- `get_container()`: Retrieves container by UUID
- `get_containers_by_room_id()`: Retrieves all containers in a room
- `get_containers_by_entity_id()`: Retrieves all containers for an entity
- `get_decayed_containers()`: Retrieves decayed corpse containers
- `update_container()`: Updates container data
- `delete_container()`: Removes container from database

### Integration with PersistenceLayer

The main `PersistenceLayer` class provides wrapper methods that delegate to container persistence functions, ensuring thread-safe access and proper connection management.

## API Layer

### Endpoints

All endpoints are in `server/api/containers.py`:

- `POST /api/containers/open`: Open container
- `POST /api/containers/transfer`: Transfer items (bidirectional)
- `POST /api/containers/close`: Close container
- `POST /api/containers/loot-all`: Loot all items

### Rate Limiting

All endpoints are rate limited to **20 requests per 60 seconds per player**.

### Authentication

All endpoints require JWT authentication via `Authorization: Bearer <token>` header.

### Error Handling

Standardized error responses with appropriate HTTP status codes:
- `400 Bad Request`: Invalid request data
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Access denied
- `404 Not Found`: Container not found
- `409 Conflict`: Capacity exceeded
- `423 Locked`: Container is locked
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error

## WebSocket Events

Real-time events emitted for container state changes:

### container.opened

Emitted when a container is opened.

**Recipients**: Opening player (private event)

**Event Data**:
```json
{
  "type": "container.opened",
  "data": {
    "container_id": "...",
    "container": {...},
    "mutation_token": "...",
    "expires_at": "..."
  }
}
```

### container.updated

Emitted when container contents are modified.

**Recipients**: All players in room (broadcast event)

**Event Data**:
```json
{
  "type": "container.updated",
  "data": {
    "container_id": "...",
    "diff": {
      "items": {
        "added": [...],
        "removed": [...]
      }
    }
  }
}
```

### container.closed

Emitted when a container is closed.

**Recipients**: All players in room (broadcast event)

**Event Data**:
```json
{
  "type": "container.closed",
  "data": {
    "container_id": "..."
  }
}
```

### container.decayed

Emitted when a corpse container decays.

**Recipients**: All players in room (broadcast event)

**Event Data**:
```json
{
  "type": "container.decayed",
  "data": {
    "container_id": "..."
  }
}
```

## Security and Compliance

### Audit Logging

All container operations are logged to audit logs with:
- Timestamp
- Player ID and name
- Container ID
- Operation type
- Security level
- Compliance flags

### COPPA Compliance

Container metadata is validated to prevent storage of personal information:
- Email addresses
- Phone numbers
- Physical addresses
- Real names
- Birth dates
- Ages
- IP addresses
- User agents
- Session IDs

### Mutation Guards

All container operations use `InventoryMutationGuard` to prevent:
- Race conditions
- Duplicate operations
- Concurrent modifications

### Access Control

Multi-layered access control:
1. **Proximity**: Player must be in same room (environment/corpse)
2. **Ownership**: Player must own container (equipment)
3. **Roles**: Player must have required role (if specified)
4. **Grace Period**: Corpse owner has exclusive access during grace period

### Rate Limiting

Per-player rate limiting prevents abuse:
- 20 requests per 60 seconds
- Metrics tracked for telemetry
- Violations logged for security monitoring

## Lifecycle Management

### Environmental Containers

1. **Definition**: Defined in room JSON with `container` block
2. **Migration**: Loaded into PostgreSQL during world loading
3. **Loading**: Attached to `Room` objects when rooms are loaded
4. **Access**: Players in room can interact with containers
5. **Persistence**: Containers persist across server restarts

### Wearable Containers

1. **Equip**: Container created in PostgreSQL when item equipped
2. **Use**: Player can access container while equipped
3. **Unequip**: Container state preserved in item's `inner_container`
4. **Re-equip**: Existing container reused if available

### Corpse Containers

1. **Creation**: Created on player/NPC death with grace period
2. **Grace Period**: Owner has exclusive access (default 5 minutes)
3. **Public Access**: After grace period, all players can access
4. **Decay**: Container decays after timer expires (default 1 hour)
5. **Cleanup**: Decayed containers removed, items redistributed

## Design Decisions

### Why PostgreSQL Instead of SQLite?

- UUID support for player and container IDs
- JSONB for flexible item and metadata storage
- Better concurrency for multiplayer scenarios
- Production-ready scalability

### Why Mutation Guards?

- Prevents race conditions in multiplayer scenarios
- Ensures idempotent operations
- Prevents duplicate transfers
- Provides audit trail

### Why Separate Services?

- Single Responsibility Principle
- Easier testing and maintenance
- Clear separation of concerns
- Reusable components

### Why Audit Logging?

- Security compliance requirements
- Forensic analysis capabilities
- Player behavior monitoring
- Incident response support

## Future Enhancements

- Weight-based capacity limits
- Container locking with keys
- Container permissions (read-only, write-only)
- Container sharing between players
- Container templates for world builders
- Container analytics and metrics
