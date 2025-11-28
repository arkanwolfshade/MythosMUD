# NPC Display Testing Guide

## Server Status
✅ **Server is RUNNING** with all fixes applied:
- UUID handling bug fixed in exploration service
- Snapshot format bug fixed - now sends structured players/npcs arrays
- Enhanced logging added for NPC queries
- Admin command created: `npc test-occupants`

## Testing Steps

### 1. Open Browser and Login
1. Navigate to: http://localhost:5173
2. Login with admin account:
   - Username: `ArkanWolfshade`
   - Password: `Cthulhu1`

### 2. Navigate to Main Foyer
The Main Foyer room is where NPCs should spawn:
- Room ID: `earth_arkhamcity_sanitarium_room_foyer_001`

You can:
- Use movement commands if already in-game
- Or use admin teleport: `/teleport earth_arkhamcity_sanitarium_room_foyer_001`

### 3. Check Room Occupants Panel
Look for the "Room Info" panel on the client. You should see:
- **Players** section: Should list players in the room
- **NPCs** section: Should list NPCs in the room

Expected NPCs in Main Foyer:
- Dr. Francis Morgan
- Sanitarium Patient (may appear multiple times)

### 4. Test Admin Command (Optional)
In the game chat, type:
```
npc test-occupants
```

Or for a specific room:
```
npc test-occupants earth_arkhamcity_sanitarium_room_foyer_001
```

This will show:
- List of players in the room
- List of NPCs in the room
- Detailed occupant information

### 5. Check Server Logs
If NPCs don't appear, check the server logs for:
- "Querying NPCs from lifecycle manager"
- "Scanning active NPCs for room match"
- "Checking NPC for room match"
- "Found NPCs in room from lifecycle manager"

## Expected Behavior

### ✅ Success Indicators:
1. NPCs appear in separate "NPCs" section in Room Info panel
2. Players appear in separate "Players" section
3. Admin command shows NPCs in the room
4. Server logs show NPC query activity

### ⚠️ If NPCs Don't Appear:
1. Check if you're in the correct room (Main Foyer)
2. Check server logs for NPC query errors
3. Verify NPCs exist using: `npc test-occupants`
4. Check warnings.log for NPC detection

## Verification from Previous Logs

Previous warnings.log showed NPCs ARE being detected:
```
npcs=['Dr. Francis Morgan', 'Sanitarium Patient', 'Sanitarium Patient']
```

This confirms:
- ✅ NPCs exist in lifecycle manager
- ✅ Query logic is working
- ✅ NPCs are being sent to clients

The fixes ensure:
- ✅ Structured format is sent (players/npcs arrays)
- ✅ Snapshot method doesn't overwrite structured data
- ✅ Client receives and displays NPCs correctly

## Files Modified

1. **server/realtime/event_handler.py**
   - Enhanced NPC query logging
   - Fixed `_send_occupants_snapshot_to_player()` to send structured format

2. **server/services/exploration_service.py**
   - Fixed UUID handling bug

3. **server/commands/npc_admin_commands.py**
   - Added `npc test-occupants` admin command

4. **server/scripts/verify_npc_occupants.py**
   - Created verification script for standalone testing
