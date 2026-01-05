# Bug Investigation Report: Non-Admin Player Mini-Maps Not Showing Explored Rooms

**Investigation Date:** 2025-01-04
**Investigator:** AI Assistant
**Session ID:** 2025-01-04_session-minimap-explored-rooms-bug

## Executive Summary

Non-admin players' mini-maps are not displaying explored rooms due to a data type mismatch in the room filtering logic. The `get_explored_rooms()` method returns room UUIDs, but the minimap endpoint incorrectly treats these UUIDs as stable_ids when filtering rooms, causing the comparison to fail and resulting in no rooms being displayed.

## Bug Description

**Reported Issue:** Non-admin player mini-maps are not showing explored rooms.

**Expected Behavior:** Non-admin players should see explored rooms in their mini-map display.

**Actual Behavior:** Non-admin players see no rooms (or only the current room) in their mini-map, even after exploring multiple rooms.

## Detailed Findings

### Phase 1: Initial Bug Report Analysis

**Parsed Bug Description:**

- Affected Component: Mini-map display for non-admin players
- Symptom: Explored rooms not appearing in mini-map
- Scope: Non-admin players only (admin players may be unaffected)
- Impact: Players cannot see their exploration progress visually

**Affected Systems Identified:**

1. Client-side: `AsciiMinimap` component (`client/src/components/map/AsciiMinimap.tsx`)
2. Server-side: `/api/maps/ascii/minimap` endpoint (`server/api/maps.py`)
3. Exploration Service: `ExplorationService.get_explored_rooms()` (`server/services/exploration_service.py`)
4. Room Filtering Logic: Room filtering in minimap endpoint

### Phase 2: Code Analysis

#### Finding 1: Client-Side Mini-Map Component

**File:** `client/src/components/map/AsciiMinimap.tsx`

**Analysis:**

- Component fetches minimap data from `/api/maps/ascii/minimap` endpoint
- Passes `authToken` for authenticated requests
- No client-side filtering logic - relies entirely on server response
- Component correctly displays whatever HTML is returned from server

**Conclusion:** Client-side code is functioning correctly. Issue is server-side.

#### Finding 2: Server-Side Mini-Map Endpoint

**File:** `server/api/maps.py`
**Lines:** 153-234

**Critical Code Section (lines 187-196):**

```python
# Filter to explored rooms if not admin
if not (current_user.is_admin or current_user.is_superuser):
    container = request.app.state.container
    exploration_service: ExplorationService = container.exploration_service
    player_id = uuid.UUID(str(player.player_id))
    explored_room_ids = await exploration_service.get_explored_rooms(player_id, session)
    explored_stable_ids = set(explored_room_ids)  # ⚠️ BUG: explored_room_ids contains UUIDs, not stable_ids!
    rooms = [
        r for r in rooms if r.get("stable_id") in explored_stable_ids or r.get("id") in explored_stable_ids
    ]
```

**Problem Identified:**

- Line 192: `explored_room_ids = await exploration_service.get_explored_rooms(player_id, session)` returns a list of **room UUIDs** (as strings)
- Line 193: `explored_stable_ids = set(explored_room_ids)` incorrectly treats UUIDs as stable_ids
- Line 195: Comparison `r.get("stable_id") in explored_stable_ids` compares stable_ids (strings like `"earth_arkhamcity_room1"`) with UUIDs (strings like `"123e4567-e89b-12d3-a456-426614174000"`)
- **Result:** The comparison always fails, so no rooms match the filter, resulting in an empty or minimal minimap

#### Finding 3: Exploration Service Implementation

**File:** `server/services/exploration_service.py`
**Lines:** 238-269

**Method:** `get_explored_rooms()`

**Analysis:**

```python
async def get_explored_rooms(self, player_id: UUID, session: AsyncSession) -> list[str]:
    """
    Get list of room IDs that a player has explored.

    Returns:
        List of room IDs (as strings) that the player has explored
    """
    query = text("""
        SELECT room_id FROM player_exploration
        WHERE player_id = :player_id
        ORDER BY explored_at ASC
    """)
    result = await session.execute(query, {"player_id": str(player_id)})
    rows = result.fetchall()
    room_ids = [str(row[0]) for row in rows]  # Returns UUIDs as strings
    return room_ids
```

