# MythosMUD Multiplayer Scenarios Playbook

## Overview

This playbook contains detailed scenarios for testing multiplayer functionality in MythosMUD. Each scenario should work correctly when run back-to-back without restarting the server or clients, ensuring proper state management and clean transitions between test cases.

## Test Players

- **ArkanWolfshade** (AW) - password: Cthulhu1
- **Ithaqua** - password: Cthulhu1
- **Default Room**: `earth_arkham_city_sanitarium_room_foyer_001` (Main Foyer)

## Scenario Validation Requirements

- ✅ **Sequential Testing**: All scenarios must work back-to-back without server/client restarts
- ✅ **Clean State Management**: No stale game state information between scenarios
- ✅ **Message Isolation**: Players should only see messages relevant to current session
- ✅ **Event Broadcasting**: Proper event-to-real-time bridge functionality
- ✅ **Self-Message Exclusion**: Players should not see their own movement messages

---

## Scenario 1: Basic Connection/Disconnection Flow

### Description

Tests basic multiplayer connection and disconnection messaging between two players.

### Steps

1. **AW enters the game**
   - Expected: AW connects successfully to Main Foyer

2. **Ithaqua enters the game**
   - Expected: Ithaqua connects successfully to Main Foyer

3. **AW should see**: `"Ithaqua has entered the game."`
   - Validates: Connection events are properly broadcast to existing players

4. **Ithaqua should NOT see any enters/leaves/entered/left messages**
   - Validates: Self-message exclusion and no stale game state

5. **Ithaqua leaves the game**
   - Expected: Ithaqua disconnects cleanly

6. **AW should see**: `"Ithaqua has left the game."`
   - Validates: Disconnection events are properly broadcast

### Technical Components Tested

- ✅ `player_entered_game` event broadcasting
- ✅ `player_left_game` event broadcasting
- ✅ Event-to-Real-Time Bridge functionality
- ✅ Self-message exclusion logic
- ✅ Room occupant tracking
- ✅ WebSocket/SSE communication

### Status: ✅ PASSED

All requirements validated via Playwright testing.

---

## Scenario 2: Clean Game State on Connection

### Description

Tests that players don't see stale/previous game state information when connecting.

### Steps

1. **AW enters the game**
   - Expected: AW connects successfully

2. **AW should NOT see any previous game state information**
   - No previous player entering/leaving messages
   - No stale chat history from previous sessions
   - Clean message log

3. **Ithaqua enters the game**
   - Expected: Ithaqua connects successfully

4. **Ithaqua should NOT see any previous game state information**
   - No previous player entering/leaving messages
   - No stale chat history from previous sessions
   - Clean message log

5. **AW should see**: `"Ithaqua has entered the game."`
   - Validates: Current session events work correctly

### Technical Components Tested

- ✅ Pending message system cleanup
- ✅ Fresh game state delivery
- ✅ Session isolation
- ✅ Message history management

### Status: ❌ FAILED - COMPREHENSIVE AUDIT COMPLETED

**Critical Issues Identified:**
1. **Stale Message Persistence**: "X has left the game" messages persist across sessions
2. **Duplicate Event Broadcasting**: Multiple "entered game" messages appearing
3. **Self-Movement Messages**: Players see their own movement messages
4. **Mute Command Failure**: "An error occurred while processing your command"
5. **Event Ordering Issues**: Complex timing problems in event processing

**Root Cause Analysis Completed**:
- ✅ Event broadcasting system audit - **DUPLICATE EVENT SYSTEMS**
- ✅ Player service integration investigation - **MISSING APP STATE SERVICES**
- ✅ Message persistence system overhaul - **STALE MESSAGE PERSISTENCE**
- ✅ Event processing timing analysis - **EVENT ORDERING AND DUPLICATION**

**Comprehensive Fixes Required**:
See `COMPREHENSIVE_SYSTEM_AUDIT.md` for detailed analysis and recommended fixes

---

## Scenario 3: Movement Between Rooms

### Description

Tests multiplayer visibility when players move between different rooms.

### Steps

1. **AW enters the game** (Main Foyer)
2. **Ithaqua enters the game** (Main Foyer)
3. **AW moves east** to `earth_arkham_city_sanitarium_room_hallway_001`
4. **Ithaqua should see**: `"ArkanWolfshade leaves the room."`
5. **AW should see**: `"ArkanWolfshade enters the room."` (in new room)
6. **AW should NOT see**: Any self-movement messages
7. **Ithaqua moves east** to join AW
8. **AW should see**: `"Ithaqua enters the room."`
9. **Ithaqua should NOT see**: Any self-movement messages

### Technical Components Tested

- ❌ `PlayerEnteredRoom` event broadcasting
- ❌ `PlayerLeftRoom` event broadcasting
- ❌ Self-message exclusion in movement events
- ❌ Room subscription management
- ❌ Movement service integration

### Status: ❌ FAILED - CRITICAL ISSUES

**Issues Identified:**

1. **Self-Movement Messages**: Players see their own movement messages
2. **Duplicate Messages**: Multiple movement messages appearing
3. **Exclude Player Logic**: Not working correctly in movement broadcasts
4. **Event Ordering**: Problems with broadcast timing

