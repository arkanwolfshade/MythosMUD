# Scenario 32: Disconnect Grace Period **[REQUIRES MULTI-PLAYER]**

## Overview

Tests the 30-second grace period system for unintentional disconnects. This scenario verifies that when a player loses
connection, their character remains in-game for 30 seconds in a "zombie" state where they can be attacked and will
auto-attack back, but cannot take other actions. Other players should see a "(linkdead)" indicator.

**⚠️ CRITICAL**: This scenario tests **unintentional disconnects only**. Intentional disconnects via `/rest` or `/quit`
should NOT have grace period.

## Prerequisites

### BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY

1. **Database State**: Both players are in `earth_arkhamcity_sanitarium_room_foyer_001`
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **Both Players Connected**: AW and Ithaqua are both logged in and in the same room
5. **No Active Grace Periods**: No players currently in grace period

### ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE

**Reference**: See @MULTIPLAYER_TEST_RULES.md for complete prerequisite verification procedures.

## Test Configuration

**Test Players**: ArkanWolfshade (AW) and Ithaqua

**Starting Room**: Main Foyer (`earth_arkhamcity_sanitarium_room_foyer_001`)

**Testing Approach**: Playwright MCP (multi-tab interaction required)

**Timeout Settings**: Use configurable timeouts from master rules

**Grace Period Duration**: 30 seconds

## Testing Approach Rationale

### Why Playwright MCP is Required

**Multi-tab Coordination**: Requires 2+ browser tabs to test disconnect behavior and visual indicators

**Real-time Interaction**: Must verify "(linkdead)" indicator appears to other players in real-time

**Connection Simulation**: Must simulate unintentional disconnect (WebSocket close)

**State Verification**: Must verify zombie state (can be attacked, auto-attacks, cannot move/command)

**Timer Verification**: Must verify 30-second grace period timer

### Standard Playwright Not Suitable

Cannot handle multiple browser tabs simultaneously

- Cannot simulate WebSocket disconnection properly
- Cannot verify real-time state changes across players

## Execution Steps

### Step 1: Both Players Connected

**Purpose**: Ensure both players are ready for disconnect testing

**Commands**:

```javascript
// Ensure both players are logged in from previous scenario
// AW should be on tab 0, Ithaqua on tab 1
// Both should be in the same room (foyer)

// Verify both players are in the same room
await mcp_playwright_browser_tabs({action: "list"});
// Should show 2 tabs: AW (tab 0) and Ithaqua (tab 1)

// Check room occupants from Ithaqua's perspective
await mcp_playwright_browser_tabs({action: "select", index: 1});
const roomOccupants = await mcp_playwright_browser_evaluate({
    function: "() => { const panel = document.querySelector('[data-testid=\"occupants-panel\"]'); return panel ?
    panel.textContent : ''; }"
});
console.log('Room occupants:', roomOccupants);
// Should include both AW and Ithaqua
```

**Expected Result**: Both players are connected and in the same room

### Step 2: Verify No Grace Period Initially

**Purpose**: Verify no players are in grace period at start

**Commands**:

```javascript
// From Ithaqua's tab, check room occupants
await mcp_playwright_browser_tabs({action: "select", index: 1});
const occupantsBefore = await mcp_playwright_browser_evaluate({
    function: "() => { const panel = document.querySelector('[data-testid=\"occupants-panel\"]'); return panel ? panel.textContent : ''; }"
});
console.log('Occupants before disconnect:', occupantsBefore);

// Verify no "(linkdead)" indicators
const hasLinkdead = occupantsBefore.includes('(linkdead)');
console.log('Has linkdead indicator:', hasLinkdead);
// Should be false
```

**Expected Result**: No "(linkdead)" indicators visible

### Step 3: Simulate Unintentional Disconnect for AW

**Purpose**: Simulate connection loss for AW (unintentional disconnect)

**Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tabs({action: "select", index: 0});

// Simulate WebSocket disconnection by closing the connection
// This simulates an unintentional disconnect (connection loss)
await mcp_playwright_browser_evaluate({
    function: "() => { if (window.gameConnection && window.gameConnection.ws) { window.gameConnection.ws.close(); } }"
});

// Wait a moment for disconnect to be detected
await mcp_playwright_browser_wait_for({time: 2});

