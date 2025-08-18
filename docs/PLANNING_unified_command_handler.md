# WebSocket Architecture Unification Plan

## Overview

**Problem**: MythosMUD currently has two separate command processing architectures that create code duplication, maintenance burden, and potential inconsistencies.

**Goal**: Unify command processing so that both HTTP API and WebSocket connections use the same `command_handler_v2.py` code path.

## Current State Analysis

### Dual Command Processing Architecture

**HTTP API Path:**

```
Client → HTTP Request → command_handler_v2.py → MovementService → Database
```

**WebSocket Path:**

```
Client → WebSocket → websocket_handler.py → MovementService → Database
```

### Current Implementation Issues

1. **Code Duplication**: Same command logic exists in two places
2. **Maintenance Burden**: Fixes and features need to be implemented twice
3. **Inconsistency Risk**: The two paths may diverge over time
4. **Testing Complexity**: Both paths need separate testing
5. **Technical Debt**: Architectural inconsistency creates long-term maintenance issues

## Target Architecture

### Unified Command Processing

**Target Flow:**

```
Client → HTTP Request/WebSocket → command_handler_v2.py → MovementService → Database
```

Both HTTP and WebSocket requests will use the same unified command handler, ensuring:

- Single source of truth for command logic
- Consistent behavior across all interfaces
- Easier maintenance and testing
- Better extensibility for future commands

## Implementation Plan

### Phase 1: Analysis and Preparation (1-2 days)

#### 1.1 Audit Current Command Handler

- [ ] Document all commands supported by `command_handler_v2.py`
- [ ] Document all commands supported by `websocket_handler.py`
- [ ] Identify any WebSocket-specific commands that don't exist in HTTP
- [ ] Map command signatures and expected parameters

#### 1.2 Analyze Request Context Requirements

- [ ] Document what `command_handler_v2.py` expects from `Request` object
- [ ] Identify required `app.state` attributes (persistence, event_bus)
- [ ] Document authentication context requirements
- [ ] Map error response formats

#### 1.3 Create Test Suite

- [ ] Create comprehensive tests for current HTTP command behavior
- [ ] Create comprehensive tests for current WebSocket command behavior
- [ ] Establish baseline for regression testing

### Phase 2: WebSocket Handler Refactoring (2-3 days)

#### 2.1 Create Request Context Factory

```python
# New file: server/realtime/request_context.py
class WebSocketRequestContext:
    """Creates FastAPI Request-like objects for WebSocket commands"""

    def __init__(self, persistence, event_bus, user):
        self.app = type("MockApp", (), {
            "state": type("MockState", (), {
                "persistence": persistence,
                "event_bus": event_bus
            })()
        })()
        self.user = user
```

#### 2.2 Refactor Command Processing

**Current (websocket_handler.py):**

```python
async def process_websocket_command(cmd: str, args: list, player_id: str) -> dict:
    # Direct implementation of commands
    if cmd == "look":
        # Custom look logic
    elif cmd == "go":
        # Custom go logic
```

**Target:**

```python
async def process_websocket_command(cmd: str, args: list, player_id: str) -> dict:
    # Create proper request context
    request = WebSocketRequestContext(persistence, event_bus, user)

    # Delegate to unified command handler
    from ..command_handler_v2 import process_command
    result = await process_command(request, cmd, args, player_id)

    return result
```

#### 2.3 Update Error Handling

- [ ] Ensure WebSocket error responses match HTTP error format
- [ ] Implement proper error propagation from unified handler
- [ ] Maintain WebSocket-specific error handling where needed

### Phase 3: Authentication Context (1-2 days)

#### 3.1 User Context Management

- [ ] Ensure WebSocket connections maintain proper user authentication
- [ ] Create user objects compatible with `command_handler_v2.py` expectations
- [ ] Handle session management consistently

#### 3.2 Permission and Authorization

- [ ] Verify that WebSocket commands respect the same authorization rules
- [ ] Implement proper permission checking in unified context
- [ ] Handle authentication failures gracefully

### Phase 4: Testing and Validation (2-3 days)

#### 4.1 Functional Testing

- [ ] Test all commands via both HTTP and WebSocket
- [ ] Verify identical behavior between interfaces
- [ ] Test error conditions and edge cases
- [ ] Validate command responses and side effects

#### 4.2 Performance Testing

- [ ] Benchmark command processing performance
- [ ] Ensure no significant performance degradation
- [ ] Test under load conditions
- [ ] Monitor memory usage and resource consumption

