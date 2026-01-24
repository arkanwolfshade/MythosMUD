# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-09-22-npc-subsystem/spec.md

## Endpoints

### GET /api/admin/npcs

**Purpose:** Retrieve all NPC definitions and their current status
**Parameters:**

- `zone_id` (optional): Filter by zone

- `npc_type` (optional): Filter by NPC type

- `include_inactive` (optional): Include inactive NPCs

**Response:**

```json
{
  "npcs": [
    {
      "id": 1,
      "name": "Blacksmith Bob",
      "npc_type": "shopkeeper",
      "zone_id": "arkham",
      "room_id": "arkham_1",
      "required_npc": true,
      "current_population": 1,
      "max_population": 1,
      "status": "active",
      "last_seen": "2025-09-22T12:00:00Z"
    }
  ]
}
```

**Errors:** 401 (Unauthorized), 403 (Forbidden)

### POST /api/admin/npcs

**Purpose:** Create a new NPC definition
**Parameters:**

```json
{
  "name": "Guard Captain",
  "description": "A stern guard captain",
  "npc_type": "aggressive_mob",
  "zone_id": "arkham",
  "room_id": "arkham_2",
  "required_npc": false,
  "max_population": 3,
  "spawn_probability": 0.8,
  "base_stats": {
    "hp": 100,
    "mp": 50,
    "str": 15,
    "dex": 12
  },
  "behavior_config": {
    "aggression_level": 0.7,
    "territory_radius": 2,
    "hunt_players": true
  }
}
```

**Response:**

```json
{
  "id": 2,
  "status": "created",
  "message": "NPC definition created successfully"
}
```

**Errors:** 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 409 (Conflict)

### PUT /api/admin/npcs/{npc_id}

**Purpose:** Update an existing NPC definition
**Parameters:**

- `npc_id`: NPC definition ID

- Request body: Same as POST but with updated fields

**Response:**

```json
{
  "id": 2,
  "status": "updated",
  "message": "NPC definition updated successfully"
}
```

**Errors:** 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found)

### DELETE /api/admin/npcs/{npc_id}

**Purpose:** Delete an NPC definition
**Parameters:**

- `npc_id`: NPC definition ID

**Response:**

```json
{
  "status": "deleted",
  "message": "NPC definition deleted successfully"
}
```

**Errors:** 401 (Unauthorized), 403 (Forbidden), 404 (Not Found), 409 (Conflict - NPCs currently spawned)

### POST /api/admin/npcs/{npc_id}/spawn

**Purpose:** Manually spawn an NPC instance
**Parameters:**

- `npc_id`: NPC definition ID

- `room_id` (optional): Override spawn room

**Response:**

```json
{
  "npc_instance_id": "npc_12345",
  "status": "spawned",
  "room_id": "arkham_1",
  "message": "NPC spawned successfully"
}
```

**Errors:** 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found), 409 (Max population reached)

### DELETE /api/admin/npcs/instances/{instance_id}

**Purpose:** Remove a specific NPC instance
**Parameters:**

- `instance_id`: NPC instance ID

**Response:**

```json
{
  "status": "removed",
  "message": "NPC instance removed successfully"
}
```

**Errors:** 401 (Unauthorized), 403 (Forbidden), 404 (Not Found)

### GET /api/admin/npcs/instances

**Purpose:** Get all currently active NPC instances
**Parameters:**

- `zone_id` (optional): Filter by zone

- `room_id` (optional): Filter by room

**Response:**

```json
{
  "instances": [
    {
      "instance_id": "npc_12345",
      "npc_definition_id": 1,
      "name": "Blacksmith Bob",
      "zone_id": "arkham",
      "room_id": "arkham_1",
      "current_hp": 100,
      "current_mp": 50,
      "status": "active",
      "spawned_at": "2025-09-22T12:00:00Z"
    }
  ]
}
```

**Errors:** 401 (Unauthorized), 403 (Forbidden)

### GET /api/admin/npcs/debug/{instance_id}

**Purpose:** Get detailed debug information for an NPC instance
**Parameters:**

- `instance_id`: NPC instance ID

**Response:**

```json
{
  "instance_id": "npc_12345",
  "npc_definition_id": 1,
  "name": "Blacksmith Bob",
  "current_state": "idle",
  "behavior_stack": ["wander", "respond_to_players"],
  "memory": {
    "last_player_interaction": "2025-09-22T12:05:00Z",
    "recent_events": ["player_entered_room", "combat_started"]
  },
  "performance_metrics": {
    "think_time_avg": 5.2,
    "message_queue_size": 3,
    "last_think": "2025-09-22T12:10:00Z"
  }
}
```

**Errors:** 401 (Unauthorized), 403 (Forbidden), 404 (Not Found)

### POST /api/admin/npcs/instances/{instance_id}/command

**Purpose:** Send a command to a specific NPC instance (debugging)
**Parameters:**

- `instance_id`: NPC instance ID

- Request body:

```json
{
  "command": "say",
  "args": ["Hello, player!"],
  "target_player_id": "player_123" // optional
}
```

**Response:**

```json
{
  "status": "command_sent",
  "message": "Command queued for NPC execution"
}
```

**Errors:** 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found)

### GET /api/admin/npcs/zones/{zone_id}/population

**Purpose:** Get population statistics for a zone
**Parameters:**

- `zone_id`: Zone identifier

**Response:**

```json
{
  "zone_id": "arkham",
  "total_npcs": 15,
  "required_npcs": 3,
  "optional_npcs": 12,
  "population_by_type": {
    "shopkeeper": 2,
    "quest_giver": 1,
    "passive_mob": 8,
    "aggressive_mob": 4
  },
  "spawn_capacity": {
    "current": 15,
    "max": 25,
    "utilization": 0.6
  }
}
```

**Errors:** 401 (Unauthorized), 403 (Forbidden), 404 (Zone not found)

## Controllers

### NPC Management Controller

**Business Logic**: CRUD operations for NPC definitions, validation of NPC types and configurations

**Error Handling**: Comprehensive validation for NPC creation/updates, conflict resolution for population limits

**Integration**: Database operations, configuration validation, spawn rule processing

### NPC Instance Controller

**Business Logic**: NPC spawning/despawning, instance lifecycle management, population control

**Error Handling**: Population limit enforcement, spawn condition validation, instance state management

**Integration**: Message queue operations, zone management, real-time state updates

### NPC Debug Controller

**Business Logic**: Debug information gathering, performance metrics, command injection for testing

**Error Handling**: Instance existence validation, debug data sanitization

**Integration**: NPC thread communication, performance monitoring, admin command processing

## Purpose

### Admin Management

**NPC Definition Management**: Create, update, delete NPC types and configurations

**Population Control**: Monitor and adjust NPC populations per zone

**Spawn Management**: Manual spawning/despawning for testing and maintenance

### Debugging and Monitoring

**Instance Debugging**: Detailed information about NPC state and behavior

**Performance Monitoring**: Metrics for NPC processing and message queue health

**Command Injection**: Direct NPC control for testing and troubleshooting

### Integration Points

**Zone Management**: Integration with existing zone/room system

**Player Management**: NPC-player interaction monitoring and control

**System Health**: NPC subsystem health monitoring and alerting
