# Scenario 34: Two Players Same Room Visibility **[REQUIRES MULTI-PLAYER]**

## Overview

Tests that when two players are in the same room, they can see each other in the room occupants list and receive
 visibility updates. This scenario verifies core multiplayer room visibility functionality.

**This is a core multi-player scenario** that requires two players to be in the same room simultaneously.

## Prerequisites

### BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY

1. **Database State**: Both players are in `earth_arkhamcity_sanitarium_room_foyer_001`
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **Both Players Connected**: AW and Ithaqua are both logged in and in the same room

### ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE

**Reference**: See @MULTIPLAYER_TEST_RULES.md for complete prerequisite verification procedures.

## Test Configuration

**Test Players**: ArkanWolfshade (AW) and Ithaqua

**Starting Room**: Main Foyer (`earth_arkhamcity_sanitarium_room_foyer_001`)

**Testing Approach**: Playwright MCP (multi-tab interaction required)

**Timeout Settings**: Use configurable timeouts from master rules

## Execution Steps

### Step 1: Verify Both Players in Same Room

**Purpose**: Ensure both players are in the same room and can see each other

**Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Verify AW can see Ithaqua in occupants
const awOccupants = await mcp_playwright_browser_evaluate({
  function: "() => {
    const occupantElements = document.querySelectorAll('[data-testid=\"occupant\"], .occupant, [class*=\"occupant\"]');
    return Array.from(occupantElements).map(el => el.textContent.trim());
  }"
});

console.log('AW sees occupants:', awOccupants);
const awSeesIthaqua = awOccupants.some(occ => occ.includes('Ithaqua'));
console.log('AW sees Ithaqua:', awSeesIthaqua);

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Verify Ithaqua can see AW in occupants
const ithaquaOccupants = await mcp_playwright_browser_evaluate({
  function: "() => {
    const occupantElements = document.querySelectorAll('[data-testid=\"occupant\"], .occupant, [class*=\"occupant\"]');
    return Array.from(occupantElements).map(el => el.textContent.trim());
  }"
});

console.log('Ithaqua sees occupants:', ithaquaOccupants);
const ithaquaSeesAW = ithaquaOccupants.some(occ => occ.includes('ArkanWolfshade'));
console.log('Ithaqua sees AW:', ithaquaSeesAW);
```

**Expected Result**: Both players can see each other in the room occupants list

### Step 2: Verify Room Description Shows Both Players

**Purpose**: Test that room descriptions/occupant counts are accurate

**Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Execute 'look' command to see room description
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "look"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for room description
await mcp_playwright_browser_wait_for({text: "Main Foyer", time: 10});

// Check if room description mentions Ithaqua
const awRoomText = await mcp_playwright_browser_evaluate({
  function: "() => document.body.innerText"
});
const awRoomShowsIthaqua = awRoomText.includes('Ithaqua') || awRoomText.includes('ithaqua');
console.log('AW room description shows Ithaqua:', awRoomShowsIthaqua);
```

**Expected Result**: Room description or occupant list shows both players

### Step 3: Verify Real-time Occupant Updates

**Purpose**: Test that occupant lists update in real-time when players join/leave

**Commands**:

```javascript
// Both players should already be visible from Step 1
// This step verifies the visibility is maintained

// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait a moment for any updates
await mcp_playwright_browser_wait_for({time: 2});

// Re-check occupants
const awOccupantsFinal = await mcp_playwright_browser_evaluate({
  function: "() => {
    const occupantElements = document.querySelectorAll('[data-testid=\"occupant\"], .occupant, [class*=\"occupant\"]');
    return Array.from(occupantElements).map(el => el.textContent.trim());
  }"
});

console.log('AW final occupants:', awOccupantsFinal);
const awStillSeesIthaqua = awOccupantsFinal.some(occ => occ.includes('Ithaqua'));
console.log('AW still sees Ithaqua:', awStillSeesIthaqua);
```

**Expected Result**: Occupant visibility is maintained and updates correctly

## Expected Results

✅ Both players can see each other in room occupants

✅ Room descriptions accurately reflect player presence

✅ Occupant lists update in real-time

## Success Criteria Checklist

[ ] AW can see Ithaqua in occupants

[ ] Ithaqua can see AW in occupants

[ ] Room descriptions show both players

[ ] Occupant visibility is maintained over time

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
**Scenario ID**: 34
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: 3-5 minutes
