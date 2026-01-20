# Implementation Tasks

This document contains the detailed task breakdown for implementing the NPC-Room Integration feature as specified in @.agent-os/specs/2025-09-24-npc-room-integration/spec.md

## Phase 1: Event Handler Implementation

### Task 1.1: Create NPC Event Handler

**File**: `server/services/npc_room_integration.py` (new)

**Description**: Create a new service to handle NPC room integration events

**Implementation**:
  - Subscribe to `NPCEnteredRoom` and `NPCLeftRoom` events
  - Process events to add/remove NPCs from room occupant tracking
  - Integrate with existing persistence layer for room access
- **Dependencies**: EventBus, PersistenceLayer, NPCLifecycleManager

### Task 1.2: Integrate Event Handler with Application Startup

**File**: `server/app/lifespan.py`

**Description**: Initialize and register the NPC room integration service during application startup

**Implementation**:
  - Import and instantiate NPC room integration service
  - Subscribe to NPC events
  - Ensure service is available on app.state for other components
- **Dependencies**: Task 1.1

## Phase 2: Room Data Integration

### Task 2.1: Implement NPC Room Entry/Exit

**File**: `server/services/npc_room_integration.py`

**Description**: Implement methods to add/remove NPCs from room occupant tracking

**Implementation**:
  - `handle_npc_entered_room(event: NPCEnteredRoom)` - Add NPC to room
  - `handle_npc_left_room(event: NPCLeftRoom)` - Remove NPC from room
  - Call `room.npc_entered(npc_id)` and `room.npc_left(npc_id)`
- **Dependencies**: Task 1.1

### Task 2.2: NPC Name Resolution Service

**File**: `server/services/npc_room_integration.py`

**Description**: Implement NPC ID to display name mapping

**Implementation**:
  - `resolve_npc_name(npc_id: str) -> str` method
  - Query NPC lifecycle manager for active NPC instances
  - Extract display name from NPC definition or instance
  - Handle cases where NPC cannot be resolved (return "Unknown NPC")
- **Dependencies**: Task 2.1

## Phase 3: Data Transformation and Broadcasting

### Task 3.1: Modify Room Data Processing

**File**: `server/realtime/event_handler.py` or `server/realtime/websocket_handler.py`

**Description**: Update room data processing to include NPCs in occupants array

**Implementation**:
  - Modify `_get_room_occupants()` method to include NPCs
  - Combine player names and NPC names into unified occupants list
  - Maintain existing client interface expectations
- **Dependencies**: Task 2.2

### Task 3.2: Real-time Occupant Broadcasting

**File**: `server/services/npc_room_integration.py`

**Description**: Implement real-time broadcasting of room occupant updates

**Implementation**:
  - `broadcast_room_occupants_update(room_id: str)` method
  - Trigger room occupant updates when NPCs enter/leave
  - Integrate with existing connection manager broadcasting
- **Dependencies**: Task 3.1

## Phase 4: Testing and Validation

### Task 4.1: Unit Tests for NPC Room Integration

**File**: `server/tests/test_npc_room_integration.py` (new)

**Description**: Create comprehensive unit tests for the NPC room integration service

**Implementation**:
  - Test NPC event handling
  - Test room occupant tracking
  - Test NPC name resolution
  - Test error handling scenarios
- **Dependencies**: All previous tasks

### Task 4.2: Integration Tests

**File**: `server/tests/test_npc_room_integration_e2e.py` (new)

**Description**: Create end-to-end integration tests

**Implementation**:
  - Test complete NPC spawning to room occupant display flow
  - Test real-time updates when NPCs enter/leave rooms
  - Test client-side room info panel updates
- **Dependencies**: Task 4.1

### Task 4.3: Manual Testing Protocol

**Description**: Create manual testing procedures to validate the feature

**Implementation**:

  - Test NPCs appear in Room Info panel after server startup
  - Test real-time updates during gameplay
  - Test occupant count accuracy
  - Test error scenarios (missing NPCs, invalid rooms)

## Phase 5: Documentation and Cleanup

### Task 5.1: Update Documentation

**Files**: Various documentation files

**Description**: Update relevant documentation to reflect NPC room integration

**Implementation**:
  - Update API documentation if needed
  - Update architecture diagrams
  - Update README files with new feature information

### Task 5.2: Code Review and Optimization

**Description**: Review and optimize the implementation

**Implementation**:

  - Code review for best practices
  - Performance optimization if needed
  - Error handling improvements
  - Logging enhancements

## Implementation Status: PENDING ⏳

**Ready for Implementation**: The specification is complete and ready for development.

**Next Steps**:

1. Begin with Phase 1: Event Handler Implementation
2. Follow the task dependencies as outlined above
3. Test each phase thoroughly before proceeding to the next
4. Validate end-to-end functionality with manual testing

**Estimated Complexity**: Medium
**Estimated Timeline**: 2-3 development sessions
**Risk Level**: Low (building on existing, well-tested systems)
