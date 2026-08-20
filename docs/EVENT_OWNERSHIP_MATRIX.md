# Event Ownership Matrix

**Version 1.0.0** · MythosMUD · 2026-07-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Document Version:** 1.0
**Date:** November 3, 2025
**Status:** Architecture Audit
**Purpose:** Map all event publishers and identify duplicate event sources

## 2. Overview

**[SPEC]**
This document maps the complete event publishing architecture in MythosMUD to identify:

1. All event publishers and their sources
2. Duplicate or overlapping events
3. Event flow through the system
4. Canonical event ownership

## 3. Event Publishing Layers

**[SPEC]**

### Layer 1: EventBus Events (Domain Events)

These are domain events published through the EventBus system defined in `server/events/event_types.py`:

| Event Class             | Publisher             | Purpose                          | Listeners            |
| ----------------------- | --------------------- | -------------------------------- | -------------------- |
| `PlayerEnteredRoom`     | Room.player_entered() | Player joins room occupant list  | RealTimeEventHandler |
| `PlayerLeftRoom`        | Room.player_left()    | Player leaves room occupant list | RealTimeEventHandler |
| `ObjectAddedToRoom`     | Room.object_added()   | Object added to room             | RealTimeEventHandler |
| `ObjectRemovedFromRoom` | Room.object_removed() | Object removed from room         | RealTimeEventHandler |
| `NPCEnteredRoom`        | Room.npc_entered()    | NPC joins room                   | RealTimeEventHandler |
| `NPCLeftRoom`           | Room.npc_left()       | NPC leaves room                  | RealTimeEventHandler |
| `PlayerDiedEvent`       | PlayerDeathService    | Player death                     | Multiple listeners   |
| `PlayerRespawnedEvent`  | PlayerRespawnService  | Player resurrection              | Multiple listeners   |

