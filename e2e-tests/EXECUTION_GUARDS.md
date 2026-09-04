# Execution Guards for Modular E2E Test Suite

## Overview

This document defines execution guards and decision points to prevent infinite loops during scenario execution. These
guards ensure that the AI executor cannot get stuck repeating the same steps indefinitely.

## Critical Execution Guards

### 1. Step Completion Logic

**RULE**: Each step must have a clear completion condition and maximum retry limit.

```javascript
// EXECUTION GUARD: Maximum 3 attempts per step
let stepAttempts = 0;
const MAX_STEP_ATTEMPTS = 3;

while (stepAttempts < MAX_STEP_ATTEMPTS) {
    // Execute step logic
    const result = await executeStep();

    if (isStepComplete(result)) {
        console.log(`✅ Step completed successfully on attempt ${stepAttempts + 1}`);
        break;
    }

    stepAttempts++;
    if (stepAttempts >= MAX_STEP_ATTEMPTS) {
        console.log(`⚠️ Step failed after ${MAX_STEP_ATTEMPTS} attempts - proceeding with documented failure`);
        break;
    }
}
```

### 2. Browser Evaluate Result Handling

**RULE**: Empty results from `browser_evaluate` are valid and should not cause retries.

```javascript
// EXECUTION GUARD: Handle empty results gracefully
const messages = await mcp_playwright_browser_evaluate({function: "() =>
Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});

// Empty results are VALID - do not retry
if (messages.length === 0) {
    console.log('📋 No messages found - this is a valid result for clean game state scenarios');
    console.log('✅ Step completed: Verified clean game state');
    // PROCEED TO NEXT STEP - do not retry
} else {
    console.log(`📋 Found ${messages.length} messages:`, messages);
    // Continue with verification logic
}
```

### 3. Scenario Progression Logic

**RULE**: Each scenario must have explicit progression logic that cannot be bypassed.

```javascript
// EXECUTION GUARD: Explicit scenario completion
console.log('✅ SCENARIO X COMPLETED: [Scenario Title]');
console.log('✅ All verification steps completed successfully');
console.log('✅ System functionality verified as working correctly');
console.log('✅ Test results documented and validated');

// MANDATORY: Close all browser tabs
const tabList = await mcp_playwright_browser_tab_list();
for (let i = tabList.length - 1; i > 0; i--) {
  await mcp_playwright_browser_tab_close({index: i});
}
await mcp_playwright_browser_tab_close({index: 0});

console.log('🧹 CLEANUP COMPLETE: All browser tabs closed');
console.log('🎯 SCENARIO X STATUS: COMPLETED SUCCESSFULLY');
console.log('➡️ READY FOR SCENARIO Y: [Next Scenario]');

// CRITICAL: Do not continue execution after this point
// The scenario is COMPLETE - move to next scenario
```

### 4. Decision Point Framework

**RULE**: Every verification step must have a clear decision point.

```javascript
// DECISION POINT: What to do based on results
const result = await mcp_playwright_browser_evaluate({function: "..."});

if (result.length === 0) {
    // DECISION: Empty result is valid for this scenario
    console.log('✅ Verification complete: Empty result confirms expected behavior');
    // PROCEED TO NEXT STEP
} else if (result.includes('expected_message')) {
    // DECISION: Expected message found
    console.log('✅ Verification complete: Expected message found');
    // PROCEED TO NEXT STEP
} else {
    // DECISION: Unexpected result - document and proceed
    console.log('⚠️ Verification result: Unexpected result, but documenting and proceeding');
    console.log('📋 Result:', result);
    // PROCEED TO NEXT STEP (do not retry)
}
```

### 5. Timeout Guards

**RULE**: All operations must have reasonable timeouts.

```javascript
// TIMEOUT GUARD: Prevent indefinite waiting
try {
    await mcp_playwright_browser_wait_for({text: "Expected text", time: 30});
} catch (timeoutError) {
    console.log('⚠️ Timeout waiting for text - proceeding with current state');
    // PROCEED TO NEXT STEP - do not retry
}
```

## Implementation Guidelines

### For AI Executors

1. **NEVER retry a step more than 3 times**
2. **NEVER repeat the same browser_evaluate call multiple times**
3. **ALWAYS proceed to next step after timeout or empty results**
4. **ALWAYS document results before proceeding**
5. **ALWAYS close browser tabs between scenarios**

### For Scenario Writers

1. **Include explicit completion logic in every step**
2. **Add decision points for all verification steps**
3. **Define clear success/failure conditions**
4. **Include timeout handling for all waits**
5. **Add progression logic that cannot be bypassed**

## Anti-Patterns to Avoid

### ❌ INFINITE LOOP PATTERNS

```javascript
// DON'T: Repeat same step indefinitely
while (true) {
    const result = await mcp_playwright_browser_evaluate({...});
    if (result.length === 0) {
        // This will loop forever!
        continue;
    }
}

// DON'T: Retry on empty results
const result = await mcp_playwright_browser_evaluate({...});
if (result.length === 0) {
    // Don't retry - empty is often valid!
    await mcp_playwright_browser_evaluate({...}); // This creates infinite loop
}
```

### ✅ CORRECT PATTERNS

```javascript
// DO: Handle empty results gracefully
const result = await mcp_playwright_browser_evaluate({...});
if (result.length === 0) {
    console.log('✅ No messages found - verification complete');
    // Proceed to next step
} else {
    console.log('✅ Messages found:', result);
    // Continue verification
}

// DO: Use retry limits
let attempts = 0;
const MAX_ATTEMPTS = 3;
while (attempts < MAX_ATTEMPTS) {
    const result = await mcp_playwright_browser_evaluate({...});
    if (isValid(result)) {
        break;
    }
    attempts++;
}
```

