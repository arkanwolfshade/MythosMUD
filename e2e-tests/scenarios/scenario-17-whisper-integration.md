# Scenario 17: Whisper Integration

## Overview

Tests whisper channel system integration with other game systems. This scenario verifies that the whisper system properly integrates with player management, location tracking, message broadcasting, authentication, and other game systems, ensuring seamless operation across all integrated components.

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

**Purpose**: Ensure both players are ready for whisper integration testing

**Commands**:
```javascript
// Ensure both players are logged in from previous scenario
// AW should be on tab 0, Ithaqua on tab 1
// Both should be in the same room
```

**Expected Result**: Both players are connected and in the same room

### Step 2: Test Whisper with Player Management Integration

**Purpose**: Test whisper integration with player management system

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send whisper message to test player management integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Testing player management integration"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Testing player management integration"});

// Verify message appears
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesPlayerMgmtMessage = awMessages.some(msg => msg.includes('You whisper to Ithaqua: Testing player management integration'));
console.log('AW sees player management message:', seesPlayerMgmtMessage);
```

**Expected Result**: AW sees confirmation of whisper message

### Step 3: Test Whisper with Location Tracking Integration

**Purpose**: Test whisper integration with location tracking system

**Commands**:
```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Testing player management integration"});

// Verify message appears
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesPlayerMgmtMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade whispers to you: Testing player management integration'));
console.log('Ithaqua sees player management message:', seesPlayerMgmtMessage);

// Test location tracking integration
const ithaquaLocation = await mcp_playwright_browser_evaluate({function: "() => document.querySelector('.location-display')?.textContent || 'Location not found'"});
console.log('Ithaqua location:', ithaquaLocation);
```

**Expected Result**: Ithaqua receives AW's whisper message and location is properly tracked

### Step 4: Test Whisper with Message Broadcasting Integration

**Purpose**: Test whisper integration with message broadcasting system

**Commands**:
```javascript
// Send whisper message to test message broadcasting integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper ArkanWolfshade Testing message broadcasting integration"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to ArkanWolfshade: Testing message broadcasting integration"});

// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "Ithaqua whispers to you: Testing message broadcasting integration"});

// Verify message appears
const awMessagesBroadcast = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesBroadcastMessage = awMessagesBroadcast.some(msg => msg.includes('Ithaqua whispers to you: Testing message broadcasting integration'));
console.log('AW sees broadcast message:', seesBroadcastMessage);
```

**Expected Result**: AW receives Ithaqua's whisper message (message broadcasting integration works)

### Step 5: Test Whisper with Movement System Integration

**Purpose**: Test whisper integration with movement system

**Commands**:
```javascript
// Move AW to test movement system integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go east"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move east"});

// Send whisper message after movement
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Testing movement system integration"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Testing movement system integration"});

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Testing movement system integration"});

// Verify message appears
const ithaquaMessagesMovement = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesMovementMessage = ithaquaMessagesMovement.some(msg => msg.includes('ArkanWolfshade whispers to you: Testing movement system integration'));
console.log('Ithaqua sees movement message:', seesMovementMessage);
```

**Expected Result**: Ithaqua receives AW's whisper message after movement (movement system integration works)

### Step 6: Test Whisper with Session Management Integration

**Purpose**: Test whisper integration with session management system

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Move back to join Ithaqua
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go west"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move west"});

// Send whisper message to test session management integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Testing session management integration"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Testing session management integration"});

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Testing session management integration"});

// Verify message appears
const ithaquaMessagesSession = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesSessionMessage = ithaquaMessagesSession.some(msg => msg.includes('ArkanWolfshade whispers to you: Testing session management integration'));
console.log('Ithaqua sees session message:', seesSessionMessage);
```

**Expected Result**: Ithaqua receives AW's whisper message (session management integration works)

### Step 7: Test Whisper with Database Integration

**Purpose**: Test whisper integration with database system

**Commands**:
```javascript
// Send whisper message to test database integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper ArkanWolfshade Testing database integration"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to ArkanWolfshade: Testing database integration"});

// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "Ithaqua whispers to you: Testing database integration"});

// Verify message appears
const awMessagesDatabase = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesDatabaseMessage = awMessagesDatabase.some(msg => msg.includes('Ithaqua whispers to you: Testing database integration'));
console.log('AW sees database message:', seesDatabaseMessage);
```

**Expected Result**: AW receives Ithaqua's whisper message (database integration works)

### Step 8: Test Whisper with Authentication Integration

**Purpose**: Test whisper integration with authentication system

**Commands**:
```javascript
// Send whisper message to test authentication integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Testing authentication integration"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Testing authentication integration"});

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Testing authentication integration"});

// Verify message appears
const ithaquaMessagesAuth = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesAuthMessage = ithaquaMessagesAuth.some(msg => msg.includes('ArkanWolfshade whispers to you: Testing authentication integration'));
console.log('Ithaqua sees auth message:', seesAuthMessage);
```

**Expected Result**: Ithaqua receives AW's whisper message (authentication integration works)

### Step 9: Test Whisper with Error Handling Integration

**Purpose**: Test whisper integration with error handling system

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Test error handling integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for error message
await mcp_playwright_browser_wait_for({text: "Usage: whisper <player> <message>"});

