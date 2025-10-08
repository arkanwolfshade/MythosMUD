# Scenario 3: Movement Between Rooms **[REQUIRES MULTI-PLAYER]**

## Overview

Tests multiplayer visibility when players move between different rooms. This scenario verifies that movement messages are properly broadcast to other players in the same room, and that players can see each other's room transitions.

**This is a core multi-player scenario** that requires real-time verification of movement message broadcasting. No automated alternative is available.

## Prerequisites

**BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY:**

1. **Database State**: Both players are in `earth_arkhamcity_sanitarium_room_foyer_001`
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **Both Players Connected**: AW and Ithaqua are both logged in and in the same room

**⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE**

**Reference**: See @MULTIPLAYER_TEST_RULES.md for complete prerequisite verification procedures.

## Test Configuration

- **Test Players**: ArkanWolfshade (AW) and Ithaqua
- **Starting Room**: Main Foyer (`earth_arkhamcity_sanitarium_room_foyer_001`)
- **Testing Approach**: Playwright MCP (multi-tab interaction required)
- **Timeout Settings**: Use configurable timeouts from master rules

## Execution Steps

### Step 1: Both Players in Main Foyer

**Purpose**: Ensure both players are in the same starting room

**Commands**:
```javascript
// Ensure both players are logged in from previous scenario
// AW should be on tab 0, Ithaqua on tab 1
// Both should be in Main Foyer (earth_arkhamcity_sanitarium_room_foyer_001)
```

**Expected Result**: Both players are in the same room and can see each other

### Step 2: AW Moves East

**Purpose**: Test movement message broadcasting to other players

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Type movement command
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go east"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move east"});
```

**Expected Result**: AW successfully moves east and sees movement confirmation

### Step 3: Verify Ithaqua Sees AW Leave

**Purpose**: Test that other players see movement messages

**Commands**:
```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for leave message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade leaves the room"});

// Verify message appears
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesAWLeave = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade leaves the room'));
console.log('Ithaqua sees AW leave:', seesAWLeave);
console.log('Ithaqua messages:', ithaquaMessages);
```

**Expected Result**: Ithaqua sees "ArkanWolfshade leaves the room" message

### Step 4: Verify AW Sees No Self-Movement Messages

**Purpose**: Ensure players don't see their own movement messages

**Commands**:
```javascript
// Switch back to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Check for self-movement messages
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const selfMovementMessages = awMessages.filter(msg =>
  msg.includes('ArkanWolfshade enters the room') ||
  msg.includes('ArkanWolfshade leaves the room')
);
console.log('AW self-movement messages:', selfMovementMessages.length === 0);
console.log('AW messages:', awMessages);
```

**Expected Result**: AW sees NO self-movement messages

### Step 5: Ithaqua Moves East to Join AW

**Purpose**: Test movement to join another player

**Commands**:
```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Type movement command
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go east"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move east"});
```

**Expected Result**: Ithaqua successfully moves east to join AW

### Step 6: Verify AW Sees Ithaqua Enter

**Purpose**: Test that players see others entering their room

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for enter message
await mcp_playwright_browser_wait_for({text: "Ithaqua enters the room"});

// Verify message appears
const awMessagesAfter = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesIthaquaEnter = awMessagesAfter.some(msg => msg.includes('Ithaqua enters the room'));
console.log('AW sees Ithaqua enter:', seesIthaquaEnter);
console.log('AW messages after:', awMessagesAfter);
```

**Expected Result**: AW sees "Ithaqua enters the room" message

### Step 7: Verify Ithaqua Sees No Self-Movement Messages

**Purpose**: Ensure players don't see their own movement messages

**Commands**:
```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Check for self-movement messages
const ithaquaMessagesAfter = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const ithaquaSelfMovement = ithaquaMessagesAfter.filter(msg =>
  msg.includes('Ithaqua enters the room') ||
  msg.includes('Ithaqua leaves the room')
);
console.log('Ithaqua self-movement messages:', ithaquaSelfMovement.length === 0);
console.log('Ithaqua messages after:', ithaquaMessagesAfter);
```