**Key Finding:**

- The method queries `player_exploration.room_id` which stores **room UUIDs** (not stable_ids)
- Returns list of UUID strings (e.g., `["123e4567-e89b-12d3-a456-426614174000", ...]`)
- Documentation says "room IDs" but these are actually UUIDs, not hierarchical stable_ids

#### Finding 4: Comparison with Working Implementation

**File:** `server/api/rooms.py`
**Lines:** 155-171

**Working Implementation:**

```python
explored_room_ids = await exploration_service.get_explored_rooms(player_id, session)

# Convert explored room UUIDs to stable_ids for filtering
if explored_room_ids:
    # Convert string UUIDs to UUID objects for proper PostgreSQL type handling
    room_uuid_list = [uuid.UUID(rid) for rid in explored_room_ids]
    # Use IN clause with expanding parameters for proper array handling
    lookup_query = text("SELECT stable_id FROM rooms WHERE id IN :room_ids").bindparams(
        bindparam("room_ids", expanding=True)
    )
    result = await session.execute(lookup_query, {"room_ids": room_uuid_list})
    explored_stable_ids = {row[0] for row in result.fetchall()}  # ✅ Correctly converts UUIDs to stable_ids

    # Filter rooms to only include explored ones
    rooms = [room for room in rooms if room.get("id") in explored_stable_ids]
```

**Key Difference:**

- The `/api/rooms/list` endpoint correctly converts UUIDs to stable_ids by querying the database
- The minimap endpoint (`/api/maps/ascii/minimap`) is missing this conversion step

#### Finding 5: Similar Issue in ASCII Map Endpoint

**File:** `server/api/maps.py`
**Lines:** 79-92

**Similar Bug:**

```python
if current_user and not (current_user.is_admin or current_user.is_superuser):
    container = request.app.state.container
    exploration_service: ExplorationService = container.exploration_service
    user_id = str(current_user.id)
    player = await persistence.get_player_by_user_id(user_id)
    if player:
        player_id = uuid.UUID(str(player.player_id))
        explored_room_ids = await exploration_service.get_explored_rooms(player_id, session)
        # Filter rooms to only explored ones
        explored_stable_ids = set(explored_room_ids)  # ⚠️ SAME BUG: UUIDs treated as stable_ids
        rooms = [
            r for r in rooms if r.get("stable_id") in explored_stable_ids or r.get("id") in explored_stable_ids
        ]
```

**Impact:** The full ASCII map endpoint (`/api/maps/ascii`) has the same bug, affecting non-admin players' full map view as well.

### Phase 3: Root Cause Analysis

**Root Cause:** Data type mismatch in room filtering logic.

**Technical Details:**

1. **Data Flow:**
   - `player_exploration` table stores `room_id` as UUID (references `rooms.id`)
   - `get_explored_rooms()` returns these UUIDs as strings
   - Room data loaded by `_load_rooms_with_coordinates()` uses `stable_id` (hierarchical string IDs like `"earth_arkhamcity_room1"`)
   - Filtering compares UUIDs with stable_ids, which never match

2. **Why It Fails:**
   - UUID format: `"123e4567-e89b-12d3-a456-426614174000"` (36 characters with hyphens)
   - Stable ID format: `"earth_arkhamcity_northside_room1"` (hierarchical string)
   - These are fundamentally different data types and formats
   - Direct set membership check (`in`) will always return `False`

3. **Why Admins Are Unaffected:**
   - Admin check happens before filtering: `if not (current_user.is_admin or current_user.is_superuser):`
   - Admins skip the filtering logic entirely, so they see all rooms regardless

### Phase 4: System Impact Assessment

**Severity:** High - Core functionality broken for non-admin players

**Scope:**

- **Affected Users:** All non-admin players
- **Affected Features:**
  - Mini-map display (`/api/maps/ascii/minimap`)
  - Full ASCII map display (`/api/maps/ascii`) - same bug exists
  - Room map viewer (`/api/rooms/list`) - correctly implemented, not affected

**User Experience Impact:**

- Non-admin players cannot see their exploration progress visually
- Mini-map appears empty or shows only current room
- Reduces player engagement and spatial awareness
- May cause confusion about game state

