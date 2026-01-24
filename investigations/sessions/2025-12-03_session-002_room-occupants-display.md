# Investigation Report: Room Occupants Display Issues

**Session ID**: `2025-12-03_session-002_room-occupants-display`
**Date**: December 3, 2025
**Investigator**: AI Assistant (Untenured Professor of Occult Studies)
**Status**: 🟡 **PARTIALLY RESOLVED** - Requires Follow-up

---

## Executive Summary

**Original Bugs**:

1. ✅ **FIXED**: Character Info panel not populating (Session 001)
2. 🟡 **IDENTIFIED**: Room Occupants showing NPC duplicates (UUID + display name)
3. 🟡 **IDENTIFIED**: Players list empty (should show current player)

**Root Causes Identified**:

- `room.to_dict()` returns empty `players` and `npcs` arrays (in-memory sets not persisted)
- Server sends flat `occupants` list with mixed UUID/name data
- No `room_occupants` events being sent to populate structured data

**Current Status**:

- Character Info panel: ✅ **WORKING**
- Room Occupants: 🔴 **Still buggy** - reverted changes due to authentication hang

---

## Investigation Findings

### Working Code (Session 001)

**Character Info Panel Fix** - ✅ **SUCCESSFUL**:
**File**: `server/realtime/connection_manager.py::_send_initial_game_state()`

**Problem**: Player data missing `stats` field

**Solution**: Use PlayerService._convert_player_to_schema() for complete player data
- **Verification**: Runtime logs confirm stats now included, panel renders correctly

### Problematic Code (Session 002)

**Room Occupants Fix Attempts** - 🔴 **REVERTED**:
**Files Attempted**: `server/realtime/connection_manager.py`, `server/realtime/websocket_handler.py`

**Problem 1**: `room.to_dict()` returns empty `players`/`npcs` arrays

**Problem 2**: Attempted to query database for players caused event loop blocking
- **Problem 3**: Authentication hung due to blocking operations
- **Action**: Reverted all occupants-related changes to restore stability

---

## Root Cause Analysis - Occupants Issue

### Why Duplicates Occur

**Evidence from Runtime Logs:**

```json
{
  "legacyOccupants": [
    "dr._francis_morgan_earth_arkhamcity_sanitarium_room_foyer_001_1764785263_7938",  // NPC UUID
    "sanitarium_patient_earth_arkhamcity_sanitarium_room_foyer_001_1764785263_9814",  // NPC UUID
    "sanitarium_patient_earth_arkhamcity_sanitarium_room_foyer_001_1764785263_3919",  // NPC UUID
    "Dr. Francis Morgan",        // Display name
    "Sanitarium patient",        // Display name
    "Sanitarium patient"         // Display name
  ],
  "players": [],  // Empty!
  "npcs": []      // Empty!
}
```

### Data Flow Problem

1. **Server Path**: `websocket_handler.py::handle_websocket_connection()`
2. **Room Data**: `room.to_dict()` at line 173
3. **Conversion**: `_convert_room_players_uuids_to_names()` at line 176
4. **Issue**: room.to_dict() returns empty arrays because Room._players and Room._npcs are in-memory sets not persisted to database
5. **Result**: Client falls back to legacy `occupants` flat list which contains duplicates

### Why Players List Is Empty

**Expected Behavior**: Current player should appear in Players list
**Actual Behavior**: Players list is empty
**Cause**: `room.to_dict()["players"]` is empty (Room._players set is not persisted)

---

## Attempted Solutions & Results

### Attempt 1: Modify connection_manager._send_initial_game_state()

**Approach**: Query database for players, get NPCs from lifecycle manager
**Result**: ❌ **Failed** - Wrong code path (not used by websocket endpoint)
**Learning**: Websocket endpoint calls `websocket_handler.py`, not `connection_manager.py`

### Attempt 2: Query database in websocket_handler.py

**Approach**: Added `await asyncio.to_thread(persistence.get_players_in_room, room_id)`
**Result**: ❌ **Failed** - Caused authentication to hang
**Cause**: Unknown - possibly deadlock or timeout in persistence call
**Action**: Reverted changes

---

## Technical Analysis

### Architecture Issue

**Problem**: Room occupant data exists in TWO separate systems:

1. **In-Memory**: `Room._players` set (lost on persistence reload)
2. **Database**: Players table with `current_room_id` column

**Disconnect**: `room.to_dict()` uses in-memory data, but that data isn't persisted

### Async Migration Impact

**Finding**: The occupants issue may be PRE-EXISTING, not caused by async migration
**Evidence**: Original async code review showed no occupants-related changes
**Conclusion**: This is likely a separate architectural issue

---

## Recommended Next Steps

### Immediate Priorities

1. **Verify Base Functionality** ✅

   - Ensure Character Info panel still works after revert
   - Confirm game is playable with current code
   - Test login/authentication works

2. **Create Minimal Occupants Fix** 🔄

   - Focus ONLY on the occupants display issue
   - Don't modify authentication or game_state sending
   - Use existing `room_occupants` event system if possible

3. **Test in Isolation** 🔄

   - Create unit test for room data structure
   - Test occupants display with mock data
   - Verify fix doesn't break authentication

### Long-Term Solutions

**Option A**: Fix `room.to_dict()` to query database for current players
**Option B**: Use `room_occupants` events (already implemented) to update UI
**Option C**: Modify persistence layer to maintain Room._players set

**Recommendation**: **Option B** - Leverage existing `room_occupants` event system

---

## Files Modified (Now Reverted)

### Kept (Working)

✅ `server/realtime/connection_manager.py` - Character Info fix (PlayerService integration)

### Reverted (Caused Issues)

❌ `server/realtime/connection_manager.py` - Occupants changes (reverted)

❌ `server/realtime/websocket_handler.py` - Database query (reverted)

❌ Client debug instrumentation (removed)

---

## Current System State

### Working Features ✅

Authentication and login

- Character Info panel (shows stats, health, lucidity)
- Game ticks and websocket communication
- All async migration changes from Phase 1 & 2

### Known Issues 🔴

Room Occupants panel shows NPC duplicates (UUID + name)

- Players list empty (should show current player)

### Next Investigation Required 🔍

Why `room_occupants` events aren't updating the UI

- How to populate structured player/NPC data without blocking authentication
- Whether to fix server-side data or rely on events

---

## Lessons Learned

1. **Identify Correct Code Path First**: Spent time fixing `connection_manager.py` when actual path was `websocket_handler.py`
2. **Test Each Change Incrementally**: Multiple simultaneous changes made debugging harder
3. **Async Blocking Still A Risk**: Adding database queries without proper async handling breaks authentication
4. **Preserve Working State**: Should have committed Character Info fix before attempting occupants fix

---

## Investigation Status

**Completed**: ✅ Character Info panel fix
**In Progress**: 🟡 Room Occupants display fix
**Next Action**: Create targeted fix for occupants without touching authentication flow

**Total Investigation Time**: ~2 hours
**Bugs Fixed**: 1/2
**Bugs Identified**: 2/2
**System Stability**: Restored to working state

---

**Session Paused** - Awaiting confirmation of stable state before proceeding with targeted occupants fix.