**Root Cause**: Event broadcasting system not properly excluding players from their own events

---

## Scenario 3.5: Muting System and Emotes

### Description

Tests the muting system and emote functionality across game sessions.

### Steps

1. **AW enters the game**
2. **Ithaqua enters the game**
3. **AW mutes Ithaqua**
4. **AW leaves the game**
5. **Ithaqua leaves the game**
6. **Run scenarios 1 through 3** - They should still succeed
7. **Ithaqua uses the `dance` emote**
8. **Ithaqua sees**: `"You dance like nobody's watching!"`
9. **AW does NOT see Ithaqua's emote**
10. **AW unmutes Ithaqua**
11. **Ithaqua uses the `dance` emote**
12. **Ithaqua sees**: `"You dance like nobody's watching!"`
13. **AW sees Ithaqua's emote**

### Technical Components Tested

- ❌ Mute command functionality
- ❌ Emote system broadcasting
- ❌ Mute state persistence
- ❌ Session state management
- ❌ Command error handling

### Status: ❌ FAILED - CRITICAL ISSUES

**Issues Identified:**

1. **Mute Command Failure**: "An error occurred while processing your command."
2. **Self-Movement Messages**: Still persisting from Scenario 3
3. **Duplicate Messages**: Still persisting from Scenario 3
4. **Player Visibility**: Mute system may not recognize online players

**Root Cause**: Multiple systemic issues in event broadcasting and command processing

---

## Scenario 3: Movement Between Rooms

### Description

Tests multiplayer visibility when players move between different rooms.

### Steps

1. **AW enters the game** (Main Foyer)
2. **Ithaqua enters the game** (Main Foyer)
3. **AW moves east** to `earth_arkham_city_sanitarium_room_hallway_001`
4. **Ithaqua should see**: `"ArkanWolfshade leaves the room."`
5. **AW should see**: `"ArkanWolfshade enters the room."` (in new room)
6. **AW should NOT see**: Any self-movement messages
7. **Ithaqua moves east** to follow AW
8. **AW should see**: `"Ithaqua enters the room."`
9. **Players in Main Foyer should see**: `"Ithaqua leaves the room."`

### Technical Components to Test

- PlayerEnteredRoom/PlayerLeftRoom events
- Room-specific message broadcasting
- Movement service integration
- Cross-room event handling

### Status: ✅ PASSED

All requirements validated via Playwright testing.

---

## Scenario 3.5: Muting System Validation

### Description

Tests the muting system functionality and persistence across game sessions.

### Steps

1. **AW enters the game**
2. **Ithaqua enters the game**
3. **AW mutes Ithaqua**
4. **AW leaves the game**
5. **Ithaqua leaves the game**
6. **Run scenarios 1 through 3. They should still succeed**
7. **Ithaqua uses the `dance` emote**
8. **Ithaqua sees**: `"You dance like nobody's watching!"`
9. **AW does NOT see Ithaqua's emote**
10. **AW unmutes Ithaqua**
11. **Ithaqua uses the `dance` emote**
12. **Ithaqua sees**: `"You dance like nobody's watching!"`
13. **AW sees Ithaqua's emote**

### Technical Components to Test

- Muting system persistence
- Emote broadcasting with muting
- Mute state management
- Cross-session mute persistence
- Emote system integration

### Status: 🔄 IN PROGRESS

---

## Scenario 3: Movement Between Rooms (PLANNED)

### Description

Tests multiplayer visibility when players move between different rooms.

### Steps

1. **AW enters the game** (Main Foyer)
2. **Ithaqua enters the game** (Main Foyer)
3. **AW moves east** to `earth_arkham_city_sanitarium_room_hallway_001`
4. **Ithaqua should see**: `"ArkanWolfshade leaves the room."`
5. **AW should see**: `"ArkanWolfshade enters the room."` (in new room)
6. **AW should NOT see**: Any self-movement messages
7. **Ithaqua moves east** to follow AW
8. **AW should see**: `"Ithaqua enters the room."`
9. **Players in Main Foyer should see**: `"Ithaqua leaves the room."`

### Technical Components to Test

- PlayerEnteredRoom/PlayerLeftRoom events
- Room-specific message broadcasting
- Movement service integration
- Cross-room event handling

---

## Scenario 4: Chat Messages Between Players (PLANNED)

### Description

Tests chat message broadcasting between players in the same room.

### Steps

1. **Both players in same room**
2. **AW sends chat message**: `"Hello Ithaqua"`
3. **Ithaqua should see**: Chat message from AW
4. **AW should see**: Own chat message echo
5. **Ithaqua replies**: `"Greetings ArkanWolfshade"`
6. **AW should see**: Chat message from Ithaqua

### Technical Components to Test

- Chat message broadcasting
- Room-based chat isolation
- Message formatting and timestamps

---

## Scenario 5: Player Commands and Interactions (PLANNED)

### Description

Tests visibility of player commands and interactions.

### Steps

