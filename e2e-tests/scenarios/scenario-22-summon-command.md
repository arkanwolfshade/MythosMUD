# Scenario 22: Administrative Summon Command **[REQUIRES MULTI-PLAYER]**

## Overview

Validates the `/summon` administrative command from end to end: parser recognition, permission gating, item instantiation, room-drop visibility, and audit messaging. Confirms non-admin rejection flow and NPC summon placeholder messaging.

**This is a core multi-player ritual** that demands two live clients to observe room updates and permissions simultaneously. Automation shortcuts are forbidden per the Master Rules.

## Prerequisites

**BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY:**

1. **Database State**
   - Item databases are initialized (`scripts/items/init_item_databases.ps1` previously executed)
   - Prototype `artifact.miskatonic.codex` exists in the catalog
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

## Execution Steps

### Step 1: Confirm Admin Status

**Purpose**: Ensure AW retains admin clearance before invoking `/summon`.

```javascript
await mcp_playwright_browser_tab_select({index: 0});
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "admin status"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "Admin privileges: Active"});
```

**Expected Result**: AW receives confirmation of active admin privileges.

### Step 2: Summon Item Prototype

**Purpose**: Validate happy-path item summoning and room-drop creation.

```javascript
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "/summon artifact.miskatonic.codex 2"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You summon 2x Codex of Whispered Secrets"});
```

**Expected Result**: AW sees success message indicating quantity and prototype ID.

### Step 3: Verify Room Drop Broadcast (Observer)

**Purpose**: Ensure nearby players see the summoned items in the room feed.

```javascript
await mcp_playwright_browser_tab_select({index: 1});
await mcp_playwright_browser_wait_for({text: "ArkanWolfshade summons 2x Codex of Whispered Secrets"});
const ithMessages = await mcp_playwright_browser_evaluate({
  function: "() => Array.from(document.querySelectorAll('.message')).map(el => el.textContent.trim())"
});
console.log("Ithaqua messages after summon:", ithMessages);
```

**Expected Result**: Ithaqua’s log contains a room message about the summon.

### Step 4: Inspect Room Drops UI (Observer)

**Purpose**: Confirm the summoned stack is present and selectable in the client.

```javascript
await mcp_playwright_browser_wait_for({text: "1. Codex of Whispered Secrets"});
await mcp_playwright_browser_wait_for({text: "Quantity: 2"});
```

**Expected Result**: Room-drop panel lists the item with matching quantity.

### Step 5: Validate Inventory Mutation Guard

**Purpose**: Ensure the summoned stack can be collected once (no duplicate tokens).

```javascript
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "pickup 1 1"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You pick up 1x Codex of Whispered Secrets"});
```

**Expected Result**: Ithaqua acquires one copy; room drop decrements to quantity 1.

### Step 6: Non-Admin Permission Check

**Purpose**: Verify that Ithaqua cannot invoke `/summon`.

```javascript
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "/summon artifact.miskatonic.codex"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "You do not currently possess the necessary administrative clearance"});
```

**Expected Result**: Permission denial message displayed to Ithaqua.

### Step 7: NPC Summon Placeholder

**Purpose**: Confirm NPC targeting returns the contextual stub response.

```javascript
await mcp_playwright_browser_tab_select({index: 0});
await mcp_playwright_browser_type({element: "Command input field", ref: "command-input", text: "/summon npc.waking_terror npc"});
await mcp_playwright_browser_press_key({key: "Enter"});
await mcp_playwright_browser_wait_for({text: "NPC summoning is not yet bound to this ritual circle"});
```

**Expected Result**: Stub guidance referencing `npc spawn` appears for AW.

### Step 8: Audit Log Verification (Optional but Recommended)

**Purpose**: Capture the admin action entry for archival review.

```javascript
await mcp_playwright_browser_tab_select({index: 0});
console.log("⛭ After scenario, inspect admin_actions_<YYYY-MM-DD>.log for summon entries.");
```

**Expected Result**: Log file contains a JSON entry detailing the summon event.

## Expected Results

- ✅ Admin privileges confirmed prior to summon
- ✅ Summon success message returned for AW
- ✅ Room-drop broadcast received by observer
- ✅ Observer can collect summoned stack without duplication
- ✅ Non-admin summon attempt rejected with lore-friendly message
- ✅ NPC summon returns the documented placeholder
- ✅ (Optional) Audit log reflects summon invocation

## Success Criteria Checklist

- [ ] Admin status verified for AW
- [ ] `/summon` command succeeds for item prototype
- [ ] Room drop displays correct quantity and metadata
- [ ] Observer inventory updates after pickup
- [ ] Non-admin summon attempt denied
- [ ] NPC summon returns placeholder guidance
- [ ] Audit log entry captured (manual verification)
- [ ] Browser tabs remain responsive throughout scenario
- [ ] Scenario execution recorded per Master Rules

## Cleanup

Execute standard cleanup from `@CLEANUP.md`:

1. Close all browser tabs opened for the scenario
2. Log out players if required by the master rules
3. Stop development server using `./scripts/stop_server.ps1` once testing concludes
4. Document results in the multiplayer testing ledger

## Status

**Drafted for Phase 3 Task 4.3** — Execute once the above prerequisites are prepared and record the outcome per project protocol.

---

**Document Version**: 1.0 (Modular E2E Test Suite)
**Last Updated**: 2025-11-12
**Scenario ID**: 22
**Testing Approach**: Playwright MCP (multi-tab required)
**Estimated Duration**: 8–10 minutes
