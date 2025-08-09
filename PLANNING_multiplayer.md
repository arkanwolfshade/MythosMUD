# 🎮 MythosMUD Multiplayer Architecture Planning

*As documented in the restricted archives of Miskatonic University, this document outlines the critical gaps preventing players from seeing each other in the eldritch realms of our MUD.*

---

## 📋 Current Architecture Analysis

### **What We Have (✅ Working Components)**

#### **Real-Time Communication Infrastructure**

- **WebSocket Handler**: `server/realtime/websocket_handler.py`
  - Handles individual player connections
  - Processes commands and sends responses
  - Manages connection lifecycle

- **Connection Manager**: `server/realtime/connection_manager.py`
  - Tracks active WebSocket connections
  - Manages room subscriptions (`room_subscriptions`)
  - Provides broadcasting capabilities (`broadcast_to_room()`)

- **SSE Handler**: `server/realtime/sse_handler.py`
  - Server-Sent Events for one-way updates
  - Handles game state streaming

#### **Event System**

- **Event Bus**: `server/events/event_bus.py`
  - Thread-safe pub/sub system
  - Asynchronous event processing
  - Supports multiple subscribers per event type

- **Room Events**: `server/models/room.py`
  - `player_entered()` - publishes `PlayerEnteredRoom` events
  - `player_left()` - publishes `PlayerLeftRoom` events
  - Room state tracking with `_players` set

#### **Movement System**

- **Movement Service**: `server/game/movement_service.py`
  - Atomic movement operations with ACID properties
  - Calls `room.player_entered()` and `room.player_left()`
  - Validates movement between rooms

#### **Client-Side Support**

- **Game Terminal**: `client/src/components/GameTerminal.tsx`
  - Handles `player_entered` and `player_left` events
  - Displays messages when players enter/leave rooms
  - Real-time connection management

---

## ✅ Current Status (post Python 3.12 upgrade)

- [x] Real-time bridge implemented: `server/realtime/event_handler.py` subscribes to `PlayerEnteredRoom` and
  `PlayerLeftRoom` and broadcasts room messages and occupant lists via `ConnectionManager`.
- [x] Presence tracking: `ConnectionManager` maintains `online_players` and `room_occupants`, reconciles on
  connect/disconnect, and emits `player_left_game` + `room_occupants` updates.
- [x] Room subscription lifecycle: on WebSocket connect we subscribe the player to their canonical room; movement
  triggers subscription updates and room broadcasts.
- [x] Client event handling: `GameTerminal.tsx` handles `game_state`, `room_update`, `player_entered`, `player_left`,
  `player_left_game`, and `room_occupants`, updating the visible occupants list.
- [x] Tests cover event bridge and connection manager behaviors (see `server/tests/test_real_time.py`,
  `server/tests/test_multiplayer_integration.py`).

Notes and follow-ups discovered:

- [x] Replace uses of `datetime.utcnow()` with timezone-aware `datetime.now(datetime.UTC)` across server code to
  address deprecations in Python 3.12 (warnings observed in test runs). All tests green.
- [x] Normalize timestamps in real-time events to a consistent, timezone-aware format.
 - [x] Unify real-time event envelope across SSE and WebSocket (single schema with event_type, timestamp Z, sequence_number, room_id, player_id, data).

---

## 🚨 Critical Gaps Identified

### **1. Missing Event-to-Real-Time Bridge**

**Status**: Implemented via `RealTimeEventHandler` → `ConnectionManager` broadcast path.

**Current Flow**:

```
Player Movement → MovementService → Room.player_entered() → EventBus.publish()
```

**Missing Link**:

```
EventBus → Real-Time Bridge → ConnectionManager → WebSocket Broadcast
```

**Impact**: Players can move between rooms, but other players never see them.

### **2. No Event Bus Subscribers for Real-Time Communication**

**Status**: Implemented in `RealTimeEventHandler._subscribe_to_events()`.

**Missing Implementation**:

- Event subscriber that listens to movement events
- Event-to-message converter
- Room-based broadcasting logic

### **3. Incomplete Room Subscription Management**

**Status**: Largely implemented.

- WebSocket handler subscribes players on connection and broadcasts initial `game_state`
- Movement flow triggers `room_update` and subscription changes
- Occupants are tracked and broadcast via `room_occupants` events; client displays them

### **4. No Player Presence Tracking**

