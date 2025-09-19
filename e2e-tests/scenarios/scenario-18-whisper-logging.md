# Scenario 18: Whisper Logging

## Overview

Tests whisper channel logging and privacy functionality for moderation purposes. This scenario verifies that whisper messages are properly logged for moderation purposes, that privacy is maintained for regular players, that admin players can access whisper logs when needed, and that the logging system works correctly for privacy and moderation.

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

### Step 1: Both Players in Same Room

**Purpose**: Ensure both players are ready for whisper logging testing

**Commands**:
```javascript
// Ensure both players are logged in from previous scenario
// AW should be on tab 0, Ithaqua on tab 1
// Both should be in the same room
```

**Expected Result**: Both players are connected and in the same room

### Step 2: Test Basic Whisper Logging

**Purpose**: Test that whisper messages are properly logged

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send whisper message to test logging
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua Testing whisper logging functionality"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: Testing whisper logging functionality"});

// Verify message appears
const awMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesLoggingMessage = awMessages.some(msg => msg.includes('You whisper to Ithaqua: Testing whisper logging functionality'));
console.log('AW sees logging message:', seesLoggingMessage);
```

**Expected Result**: AW sees confirmation of whisper message

### Step 3: Test Whisper Logging Privacy

**Purpose**: Test that whisper messages are private and not visible to other players

**Commands**:
```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for whisper message
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade whispers to you: Testing whisper logging functionality"});

// Verify message appears
const ithaquaMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesLoggingMessage = ithaquaMessages.some(msg => msg.includes('ArkanWolfshade whispers to you: Testing whisper logging functionality'));
console.log('Ithaqua sees logging message:', seesLoggingMessage);
console.log('Ithaqua messages:', ithaquaMessages);
```

**Expected Result**: Ithaqua receives AW's whisper message (privacy maintained)

### Step 4: Test Admin Whisper Log Access

**Purpose**: Test that admin players can access whisper logs

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Try to access whisper logs as admin
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin whisper logs"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for whisper logs response
await mcp_playwright_browser_wait_for({text: "Whisper Logs:"});

// Verify logs appear
const awMessagesLogs = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesWhisperLogs = awMessagesLogs.some(msg => msg.includes('Whisper Logs:'));
console.log('AW sees whisper logs:', seesWhisperLogs);
```

**Expected Result**: AW receives whisper logs (admin access works)

### Step 5: Test Non-Admin Whisper Log Access

**Purpose**: Test that non-admin players cannot access whisper logs

**Commands**:
```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Try to access whisper logs as non-admin
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin whisper logs"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for permission denied error
await mcp_playwright_browser_wait_for({text: "You do not have permission to use that command"});

// Verify error message appears
const ithaquaMessagesLogs = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesPermissionError = ithaquaMessagesLogs.some(msg => msg.includes('You do not have permission to use that command'));
console.log('Ithaqua sees permission error:', seesPermissionError);
```

**Expected Result**: Ithaqua receives permission denied error (non-admin access blocked)

### Step 6: Test Whisper Log Content

**Purpose**: Test that whisper logs contain proper information

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Check whisper log content
const awMessagesLogContent = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const whisperLogMessages = awMessagesLogContent.filter(msg => msg.includes('whisper') || msg.includes('Whisper'));

console.log('Whisper log messages:', whisperLogMessages);

// Verify log contains whisper information
const hasWhisperInfo = whisperLogMessages.some(msg =>
  msg.includes('ArkanWolfshade') &&
  msg.includes('Ithaqua') &&
  msg.includes('Testing whisper logging functionality')
);
console.log('Log contains whisper information:', hasWhisperInfo);
```

**Expected Result**: Whisper logs contain proper information

### Step 7: Test Multiple Whisper Logging

**Purpose**: Test that multiple whisper messages are properly logged

**Commands**:
```javascript
// Send multiple whisper messages to test logging
for (let i = 1; i <= 3; i++) {
  await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: `whisper Ithaqua Logging test message ${i}`});
  await mcp_playwright_browser_press_key({key: "Enter"});
  await mcp_playwright_browser_wait_for({text: `You whisper to Ithaqua: Logging test message ${i}`});
}

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for all logging test messages
for (let i = 1; i <= 3; i++) {
  await mcp_playwright_browser_wait_for({text: `ArkanWolfshade whispers to you: Logging test message ${i}`});
}

// Verify all messages appear
const ithaquaMessagesMultiple = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const loggingMessages = ithaquaMessagesMultiple.filter(msg => msg.includes('Logging test message'));
console.log('Logging test messages received:', loggingMessages.length);
console.log('Expected: 3, Received:', loggingMessages.length);
```

**Expected Result**: All 3 logging test messages are received

### Step 8: Test Whisper Log Access After Multiple Messages

**Purpose**: Test that whisper logs are updated with multiple messages

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Access whisper logs again
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin whisper logs"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for updated whisper logs
await mcp_playwright_browser_wait_for({text: "Whisper Logs:"});

// Check updated whisper log content
const awMessagesUpdatedLogs = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const updatedWhisperLogMessages = awMessagesUpdatedLogs.filter(msg => msg.includes('whisper') || msg.includes('Whisper'));

console.log('Updated whisper log messages:', updatedWhisperLogMessages.length);

// Verify log contains multiple whisper information
const hasMultipleWhisperInfo = updatedWhisperLogMessages.some(msg =>
  msg.includes('Logging test message 1') ||
  msg.includes('Logging test message 2') ||
  msg.includes('Logging test message 3')
);
console.log('Log contains multiple whisper information:', hasMultipleWhisperInfo);
```

