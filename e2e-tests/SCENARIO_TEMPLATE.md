# Scenario X: [Scenario Title]

## 🤖 MANDATORY AI EXECUTION CONTRACT 🤖

**BEFORE EXECUTING THIS SCENARIO, YOU MUST:**

1. ✅ Read this ENTIRE scenario file from start to finish
2. ✅ Execute EVERY step in EXACT order (Step 1, 2, 3...)
3. ✅ Execute EACH step EXACTLY ONCE (no repeats unless explicitly instructed)
4. ✅ Use EXACT commands as written (no modifications, character for character)
5. ✅ Never skip steps, even if they seem unnecessary
6. ✅ Never add steps, even if they seem helpful
7. ✅ Never modify steps, even if you think there's a better way
8. ✅ Stop IMMEDIATELY when you see "SCENARIO X COMPLETED"

**EXECUTION AFFIRMATION (Type this before proceeding):**
"I will execute Scenario X: [Scenario Title] exactly as written without modification, addition, or omission"

**CONFIRMATION CHECKLIST:**
- [ ] I have read the entire scenario file
- [ ] I understand that I must execute every step exactly as written
- [ ] I will not skip, add, or modify any steps
- [ ] I will stop at scenario completion marker
- [ ] I understand that VIOLATION = COMPLETE FAILURE

**⚠️ VIOLATION = COMPLETE FAILURE**

---

## Overview

[Brief description of what this scenario tests]

## Prerequisites

**BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY:**

1. **Database State**: Both players are in `earth_arkhamcity_sanitarium_room_foyer_001`
2. **Server Running**: Development server is running on port 54731
3. **Client Accessible**: Client is accessible on port 5173
4. **Both Players Connected**: [Additional prerequisites]

**⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE**

**Reference**: See @MULTIPLAYER_TEST_RULES.md for complete prerequisite verification procedures.

## Test Configuration

- **Test Players**: ArkanWolfshade (AW) and Ithaqua
- **Starting Room**: Main Foyer (`earth_arkhamcity_sanitarium_room_foyer_001`)
- **Testing Approach**: Playwright MCP (multi-tab interaction required)
- **Timeout Settings**: Use configurable timeouts from master rules

## Execution Steps

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### STEP 1 of [N]: [Step Title]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🎯 Purpose**: [Why this step exists]
**⏱️ Expected Duration**: [Estimated time]
**🚫 DO NOT**: Skip, modify, or add additional verification

**📋 Mandatory Commands** (execute exactly as written):

```javascript
// Command 1 - [Description]
await mcp_playwright_browser_[action]({[exact parameters]});

// Command 2 - [Description]
await mcp_playwright_browser_[action]({[exact parameters]});
```

**Expected Result**: [What should happen]

**✅ Step 1 Completion Checklist:**
- [ ] Commands executed exactly as written
- [ ] Expected result observed or documented
- [ ] No errors encountered that require retry
- [ ] Ready to proceed to Step 2

**🚫 STOP! Before proceeding:**
Did you complete ALL items above? (Yes/No)
- If No: Document the issue and STOP
- If Yes: Proceed IMMEDIATELY to Step 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### STEP 2 of [N]: [Step Title]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🎯 Purpose**: [Why this step exists]
**⏱️ Expected Duration**: [Estimated time]
**🚫 DO NOT**: Skip, modify, or add additional verification

**📋 Mandatory Commands** (execute exactly as written):

```javascript
// ═══════════════════════════════════════════════════════════════
// EXECUTION GUARD: ONE ATTEMPT ONLY - DO NOT RETRY
// ═══════════════════════════════════════════════════════════════
const result = await mcp_playwright_browser_evaluate({
  function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"
});

// ═══════════════════════════════════════════════════════════════
// DECISION POINT: Process results and proceed (NO RETRY)
// ═══════════════════════════════════════════════════════════════
if (result.length === 0) {
    console.log('✅ Result: No messages found');
    console.log('✅ Action: Proceeding to next step');
    console.log('🚫 DO NOT: Retry this verification');
    // MANDATORY: Continue to next step
} else {
    console.log('✅ Result: Messages found');
    console.log('✅ Action: Proceeding to next step');
    console.log('🚫 DO NOT: Retry this verification');
    // MANDATORY: Continue to next step
}
```

**Expected Result**: [What should happen]

**✅ Step 2 Completion Checklist:**
- [ ] Commands executed exactly as written
- [ ] Expected result observed or documented
- [ ] No errors encountered that require retry
- [ ] Ready to proceed to Step 3

**🚫 STOP! Before proceeding:**
Did you complete ALL items above? (Yes/No)
- If No: Document the issue and STOP
- If Yes: Proceed IMMEDIATELY to Step 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### STEP [N]: Scenario Completion
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**🎯 Purpose**: Finalize scenario execution and prepare for next scenario
**⏱️ Expected Duration**: 30 seconds
**🚫 DO NOT**: Add additional verification or continue past this point

**📋 Mandatory Commands** (execute exactly as written):

```javascript
╔═══════════════════════════════════════════════════════════════╗
║              🎉 SCENARIO X COMPLETED 🎉                       ║
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
console.log('✅ SCENARIO X COMPLETED: [Scenario Title]');
console.log('✅ [Achievement 1]');
console.log('✅ [Achievement 2]');
console.log('✅ [Achievement 3]');
console.log('📋 PROCEEDING TO CLEANUP: Close browser tabs and stop server');

// Close all browser tabs
const tabList = await mcp_playwright_browser_tab_list();
for (let i = tabList.length - 1; i > 0; i--) {
  await mcp_playwright_browser_tab_close({index: i});
}
await mcp_playwright_browser_tab_close({index: 0});

// Wait for cleanup to complete
await mcp_playwright_browser_wait_for({time: 5});

console.log('🧹 CLEANUP COMPLETE: All browser tabs closed');
console.log('🎯 SCENARIO X STATUS: COMPLETED SUCCESSFULLY');
console.log('➡️ READY FOR: [Next Scenario Name]');
```

**Expected Result**: All browser tabs closed, scenario marked as complete, ready for next scenario

**✅ Scenario Completion Verification:**
- [ ] All browser tabs closed
- [ ] Scenario completion logged
- [ ] No additional verification performed
- [ ] Ready for cleanup procedures

**🛑 EXECUTION ENDS HERE - DO NOT PROCEED FURTHER**

---

## Expected Results

- ✅ [Expected result 1]
- ✅ [Expected result 2]
- ✅ [Expected result 3]

## Success Criteria Checklist

- [ ] [Success criterion 1]
- [ ] [Success criterion 2]
- [ ] [Success criterion 3]
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

**✅ TEMPLATE FILE**

This is a template for creating new scenarios or updating existing scenarios with improved execution guards and completion logic.

---

**Document Version**: 1.0 (Improved Execution Format)
**Last Updated**: 2025-10-07
**Scenario ID**: [XX]
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: [X-Y minutes]