**[SPEC]** Combat event classes (`CombatStartedEvent`, `PlayerAttackedEvent`, `NPCAttackedEvent`,
`CombatEndedEvent`, `CombatTargetSwitchEvent`, etc., all in `server/events/combat_events.py`)
subclass `BaseEvent` and are EventBus-*eligible*, but **combat never publishes them to EventBus** —
they were never actually listened to by `CombatEventPublisher`; the rows above claiming that were
wrong and are removed here. `PlayerDiedEvent`/`PlayerMortallyWoundedEvent`/`PlayerDPDecayEvent`
above are a separate case: `PlayerDeathService` publishes them to EventBus for its own listeners,
and `CombatEventPublisher` separately publishes the *same* dataclasses straight to NATS when
death/mortally-wounded happens mid-combat (`combat_death_handler.py`) — two independent consumers
of one dataclass, not a chain. See §4 and §5 for the corrected combat delivery model (#634).

### Layer 2: Real-Time Messages (Client-Facing)

These are WebSocket messages sent to clients:

| Message Type     | Publisher                                     | Purpose                            | Recipients                                 |
| ---------------- | --------------------------------------------- | ---------------------------------- | ------------------------------------------ |
| `player_entered` | RealTimeEventHandler._handle_player_entered() | Notify room about new player       | Room occupants (excluding entering player) |
| `player_left`    | RealTimeEventHandler._handle_player_left()    | Notify room about departing player | Room occupants (excluding leaving player)  |
| `room_update`    | broadcast_room_update()                       | Full room state update             | Specific player                            |
| `game_state`     | Initial connection                            | Complete game state                | Connecting player                          |
| `combat_event`   | Combat system                                 | Combat updates                     | Combat participants                        |
| `chat_message`   | NATS message handler                          | Chat messages                      | Channel subscribers                        |
| `whisper`        | NATS message handler                          | Private messages                   | Target player                              |
| `system_message` | Various                                       | System announcements               | All players or specific targets            |

### Layer 3: NATS Messages (Internal Pub/Sub)

NATS subject-based messages for inter-service communication:

| Subject Pattern                        | Publisher             | Purpose                       | Subscribers      |
| --------------------------------------- | --------------------- | ------------------------------ | ---------------- |
| `chat.say.{room_id}`                    | ChatService           | Room-based chat                | Players in room  |
| `chat.whisper.{player_id}`              | ChatService           | Private messages               | Target player    |
| `chat.global`                           | ChatService (planned) | Server-wide chat                | All players      |
| `chat.local.{subzone}`                  | ChatService (planned) | Sub-zone chat                   | Players in sub-zone |
| `combat.started.{room_id}`              | CombatEventPublisher  | Combat begins                   | Players in room  |
| `combat.ended.{room_id}`                | CombatEventPublisher  | Combat ends                     | Players in room  |
| `combat.attack.{room_id}`               | CombatEventPublisher  | Player attacks (any target)     | Players in room  |
| `combat.npc_attacked.{room_id}`         | CombatEventPublisher  | Player attacks an NPC           | Players in room  |
| `combat.damage.{room_id}`               | CombatEventPublisher  | NPC takes damage                | Players in room  |
| `combat.npc_died.{room_id}`             | CombatEventPublisher  | NPC dies                        | Players in room  |
| `combat.dp_update.{player_id}`          | CombatPersistenceHandler (not CombatEventPublisher) | Player DP changes in combat | Target player |
| `combat.player_died.{room_id}`          | CombatEventPublisher  | Player dies (#634)              | Players in room  |
| `combat.player_mortally_wounded.{room_id}` | CombatEventPublisher | Player enters mortally-wounded state (#634) | Players in room |
| `combat.target_switch.{room_id}`        | CombatEventPublisher  | NPC aggro switches target, ADR-016 (#634) | Players in room |
| `combat.dp_decay.{player_id}`           | CombatEventPublisher  | Mortally-wounded DP decay tick (#634) | Target player |

All `combat.*` subjects above are published by direct, synchronous, imperative calls from
`CombatService`/`CombatEventHandler`/`CombatDeathHandler`/the taunt command/the game tick — **never**
via an EventBus subscription. See §4.

## 4. Duplicate Event Analysis

**[SPEC]**

### 🔴 CRITICAL: Player Movement Duplication - CONFIRMED

**Issue:** Players entering/leaving rooms trigger TWO separate message paths:

### Path 1: EventBus → RealTimeEventHandler → WebSocket (CORRECT)

```
Source: server/models/room.py
1. Room.player_entered() publishes PlayerEnteredRoom event to EventBus
2. EventBus notifies RealTimeEventHandler
3. RealTimeEventHandler._handle_player_entered() sends "player_entered" message to clients
Location: server/realtime/event_handler.py lines 86-140
```

### Path 2: Direct broadcast_room_update() calls (DUPLICATE - REMOVED)

**Status:** Resolved. Duplicate calls have been removed; room state is notified only via EventBus.

- **websocket_handler.py:** Duplicate calls after movement were removed in Phase 1.2 (see comment at line 526).
- **teleport_helpers.py:** Removed from `broadcast_teleport_updates()` and `execute_confirm_teleport()`. Confirm teleport now uses `update_player_room_location()` so `Room.player_entered()`/`player_left()` fire and EventBus sends notifications.
- **goto_helpers.py:** Removed from `execute_goto_teleport()` and `execute_confirm_goto()`. Goto flows now use `update_player_room_location()` so EventBus handles room state.

### Impact

Players receive BOTH "player_entered" AND "room_update" messages

- Duplicate occupant list information
- Out-of-order delivery creates UX confusion
- Performance overhead from redundant broadcasts

### Solution (Implemented)

Direct broadcast_room_update() calls after movement have been removed. Teleport and goto flows now call `update_player_room_location()` (which invokes `Room.player_left()`/`player_entered()`), so EventBus handles all room state notifications.

### 🟡 RESOLVED (#634): Combat's Two Delivery Paths, Documented as an Intentional Dual Path

**Prior claim (wrong, corrected 2026-08):** this section previously stated combat events flow
`CombatService → EventBus → CombatEventPublisher (subscriber) → NATS`. Verified against code: that
subscription never existed. `CombatEventPublisher` has no `event_bus` parameter and subscribes to
nothing; `CombatService`/`CombatEventHandler`/`CombatDeathHandler` call its `publish_*` methods
directly and imperatively. Zero combat event ever touches EventBus (the `PlayerDied*` family is the
one exception — see the Layer 1 note above).

**Actual architecture — two independent delivery paths, kept intentionally, not merged:**

1. **NATS path (`CombatEventPublisher`, `server/services/combat_event_publisher.py`).** Direct,
   synchronous, `await`-chained calls to NATS. Preserves per-call-chain ordering and surfaces
   failures via error-level logs (no silent drop). This is what makes combat "NATS-consumable" —
   cross-instance fan-out, logging, replay.
2. **Direct room broadcast path (`server/services/combat_messaging/`, `CombatBroadcastMixin` +
   `PlayerBroadcastMixin`).** Direct `ConnectionManager.broadcast_to_room()` /
   `send_personal_message()` calls — the low-latency path for the room the action happened in.

**Why not route combat through EventBus instead (considered and rejected in #634):** `DistributedEventBus.publish()`
does local fan-out *and* a fire-and-forget `loop.create_task(bridge.publish(event))` with no task
tracking and a silent `except RuntimeError: pass` — both violations of this repo's own
`ASYNC_ANTI_PATTERNS_QUICK_REF.md`. Adding that hop to a latency- and ordering-sensitive path like
combat, on top of building net-new EventBus subscribers to replace the direct broadcast path, was
judged a materially bigger and riskier lift than the map justified. `DistributedEventBus`'s own bugs
are unaddressed here and would need fixing before combat could safely route through it.

**Every live combat action publishes to both paths deliberately** — this is `BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md`
rule 5's chat exemption extended to combat, not a bug to fix. See rule 5 there for the exact wording.

### 🟢 LOW: System Message Fragmentation

**Issue:** System messages sent through multiple paths

### Sources

Direct WebSocket sends

- EventBus system events
- NATS system channel (planned)

## 5. Event Ownership Recommendations

**[SPEC]**

### Canonical Event Sources

Establish single authoritative source for each domain event:

| Domain               | Canonical Publisher       | Event Types                                        |
| -------------------- | ------------------------- | -------------------------------------------------- |
| **Room Occupancy**   | Room model                | PlayerEnteredRoom, PlayerLeftRoom, NPCEntered/Left |
| **Combat**           | CombatService             | All combat events                                  |
| **Chat**             | ChatService via NATS      | All chat messages                                  |
| **Player Lifecycle** | AuthService/PlayerService | PlayerCreated, PlayerDeleted                       |
| **Admin Actions**    | Admin commands            | AdminTeleport, AdminKick, etc.                     |

### Message Delivery Rules

1. **Domain Events → EventBus ONLY**

   - All domain events MUST be published to EventBus
   - Domain code NEVER sends client messages directly

2. **EventBus → RealTimeEventHandler → Client Messages**

   - RealTimeEventHandler subscribes to EventBus events
   - Transforms events into client-facing messages
   - Handles all WebSocket message delivery

3. **Chat → NATS → Client Messages**

   - Chat messages use NATS pub/sub
   - NATSMessageHandler transforms NATS messages to client format
   - Delivered via WebSocket to clients
   - Clear separation from domain events

4. **Combat → NATS AND direct room broadcast, deliberately dual (#634)**

   - `CombatEventPublisher` publishes to NATS `combat.*` subjects for cross-instance
     consumption/logging/replay, in parallel with `CombatBroadcastMixin`/`PlayerBroadcastMixin`
     direct `ConnectionManager` calls for low-latency in-room delivery
   - Combat does **not** go through EventBus — see §4's resolved combat section
   - Not a rule violation: this is the same NATS exemption chat has, extended to combat

## 6. Event Flow Diagram

**[NOTE]**

```
Domain Layer (Room, Combat, Player)
    ↓ publishes
EventBus (Single Source of Truth)
    ↓ notifies
RealTimeEventHandler (Event → Message Transformer)
    ↓ sends
WebSocket (Client Delivery)
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
WebSocket
    ↓ receives
React Client
```

## 7. Consolidation Strategy

**[SPEC]**

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

## 8. Implementation Checklist

**[SPEC]**
[x] Map all EventBus event types

- [x] Map all Real-Time message types
- [x] Map all NATS subject patterns
- [x] Identify duplicate event publishers
- [x] Document canonical event ownership
- [ ] Remove duplicate event publishers
- [ ] Add tests for event uniqueness
- [ ] Document event flow in architecture docs

## 9. References

**[SPEC]**
`server/events/event_types.py` - EventBus event definitions

- `server/models/room.py` - Room event publishers
- `server/realtime/event_handler.py` - Event → Message transformation
- `server/realtime/connection_manager.py` - WebSocket message delivery
- `server/realtime/nats_message_handler.py` - NATS → Client messages
- `docs/COMPREHENSIVE_SYSTEM_AUDIT.md` - Original issue documentation

## 10. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 1.1.0 | 2026-08-20 | #634: corrected the false claim that combat events flow through EventBus (they never have); documented the actual dual NATS + direct-broadcast delivery path as intentional; added 4 new NATS subjects (`combat.player_died`, `combat.player_mortally_wounded`, `combat.target_switch`, `combat.dp_decay`) and removed 3 dead ones (`combat.turn`, `combat.timeout`, `combat.npc_action`) |
