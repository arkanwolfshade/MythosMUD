# Event Ownership Matrix

**Document Version:** 1.0
**Date:** November 3, 2025
**Status:** Architecture Audit
**Purpose:** Map all event publishers and identify duplicate event sources

## Overview

This document maps the complete event publishing architecture in MythosMUD to identify:
1. All event publishers and their sources
2. Duplicate or overlapping events
3. Event flow through the system
4. Canonical event ownership

## Event Publishing Layers

### Layer 1: EventBus Events (Domain Events)

These are domain events published through the EventBus system defined in `server/events/event_types.py`:

| Event Class | Publisher | Purpose | Listeners |
|------------|-----------|---------|-----------|
| `PlayerEnteredRoom` | Room.player_entered() | Player joins room occupant list | RealTimeEventHandler |
| `PlayerLeftRoom` | Room.player_left() | Player leaves room occupant list | RealTimeEventHandler |
| `ObjectAddedToRoom` | Room.object_added() | Object added to room | RealTimeEventHandler |
| `ObjectRemovedFromRoom` | Room.object_removed() | Object removed from room | RealTimeEventHandler |
| `NPCEnteredRoom` | Room.npc_entered() | NPC joins room | RealTimeEventHandler |
| `NPCLeftRoom` | Room.npc_left() | NPC leaves room | RealTimeEventHandler |
| `CombatStartedEvent` | CombatService | Combat begins | CombatEventPublisher |
| `PlayerAttackedEvent` | CombatService | Attack occurs | CombatEventPublisher |
| `NPCAttackedEvent` | CombatService | NPC attacks | CombatEventPublisher |
| `CombatEndedEvent` | CombatService | Combat ends | CombatEventPublisher |
| `PlayerDiedEvent` | PlayerDeathService | Player death | Multiple listeners |
| `PlayerRespawnedEvent` | PlayerRespawnService | Player resurrection | Multiple listeners |

### Layer 2: Real-Time Messages (Client-Facing)

These are SSE/WebSocket messages sent to clients:

| Message Type | Publisher | Purpose | Recipients |
|-------------|-----------|---------|------------|
| `player_entered` | RealTimeEventHandler._handle_player_entered() | Notify room about new player | Room occupants (excluding entering player) |
| `player_left` | RealTimeEventHandler._handle_player_left() | Notify room about departing player | Room occupants (excluding leaving player) |
| `room_update` | broadcast_room_update() | Full room state update | Specific player |
| `game_state` | Initial connection | Complete game state | Connecting player |
| `combat_event` | Combat system | Combat updates | Combat participants |
| `chat_message` | NATS message handler | Chat messages | Channel subscribers |
| `whisper` | NATS message handler | Private messages | Target player |
| `system_message` | Various | System announcements | All players or specific targets |

### Layer 3: NATS Messages (Internal Pub/Sub)

NATS subject-based messages for inter-service communication:

| Subject Pattern | Publisher | Purpose | Subscribers |
|----------------|-----------|---------|-------------|
| `chat.say.{room_id}` | ChatService | Room-based chat | Players in room |
| `chat.whisper.{player_id}` | ChatService | Private messages | Target player |
| `chat.global` | ChatService (planned) | Server-wide chat | All players |
| `chat.local.{subzone}` | ChatService (planned) | Sub-zone chat | Players in sub-zone |
| `combat.{room_id}` | CombatEventPublisher | Combat events | Players in room |

## Duplicate Event Analysis

### 🔴 CRITICAL: Player Movement Duplication - CONFIRMED

**Issue:** Players entering/leaving rooms trigger TWO separate message paths:

**Path 1: EventBus → RealTimeEventHandler → SSE/WebSocket (CORRECT)**
```
Source: server/models/room.py
1. Room.player_entered() publishes PlayerEnteredRoom event to EventBus
2. EventBus notifies RealTimeEventHandler
3. RealTimeEventHandler._handle_player_entered() sends "player_entered" message to clients
Location: server/realtime/event_handler.py lines 86-140
```

**Path 2: Direct broadcast_room_update() calls (DUPLICATE - SHOULD BE REMOVED)**
```
Source: server/realtime/websocket_handler.py
1. Movement command completes (line 424-432)
2. broadcast_room_update(player_id, room_id) called directly
3. Sends "room_update" message with full room state including occupants
4. Provides redundant occupant information already sent via Path 1
Location: server/realtime/websocket_handler.py lines 672-807
```