**Data Integrity:**

- Exploration data is correctly stored in database
- Issue is purely in the filtering/display logic
- No data corruption or loss

### Phase 5: Evidence Documentation

**Code References:**

1. **Bug Location 1:** `server/api/maps.py:193`

   ```python
   explored_stable_ids = set(explored_room_ids)  # Bug: UUIDs, not stable_ids
   ```

2. **Bug Location 2:** `server/api/maps.py:89`

   ```python
   explored_stable_ids = set(explored_room_ids)  # Same bug in ASCII map endpoint
   ```

3. **Correct Implementation Reference:** `server/api/rooms.py:157-168`

   ```python
   # Correctly converts UUIDs to stable_ids via database query
   room_uuid_list = [uuid.UUID(rid) for rid in explored_room_ids]
   lookup_query = text("SELECT stable_id FROM rooms WHERE id IN :room_ids").bindparams(
       bindparam("room_ids", expanding=True)
   )
   result = await session.execute(lookup_query, {"room_ids": room_uuid_list})
   explored_stable_ids = {row[0] for row in result.fetchall()}
   ```

4. **Exploration Service:** `server/services/exploration_service.py:238-269`
   - Returns UUIDs, not stable_ids
   - Documentation could be clearer about return type

**Database Schema:**

- `player_exploration.room_id` → UUID (references `rooms.id`)
- `rooms.id` → UUID (primary key)
- `rooms.stable_id` → String (hierarchical ID like `"earth_arkhamcity_room1"`)

## Investigation Recommendations

### Priority 1: Fix Mini-Map Endpoint

- Apply the same UUID-to-stable_id conversion logic used in `/api/rooms/list` to `/api/maps/ascii/minimap`
- Location: `server/api/maps.py:187-196`

### Priority 2: Fix ASCII Map Endpoint

- Apply the same fix to `/api/maps/ascii` endpoint
- Location: `server/api/maps.py:79-92`

### Priority 3: Code Review

- Review all endpoints that use `get_explored_rooms()` to ensure proper UUID-to-stable_id conversion
- Consider adding a helper function to avoid code duplication

### Priority 4: Documentation

- Update `get_explored_rooms()` documentation to clarify it returns UUIDs, not stable_ids
- Add comments in filtering code explaining the conversion step

### Priority 5: Testing

- Add integration tests for minimap endpoint with non-admin players
- Verify explored rooms appear correctly after fix
- Test edge cases (no explored rooms, all rooms explored, etc.)

## Remediation Prompt

**For Cursor Chat:**

```
Fix the bug where non-admin player mini-maps are not showing explored rooms.

The issue is in server/api/maps.py in the get_ascii_minimap() function (lines 187-196) and get_ascii_map() function (lines 79-92). The code incorrectly treats room UUIDs as stable_ids when filtering explored rooms.

The get_explored_rooms() method returns room UUIDs (from player_exploration.room_id), but the filtering code compares these UUIDs directly with stable_ids, which never match.

Fix by applying the same UUID-to-stable_id conversion logic that's already correctly implemented in server/api/rooms.py (lines 157-168). Convert the UUIDs to stable_ids by querying the database before filtering.

Also update the get_ascii_map() endpoint (lines 79-92) which has the same bug.

After fixing, verify that:
1. Non-admin players see explored rooms in their mini-map
2. Non-admin players see explored rooms in the full ASCII map
3. Admin players continue to see all rooms (unaffected)
4. The fix matches the working implementation in /api/rooms/list
```

## Investigation Completion Checklist

- [x] All investigation steps completed as written
- [x] Comprehensive evidence collected and documented
- [x] Root cause analysis completed
- [x] System impact assessed
- [x] Investigation report generated
- [x] No attempt made to fix issues (investigation only)
- [x] All findings clearly documented with evidence
- [x] Only official test credentials were used (not applicable - no runtime testing performed)
- [x] Session logged in investigation history
- [x] Pattern analysis updated if applicable
- [x] Remediation prompt generated (root cause found)

---

**Investigation Status:** ✅ Complete - Root cause identified

**Next Steps:** Use the remediation prompt above to fix the identified issues in `server/api/maps.py`.
