# Scenario 33: Rest Command **[REQUIRES MULTI-PLAYER]**

## Overview

Tests the `/rest` command functionality including 10-second countdown, combat blocking, rest location instant
disconnect, and interruption logic. This scenario verifies that players can cleanly disconnect using `/rest` with proper
countdown and interruption handling.

## Prerequisites

### BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY

1. **Database State**: Both players are in `earth_arkhamcity_sanitarium_room_foyer_001`
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **Both Players Connected**: AW and Ithaqua are both logged in and in the same room
5. **No Active Rest Countdowns**: No players currently resting

### ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE

**Reference**: See @MULTIPLAYER_TEST_RULES.md for complete prerequisite verification procedures.

## Test Configuration

**Test Players**: ArkanWolfshade (AW) and Ithaqua

**Starting Room**: Main Foyer (`earth_arkhamcity_sanitarium_room_foyer_001`)

**Testing Approach**: Playwright MCP (multi-tab interaction required)

**Timeout Settings**: Use configurable timeouts from master rules

**Rest Countdown Duration**: 10 seconds

## Testing Approach Rationale

### Why Playwright MCP is Required

**Multi-tab Coordination**: Requires 2+ browser tabs to test rest interruption and message broadcasting

**Real-time Interaction**: Must verify rest countdown messages and interruption behavior

**Combat Testing**: Must test combat blocking and interruption

**Movement Testing**: Must test movement interruption

**State Verification**: Must verify player position changes (sitting) and disconnect behavior

### Standard Playwright Not Suitable

Cannot handle multiple browser tabs simultaneously

- Cannot verify real-time state changes across players
- Cannot test complex interruption scenarios

## Execution Steps

### Step 1: Both Players Connected

**Purpose**: Ensure both players are ready for rest command testing

**Commands**:

```javascript
// Ensure both players are logged in from previous scenario
// AW should be on tab 0, Ithaqua on tab 1
// Both should be in the same room (foyer)

// Verify both players are in the same room
await mcp_playwright_browser_tabs({action: "list"});
// Should show 2 tabs: AW (tab 0) and Ithaqua (tab 1)
```

**Expected Result**: Both players are connected and in the same room

### Step 2: Test /rest Command Blocked During Combat

**Purpose**: Verify `/rest` command is blocked entirely during combat

**Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tabs({action: "select", index: 0});

// Start combat with Ithaqua (if NPC available) or verify combat state
// For this test, we'll simulate being in combat
// Note: Actual combat initiation may require an NPC or another mechanism

// Try to use /rest during combat
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/rest"
});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for response
await mcp_playwright_browser_wait_for({time: 1});

// Check response message
const restResponse = await mcp_playwright_browser_evaluate({
    function: "() => { const messages = Array.from(document.querySelectorAll('.message')).slice(-2); return messages.map(m
    => m.textContent.trim()).join('\\n'); }"
});
console.log('Rest command response:', restResponse);

// Verify command is blocked
const isBlocked = restResponse.includes('cannot rest during combat') ||
                  restResponse.includes('combat') && restResponse.includes('cannot');
console.log('Rest blocked during combat:', isBlocked);
// Should be true
```

**Expected Result**: `/rest` command is blocked with "Cannot rest during combat" message

### Step 3: Test /rest Command Starts Countdown

**Purpose**: Verify `/rest` command starts 10-second countdown when not in combat

**Commands**:

```javascript
// Ensure AW is not in combat
// Switch to AW's tab
await mcp_playwright_browser_tabs({action: "select", index: 0});

// Use /rest command
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/rest"
});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for response
await mcp_playwright_browser_wait_for({time: 1});

// Check response message
const restStartResponse = await mcp_playwright_browser_evaluate({
    function: "() => { const messages = Array.from(document.querySelectorAll('.message')).slice(-2); return messages.map(m => m.textContent.trim()).join('\\n'); }"
});
console.log('Rest start response:', restStartResponse);

// Verify countdown started
const countdownStarted = restStartResponse.includes('rest') &&
                         (restStartResponse.includes('10') || restStartResponse.includes('countdown'));
console.log('Countdown started:', countdownStarted);
// Should be true

// Verify player position changed to sitting (check character info panel)
const characterInfo = await mcp_playwright_browser_evaluate({
    function: "() => { const panel = document.querySelector('[data-testid=\"character-info-panel\"]'); return panel ? panel.textContent : ''; }"
});
console.log('Character info:', characterInfo);
const isSitting = characterInfo.includes('sitting') || characterInfo.includes('Sitting');
console.log('Player is sitting:', isSitting);
// Should be true
```

**Expected Result**: `/rest` command starts countdown, player position changes to sitting

### Step 4: Test Rest Interruption by Movement

**Purpose**: Verify movement interrupts rest countdown

**Commands**:

```javascript
// AW should be resting (from Step 3)
// Switch to AW's tab
await mcp_playwright_browser_tabs({action: "select", index: 0});