// Note: AW's tab may show connection error - this is expected
```

**Expected Result**: AW's connection is closed, triggering disconnect detection

### Step 4: Verify Grace Period Started (Zombie State)

**Purpose**: Verify AW enters grace period and shows "(linkdead)" indicator

**Commands**:

```javascript
// Switch to Ithaqua's tab (still connected)
await mcp_playwright_browser_tabs({action: "select", index: 1});

// Wait for grace period to start (disconnect detection may take a moment)
await mcp_playwright_browser_wait_for({time: 3});

// Check room occupants - should show AW with "(linkdead)" indicator
const occupantsAfter = await mcp_playwright_browser_evaluate({
    function: "() => { const panel = document.querySelector('[data-testid=\"occupants-panel\"]'); return panel ? panel.textContent : ''; }"
});
console.log('Occupants after disconnect:', occupantsAfter);

// Verify "(linkdead)" indicator appears
const hasLinkdeadAfter = occupantsAfter.includes('(linkdead)');
console.log('Has linkdead indicator after disconnect:', hasLinkdeadAfter);
// Should be true

// Verify AW's name is still visible
const hasAW = occupantsAfter.includes('ArkanWolfshade') || occupantsAfter.includes('AW');
console.log('AW still visible:', hasAW);
// Should be true
```

**Expected Result**: AW shows "(linkdead)" indicator in room occupants list

### Step 5: Verify Zombie State - Cannot Move/Command

**Purpose**: Verify AW cannot move or use commands during grace period

**Commands**:

```javascript
// Try to reconnect AW (simulate reconnection attempt)
await mcp_playwright_browser_tabs({action: "select", index: 0});

// Check if AW can see connection error or reconnection prompt
const connectionState = await mcp_playwright_browser_evaluate({
    function: "() => { return document.body.textContent; }"
});
console.log('Connection state:', connectionState);

// Note: During grace period, AW should not be able to send commands
// This is verified server-side, but we can check if reconnection is possible
```

**Expected Result**: AW cannot send commands during grace period (server-side blocking)

### Step 6: Verify Zombie State - Can Be Attacked

**Purpose**: Verify AW can be attacked during grace period and will auto-attack back

**Commands**:

```javascript
// From Ithaqua's tab, attack AW
await mcp_playwright_browser_tabs({action: "select", index: 1});

// Send attack command on AW
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/attack ArkanWolfshade"
});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for combat to start
await mcp_playwright_browser_wait_for({time: 2});

// Check combat messages
const combatMessages = await mcp_playwright_browser_evaluate({
    function: "() => { const messages = Array.from(document.querySelectorAll('.message')).slice(-5); return messages.map(m => m.textContent.trim()); }"
});
console.log('Combat messages:', combatMessages);

// Verify AW auto-attacks back (should see attack messages)
const hasAutoAttack = combatMessages.some(msg =>
    msg.includes('ArkanWolfshade') || msg.includes('AW') || msg.includes('attacks')
);
console.log('AW auto-attacked:', hasAutoAttack);
// Should be true (AW should auto-attack when attacked)
```

**Expected Result**: AW can be attacked and auto-attacks back during grace period

### Step 7: Verify Visual Indicator in /look Command

**Purpose**: Verify "(linkdead)" appears in /look command output

**Commands**:

```javascript
// From Ithaqua's tab, look at AW
await mcp_playwright_browser_tabs({action: "select", index: 1});

// Send look command
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/look ArkanWolfshade"
});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for look response
await mcp_playwright_browser_wait_for({time: 1});

// Check look output
const lookOutput = await mcp_playwright_browser_evaluate({
    function: "() => { const messages = Array.from(document.querySelectorAll('.message')).slice(-3); return messages.map(m => m.textContent.trim()).join('\\n'); }"
});
console.log('Look output:', lookOutput);

// Verify "(linkdead)" appears in look output
const hasLinkdeadInLook = lookOutput.includes('(linkdead)');
console.log('(linkdead) in look output:', hasLinkdeadInLook);
// Should be true
```

**Expected Result**: "(linkdead)" indicator appears in `/look` command output

### Step 8: Verify Grace Period Expires (30 seconds)

**Purpose**: Verify AW is removed from game after 30 seconds

**Commands**:

```javascript
// Wait for grace period to expire (30 seconds)
// Note: This is a long wait, but necessary to verify timer
console.log('Waiting for grace period to expire (30 seconds)...');
await mcp_playwright_browser_wait_for({time: 32});

