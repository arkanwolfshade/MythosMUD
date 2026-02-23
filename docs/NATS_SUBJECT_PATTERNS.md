# NATS Subject Pattern Management

> _As noted in the restricted archives of Miskatonic University, proper subject naming conventions are essential for
> maintaining the integrity of our messaging infrastructure across dimensional boundaries._

## Overview

The NATS Subject Manager provides centralized management of NATS subject naming conventions for MythosMUD's real-time
messaging system. It eliminates hardcoded subject strings, provides validation, and enables dynamic pattern
registration.

### Key Features

**Centralized Pattern Management**: All subject patterns defined in one location

**Type-Safe Subject Building**: Compile-time parameter validation

**Performance Monitoring**: Built-in metrics for all operations

**Caching**: Automatic caching of validation results

**Dynamic Registration**: Runtime pattern registration without code changes

- **Admin API**: REST endpoints for pattern management and monitoring

## Architecture

### Pattern Hierarchy

Subject patterns follow a hierarchical structure:

```
{service}.{channel}.{scope}.{identifier}
```

**Components:**

- `service`: Top-level service category (chat, events, combat)
- `channel`: Communication channel or event type (say, local, attack)
- `scope`: Scope of the message (room, subzone, player)
- `identifier`: Unique identifier (room_id, player_id, etc.)

### Example Patterns

```python
chat.say.room.{room_id}           # Room-level say messages
chat.local.subzone.{subzone}      # Subzone-level local messages
chat.global                       # Global chat (no parameters)
chat.whisper.player.{target_id}   # Player whispers
events.player_entered.{room_id}   # Player entered room events
combat.attack.{room_id}           # Combat attack events
```

## Usage

### Basic Usage

```python
from server.services.nats_subject_manager import nats_subject_manager

# Build a subject for room-level say message

subject = nats_subject_manager.build_subject(
    "chat_say_room",
    room_id="arkham_university_library"
)
# Result: "chat.say.room.arkham_university_library"

# Validate a subject

is_valid = nats_subject_manager.validate_subject("chat.say.room.test_room")
# Result: True

```

### Publishing Messages

```python
from server.services.nats_service import nats_service
from server.services.nats_subject_manager import nats_subject_manager

# Build subject using pattern

subject = nats_subject_manager.build_subject(
    "chat_say_room",
    room_id=player.current_room_id
)

# Publish message

await nats_service.publish(subject, {
    "message_id": message_id,
    "sender_id": player.player_id,
    "sender_name": player.name,
    "channel": "say",
    "content": message_content,
    "room_id": player.current_room_id,
})
```

### Subscribing to Messages

```python
from server.services.nats_subject_manager import nats_subject_manager

# Get subscription pattern with wildcards

subscription_pattern = nats_subject_manager.get_subscription_pattern("chat_say_room")
# Result: "chat.say.room.*"

# Subscribe to pattern

await nats_service.subscribe(subscription_pattern, message_handler)

# Or get all chat subscription patterns

chat_patterns = nats_subject_manager.get_chat_subscription_patterns()
for pattern in chat_patterns:
    await nats_service.subscribe(pattern, message_handler)
```

## Predefined Patterns

### Chat Patterns

| Pattern Name          | Subject Template                  | Parameters | Description                  |
| --------------------- | --------------------------------- | ---------- | ---------------------------- |
| `chat_say_room`       | `chat.say.room.{room_id}`         | room_id    | Room-level say messages      |
| `chat_local_subzone`  | `chat.local.subzone.{subzone}`    | subzone    | Subzone-level local messages |
| `chat_global`         | `chat.global`                     | -          | Global chat messages         |
| `chat_whisper_player` | `chat.whisper.player.{target_id}` | target_id  | Player-to-player whispers    |
| `chat_system`         | `chat.system`                     | -          | System-wide messages         |
| `chat_emote_room`     | `chat.emote.room.{room_id}`       | room_id    | Room-level emote messages    |
| `chat_pose_room`      | `chat.pose.room.{room_id}`        | room_id    | Room-level pose messages     |
| `chat_party_group`    | `chat.party.group.{party_id}`     | party_id   | Party group chat             |

### Event Patterns

| Pattern Name                    | Subject Template                           | Parameters | Description                |
| ------------------------------- | ------------------------------------------ | ---------- | -------------------------- |
| `event_player_entered`          | `events.player_entered.{room_id}`          | room_id    | Player entered room events |
| `event_player_left`             | `events.player_left.{room_id}`             | room_id    | Player left room events    |
| `event_game_tick`               | `events.game_tick`                         | -          | Global game tick events    |
| `event_player_mortally_wounded` | `events.player_mortally_wounded.{room_id}` | room_id    | Player mortally wounded    |
| `event_player_hp_decay`         | `events.player_hp_decay.{room_id}`         | room_id    | Player HP decay events     |
| `event_player_died`             | `events.player_died.{room_id}`             | room_id    | Player death events        |
| `event_player_respawned`        | `events.player_respawned.{room_id}`        | room_id    | Player respawn events      |

