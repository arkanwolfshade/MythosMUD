# REMEDIATION IMPLEMENTATION: NPCs Not Updating in Occupants List

**Date**: 2025-01-30
**Investigation Session**: 2025-01-30_session-001_npcs-not-updating-on-player-movement
**Status**: Remediation Implemented

---

## SUMMARY OF FIXES

This document describes the remediation fixes implemented to resolve the issue where NPCs in the Occupants list were not updating when players moved to other rooms.

---

## CHANGES IMPLEMENTED

### 1. Enhanced Logging in Player Entry Handler

**File**: `server/realtime/event_handler.py:466-482`

**Changes**:
- Added detailed logging when sending occupants snapshot to entering player
- Added debug logging after snapshot is sent successfully
- Improved error context in logging

**Purpose**: Track NPC query execution during player movement to identify any issues with personal message delivery.

### 2. Enhanced NPC Query Logging and Validation

**File**: `server/realtime/event_handler.py:319-406` (specifically `_send_occupants_snapshot_to_player`)

**Changes**:
- Added logging before querying room occupants
- Added validation to count NPCs and players in snapshot
- Added warning if no NPCs are included in snapshot
- Added debug logging when NPCs are successfully included
- Enhanced error logging with full exception context

**Purpose**: Ensure NPCs are always included in personal messages to entering players and provide visibility into any failures.

### 3. Canonical Room ID Normalization

**File**: `server/realtime/event_handler.py:957-1046` (specifically `_get_room_occupants`)

**Changes**:
- Added canonical room ID resolution for consistent comparison
- Enhanced NPC room matching to check both original and canonical room IDs
- Added tracking of NPCs without room tracking attributes
- Added warning when NPCs exist but none match the room (potential format mismatch)
- Enhanced logging with canonical room ID information

**Purpose**: Ensure room ID format consistency when matching NPCs to rooms, preventing mismatches due to string vs canonical ID differences.

### 4. NPC Room Tracking Validation

**File**: `server/npc/lifecycle_manager.py:415-442`

**Changes**:
- Changed from conditional setting to always setting `current_room` and `current_room_id`
- Added validation to verify room tracking was set correctly
- Added error logging if room tracking fails
- Added debug logging when room tracking succeeds

**Purpose**: Ensure NPC instances always have room tracking attributes set correctly during spawning.

### 5. NPC Movement Room Tracking Validation

**File**: `server/npc/movement_integration.py:106-130`

**Changes**:
- Enhanced room tracking update to always set both `current_room` and `current_room_id`
- Added creation of `current_room_id` attribute if it doesn't exist
- Added validation to verify room tracking was updated correctly
- Enhanced error logging if room tracking update fails

**Purpose**: Ensure NPC instances have room tracking updated correctly when NPCs move between rooms.

---

## TECHNICAL DETAILS

### Room ID Canonicalization

The fix adds canonical room ID resolution to ensure consistent comparison:

```python
# Get canonical room ID for consistent comparison
canonical_room_id = None
if hasattr(self.connection_manager, "_canonical_room_id"):
    canonical_room_id = self.connection_manager._canonical_room_id(room_id) or room_id
else:
    canonical_room_id = room_id
```

NPC room matching now checks multiple formats:

```python
room_matches = (
    npc_room_id == room_id
    or npc_room_id == canonical_room_id
    or npc_canonical_room_id == room_id
    or npc_canonical_room_id == canonical_room_id
)
```

### NPC Room Tracking Validation

NPC instances are now validated to ensure room tracking is set:

```python
# CRITICAL: Validate room tracking was set correctly
if not npc_instance.current_room or npc_instance.current_room != room_id:
    logger.error("Failed to set NPC room tracking correctly", ...)
else:
    logger.debug("NPC room tracking set successfully", ...)
```

### Enhanced Logging

All NPC queries now include detailed logging:

- Query start with room IDs
- NPC instance service availability
- Lifecycle manager availability
- NPC scanning progress
- Room matching results
- Final NPC count and IDs

---

## TESTING RECOMMENDATIONS

### Test Scenarios

1. **Player enters room with NPCs**:
   - Verify NPCs appear in Occupants panel immediately
   - Check server logs for NPC query execution
   - Verify NPCs are included in personal message

2. **Player moves between rooms with different NPCs**:
   - Verify NPCs from old room disappear
   - Verify NPCs in new room appear
   - Check for room ID format consistency

3. **Player enters room with no NPCs**:
   - Verify no NPCs are shown (correct behavior)
   - Check logs for proper NPC query execution

4. **NPC moves while player is in room**:
   - Verify NPC appears/disappears correctly
   - Check NPC room tracking is updated

### Log Verification

Check server logs for:

- `"Querying NPCs from lifecycle manager"` - NPC query started
- `"Found NPC in room"` - NPCs matched to room
- `"Completed NPC query from lifecycle manager"` - Query completed with counts
- `"NPCs included in occupants snapshot"` - NPCs included in personal message
- `"No NPCs included in occupants snapshot"` - Warning if NPCs missing

### Error Indicators

Watch for these warning/error logs:

- `"NPC instance missing room tracking"` - NPC doesn't have room attribute
- `"No NPCs matched room ID - possible room ID format mismatch"` - Room ID format issue
- `"Failed to set NPC room tracking correctly"` - Room tracking set failed
- `"No NPCs included in occupants snapshot"` - NPCs missing from personal message

---

## EXPECTED BEHAVIOR AFTER FIX

1. **When player enters room with NPCs**:
   - NPCs should appear in Occupants panel immediately
   - Server logs should show NPC query execution
   - Personal message should include NPCs

2. **When player moves between rooms**:
   - NPCs from old room should disappear
   - NPCs in new room should appear
   - Room ID matching should work consistently

3. **When NPCs move**:
   - NPC room tracking should be updated correctly
   - NPCs should appear in correct room's occupants

---

## FILES MODIFIED

1. `server/realtime/event_handler.py`
   - Enhanced `_handle_player_entered()` with better logging
   - Enhanced `_send_occupants_snapshot_to_player()` with validation
   - Enhanced `_get_room_occupants()` with canonical room ID matching

2. `server/npc/lifecycle_manager.py`
   - Enhanced NPC room tracking during spawning
   - Added validation for room tracking

3. `server/npc/movement_integration.py`
   - Enhanced NPC room tracking during movement
   - Added validation for room tracking updates

---

## RELATED INVESTIGATIONS

- **2025-01-29_session-001_npc-occupants-display-issue.md**: Previous investigation that fixed NPC room tracking during spawning
- **2025-01-30_session-001_npcs-not-updating-on-player-movement.md**: Current investigation that identified the dual update mechanism issue

---

## NEXT STEPS

1. **Test the fixes** in a development environment
2. **Monitor server logs** for NPC query execution and any warnings
3. **Verify NPC visibility** in Occupants panel when players move
4. **Check for any room ID format mismatches** in logs
5. **Validate NPC room tracking** is set correctly for all NPCs

---

**Remediation completed**: 2025-01-30
**Status**: Ready for testing
