# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-10-25-subject-naming-standardization/spec.md

## Technical Requirements

### NATSSubjectManager Class Implementation

- **Location**: `server/services/nats_subject_manager.py`
- **Purpose**: Centralized subject pattern management and validation
- **Key Methods**:
  - `build_subject(pattern_name: str, **params) -> str`: Build subject from pattern with parameters
  - `validate_subject(subject: str) -> bool`: Validate subject against registered patterns
  - `register_pattern(name: str, pattern: str, required_params: list)`: Register new subject patterns
  - `get_pattern_info(pattern_name: str) -> dict`: Get pattern information and requirements

### Subject Pattern Registry

- **Pattern Format**: `{service}.{channel}.{scope}.{identifier}`
- **Service Types**: `chat`, `system`, `admin`, `player`
- **Channel Types**: `say`, `local`, `global`, `whisper`, `system`, `emote`, `pose`
- **Scope Types**: `room`, `subzone`, `player`, `global`
- **Identifier Types**: Room IDs, Player IDs, Subzone names

### Predefined Subject Patterns

```python
SUBJECT_PATTERNS = {
    "chat_say_room": {
        "pattern": "chat.say.room.{room_id}",
        "required_params": ["room_id"],
        "description": "Room-level say messages"
    },
    "chat_local_subzone": {
        "pattern": "chat.local.subzone.{subzone}",
        "required_params": ["subzone"],
        "description": "Subzone-level local messages"
    },
    "chat_global": {
        "pattern": "chat.global",
        "required_params": [],
        "description": "Global chat messages"
    },
    "chat_whisper_player": {
        "pattern": "chat.whisper.player.{target_id}",
        "required_params": ["target_id"],
        "description": "Player-to-player whisper messages"
    },
    "chat_system": {
        "pattern": "chat.system",
        "required_params": [],
        "description": "System-wide messages"
    },
    "chat_emote_room": {
        "pattern": "chat.emote.room.{room_id}",
        "required_params": ["room_id"],
        "description": "Room-level emote messages"
    },
    "chat_pose_room": {
        "pattern": "chat.pose.room.{room_id}",
        "required_params": ["room_id"],
        "description": "Room-level pose messages"
    }
}
```

### Subject Validation System

- **Parameter Validation**: Check required parameters are provided and valid
- **Pattern Matching**: Validate subject matches registered patterns
- **Type Checking**: Ensure parameter types match expected formats
- **Length Limits**: Enforce maximum subject length constraints
- **Character Validation**: Ensure only valid characters in subject components

### Integration Points

- **ChatService**: Replace manual subject construction with NATSSubjectManager
- **NATSService**: Add subject validation before publishing
- **Message Handlers**: Use standardized subjects for subscription patterns
- **Configuration**: Add subject pattern configuration options

### Performance Considerations

- **Pattern Caching**: Cache compiled patterns for fast validation
- **Lazy Loading**: Load patterns on first use to reduce startup time
- **Memory Efficiency**: Use string templates instead of regex for better performance
- **Validation Caching**: Cache validation results for repeated subjects

### Error Handling

- **Invalid Pattern**: Clear error messages for unknown patterns
- **Missing Parameters**: Detailed error for missing required parameters
- **Invalid Parameters**: Type and format validation errors
- **Subject Too Long**: Length limit enforcement with helpful messages

### Migration Strategy

1. **Phase 1**: Implement NATSSubjectManager alongside existing code
2. **Phase 2**: Update ChatService to use NATSSubjectManager for new messages
3. **Phase 3**: Migrate existing subject construction to use patterns
4. **Phase 4**: Remove old subject construction code
5. **Phase 5**: Add comprehensive validation and error handling

### Testing Requirements

- **Unit Tests**: Test pattern building, validation, and error handling
- **Integration Tests**: Test with actual NATS message publishing
- **Performance Tests**: Validate performance impact of subject validation
- **Migration Tests**: Ensure backward compatibility during migration

### Configuration Options

```python
class SubjectConfig(BaseSettings):
    enable_validation: bool = Field(default=True, description="Enable subject validation")
    max_subject_length: int = Field(default=255, description="Maximum subject length")
    strict_validation: bool = Field(default=True, description="Strict parameter validation")
    cache_patterns: bool = Field(default=True, description="Cache compiled patterns")
```

### Logging and Monitoring

- **Subject Usage**: Log subject pattern usage for monitoring
- **Validation Failures**: Log validation errors with context
- **Performance Metrics**: Track subject building and validation performance
- **Pattern Statistics**: Monitor most-used patterns for optimization