### Combat Patterns

| Pattern Name          | Subject Template                | Parameters | Description           |
| --------------------- | ------------------------------- | ---------- | --------------------- |
| `combat_attack`       | `combat.attack.{room_id}`       | room_id    | Combat attack events  |
| `combat_npc_attacked` | `combat.npc_attacked.{room_id}` | room_id    | NPC attacked events   |
| `combat_npc_action`   | `combat.npc_action.{room_id}`   | room_id    | NPC action events     |
| `combat_started`      | `combat.started.{room_id}`      | room_id    | Combat started events |
| `combat_ended`        | `combat.ended.{room_id}`        | room_id    | Combat ended events   |
| `combat_npc_died`     | `combat.npc_died.{room_id}`     | room_id    | NPC death events      |

## Dynamic Pattern Registration

Administrators can register new patterns at runtime via the Admin API:

```python
POST /api/admin/nats/subjects/patterns
{
    "name": "chat_party_group",
    "pattern": "chat.party.group.{party_id}",
    "required_params": ["party_id"],
    "description": "Party group messages"
}
```

Or programmatically:

```python
manager.register_pattern(
    name="chat_party_group",
    pattern="chat.party.group.{party_id}",
    required_params=["party_id"],
    description="Party group messages"
)
```

## Performance Optimization

### Caching

The subject manager implements two levels of caching:

1. **Validation Result Caching**: Caches subject validation results
   - Provides 5-8x speedup for repeated validations
   - Automatic cache invalidation when patterns change
   - Configurable via `enable_cache` parameter

2. **Pattern Compilation Caching**: Pre-compiles regex patterns
   - Used for component validation
   - Eliminates runtime compilation overhead

### Performance Metrics

The subject manager tracks comprehensive performance metrics:

```python
metrics = manager.get_performance_metrics()

# Returns

{
    "validation": {
        "total_count": 1000,
        "success_count": 950,
        "failure_count": 50,
        "success_rate": 0.95,
        "avg_time_ms": 0.05,
        "p95_time_ms": 0.12
    },
    "cache": {
        "hits": 900,
        "misses": 100,
        "hit_rate": 0.9
    },
    "build": {
        "total_count": 500,
        "success_count": 498,
        "failure_count": 2,
        "success_rate": 0.996,
        "avg_time_ms": 0.03,
        "p95_time_ms": 0.08
    },
    "errors": {
        "pattern_not_found": 1,
        "missing_parameter": 1,
        "validation_errors": 0,
        "total_errors": 2
    }
}
```

### Performance Benchmarks

Established performance baselines:

**Build Subject**: < 0.01ms per operation (100,000+ ops/sec)

**Validate Subject (no cache)**: < 0.05ms per operation (20,000+ ops/sec)

**Validate Subject (cached)**: < 0.01ms per operation (100,000+ ops/sec)

**Cache Speedup**: 5-8x for repeated validations

**Metrics Overhead**: < 30% performance impact

- **Concurrent Operations**: Thread-safe, supports concurrent access

## Admin API Reference

### GET /api/admin/nats/subjects/health

Get subject management statistics and health status.

**Response:**

```json
{
    "status": "healthy",
    "metrics": { ... },
    "patterns_registered": 20,
    "cache_enabled": true,
    "strict_validation": false
}
```

### POST /api/admin/nats/subjects/validate

Validate a NATS subject against registered patterns.

**Request:**

```json
{
  "subject": "chat.say.room.arkham_1"
}
```

**Response:**

```json
{
  "subject": "chat.say.room.arkham_1",
  "is_valid": true,
  "validation_time_ms": 0.05,
  "details": null
}
```

### GET /api/admin/nats/subjects/patterns

Get all registered subject patterns.

**Response:**

```json
{
    "patterns": {
        "chat_say_room": {
            "name": "chat_say_room",
            "pattern": "chat.say.room.{room_id}",
            "required_params": ["room_id"],
            "description": "Room-level say messages"
        },
        ...
    },
    "total_count": 20
}
```

### POST /api/admin/nats/subjects/patterns

Register a new subject pattern (admin-only).

**Request:**

```json
{
  "name": "chat_party_group",
  "pattern": "chat.party.group.{party_id}",
  "required_params": ["party_id"],
  "description": "Party group messages"
}
```

**Response:**

```json
{
  "success": true,
  "pattern_name": "chat_party_group",
  "message": "Pattern registered successfully"
}
```