// Try to move (this should interrupt rest)
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/go north"
});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for response
await mcp_playwright_browser_wait_for({time: 1});

// Check response messages
const movementResponse = await mcp_playwright_browser_evaluate({
    function: "() => { const messages = Array.from(document.querySelectorAll('.message')).slice(-3); return messages.map(m => m.textContent.trim()).join('\\n'); }"
});
console.log('Movement response:', movementResponse);

// Verify rest was interrupted
const restInterrupted = movementResponse.includes('interrupted') ||
                       movementResponse.includes('interrupt');
console.log('Rest interrupted by movement:', restInterrupted);
// Should be true

// Verify player can move (rest was cancelled)
const canMove = movementResponse.includes('moved') ||
                movementResponse.includes('north') ||
                movementResponse.includes('room');
console.log('Player can move:', canMove);
// Should be true
```

**Expected Result**: Movement interrupts rest countdown, player can move normally

### Step 5: Test Rest Interruption by Spellcasting

**Purpose**: Verify spellcasting interrupts rest countdown

**Commands**:

```javascript
// Start rest again
await mcp_playwright_browser_tabs({action: "select", index: 0});
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/rest"
});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({time: 1});

// Try to cast a spell (this should interrupt rest)
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/cast heal"
});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for response
await mcp_playwright_browser_wait_for({time: 1});

// Check response messages
const spellResponse = await mcp_playwright_browser_evaluate({
    function: "() => { const messages = Array.from(document.querySelectorAll('.message')).slice(-3); return messages.map(m => m.textContent.trim()).join('\\n'); }"
});
console.log('Spell response:', spellResponse);

// Verify rest was interrupted
const restInterruptedBySpell = spellResponse.includes('interrupted') ||
                                spellResponse.includes('interrupt');
console.log('Rest interrupted by spellcasting:', restInterruptedBySpell);
// Should be true
```

**Expected Result**: Spellcasting interrupts rest countdown

### Step 6: Test Rest Interruption by Being Attacked

**Purpose**: Verify being attacked interrupts rest countdown

**Commands**:

```javascript
// Start rest again
await mcp_playwright_browser_tabs({action: "select", index: 0});
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/rest"
});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({time: 1});

// From Ithaqua's tab, attack AW (this should interrupt AW's rest)
await mcp_playwright_browser_tabs({action: "select", index: 1});
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/attack ArkanWolfshade"
});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for combat to start
await mcp_playwright_browser_wait_for({time: 2});

// Switch back to AW's tab to check if rest was interrupted
await mcp_playwright_browser_tabs({action: "select", index: 0});
const attackResponse = await mcp_playwright_browser_evaluate({
    function: "() => { const messages = Array.from(document.querySelectorAll('.message')).slice(-5); return messages.map(m => m.textContent.trim()).join('\\n'); }"
});
console.log('Attack response:', attackResponse);

// Verify rest was interrupted
const restInterruptedByAttack = attackResponse.includes('interrupted') ||
                                 attackResponse.includes('interrupt') ||
                                 attackResponse.includes('combat');
console.log('Rest interrupted by attack:', restInterruptedByAttack);
// Should be true
```

**Expected Result**: Being attacked interrupts rest countdown

### Step 7: Test Rest Countdown Completion

**Purpose**: Verify rest countdown completes and player disconnects after 10 seconds

**Commands**:

```javascript
// Start rest again (ensure not in combat)
await mcp_playwright_browser_tabs({action: "select", index: 0});

// Use /rest command
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/rest"
});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({time: 1});

// Wait for countdown to complete (10 seconds)
console.log('Waiting for rest countdown to complete (10 seconds)...');
await mcp_playwright_browser_wait_for({time: 12});

// From Ithaqua's tab, check if AW is gone
await mcp_playwright_browser_tabs({action: "select", index: 1});
const occupantsAfterRest = await mcp_playwright_browser_evaluate({
    function: "() => { const panel = document.querySelector('[data-testid=\"occupants-panel\"]'); return panel ? panel.textContent : ''; }"
});
console.log('Occupants after rest completion:', occupantsAfterRest);

// Verify AW is gone (disconnected)
const hasAWAfterRest = occupantsAfterRest.includes('ArkanWolfshade') ||
                       occupantsAfterRest.includes('AW');
console.log('AW visible after rest:', hasAWAfterRest);
// Should be false (AW should be disconnected)

