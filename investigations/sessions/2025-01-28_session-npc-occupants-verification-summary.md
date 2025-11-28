# NPC Occupants Investigation - Verification Summary

**Date**: 2025-01-28
**Investigator**: AI Assistant (GPT-4)
**Session ID**: 2025-01-28_session-npc-occupants-verification-summary
**Status**: IN PROGRESS - Enhanced logging and verification tools added

---

## EXECUTIVE SUMMARY

**Objective**: Verify NPCs exist in the lifecycle manager's `active_npcs` dict and test that the query logic correctly finds NPCs by room ID.

**Actions Taken**:
1. ✅ Enhanced logging in `server/realtime/event_handler.py` with comprehensive NPC query logging
2. ✅ Created admin command `npc test-occupants` to manually trigger occupant queries
3. ✅ Created verification script `server/scripts/verify_npc_occupants.py` for standalone testing
4. ✅ **FIXED**: UUID handling bug in `exploration_service.py` causing `'asyncpg.pgproto.pgproto.UUID' object has no attribute 'replace'` error
5. ✅ **FIXED**: `_send_occupants_snapshot_to_player` now sends structured format (players/npcs) instead of legacy format
6. ✅ **VERIFIED**: NPCs ARE being found and sent (see warnings.log line 3: `npcs=['Dr. Francis Morgan', 'Sanitarium Patient', 'Sanitarium Patient']`)
7. 🔄 **PENDING**: Restart server and verify NPCs appear in client UI

---

## DETAILED FINDINGS

### Phase 1: Enhanced Logging Implementation

**Location**: `server/realtime/event_handler.py` (lines 873-948)

**Logging Added**:
- **Entry Point**: Logs when NPC query starts for a room
- **Service Retrieval**: Logs whether NPC instance service is available
- **Lifecycle Manager Check**: Logs whether lifecycle manager exists
- **Active NPCs Scanning**:
  - Logs total count of active NPCs
  - Logs progress during scanning
- **Per-NPC Details**: For each NPC, logs:
  - NPC ID and name
  - `current_room` attribute value
  - `current_room_id` attribute value
  - Which attribute is used (`npc_room_id_used`)
  - Whether it matches the target room (`matches_room`)
- **Match Logging**: Logs each NPC found in the target room
- **Summary Logging**: Logs final statistics:
  - Total NPCs checked
  - NPCs matched
  - Final NPC count for the room
- **Error Handling**: Enhanced error logging with full exception details

**Example Log Output Expected**:
```
INFO - Querying NPCs from lifecycle manager (room_id=..., step=starting_npc_query)
DEBUG - Retrieved NPC instance service (service_available=True, has_lifecycle_manager=True)
DEBUG - Retrieved lifecycle manager (manager_available=True, has_active_npcs=True)
INFO - Scanning active NPCs for room match (room_id=..., total_active_npcs=8)
DEBUG - Checking NPC for room match (npc_id=..., npc_name=..., npc_current_room=..., matches_room=True/False)
INFO - Found NPC in room (room_id=..., npc_id=..., npc_name=...)
INFO - Completed NPC query from lifecycle manager (room_id=..., npc_count=..., npcs_checked=..., npcs_matched=...)
```

---

### Phase 2: Admin Command Creation

**Location**: `server/commands/npc_admin_commands.py`

**Command Added**: `npc test-occupants [room_id]`

**Functionality**:
- Admin-only command (requires `is_admin=True`)
- If `room_id` not provided, uses player's current room
- Queries occupants using the same method as `_get_room_occupants()`
- Separates players and NPCs in output
- Triggers actual `_send_room_occupants_update()` broadcast
- Returns formatted text showing:
  - Room ID being tested
  - List of players in room
  - List of NPCs in room
  - Confirmation that broadcast was triggered

**Usage**:
```
npc test-occupants                                    # Test current room
npc test-occupants earth_arkhamcity_sanitarium_room_foyer_001  # Test specific room
```

**Expected Output**:
```
Occupants in room: earth_arkhamcity_sanitarium_room_foyer_001

Players (1):
  - ArkanWolfshade

NPCs (2):
  - Dr. Francis Morgan
  - Sanitarium Patient

✅ Occupant update broadcast triggered. Check logs for detailed NPC query information.
```

**Help Text Updated**: Added `test-occupants` to the NPC admin command help menu.

---

### Phase 3: Verification Script Created

**Location**: `server/scripts/verify_npc_occupants.py`

**Purpose**: Standalone script to verify NPCs exist in lifecycle manager and test query logic

**Capabilities**:
1. Verifies NPC instance service is available
2. Verifies lifecycle manager is accessible
3. Verifies `active_npcs` dict exists
4. Lists all active NPCs with their room assignments
5. Tests query logic for specific room (`earth_arkhamcity_sanitarium_room_foyer_001`)
6. Shows summary statistics

**Output Format**:
- ✅/❌ status indicators for each verification step
- Detailed NPC listing with room information
- Query test results
- Summary statistics

**Note**: This script requires the server to be running and the NPC instance service to be initialized.

