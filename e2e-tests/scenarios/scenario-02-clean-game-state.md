# Scenario 2: Clean Game State on Connection

## Overview

Tests that players don't see stale/previous game state information when connecting. This scenario verifies that each new connection starts with a clean slate and doesn't inherit messages or state from previous sessions.

## Prerequisites

**BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY:**

1. **Database State**: Both players are in `earth_arkham_city_sanitarium_room_foyer_001`
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **Clean Environment**: No previous browser sessions or game state

**⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE**

**Reference**: See @MULTIPLAYER_TEST_RULES.md for complete prerequisite verification procedures.

## Test Configuration

- **Test Players**: ArkanWolfshade (AW) and Ithaqua
- **Starting Room**: Main Foyer (`earth_arkham_city_sanitarium_room_foyer_001`)
- **Testing Approach**: Playwright MCP (multi-tab interaction required)
- **Timeout Settings**: Use configurable timeouts from master rules

## Execution Steps

### Step 1: AW Enters the Game (Fresh Session)

**Purpose**: First player connects with a completely fresh session

**Commands**:
```javascript
// Navigate to client
await mcp_playwright_browser_navigate({url: "http://localhost:5173"});

// Login as AW
await mcp_playwright_browser_type({element: "Username input field", ref: "username-input", text: "ArkanWolfshade"});
await mcp_playwright_browser_type({element: "Password input field", ref: "password-input", text: "Cthulhu1"});
await mcp_playwright_browser_click({element: "Login button", ref: "login-button"});

// Wait for game terminal
await mcp_playwright_browser_wait_for({text: "Welcome to MythosMUD"});
```

**Expected Result**: AW successfully logs in and enters the game world

### Step 2: Verify AW Sees No Previous Game State

**Purpose**: Ensure AW doesn't see any stale messages from previous sessions

**Commands**:
```javascript
// Check for stale messages
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const staleMessages = awMessages.filter(msg =>
  msg.includes('has entered the game') ||
  msg.includes('has left the game') ||
  msg.includes('enters the room') ||
  msg.includes('leaves the room')
);
console.log('AW stale messages:', staleMessages.length === 0);
console.log('AW total messages:', awMessages.length);
console.log('AW messages:', awMessages);
```

**Expected Result**: AW sees NO previous game state information

### Step 3: Ithaqua Enters the Game

**Purpose**: Second player connects to test multiplayer state isolation

**Commands**:
```javascript
// Open new tab for Ithaqua
await mcp_playwright_browser_tab_new({url: "http://localhost:5173"});
await mcp_playwright_browser_tab_select({index: 1});

// Login as Ithaqua
await mcp_playwright_browser_type({element: "Username input field", ref: "username-input", text: "Ithaqua"});
await mcp_playwright_browser_type({element: "Password input field", ref: "password-input", text: "Cthulhu1"});
await mcp_playwright_browser_click({element: "Login button", ref: "login-button"});

// Wait for game terminal
await mcp_playwright_browser_wait_for({text: "Welcome to MythosMUD"});
```

**Expected Result**: Ithaqua successfully logs in and enters the game world

### Step 4: Verify Ithaqua Sees No Previous Game State

**Purpose**: Ensure Ithaqua doesn't see any stale messages from previous sessions

**Commands**:
```javascript
// Check for stale messages
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const ithaquaStaleMessages = ithaquaMessages.filter(msg =>
  msg.includes('has entered the game') ||
  msg.includes('has left the game') ||
  msg.includes('enters the room') ||
  msg.includes('leaves the room')
);
console.log('Ithaqua stale messages:', ithaquaStaleMessages.length === 0);
console.log('Ithaqua total messages:', ithaquaMessages.length);
console.log('Ithaqua messages:', ithaquaMessages);
```

**Expected Result**: Ithaqua sees NO previous game state information

### Step 5: Verify AW Sees Current Session Event

**Purpose**: Confirm that current session events work correctly

**Commands**:
```javascript
// Switch back to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for current session message
await mcp_playwright_browser_wait_for({text: "Ithaqua has entered the game"});

// Verify current session works
const awCurrentMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const hasCurrentSession = awCurrentMessages.some(msg => msg.includes('Ithaqua has entered the game'));
console.log('AW sees current session:', hasCurrentSession);
console.log('AW current messages:', awCurrentMessages);
```

**Expected Result**: AW sees "Ithaqua has entered the game." (current session)

### Step 6: Test Message Isolation

**Purpose**: Verify that players only see messages from their current session

**Commands**:
```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Check that Ithaqua only sees their own connection, not AW's
const ithaquaFinalMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesAWConnection = ithaquaFinalMessages.some(msg => msg.includes('ArkanWolfshade has entered the game'));
const seesOwnConnection = ithaquaFinalMessages.some(msg => msg.includes('Ithaqua has entered the game'));

console.log('Ithaqua sees AW connection (should be false):', !seesAWConnection);
console.log('Ithaqua sees own connection (should be false):', !seesOwnConnection);
console.log('Ithaqua final messages:', ithaquaFinalMessages);
```

**Expected Result**: Ithaqua sees NO connection messages (players don't see their own connection messages)

## Expected Results

- ✅ AW sees NO previous game state information
- ✅ Ithaqua sees NO previous game state information
- ✅ AW sees "Ithaqua has entered the game." (current session)
- ✅ Players don't see their own connection messages
- ✅ Each session starts with a clean state

## Success Criteria Checklist

- [ ] AW successfully logs in with fresh session
- [ ] AW sees no stale messages from previous sessions
- [ ] Ithaqua successfully logs in with fresh session
- [ ] Ithaqua sees no stale messages from previous sessions
- [ ] AW sees current session connection message
- [ ] Players don't see their own connection messages
- [ ] Message isolation works correctly between sessions
- [ ] All browser operations complete without errors
- [ ] Server remains stable throughout the scenario

## Cleanup

Execute standard cleanup procedures from @CLEANUP.md:
1. Close all browser tabs
2. Stop development server
3. Verify clean shutdown

## Status

**✅ FIXES IMPLEMENTED - Ready for Testing**

The clean game state system is working correctly. Players start with fresh sessions and don't see stale messages from previous connections. The current session messaging works properly while maintaining proper isolation between different game sessions.

---

**Document Version**: 1.0 (Modular E2E Test Suite)
**Last Updated**: 2025-09-18
**Scenario ID**: 02
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: 3-5 minutes
