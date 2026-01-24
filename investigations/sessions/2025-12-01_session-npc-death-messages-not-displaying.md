# BUG INVESTIGATION REPORT: NPC Death Messages Not Displaying in Game Info Panel

**Investigation Date**: 2025-12-01
**Investigator**: AI Assistant (Auto)
**Session ID**: 2025-12-01_session-npc-death-messages-not-displaying
**Bug Description**: NPC death messages are not printing in the Game Info panel

---

## EXECUTIVE SUMMARY

NPC death messages are not appearing in the Game Info panel because the client-side event processing in `GameClientV2Container.tsx` does not include handlers for NPC death events. The server correctly broadcasts NPC death events (`npc_died` via NATS and potentially `combat_death` events), but the client falls through to the default case which only logs unhandled event types without displaying messages.

**Root Cause**: Missing client-side event handlers for `combat_death` and `npc_died` event types.

**Impact**: Players do not see NPC death messages in the Game Info panel, reducing combat feedback and game immersion.

---

## DETAILED FINDINGS

### Phase 1: Bug Report Analysis

**Bug Description Parsed**:
**Symptom**: NPC death messages not displaying in Game Info panel

**Affected Component**: Client-side UI (Game Info Panel)

**Expected Behavior**: NPC death messages should appear in Game Info panel when NPCs die
- **Actual Behavior**: No NPC death messages appear in Game Info panel

**Affected Systems Identified**:

1. Server-side: NPC death event broadcasting (`CombatService`, `NATSMessageHandler`)
2. Server-side: Combat messaging integration (`CombatMessagingIntegration`)
3. Client-side: Event processing (`GameClientV2Container`)
4. Client-side: Message display (`GameInfoPanel`)

---

### Phase 2: System State Investigation

**Server Status**: No server errors related to NPC death event broadcasting found in recent logs.

**Log Analysis**:

- No specific errors for NPC death message broadcasting
- Server appears to be broadcasting events successfully (no broadcast errors found)
- Error logs contain unrelated issues (UUID serialization errors, WebSocket connection errors)

**Configuration Review**: Standard configuration; no anomalies detected.

---

### Phase 3: Code Analysis

#### Server-Side NPC Death Event Flow

**1. CombatService NPC Death Handling** (`server/services/combat_service.py:761-858`):

```758:858:server/services/combat_service.py
            # Publish death event if target died
            # BUGFIX: Enhanced logging and defensive exception handling to prevent disconnections
            # during NPC death event publishing. See: investigations/sessions/2025-11-20_combat-disconnect-bug-investigation.md

            if target_died and target.participant_type == CombatParticipantType.NPC:
                logger.info(
                    "NPC died in combat - starting death event handling",
                    target_name=target.name,
                    target_id=target.participant_id,
                    combat_id=combat.combat_id,
                    room_id=combat.room_id,
                )
```

**Key Finding**: `CombatService` publishes `NPCDiedEvent` to NATS via `_combat_event_publisher.publish_npc_died(death_event)` (line 841).

**2. NATSMessageHandler NPC Death Event Broadcasting** (`server/realtime/nats_message_handler.py:1939-2003`):

```1939:1987:server/realtime/nats_message_handler.py
    async def _handle_npc_died_event(self, data: dict[str, Any]):
        """
        Handle npc_died event - NATS to EventBus bridge pattern.
        ...
        """
        try:
            room_id = data.get("room_id")
            npc_id = data.get("npc_id")
            npc_name = data.get("npc_name")

            if not room_id:
                logger.warning("NPC died event missing room_id", data=data)
                return

            if not npc_id:
                logger.warning("NPC died event missing npc_id", data=data)
                return

            # Import here to avoid circular imports

            from server.events.event_types import NPCDied

            # Broadcast death event to room clients using injected connection_manager
            # AI: Room state mutation is handled by NPCLeftRoom event from lifecycle manager
            # AI: This prevents duplicate removal attempts and maintains single source of truth

            await self.connection_manager.broadcast_room_event("npc_died", room_id, data)
            logger.debug("NPC died event broadcasted", room_id=room_id, npc_id=npc_id, npc_name=npc_name)
```

