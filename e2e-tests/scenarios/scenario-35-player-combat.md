# Scenario 35: Player Combat **[REQUIRES MULTI-PLAYER]**

## Overview

Tests combat functionality between two players. This scenario verifies that players can engage in combat, that
 combat messages are properly broadcast, and that combat state is correctly managed in multiplayer scenarios.

**This is a core multi-player scenario** that requires two players to interact in combat.

## Prerequisites

### BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY

1. **Database State**: Both players are in `earth_arkhamcity_sanitarium_room_foyer_001`
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **Both Players Connected**: AW and Ithaqua are both logged in and in the same room
5. **Combat Enabled**: Combat system is enabled and functional

### ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE

**Reference**: See @MULTIPLAYER_TEST_RULES.md for complete prerequisite verification procedures.

## Test Configuration

**Test Players**: ArkanWolfshade (AW) and Ithaqua

**Starting Room**: Main Foyer (`earth_arkhamcity_sanitarium_room_foyer_001`)

**Testing Approach**: Playwright MCP (multi-tab interaction required)

**Timeout Settings**: Use configurable timeouts from master rules

## Execution Steps

### Step 1: Verify Both Players Ready for Combat

**Purpose**: Ensure both players are in the same room and ready for combat testing

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
console.log('AW sees Ithaqua:', awSeesIthaqua);

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
console.log('Ithaqua sees AW:', ithaquaSeesAW);
```

**Expected Result**: Both players can see each other

### Step 2: AW Initiates Combat

**Purpose**: Test combat initiation between players

**Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// AW attacks Ithaqua
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "attack Ithaqua"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for combat initiation message
await mcp_playwright_browser_wait_for({text: "attack", time: 10});
```

**Expected Result**: AW sees combat initiation message

### Step 3: Verify Ithaqua Receives Combat Message

**Purpose**: Test that combat messages are broadcast to the target player

**Commands**:

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for combat message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade", time: 10});

// Check for combat-related messages
const ithaquaMessages = await mcp_playwright_browser_evaluate({
  function: "() => Array.from(document.querySelectorAll('.message, [class*=\"message\"]')).map(el => el.textContent.trim())"
});

const seesCombatMessage = ithaquaMessages.some(msg =>
  msg.includes('ArkanWolfshade') && (msg.includes('attack') || msg.includes('hit') || msg.includes('damage'))
);
console.log('Ithaqua sees combat message:', seesCombatMessage);
console.log('Ithaqua messages:', ithaquaMessages);
```

**Expected Result**: Ithaqua receives combat message from AW

### Step 4: Verify Combat State Updates

**Purpose**: Test that combat state (health, status) updates correctly for both players

**Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Check AW's health/stats display
const awStats = await mcp_playwright_browser_evaluate({
  function: "() => {
    const statsElements = document.querySelectorAll('[data-testid=\"stats\"], .stats, [class*=\"stats\"]');
    return Array.from(statsElements).map(el => el.textContent.trim());
  }"
});

console.log('AW stats:', awStats);

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Check Ithaqua's health/stats display
const ithaquaStats = await mcp_playwright_browser_evaluate({
  function: "() => {
    const statsElements = document.querySelectorAll('[data-testid=\"stats\"], .stats, [class*=\"stats\"]');
    return Array.from(statsElements).map(el => el.textContent.trim());
  }"
});

console.log('Ithaqua stats:', ithaquaStats);
```

**Expected Result**: Both players see updated combat state

## Expected Results

✅ Combat can be initiated between players

✅ Combat messages are broadcast to both players

✅ Combat state updates correctly for both players

✅ Combat system functions correctly in multiplayer scenarios

## Success Criteria Checklist

[ ] AW can initiate combat with Ithaqua

[ ] Ithaqua receives combat messages from AW

[ ] Combat state updates are visible to both players

[ ] Combat messages are properly formatted and delivered

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
**Scenario ID**: 35
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: 5-7 minutes
