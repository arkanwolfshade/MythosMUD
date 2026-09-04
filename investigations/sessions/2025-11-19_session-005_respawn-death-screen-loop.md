# Investigation Report: Respawn Death Screen Loop Bug

**Session ID**: 2025-11-20_session-001_respawn-death-screen-loop
**Date**: 2025-11-20
**Investigator**: AI Agent (GPT-4)
**Bug Report**: After logging in as ArkanWolfshade/Cthulhu1, player initiated combat and died to the Santarium Patient. Player then continued to see the death screen, clicked "enter the realm" to respawn, but then saw the death screen again. This was repeated multiple times.

## Executive Summary

**Root Cause Identified**: Room ID mismatch between the limbo room ID constant used in code (`limbo_death_void`) and the actual room ID stored in the database/cache (`limbo_death_void_limbo_death_void`). This mismatch prevents the respawn system from correctly identifying when a player is in limbo and from successfully respawning them.

**Impact**: Critical - Players cannot respawn after death, causing them to be stuck in a death screen loop.

**Status**: Root cause identified, fix ready for implementation.

## Detailed Findings

### Phase 1: Initial Bug Report Analysis

**Bug Description**:

- Player: ArkanWolfshade
- Sequence: Login → Combat → Death → Respawn attempt → Death screen reappears → Loop repeats
- Expected behavior: Player should respawn at designated respawn room with full HP
- Actual behavior: Player remains in death state, seeing death screen repeatedly

**Affected Systems**:

- Player respawn service
- Death state management
- Room lookup/cache system
- Client-side death/respawn UI

### Phase 2: System State Investigation

#### Log Analysis

**Key Error from `logs/local/errors.log` (Line 52)**:

```
2025-11-19 18:45:26 - PersistenceLayer - WARNING -
requested_room_id='limbo_death_void'
cache_size=116
similar_rooms=['limbo_death_void_limbo_death_void']
event='Room not found in cache'
```

**Analysis**: The system is looking for a room with ID `limbo_death_void`, but the actual room ID in the cache is `limbo_death_void_limbo_death_void`. This indicates a mismatch between the room ID constant used in code and the actual room ID generated from the database.

**Combat Log Evidence** (`logs/local/combat.log`):

- Combat started at 18:44:42
- Player died at 18:45:25 (combat ended)
- Death occurred in room: `earth_arkhamcity_sanitarium_room_foyer_001`

**Server Log Evidence** (`logs/local/server.log`):

- Player disconnected at 18:45:50 (after multiple respawn attempts failed)
- Room lookup warning occurred at 18:45:26, immediately after death

### Phase 3: Code Analysis

#### Room ID Generation Logic

**File**: `server/persistence.py` (Lines 495-717)

The persistence layer loads rooms from PostgreSQL and generates room IDs using the following logic:

1. **Room ID Format**: `{plane}_{zone}_{sub_zone}_{stable_id}`

2. **For Limbo Room**:

   - Plane: `limbo`
   - Zone: `death`
   - Sub-zone: `void`
   - Stable ID: `limbo_death_void`
   - **Generated Room ID**: `limbo_death_void_limbo_death_void`

**Code Reference** (`server/persistence.py:565-571`):

```python
expected_prefix = f"{plane_name}_{zone_name}_{subzone_stable_id}_"
if stable_id.startswith(expected_prefix):
    # stable_id is already a full hierarchical room ID, use it directly

    room_id = stable_id
else:
    # stable_id is just the room identifier, generate full ID

    room_id = generate_room_id(plane_name, zone_name, subzone_stable_id, stable_id)
```

Since `limbo_death_void` does NOT start with `limbo_death_void_`, the code generates: `limbo_death_void_limbo_death_void`.

#### Respawn Service Code

**File**: `server/services/player_respawn_service.py` (Line 23)

**Current Code**:

```python
LIMBO_ROOM_ID = "limbo_death_void"
```

**Problem**: This constant does not match the actual room ID in the cache (`limbo_death_void_limbo_death_void`).

**Impact Points**:

1. `move_player_to_limbo()` (Line 78): Sets `player.current_room_id = LIMBO_ROOM_ID` - This sets an invalid room ID
2. `respawn_player()` (Line 196): Checks `old_room == LIMBO_ROOM_ID` - This check will always fail
3. Room lookup fails when trying to get the limbo room from cache

#### Additional Usage

**File**: `server/app/lifespan.py` (Line 626)

**Current Code**:

```python
if current_hp <= -10 and player.current_room_id != "limbo_death_void":
```

**Problem**: Hardcoded string instead of using the constant, and uses the wrong room ID.

### Phase 4: Evidence Collection

#### Database Room Data

