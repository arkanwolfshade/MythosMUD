# Scenario 37: Chat Message Ordering **[REQUIRES MULTI-PLAYER]**

## Overview

Tests that chat messages are delivered in the correct order to all players in the same room, and that message
 ordering is consistent across all recipients. This scenario verifies message delivery ordering and consistency in
  multiplayer scenarios.

**This is a core multi-player scenario** that requires two players to send multiple messages and verify ordering.

## Prerequisites

### BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY

1. **Database State**: Both players are in `earth_arkhamcity_sanitarium_room_foyer_001`
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **Both Players Connected**: AW and Ithaqua are both logged in and in the same room
5. **Clean State**: Both players are unmuted (no mute filters active)

### ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE

**Reference**: See @MULTIPLAYER_TEST_RULES.md for complete prerequisite verification procedures.

## Test Configuration

**Test Players**: ArkanWolfshade (AW) and Ithaqua

**Starting Room**: Main Foyer (`earth_arkhamcity_sanitarium_room_foyer_001`)

**Testing Approach**: Playwright MCP (multi-tab interaction required)

**Timeout Settings**: Use configurable timeouts from master rules

## Execution Steps

### Step 1: Clean State - Unmute Both Players

**Purpose**: Ensure clean state for message ordering testing

**Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Unmute Ithaqua to ensure clean state
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "unmute Ithaqua"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for confirmation
await mcp_playwright_browser_wait_for({text: "unmuted", time: 10});
```

**Expected Result**: Both players are unmuted and ready for message testing

### Step 2: AW Sends Sequence of Messages

**Purpose**: Test that multiple messages from one player are delivered in order

**Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Send first message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "say Message 1"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You say: Message 1", time: 10});

// Wait a moment
await mcp_playwright_browser_wait_for({time: 1});

// Send second message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "say Message 2"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You say: Message 2", time: 10});

// Wait a moment
await mcp_playwright_browser_wait_for({time: 1});

// Send third message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "say Message 3"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You say: Message 3", time: 10});
```

**Expected Result**: AW sees all three messages in order

### Step 3: Verify Ithaqua Receives Messages in Order

**Purpose**: Test that Ithaqua receives AW's messages in the correct order

**Commands**:

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Wait for all messages to arrive
await mcp_playwright_browser_wait_for({time: 5});

// Get all messages
const ithaquaMessages = await mcp_playwright_browser_evaluate({
  function: "() => Array.from(document.querySelectorAll('.message, [class*=\"message\"]')).map(el => el.textContent.trim())"
});

console.log('Ithaqua messages:', ithaquaMessages);

// Find AW's messages
const awMessages = ithaquaMessages.filter(msg => msg.includes('ArkanWolfshade says:'));
console.log('AW messages received by Ithaqua:', awMessages);

// Verify order: Message 1, Message 2, Message 3
const message1Index = awMessages.findIndex(msg => msg.includes('Message 1'));
const message2Index = awMessages.findIndex(msg => msg.includes('Message 2'));
const message3Index = awMessages.findIndex(msg => msg.includes('Message 3'));

const correctOrder = message1Index !== -1 && message2Index !== -1 && message3Index !== -1 &&
                     message1Index < message2Index && message2Index < message3Index;

console.log('Messages in correct order:', correctOrder);
console.log('Message 1 index:', message1Index);
console.log('Message 2 index:', message2Index);
console.log('Message 3 index:', message3Index);
```

**Expected Result**: Ithaqua receives all three messages in the correct order (1, 2, 3)

### Step 4: Ithaqua Sends Sequence of Messages

**Purpose**: Test message ordering from the other player

**Commands**:

```javascript
// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});

// Send first message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "say Reply 1"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You say: Reply 1", time: 10});

// Wait a moment
await mcp_playwright_browser_wait_for({time: 1});

