# Scenario SAN-02: Sanitarium Failover Escalation **[REQUIRES MULTI-PLAYER]**

## Overview

Exercises the automatic sanitarium transfer that fires when a catatonic investigator’s SAN continues to plummet. The test validates that passive flux drives SAN below the floor, the failover hook relocates the player, and both clients surface the `"Sanitarium"` rescue outcome.

## Prerequisites

Complete the global prerequisites in `@MULTIPLAYER_TEST_RULES.md` first. Additional setup for this scenario:

1. **Server & Client** – Server listening on `54731`, client reachable on `5173`.
2. **Players** – `ArkanWolfshade` (victim) and `Ithaqua` (observer) exist in `data/local/players/local_players.db`.
3. **Clean Sessions** – No lingering browser tabs for either account.

### Sanity Ledger Seeding

Prime the victim with dangerously low SAN so passive flux can finish the collapse.

```powershell
cd E:\projects\GitHub\MythosMUD
sqlite3 data\local\players\local_players.db "
UPDATE player_sanity
   SET current_san = -95,
       current_tier = 'catatonic',
       catatonia_entered_at = datetime('now','-10 minutes')
 WHERE player_id = (
   SELECT player_id FROM players WHERE name = 'ArkanWolfshade'
 );
.quit"
```

**Why -95?** Passive flux in the sanitarium foyer drains roughly 1–2 SAN per server tick for catatonic bodies. This ensures the failover observer fires within ~2 real-time minutes.

## Test Configuration

- **Players**: Tab 0 – `ArkanWolfshade` (catatonic target), Tab 1 – `Ithaqua` (party observer)
- **Room**: `earth_arkhamcity_sanitarium_room_foyer_001`
- **Tools**: Playwright MCP with two tabs, SQLite CLI
- **Timeout Guidance**: Allow up to 180 s for the failover transition after both tabs are connected.

## Execution Steps

### Step 1 – Connect Target (Tab 0)

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

**Verification**: `RescueStatusBanner` shows `"Catatonic"` and command attempts (`look`) are rejected with the standard lockout message.

### Step 2 – Connect Observer (Tab 1)

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

Stay in Tab 1; no rescue command should be issued. The objective is to let passive flux reach the floor naturally.

### Step 3 – Monitor Passive Flux to −100 SAN

**Purpose**: Confirm SAN ticks downward and triggers failover.

1. Keep both tabs idle for up to 3 minutes. Do **not** attempt `ground` or any recovery action.
2. Optional: Every 30 s, issue `status` from Tab 1 (`/status ArkanWolfshade`) if an admin account is available, or observe the `[Sanity]` system lines on Tab 0. Each passive tick should log `Sanity loses 1 ... → -96/100 (Catatonic)` style entries.

```javascript
await mcp_playwright_browser_wait_for({ text: "Sanity loses", time: 120 });
```

### Step 4 – Validate Sanitarium Failover

When SAN reaches −100, the catatonia observer triggers the sanitarium transfer.

Expected signals on **both** tabs:

- Chat message: `[Rescue] Caretakers escort the target to Arkham Sanitarium for observation.`
- `RescueStatusBanner` transitions to the **Sanitarium** variant (amber tone) then auto-dismisses after 8 s.
- Target SAN meter jumps to `1 / 100`, tier `Deranged`.
- Target’s room data refreshes to Sanitarium recovery ward (`earth_arkhamcity_sanitarium_room_infirmary_001`).

```javascript
await mcp_playwright_browser_wait_for({ text: "Caretakers escort the target to Arkham Sanitarium", time: 60 });
```

Post-event verification on Tab 0:

```javascript
const sanitySummary = await mcp_playwright_browser_evaluate({
  function: "() => document.querySelector('[data-testid=\"sanity-meter\"]')?.textContent || ''"
});
console.log("SAN meter snapshot:", sanitySummary);
await mcp_playwright_browser_wait_for({ text: "Infirmary", time: 10 });
```

Attempt a simple command (`look`) to ensure normal interaction is restored.

### Expected Residuals

- Tab 0 game log contains both the failover message and a teleport notification describing arrival at the recovery ward.
- Tab 1 records the same `[Rescue]` line for party awareness but remains in the foyer.

## Cleanup

Reset the victim’s sanity and room placement to pre-test defaults.

```powershell
sqlite3 data\local\players\local_players.db "
WITH victim AS (
  SELECT player_id FROM players WHERE name = 'ArkanWolfshade'
)
UPDATE player_sanity
   SET current_san = 100,
       current_tier = 'lucid',
       catatonia_entered_at = NULL
 WHERE player_id = (SELECT player_id FROM victim);

UPDATE players
   SET current_room_id = 'earth_arkhamcity_sanitarium_room_foyer_001'
 WHERE player_id = (SELECT player_id FROM victim);
.quit"
```

Log out both players or close the tabs once verification is complete. Document the SAN tick timing in `TESTING_APPROACH.md` if the failover took longer than 3 minutes so future runs can adjust the wait window.