**Status**: Implemented. `ConnectionManager` maintains `online_players` and `room_occupants`, and emits
`player_left_game` notifications and occupancy updates on disconnect.

---

## 🏗️ Required Implementation

### **Phase 1: Event-to-Real-Time Bridge**

#### **1.1 Create Real-Time Event Handler** (Done)

**File**: `server/realtime/event_handler.py`

```python
class RealTimeEventHandler:
    """Bridges EventBus events to real-time communication."""

    def __init__(self, connection_manager: ConnectionManager):
        self.connection_manager = connection_manager
        self.event_bus = get_event_bus()
        self._subscribe_to_events()

    def _subscribe_to_events(self):
        """Subscribe to relevant game events."""
        self.event_bus.subscribe(PlayerEnteredRoom, self._handle_player_entered)
        self.event_bus.subscribe(PlayerLeftRoom, self._handle_player_left)

    async def _handle_player_entered(self, event: PlayerEnteredRoom):
        """Handle player entering a room."""
        # Convert event to real-time message
        # Broadcast to room occupants
        # Update room subscriptions

    async def _handle_player_left(self, event: PlayerLeftRoom):
        """Handle player leaving a room."""
        # Convert event to real-time message
        # Broadcast to room occupants
        # Update room subscriptions
```

#### **1.2 Event-to-Message Conversion** (Done)

**Message Format**:

```json
{
  "event_type": "player_entered|player_left",
  "timestamp": "2024-01-15T10:30:00Z",
  "sequence_number": 12345,
  "room_id": "arkham_city_downtown_001",
  "data": {
    "player_id": "player123",
    "player_name": "Professor Armitage",
    "message": "Professor Armitage enters the room."
  }
}
```

### **Phase 2: Enhanced Connection Management**

#### **2.1 Room Subscription Integration** (Done)

**Update**: `server/realtime/websocket_handler.py`

```python
async def handle_websocket_connection(websocket: WebSocket, player_id: str):
    # ... existing connection logic ...

    # Subscribe player to their current room
    player = connection_manager._get_player(player_id)
    if player and hasattr(player, "current_room_id"):
        await connection_manager.subscribe_to_room(player_id, player.current_room_id)

        # Send current room occupants to the player
        await send_room_occupants(websocket, player.current_room_id)
```

#### **2.2 Player Presence Tracking** (Done)

**Add to**: `server/realtime/connection_manager.py`

```python
class ConnectionManager:
    def __init__(self):
        # ... existing initialization ...
        self.online_players: dict[str, dict] = {}  # player_id -> player_info
        self.room_occupants: dict[str, set[str]] = {}  # room_id -> set of player_ids

    async def player_connected(self, player_id: str, player_info: dict):
        """Track when a player connects."""
        self.online_players[player_id] = player_info
        await self._notify_player_presence(player_id, "connected")

    async def player_disconnected(self, player_id: str):
        """Track when a player disconnects."""
        if player_id in self.online_players:
            del self.online_players[player_id]
            await self._notify_player_presence(player_id, "disconnected")
```

### **Phase 3: Client-Side Enhancements**

#### **3.1 Room Occupancy Display**

**Update**: `client/src/components/RoomInfoPanel.tsx` (Partially addressed via `GameTerminal.tsx` occupants list)

```typescript
interface RoomOccupants {
  players: Player[];
  count: number;
}

// Add room occupants display
const [roomOccupants, setRoomOccupants] = useState<RoomOccupants>({
  players: [],
  count: 0
});
```

#### **3.2 Enhanced Event Handling**

**Update**: `client/src/components/GameTerminal.tsx` (Done for current events)

```typescript
function handleGameEvent(event: GameEvent) {
  switch (event.event_type) {
    case 'player_entered':
      addMessage(`${event.data.player_name} enters the room.`);
      updateRoomOccupants(event.data.room_occupants);
      break;

    case 'player_left':
      addMessage(`${event.data.player_name} leaves the room.`);
      updateRoomOccupants(event.data.room_occupants);
      break;

    case 'room_occupants':
      updateRoomOccupants(event.data);
      break;
  }
}
```

---

## 🔧 Implementation Steps

### **Step 1: Create Event Handler (Done)**

1. Create `server/realtime/event_handler.py`
2. Implement `RealTimeEventHandler` class
3. Add event subscription logic
4. Create event-to-message conversion methods
5. Add integration with `ConnectionManager`

### **Step 2: Update Connection Management (Done)**