// Send second message
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "say Reply 2"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You say: Reply 2", time: 10});
```

**Expected Result**: Ithaqua sees both reply messages in order

### Step 5: Verify AW Receives Ithaqua's Messages in Order

**Purpose**: Test that AW receives Ithaqua's messages in the correct order

**Commands**:

```javascript
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});

// Wait for all messages to arrive
await mcp_playwright_browser_wait_for({time: 5});

// Get all messages
const awMessages = await mcp_playwright_browser_evaluate({
  function: "() => Array.from(document.querySelectorAll('.message, [class*=\"message\"]')).map(el => el.textContent.trim())"
});

console.log('AW messages:', awMessages);

// Find Ithaqua's messages
const ithaquaMessages = awMessages.filter(msg => msg.includes('Ithaqua says:'));
console.log('Ithaqua messages received by AW:', ithaquaMessages);

// Verify order: Reply 1, Reply 2
const reply1Index = ithaquaMessages.findIndex(msg => msg.includes('Reply 1'));
const reply2Index = ithaquaMessages.findIndex(msg => msg.includes('Reply 2'));

const correctOrder = reply1Index !== -1 && reply2Index !== -1 && reply1Index < reply2Index;

console.log('Ithaqua messages in correct order:', correctOrder);
```

**Expected Result**: AW receives Ithaqua's messages in the correct order

### Step 6: Verify Interleaved Message Ordering

**Purpose**: Test that messages from different players maintain correct ordering

**Commands**:

```javascript
// Both players send messages rapidly
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "say Final AW"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Immediately switch to Ithaqua and send message
await mcp_playwright_browser_tab_select({index: 1});
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "say Final Ithaqua"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for messages
await mcp_playwright_browser_wait_for({time: 3});

// Check both players see messages in consistent order
// Switch to AW's tab
await mcp_playwright_browser_tab_select({index: 0});
const awFinalMessages = await mcp_playwright_browser_evaluate({
  function: "() => Array.from(document.querySelectorAll('.message, [class*=\"message\"]')).slice(-5).map(el => el.textContent.trim())"
});

// Switch to Ithaqua's tab
await mcp_playwright_browser_tab_select({index: 1});
const ithaquaFinalMessages = await mcp_playwright_browser_evaluate({
  function: "() => Array.from(document.querySelectorAll('.message, [class*=\"message\"]')).slice(-5).map(el => el.textContent.trim())"
});

console.log('AW final messages:', awFinalMessages);
console.log('Ithaqua final messages:', ithaquaFinalMessages);

// Both should see the same relative ordering of the final two messages
const awHasBoth = awFinalMessages.some(msg => msg.includes('Final AW')) &&
                  awFinalMessages.some(msg => msg.includes('Final Ithaqua'));
const ithaquaHasBoth = ithaquaFinalMessages.some(msg => msg.includes('Final AW')) &&
                       ithaquaFinalMessages.some(msg => msg.includes('Final Ithaqua'));

console.log('AW sees both final messages:', awHasBoth);
console.log('Ithaqua sees both final messages:', ithaquaHasBoth);
```

**Expected Result**: Both players see messages in consistent order

## Expected Results

✅ Messages from the same player are delivered in order

✅ Messages from different players maintain consistent ordering

✅ All players in the room receive messages in the same relative order

✅ Message delivery is reliable and consistent

## Success Criteria Checklist

[ ] AW's messages are received by Ithaqua in correct order (1, 2, 3)

[ ] Ithaqua's messages are received by AW in correct order (Reply 1, Reply 2)

[ ] Interleaved messages maintain consistent ordering for all players

[ ] Message delivery is reliable (no missing messages)

[ ] All browser operations complete without errors

[ ] Server remains stable throughout the scenario

## Cleanup

Execute standard cleanup procedures from @CLEANUP.md:

1. Close all browser tabs
2. Stop development server
3. Verify clean shutdown

## Status

**Document Version**: 1.0
**Last Updated**: 2025-01-XX
**Scenario ID**: 37
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: 5-7 minutes