## Migration Guide

### Migrating from Hardcoded Subjects

**Before** (hardcoded subject strings):

```python
# Old approach - error-prone hardcoded strings

subject = f"chat.say.{room_id}"  # Risk of typos and inconsistency
await nats_service.publish(subject, data)
```

**After** (standardized patterns):

```python
# New approach - type-safe pattern-based subjects

subject = nats_subject_manager.build_subject(
    "chat_say_room",  # Pattern name prevents typos
    room_id=room_id
)
await nats_service.publish(subject, data)
```

### Migration Steps

1. **Identify hardcoded subjects**: Search codebase for `f"chat.` or direct string construction
2. **Map to patterns**: Determine which predefined pattern matches the subject
3. **Replace with build_subject()**: Use pattern name and parameters
4. **Test validation**: Verify subjects are valid using `validate_subject()`
5. **Update subscriptions**: Use `get_subscription_pattern()` for wildcard patterns

### ChatService Migration Example

**Before:**

```python
# Hardcoded subject construction

subject = f"chat.say.{room_id}"
```

**After:**

```python
# Pattern-based subject construction

subject = self.subject_manager.build_subject(
    "chat_say_room",
    room_id=room_id
)
```

## Error Handling

### Pattern Not Found

```python
try:
    subject = manager.build_subject("nonexistent_pattern", param="value")
except PatternNotFoundError as e:
    logger.error("Pattern not found", pattern_name="nonexistent_pattern", error=str(e))
```

### Missing Parameters

```python
try:
    subject = manager.build_subject("chat_say_room")  # Missing room_id
except MissingParameterError as e:
    logger.error("Missing required parameters", error=str(e))
```

### Invalid Parameter Values

```python
try:
    subject = manager.build_subject("chat_say_room", room_id="invalid@chars")
except SubjectValidationError as e:
    logger.error("Invalid parameter value", error=str(e))
```

## Configuration

### Initialization Options

```python
from server.services.nats_subject_manager import NATSSubjectManager

manager = NATSSubjectManager(
    enable_cache=True,              # Enable validation caching (default: True)
    max_subject_length=255,         # Max subject length (NATS limit)
    strict_validation=False,        # Strict mode: no underscores (default: False)
    enable_metrics=True             # Enable performance metrics (default: True)
)
```

### Strict Validation Mode

In strict mode, parameter values cannot contain underscores:

```python
manager = NATSSubjectManager(strict_validation=True)

# This will fail in strict mode

manager.build_subject("chat_say_room", room_id="room_with_underscore")
# SubjectValidationError: only letters, numbers, and hyphens allowed

# This works in strict mode

manager.build_subject("chat_say_room", room_id="room-with-hyphens")
```

## Best Practices

### 1. Always Use Pattern Names

```python
# GOOD: Use pattern names

subject = manager.build_subject("chat_say_room", room_id=room_id)

# BAD: Hardcoded strings

subject = f"chat.say.room.{room_id}"
```

### 2. Validate Before Publishing

```python
# Validate custom subjects before use

if manager.validate_subject(custom_subject):
    await nats_service.publish(custom_subject, data)
else:
    logger.warning("Invalid subject", subject=custom_subject)
```

### 3. Use Subscription Pattern Helpers

```python
# GOOD: Use helper methods for subscription patterns

chat_patterns = manager.get_chat_subscription_patterns()
for pattern in chat_patterns:
    await nats_service.subscribe(pattern, handler)

# BAD: Hardcoded subscription patterns

await nats_service.subscribe("chat.say.*", handler)  # Missing hierarchy level
```

### 4. Monitor Performance

```python
# Periodically check performance metrics

metrics = manager.get_performance_metrics()

if metrics["cache"]["hit_rate"] < 0.8:
    logger.warning("Low cache hit rate", hit_rate=metrics["cache"]["hit_rate"])

if metrics["validation"]["success_rate"] < 0.95:
    logger.error("High validation failure rate", success_rate=metrics["validation"]["success_rate"])
```

### 5. Handle Errors Gracefully

```python
from server.services.nats_subject_manager import (
    PatternNotFoundError,
    MissingParameterError,
    SubjectValidationError
)

try:
    subject = manager.build_subject(pattern_name, **params)
except PatternNotFoundError:
    logger.error("Unknown pattern", pattern_name=pattern_name)
    # Fall back to legacy subject construction

except MissingParameterError as e:
    logger.error("Missing parameters", error=str(e), pattern_name=pattern_name)
    raise
except SubjectValidationError as e:
    logger.error("Invalid parameter values", error=str(e))
    raise
```

## Testing

### Unit Testing

