# Scenario 29: Character Deletion **[REQUIRES MULTI-PLAYER]**

## Overview

Tests soft deletion of characters, including deletion confirmation, list updates, and name reuse after deletion.

**MULTI-CHARACTER**: This scenario tests the soft deletion functionality.

## Prerequisites

### BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY

1. **Database State**: Test user has at least 2 active characters
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **No Previous Sessions**: Browser is clean with no existing game sessions

### ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE

## Test Configuration

**Test Player**: ArkanWolfshade (with multiple characters)

**Testing Approach**: Playwright MCP

**Timeout Settings**: Use configurable timeouts from master rules

## Execution Steps

### Step 1: Login and View Character Selection

**Purpose**: Login and view character list

**Commands**:

```javascript
// Navigate and login
await mcp_playwright_browser_navigate({url: "http://localhost:5173"});
await mcp_playwright_browser_wait_for({time: 10});

await mcp_playwright_browser_wait_for({text: "Username", time: 30});
await mcp_playwright_browser_type({element: "Username input field", ref: "e9", text: "ArkanWolfshade"});
await mcp_playwright_browser_type({element: "Password input field", ref: "e10", text: "Cthulhu1"});
await mcp_playwright_browser_click({element: "Login button", ref: "e11"});
await mcp_playwright_browser_wait_for({time: 15});

// Verify character selection screen
await mcp_playwright_browser_wait_for({text: "Select Your Character", time: 30});
```

**Expected Result**: Character selection screen shows list of characters

### Step 2: Initiate Character Deletion

**Purpose**: Click delete button and verify confirmation dialog

**Commands**:

```javascript
// Click delete button for a character (confirm ref via snapshot)
await mcp_playwright_browser_click({element: "Delete button", ref: "eXX"});
await mcp_playwright_browser_wait_for({time: 2});

// Verify confirmation dialog appears
await mcp_playwright_browser_wait_for({text: "Are you sure", time: 10});
```

**Expected Result**: Confirmation dialog appears asking to confirm deletion

### Step 3: Cancel Deletion

**Purpose**: Verify cancellation works

**Commands**:

```javascript
// Click cancel button
await mcp_playwright_browser_click({element: "Cancel button", ref: "eXX"});
await mcp_playwright_browser_wait_for({time: 2});

// Verify character is still in list
const snapshot = await mcp_playwright_browser_snapshot();
// Character should still be visible
```

**Expected Result**: Character remains in list, deletion cancelled

### Step 4: Confirm Deletion

**Purpose**: Confirm and verify character is deleted

**Commands**:

```javascript
// Click delete button again
await mcp_playwright_browser_click({element: "Delete button", ref: "eXX"});
await mcp_playwright_browser_wait_for({time: 2});

// Click confirm delete
await mcp_playwright_browser_click({element: "Confirm Delete button", ref: "eXX"});
await mcp_playwright_browser_wait_for({time: 5});

// Verify character is removed from list
const snapshot = await mcp_playwright_browser_snapshot();
// Deleted character should not appear in list
```

**Expected Result**: Character is removed from selection list

### Step 5: Verify Name Can Be Reused

**Purpose**: Verify that deleted character name can be reused

**Commands**:

```javascript
// Note the deleted character's name (e.g., "TestCharacter1")

// Click "Create New Character"
await mcp_playwright_browser_click({element: "Create New Character button", ref: "eXX"});
await mcp_playwright_browser_wait_for({time: 5});

// Create new character with same name as deleted character
await mcp_playwright_browser_type({element: "Character name input", ref: "eXX", text: "TestCharacter1"});

// Complete character creation
// ... stats rolling and creation steps ...

// Verify character is created successfully
await mcp_playwright_browser_wait_for({text: "Select Your Character", time: 30});
// New character with reused name should appear in list
```

**Expected Result**: Character with reused name is created successfully

## Expected Results Summary

1. ✅ Delete button appears for each character
2. ✅ Confirmation dialog appears before deletion
3. ✅ Cancellation works correctly
4. ✅ Character is removed from list after confirmation
5. ✅ Deleted character name can be reused
6. ✅ Character slot becomes available for new character

## Failure Modes

**Delete button not visible**: UI may not be rendering correctly

**Confirmation dialog doesn't appear**: Deletion flow may have issues

**Character not removed from list**: Soft delete may not be working

**Name reuse fails**: Uniqueness check may not exclude deleted characters

## Notes

Characters are soft-deleted (hidden but data preserved)

- Deleted characters cannot be restored by players
- Deleted character names can be reused immediately
- Character limit is based on active characters only
