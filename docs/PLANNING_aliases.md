# Alias System Implementation Plan

## Overview

This document outlines the implementation plan for the user command aliasing system in MythosMUD. The system will allow players to create shortcuts for commonly used commands, improving user experience and gameplay efficiency.

## Architecture

### Data Model

```python
class Alias(BaseModel):
    name: str = Field(..., description="Alias name (case-insensitive)")
    command: str = Field(..., description="Target command to execute")
    version: str = Field(default="1.0", description="Schema version for future compatibility")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    # Future expansion fields (commented for now):
    # alias_type: str = Field(default="simple", description="simple|parameter|multi")
    # parameters: dict = Field(default_factory=dict, description="Parameter definitions for future use")
    # conditions: dict = Field(default_factory=dict, description="Conditional logic for future use")
    # metadata: dict = Field(default_factory=dict, description="Additional metadata")
```

### Storage Structure

- **Location**: `data/players/aliases/` (production)
- **Format**: One JSON file per player: `{player_name}_aliases.json`
- **Schema**: Validated JSON structure with version tracking

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "version": {
      "type": "string",
      "pattern": "^1\\.0$"
    },
    "aliases": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "pattern": "^[a-zA-Z][a-zA-Z0-9_]*$"
          },
          "command": {
            "type": "string",
            "maxLength": 200
          },
          "version": {
            "type": "string"
          },
          "created_at": {
            "type": "string",
            "format": "date-time"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time"
          }
        },
        "required": ["name", "command", "version", "created_at", "updated_at"]
      },
      "maxItems": 50
    }
  },
  "required": ["version", "aliases"]
}
```

## Implementation Phases

### Phase 1: MVP Core (Priority: High)

#### 1.1 Data Model and Storage
- [ ] Create `Alias` model in `server/models.py`
- [ ] Implement alias storage in `data/players/aliases/` (production)
- [ ] Add JSON schema validation
- [ ] Create alias loading/saving utilities

#### 1.2 Command Integration
- [ ] Add alias management commands to `server/command_handler.py`
- [ ] Implement alias expansion in command processing pipeline
- [ ] Add server-side caching for alias lookups

#### 1.3 Client Integration
- [ ] Add visual indicators for alias usage in `client/src/components/GameTerminal.tsx`
- [ ] Implement expanded command display
- [ ] Add success/error message handling

### Phase 2: Security & Polish (Priority: Medium)

#### 2.1 Security Implementation
- [ ] Implement reserved command blocking
- [ ] Add infinite loop detection
- [ ] Implement spam prevention (rate limiting)
- [ ] Add communication command blocking

#### 2.2 User Experience
- [ ] Add confirmation prompts for overwrite/delete
- [ ] Implement comprehensive error handling
- [ ] Add user feedback messages
- [ ] Format alias list display

### Phase 3: Testing & Documentation (Priority: Medium)

#### 3.1 Testing
- [ ] Create comprehensive test suite
- [ ] Add integration tests for command processing
- [ ] Test client-side visual indicators
- [ ] Performance testing with multiple aliases

#### 3.2 Documentation
- [ ] Create user help commands
- [ ] Document JSON storage format
- [ ] Add developer documentation
- [ ] Create troubleshooting guides

## Technical Implementation Details

### Command Processing Flow

1. **Client sends command** via WebSocket
2. **Server receives command** in `command_handler.py`
3. **Alias expansion** occurs before command parsing
4. **Expanded command** is processed normally
5. **Client displays** expanded command with visual indicator

### Alias Management Commands

```python
# Create/update alias
alias <name> <command>

# Remove alias
unalias <name>

# List all aliases
aliases

# Show specific alias
alias <name>
```

### Reserved Commands

- `alias`, `aliases`, `unalias` (management commands)
- `help` (system command)
- Future: Communication commands for spam prevention

### Error Handling

- Invalid alias names (must start with letter)
- Reserved command attempts
- Non-existent target commands
- Maximum alias limits (50 per player, 200 chars)
- Infinite loop detection
- Rate limiting violations

### Performance Considerations

- Hash table lookup for O(1) alias resolution
- Server-side caching of alias data
- Efficient JSON parsing and validation
- Minimal impact on command processing time

## Future Expansion Architecture

### Parameter-Based Aliases (Future)

```python
# Example future syntax:
alias heal cast 'heal' $1
alias attack wield sword;kill $1
```

### Multi-Command Aliases (Future)

```python
# Example future syntax:
alias combat k $1;f
alias gohome recall;quit
```

### Extensible Design

- Version field for schema evolution
- Placeholder fields for future features
- Modular alias processor interface
- Backward compatibility for simple aliases

## Testing Strategy

### Unit Tests
- Alias model validation
- JSON schema validation
- Command parsing and expansion
- Error handling scenarios

### Integration Tests
- End-to-end alias creation and usage
- WebSocket communication with aliases
- Client-side visual indicators
- Performance with multiple aliases

### Security Tests
- Reserved command bypass attempts
- Infinite loop creation attempts
- Spam prevention effectiveness
- Rate limiting validation

## Success Metrics

- [ ] Players can successfully create and use aliases
- [ ] No performance impact on command processing
- [ ] 80%+ test coverage
- [ ] Clear user documentation
- [ ] Extensible architecture ready for future expansion
- [ ] No security vulnerabilities introduced

## Notes for AI Implementation

When implementing this feature:

1. **Follow TDD**: Write tests before implementing features
2. **Use existing patterns**: Follow the established code structure
3. **Document thoroughly**: Add comprehensive docstrings and comments
4. **Consider future expansion**: Design with extensibility in mind
5. **Test edge cases**: Cover all error scenarios and boundary conditions
6. **Performance first**: Ensure alias processing doesn't impact game performance
7. **Security conscious**: Validate all inputs and prevent abuse

## Related Files

- `server/models.py` - Alias model definition
- `server/command_handler.py` - Command processing and alias management
- `client/src/components/GameTerminal.tsx` - Client-side visual indicators
- `data/players/aliases/` - Alias storage directory (production)
- `server/tests/` - Test suite for alias functionality
