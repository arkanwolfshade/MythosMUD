# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-09-13-occupant-count-display-fix/spec.md

## Technical Requirements

**Server-Side Event Subscription**: Add event listeners in `connection_manager.py` for `PlayerEnteredRoom` and `PlayerLeftRoom` events published by the room model

**Server-Side Event Broadcasting**: Broadcast `room_occupants` events to all room occupants when players enter or leave rooms, using the existing event broadcasting infrastructure

**Client-Side Event Processing**: Add `room_occupants` case to the switch statement in `GameTerminalWithPanels.tsx` to handle occupant count updates
- **State Management**: Update the client's room state with new occupant count and occupant list when `room_occupants` events are received
- **Event Format Consistency**: Ensure `room_occupants` events use the same format as existing events: `{"occupants": names, "count": len(names)}`

## Implementation Details

### Server-Side Changes (connection_manager.py)

1. **Event Subscription**: Subscribe to `PlayerEnteredRoom` and `PlayerLeftRoom` events from the event bus

2. **Event Handlers**: Create async handlers that:

   - Get current room occupants using `self.room_manager.get_room_occupants()`

   - Build `room_occupants` event with occupant names and count

   - Broadcast to all room occupants using `self.broadcast_to_room()`

3. **Event Bus Access**: Use `persistence._event_bus` to subscribe to room movement events

### Client-Side Changes (GameTerminalWithPanels.tsx)

1. **Event Case Addition**: Add `room_occupants` case to the switch statement in `processEventQueue()` method (around line 193-207)

2. **State Updates**: Extract occupant data from event and update the room state:

   - Update `occupants` array with new occupant names

   - Update `occupant_count` with new count value

3. **UI Synchronization**: Ensure UI components automatically reflect the updated state

### Event Flow

1. **Player Movement**: Player uses movement command → MovementService processes → Room model calls `player_entered()`/`player_left()`
2. **Event Publishing**: Room model publishes `PlayerEnteredRoom`/`PlayerLeftRoom` events to event bus
3. **Server Processing**: Connection manager receives events → builds `room_occupants` event → broadcasts to room
4. **Client Processing**: Client receives `room_occupants` event → updates room state → UI reflects changes

### Error Handling

**Server-Side**: Wrap event handlers in try-catch blocks with proper logging

**Client-Side**: Validate event data before updating state to prevent UI corruption

**Fallback Behavior**: Maintain existing `room_update` event handling as fallback mechanism

### Testing Requirements

**Unit Tests**: Test server event handlers with mock room movement events

**Integration Tests**: Verify end-to-end flow from player movement to UI update

**Multi-Client Tests**: Test occupant count synchronization across multiple browser instances
- **Edge Cases**: Test with rapid player movements and connection/disconnection scenarios