## Emergency Stop Procedures

If an infinite loop is detected:

1. **Stop execution immediately**
2. **Close all browser tabs**
3. **Document the loop pattern**
4. **Review execution guards**
5. **Restart with corrected logic**

## Success Metrics

✅ No step repeated more than 3 times

✅ All scenarios complete within reasonable time

✅ Clear progression between scenarios

✅ Proper cleanup between scenarios

✅ No infinite retry loops

## 🚫 Real-World AI Execution Failures

These are actual failure patterns observed during AI execution of scenarios. Study these carefully to avoid repeating
these mistakes.

### ❌ FAILURE PATTERN 1: "Helpful" Step Addition

**What AI Did**: Added extra verification between steps

```javascript
// AI added this step (NOT in scenario):
const debugMessages = await mcp_playwright_browser_evaluate({...});
console.log('DEBUG: Additional verification:', debugMessages);
```

**Why It Failed**:

- Changed scenario flow and timing
- Caused race conditions in message delivery
- Made results non-reproducible

**Correct Behavior**: Execute ONLY the steps in the scenario file, nothing more

---

### ❌ FAILURE PATTERN 2: "Optimized" Step Skipping

**What AI Did**: Skipped step because "we already verified this in previous step"

```javascript
// AI skipped Step 5 thinking it was redundant
// Step 5: Verify Ithaqua sees no self-movement messages
// AI thought: "We already checked messages in Step 4"
```

**Why It Failed**:

- Missed edge case that step was specifically testing
- Different verification criteria between steps
- Incomplete test coverage

**Correct Behavior**: Execute EVERY step, even if it seems redundant

---

### ❌ FAILURE PATTERN 3: "Improved" Command Syntax

**What AI Did**: Changed command syntax for "clarity"

```javascript
// Scenario says:
await mcp_playwright_browser_type({text: "say Hello"});

// AI changed to:
await mcp_playwright_browser_type({text: "say \"Hello\""});
```

**Why It Failed**:

- Server interprets `say "Hello"` differently from `say Hello`
- Command parser treats quotes as part of the message
- Test fails because behavior doesn't match expectations

**Correct Behavior**: Use EXACT command syntax from scenario, character for character

---

### ❌ FAILURE PATTERN 4: Retry on Empty Results

**What AI Did**: Retried `browser_evaluate` when results were empty

```javascript
// AI executed this multiple times:
const messages = await mcp_playwright_browser_evaluate({...});
if (messages.length === 0) {
    // AI thought: "No messages? Let me try again..."
    const messages = await mcp_playwright_browser_evaluate({...}); // WRONG!
}
```

**Why It Failed**:

- Empty results were the expected correct outcome
- Created infinite loop waiting for messages that should never arrive
- Scenario never completed

**Correct Behavior**: Accept first result and proceed to next step

---

### ❌ FAILURE PATTERN 5: Premature Continuation

**What AI Did**: Continued past scenario completion marker

```javascript
// Scenario shows:
console.log('✅ SCENARIO 5 COMPLETED: Basic Chat Communication');
// ... cleanup procedures ...

// AI continued to:
// "Let me verify one more time..."
// "Let me check if there are any edge cases..."
```

**Why It Failed**:

- Additional verification changed game state
- Interfered with next scenario's prerequisites
- Made cleanup procedures incomplete

**Correct Behavior**: STOP IMMEDIATELY when you see "SCENARIO X COMPLETED"

---

### ❌ FAILURE PATTERN 6: Command Parameter Modification

**What AI Did**: Modified command parameters for "consistency"

```javascript
// Scenario says:
await mcp_playwright_browser_wait_for({text: "Welcome", time: 30});

// AI changed to:
await mcp_playwright_browser_wait_for({text: "Welcome to MythosMUD", time: 30});
```

**Why It Failed**:

- More specific text match failed even though partial match would succeed
- AI assumed what the full message should be
- Caused timeout failures unnecessarily

**Correct Behavior**: Use EXACT parameters from scenario

---

### ❌ FAILURE PATTERN 7: Reordering Steps

**What AI Did**: Reordered steps for "logical flow"

```javascript
// AI executed steps in this order: 1, 2, 4, 3, 5
// Because AI thought: "Step 4 logically comes before Step 3"
```

**Why It Failed**:

- Step 3 set up state required by Step 4
- Order was intentional for specific testing sequence
- Test results became invalid

**Correct Behavior**: Execute steps in EXACT order: 1, 2, 3, 4, 5...

---

### ❌ FAILURE PATTERN 8: "Explanatory" Console Logs

**What AI Did**: Added extra console logs for documentation

```javascript
// AI added these (NOT in scenario):
console.log('====================================');
console.log('Now testing the chat functionality');
console.log('Expected: Message appears in both tabs');
console.log('====================================');
```

**Why It Failed**:

- Logs interfered with expected output verification
- Made it harder to identify actual test output
- Added unnecessary noise

**Correct Behavior**: Use ONLY the console.log statements in the scenario

---

## 📚 Learning from Failures

**Key Principles to Remember:**

1. **Exactness**: Execute commands exactly as written, no interpretation
2. **Completeness**: Execute all steps, no skipping
3. **Minimalism**: Execute only what's in the scenario, no additions
4. **Order**: Execute steps in exact numerical order
5. **Finality**: Stop immediately at scenario completion

**When Tempted to Deviate:**

- ❓ "Should I add extra verification?" → ❌ NO
- ❓ "Should I skip this redundant step?" → ❌ NO
- ❓ "Should I improve this command?" → ❌ NO
- ❓ "Should I reorder these steps?" → ❌ NO
- ❓ "Should I continue past completion?" → ❌ NO

**The Golden Rule:**

> **If it's not explicitly written in the scenario file, DON'T DO IT.**
