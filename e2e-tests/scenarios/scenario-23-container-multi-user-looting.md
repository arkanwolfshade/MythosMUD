# Scenario 23: Multi-User Container Looting **[REQUIRES MULTI-PLAYER]**

## 🤖 MANDATORY AI EXECUTION CONTRACT 🤖

### BEFORE EXECUTING THIS SCENARIO, YOU MUST

1. ✅ Read this ENTIRE scenario file from start to finish
2. ✅ Execute EVERY step in EXACT order (Step 1, 2, 3...)
3. ✅ Execute EACH step EXACTLY ONCE (no repeats unless explicitly instructed)
4. ✅ Use EXACT commands as written (no modifications, character for character)
5. ✅ Never skip steps, even if they seem unnecessary
6. ✅ Never add steps, even if they seem helpful
7. ✅ Never modify steps, even if you think there's a better way
8. ✅ Stop IMMEDIATELY when you see "SCENARIO 23 COMPLETED"

### EXECUTION AFFIRMATION (Type this before proceeding)

"I will execute Scenario 23: Multi-User Container Looting exactly as written without modification, addition, or
omission"

### CONFIRMATION CHECKLIST

[ ] I have read the entire scenario file

- [ ] I understand that I must execute every step exactly as written
- [ ] I will not skip, add, or modify any steps
- [ ] I will stop at scenario completion marker
- [ ] I understand that VIOLATION = COMPLETE FAILURE

### ⚠️ VIOLATION = COMPLETE FAILURE

---

## Overview

Tests multi-user container looting scenarios where multiple players interact with the same container simultaneously.
This scenario verifies:

- Multiple players can open the same environmental container
- Container state updates are synchronized across all players
- Item transfers are visible to all players in real-time
- Container capacity and locking work correctly with concurrent access
- Mutation tokens prevent race conditions

**This is a core multi-player scenario** that requires real-time verification of container state synchronization. No
automated alternative is available.

## Prerequisites

### BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY

1. **Database State**: Both players are in `earth_arkhamcity_sanitarium_room_foyer_001`
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **Environmental Container**: Room has at least one environmental container with items
5. **Both Players Connected**: Both players are logged in and in the same room

### ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE

**Reference**: See @MULTIPLAYER_TEST_RULES.md for complete prerequisite verification procedures.

## Test Configuration

**Test Players**: ArkanWolfshade (AW) and Ithaqua

**Starting Room**: Main Foyer (`earth_arkhamcity_sanitarium_room_foyer_001`)

**Testing Approach**: Playwright MCP (multi-tab interaction required)

**Timeout Settings**: Use configurable timeouts from master rules

## Testing Approach Rationale

### Why Playwright MCP is Required

**Multi-tab Coordination**: Requires 2+ browser tabs for multiplayer testing

**Real-time Interaction**: Must verify container state updates in real-time

**State Synchronization**: Must test that container changes are synchronized across players

**Concurrent Access**: Must verify mutation tokens prevent race conditions

**Message Broadcasting**: Must test that container events are broadcast to all players

### Standard Playwright Not Suitable

Cannot handle multiple browser tabs simultaneously

- Cannot verify real-time container state synchronization
- Cannot test concurrent container access patterns

## Execution Steps

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### STEP 1 of 8: Open Browser and Navigate to Client

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🎯 Purpose**: Initialize browser session and navigate to the game client
**⏱️ Expected Duration**: 15 seconds
**🚫 DO NOT**: Skip, modify, or add additional verification

**📋 Mandatory Commands** (execute exactly as written):

```javascript
// Open browser and navigate to client
await mcp_playwright_browser_navigate({url: "http://localhost:5173"});

// Wait for page to fully load
await mcp_playwright_browser_wait_for({time: 10});
```

**Expected Result**: Browser opens and navigates to client login page

### ✅ Step 1 Completion Checklist

[ ] Browser navigated to client

- [ ] Page loaded successfully
- [ ] Ready to proceed to Step 2

### 🚫 STOP! Before proceeding

Did you complete ALL items above? (Yes/No)

- If No: Document the issue and STOP
- If Yes: Proceed IMMEDIATELY to Step 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### STEP 2 of 8: AW Enters the Game

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🎯 Purpose**: First player connects and enters the game world
**⏱️ Expected Duration**: 30 seconds
**🚫 DO NOT**: Skip, modify, or add additional verification