**Key Finding**: `NATSMessageHandler` broadcasts `"npc_died"` room events to all clients in the room (line 1986).

**3. CombatMessagingIntegration** (`server/services/combat_messaging_integration.py:239-294`):

```239:294:server/services/combat_messaging_integration.py
    async def broadcast_combat_death(
        self,
        room_id: str,
        npc_name: str,
        xp_reward: int,
        combat_id: str,
    ) -> dict[str, Any]:
        """
        Broadcast NPC death message to all players in the room.
        ...
        """
        logger.info(
            "Broadcasting combat death",
            room_id=room_id,
            npc_name=npc_name,
            xp_reward=xp_reward,
            combat_id=combat_id,
        )

        # Generate death messages

        messages = {
            "death_message": f"{npc_name} dies.",
            "xp_reward": f"You gain {xp_reward} experience points.",
        }

        # Create death event

        death_event = build_event(
            "combat_death",
            {
                "combat_id": combat_id,
                "npc_name": npc_name,
                "xp_reward": xp_reward,
                "messages": messages,
            },
            room_id=room_id,
        )

        # Broadcast to all players in the room

        broadcast_stats = await self.connection_manager.broadcast_to_room(room_id, death_event)

        logger.debug(
            "Combat death broadcast completed",
            room_id=room_id,
            combat_id=combat_id,
            broadcast_stats=broadcast_stats,
        )

        return broadcast_stats
```

**Key Finding**: `broadcast_combat_death()` creates `"combat_death"` events with death messages. However, this method is **not currently being called** (see comment in `npc_combat_integration_service.py:540-542` indicating it was removed to prevent duplicate messages).

#### Client-Side Event Processing

**GameClientV2Container Event Processing** (`client/src/components/ui-v2/GameClientV2Container.tsx:258-873`):

The client processes events in `processEventQueue()` function with a switch statement. **CRITICAL FINDING**: No handler exists for `combat_death` or `npc_died` event types.

**Handled Event Types**:

- `game_state`
- `room_update` / `room_state`
- `lucidity_change`
- `player_hp_updated`
- `command_response`
- `chat_message`
- `room_occupants`
- `mythos_time_update`
- `game_tick`
- `npc_attacked`
- `player_attacked`
- `combat_started`
- `combat_ended`
- `player_update`
- `player_died`
- `player_respawned`

**Missing Event Handlers**:
❌ `combat_death` - **NOT HANDLED**

❌ `npc_died` - **NOT HANDLED**

**Default Case Behavior** (`client/src/components/ui-v2/GameClientV2Container.tsx:866-872`):

```866:872:client/src/components/ui-v2/GameClientV2Container.tsx
          // Add more event types as needed - this is a simplified version
          default: {
            logger.info('GameClientV2Container', 'Unhandled event type', {
              event_type: event.event_type,
              data_keys: event.data ? Object.keys(event.data) : [],
            });
            break;
          }
```

**Key Finding**: Unhandled events are only logged; no messages are added to the messages array for display in the Game Info panel.

#### Client-Side Message Display

**GameInfoPanel Component** (`client/src/components/ui-v2/panels/GameInfoPanel.tsx:15-181`):

The `GameInfoPanel` correctly receives and displays messages from the `messages` prop. The component supports various message types including `combat` (line 37-38), but messages are never added to the array because the event handlers are missing.

---

### Phase 4: Evidence Collection

#### Server-Side Evidence

1. **NPC Death Event Broadcasting**: `NATSMessageHandler._handle_npc_died_event()` broadcasts `"npc_died"` events (line 1986).

