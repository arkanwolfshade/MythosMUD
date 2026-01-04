# Scenario 31: Administrative Set Stat Command **[REQUIRES MULTI-PLAYER]**

## Overview

Validates the `admin set` administrative command from end to end: parser recognition, permission gating, stat modification, DP/MP maximum warnings, error handling, and audit logging. Confirms non-admin rejection flow and validates all stat types.

**This is a core multi-player ritual** that demands two live clients to observe stat modifications and permissions simultaneously. Automation shortcuts are forbidden per the Master Rules.

## Prerequisites

**BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY:**

1. **Database State**
   - Both players are in `earth_arkhamcity_sanitarium_room_foyer_001`
2. **Server Status**
   - Development server running via `./scripts/start_local.ps1` (One Server Rule enforced)
   - Client accessible on port **5173**
3. **Player Setup**
   - `ArkanWolfshade` (AW) logged in and flagged `is_admin = true`
   - `Ithaqua` logged in (non-admin) in the **Main Foyer** `earth_arkhamcity_sanitarium_room_foyer_001`
4. **Browser Harness**
   - Playwright MCP session using the GPT-4 agent per multiplayer rules
   - Two browser tabs already authenticated (Tab 0 = AW / Tab 1 = Ithaqua)

**⚠️ FAILURE TO CONFIRM THESE ITEMS INVALIDATES THE SCENARIO.**
Reference `@MULTIPLAYER_TEST_RULES.md` for full verification ritual.

## Test Configuration

- **Test Players**:
  - Tab 0: `ArkanWolfshade` (Admin)
  - Tab 1: `Ithaqua` (Non-Admin)
- **Starting Room**: `earth_arkhamcity_sanitarium_room_foyer_001`
- **Testing Approach**: Playwright MCP (multi-tab)
- **Timeouts**: Use global defaults from Master Rules (no ad-hoc overrides)
- **Estimated Duration**: 15-20 minutes

## Execution Steps

### Step 1: Confirm Admin Status

**Purpose**: Ensure AW retains admin clearance before invoking `admin set`.

```javascript
await mcp_playwright_browser_tab_select({index: 0});
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin status"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Admin privileges: Active"});
```

**Expected Result**: AW receives confirmation of active admin privileges.

### Step 2: Test Setting Core Attribute (STR)

**Purpose**: Validate basic stat setting functionality.

```javascript
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set STR Ithaqua 75"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's STR"});
```

**Expected Result**: AW sees success message indicating STR was set from original value to 75.

### Step 3: Test Setting Multiple Attributes

**Purpose**: Validate multiple stat modifications work correctly.

```javascript
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set CON Ithaqua 80"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's CON"});

await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set INT Ithaqua 70"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's INT"});

await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set DEX Ithaqua 65"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's DEX"});
```

**Expected Result**: All three stat modifications succeed with appropriate success messages.

### Step 4: Test Setting DP (with Maximum Warning)

**Purpose**: Validate DP setting with maximum calculation warning.

```javascript
// Default CON=50, SIZ=50, max_dp = (50+50)//5 = 20
// Setting to 25 should trigger warning
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set DP Ithaqua 25"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's DP"});
await mcp_playwright_browser_wait_for({text: "Warning"});
```

**Expected Result**: AW sees success message with warning about exceeding calculated maximum.

### Step 5: Test Setting MP (with Maximum Warning)

**Purpose**: Validate MP setting with maximum calculation warning.

```javascript
// Default POW=50, max_mp = ceil(50 * 0.2) = 10
// Setting to 15 should trigger warning
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set MP Ithaqua 15"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's MP"});
await mcp_playwright_browser_wait_for({text: "Warning"});
```

**Expected Result**: AW sees success message with warning about exceeding calculated maximum.

### Step 6: Test Setting Lucidity

**Purpose**: Validate lucidity setting via new command.

```javascript
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set LCD Ithaqua 85"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's LCD"});
```

**Expected Result**: AW sees success message indicating lucidity was set.

### Step 7: Test Setting Occult and Corruption

**Purpose**: Validate occult and corruption stat setting.

```javascript
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set Occult Ithaqua 25"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's Occult"});

await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set Corruption Ithaqua 15"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's Corruption"});
```

**Expected Result**: Both occult and corruption modifications succeed.

### Step 8: Test Case-Insensitive Stat Names

**Purpose**: Validate stat name case variations work.

```javascript
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set str Ithaqua 60"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's str"});

await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set STR Ithaqua 65"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's STR"});

await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set strength Ithaqua 70"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's strength"});
```

**Expected Result**: All case variations (lowercase, uppercase, full name) work correctly.

### Step 9: Test Non-Admin Permission Denial

**Purpose**: Verify that Ithaqua cannot invoke `admin set`.