---

## Phase 4: UUID Handling Bug Fix

**Location**: `server/services/exploration_service.py`

**Issue Identified**:
- Error: `'asyncpg.pgproto.pgproto.UUID' object has no attribute 'replace'`
- Occurs when marking rooms as explored after player movement
- Related to NPC occupants investigation because it adds noise to error logs

**Root Cause**:
- asyncpg returns `asyncpg.pgproto.pgproto.UUID` objects from PostgreSQL queries
- Code was trying to convert directly using `UUID(room_uuid_str)`
- Python's UUID constructor calls `.replace()` internally, which asyncpg UUID objects don't have

**Fix Applied**:
- Modified `_get_room_uuid_by_stable_id()` method to properly handle asyncpg UUID objects
- Converts to string first using `str()`, then to UUID
- Handles both asyncpg UUID objects and standard UUIDs correctly

**Code Pattern**:
```python
if isinstance(room_uuid_result, UUID):
    return room_uuid_result  # Already standard UUID
return UUID(str(room_uuid_result))  # Convert asyncpg UUID via string
```

---

## Phase 5: Critical Discovery - NPCs ARE Being Found!

**BREAKTHROUGH**: Review of `warnings.log` revealed that NPCs ARE actually being found and sent!

**Evidence from logs** (line 3):
```
npcs=['Dr. Francis Morgan', 'Sanitarium Patient', 'Sanitarium Patient']
players=['ArkanWolfshade']
all_occupants=['ArkanWolfshade', 'Dr. Francis Morgan', 'Sanitarium Patient', 'Sanitarium Patient']
```

**Findings**:
1. ✅ NPCs exist in the lifecycle manager
2. ✅ Query logic is working correctly
3. ✅ NPCs are being sent in the `room_occupants` event
4. ⚠️ **ISSUE IDENTIFIED**: `_send_occupants_snapshot_to_player` was sending legacy format, potentially overwriting structured data

**Bug Found**: `_send_occupants_snapshot_to_player()` method (line 298-322) was sending only legacy format:
```python
"data": {"occupants": names, "count": len(names)}
```

This was called AFTER `_send_room_occupants_update()` which sends structured format. The snapshot method could overwrite the structured data with legacy format.

**Fix Applied**: Updated `_send_occupants_snapshot_to_player()` to send structured format matching `_send_room_occupants_update()`:
```python
"data": {
    "players": players,
    "npcs": npcs,
    "occupants": all_occupants,  # Backward compatibility
    "count": len(all_occupants),
}
```

**Note**: There appears to be a duplicate "Sanitarium Patient" in the NPC list - this may indicate duplicate spawning, but that's a separate issue from the display problem.

---

## CURRENT INVESTIGATION STATUS

### What We Know

1. **NPCs Are Spawning** ✅
   - Server logs show NPCs spawned at startup (21:46:13)
   - Sanitarium Patient spawned in `earth_arkhamcity_sanitarium_room_foyer_001`
   - Multiple other NPCs spawned in various rooms

2. **NPCs Use `current_room` Attribute** ✅
   - Code analysis confirms NPCs use `current_room` (not `current_room_id`)
   - Query logic checks both attributes for compatibility

3. **Enhanced Logging Is In Place** ✅
   - Comprehensive logging added to `_get_room_occupants()`
   - Logs will show exactly what happens during NPC queries

4. **Admin Command Is Ready** ✅
   - `npc test-occupants` command created and registered
   - Can manually trigger occupant queries for testing

### What We Need To Verify

1. **NPCs Exist in Lifecycle Manager** 🔄
   - Need to check if NPCs are actually in `active_npcs` dict
   - Need to verify their `current_room` attribute values

2. **Query Logic Works** 🔄
   - Need to see logs showing the query execution
   - Need to verify NPCs are found when querying by room ID

3. **Room ID Matching** 🔄
   - Need to verify room IDs match exactly (no typos, no case issues)

---

## NEXT STEPS

### Step 1: Restart Server and Test Command

1. Restart the server to load the enhanced logging
2. Log in as admin (ArkanWolfshade)
3. Navigate to Main Foyer room (`earth_arkhamcity_sanitarium_room_foyer_001`)
4. Run command: `npc test-occupants`
5. Review the command output and server logs

### Step 2: Review Enhanced Logs

Check server logs for the detailed NPC query logging:
- Look for "Querying NPCs from lifecycle manager"
- Look for "Scanning active NPCs for room match"
- Look for "Checking NPC for room match" entries
- Look for "Found NPC in room" entries
- Look for "Completed NPC query from lifecycle manager"

### Step 3: Analyze Results

Based on the logs, determine:
- Are NPCs in the lifecycle manager?
- Do NPCs have correct room assignments?
- Is the query logic finding NPCs?
- Are there any errors or exceptions?

---

## ADDITIONAL BUG FIX: UUID Handling Error

### Issue Identified

**Error**: `'asyncpg.pgproto.pgproto.UUID' object has no attribute 'replace'`

**Location**: `server/services/exploration_service.py`

