# Scenario LCD-01: Catatonia Grounding Ritual **[REQUIRES MULTI-PLAYER]**

## Overview

Validates the end-to-end rescue flow when an investigator becomes catatonic: the target is locked out of commands, UI
banners surface the rescue status, the rescuer channels `ground`, and both players receive synchronized feedback when
lucidity stabilizes.

## Prerequisites

Before running this scenario you MUST complete the checklist in `@MULTIPLAYER_TEST_RULES.md`. Pay special attention to:

1. **Server State** – Development server running on `54731`, client served on `5173`.

2. **Database Prep** – The players `ArkanWolfshade` (target) and `Ithaqua` (rescuer) exist in PostgreSQL database

   `mythos_e2e`.

3. **Clean Browser** – No active sessions for either account.

### lucidity Ledger Seeding

Set `ArkanWolfshade` to an induced catatonic state so the rescue flow can begin immediately.

```powershell
$env:PGPASSWORD="Cthulhu1"; psql -h localhost -U postgres -d mythos_e2e -c "UPDATE player_lucidity SET current_san =
-60, current_tier = 'catatonic', catatonia_entered_at = NOW() WHERE player_id = (SELECT player_id FROM players WHERE
name = 'ArkanWolfshade');"
```

Verify the update returned `changes = 1`. If not, halt and inspect the ledger.

## Test Configuration

**Players**: `ArkanWolfshade` (target) and `Ithaqua` (rescuer)

**Starting Room**: `earth_arkhamcity_sanitarium_room_foyer_001`

**Tools**: Playwright MCP (two tabs), PostgreSQL CLI (psql)

**Timeouts**: Apply master rule defaults (`wait_for` 10 – 30 s depending on step)

## Execution Steps

### Step 1 – Establish Target Session (Tab 0)

**Purpose**: Connect the catatonic investigator and confirm command lock.

```javascript
await mcp_playwright_browser_navigate({ url: "http://localhost:5173" });
await mcp_playwright_browser_wait_for({ text: "Username", time: 30 });
await mcp_playwright_browser_type({ element: "Username input field", ref: "e9", text: "ArkanWolfshade" });
await mcp_playwright_browser_type({ element: "Password input field", ref: "e10", text: "Cthulhu1" });
await mcp_playwright_browser_click({ element: "Login button", ref: "e11" });
await mcp_playwright_browser_wait_for({ text: "Continue", time: 30 });
await mcp_playwright_browser_click({ element: "Continue button", ref: "e59" });
await mcp_playwright_browser_wait_for({ text: "Chat", time: 30 });
```

**Verification**:

- `RescueStatusBanner` appears at the top of the terminal: `"Catatonic"` headline, purple accent.
- Command input remains visible but attempting `look` produces `"Your body lies unresponsive..."` in the Game Log.

```javascript
await mcp_playwright_browser_type({ element: "Command input", ref: "e143", text: "look", submit: true });
await mcp_playwright_browser_wait_for({ text: "unresponsive, trapped in catatonia", time: 10 });
```

### Step 2 – Connect Rescuer (Tab 1)

**Purpose**: Bring the rescuer online to initiate grounding.

```javascript
await mcp_playwright_browser_tabs({ action: "new", url: "http://localhost:5173" });
await mcp_playwright_browser_wait_for({ time: 5 });
await mcp_playwright_browser_tabs({ action: "select", index: 1 });
await mcp_playwright_browser_wait_for({ text: "Username", time: 30 });
await mcp_playwright_browser_type({ element: "Username input field", ref: "e9", text: "Ithaqua" });
await mcp_playwright_browser_type({ element: "Password input field", ref: "e10", text: "Cthulhu1" });
await mcp_playwright_browser_click({ element: "Login button", ref: "e11" });
await mcp_playwright_browser_wait_for({ text: "Continue", time: 30 });
await mcp_playwright_browser_click({ element: "Continue button", ref: "e59" });
await mcp_playwright_browser_wait_for({ text: "Chat", time: 30 });
```

**Verification**: Rescuer chat panel shows system line noting that `ArkanWolfshade` is unresponsive. If not, fetch chat
history via DOM dump and confirm presence of `[Rescue]` tag once the grounding begins (next step).

### Step 3 – Initiate Grounding

**Purpose**: Execute `ground` and observe channeling progress across both clients.

```javascript
await mcp_playwright_browser_type({ element: "Command input", ref: "e143", text: "ground ArkanWolfshade", submit: true });
await mcp_playwright_browser_wait_for({ text: "Rescue ritual", time: 15 });
```

**Expected Artifacts**:

- Rescuer tab logs `[Rescue] Rescue ritual 0% by Ithaqua` (progress increments in 10 – 25% steps).
- Target tab banner transitions to **Channeling**, shows progress meter and rescuer name.

```javascript
const rescueBanner = await mcp_playwright_browser_evaluate({
  function: "() => Array.from(document.querySelectorAll('[data-testid=\"rescue-status-banner\"]')).map(el => el.textContent)"
});
console.log("Rescue banner snapshot:", rescueBanner);
```

### Step 4 – Verify Completion

**Purpose**: Confirm LCD stabilizes and UI clears the emergency banner.

```javascript
await mcp_playwright_browser_wait_for({ text: "Rescue ritual succeeds", time: 20 });
```

- Target LCD meter updates to `1 / 100` with tier `Deranged`.
- `RescueStatusBanner` automatically dismisses within 8 s.
- Command input on Tab 0 accepts `look` successfully after dismissal.

```javascript
await mcp_playwright_browser_tabs({ action: "select", index: 0 });
await mcp_playwright_browser_wait_for({ text: "Rescue ritual succeeds", time: 5 });
await mcp_playwright_browser_wait_for({ time: 8 });
await mcp_playwright_browser_type({ element: "Command input", ref: "e143", text: "look", submit: true });
await mcp_playwright_browser_wait_for({ text: "Location:", time: 10 });
```

## Cleanup

Restore the target’s lucidity to the default lucidity to avoid cross-scenario drift.

```powershell
$env:PGPASSWORD="Cthulhu1"; psql -h localhost -U postgres -d mythos_e2e -c "UPDATE player_lucidity SET current_san = 100, current_tier = 'lucid', catatonia_entered_at = NULL WHERE player_id = (SELECT player_id FROM players WHERE name = 'ArkanWolfshade');"
```

Double-check that `RescueStatusBanner` is absent on both tabs before closing the browser. Log out both users via the UI
or simply close the tabs once verification is complete.
