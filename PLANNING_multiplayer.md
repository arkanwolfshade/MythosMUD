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

## 🚨 Critical Gaps Identified

### **1. Missing Event-to-Real-Time Bridge**

**Problem**: Events are published to the EventBus but never reach connected clients.

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

**Problem**: No component subscribes to `PlayerEnteredRoom` and `PlayerLeftRoom` events.

**Missing Implementation**:

- Event subscriber that listens to movement events
- Event-to-message converter
- Room-based broadcasting logic

### **3. Incomplete Room Subscription Management**

**Problem**: Players aren't properly subscribed to their current room when connecting.

**Current Issues**:

- WebSocket handler doesn't subscribe players to their room on connection
- No automatic subscription updates when players move
- Missing "who's in the room" functionality

### **4. No Player Presence Tracking**

**Problem**: No way to track which players are online or in specific rooms.

**Missing Features**:

- Online player tracking
- Room occupancy lists
- Player connection/disconnection notifications

---

## 🏗️ Required Implementation

### **Phase 1: Event-to-Real-Time Bridge**

#### **1.1 Create Real-Time Event Handler**

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

#### **1.2 Event-to-Message Conversion**

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

#### **2.1 Room Subscription Integration**

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

#### **2.2 Player Presence Tracking**

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

**Update**: `client/src/components/RoomInfoPanel.tsx`

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

**Update**: `client/src/components/GameTerminal.tsx`

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

### **Step 1: Create Event Handler (2-3 hours)**

1. Create `server/realtime/event_handler.py`
2. Implement `RealTimeEventHandler` class
3. Add event subscription logic
4. Create event-to-message conversion methods
5. Add integration with `ConnectionManager`

### **Step 2: Update Connection Management (2-3 hours)**

1. Enhance `ConnectionManager` with presence tracking
2. Update WebSocket handler for room subscriptions
3. Add player connection/disconnection notifications
4. Implement room occupant tracking

### **Step 3: Client-Side Updates (1-2 hours)**

1. Update `GameTerminal.tsx` for new event types
2. Add room occupancy display to `RoomInfoPanel.tsx`
3. Enhance event handling for presence updates
4. Add visual indicators for online players

### **Step 4: Testing and Integration (2-3 hours)**

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

### **Functional Requirements**

- [ ] Players can see each other in the same room
- [ ] Players receive notifications when others enter/leave their room
- [ ] Room occupancy is displayed correctly
- [ ] Movement updates are broadcast in real-time
- [ ] Disconnections are handled gracefully

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