**Evidence:**
- Line 254: `await broadcast_room_update(player_id_str, str(canonical_room_id))` - After connection
- Line 425: `await broadcast_room_update(player_id, str(changed_room_id))` - After go command
- Line 432: `await broadcast_room_update(player_id, str(player.current_room_id))` - After go command

**Impact:**
- Players receive BOTH "player_entered" AND "room_update" messages
- Duplicate occupant list information
- Out-of-order delivery creates UX confusion
- Performance overhead from redundant broadcasts

**Solution:**
Remove direct broadcast_room_update() calls after movement. Let EventBus flow handle ALL room state notifications.

### 🟡 MEDIUM: Combat Event Overlap

**Issue:** Combat events published through both EventBus and NATS

**Paths:**
1. `CombatService` publishes `CombatStartedEvent` to EventBus
2. `CombatEventPublisher` subscribes to events and publishes to NATS `combat.{room_id}` subject
3. `NATSMessageHandler` subscribes to NATS and sends to clients

This appears intentional (event sourcing + message delivery) but creates complexity.

### 🟢 LOW: System Message Fragmentation

**Issue:** System messages sent through multiple paths

**Sources:**
- Direct SSE/WebSocket sends
- EventBus system events
- NATS system channel (planned)

## Event Ownership Recommendations

### Canonical Event Sources

Establish single authoritative source for each domain event:

| Domain | Canonical Publisher | Event Types |
|--------|-------------------|-------------|
| **Room Occupancy** | Room model | PlayerEnteredRoom, PlayerLeftRoom, NPCEntered/Left |
| **Combat** | CombatService | All combat events |
| **Chat** | ChatService via NATS | All chat messages |
| **Player Lifecycle** | AuthService/PlayerService | PlayerCreated, PlayerDeleted |
| **Admin Actions** | Admin commands | AdminTeleport, AdminKick, etc. |

### Message Delivery Rules

1. **Domain Events → EventBus ONLY**
   - All domain events MUST be published to EventBus
   - Domain code NEVER sends client messages directly

2. **EventBus → RealTimeEventHandler → Client Messages**
   - RealTimeEventHandler subscribes to EventBus events
   - Transforms events into client-facing messages
   - Handles all SSE/WebSocket message delivery

3. **Chat → NATS → Client Messages**
   - Chat messages use NATS pub/sub
   - NATSMessageHandler transforms NATS messages to client format
   - Clear separation from domain events

## Event Flow Diagram

```
Domain Layer (Room, Combat, Player)
    ↓ publishes
EventBus (Single Source of Truth)
    ↓ notifies
RealTimeEventHandler (Event → Message Transformer)
    ↓ sends
SSE/WebSocket (Client Delivery)
    ↓ receives
React Client
```

Parallel path for Chat:
```
ChatService
    ↓ publishes
NATS (chat.* subjects)
    ↓ subscribes
NATSMessageHandler
    ↓ sends
SSE/WebSocket
    ↓ receives
React Client
```

## Consolidation Strategy

### Phase 1: Audit Complete ✓

This document represents the audit results.

### Phase 2: Eliminate Duplicates

1. **Remove direct message sends from domain code**
   - Room model should ONLY publish EventBus events
   - Movement service should ONLY publish EventBus events
   - No direct broadcast_game_event() calls from domain layer

2. **Centralize message transformation in RealTimeEventHandler**
   - All EventBus events → client messages happen here
   - Single place to manage message format and delivery

3. **Document event ownership**
   - Each event type has ONE canonical publisher
   - Clear documentation of event flow
   - Tests verify no duplicate events

### Phase 3: Verify No Duplicates

1. Add integration tests that verify players receive exactly ONE message per domain action
2. Add event tracing to track event flow
3. Monitor for duplicate messages in production

## Implementation Checklist

- [x] Map all EventBus event types
- [x] Map all Real-Time message types
- [x] Map all NATS subject patterns
- [x] Identify duplicate event publishers
- [x] Document canonical event ownership
- [ ] Remove duplicate event publishers
- [ ] Add tests for event uniqueness
- [ ] Document event flow in architecture docs

## References

- `server/events/event_types.py` - EventBus event definitions
- `server/models/room.py` - Room event publishers
- `server/realtime/event_handler.py` - Event → Message transformation
- `server/realtime/sse_handler.py` - SSE message delivery
- `server/realtime/nats_message_handler.py` - NATS → Client messages
- `docs/COMPREHENSIVE_SYSTEM_AUDIT.md` - Original issue documentation