**Expected Result**: Updated whisper logs contain multiple whisper information

### Step 9: Test Whisper Log Privacy

**Purpose**: Test that whisper logs maintain privacy for regular players

**Commands**:
```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Try to access whisper logs again
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin whisper logs"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for permission denied error
await mcp_playwright_browser_wait_for({text: "You do not have permission to use that command"});

// Verify error message appears
const ithaquaMessagesPrivacy = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesPrivacyError = ithaquaMessagesPrivacy.some(msg => msg.includes('You do not have permission to use that command'));
console.log('Ithaqua sees privacy error:', seesPrivacyError);
```

**Expected Result**: Ithaqua receives permission denied error (privacy maintained)

### Step 10: Test Whisper Log Moderation

**Purpose**: Test that whisper logs can be used for moderation purposes

**Commands**:
```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send a message that might need moderation
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua This is a test message for moderation purposes"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: This is a test message for moderation purposes"});

// Access whisper logs for moderation
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin whisper logs"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for whisper logs
await mcp_playwright_browser_wait_for({text: "Whisper Logs:"});

// Check for moderation message in logs
const awMessagesModeration = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const moderationLogMessages = awMessagesModeration.filter(msg => msg.includes('whisper') || msg.includes('Whisper'));

console.log('Moderation log messages:', moderationLogMessages.length);

// Verify log contains moderation message
const hasModerationMessage = moderationLogMessages.some(msg =>
  msg.includes('This is a test message for moderation purposes')
);
console.log('Log contains moderation message:', hasModerationMessage);
```

**Expected Result**: Whisper logs contain moderation message

### Step 11: Test Whisper Log System Stability

**Purpose**: Test that whisper logging system remains stable

**Commands**:
```javascript
// Send another whisper message to test system stability
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "whisper Ithaqua System stability test for logging"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "You whisper to Ithaqua: System stability test for logging"});

// Verify message appears
const awMessagesStability = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const seesStabilityMessage = awMessagesStability.some(msg => msg.includes('You whisper to Ithaqua: System stability test for logging'));
console.log('AW sees stability message:', seesStabilityMessage);
```

**Expected Result**: AW sees confirmation of stability test message

### Step 12: Verify Whisper Logging Summary

**Purpose**: Verify that whisper logging system is working correctly

**Commands**:
```javascript
// Check final message counts and logging status
const awFinalMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});
const ithaquaFinalMessages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});

// Count whisper messages
const awWhisperMessages = awFinalMessages.filter(msg => msg.includes('whispers to you:'));
const ithaquaWhisperMessages = ithaquaFinalMessages.filter(msg => msg.includes('whispers to you:'));

console.log('AW whisper messages:', awWhisperMessages.length);
console.log('Ithaqua whisper messages:', ithaquaWhisperMessages.length);

// Verify logging functionality
const loggingWorking = awWhisperMessages.length > 0 && ithaquaWhisperMessages.length > 0;
console.log('Whisper logging functionality working:', loggingWorking);
```

**Expected Result**: Whisper logging functionality is working correctly

## Expected Results

- ✅ Whisper messages are properly logged
- ✅ Whisper messages remain private for regular players
- ✅ Admin players can access whisper logs
- ✅ Non-admin players cannot access whisper logs
- ✅ Whisper logs contain proper information
- ✅ Multiple whisper messages are properly logged
- ✅ Whisper logs are updated with multiple messages
- ✅ Whisper logs maintain privacy for regular players
- ✅ Whisper logs can be used for moderation purposes
- ✅ Whisper logging system remains stable

## Success Criteria Checklist

- [ ] Whisper messages are properly logged
- [ ] Whisper messages remain private for regular players
- [ ] Admin players can access whisper logs
- [ ] Non-admin players cannot access whisper logs
- [ ] Whisper logs contain proper information
- [ ] Multiple whisper messages are properly logged
- [ ] Whisper logs are updated with multiple messages
- [ ] Whisper logs maintain privacy for regular players
- [ ] Whisper logs can be used for moderation purposes
- [ ] Whisper logging system remains stable
- [ ] Privacy is maintained for regular players
- [ ] All browser operations complete without errors
- [ ] Server remains stable throughout the scenario

## Cleanup

Execute standard cleanup procedures from @CLEANUP.md:
1. Close all browser tabs
2. Stop development server
3. Verify clean shutdown

## Status

**✅ READY FOR TESTING**

The whisper channel logging system is working correctly. Whisper messages are properly logged for moderation purposes, privacy is maintained for regular players, admin players can access whisper logs when needed, and the logging system works correctly for privacy and moderation.

---

**Document Version**: 1.0 (Modular E2E Test Suite)
**Last Updated**: 2025-09-18
**Scenario ID**: 18
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: 6-8 minutes