// Check room occupants - AW should be gone
const occupantsAfterExpiry = await mcp_playwright_browser_evaluate({
    function: "() => { const panel = document.querySelector('[data-testid=\"occupants-panel\"]'); return panel ? panel.textContent : ''; }"
});
console.log('Occupants after grace period expiry:', occupantsAfterExpiry);

// Verify AW is no longer visible
const hasAWAfter = occupantsAfterExpiry.includes('ArkanWolfshade') || occupantsAfterExpiry.includes('AW');
console.log('AW still visible after expiry:', hasAWAfter);
// Should be false

// Verify no "(linkdead)" indicators
const hasLinkdeadAfterExpiry = occupantsAfterExpiry.includes('(linkdead)');
console.log('Has linkdead after expiry:', hasLinkdeadAfterExpiry);
// Should be false
```

**Expected Result**: AW is removed from game after 30 seconds, no "(linkdead)" indicator

### Step 9: Verify Intentional Disconnect Has No Grace Period

**Purpose**: Verify `/rest` command does NOT trigger grace period

**Commands**:

```javascript
// Reconnect AW for this test
// (This step may require manual reconnection or using a new tab)

// From AW's tab, use /rest command (intentional disconnect)
await mcp_playwright_browser_tabs({action: "select", index: 0});

// Send /rest command
await mcp_playwright_browser_type({
    element: "Command input",
    ref: "command-input",
    text: "/rest"
});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for disconnect
await mcp_playwright_browser_wait_for({time: 2});

// From Ithaqua's tab, check room occupants immediately
await mcp_playwright_browser_tabs({action: "select", index: 1});
const occupantsAfterRest = await mcp_playwright_browser_evaluate({
    function: "() => { const panel = document.querySelector('[data-testid=\"occupants-panel\"]'); return panel ? panel.textContent : ''; }"
});
console.log('Occupants after /rest:', occupantsAfterRest);

// Verify AW is immediately gone (no grace period for intentional disconnect)
const hasAWAfterRest = occupantsAfterRest.includes('ArkanWolfshade') || occupantsAfterRest.includes('AW');
console.log('AW visible after /rest:', hasAWAfterRest);
// Should be false (immediate removal, no grace period)
```

**Expected Result**: AW is immediately removed (no grace period for intentional disconnect)

## Expected Results

### Success Criteria Checklist

[ ] **Step 1**: Both players connected and in same room

- [ ] **Step 2**: No "(linkdead)" indicators initially
- [ ] **Step 3**: Unintentional disconnect detected
- [ ] **Step 4**: AW shows "(linkdead)" indicator in room occupants
- [ ] **Step 5**: AW cannot move or use commands (zombie state)
- [ ] **Step 6**: AW can be attacked and auto-attacks back
- [ ] **Step 7**: "(linkdead)" appears in `/look` command output
- [ ] **Step 8**: AW removed after 30 seconds (grace period expires)
- [ ] **Step 9**: Intentional disconnect via `/rest` has no grace period (immediate removal)

### Key Behaviors Verified

1. **Grace Period Duration**: 30 seconds for unintentional disconnects
2. **Visual Indicator**: "(linkdead)" appears in room lists and `/look` output
3. **Zombie State**: Cannot move/command, but can be attacked and auto-attacks
4. **Intentional Disconnect**: No grace period for `/rest` or `/quit` commands
5. **Timer Expiration**: Player removed after 30 seconds

## Notes

**Grace Period Only for Unintentional**: Only connection loss triggers grace period, not `/rest` or `/quit`

**Auto-Attack**: Grace period players use normal auto-attack (with weapons, no special abilities)

**Visual Feedback**: Other players see "(linkdead)" to understand why character isn't responding

**Reconnection**: If player reconnects during grace period, it cancels immediately

## Cleanup

After scenario completion:

1. Close all browser tabs
2. Verify server is still running
3. Check for any remaining grace period tasks (should be none)
4. Reset player positions if needed for next scenario
