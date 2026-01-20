# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-09-14-room-title-sync-fix/spec.md

## Technical Requirements

### Event Processing Race Condition Fix

Modify the `room_occupants` event handler in `GameTerminalWithPanels.tsx` (lines 393-432) to prevent overwriting new room data with stale room information

- Implement proper state merging logic that preserves room data from `room_update` events when processing `room_occupants` events
- Add validation to ensure room data consistency before applying state updates

### State Synchronization Improvement

Implement event processing order logic to ensure `room_update` events are processed before `room_occupants` events

- Add state validation checks to prevent stale room data from being applied to the UI
- Implement proper state merging that prioritizes newer room data over older room data

### Event Ordering Logic

Modify the event processing queue to handle room transition events in the correct order

- Implement event deduplication that considers room data freshness
- Add event sequence validation to ensure proper event processing order

### UI Consistency Validation

Add validation in the Room Info panel component to detect and handle stale room data

- Implement fallback logic to request fresh room data when inconsistencies are detected
- Add logging for debugging room data synchronization issues

### Code Changes Required

#### File: `client/src/components/GameTerminalWithPanels.tsx`

**Lines 393-432**: Fix the `room_occupants` event handler to prevent state overwrites

**Lines 130-200**: Improve event processing logic to handle room transitions correctly

**Lines 142-200**: Add state validation and merging logic

#### File: `client/src/components/RoomInfoPanel.tsx`

**Lines 26-50**: Add validation for room data consistency

**Lines 32-49**: Improve fallback room data handling

### Implementation Details

#### Event Processing Fix

```typescript
case 'room_occupants': {
  const occupants = event.data.occupants as string[];
  const occupantCount = event.data.count as number;

  // Validate event data
  if (occupants && Array.isArray(occupants) && typeof occupantCount === 'number') {
    // FIXED: Always use the most recent room data, not stale data
    if (updates.room) {
      // Room data already updated by room_update event - preserve it
      updates.room = {
        ...updates.room,
        occupants: occupants,
        occupant_count: occupantCount,
      };
    } else {
      // Only use current room data if no newer room data exists
      const currentRoom = gameState.room;
      if (currentRoom) {
        updates.room = {
          ...currentRoom,
          occupants: occupants,
          occupant_count: occupantCount,
        };
      }
    }
  }
  break;
}
```

#### State Validation

```typescript
// Add room data validation before applying updates
const validateRoomData = (newRoom: Room, currentRoom: Room | null): boolean => {
  if (!currentRoom) return true;

  // Prevent older room data from overwriting newer room data
  if (newRoom.id === currentRoom.id) return true;

  // Log potential race condition
  logger.warn('GameTerminalWithPanels', 'Potential room data race condition detected', {
    newRoomId: newRoom.id,
    currentRoomId: currentRoom.id,
    newRoomName: newRoom.name,
    currentRoomName: currentRoom.name,
  });

  return true; // Allow update but log the issue
};
```

### Testing Requirements

Unit tests for event processing logic

- Integration tests for room transition scenarios
- Browser automation tests to verify UI consistency
- Performance tests to ensure no regression in event processing speed

### Performance Considerations

Event processing should remain efficient with minimal overhead

- State validation should not impact real-time performance
- Logging should be minimal in production builds