2. **Combat Death Event Creation**: `CombatMessagingIntegration.broadcast_combat_death()` creates `"combat_death"` events with formatted messages (line 273-274), but this method is not currently called.

3. **CombatService NPC Death Publishing**: `CombatService` publishes `NPCDiedEvent` to NATS which routes to `NATSMessageHandler._handle_npc_died_event()`.

#### Client-Side Evidence

1. **Missing Event Handlers**: `GameClientV2Container.tsx` has no case for `combat_death` or `npc_died` in the event processing switch statement.

2. **Unhandled Event Logging**: Unhandled events fall through to default case which only logs, does not create messages.

3. **Message Type Support**: `GameInfoPanel` supports `combat` message type styling (line 37-38), indicating the UI is prepared for combat messages.

#### Code References

**Server NPC Death Broadcast**: `server/realtime/nats_message_handler.py:1986` - broadcasts `"npc_died"` events

**Server Combat Death Event**: `server/services/combat_messaging_integration.py:273-274` - creates `"combat_death"` events (currently unused)

**Client Event Processing**: `client/src/components/ui-v2/GameClientV2Container.tsx:866-872` - default case for unhandled events
- **Client Message Display**: `client/src/components/ui-v2/panels/GameInfoPanel.tsx:37-38` - supports combat message type

---

### Phase 5: Root Cause Analysis

#### Root Cause Identified

**PRIMARY ROOT CAUSE**: Missing client-side event handlers for NPC death events.

The server correctly broadcasts NPC death events to clients:

1. `NPCDiedEvent` is published to NATS by `CombatService`
2. `NATSMessageHandler` receives the NATS message and broadcasts `"npc_died"` room events via WebSocket
3. Events are successfully sent to connected clients

However, the client-side event processing in `GameClientV2Container.tsx` does not include handlers for:

- `npc_died` events (currently broadcast by server)
- `combat_death` events (available in codebase but not currently used)

When these events arrive at the client, they fall through to the default case which only logs the event type without creating any messages for display in the Game Info panel.

#### Why This Happened

Based on code comments and architecture:

1. The system migrated from `broadcast_combat_death()` to NATS-based `NPCDiedEvent` publishing
2. Client-side handlers were not updated to handle the new `npc_died` event type
3. The old `combat_death` event handler was never implemented on the client side

#### Related Systems

**Combat System**: Correctly detects NPC death and publishes events

**NATS Message System**: Correctly routes NPC death events to clients

**WebSocket Broadcasting**: Successfully delivers events to connected clients
- **Client Event Queue**: Successfully receives events but doesn't process NPC death types

---

## SYSTEM IMPACT ASSESSMENT

### Scope

**Affected Component**: Client-side Game Info Panel message display

**Affected Users**: All players engaging in NPC combat

**Severity**: Medium - Reduces game feedback and immersion but does not break core functionality

### Impact

**User Experience**:

- Players do not see NPC death messages in the Game Info panel
- Reduced combat feedback and immersion
- Players may be uncertain if NPCs actually died

**System Functionality**:

- NPC death detection works correctly on server
- NPC respawning system works correctly
- XP awards work correctly
- Only the message display is affected

### Dependencies

No other systems depend on NPC death messages being displayed

- Combat system functions independently of message display
- NPC lifecycle management functions independently

---

## EVIDENCE DOCUMENTATION

### Server-Side Evidence

**1. NPC Death Event Broadcasting**:

- File: `server/realtime/nats_message_handler.py`
- Lines: 1986
- Evidence: `await self.connection_manager.broadcast_room_event("npc_died", room_id, data)`

**2. Combat Death Event Creation**:

- File: `server/services/combat_messaging_integration.py`
- Lines: 273-274
- Evidence: `death_event = build_event("combat_death", {...}, room_id=room_id)`

### Client-Side Evidence

**1. Missing Event Handlers**:

- File: `client/src/components/ui-v2/GameClientV2Container.tsx`
- Lines: 289-872
- Evidence: Switch statement contains no cases for `combat_death` or `npc_died`

