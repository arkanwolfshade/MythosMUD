# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-10-25-subject-naming-standardization/spec.md

## Endpoints

### GET /api/health/nats/subjects

**Purpose:** Get NATS subject pattern statistics and health information
**Parameters:** None
**Response:**

```json
{
  "subject_patterns": {
    "total_patterns": 7,
    "registered_patterns": ["chat_say_room", "chat_local_subzone", "chat_global", "chat_whisper_player", "chat_system", "chat_emote_room", "chat_pose_room"],
    "validation_enabled": true,
    "cache_enabled": true
  },
  "usage_stats": {
    "total_subjects_built": 1234,
    "validation_failures": 5,
    "most_used_patterns": [
      {"pattern": "chat_say_room", "count": 456},
      {"pattern": "chat_global", "count": 234}
    ]
  },
  "performance": {
    "avg_build_time_ms": 0.5,
    "avg_validation_time_ms": 0.2,
    "cache_hit_rate": 0.95
  }
}
```

**Errors:**

- 500: Internal server error if subject manager unavailable

### POST /api/admin/nats/subjects/validate

**Purpose:** Validate a subject pattern and parameters
**Parameters:**

```json
{
  "pattern_name": "chat_say_room",
  "parameters": {
    "room_id": "arkham_1"
  }
}
```

**Response:**

```json
{
  "valid": true,
  "subject": "chat.say.room.arkham_1",
  "pattern_info": {
    "name": "chat_say_room",
    "description": "Room-level say messages",
    "required_params": ["room_id"]
  }
}
```

**Errors:**

- 400: Invalid pattern name or missing required parameters
- 422: Parameter validation failed

### GET /api/admin/nats/subjects/patterns

**Purpose:** List all registered subject patterns
**Parameters:** None
**Response:**

```json
{
  "patterns": [
    {
      "name": "chat_say_room",
      "pattern": "chat.say.room.{room_id}",
      "description": "Room-level say messages",
      "required_params": ["room_id"],
      "example": "chat.say.room.arkham_1"
    }
  ]
}
```

**Errors:** None

### POST /api/admin/nats/subjects/patterns

**Purpose:** Register a new subject pattern (admin only)
**Parameters:**

```json
{
  "name": "chat_custom_channel",
  "pattern": "chat.custom.{channel}.{scope}",
  "description": "Custom channel messages",
  "required_params": ["channel", "scope"]
}
```

**Response:**

```json
{
  "success": true,
  "pattern": {
    "name": "chat_custom_channel",
    "pattern": "chat.custom.{channel}.{scope}",
    "description": "Custom channel messages",
    "required_params": ["channel", "scope"]
  }
}
```

**Errors:**

- 400: Invalid pattern format or duplicate name
- 401: Unauthorized (admin required)
- 422: Pattern validation failed

## Controllers

### SubjectController

**Location:** `server/api/controllers/subject_controller.py`

**Actions:**

- `get_subject_stats()`: Retrieve subject pattern statistics
- `validate_subject_pattern()`: Validate subject pattern and parameters
- `list_patterns()`: List all registered patterns
- `register_pattern()`: Register new subject pattern (admin only)

**Business Logic:**

- Integrate with NATSSubjectManager for pattern operations
- Provide comprehensive error handling and validation
- Support admin-only operations for pattern management
- Cache frequently accessed pattern information

**Error Handling:**

- Validate admin permissions for pattern registration
- Provide detailed error messages for validation failures
- Handle NATSSubjectManager exceptions gracefully
- Log all pattern operations for audit purposes

## Purpose

### Subject Statistics Endpoint

**Rationale**: Monitor subject pattern usage and performance

**Integration**: Used by system administrators to track NATS subject health

**Benefits**: Provides visibility into subject usage patterns and validation performance

### Subject Validation Endpoint

**Rationale**: Allow external validation of subject patterns before use

**Integration**: Used by client applications and testing frameworks

**Benefits**: Prevents invalid subjects from being constructed and published

### Pattern Management Endpoints

**Rationale**: Enable dynamic pattern registration and management

**Integration**: Used by system administrators to add new subject patterns

**Benefits**: Allows system extension without code changes for new subject types

### Health Monitoring Integration

**Rationale**: Integrate subject health with overall NATS health monitoring

**Integration**: Connected to existing NATS health check endpoints

**Benefits**: Provides comprehensive NATS system health visibility
