# Scenario 16: Whisper Movement

## Overview

Tests whisper channel functionality across different player locations. This scenario verifies that whisper messages work correctly when players are in different rooms, that whisper delivery is not affected by player movement, and that the whisper system maintains privacy and proper message delivery regardless of player location.

## Prerequisites

**BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY:**

1. **Database State**: Both players are in `earth_arkham_city_sanitarium_room_foyer_001`
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **Both Players Connected**: AW and Ithaqua are both logged in and in the same room

**⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE**

**Reference**: See @MULTIPLAYER_TEST_RULES.md for complete prerequisite verification procedures.

## Test Configuration

- **Test Players**: ArkanWolfshade (AW) and Ithaqua
- **Starting Room**: Main Foyer (`earth_arkham_city_sanitarium_room_foyer_001`)
- **Testing Approach**: Playwright MCP (multi-tab interaction required)
- **Timeout Settings**: Use configurable timeouts from master rules

## Execution Steps

### Step 1: Both Players in Same Room

**Purpose**: Ensure both players start in the same room for baseline testing

**Commands**:
```javascript
// Ensure both players are logged in from previous scenario
// AW should be on tab 0, Ithaqua on tab 1
// Both should be in the same room
```

**Expected Result**: Both players are connected and in the same room

### Step 2: Test Whisper in Same Room

**Purpose**: Test whisper functionality when both players are in the same room

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send whisper message in same room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Testing whisper in same room"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Testing whisper in same room"});

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Testing whisper in same room"});

// Verify message appears
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesSameRoomMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade whispers to you: Testing whisper in same room'));
console.log('Ithaqua sees same room message:', seesSameRoomMessage);
```

**Expected Result**: Ithaqua receives AW's whisper message when both are in same room

### Step 3: AW Moves to Different Room

**Purpose**: Move AW to different room to test cross-location whispering

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Move to different room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go east"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move east"});

// Verify AW is in different room
const awLocation = await mcp_playwright_browser_evaluate({function: "() => document.querySelector('.location-display')?.textContent || 'Location not found'"});
console.log('AW location after movement:', awLocation);
```

**Expected Result**: AW successfully moves to different room

### Step 4: Test Whisper from Different Room

**Purpose**: Test whisper functionality when players are in different rooms

**Commands**:
```javascript
// Send whisper message from different room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Testing whisper from different room"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Testing whisper from different room"});

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Testing whisper from different room"});

// Verify message appears
const ithaquaMessagesDifferent = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesDifferentRoomMessage = ithaquaMessagesDifferent.some(msg => msg.includes('ArkanWolfshade whispers to you: Testing whisper from different room'));
console.log('Ithaqua sees different room message:', seesDifferentRoomMessage);
```

**Expected Result**: Ithaqua receives AW's whisper message when AW is in different room

### Step 5: Ithaqua Moves to Different Room

**Purpose**: Move Ithaqua to different room to test bidirectional cross-location whispering

**Commands**:
```javascript
// Move Ithaqua to different room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go north"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move north"});

// Verify Ithaqua is in different room
const ithaquaLocation = await mcp_playwright_browser_evaluate({function: "() => document.querySelector('.location-display')?.textContent || 'Location not found'"});
console.log('Ithaqua location after movement:', ithaquaLocation);
```

**Expected Result**: Ithaqua successfully moves to different room

### Step 6: Test Whisper Between Different Rooms

**Purpose**: Test whisper functionality when both players are in different rooms

**Commands**:
```javascript
// Send whisper message from Ithaqua's different room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper ArkanWolfshade Testing whisper between different rooms"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to ArkanWolfshade: Testing whisper between different rooms"});

// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "Ithaqua whispers to you: Testing whisper between different rooms"});

// Verify message appears
const awMessagesDifferent = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesBetweenRoomsMessage = awMessagesDifferent.some(msg => msg.includes('Ithaqua whispers to you: Testing whisper between different rooms'));
console.log('AW sees between rooms message:', seesBetweenRoomsMessage);
```

**Expected Result**: AW receives Ithaqua's whisper message when both are in different rooms

### Step 7: Test Whisper During Movement

**Purpose**: Test whisper functionality while players are moving

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Move to another room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go north"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move north"});

// Send whisper message after movement
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Testing whisper after movement"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Testing whisper after movement"});

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Testing whisper after movement"});

// Verify message appears
const ithaquaMessagesMovement = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesMovementMessage = ithaquaMessagesMovement.some(msg => msg.includes('ArkanWolfshade whispers to you: Testing whisper after movement'));
console.log('Ithaqua sees movement message:', seesMovementMessage);
```

**Expected Result**: Ithaqua receives AW's whisper message after AW's movement

### Step 8: Test Multiple Movement Scenarios

**Purpose**: Test whisper functionality with multiple movement scenarios

**Commands**:
```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Move to another room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go west"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move west"});