#### 4.3 Integration Testing

- [ ] Test full game flow (login → command → response)
- [ ] Verify real-time updates work correctly
- [ ] Test concurrent user scenarios
- [ ] Validate event bus integration

### Phase 5: Cleanup and Documentation (1 day)

#### 5.1 Code Cleanup

- [ ] Remove duplicate command logic from `websocket_handler.py`
- [ ] Clean up any unused imports or functions
- [ ] Update code comments and documentation

#### 5.2 Documentation Updates

- [ ] Update API documentation to reflect unified architecture
- [ ] Document the new request context pattern
- [ ] Update development guidelines
- [ ] Create architectural decision record (ADR)

## Technical Specifications

### Request Context Requirements

The unified `command_handler_v2.py` expects:

```python
# Required Request object structure
request.app.state.persistence  # Database access layer
request.app.state.event_bus    # Event bus for inter-service communication
request.user                   # Authenticated user object
request.user.id               # User ID
request.user.username         # Username
```

### Error Response Format

Ensure consistent error responses:

```python
# HTTP Error Response
{
    "error": {
        "type": "validation_error",
        "message": "Invalid command format",
        "details": {...}
    }
}

# WebSocket Error Response (should match)
{
    "type": "error",
    "error": {
        "type": "validation_error",
        "message": "Invalid command format",
        "details": {...}
    }
}
```

### Command Signature Compatibility

All commands must maintain the same signature:

```python
# Unified command signature
async def process_command(
    request: Request,
    command: str,
    args: List[str],
    player_id: str
) -> Dict[str, Any]:
    # Command processing logic
    pass
```

## Risk Assessment

### High Risk Areas

1. **Authentication Context**: WebSocket authentication may not match HTTP
2. **Error Handling**: Different error formats could break client expectations
3. **Performance**: Additional request context creation could impact performance
4. **Event Bus Integration**: WebSocket events may not propagate correctly

### Mitigation Strategies

1. **Comprehensive Testing**: Extensive test coverage for all scenarios
2. **Gradual Rollout**: Implement changes incrementally with feature flags
3. **Monitoring**: Add detailed logging and monitoring during transition
4. **Rollback Plan**: Maintain ability to revert to previous architecture

## Success Criteria

### Functional Requirements

- [ ] All existing commands work identically via HTTP and WebSocket
- [ ] No regression in game functionality
- [ ] Error responses are consistent between interfaces
- [ ] Authentication and authorization work correctly

### Non-Functional Requirements

- [ ] Performance is maintained or improved
- [ ] Code duplication is eliminated
- [ ] Test coverage is comprehensive
- [ ] Documentation is updated and accurate

## Implementation Timeline

**Total Estimated Time: 7-11 days**

- **Phase 1**: Analysis and Preparation (1-2 days)
- **Phase 2**: WebSocket Handler Refactoring (2-3 days)
- **Phase 3**: Authentication Context (1-2 days)
- **Phase 4**: Testing and Validation (2-3 days)
- **Phase 5**: Cleanup and Documentation (1 day)

## Dependencies

### Prerequisites

- [ ] TailwindCSS migration completed and stable
- [ ] Current WebSocket functionality working correctly
- [ ] Comprehensive test suite in place
- [ ] Development environment stable

### Blocking Issues

- None identified at this time

## Future Considerations

### Post-Implementation Benefits

1. **Easier Feature Development**: New commands only need one implementation
2. **Better Testing**: Single code path reduces testing complexity
3. **Improved Maintainability**: Bug fixes apply to all interfaces
4. **Enhanced Extensibility**: Easier to add new command interfaces

### Potential Future Work

1. **GraphQL Integration**: Unified command handler could support GraphQL
2. **REST API Expansion**: Easier to add new REST endpoints
3. **Command Middleware**: Centralized command processing enables middleware
4. **Analytics and Monitoring**: Unified logging and metrics

## Conclusion

This architectural unification will significantly improve the maintainability and consistency of the MythosMUD codebase. While it represents substantial work, the long-term benefits in reduced technical debt and improved developer experience make it a worthwhile investment.

The implementation should be approached methodically with extensive testing to ensure no regression in functionality. The phased approach allows for incremental validation and reduces risk.

---

**Document Version**: 1.0
**Created**: 2025-08-18
**Last Updated**: 2025-08-18
**Status**: Planning Complete - Ready for Implementation
