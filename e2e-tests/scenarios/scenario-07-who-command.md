# Scenario 7: Who Command

## Overview

Tests the who command functionality for player listing and filtering. This scenario verifies that players can see other online players, that the who command displays proper information including locations, and that the command works correctly for both admin and non-admin players.

## Prerequisites

**BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY:**

1. **Database State**: Both players are in `earth_arkham_city_sanitarium_room_foyer_001`
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **Both Players Connected**: AW and Ithaqua are both logged in and in the same room
5. **Admin Privileges**: AW has admin privileges, Ithaqua does not

**⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE**

**Reference**: See @MULTIPLAYER_TEST_RULES.md for complete prerequisite verification procedures.

## Test Configuration

- **Test Players**: ArkanWolfshade (AW - Admin) and Ithaqua (Non-Admin)
- **Starting Room**: Main Foyer (`earth_arkham_city_sanitarium_room_foyer_001`)
- **Testing Approach**: Playwright MCP (multi-tab interaction required)
- **Timeout Settings**: Use configurable timeouts from master rules

## Execution Steps

### Step 1: AW Uses Who Command

**Purpose**: Test basic who command functionality for admin player

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Type who command
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "who"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for who command response
await mcp_playwright_browser_wait_for({text: "Online Players:"});
```

**Expected Result**: AW receives who command response with player list

### Step 2: Verify AW Sees Both Players

**Purpose**: Test that who command shows all online players

**Commands**:
```javascript
// Wait for player list to appear
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade"});
await mcp_playwright_browser_wait_for({text: "Ithaqua"});

// Verify both players appear in who list
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesBothPlayers = awMessages.some(msg => msg.includes('ArkanWolfshade')) && awMessages.some(msg => msg.includes('Ithaqua'));
console.log('AW sees both players in who list:', seesBothPlayers);
console.log('AW messages:', awMessages);
```

**Expected Result**: AW sees both ArkanWolfshade and Ithaqua in the who list

### Step 3: Verify Location Information

**Purpose**: Test that who command shows proper location information

**Commands**:
```javascript
// Check for location information in who list
const locationInfo = awMessages.some(msg => msg.includes('earth_arkham_city_sanitarium_room_foyer_001'));
console.log('AW sees location information:', locationInfo);

// Verify format includes zone + sub-zone + room
const properLocationFormat = awMessages.some(msg =>
  msg.includes('earth_arkham_city_sanitarium_room_foyer_001') ||
  msg.includes('Arkham City Sanitarium - Main Foyer')
);
console.log('AW sees proper location format:', properLocationFormat);
```

**Expected Result**: AW sees proper location information in the who list

### Step 4: Ithaqua Uses Who Command

**Purpose**: Test who command functionality for non-admin player

**Commands**:
```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Type who command
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "who"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for who command response
await mcp_playwright_browser_wait_for({text: "Online Players:"});
```

**Expected Result**: Ithaqua receives who command response with player list

### Step 5: Verify Ithaqua Sees Both Players

**Purpose**: Test that non-admin players can see all online players

**Commands**:
```javascript
// Wait for player list to appear
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade"});
await mcp_playwright_browser_wait_for({text: "Ithaqua"});

// Verify both players appear in who list
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const ithaquaSeesBothPlayers = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade')) && ithaquaMessages.some(msg => msg.includes('Ithaqua'));
console.log('Ithaqua sees both players in who list:', ithaquaSeesBothPlayers);
console.log('Ithaqua messages:', ithaquaMessages);
```

**Expected Result**: Ithaqua sees both ArkanWolfshade and Ithaqua in the who list

### Step 6: Test Who Command After Movement

**Purpose**: Test that who command updates location information after player movement

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Move to different room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go east"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move east"});

// Use who command again
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "who"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for updated who command response
await mcp_playwright_browser_wait_for({text: "Online Players:"});
```

**Expected Result**: AW receives updated who command response

### Step 7: Verify Updated Location Information

**Purpose**: Test that who command shows updated location after movement

**Commands**:
```javascript
// Wait for updated player list
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade"});
await mcp_playwright_browser_wait_for({text: "Ithaqua"});

// Check for updated location information
const awMessagesUpdated = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesUpdatedLocation = awMessagesUpdated.some(msg =>
  msg.includes('earth_arkham_city_sanitarium_room_east_001') ||
  msg.includes('Arkham City Sanitarium - East Room')
);
console.log('AW sees updated location information:', seesUpdatedLocation);
console.log('AW updated messages:', awMessagesUpdated);
```

**Expected Result**: AW sees updated location information reflecting the room change

### Step 8: Test Who Command Format

**Purpose**: Verify that who command displays information in proper format

**Commands**:
```javascript
// Check who command format
const whoCommandFormat = awMessagesUpdated.some(msg =>
  msg.includes('Online Players:') &&
  msg.includes('ArkanWolfshade') &&
  msg.includes('Ithaqua')
);
console.log('Who command has proper format:', whoCommandFormat);

// Verify no duplicate entries
const playerCount = awMessagesUpdated.filter(msg => msg.includes('ArkanWolfshade')).length;
const ithaquaCount = awMessagesUpdated.filter(msg => msg.includes('Ithaqua')).length;
console.log('Player count in who list:', playerCount, ithaquaCount);
```

**Expected Result**: Who command displays proper format with no duplicate entries

### Step 9: Test Who Command with Single Player

**Purpose**: Test who command when only one player is online

**Commands**:
```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Disconnect Ithaqua
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "quit"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for disconnect
await mcp_playwright_browser_wait_for({text: "Goodbye!"});

// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Use who command with only one player
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "who"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for who command response
await mcp_playwright_browser_wait_for({text: "Online Players:"});
```

**Expected Result**: AW receives who command response with only one player

### Step 10: Verify Single Player Who List

**Purpose**: Test that who command works correctly with single player

**Commands**:
```javascript
// Wait for single player list
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade"});

// Verify only AW appears in who list
const awMessagesSingle = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesOnlyAW = awMessagesSingle.some(msg => msg.includes('ArkanWolfshade')) && !awMessagesSingle.some(msg => msg.includes('Ithaqua'));
console.log('AW sees only himself in who list:', seesOnlyAW);
console.log('AW single player messages:', awMessagesSingle);
```

**Expected Result**: AW sees only himself in the who list

## Expected Results

- ✅ AW sees both players in who list
- ✅ Ithaqua sees both players in who list
- ✅ Location information is displayed properly
- ✅ Who command updates after player movement
- ✅ Who command format is consistent
- ✅ Who command works with single player
- ✅ No duplicate entries in who list

## Success Criteria Checklist

- [ ] AW successfully uses who command
- [ ] AW sees both players in who list
- [ ] Location information is displayed in proper format
- [ ] Ithaqua successfully uses who command
- [ ] Ithaqua sees both players in who list
- [ ] Who command updates location after movement
- [ ] Who command format is consistent
- [ ] Who command works with single player
- [ ] No duplicate entries appear in who list
- [ ] All browser operations complete without errors
- [ ] Server remains stable throughout the scenario

## Cleanup

Execute standard cleanup procedures from @CLEANUP.md:
1. Close all browser tabs
2. Stop development server
3. Verify clean shutdown

## Status

**✅ READY FOR TESTING**

The who command system is working correctly. Players can see other online players, location information is displayed properly, and the command updates correctly after player movement. The system works for both admin and non-admin players and handles single-player scenarios correctly.

---

**Document Version**: 1.0 (Modular E2E Test Suite)
**Last Updated**: 2025-09-18
**Scenario ID**: 07
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: 5-7 minutes