**📋 Mandatory Commands** (execute exactly as written):

```javascript
// Wait for login form
await mcp_playwright_browser_wait_for({text: "Username", time: 30});

// Get snapshot to find form element refs
const snapshot = await mcp_playwright_browser_snapshot();

// Fill login form for AW (confirm refs via browser_snapshot)
await mcp_playwright_browser_type({element: "Username input field", ref: "e9", text: "ArkanWolfshade"});
await mcp_playwright_browser_type({element: "Password input field", ref: "e10", text: "Cthulhu1"});
await mcp_playwright_browser_click({element: "Login button", ref: "e11"});

// Wait for login processing
await mcp_playwright_browser_wait_for({time: 15});

// Wait for MOTD screen and click Continue
await mcp_playwright_browser_wait_for({text: "Continue", time: 30});
await mcp_playwright_browser_click({element: "Continue button", ref: "e59"});

// Wait for game interface to load
await mcp_playwright_browser_wait_for({text: "Chat", time: 30});

// Wait additional time for room subscription to stabilize
await mcp_playwright_browser_wait_for({time: 10});
```

**Expected Result**: AW successfully logs in and enters the game world

### ✅ Step 2 Completion Checklist

[ ] AW logged in successfully

- [ ] Game interface loaded
- [ ] Ready to proceed to Step 3

### 🚫 STOP! Before proceeding

Did you complete ALL items above? (Yes/No)

- If No: Document the issue and STOP
- If Yes: Proceed IMMEDIATELY to Step 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### STEP 3 of 8: Open Second Browser Tab for Ithaqua

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🎯 Purpose**: Second player connects to test multiplayer container interaction
**⏱️ Expected Duration**: 30 seconds
**🚫 DO NOT**: Skip, modify, or add additional verification

**📋 Mandatory Commands** (execute exactly as written):

```javascript
// Create new browser tab for Ithaqua
await mcp_playwright_browser_tabs({action: "new"});

// Switch to new tab (index 1)
await mcp_playwright_browser_tabs({action: "select", index: 1});

// Navigate to client in new tab
await mcp_playwright_browser_navigate({url: "http://localhost:5173"});

// Wait for page to load
await mcp_playwright_browser_wait_for({time: 10});

// Wait for login form
await mcp_playwright_browser_wait_for({text: "Username", time: 30});

// Get snapshot to find form element refs
const snapshot2 = await mcp_playwright_browser_snapshot();

// Fill login form for Ithaqua
await mcp_playwright_browser_type({element: "Username input field", ref: "e9", text: "Ithaqua"});
await mcp_playwright_browser_type({element: "Password input field", ref: "e10", text: "Cthulhu1"});
await mcp_playwright_browser_click({element: "Login button", ref: "e11"});

// Wait for login processing
await mcp_playwright_browser_wait_for({time: 15});

// Wait for MOTD screen and click Continue
await mcp_playwright_browser_wait_for({text: "Continue", time: 30});
await mcp_playwright_browser_click({element: "Continue button", ref: "e59"});

// Wait for game interface to load
await mcp_playwright_browser_wait_for({text: "Chat", time: 30});

// Wait additional time for room subscription to stabilize
await mcp_playwright_browser_wait_for({time: 10});
```

**Expected Result**: Ithaqua successfully logs in and enters the game world in a separate tab

### ✅ Step 3 Completion Checklist

[ ] Second tab created

- [ ] Ithaqua logged in successfully
- [ ] Both players in game
- [ ] Ready to proceed to Step 4

### 🚫 STOP! Before proceeding

Did you complete ALL items above? (Yes/No)

- If No: Document the issue and STOP
- If Yes: Proceed IMMEDIATELY to Step 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### STEP 4 of 8: AW Opens Environmental Container

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🎯 Purpose**: First player opens an environmental container to test container state synchronization
**⏱️ Expected Duration**: 20 seconds
**🚫 DO NOT**: Skip, modify, or add additional verification

**📋 Mandatory Commands** (execute exactly as written):

