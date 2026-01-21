# Scenario 36: Movement Visibility to Other Players **[REQUIRES MULTI-PLAYER]**

## Overview

Tests that when one player moves to a different room, other players in the original room and destination room
 receive proper visibility updates. This scenario verifies movement broadcasting and occupant list updates in
  multiplayer scenarios.

**This is a core multi-player scenario** that requires two players to observe each other's movements.

## Prerequisites

### BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY

1. **Database State**: Both players are in `earth_arkhamcity_sanitarium_room_foyer_001`
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **Both Players Connected**: AW and Ithaqua are both logged in and in the same room
5. **Room Connections**: Verify there is an adjacent room AW can move to

### ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE

**Reference**: See @MULTIPLAYER_TEST_RULES.md for complete prerequisite verification procedures.

## Test Configuration

**Test Players**: ArkanWolfshade (AW) and Ithaqua

**Starting Room**: Main Foyer (`earth_arkhamcity_sanitarium_room_foyer_001`)

**Testing Approach**: Playwright MCP (multi-tab interaction required)

**Timeout Settings**: Use configurable timeouts from master rules

## Execution Steps

### Step 1: Verify Both Players in Starting Room

**Purpose**: Ensure both players start in the same room

**Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Verify AW can see Ithaqua
const awOccupants = await mcp_playwright_browser_evaluate({
  function: "() => {
    const occupantElements = document.querySelectorAll('[data-testid=\"occupant\"], .occupant, [class*=\"occupant\"]');
    return Array.from(occupantElements).map(el => el.textContent.trim());
  }"
});

const awSeesIthaqua = awOccupants.some(occ => occ.includes('Ithaqua'));
console.log('AW sees Ithaqua in starting room:', awSeesIthaqua);

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Verify Ithaqua can see AW
const ithaquaOccupants = await mcp_playwright_browser_evaluate({
  function: "() => {
    const occupantElements = document.querySelectorAll('[data-testid=\"occupant\"], .occupant, [class*=\"occupant\"]');
    return Array.from(occupantElements).map(el => el.textContent.trim());
  }"
});

const ithaquaSeesAW = ithaquaOccupants.some(occ => occ.includes('ArkanWolfshade'));
console.log('Ithaqua sees AW in starting room:', ithaquaSeesAW);
```

**Expected Result**: Both players can see each other in the starting room

### Step 2: AW Moves to Different Room

**Purpose**: Test that AW's movement is visible to Ithaqua

**Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// AW moves to an adjacent room (adjust direction as needed based on room layout)
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "east"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move", time: 10});
```

**Expected Result**: AW successfully moves to a different room

### Step 3: Verify Ithaqua Sees AW Leave

**Purpose**: Test that Ithaqua receives notification when AW leaves the room

**Commands**:

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for movement message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade", time: 10});

// Check for movement-related messages
const ithaquaMessages = await mcp_playwright_browser_evaluate({
  function: "() => Array.from(document.querySelectorAll('.message, [class*=\"message\"]')).map(el => el.textContent.trim())"
});

const seesAWLeave = ithaquaMessages.some(msg =>
  msg.includes('ArkanWolfshade') && (msg.includes('leave') || msg.includes('depart') || msg.includes('goes'))
);
console.log('Ithaqua sees AW leave:', seesAWLeave);

// Verify Ithaqua no longer sees AW in occupants
const ithaquaOccupantsAfter = await mcp_playwright_browser_evaluate({
  function: "() => {
    const occupantElements = document.querySelectorAll('[data-testid=\"occupant\"], .occupant, [class*=\"occupant\"]');
    return Array.from(occupantElements).map(el => el.textContent.trim());
  }"
});

const stillSeesAW = ithaquaOccupantsAfter.some(occ => occ.includes('ArkanWolfshade'));
console.log('Ithaqua still sees AW (should be false):', stillSeesAW);
```

**Expected Result**: Ithaqua sees AW leave and AW is removed from occupants list

### Step 4: Verify AW in New Room

**Purpose**: Test that AW's new location is correctly updated

**Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Verify AW is in new room
const awRoomInfo = await mcp_playwright_browser_evaluate({
  function: "() => {
    const roomElements = document.querySelectorAll('[data-testid=\"room\"], .room, [class*=\"room\"]');
    return Array.from(roomElements).map(el => el.textContent.trim());
  }"
});

console.log('AW room info:', awRoomInfo);

// Verify AW no longer sees Ithaqua (they're in different rooms)
const awOccupantsAfter = await mcp_playwright_browser_evaluate({
  function: "() => {
    const occupantElements = document.querySelectorAll('[data-testid=\"occupant\"], .occupant, [class*=\"occupant\"]');
    return Array.from(occupantElements).map(el => el.textContent.trim());
  }"
});

const awStillSeesIthaqua = awOccupantsAfter.some(occ => occ.includes('Ithaqua'));
console.log('AW still sees Ithaqua (should be false):', awStillSeesIthaqua);
```

**Expected Result**: AW is in new room and no longer sees Ithaqua

### Step 5: AW Returns to Original Room

**Purpose**: Test that movement back to original room is visible

**Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// AW moves back to original room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "west"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move", time: 10});
```

**Expected Result**: AW successfully returns to original room

### Step 6: Verify Ithaqua Sees AW Return

**Purpose**: Test that Ithaqua receives notification when AW returns

**Commands**:

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for movement message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade", time: 10});

// Verify Ithaqua sees AW in occupants again
const ithaquaOccupantsFinal = await mcp_playwright_browser_evaluate({
  function: "() => {
    const occupantElements = document.querySelectorAll('[data-testid=\"occupant\"], .occupant, [class*=\"occupant\"]');
    return Array.from(occupantElements).map(el => el.textContent.trim());
  }"
});

const seesAWReturn = ithaquaOccupantsFinal.some(occ => occ.includes('ArkanWolfshade'));
console.log('Ithaqua sees AW return:', seesAWReturn);
```

**Expected Result**: Ithaqua sees AW return and AW appears in occupants list again

## Expected Results

✅ Players can see each other's movements in real-time

✅ Movement messages are broadcast to other players in the room

✅ Occupant lists update correctly when players move

✅ Players in destination rooms see new arrivals

✅ Players in origin rooms see departures

## Success Criteria Checklist

[ ] Ithaqua sees AW leave the room

[ ] Ithaqua's occupant list updates when AW leaves

[ ] AW's location updates correctly

[ ] Ithaqua sees AW return to the room

[ ] Ithaqua's occupant list updates when AW returns

[ ] Movement messages are properly formatted and delivered

[ ] All browser operations complete without errors

[ ] Server remains stable throughout the scenario

## Cleanup

Execute standard cleanup procedures from @CLEANUP.md:

1. Close all browser tabs
2. Stop development server
3. Verify clean shutdown

## Status

**Document Version**: 1.0
**Last Updated**: 2025-01-XX
**Scenario ID**: 36
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: 5-7 minutes
