# Test Results: Scenario 01 - Basic Connection (RERUN)

**Test Date**: 2025-12-02
**Status**: FAILED (Critical Bugs Found)

## Execution Summary

✅ Tab management working correctly (Playwright MCP)

✅ Both players successfully logged in

✅ Both players successfully connected to game world

✅ Player synchronization working (both see each other in occupants panel)

❌ **BUG #1**: Players started in wrong room (Sanitarium Entrance instead of Main Foyer)

- ❌ **BUG #2**: Connection messages not being displayed/broadcast

## Issues Found

### BUG #1: Wrong Starting Room

**Expected**: Both players should start in `earth_arkhamcity_sanitarium_room_foyer_001` (Main Foyer)
**Actual**: Both players started in `earth_arkhamcity_sanitarium_room_foyer_entrance` (Sanitarium Entrance)

**Database State Before Test**:

- Verified: Both players set to Main Foyer in database

- SQL executed: `UPDATE players SET current_room_id = 'earth_arkhamcity_sanitarium_room_foyer_001' WHERE name IN

  ('ArkanWolfshade', 'Ithaqua');`

- Database verification: Both players confirmed in Main Foyer

**Observation**:

- Both AW and Ithaqua spawned in Sanitarium Entrance despite database configuration

- This suggests player room assignment is being overridden during login/spawn

- Possible causes:

  1. Default spawn logic overrides database room
  2. Room validation/reset on connection
  3. Entrance room is hardcoded as default starting location

**Impact**: HIGH - E2E tests cannot reliably place players in specific rooms

### BUG #2: Connection Messages Not Displayed

**Expected**: AW should see "Ithaqua has entered the game" message in chat
**Actual**: AW's chat panel shows "(0 messages)" - no connection message received

**Observations**:

- AW's chat messages panel is empty (0 messages)

- AW's Game Info panel shows game ticks and NPC movements

- Ithaqua's occupants panel shows both players correctly synchronized

- Connection message broadcasting system may be:

  1. Not sending messages
  2. Sending but not displaying in chat panel
  3. Filtered out by chat channel settings

**Impact**: MEDIUM - Connection/disconnection messaging is a core multiplayer feature

## Test Execution Details

### Step 1: Browser Navigation

✅ Successfully opened browser and navigated to client

### Step 2: AW Login

✅ Successfully logged in as ArkanWolfshade

✅ Successfully entered game world

❌ AW spawned in wrong room (Sanitarium Entrance)

### Step 3: Ithaqua Login

✅ Successfully opened second browser tab

✅ Successfully logged in as Ithaqua

✅ Successfully entered game world

❌ Ithaqua spawned in wrong room (Sanitarium Entrance)

✅ Both players see each other in occupants panel

### Step 4: Connection Message Verification

❌ AW did not receive "Ithaqua has entered the game" message

✅ Both players are in same room (enables visibility)

✅ Occupants panel correctly shows both players

## Additional Observations

Player synchronization is working (occupants panel shows correct state)

- Game ticks and NPC movement messages are working
- Chat panel message display may have issues (0 messages shown)

## Next Steps

1. **Investigate Room Assignment**:

   - Find where player spawn location is determined
   - Check if default room logic overrides database settings
   - Verify room assignment happens before/after database load

2. **Investigate Connection Messages**:

   - Check connection message broadcasting logic
   - Verify chat panel message rendering
   - Check if messages are filtered by channel settings

3. **Continue Scenario Execution**:

   - Complete remaining steps of scenario-01
   - Document all findings before proceeding to other scenarios