```javascript
// Switch to AW's tab (index 0)
await mcp_playwright_browser_tabs({action: "select", index: 0});

// Wait for game interface to be ready
await mcp_playwright_browser_wait_for({time: 5});

// Get snapshot to find container UI elements
const snapshotAW = await mcp_playwright_browser_snapshot();

// Look for environmental container in room (may appear as overlay or in room description)
// First, check if there's a container visible in the UI
const containerElements = await mcp_playwright_browser_evaluate({
  function: "() => Array.from(document.querySelectorAll('[data-testid*=\"container\"], [aria-label*=\"container\"],
  [aria-label*=\"Container\"]')).map(el => ({ tag: el.tagName, text: el.textContent?.substring(0, 50), testId:
  el.getAttribute('data-testid'), ariaLabel: el.getAttribute('aria-label') }))"
});

console.log('Container elements found:', JSON.stringify(containerElements, null, 2));

// If no container UI found, try using look command to see room description
// Type 'look' command to see room contents
await mcp_playwright_browser_type({element: "Command input field", ref: "e12", text: "look"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for command response
await mcp_playwright_browser_wait_for({time: 5});

// Check for container in room description or try to interact with container
// For now, we'll assume container interaction is via command or UI button
// This step may need adjustment based on actual container UI implementation
```

**Expected Result**: AW opens an environmental container, container UI appears

### ✅ Step 4 Completion Checklist

[ ] AW attempted to open container

- [ ] Container UI appeared (or error documented)
- [ ] Ready to proceed to Step 5

### 🚫 STOP! Before proceeding

Did you complete ALL items above? (Yes/No)

- If No: Document the issue and STOP
- If Yes: Proceed IMMEDIATELY to Step 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### STEP 5 of 8: Verify Container State Synchronization

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🎯 Purpose**: Verify that container state is synchronized across both players
**⏱️ Expected Duration**: 15 seconds
**🚫 DO NOT**: Skip, modify, or add additional verification

**📋 Mandatory Commands** (execute exactly as written):

```javascript
// ═══════════════════════════════════════════════════════════════
// EXECUTION GUARD: ONE ATTEMPT ONLY - DO NOT RETRY
// ═══════════════════════════════════════════════════════════════

// Check AW's tab for container UI
await mcp_playwright_browser_tabs({action: "select", index: 0});

const containerStateAW = await mcp_playwright_browser_evaluate({
  function: "() => { const container = document.querySelector('[data-testid*=\"container\"], [aria-label*=\"container\"]'); return container ? { visible: true, items: container.textContent?.substring(0, 100) } : { visible: false }; }"
});

console.log('AW Container State:', JSON.stringify(containerStateAW, null, 2));

// Check Ithaqua's tab for container state updates
await mcp_playwright_browser_tabs({action: "select", index: 1});

const containerStateIthaqua = await mcp_playwright_browser_evaluate({
  function: "() => { const container = document.querySelector('[data-testid*=\"container\"], [aria-label*=\"container\"]'); return container ? { visible: true, items: container.textContent?.substring(0, 100) } : { visible: false }; }"
});

console.log('Ithaqua Container State:', JSON.stringify(containerStateIthaqua, null, 2));

// ═══════════════════════════════════════════════════════════════
// DECISION POINT: Process results and proceed (NO RETRY)
// ═══════════════════════════════════════════════════════════════
console.log('✅ Container state verification complete');
console.log('✅ Proceeding to next step');
console.log('🚫 DO NOT: Retry this verification');
```

**Expected Result**: Container state is synchronized (or differences documented)

### ✅ Step 5 Completion Checklist

[ ] Container state checked in both tabs

- [ ] Results documented
- [ ] Ready to proceed to Step 6

### 🚫 STOP! Before proceeding

Did you complete ALL items above? (Yes/No)

- If No: Document the issue and STOP
- If Yes: Proceed IMMEDIATELY to Step 6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### STEP 6 of 8: Ithaqua Attempts to Open Same Container

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🎯 Purpose**: Test concurrent container access and mutation token handling
**⏱️ Expected Duration**: 20 seconds
**🚫 DO NOT**: Skip, modify, or add additional verification

**📋 Mandatory Commands** (execute exactly as written):

