# Scenario 30: Character Name Uniqueness **[REQUIRES MULTI-PLAYER]**

## Overview

Tests case-insensitive character name uniqueness, including conflict detection and case preservation.

**MULTI-CHARACTER**: This scenario tests case-insensitive name validation.

## Prerequisites

### BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY

1. **Database State**: Test user has 0-2 active characters
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **No Previous Sessions**: Browser is clean with no existing game sessions

### ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE

## Test Configuration

**Test Player**: ArkanWolfshade

**Testing Approach**: Playwright MCP

**Timeout Settings**: Use configurable timeouts from master rules

## Execution Steps

### Step 1: Create Character with Mixed Case

**Purpose**: Create first character with specific case

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

// Navigate to character creation
// ... character creation steps ...

// Create character with name "Ithaqua" (mixed case)
await mcp_playwright_browser_type({element: "Character name input", ref: "eXX", text: "Ithaqua"});
// ... complete character creation ...
```

**Expected Result**: Character "Ithaqua" created successfully

### Step 2: Attempt to Create Character with Different Case

**Purpose**: Verify case-insensitive conflict detection

**Commands**:

```javascript
// From character selection, create new character
await mcp_playwright_browser_click({element: "Create New Character button", ref: "eXX"});
await mcp_playwright_browser_wait_for({time: 5});

// Try to create character with name "ithaqua" (lowercase, conflicts with "Ithaqua")
await mcp_playwright_browser_type({element: "Character name input", ref: "eXX", text: "ithaqua"});

// Complete character creation attempt
// ... stats rolling and accept ...

// Verify error message
await mcp_playwright_browser_wait_for({text: "already exists", time: 30});
// Or check for case-insensitive conflict message
```

**Expected Result**: Error message indicating character name already exists (case-insensitive)

### Step 3: Verify Case Preservation

**Purpose**: Verify that original case is preserved in storage

**Commands**:

```javascript
// Return to character selection
// Verify that character name is displayed as "Ithaqua" (original case)
const snapshot = await mcp_playwright_browser_snapshot();
// Character name should show as "Ithaqua", not "ithaqua"
```

**Expected Result**: Character name displayed with original case ("Ithaqua")

### Step 4: Test with All Lowercase

**Purpose**: Create character with all lowercase and verify conflict

**Commands**:

```javascript
// Create character with name "testcharacter" (all lowercase)
// ... character creation with "testcharacter" ...

// Attempt to create "TestCharacter" (mixed case)
// Should fail with conflict error
```

**Expected Result**: Case-insensitive conflict detected regardless of case combination

## Expected Results Summary

1. ✅ Character names are case-insensitive unique
2. ✅ "Ithaqua" and "ithaqua" are mutually exclusive
3. ✅ Original case is preserved in storage and display
4. ✅ First name created wins in case of conflict
5. ✅ Error messages indicate case-insensitive uniqueness

## Failure Modes

**Case-insensitive conflict not detected**: Database index or validation may not be working

**Case not preserved**: Name may be normalized incorrectly

**Wrong error message**: Error handling may need updates

## Notes

Character names are stored exactly as entered (case-sensitive storage)

- Uniqueness is enforced case-insensitively
- First name created wins in case of conflict
- Same applies to usernames (case-insensitive unique)