// Check for disconnect message
const disconnectMessages = await mcp_playwright_browser_evaluate({
    function: "() => { const messages = Array.from(document.querySelectorAll('.message')).slice(-5); return messages.map(m => m.textContent.trim()).join('\\n'); }"
});
console.log('Disconnect messages:', disconnectMessages);
```

**Expected Result**: AW disconnects after 10-second countdown completes

### Step 8: Test Rest Location Instant Disconnect

**Purpose**: Verify instant disconnect in rest locations (inns/hotels/motels)

**Commands**:

```javascript
// Note: This test requires a room with rest_location: true
// For now, we'll test the logic that checks for rest_location
// Actual rest location rooms may need to be created in the game world

// Reconnect AW for this test
// (This step may require manual reconnection or using a new tab)

// Move AW to a rest location (if available)
// Or verify the rest_location check logic works

// From AW's tab, use /rest in rest location
await mcp_playwright_browser_tabs({action: "select", index: 0});
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/rest"
});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for response
await mcp_playwright_browser_wait_for({time: 1});

// Check response - should be instant disconnect if in rest location
const restLocationResponse = await mcp_playwright_browser_evaluate({
    function: "() => { const messages = Array.from(document.querySelectorAll('.message')).slice(-2); return messages.map(m => m.textContent.trim()).join('\\n'); }"
});
console.log('Rest location response:', restLocationResponse);

// If in rest location, should disconnect immediately (no countdown)
// If not in rest location, should start countdown (from Step 3)
```

**Expected Result**: In rest location, instant disconnect; otherwise, countdown starts

### Step 9: Test Non-Interrupt Actions

**Purpose**: Verify chat, look, and inventory commands do NOT interrupt rest

**Commands**:

```javascript
// Start rest again
await mcp_playwright_browser_tabs({action: "select", index: 0});
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/rest"
});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({time: 1});

// Try chat command (should NOT interrupt)
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/say Hello"
});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({time: 1});

// Try look command (should NOT interrupt)
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/look"
});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({time: 1});

// Check if rest is still active (countdown should continue)
// Wait a few seconds and verify player is still resting
await mcp_playwright_browser_wait_for({time: 3});

// Verify rest countdown is still active (player should still be in room)
await mcp_playwright_browser_tabs({action: "select", index: 1});
const occupantsDuringRest = await mcp_playwright_browser_evaluate({
    function: "() => { const panel = document.querySelector('[data-testid=\"occupants-panel\"]'); return panel ? panel.textContent : ''; }"
});
console.log('Occupants during rest (non-interrupt actions):', occupantsDuringRest);

// AW should still be visible (rest not interrupted by chat/look)
const hasAWDuringRest = occupantsDuringRest.includes('ArkanWolfshade') ||
                        occupantsDuringRest.includes('AW');
console.log('AW visible during rest (non-interrupt):', hasAWDuringRest);
// Should be true (rest continues, not interrupted)
```

**Expected Result**: Chat and look commands do NOT interrupt rest countdown

## Expected Results

### Success Criteria Checklist

[ ] **Step 1**: Both players connected and in same room

- [ ] **Step 2**: `/rest` command blocked during combat
- [ ] **Step 3**: `/rest` command starts 10-second countdown, player position changes to sitting
- [ ] **Step 4**: Movement interrupts rest countdown
- [ ] **Step 5**: Spellcasting interrupts rest countdown
- [ ] **Step 6**: Being attacked interrupts rest countdown
- [ ] **Step 7**: Rest countdown completes and player disconnects after 10 seconds
- [ ] **Step 8**: Instant disconnect in rest locations (when available)
- [ ] **Step 9**: Chat, look, and inventory commands do NOT interrupt rest

### Key Behaviors Verified

1. **Combat Blocking**: `/rest` is blocked entirely during combat
2. **Countdown**: 10-second countdown starts when not in combat
3. **Position Change**: Player position changes to sitting when rest starts
4. **Interruption**: Movement, spellcasting, and being attacked interrupt rest
5. **Non-Interruption**: Chat, look, and inventory commands do NOT interrupt rest
6. **Completion**: Player disconnects after countdown completes (no grace period)
7. **Rest Locations**: Instant disconnect in rest locations when not in combat

## Notes

**Combat Restriction**: `/rest` cannot be used to escape combat

**Interrupt Conditions**: Movement, spellcasting, and being attacked interrupt rest

**Non-Interrupt Actions**: Chat, look, inventory management do NOT interrupt

**Intentional Disconnect**: `/rest` is an intentional disconnect (no grace period)

**Rest Locations**: Inns/hotels/motels provide instant disconnect when not in combat

## Cleanup

After scenario completion:

1. Close all browser tabs
2. Verify server is still running
3. Check for any remaining rest countdown tasks (should be none)
4. Reset player positions if needed for next scenario
