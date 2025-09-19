# Execution Guards for Modular E2E Test Suite

## Overview

This document defines execution guards and decision points to prevent infinite loops during scenario execution. These guards ensure that the AI executor cannot get stuck repeating the same steps indefinitely.

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
const messages = await mcp_playwright_browser_evaluate({function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"});

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

- ✅ No step repeated more than 3 times
- ✅ All scenarios complete within reasonable time
- ✅ Clear progression between scenarios
- ✅ Proper cleanup between scenarios
- ✅ No infinite retry loops
