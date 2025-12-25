# Scenario 27: Character Selection at Login **[REQUIRES MULTI-PLAYER]**

## Overview

Tests the character selection flow when a user has multiple characters. Verifies that users with multiple characters see the selection screen, can select a character, and that the selected character is used for game connection.

**MULTI-CHARACTER**: This scenario tests the new multi-character support system.

## Prerequisites

**BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY:**

1. **Database State**: Test user has at least 2 active characters
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **No Previous Sessions**: Browser is clean with no existing game sessions

**⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE**

## Test Configuration

- **Test Player**: ArkanWolfshade (with multiple characters)
- **Starting Room**: Main Foyer (`earth_arkhamcity_sanitarium_room_foyer_001`)
- **Testing Approach**: Playwright MCP (multi-tab interaction required)
- **Timeout Settings**: Use configurable timeouts from master rules

## Execution Steps

### Step 1: Open Browser and Navigate to Client

**Purpose**: Initialize browser session and navigate to the game client

**Commands**:

```javascript
// Open browser and navigate to client
await mcp_playwright_browser_navigate({url: "http://localhost:5173"});

// Wait for page to fully load
await mcp_playwright_browser_wait_for({time: 10});
```

**Expected Result**: Browser opens and navigates to client login page

### Step 2: Login with Multiple Characters

**Purpose**: Login as user with multiple characters and verify character selection screen appears

**Commands**:

```javascript
// Wait for login form
await mcp_playwright_browser_wait_for({text: "Username", time: 30});

// Fill login form (confirm refs via browser_snapshot)
await mcp_playwright_browser_type({element: "Username input field", ref: "e9", text: "ArkanWolfshade"});
await mcp_playwright_browser_type({element: "Password input field", ref: "e10", text: "Cthulhu1"});
await mcp_playwright_browser_click({element: "Login button", ref: "e11"});

// Wait for login processing
await mcp_playwright_browser_wait_for({time: 15});

// Verify character selection screen appears
await mcp_playwright_browser_wait_for({text: "Select Your Character", time: 30});
```

**Expected Result**: Character selection screen appears showing list of characters

### Step 3: Verify Character List Display

**Purpose**: Verify that all active characters are displayed correctly

**Commands**:

```javascript
// Take snapshot to verify character list
const snapshot = await mcp_playwright_browser_snapshot();

// Verify character names are visible
// Verify "Select Character" buttons are present
// Verify "Create New Character" button is visible (if < 3 characters)
```

**Expected Result**: Character list shows all active characters with correct information (name, profession, level)

### Step 4: Select a Character

**Purpose**: Select a character and verify game connection

**Commands**:

```javascript
// Click "Select Character" button for first character (confirm ref via snapshot)
await mcp_playwright_browser_click({element: "Select Character button", ref: "eXX"});

// Wait for character selection processing
await mcp_playwright_browser_wait_for({time: 5});

// Wait for MOTD screen
await mcp_playwright_browser_wait_for({text: "Continue", time: 30});
await mcp_playwright_browser_click({element: "Continue button", ref: "e59"});

// Wait for game interface
await mcp_playwright_browser_wait_for({text: "Chat", time: 30});
```

**Expected Result**: Selected character is used for game connection, MOTD appears, then game interface loads

### Step 5: Verify Character Name in Game

**Purpose**: Verify that the correct character name is displayed in the game

**Commands**:

```javascript
// Check game interface for character name
// Verify character name matches selected character
const snapshot = await mcp_playwright_browser_snapshot();
// Character name should be visible in game interface
```

**Expected Result**: Game interface shows the selected character's name

## Expected Results Summary

1. ✅ Character selection screen appears after login for users with multiple characters
2. ✅ All active characters are displayed in the list
3. ✅ Character selection works correctly
4. ✅ Selected character is used for game connection
5. ✅ Character name is correctly displayed in game interface

## Failure Modes

- **Character selection screen doesn't appear**: User may not have multiple characters, or login failed
- **Character list is empty**: User has no active characters (should show creation flow instead)
- **Character selection fails**: API endpoint may be failing, check server logs
- **Wrong character selected**: Character selection logic may have issues

## Notes

- This scenario requires a user with at least 2 active characters
- Character names are case-insensitive unique
- Soft-deleted characters are not shown in the selection list
- Maximum 3 active characters per user
