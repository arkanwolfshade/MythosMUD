# 🗺️ Movement System Planning Document

## Overview

This document outlines the implementation plan for a dynamic room tracking system that enables multiplayer awareness and real-time room state management. The system will transform static room representations into living entities that track players, objects, and NPCs.

## Design Decisions

### Core Architecture
- **Real-time tracking only**: Players disappear from rooms when they log out
- **Simple ID-based tracking**: Objects and NPCs tracked by IDs only (stubs for future implementation)
- **Complete replacement**: Room objects replace dictionary-based room cache
- **Event-driven API**: Room methods trigger events for state changes
- **MovementService**: Centralized service for atomic movement operations
- **In-memory event bus**: Simple pub/sub system (Redis-ready for future)
- **Stateless Room objects**: Recreated from JSON data, no persistent state
- **Server-lifetime cache**: All rooms loaded at startup, no cleanup
- **Fail-fast error handling**: Exceptions for invalid states during development
- **Test-driven development**: Comprehensive testing at each phase

### Room Object Design
- **Location**: `server/models/room.py`
- **Event methods**: `player_entered()`, `player_left()`, `object_added()`, `object_removed()`, `npc_entered()`, `npc_left()`
- **Tracking**: Player IDs, object IDs, and NPC IDs only
- **Integration**: EventBus for notifications

### Movement Service Design
- **Location**: `server/game/movement_service.py`
- **Atomic operations**: ACID properties for player movement
- **Validation**: Movement rules and room existence checks
- **Coordination**: Between Room objects and PersistenceLayer

### Event System Design
- **Location**: `server/events/`
- **Event types**: `PlayerEnteredRoom`, `PlayerLeftRoom`, `ObjectAddedToRoom`, `ObjectRemovedFromRoom`, `NPCEnteredRoom`, `NPCLeftRoom`
- **Processing**: Asynchronous, non-blocking
- **Architecture**: In-memory pub/sub (migratable to Redis)

## Implementation Plan

### Phase 1: Foundation - Room Model and Event System

#### 1.1 Create Event Bus System
- **Components**:
  - `EventBus` class for in-memory pub/sub
  - Event type definitions
  - Async event processing with queue system
  - Event logging and debugging capabilities
- **Testing**: Unit tests with mocked event handlers
- **Timeline**: Week 1

#### 1.2 Create Room Model
- **Components**:
  - `Room` class with stateless design
  - Event-driven methods for state changes
  - Simple ID-based tracking
  - Integration with EventBus
- **Testing**: Unit tests with mocked EventBus
- **Timeline**: Week 2

### Phase 2: Movement Service

#### 2.1 Create MovementService
- **Components**:
  - Atomic movement operations with ACID properties
  - Validation of movement rules
  - Coordination between Room objects and PersistenceLayer
  - Integration with EventBus for movement events
- **Testing**: Unit tests with mocked Room and Player objects
- **Timeline**: Week 3

### Phase 3: Integration and Migration

#### 3.1 Update PersistenceLayer
- **Changes**:
  - Modify `_load_room_cache()` to create Room objects
  - Update `get_room()` and `list_rooms()` for Room objects
  - Maintain backward compatibility during transition
- **Testing**: Integration tests for room loading and access
- **Timeline**: Week 4

#### 3.2 Update Player Movement Logic
- **Changes**:
  - Integrate MovementService with existing player movement commands
  - Ensure atomic operations for room entry/exit
  - Add proper error handling and validation
- **Testing**: Integration tests for complete movement flow
- **Timeline**: Week 4

### Phase 4: Testing Strategy

#### 4.1 Unit Tests
- **Coverage**:
  - Room class methods with mocked EventBus
  - MovementService with mocked Room and Player objects
  - EventBus with mocked event handlers
- **Patterns**: Follow existing test patterns in `server/tests/`

#### 4.2 Integration Tests
- **Coverage**:
  - Complete movement flow from command to room updates
  - Concurrent player movements
  - Error conditions and edge cases
  - Event propagation and handling

### Phase 5: Error Handling and Monitoring

#### 5.1 Fail-Fast Implementation
- **Components**:
  - Comprehensive validation in MovementService
  - Proper exception handling with detailed error messages
  - Logging of all movement operations and errors

#### 5.2 Monitoring and Debugging
- **Components**:
  - Event logging for debugging movement issues
  - Performance monitoring for room operations
  - Health checks for room cache integrity

## Technical Specifications

### Room Object Interface
```python
class Room:
    def __init__(self, room_data: dict):
        # Initialize from JSON data
        pass

    def player_entered(self, player_id: str) -> None:
        # Add player to room, trigger event
        pass

    def player_left(self, player_id: str) -> None:
        # Remove player from room, trigger event
        pass

    def get_players(self) -> list[str]:
        # Return list of player IDs in room
        pass
```

### MovementService Interface
```python
class MovementService:
    def move_player(self, player_id: str, from_room_id: str, to_room_id: str) -> bool:
        # Atomic movement operation
        pass

    def validate_movement(self, player_id: str, to_room_id: str) -> bool:
        # Validate movement rules
        pass
```

### EventBus Interface
```python
class EventBus:
    def publish(self, event: BaseEvent) -> None:
        # Publish event asynchronously
        pass

    def subscribe(self, event_type: type, handler: Callable) -> None:
        # Subscribe to event type
        pass
```

## Success Criteria

### Functional Requirements
- [ ] Players can see other players in the same room
- [ ] Room state accurately reflects current occupants
- [ ] Movement operations are atomic and consistent
- [ ] Events are properly triggered and processed
- [ ] Error conditions are handled gracefully

### Performance Requirements
- [ ] Room operations complete within 100ms
- [ ] Event processing doesn't block main game loop
- [ ] Memory usage remains reasonable with all rooms loaded

### Quality Requirements
- [ ] 80%+ test coverage for new components
- [ ] All integration tests pass
- [ ] No memory leaks in room tracking
- [ ] Proper error logging and debugging capabilities

## Risk Mitigation

### Technical Risks
- **Concurrency issues**: Mitigated by atomic operations and proper locking
- **Memory usage**: Mitigated by stateless design and monitoring
- **Event processing delays**: Mitigated by async processing and queue management

### Integration Risks
- **Breaking existing functionality**: Mitigated by comprehensive testing and gradual migration
- **Performance impact**: Mitigated by efficient data structures and caching

## Future Enhancements

### Phase 6: Advanced Features
- **Object interaction**: Full object system integration
- **NPC behavior**: Dynamic NPC movement and interaction
- **Room effects**: Environmental effects and hazards
- **Distributed events**: Redis integration for multi-server support

### Phase 7: Optimization
- **Ephemeral room loading**: On-demand room creation for memory efficiency
- **Room cleanup**: Automatic cleanup of unused rooms
- **Performance monitoring**: Advanced metrics and alerting

## Conclusion

This movement system will provide the foundation for rich multiplayer interactions while maintaining the architectural principles that govern our eldritch systems. The phased approach ensures we can validate progress at each step and maintain system stability throughout the implementation.

---

*"The spaces between spaces are not empty, but filled with the awareness of those who traverse them."* - From the Pnakotic Manuscripts