```python
from server.services.nats_subject_manager import NATSSubjectManager

def test_build_subject():
    manager = NATSSubjectManager()

    subject = manager.build_subject("chat_say_room", room_id="test_room")

    assert subject == "chat.say.room.test_room"
```

### Performance Testing

```python
import time

def test_cache_performance():
    manager = NATSSubjectManager()
    subject = "chat.say.room.test"

    # Prime cache

    manager.validate_subject(subject)

    # Measure cached performance

    start = time.perf_counter()
    for _ in range(1000):
        manager.validate_subject(subject)
    elapsed = time.perf_counter() - start

    assert elapsed < 0.01  # Should be very fast with cache
```

## Monitoring and Observability

### Health Endpoint

```bash
GET /api/admin/nats/subjects/health
```

Returns comprehensive statistics for monitoring:

- Validation success/failure rates
- Cache hit rates
- Average and P95 latencies
- Error counts by type
- Total patterns registered

### Accessing Performance Metrics

Access metrics programmatically:

```python
metrics = manager.get_performance_metrics()

# Monitor critical metrics

cache_hit_rate = metrics["cache"]["hit_rate"]
validation_success_rate = metrics["validation"]["success_rate"]
avg_validation_time = metrics["validation"]["avg_time_ms"]

# Set up alerts

if cache_hit_rate < 0.7:
    alert("Low cache hit rate", hit_rate=cache_hit_rate)

if avg_validation_time > 1.0:
    alert("High validation latency", avg_time_ms=avg_validation_time)
```

## Troubleshooting

### Common Issues

#### High Validation Failure Rate

**Problem**: `metrics["validation"]["failure_count"]` is high

**Solutions**:

1. Check for subjects that don't match any registered patterns
2. Review recent pattern changes
3. Check for malformed subjects in application code

#### Low Cache Hit Rate

**Problem**: `metrics["cache"]["hit_rate"]` < 0.5

**Solutions**:

1. Check if subjects are being dynamically generated with unique IDs
2. Consider registering more specific patterns
3. Review application message flow for caching opportunities

#### Pattern Not Found Errors

**Problem**: `PatternNotFoundError` exceptions

**Solutions**:

1. Verify pattern name spelling
2. Check if pattern was registered (call `get_all_patterns()`)
3. Register missing pattern via Admin API

## Future Enhancements

**Pattern Namespaces**: Organize patterns by feature area

**Pattern Versioning**: Support multiple versions of patterns

**Pattern Migration Tools**: Automated migration from old to new patterns

**Advanced Validation Rules**: Custom validation logic per pattern

**Pattern Analytics**: Usage statistics per pattern

- **Pattern Deprecation**: Mark patterns as deprecated with warnings

## Migration Status

### ✅ Fully Migrated Components

The following components have been successfully migrated to use the standardized subject manager:

**ChatService** (`server/game/chat_service.py`) - All chat channels use standardized patterns

**EventPublisher** (`server/realtime/event_publisher.py`) - Player movement events migrated

**CombatEventPublisher** (`server/services/combat_event_publisher.py`) - All 8 combat event types migrated

**NATSMessageHandler** (`server/realtime/nats_message_handler.py`) - Subscription patterns updated

**NATSService** (`server/services/nats_service.py`) - Pre-publish validation integrated

### 🔄 Backward Compatibility

All migrations include backward-compatible fallbacks:

- Components function without subject_manager injection (legacy mode)
- Fallback paths log warnings for monitoring deprecated usage
- Tests continue to work without modifications
- No breaking changes to existing code

### 📊 Migration Impact

**3 new combat patterns added**: `combat_damage`, `combat_turn`, `combat_timeout`

**20+ total patterns** now managed centrally

**5 production files** migrated to standardized patterns

**100% backward compatibility** maintained

**Zero breaking changes** to existing functionality

### ⚠️ Deprecated Utilities

The following utility functions are marked as deprecated:

- `server/utils/room_utils.get_local_channel_subject()` - Emits DeprecationWarning
- Only used in tests, safe to use but not recommended for new code

## Related Documentation

- [Real-Time Architecture](REAL_TIME_ARCHITECTURE.md) - Overall real-time system design
- [Enhanced Logging Guide](ENHANCED_LOGGING_GUIDE.md) - Structured logging practices
- [realtime.md](realtime.md) - WebSocket authentication and production deployment

## References

[NATS Subject-Based Messaging](https://docs.nats.io/nats-concepts/subjects)

- [NATS Best Practices](https://docs.nats.io/running-a-nats-service/nats_admin/best_practices)
- Source: `server/services/nats_subject_manager/` (package)
- Tests: `server/tests/unit/services/nats_subject_manager/`
- API Controller: `server/api/admin/subject_controller.py`