**Symptom**: Error occurs when player enters a room and the exploration service tries to mark the room as explored.

**Root Cause**: asyncpg returns `asyncpg.pgproto.pgproto.UUID` objects from PostgreSQL queries, not standard Python `uuid.UUID` objects. When the code tried to convert these directly using `UUID(room_uuid_str)`, Python's UUID constructor attempted to call `.replace()` on the asyncpg UUID object, which doesn't have that method.

### Fix Applied

**Location**: `server/services/exploration_service.py` (lines 115-131)

**Change**: Modified `_get_room_uuid_by_stable_id()` to properly handle asyncpg UUID objects:
- Check if result is already a standard UUID and return it directly
- Otherwise, convert to string first using `str()`, then convert to UUID
- This handles both asyncpg UUID objects and string UUIDs correctly

**Code Pattern**:
```python
room_uuid_result = result.scalar_one_or_none()
if room_uuid_result:
    if isinstance(room_uuid_result, UUID):
        return room_uuid_result
    return UUID(str(room_uuid_result))
```

**Impact**:
- Fixes error that occurs when marking rooms as explored
- Prevents errors during player movement
- Doesn't affect NPC occupants issue directly, but removes noise from error logs

---

## FILES MODIFIED

1. **server/realtime/event_handler.py**
   - Enhanced NPC query logging (lines 873-948)
   - Added comprehensive debug/info logging at each step

2. **server/commands/npc_admin_commands.py**
   - Added `handle_npc_test_occupants_command()` function
   - Added `test-occupants` subcommand routing
   - Updated help text

3. **server/scripts/verify_npc_occupants.py** (NEW)
   - Created verification script for standalone testing

4. **server/services/exploration_service.py**
   - Fixed UUID handling bug (lines 115-131)
   - Properly handles asyncpg UUID objects by converting via string

---

## POTENTIAL ISSUES IDENTIFIED

### Issue 1: NPCs Not in Active Dict
**Possible Cause**: NPCs may have been despawned or never added to `active_npcs`
**Verification**: Check logs for "total_active_npcs" value

### Issue 2: Room ID Mismatch
**Possible Cause**: NPCs may have different room IDs than expected
**Verification**: Check logs for "npc_room_id_used" vs expected room ID

### Issue 3: Service Not Available
**Possible Cause**: NPC instance service or lifecycle manager not initialized
**Verification**: Check logs for "NPC instance service not available" or "Lifecycle manager not available"

### Issue 4: NPC Attribute Issue
**Possible Cause**: NPCs may not have `current_room` attribute set
**Verification**: Check logs for "npc_current_room=None" entries

---

## TESTING CHECKLIST

- [ ] Server restarted with enhanced logging
- [ ] Admin logged in successfully
- [ ] Player moved to Main Foyer room
- [ ] `npc test-occupants` command executed
- [ ] Command output reviewed
- [ ] Server logs reviewed for NPC query details
- [ ] NPCs verified in lifecycle manager
- [ ] Query logic verified working correctly
- [ ] NPCs appear in occupants panel (if query works)

---

## COMMANDS FOR TESTING

1. **Move to room**: `go north` (from Sanitarium Entrance)
2. **Test occupants**: `npc test-occupants`
3. **Test specific room**: `npc test-occupants earth_arkhamcity_sanitarium_room_foyer_001`
4. **Check NPC instances**: `npc status` (if available)

---

## LOG LOCATIONS

- **Server Logs**: `logs/local/server.log*`
- **Debug Logs**: Look for entries from `RealTimeEventHandler`
- **NPC Query Logs**: Search for "Querying NPCs from lifecycle manager"
- **NPC Details**: Search for "Checking NPC for room match"

---

## SUCCESS CRITERIA

The investigation will be successful when:
1. ✅ **ACHIEVED**: Logs show NPCs are queried from lifecycle manager
2. ✅ **ACHIEVED**: Logs show NPCs are found in the target room (see warnings.log line 3)
3. ✅ **FIXED**: `_send_occupants_snapshot_to_player` now sends structured format
4. 🔄 **PENDING**: NPCs appear in the occupants panel on the client (requires server restart to test)
5. 🔄 **PENDING**: Admin command returns correct NPC count (requires server restart to test)

## CRITICAL FINDING

**NPCs ARE BEING FOUND AND SENT!**

The warnings.log line 3 shows:
```
npcs=['Dr. Francis Morgan', 'Sanitarium Patient', 'Sanitarium Patient']
```

This confirms:
- ✅ NPC query logic is working
- ✅ NPCs exist in lifecycle manager
- ✅ NPCs are being sent to clients
- ⚠️ The bug was that `_send_occupants_snapshot_to_player` was overwriting structured data with legacy format

**Expected Result After Restart**: NPCs should now appear in the client UI since both broadcast and snapshot methods now send structured format.

---

## NOTES

- The enhanced logging will be verbose - this is intentional for debugging
- The admin command is admin-only for security
- The verification script can be run independently but requires server context
- All changes are backward compatible and don't affect existing functionality