**2. Default Case Behavior**:

- File: `client/src/components/ui-v2/GameClientV2Container.tsx`
- Lines: 866-872
- Evidence: Unhandled events only logged, no messages created

**3. Message Type Support**:

- File: `client/src/components/ui-v2/panels/GameInfoPanel.tsx`
- Lines: 37-38
- Evidence: `case 'combat': return 'text-mythos-terminal-warning font-bold';`

---

## INVESTIGATION RECOMMENDATIONS

### Priority 1: Implement Missing Event Handlers (CRITICAL)

**Action Required**: Add event handlers for NPC death events in `GameClientV2Container.tsx`

**Recommended Implementation**:

1. Add handler for `npc_died` events that extracts NPC name and creates death message
2. Optionally add handler for `combat_death` events for future compatibility
3. Format messages consistently with existing combat messages
4. Add messages to the messages array using `appendMessage()` function

**Investigation Notes**:

- Server broadcasts `npc_died` events with data: `{room_id, npc_id, npc_name, ...}`
- `combat_death` events contain structured messages: `{death_message, xp_reward}`
- Follow existing patterns from `npc_attacked` and `player_attacked` handlers

### Priority 2: Verify Event Data Structure (HIGH)

**Action Required**: Confirm exact structure of `npc_died` event data from server

**Investigation Notes**:

- Check what fields are included in `npc_died` events
- Verify XP reward information is available
- Ensure message formatting matches player expectations

### Priority 3: Testing Requirements (MEDIUM)

**Action Required**: Create test scenarios to verify NPC death messages display correctly

**Test Scenarios**:

1. NPC dies from player attack - verify death message appears
2. NPC dies with XP reward - verify XP message appears
3. Multiple NPCs die in sequence - verify all messages display
4. Player in different room - verify messages don't appear

---

## REMEDIATION PROMPT

**For Cursor Chat - Fix NPC Death Message Display**:

```
Fix the NPC death message display bug in the Game Info panel.

ROOT CAUSE:
The client-side event processing in GameClientV2Container.tsx is missing handlers for
npc_died and combat_death events. The server correctly broadcasts these events, but the
client falls through to the default case which only logs events without creating messages.

REQUIRED CHANGES:

1. Add event handler for 'npc_died' events in GameClientV2Container.tsx processEventQueue():
   - Extract npc_name from event.data
   - Create death message: "{npc_name} dies."
   - Add message to messages array using appendMessage() with messageType: 'system', channel: GAME_LOG_CHANNEL
   - Follow pattern from existing npc_attacked handler (lines 717-737)

2. Optionally add event handler for 'combat_death' events for future compatibility:
   - Extract messages.death_message and messages.xp_reward from event.data.messages
   - Add both messages to messages array with appropriate formatting
   - Use messageType: 'system' or 'combat' as appropriate

3. Test that NPC death messages now appear in Game Info panel when NPCs die in combat

FILES TO MODIFY:
- client/src/components/ui-v2/GameClientV2Container.tsx (add event handlers in processEventQueue switch statement)

REFERENCE IMPLEMENTATION:
- See npc_attacked handler (lines 717-737) for pattern
- See player_attacked handler (lines 739-764) for message formatting examples
- GameInfoPanel already supports 'combat' message type (line 37-38)
```

---

## INVESTIGATION COMPLETION CHECKLIST

[x] All investigation steps completed as written

- [x] Comprehensive evidence collected and documented
- [x] Root cause analysis completed
- [x] System impact assessed
- [x] Investigation report generated
- [x] No attempt made to fix issues (investigation only)
- [x] All findings clearly documented with evidence
- [x] Code references provided for all findings
- [x] Remediation prompt generated with root cause identified

---

**Investigation Status**: ✅ COMPLETE

**Next Steps**: Implement client-side event handlers for NPC death events as outlined in Remediation Prompt.