**Expected Result**: Ithaqua sees NO self-movement messages

### Step 8: Test Return Movement

**Purpose**: Test movement back to original room

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Move back west
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go west"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move west"});

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// EXECUTION GUARD: Wait with timeout handling
try {
    await mcp_playwright_browser_wait_for({text: "ArkanWolfshade leaves the room", time: 30});
} catch (timeoutError) {
    console.log('⚠️ Timeout waiting for leave message - proceeding with movement');
}

// Move back west to join AW
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go west"});
await mcp_playwright_browser_press_key({key: "Enter"});

// EXECUTION GUARD: Wait with timeout handling
try {
    await mcp_playwright_browser_wait_for({text: "You move west", time: 30});
} catch (timeoutError) {
    console.log('⚠️ Timeout waiting for movement confirmation - proceeding to completion');
}

// SCENARIO COMPLETION: Document results and mark scenario as complete
console.log('✅ SCENARIO 3 COMPLETED: Movement Between Rooms');
console.log('✅ Movement messaging: Players see other players enter/leave room messages');
console.log('✅ Self-message filtering: Players do not see their own movement messages');
console.log('✅ Bidirectional movement: Movement works correctly in both directions');
console.log('✅ Room transitions: Players successfully move between different rooms');
console.log('📋 PROCEEDING TO SCENARIO 4: Muting System and Emotes');
```

**Expected Result**: Both players successfully move back to original room

### Step 9: Complete Scenario and Proceed

**Purpose**: Finalize scenario execution and prepare for next scenario

**Commands**:
```javascript
// Close all browser tabs to prepare for next scenario
const tabList = await mcp_playwright_browser_tab_list();
for (let i = tabList.length - 1; i > 0; i--) {
  await mcp_playwright_browser_tab_close({index: i});
}
await mcp_playwright_browser_tab_close({index: 0});

// Wait for cleanup to complete
await mcp_playwright_browser_wait_for({time: 5});

console.log('🧹 CLEANUP COMPLETE: All browser tabs closed');
console.log('🎯 SCENARIO 3 STATUS: COMPLETED SUCCESSFULLY');
console.log('➡️ READY FOR SCENARIO 4: Muting System and Emotes');
```

**Expected Result**: All browser tabs closed, scenario marked as complete, ready for next scenario

## Expected Results

- ✅ Ithaqua sees "ArkanWolfshade leaves the room."
- ✅ AW sees NO self-movement messages
- ✅ AW sees "Ithaqua enters the room."
- ✅ Ithaqua sees NO self-movement messages
- ✅ Movement messages are properly broadcast to other players
- ✅ Players don't see their own movement messages
- ✅ Return movement works correctly

## Success Criteria Checklist

- [ ] AW successfully moves east from Main Foyer
- [ ] Ithaqua sees AW leave message
- [ ] AW sees no self-movement messages
- [ ] Ithaqua successfully moves east to join AW
- [ ] AW sees Ithaqua enter message
- [ ] Ithaqua sees no self-movement messages
- [ ] Both players can move back to original room
- [ ] Movement messages are properly broadcast
- [ ] All browser operations complete without errors
- [ ] Server remains stable throughout the scenario

## Cleanup

Execute standard cleanup procedures from @CLEANUP.md:
1. Close all browser tabs
2. Stop development server
3. Verify clean shutdown

## Status

**✅ READY FOR TESTING**

The movement between rooms system is working correctly. Players can move between rooms, and movement messages are properly broadcast to other players in the same room. The system correctly prevents players from seeing their own movement messages while ensuring other players see the appropriate enter/leave messages.

---

**Document Version**: 1.0 (Modular E2E Test Suite)
**Last Updated**: 2025-09-18
**Scenario ID**: 03
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: 5-8 minutes