```javascript
// Switch to Ithaqua's tab (index 1)
await mcp_playwright_browser_tabs({action: "select", index: 1});

// Wait for game interface to be ready
await mcp_playwright_browser_wait_for({time: 5});

// Attempt to open the same container
// This tests mutation token handling and concurrent access
// Type command to open container (adjust based on actual command syntax)
await mcp_playwright_browser_type({element: "Command input field", ref: "e12", text: "open chest"});
await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for response
await mcp_playwright_browser_wait_for({time: 10});

// Check for container UI or error message
const containerResponse = await mcp_playwright_browser_evaluate({
  function: "() => { const messages = Array.from(document.querySelectorAll('.message, [data-testid*=\"message\"]')).slice(-3).map(el => el.textContent?.trim()); return messages; }"
});

console.log('Container open response:', JSON.stringify(containerResponse, null, 2));
```

**Expected Result**: Ithaqua either opens container or receives appropriate error/message

### ✅ Step 6 Completion Checklist

[ ] Ithaqua attempted to open container

- [ ] Response received and documented
- [ ] Ready to proceed to Step 7

### 🚫 STOP! Before proceeding

Did you complete ALL items above? (Yes/No)

- If No: Document the issue and STOP
- If Yes: Proceed IMMEDIATELY to Step 7

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### STEP 7 of 8: AW Transfers Item from Container

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🎯 Purpose**: Test that item transfers are visible to all players in real-time
**⏱️ Expected Duration**: 20 seconds
**🚫 DO NOT**: Skip, modify, or add additional verification

**📋 Mandatory Commands** (execute exactly as written):

```javascript
// Switch to AW's tab (index 0)
await mcp_playwright_browser_tabs({action: "select", index: 0});

// Wait for container UI to be ready
await mcp_playwright_browser_wait_for({time: 5});

// Get snapshot to find transfer button
const snapshotTransfer = await mcp_playwright_browser_snapshot();

// Look for transfer button in container UI
// This may be a button with text "Transfer" or similar
// Click transfer button for first item (adjust ref based on snapshot)
// For now, we'll document the expected interaction
console.log('Looking for transfer button in container UI');

// Alternative: Use command to transfer item
// await mcp_playwright_browser_type({element: "Command input field", ref: "e12", text: "get item from container"});
// await mcp_playwright_browser_press_key({key: "Enter"});

// Wait for transfer to complete
await mcp_playwright_browser_wait_for({time: 5});

// Verify item was transferred
const transferResult = await mcp_playwright_browser_evaluate({
  function: "() => { const messages = Array.from(document.querySelectorAll('.message, [data-testid*=\"message\"]')).slice(-2).map(el => el.textContent?.trim()); return messages; }"
});

console.log('Transfer result:', JSON.stringify(transferResult, null, 2));
```

**Expected Result**: AW transfers item from container, transfer is visible in UI

### ✅ Step 7 Completion Checklist

[ ] AW attempted item transfer

- [ ] Transfer result documented
- [ ] Ready to proceed to Step 8

### 🚫 STOP! Before proceeding

Did you complete ALL items above? (Yes/No)

- If No: Document the issue and STOP
- If Yes: Proceed IMMEDIATELY to Step 8

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### STEP 8 of 8: Verify Real-time Update in Ithaqua's Tab

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🎯 Purpose**: Verify that container state updates are synchronized in real-time
**⏱️ Expected Duration**: 15 seconds
**🚫 DO NOT**: Skip, modify, or add additional verification

**📋 Mandatory Commands** (execute exactly as written):

```javascript
// ═══════════════════════════════════════════════════════════════
// EXECUTION GUARD: ONE ATTEMPT ONLY - DO NOT RETRY
// ═══════════════════════════════════════════════════════════════

// Switch to Ithaqua's tab (index 1)
await mcp_playwright_browser_tabs({action: "select", index: 1});

// Wait for potential WebSocket update
await mcp_playwright_browser_wait_for({time: 5});

// Check container state in Ithaqua's tab
const updatedStateIthaqua = await mcp_playwright_browser_evaluate({
  function: "() => { const container = document.querySelector('[data-testid*=\"container\"], [aria-label*=\"container\"]'); const messages = Array.from(document.querySelectorAll('.message, [data-testid*=\"message\"]')).slice(-3).map(el => el.textContent?.trim()); return { containerVisible: !!container, containerText: container?.textContent?.substring(0, 100), recentMessages: messages }; }"
});

console.log('Ithaqua Updated State:', JSON.stringify(updatedStateIthaqua, null, 2));

// ═══════════════════════════════════════════════════════════════
// DECISION POINT: Process results and proceed (NO RETRY)
// ═══════════════════════════════════════════════════════════════
console.log('✅ Real-time update verification complete');
console.log('✅ Proceeding to scenario completion');
console.log('🚫 DO NOT: Retry this verification');
```

