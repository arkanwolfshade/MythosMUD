# Scenario 28: Multi-Character Creation **[REQUIRES MULTI-PLAYER]**

## Overview

Tests creating multiple characters for a single user, including character limit enforcement and character name validation.

**MULTI-CHARACTER**: This scenario tests the character creation limits and name uniqueness.

## Prerequisites

### BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY

1. **Database State**: Test user has 0-2 active characters (to test limit)
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **No Previous Sessions**: Browser is clean with no existing game sessions

### ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE

## Test Configuration

**Test Player**: ArkanWolfshade

**Testing Approach**: Playwright MCP

**Timeout Settings**: Use configurable timeouts from master rules

## Execution Steps

### Step 1: Login and Navigate to Character Creation

**Purpose**: Login and access character creation flow

**Commands**:

```javascript
// Navigate to client
await mcp_playwright_browser_navigate({url: "http://localhost:5173"});
await mcp_playwright_browser_wait_for({time: 10});

// Login
await mcp_playwright_browser_wait_for({text: "Username", time: 30});
await mcp_playwright_browser_type({element: "Username input field", ref: "e9", text: "ArkanWolfshade"});
await mcp_playwright_browser_type({element: "Password input field", ref: "e10", text: "Cthulhu1"});
await mcp_playwright_browser_click({element: "Login button", ref: "e11"});
await mcp_playwright_browser_wait_for({time: 15});

// If character selection appears, click "Create New Character"
const snapshot = await mcp_playwright_browser_snapshot();
if (snapshot.includes("Select Your Character")) {
  await mcp_playwright_browser_click({element: "Create New Character button", ref: "eXX"});
  await mcp_playwright_browser_wait_for({time: 5});
}
```

**Expected Result**: Character creation flow begins (profession selection or stats rolling)

### Step 2: Create First Character

**Purpose**: Create the first character with explicit name

**Commands**:

```javascript
// Select profession (if profession selection appears)
// ... profession selection steps ...

// Enter character name in stats rolling screen
await mcp_playwright_browser_wait_for({text: "Character Name", time: 30});
await mcp_playwright_browser_type({element: "Character name input", ref: "eXX", text: "TestCharacter1"});

// Roll and accept stats
// ... stats rolling steps ...

// Click "Accept Stats & Create Character"
await mcp_playwright_browser_click({element: "Accept button", ref: "eXX"});
await mcp_playwright_browser_wait_for({time: 10});
```

**Expected Result**: Character created successfully, returns to character selection screen

### Step 3: Create Second Character

**Purpose**: Create a second character to test multiple characters

**Commands**:

```javascript
// From character selection screen, click "Create New Character"
await mcp_playwright_browser_wait_for({text: "Create New Character", time: 30});
await mcp_playwright_browser_click({element: "Create New Character button", ref: "eXX"});
await mcp_playwright_browser_wait_for({time: 5});

// Create second character with different name
// ... repeat character creation steps with name "TestCharacter2" ...
```

**Expected Result**: Second character created successfully

### Step 4: Test Character Limit (Create 4th Character)

**Purpose**: Verify that creating a 4th character is rejected

**Commands**:

```javascript
// Create third character first
// ... create "TestCharacter3" ...

// Attempt to create fourth character
await mcp_playwright_browser_click({element: "Create New Character button", ref: "eXX"});
await mcp_playwright_browser_wait_for({time: 5});

// Try to create character
// ... attempt character creation ...

// Verify error message about character limit
await mcp_playwright_browser_wait_for({text: "maximum", time: 30});
// Or check for error message about 3 character limit
```

**Expected Result**: Error message displayed indicating character limit reached (3 characters maximum)

### Step 5: Test Case-Insensitive Name Conflict

**Purpose**: Verify that case-insensitive name conflicts are detected

**Commands**:

```javascript
// From character selection, click "Create New Character"
// Enter character name with different case: "testcharacter1" (conflicts with "TestCharacter1")
await mcp_playwright_browser_type({element: "Character name input", ref: "eXX", text: "testcharacter1"});

// Attempt to create character
await mcp_playwright_browser_click({element: "Accept button", ref: "eXX"});
await mcp_playwright_browser_wait_for({time: 5});

// Verify error message about name conflict
await mcp_playwright_browser_wait_for({text: "already exists", time: 30});
```

**Expected Result**: Error message displayed indicating character name already exists (case-insensitive)

## Expected Results Summary

1. ✅ Users can create up to 3 active characters
2. ✅ Character creation requires explicit name (no auto-naming)
3. ✅ 4th character creation is rejected with appropriate error
4. ✅ Case-insensitive name conflicts are detected
5. ✅ Character names are stored with original case
6. ✅ Character selection screen shows all created characters

## Failure Modes

**Character limit not enforced**: Service layer may not be checking limit correctly

**Name conflict not detected**: Case-insensitive comparison may not be working

**Character creation fails**: API endpoint or validation may have issues

**Character not appearing in list**: Character may be soft-deleted or persistence issue

## Notes

Character names must be between 1-50 characters

- Character names are case-insensitive unique among active characters
- Deleted character names can be reused
- Maximum 3 active characters per user