1. Enhance `ConnectionManager` with presence tracking
2. Update WebSocket handler for room subscriptions
3. Add player connection/disconnection notifications
4. Implement room occupant tracking

### **Step 3: Client-Side Updates (In progress)**

1. Update `GameTerminal.tsx` for new event types
2. Add room occupancy display to `RoomInfoPanel.tsx`
3. Enhance event handling for presence updates
4. Add visual indicators for online players

### **Step 4: Testing and Integration (Ongoing)**

1. Create comprehensive test suite for multiplayer functionality
2. Test multiple client connections
3. Verify real-time updates work correctly
4. Test edge cases (disconnections, reconnections)

---

## 🧪 Testing Strategy

### **Unit Tests**

- **Event Handler Tests**: Test event subscription and message conversion
- **Connection Manager Tests**: Test room subscriptions and broadcasting
- **Movement Integration Tests**: Test end-to-end movement with real-time updates

### **Integration Tests**

- **Multi-Client Tests**: Test multiple clients connecting simultaneously
- **Movement Tests**: Test players moving between rooms and seeing each other
- **Disconnection Tests**: Test handling of client disconnections

### **Manual Testing**

- **Two-Client Test**: Connect two browser clients and verify they see each other
- **Movement Test**: Have one client move between rooms while other watches
- **Chat Test**: Test real-time chat functionality between clients

---

## 📊 Success Metrics

### **Functional Requirements** (Updated status)

- [x] Players can see each other in the same room
- [x] Players receive notifications when others enter/leave their room
- [x] Room occupancy is displayed correctly
- [x] Movement updates are broadcast in real-time
- [x] Disconnections are handled gracefully

---

## 📝 Newly Identified Work

- [x] Migrate all server timestamps to timezone-aware datetime (`datetime.now(datetime.UTC)`) to remove Python 3.12
      deprecations and ensure consistent event times. (See issue #118)
- [x] Normalize real-time event timestamps (replace placeholder timestamps in WebSocket events with real values).
      (See issue #119)
- [ ] Room occupants panel in `RoomInfoPanel.tsx` to show the same occupants list already available in
      `GameTerminal.tsx` for parity with planning. (See issue #120)
 - [ ] Client: migrate any remaining legacy `type` consumers to `event_type` and add a thin adapter for backward compatibility in the hook.

---

## 📌 Issue Checklist

- [x] #118 Replace utcnow with timezone-aware datetimes across server (Python 3.12)
- [x] #119 Normalize real-time event timestamps (use real, timezone-aware times)
- [ ] #120 Add RoomInfoPanel occupants list to match server events
 - [x] #121 Unify real-time event envelope across SSE and WebSocket

### **Performance Requirements**

- [ ] Support 10+ concurrent players in same room
- [ ] Movement updates delivered within 100ms
- [ ] No memory leaks from connection management
- [ ] Graceful handling of network interruptions

### **Quality Requirements**

- [ ] 90%+ test coverage for multiplayer functionality
- [ ] No race conditions in concurrent movement
- [ ] Proper error handling for all edge cases
- [ ] Comprehensive logging for debugging

---

## 🚀 Future Enhancements

### **Advanced Multiplayer Features**

- **Player Status**: Online/away/busy status indicators
- **Room Descriptions**: Dynamic room descriptions based on occupants
- **Group Movement**: Allow players to move together
- **Private Messages**: Direct messaging between players
- **Room Chat**: Room-specific chat channels

### **Performance Optimizations**

- **Message Batching**: Combine multiple updates into single messages
- **Room Partitioning**: Split large rooms for better performance
- **Connection Pooling**: Optimize WebSocket connection management
- **Caching**: Cache frequently accessed room data

---

## 📚 References

### **Current Architecture Files**

- `server/realtime/connection_manager.py` - Connection management
- `server/realtime/websocket_handler.py` - WebSocket processing
- `server/events/event_bus.py` - Event system
- `server/models/room.py` - Room state management
- `server/game/movement_service.py` - Movement logic
- `client/src/components/GameTerminal.tsx` - Client interface

### **Related Documentation**

- `docs/REAL_TIME_ARCHITECTURE.md` - Real-time communication design
- `PLANNING_movement_system.md` - Movement system planning
- `TASKS.local.md` - Task tracking and implementation status

---

*"The proper coordination of eldritch forces requires both individual awareness and collective consciousness. So too must our multiplayer architecture balance personal experience with shared reality." - Prof. Armitage's Notes on Multiplayer Systems*
