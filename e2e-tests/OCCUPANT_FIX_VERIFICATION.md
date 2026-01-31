# Occupant Panel Fix – Verification Steps

Verify that the entering player sees existing room occupants using the local server and test accounts from [MULTIPLAYER_TEST_RULES.md](./MULTIPLAYER_TEST_RULES.md).

## Test Accounts (from MULTIPLAYER_TEST_RULES.md)

- **ArkanWolfshade** (AW) – password: `Cthulhu1`, Character: ArkanWolfshade  
- **Ithaqua** – password: `Cthulhu1`, Character: Ithaqua  

**Note:** For local server, ensure these users exist in your DB (e.g. run DB verification from MULTIPLAYER_TEST_RULES Step 2 if using `mythos_e2e`).

## Prerequisites

1. **Stop any running server:** `.\scripts\stop_server.ps1`
2. **Start environment:** `.\dev.bat` (or `.\scripts\start_local.ps1`)
3. Wait ~15 seconds for server and client to be ready.

## Manual Verification (two browsers/tabs)

### Tab 1 – Player already in room (ArkanWolfshade)

1. Open `http://localhost:5173`
2. Log in: **ArkanWolfshade** / **Cthulhu1**
3. If character selection appears, choose **ArkanWolfshade**, then Continue
4. Wait for game UI; ensure you are in a room (e.g. Main Foyer)
5. Leave this tab open (Player A stays in room)

### Tab 2 – Entering player (Ithaqua)

1. Open a **new** tab (or incognito): `http://localhost:5173`
2. Log in: **Ithaqua** / **Cthulhu1**
3. If character selection appears, choose **Ithaqua**, then Continue
4. Wait for game UI
5. Move Ithaqua into the **same room** as ArkanWolfshade (e.g. same room name / use `go` commands until both are in the same room)

### Verify the fix

- **On Tab 2 (Ithaqua – entering player):** Open the **Occupants** panel.  
  **Pass:** ArkanWolfshade is listed under Players.  
  **Fail:** Occupants panel is empty or does not show ArkanWolfshade.

- **On Tab 1 (ArkanWolfshade):** Open the **Occupants** panel.  
  **Pass:** Ithaqua is listed (existing behavior).

## Playwright MCP verification (when browser launches)

If Playwright MCP launches successfully:

1. `browser_navigate` → `http://localhost:5173`
2. Log in as **ArkanWolfshade** / **Cthulhu1**, handle character selection, click Continue
3. `browser_snapshot` to confirm game UI and note room
4. Open a **new** tab (or new context), `browser_navigate` → `http://localhost:5173`
5. Log in as **Ithaqua** / **Cthulhu1**, handle character selection, click Continue
6. Move Ithaqua to the same room (e.g. type movement command)
7. `browser_snapshot` on the Ithaqua tab and confirm the Occupants panel shows **ArkanWolfshade**

## Fix summary

- **Server:** Sends `room_occupants` → `room_update` (with occupants) → `room_occupants` again to the entering player so the client has two chances to apply occupant data.
- **Client:** Uses payload occupants in `handleRoomUpdate` (initial and merge branches) and preserves non-empty occupants in `mergeOccupantData` when the incoming room has no occupant data.

## If Playwright fails to launch

Error such as `browserType.launchPersistentContext: Failed to launch the browser process` / "Opening in existing browser session" then exit usually means:

- Another Chrome instance is using the Playwright profile, or
- The MCP browser context is conflicting.

Try closing any browser launched by Playwright MCP, then run the manual verification above in normal Chrome.