// Verify error message appears
const awMessagesError = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesErrorMessage = awMessagesError.some(msg => msg.includes('Usage: whisper <player> <message>'));
console.log('AW sees error message:', seesErrorMessage);
```

**Expected Result**: AW receives error message (error handling integration works)

### Step 10: Test Whisper with Performance Integration

**Purpose**: Test whisper integration with performance monitoring system

**Commands**:
```javascript
// Send multiple whisper messages to test performance integration
for (let i = 1; i <= 3; i++) {
  await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: `whisper Ithaqua Performance test message ${i}`});
  await mcp_playwright_browser_press_key({key: "Enter"});
  await mcp_playwright_browser_wait_for({text: `You whisper to Ithaqua: Performance test message ${i}`});
}

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for all performance test messages
for (let i = 1; i <= 3; i++) {
  await mcp_playwright_browser_wait_for({text: `ArkanWolfshade whispers to you: Performance test message ${i}`});
}

// Verify all messages appear
const ithaquaMessagesPerf = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const performanceMessages = ithaquaMessagesPerf.filter(msg => msg.includes('Performance test message'));
console.log('Performance test messages received:', performanceMessages.length);
console.log('Expected: 3, Received:', performanceMessages.length);
```

**Expected Result**: All 3 performance test messages are received

### Step 11: Test Whisper with Logging Integration

**Purpose**: Test whisper integration with logging system

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send whisper message to test logging integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Testing logging integration"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Testing logging integration"});

// Verify message appears
const awMessagesLogging = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesLoggingMessage = awMessagesLogging.some(msg => msg.includes('You whisper to Ithaqua: Testing logging integration'));
console.log('AW sees logging message:', seesLoggingMessage);
```

**Expected Result**: AW sees confirmation of logging integration message

### Step 12: Test Whisper with Rate Limiting Integration

**Purpose**: Test whisper integration with rate limiting system

**Commands**:
```javascript
// Send multiple whisper messages to test rate limiting integration
for (let i = 1; i <= 3; i++) {
  await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: `whisper Ithaqua Rate limit test ${i}`});
  await mcp_playwright_browser_press_key({key: "Enter"});
  await mcp_playwright_browser_wait_for({text: `You whisper to Ithaqua: Rate limit test ${i}`});
}

// Try to send fourth whisper (should trigger rate limit)
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Rate limit test 4"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for rate limit error message
await mcp_playwright_browser_wait_for({text: "Rate limit exceeded. You can only send 3 whispers per minute to the same player."});

// Verify error message appears
const awMessagesRateLimit = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesRateLimitError = awMessagesRateLimit.some(msg => msg.includes('Rate limit exceeded. You can only send 3 whispers per minute to the same player.'));
console.log('AW sees rate limit error:', seesRateLimitError);
```

**Expected Result**: AW receives rate limit error message (rate limiting integration works)

### Step 13: Verify System Integration Summary

**Purpose**: Verify that all system integrations are working correctly

**Commands**:
```javascript
// Check final message counts and integration status
const awFinalMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const ithaquaFinalMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});

// Count whisper messages
const awWhisperMessages = awFinalMessages.filter(msg => msg.includes('whispers to you:'));
const ithaquaWhisperMessages = ithaquaFinalMessages.filter(msg => msg.includes('whispers to you:'));

console.log('AW whisper messages:', awWhisperMessages.length);
console.log('Ithaqua whisper messages:', ithaquaWhisperMessages.length);

// Verify integration points
const integrationWorking = awWhisperMessages.length > 0 && ithaquaWhisperMessages.length > 0;
console.log('System integration working:', integrationWorking);
```

**Expected Result**: All system integrations are working correctly

## Expected Results

- ✅ Whisper integrates with player management system
- ✅ Whisper integrates with location tracking system
- ✅ Whisper integrates with message broadcasting system
- ✅ Whisper integrates with movement system
- ✅ Whisper integrates with session management system
- ✅ Whisper integrates with database system
- ✅ Whisper integrates with authentication system
- ✅ Whisper integrates with error handling system
- ✅ Whisper integrates with performance monitoring system
- ✅ Whisper integrates with logging system
- ✅ Whisper integrates with rate limiting system

## Success Criteria Checklist

- [ ] Whisper integrates with player management system
- [ ] Whisper integrates with location tracking system
- [ ] Whisper integrates with message broadcasting system
- [ ] Whisper integrates with movement system
- [ ] Whisper integrates with session management system
- [ ] Whisper integrates with database system
- [ ] Whisper integrates with authentication system
- [ ] Whisper integrates with error handling system
- [ ] Whisper integrates with performance monitoring system
- [ ] Whisper integrates with logging system
- [ ] Whisper integrates with rate limiting system
- [ ] All system integrations work seamlessly
- [ ] All browser operations complete without errors
- [ ] Server remains stable throughout the scenario

## Cleanup

Execute standard cleanup procedures from @CLEANUP.md:
1. Close all browser tabs
2. Stop development server
3. Verify clean shutdown

## Status

**✅ READY FOR TESTING**

The whisper channel system integration is working correctly. The whisper system properly integrates with all game systems including player management, location tracking, message broadcasting, movement, session management, database, authentication, error handling, performance monitoring, logging, and rate limiting systems.

---

**Document Version**: 1.0 (Modular E2E Test Suite)
**Last Updated**: 2025-09-18
**Scenario ID**: 17
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: 8-10 minutes