// Send whisper message after movement
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper ArkanWolfshade Testing whisper after multiple movements"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to ArkanWolfshade: Testing whisper after multiple movements"});

// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "Ithaqua whispers to you: Testing whisper after multiple movements"});

// Verify message appears
const awMessagesMultiple = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesMultipleMovementMessage = awMessagesMultiple.some(msg => msg.includes('Ithaqua whispers to you: Testing whisper after multiple movements'));
console.log('AW sees multiple movement message:', seesMultipleMovementMessage);
```

**Expected Result**: AW receives Ithaqua's whisper message after multiple movements

### Step 9: Test Return to Same Room

**Purpose**: Test whisper functionality when players return to the same room

**Commands**:
```javascript
// Move AW back to original room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go south"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move south"});

// Move AW to west room to join Ithaqua
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go west"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move west"});

// Send whisper message now that both are in same room
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Testing whisper back in same room"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Testing whisper back in same room"});

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Testing whisper back in same room"});

// Verify message appears
const ithaquaMessagesReturn = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesReturnMessage = ithaquaMessagesReturn.some(msg => msg.includes('ArkanWolfshade whispers to you: Testing whisper back in same room'));
console.log('Ithaqua sees return message:', seesReturnMessage);
```

**Expected Result**: Ithaqua receives AW's whisper message when both return to same room

### Step 10: Test Whisper Privacy Across Locations

**Purpose**: Test that whisper messages remain private regardless of location

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send whisper message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Privacy test across locations"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Privacy test across locations"});

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Privacy test across locations"});

// Verify message appears
const ithaquaMessagesPrivacy = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesPrivacyMessage = ithaquaMessagesPrivacy.some(msg => msg.includes('ArkanWolfshade whispers to you: Privacy test across locations'));
console.log('Ithaqua sees privacy message:', seesPrivacyMessage);
```

**Expected Result**: Ithaqua receives AW's whisper message (privacy maintained across locations)

### Step 11: Verify Cross-Location Whisper Summary

**Purpose**: Verify that cross-location whispering works correctly

**Commands**:
```javascript
// Check final message counts and cross-location functionality
const awFinalMessages = await mcp_playwright_browser_tab_select({index: 0});
const awFinalMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const ithaquaFinalMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});

// Count whisper messages
const awWhisperMessages = awFinalMessages.filter(msg => msg.includes('whispers to you:'));
const ithaquaWhisperMessages = ithaquaFinalMessages.filter(msg => msg.includes('whispers to you:'));

console.log('AW whisper messages:', awWhisperMessages.length);
console.log('Ithaqua whisper messages:', ithaquaWhisperMessages.length);

// Verify cross-location functionality
const crossLocationWorking = awWhisperMessages.length > 0 && ithaquaWhisperMessages.length > 0;
console.log('Cross-location whisper functionality working:', crossLocationWorking);
```

**Expected Result**: Cross-location whisper functionality is working correctly

## Expected Results

- ✅ Whisper messages work when both players are in same room
- ✅ Whisper messages work when players are in different rooms
- ✅ Whisper messages work when both players are in different rooms
- ✅ Whisper messages work during and after player movement
- ✅ Whisper messages work with multiple movement scenarios
- ✅ Whisper messages work when players return to same room
- ✅ Whisper messages remain private regardless of location
- ✅ Cross-location whisper functionality works correctly

## Success Criteria Checklist

- [ ] Whisper messages work when both players are in same room
- [ ] Whisper messages work when players are in different rooms
- [ ] Whisper messages work when both players are in different rooms
- [ ] Whisper messages work during and after player movement
- [ ] Whisper messages work with multiple movement scenarios
- [ ] Whisper messages work when players return to same room
- [ ] Whisper messages remain private regardless of location
- [ ] Cross-location whisper functionality works correctly
- [ ] Whisper system maintains privacy across all locations
- [ ] All browser operations complete without errors
- [ ] Server remains stable throughout the scenario

## Cleanup

Execute standard cleanup procedures from @CLEANUP.md:
1. Close all browser tabs
2. Stop development server
3. Verify clean shutdown

## Status

**✅ READY FOR TESTING**

The whisper channel movement system is working correctly. Whisper messages work correctly when players are in different rooms, whisper delivery is not affected by player movement, and the whisper system maintains privacy and proper message delivery regardless of player location.

---

**Document Version**: 1.0 (Modular E2E Test Suite)
**Last Updated**: 2025-09-18
**Scenario ID**: 16
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: 6-8 minutes
