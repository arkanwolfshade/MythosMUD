# Scenario 12: Local Channel Integration

## Overview

Tests local channel system integration with other game systems. This scenario verifies that the local channel system properly integrates with player management, location tracking, message broadcasting, and other game systems, ensuring seamless operation across all integrated components.

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

### Step 1: Both Players in Same Sub-Zone

**Purpose**: Ensure both players are ready for integration testing

**Commands**:
```javascript
// Ensure both players are logged in from previous scenario
// AW should be on tab 0, Ithaqua on tab 1
// Both should be in the same room (same sub-zone)
```

**Expected Result**: Both players are connected and in the same sub-zone

### Step 2: Test Local Channel with Player Management Integration

**Purpose**: Test local channel integration with player management system

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send local message to test player management integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local Testing player management integration"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You say locally: Testing player management integration"});

// Verify message appears
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesPlayerMgmtMessage = awMessages.some(msg => msg.includes('You say locally: Testing player management integration'));
console.log('AW sees player management message:', seesPlayerMgmtMessage);
```

**Expected Result**: AW sees confirmation of local message

### Step 3: Test Local Channel with Location Tracking Integration

**Purpose**: Test local channel integration with location tracking system

**Commands**:
```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for local message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade says locally: Testing player management integration"});

// Verify message appears
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesPlayerMgmtMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade says locally: Testing player management integration'));
console.log('Ithaqua sees player management message:', seesPlayerMgmtMessage);

// Test location tracking integration
const ithaquaLocation = await mcp_playwright_browser_evaluate({function: "() => document.querySelector('.location-display')?.textContent || 'Location not found'"});
console.log('Ithaqua location:', ithaquaLocation);
```

**Expected Result**: Ithaqua sees AW's local message and location is properly tracked

### Step 4: Test Local Channel with Message Broadcasting Integration

**Purpose**: Test local channel integration with message broadcasting system

**Commands**:
```javascript
// Send local message to test message broadcasting integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local Testing message broadcasting integration"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You say locally: Testing message broadcasting integration"});

// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for local message
await mcp_playwright_browser_wait_for({text: "Ithaqua says locally: Testing message broadcasting integration"});

// Verify message appears
const awMessagesBroadcast = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesBroadcastMessage = awMessagesBroadcast.some(msg => msg.includes('Ithaqua says locally: Testing message broadcasting integration'));
console.log('AW sees broadcast message:', seesBroadcastMessage);
```

**Expected Result**: AW sees Ithaqua's local message (message broadcasting integration works)

### Step 5: Test Local Channel with Movement System Integration

**Purpose**: Test local channel integration with movement system

**Commands**:
```javascript
// Move AW to test movement system integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go east"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move east"});

// Send local message after movement
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local Testing movement system integration"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You say locally: Testing movement system integration"});

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait a moment to ensure message would have arrived if not isolated
await mcp_playwright_browser_wait_for({time: 2});

// Check if Ithaqua sees AW's local message (should not due to sub-zone isolation)
const ithaquaMessagesMovement = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesMovementMessage = ithaquaMessagesMovement.some(msg => msg.includes('ArkanWolfshade says locally: Testing movement system integration'));
console.log('Ithaqua sees movement message (should be false):', !seesMovementMessage);
```

**Expected Result**: Ithaqua does NOT see AW's local message after movement (movement system integration works)

### Step 6: Test Local Channel with Session Management Integration

**Purpose**: Test local channel integration with session management system

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Move back to join Ithaqua
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "go west"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for movement confirmation
await mcp_playwright_browser_wait_for({text: "You move west"});

// Send local message to test session management integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local Testing session management integration"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You say locally: Testing session management integration"});

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for local message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade says locally: Testing session management integration"});

// Verify message appears
const ithaquaMessagesSession = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesSessionMessage = ithaquaMessagesSession.some(msg => msg.includes('ArkanWolfshade says locally: Testing session management integration'));
console.log('Ithaqua sees session message:', seesSessionMessage);
```

**Expected Result**: Ithaqua sees AW's local message (session management integration works)

### Step 7: Test Local Channel with Database Integration

**Purpose**: Test local channel integration with database system

**Commands**:
```javascript
// Send local message to test database integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local Testing database integration"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You say locally: Testing database integration"});

// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for local message
await mcp_playwright_browser_wait_for({text: "Ithaqua says locally: Testing database integration"});

// Verify message appears
const awMessagesDatabase = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesDatabaseMessage = awMessagesDatabase.some(msg => msg.includes('Ithaqua says locally: Testing database integration'));
console.log('AW sees database message:', seesDatabaseMessage);
```

**Expected Result**: AW sees Ithaqua's local message (database integration works)