```javascript
await mcp_playwright_browser_tab_select({index: 1});
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set STR ArkanWolfshade 50"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You do not have permission"});
await mcp_playwright_browser_tab_select({index: 0});
```

**Expected Result**: Permission denial message displayed to Ithaqua.

### Step 10: Test Invalid Stat Name

**Purpose**: Validate error handling for invalid stat names.

```javascript
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set INVALID Ithaqua 50"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Invalid stat name"});
```

**Expected Result**: Error message about invalid stat name is displayed.

### Step 11: Test Invalid Value (Non-Integer)

**Purpose**: Validate error handling for non-integer values.

```javascript
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set STR Ithaqua abc"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Invalid value"});
```

**Expected Result**: Error message about invalid value (must be integer) is displayed.

### Step 12: Test Missing Arguments

**Purpose**: Validate usage message for missing arguments.

```javascript
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set STR"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Usage"});

await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set STR Ithaqua"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Usage"});
```

**Expected Result**: Usage/error messages displayed for missing arguments.

### Step 13: Test Target Player Not Found

**Purpose**: Validate error handling for non-existent players.

```javascript
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set STR NonExistentPlayer 50"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "not found"});
```

**Expected Result**: Error message indicating player not found.

### Step 14: Test Value Out of Range (Warning)

**Purpose**: Validate warning messages for out-of-range values (but command still succeeds).

```javascript
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set STR Ithaqua 150"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's STR"});
await mcp_playwright_browser_wait_for({text: "Warning"});

await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set STR Ithaqua -10"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's STR"});
await mcp_playwright_browser_wait_for({text: "Warning"});
```

**Expected Result**: Warning messages appear but commands succeed (admin override).

### Step 15: Test Additional Stat Types

**Purpose**: Validate remaining stat types (EDU, LUCK, SIZ, POW, CHA).

```javascript
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set EDU Ithaqua 75"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's EDU"});

await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set LUCK Ithaqua 60"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's LUCK"});

await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set SIZ Ithaqua 55"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's SIZ"});

await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set POW Ithaqua 85"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's POW"});

await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin set CHA Ithaqua 90"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Set Ithaqua's CHA"});
```

**Expected Result**: All stat types can be set successfully.

### Step 16: Scenario Completion

**Purpose**: Finalize scenario execution and prepare for cleanup.

```javascript
╔═══════════════════════════════════════════════════════════════╗
║        🎉 SCENARIO 31 COMPLETED 🎉                           ║
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

console.log('✅ SCENARIO 31 COMPLETED: Admin Set Stat Command');
console.log('✅ All stat setting commands executed successfully');
console.log('✅ Permission checks verified');
console.log('✅ Warning messages validated');
console.log('✅ Error handling confirmed');
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
console.log('🎯 SCENARIO 31 STATUS: COMPLETED SUCCESSFULLY');
```

**Expected Result**: All browser tabs closed, scenario marked as complete, ready for cleanup.

## Expected Results

- ✅ Admin privileges confirmed prior to stat setting
- ✅ All stat types can be set successfully (STR, CON, INT, EDU, LUCK, DEX, SIZ, POW, CHA, DP, MP, LCD, Occult, Corruption)
- ✅ DP/MP maximum warnings appear when values exceed calculated maximums
- ✅ Value range warnings appear for out-of-range values (but commands succeed)
- ✅ Case-insensitive stat names work (uppercase, lowercase, full names)
- ✅ Non-admin set attempt denied with permission error
- ✅ Invalid stat names return appropriate error messages
- ✅ Invalid values return appropriate error messages
- ✅ Missing arguments return usage messages
- ✅ Non-existent players return "not found" error
- ✅ All error cases handled gracefully

## Success Criteria Checklist

- [ ] Admin status verified for AW
- [ ] `admin set` command succeeds for all stat types
- [ ] DP/MP maximum warnings appear when appropriate
- [ ] Value range warnings appear for out-of-range values
- [ ] Case-insensitive stat names work correctly
- [ ] Non-admin set attempt denied
- [ ] Invalid stat names return error messages
- [ ] Invalid values return error messages
- [ ] Missing arguments return usage messages
- [ ] Non-existent players return error messages
- [ ] All stat modifications persist correctly
- [ ] Audit log entries captured (manual verification)
- [ ] Browser tabs remain responsive throughout scenario
- [ ] Scenario execution recorded per Master Rules

## Cleanup

Execute standard cleanup from `@CLEANUP.md`:

1. Close all browser tabs opened for the scenario
2. Log out players if required by the master rules
3. Stop development server using `./scripts/stop_server.ps1` once testing concludes
4. Document results in the multiplayer testing ledger

## Status

**Drafted for Implementation** — Execute once the above prerequisites are prepared and record the outcome per project protocol.

---

**Document Version**: 1.0 (Modular E2E Test Suite)
**Last Updated**: 2025-01-04
**Scenario ID**: 31
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: 15-20 minutes