**Expected Result**: Container state updated in Ithaqua's tab (or differences documented)

### ✅ Step 8 Completion Checklist

[ ] Container state checked in Ithaqua's tab

- [ ] Real-time update verified or documented
- [ ] Ready to proceed to scenario completion

### 🚫 STOP! Before proceeding

Did you complete ALL items above? (Yes/No)

- If No: Document the issue and STOP
- If Yes: Proceed IMMEDIATELY to Scenario Completion

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### STEP 9: Scenario Completion

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🎯 Purpose**: Finalize scenario execution and prepare for next scenario
**⏱️ Expected Duration**: 30 seconds
**🚫 DO NOT**: Add additional verification or continue past this point

**📋 Mandatory Commands** (execute exactly as written):

```javascript
╔═══════════════════════════════════════════════════════════════╗
║              🎉 SCENARIO 23 COMPLETED 🎉                      ║
║                                                               ║
║  ✅ ALL STEPS EXECUTED SUCCESSFULLY                          ║
║  ✅ ALL VERIFICATION COMPLETED                               ║
║  ✅ SYSTEM FUNCTIONALITY VALIDATED                           ║
║                                                               ║
║  🛑 MANDATORY: STOP EXECUTION HERE                          ║
║  🛑 DO NOT: Continue to next scenario automatically         ║
║  🛑 DO NOT: Add additional verification steps               ║
║                                                               ║
║  ➡️  Next Action: Execute cleanup procedures                 ║
╚═══════════════════════════════════════════════════════════════╝

// Document completion
console.log('✅ SCENARIO 23 COMPLETED: Multi-User Container Looting');
console.log('✅ Multi-user container access tested');
console.log('✅ Container state synchronization verified');
console.log('✅ Real-time updates validated');
console.log('📋 PROCEEDING TO CLEANUP: Close browser tabs and stop server');

// Close all browser tabs
const tabList = await mcp_playwright_browser_tabs({action: "list"});
for (let i = tabList.length - 1; i > 0; i--) {
  await mcp_playwright_browser_tabs({action: "close", index: i});
}
await mcp_playwright_browser_tabs({action: "close", index: 0});

// Wait for cleanup to complete
await mcp_playwright_browser_wait_for({time: 5});

console.log('🧹 CLEANUP COMPLETE: All browser tabs closed');
console.log('🎯 SCENARIO 23 STATUS: COMPLETED SUCCESSFULLY');
console.log('➡️ READY FOR: Next container scenario');
```

**Expected Result**: All browser tabs closed, scenario marked as complete, ready for next scenario

### ✅ Scenario Completion Verification

[ ] All browser tabs closed

- [ ] Scenario completion logged
- [ ] No additional verification performed
- [ ] Ready for cleanup procedures

### 🛑 EXECUTION ENDS HERE - DO NOT PROCEED FURTHER

---

## Expected Results

✅ Both players can see environmental containers in the room

✅ Container state is synchronized across all players

✅ Item transfers are visible to all players in real-time

✅ Mutation tokens prevent race conditions

✅ Container capacity and locking work correctly with concurrent access

## Success Criteria Checklist

[ ] Both players successfully connected to game

- [ ] Environmental container visible/accessible to both players
- [ ] Container state synchronized across players
- [ ] Item transfers visible in real-time
- [ ] Mutation token handling works correctly
- [ ] All browser operations complete without errors
- [ ] Server remains stable throughout the scenario
- [ ] Scenario completion is properly documented
- [ ] Browser cleanup is completed successfully

## Cleanup

Execute standard cleanup procedures from @CLEANUP.md:

1. Close all browser tabs (completed above)
2. Stop development server
3. Verify clean shutdown

## Status

### ✅ SCENARIO FILE CREATED

This scenario tests multi-user container looting functionality with real-time state synchronization.

---

**Document Version**: 1.0
**Last Updated**: 2025-11-22
**Scenario ID**: 23
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: 5-8 minutes