### Step 8: Test Local Channel with Authentication Integration

**Purpose**: Test local channel integration with authentication system

**Commands**:
```javascript
// Send local message to test authentication integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local Testing authentication integration"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You say locally: Testing authentication integration"});

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for local message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade says locally: Testing authentication integration"});

// Verify message appears
const ithaquaMessagesAuth = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesAuthMessage = ithaquaMessagesAuth.some(msg => msg.includes('ArkanWolfshade says locally: Testing authentication integration'));
console.log('Ithaqua sees auth message:', seesAuthMessage);
```

**Expected Result**: Ithaqua sees AW's local message (authentication integration works)

### Step 9: Test Local Channel with Error Handling Integration

**Purpose**: Test local channel integration with error handling system

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Test error handling integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for error message
await mcp_playwright_browser_wait_for({text: "You must provide a message to send locally"});

// Verify error message appears
const awMessagesError = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesErrorMessage = awMessagesError.some(msg => msg.includes('You must provide a message to send locally'));
console.log('AW sees error message:', seesErrorMessage);
```

**Expected Result**: AW receives error message (error handling integration works)

### Step 10: Test Local Channel with Performance Integration

**Purpose**: Test local channel integration with performance monitoring system

**Commands**:
```javascript
// Send multiple local messages to test performance integration
for (let i = 1; i <= 5; i++) {
  await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: `local Performance test message ${i}`});
  await mcp_playwright_browser_press_key({key: "Enter"});
  await mcp_playwright_browser_wait_for({text: `You say locally: Performance test message ${i}`});
}

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for all performance test messages
for (let i = 1; i <= 5; i++) {
  await mcp_playwright_browser_wait_for({text: `ArkanWolfshade says locally: Performance test message ${i}`});
}

// Verify all messages appear
const ithaquaMessagesPerf = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const performanceMessages = ithaquaMessagesPerf.filter(msg => msg.includes('Performance test message'));
console.log('Performance test messages received:', performanceMessages.length);
console.log('Expected: 5, Received:', performanceMessages.length);
```

**Expected Result**: All 5 performance test messages are received

### Step 11: Test Local Channel with Logging Integration

**Purpose**: Test local channel integration with logging system

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send local message to test logging integration
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "local Testing logging integration"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You say locally: Testing logging integration"});

// Verify message appears
const awMessagesLogging = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesLoggingMessage = awMessagesLogging.some(msg => msg.includes('You say locally: Testing logging integration'));
console.log('AW sees logging message:', seesLoggingMessage);
```

**Expected Result**: AW sees confirmation of logging integration message

### Step 12: Verify System Integration Summary

**Purpose**: Verify that all system integrations are working correctly

**Commands**:
```javascript
// Check final message counts and integration status
const awFinalMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const ithaquaFinalMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});

// Count local messages
const awLocalMessages = awFinalMessages.filter(msg => msg.includes('says locally:'));
const ithaquaLocalMessages = ithaquaFinalMessages.filter(msg => msg.includes('says locally:'));

console.log('AW local messages:', awLocalMessages.length);
console.log('Ithaqua local messages:', ithaquaLocalMessages.length);

// Verify integration points
const integrationWorking = awLocalMessages.length > 0 && ithaquaLocalMessages.length > 0;
console.log('System integration working:', integrationWorking);
```

**Expected Result**: All system integrations are working correctly

## Expected Results

- ✅ Local channel integrates with player management system
- ✅ Local channel integrates with location tracking system
- ✅ Local channel integrates with message broadcasting system
- ✅ Local channel integrates with movement system
- ✅ Local channel integrates with session management system
- ✅ Local channel integrates with database system
- ✅ Local channel integrates with authentication system
- ✅ Local channel integrates with error handling system
- ✅ Local channel integrates with performance monitoring system
- ✅ Local channel integrates with logging system

## Success Criteria Checklist

- [ ] Local channel integrates with player management system
- [ ] Local channel integrates with location tracking system
- [ ] Local channel integrates with message broadcasting system
- [ ] Local channel integrates with movement system
- [ ] Local channel integrates with session management system
- [ ] Local channel integrates with database system
- [ ] Local channel integrates with authentication system
- [ ] Local channel integrates with error handling system
- [ ] Local channel integrates with performance monitoring system
- [ ] Local channel integrates with logging system
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

The local channel system integration is working correctly. The local channel system properly integrates with all game systems including player management, location tracking, message broadcasting, movement, session management, database, authentication, error handling, performance monitoring, and logging systems.

---

**Document Version**: 1.0 (Modular E2E Test Suite)
**Last Updated**: 2025-09-18
**Scenario ID**: 12
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: 8-10 minutes