**File**: `data/local/rooms/limbo/death/void/limbo_room.json`

```json
{
  "id": "limbo_death_void",
  "name": "The Spaces Between",
  "plane": "limbo",
  "zone": "death",
  "sub_zone": "void",
  ...
}
```

**Analysis**: The JSON file has `"id": "limbo_death_void"`, but when loaded into the database and processed by the persistence layer, it becomes `limbo_death_void_limbo_death_void` due to the room ID generation algorithm.

#### Error Pattern

The error log shows:

**Requested**: `limbo_death_void`

**Available**: `limbo_death_void_limbo_death_void`

**Result**: Room not found in cache

This confirms the mismatch between code expectations and actual database state.

### Phase 5: Root Cause Analysis

#### Primary Root Cause

**Room ID Mismatch**: The limbo room ID constant (`limbo_death_void`) does not match the actual room ID generated by the persistence layer (`limbo_death_void_limbo_death_void`).

**Why This Causes the Bug**:

1. **Death Sequence**:

   - Player dies → `move_player_to_limbo()` is called
   - Player's `current_room_id` is set to `limbo_death_void` (invalid ID)
   - Room lookup fails because cache has `limbo_death_void_limbo_death_void`

2. **Respawn Sequence**:

   - Player clicks "enter the realm" → `respawn_player()` is called
   - System checks if player is in limbo: `old_room == LIMBO_ROOM_ID`
   - Check fails because player's room ID is `limbo_death_void` but constant is also `limbo_death_void` (but room doesn't exist)
   - System tries to get respawn room but player state is inconsistent
   - Respawn fails or partially succeeds, leaving player in death state

3. **Loop**:

   - Player remains in death state (HP <= -10)
   - Client shows death screen
   - Player clicks respawn again
   - Cycle repeats

#### Contributing Factors

1. **Inconsistent Room ID Generation**: The room ID generation algorithm creates hierarchical IDs, but the limbo room's stable_id already contains the full path, causing duplication.

2. **Hardcoded Values**: Multiple places use hardcoded strings instead of constants, making updates error-prone.

3. **Missing Validation**: No validation that the limbo room ID exists in the cache before using it.

## System Impact Assessment

### Severity: **CRITICAL**

**Affected Users**: All players who die in combat

**Impact**:

- Players cannot respawn after death
- Game becomes unplayable after death
- Player experience severely degraded
- Potential for player frustration and abandonment

**Scope**:

- Affects all death/respawn scenarios
- No workaround available to players
- Requires server restart or manual database intervention to fix stuck players

## Recommended Fix

### Fix 1: Update LIMBO_ROOM_ID Constant

**File**: `server/services/player_respawn_service.py`

**Change**:

```python
# Before

LIMBO_ROOM_ID = "limbo_death_void"

# After

LIMBO_ROOM_ID = "limbo_death_void_limbo_death_void"
```

### Fix 2: Update Hardcoded String in Lifespan

**File**: `server/app/lifespan.py`

**Change**:

```python
# Before

if current_hp <= -10 and player.current_room_id != "limbo_death_void":

# After

from server.services.player_respawn_service import LIMBO_ROOM_ID
if current_hp <= -10 and player.current_room_id != LIMBO_ROOM_ID:
```

### Fix 3: Add Room Validation (Optional Enhancement)

Add validation in `move_player_to_limbo()` to ensure the limbo room exists in cache before moving the player.

## Testing Recommendations

1. **Unit Tests**: Update existing tests that use `limbo_death_void` to use the correct room ID
2. **Integration Tests**: Test full death/respawn cycle
3. **E2E Tests**: Use Playwright MCP to reproduce the bug scenario and verify fix

## Remediation Prompt

```
Fix the respawn death screen loop bug by updating the LIMBO_ROOM_ID constant in
server/services/player_respawn_service.py from "limbo_death_void" to
"limbo_death_void_limbo_death_void" to match the actual room ID generated by the
persistence layer. Also update the hardcoded string in server/app/lifespan.py line 626
to use the LIMBO_ROOM_ID constant instead. Update all unit tests that reference the
old room ID. Verify the fix by reproducing the bug scenario with Playwright MCP.
```

## Investigation Completion Checklist

[x] All investigation steps completed as written

- [x] Comprehensive evidence collected and documented
- [x] Root cause analysis completed
- [x] System impact assessed
- [x] Investigation report generated
- [x] No attempt made to fix issues (investigation only)
- [x] All findings clearly documented with evidence
- [x] Only official test credentials were used (ArkanWolfshade/Cthulhu1)
- [x] Session logged in investigation history
- [x] Remediation prompt generated

---

**Investigation Status**: COMPLETE
**Next Steps**: Implement fixes as outlined in Recommended Fix section