1. **Both players in same room**
2. **AW uses command**: `look`
3. **Ithaqua should NOT see**: AW's look command results
4. **AW uses emote**: `wave`
5. **Ithaqua should see**: AW's emote action
6. **Test room occupancy commands**: `who`

### Technical Components to Test

- Command privacy vs. visibility
- Emote system broadcasting
- Room occupancy display

---

## Scenario 6: Reconnection Handling (PLANNED)

### Description

Tests proper handling when players reconnect after disconnection.

### Steps

1. **Both players connected**
2. **AW force disconnects** (close browser/network issue)
3. **Ithaqua should see**: `"ArkanWolfshade has left the game."`
4. **AW reconnects**
5. **Ithaqua should see**: `"ArkanWolfshade has entered the game."`
6. **AW should see**: Current room state, no duplicate messages

### Technical Components to Test

- Connection state management
- Reconnection event handling
- State synchronization
- Duplicate message prevention

---

## Scenario 7: Multiple Players in Different Rooms (PLANNED)

### Description

Tests event isolation between different rooms.

### Steps

1. **AW in Main Foyer**
2. **Ithaqua in East Hallway**
3. **Third player joins Main Foyer**
4. **AW should see**: Third player join messages
5. **Ithaqua should NOT see**: Third player join messages
6. **Test cross-room isolation**

### Technical Components to Test

- Room-based event isolation
- Multi-player state management
- Event broadcasting scope

---

## Testing Infrastructure

### Playwright Test Framework

- **Location**: `client/test_multiplayer_scenario_1.js`
- **Capabilities**: Automated multi-browser testing
- **Usage**: Validates scenarios systematically

### Manual Testing Protocol

1. Use fresh browser sessions for each scenario
2. Clear browser state between scenarios if needed
3. Monitor console logs for event flow
4. Verify WebSocket/SSE communication
5. Check chat log message ordering

### Test Data Cleanup

Between scenarios, ensure:

- Pending messages are cleared
- Room occupancy is accurate
- No stale event subscriptions
- Clean WebSocket connections

---

## Implementation Status

### Completed Components

- ✅ Event-to-Real-Time Bridge (`server/realtime/event_handler.py`)
- ✅ Connection Manager (`server/realtime/connection_manager.py`)
- ✅ WebSocket Handler (`server/realtime/websocket_handler.py`)
- ✅ Client-side event handling (`client/src/components/GameTerminalWithPanels.tsx`)
- ✅ Room occupant tracking
- ✅ `player_entered_game` and `player_left_game` events

### 🚨 CRITICAL ISSUES IDENTIFIED (TESTING PAUSED)

**Root Cause Analysis Required:**

1. **Self-Movement Message Bug**: Players see their own movement messages
   - `exclude_player` logic not working correctly in movement broadcasts
   - Issue in `server/realtime/event_handler.py` movement handling
   - Affects both initial connection and regular movement

2. **Stale Message Persistence**: "X has left the game" messages persist on reconnection
   - Pending message clearing logic incomplete
   - Issue in `server/realtime/connection_manager.py` and `server/realtime/sse_handler.py`
   - Multiple attempts to fix have been insufficient

3. **Duplicate Message Issues**: Multiple "entered game" messages appearing
   - Event ordering and broadcast timing problems
   - Initial connection setup triggering unintended events

4. **Initial Connection Event Cascade**: Self-movement messages on first connect
   - `room.player_entered()` vs `room._players.add()` distinction not working
   - Connection setup in `server/realtime/websocket_handler.py` needs review

**Impact**: All multiplayer scenarios failing basic requirements

### Previous Known Issues (Less Critical)

- 🔧 Need better session isolation between scenarios

### Next Steps

1. Complete Scenario 2 fixes for clean game state
2. Implement Scenario 3 movement testing
3. Add comprehensive chat testing (Scenario 4)
4. Build automated test suite for all scenarios

---

## Code References

### Key Files

- **Event Handler**: `server/realtime/event_handler.py`
- **Connection Manager**: `server/realtime/connection_manager.py`
- **WebSocket Handler**: `server/realtime/websocket_handler.py`
- **Client Event Handling**: `client/src/components/GameTerminalWithPanels.tsx`
- **Movement Service**: `server/game/movement_service.py`

### Test Files

- **Self-Message Bug Tests**: `server/tests/test_self_message_bug.py`
- **Event Broadcasting Tests**: `server/tests/test_event_broadcasting_bugs.py`
- **Playwright Scenario Tests**: `client/test_multiplayer_scenario_1.js`

---

## Development Notes

As noted in the Pnakotic Manuscripts, "The boundaries between states must remain distinct, lest chaos seep through the dimensional barriers." Each scenario must maintain proper isolation while demonstrating the interconnected nature of the multiplayer system.

The multiplayer implementation represents a successful bridge between the event-driven backend architecture and the real-time client requirements, much like the dimensional gateways described in Wilmarth's Vermont correspondence - functional, but requiring careful management to prevent unwanted intrusions from previous sessions.

*"What has been tested once can be tested again, and with proper documentation, even madness becomes methodical."* - Dr. Armitage, 1928
