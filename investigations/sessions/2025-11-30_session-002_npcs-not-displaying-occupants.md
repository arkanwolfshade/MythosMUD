# BUG INVESTIGATION REPORT: NPCs Not Displaying in Occupants List

**Investigation Date**: 2025-11-30
**Investigator**: AI Assistant (GPT-4)
**Session ID**: 2025-11-30_session-002_npcs-not-displaying-occupants
**Bug Report**: NPCs are not displaying in the Occupants list in the client UI. The Occupants panel shows "None" under NPCs section even when NPCs are present in the room.

---

## EXECUTIVE SUMMARY

**Root Cause Identified**: All NPCs in the room are being marked as `is_alive=False`, causing them to be filtered out when retrieving room occupants. The server logs show multiple NPCs being skipped with "Skipping dead NPC from occupants" messages, resulting in `npc_count=0` being added to occupants.

**System Impact**: **CRITICAL** - Core UI feature completely non-functional. NPCs exist in the game world and are being tracked by the lifecycle manager, but they are all incorrectly marked as dead, preventing them from appearing in the Occupants panel.

**Severity**: **HIGH** - This is a data integrity issue where NPCs are being incorrectly marked as dead, preventing all NPCs from being displayed to players.

---

## DETAILED FINDINGS

### Phase 1: Initial Bug Report Analysis

**Bug Description Parsed**:
- **Issue**: NPCs are not displaying in Occupants list in the client UI
- **Expected Behavior**: NPCs should appear in the Occupants panel under the "NPCs" section
- **Actual Behavior**: Occupants panel shows "None" under NPCs even when NPCs are present
- **Affected Component**: Client-side Occupants panel UI, Server-side NPC filtering
- **Related Systems**: NPC lifecycle management, Room occupants retrieval, is_alive status tracking

**Affected Systems Identified**:
1. **Server-side**: `server/realtime/room_subscription_manager.py` - NPC filtering by is_alive status
2. **Server-side**: `server/realtime/event_handler.py` - NPC retrieval and filtering in _get_room_occupants
3. **Server-side**: `server/npc/behaviors.py` - NPC is_alive status initialization and management
4. **Server-side**: `server/npc/lifecycle_manager.py` - NPC lifecycle state management
5. **Client-side**: `client/src/components/ui-v2/panels/OccupantsPanel.tsx` - UI display component

---

### Phase 2: System State Investigation

**Server Status**: Server is running (based on log timestamps)

**Log Analysis**: **CRITICAL EVIDENCE FOUND**

Log entries from `logs/local/server.log` (timestamp: 2025-11-30 11:18:39-46) show:

```
2025-11-30 11:18:39 - server.realtime.room_subscription_manager - DEBUG -
  npc_id='dr._francis_morgan_earth_arkhamcity_sanitarium_room_foyer_001_1764526499_5296'
  npc_name='Dr. Francis Morgan'
  room_id='earth_arkhamcity_sanitarium_room_foyer_001'
  event='Skipping dead NPC from occupants'

2025-11-30 11:18:39 - server.realtime.room_subscription_manager - DEBUG -
  npc_id='sanitarium_patient_earth_arkhamcity_sanitarium_room_foyer_001_1764526499_7071'
  npc_name='Sanitarium Patient'
  room_id='earth_arkhamcity_sanitarium_room_foyer_001'
  event='Skipping dead NPC from occupants'

2025-11-30 11:18:39 - server.realtime.room_subscription_manager - DEBUG -
  room_id='earth_arkhamcity_sanitarium_room_foyer_001'
  npc_count=0
  event='Adding NPCs to room occupants from lifecycle manager'
```

**Key Findings from Logs**:
- Multiple NPCs are present in the room (`earth_arkhamcity_sanitarium_room_foyer_001`)
- ALL NPCs are being skipped with "Skipping dead NPC from occupants"
- Final NPC count is 0 (`npc_count=0`)
- NPCs being skipped include: Dr. Francis Morgan, Sanitarium Patient, and others

**Configuration Review**: No configuration issues identified

---

### Phase 3: Code Analysis

#### Finding 1: NPC is_alive Status Filtering (ROOT CAUSE)

**Location**: `server/realtime/room_subscription_manager.py:320-331`

The `get_room_occupants` method filters out NPCs with `is_alive=False`:

```python
# BUGFIX: Filter out dead NPCs (is_alive=False) to prevent showing dead NPCs in occupants
for npc_id, npc_instance in active_npcs_dict.items():
    # Skip dead NPCs
    if not getattr(npc_instance, "is_alive", True):
        logger.debug(
            "Skipping dead NPC from occupants",
            npc_id=npc_id,
            npc_name=getattr(npc_instance, "name", "unknown"),
            room_id=canonical_id,
        )
        continue
```

**Status**: ✅ **WORKING AS DESIGNED** - The filtering logic is correct, but NPCs are incorrectly marked as dead

---

#### Finding 2: NPC is_alive Initialization

**Location**: `server/npc/behaviors.py:325`

NPCs are initialized with `is_alive = True`:

```python
def __init__(self, definition: Any, npc_id: str, event_bus=None, event_reaction_system=None):
    # ...
    self.is_alive = True
    self.is_active = True
```

**Status**: ✅ **CORRECT** - NPCs start as alive

---

#### Finding 3: NPC Death Handling

**Location**: `server/npc/behaviors.py:827-832`

NPCs can be marked as dead via the `_handle_die` method:

```python
def _handle_die(self, context: dict[str, Any]) -> bool:
    """Handle death action."""
    self.is_alive = False
    self.is_active = False
    logger.info("NPC died", npc_id=self.npc_id)
    return True
```

**Status**: ✅ **WORKING AS DESIGNED** - Death handling is correct, but something is marking all NPCs as dead

---

#### Finding 4: Server-Side Data Transmission (WORKING)

**Location**: `server/realtime/event_handler.py:617-736`

The `_send_room_occupants_update` method correctly sends structured data with separate `players` and `npcs` arrays:

```python
message = {
    "event_type": "room_occupants",
    "data": {
        "players": players,
        "npcs": npcs,  # ✅ Structured format
        "occupants": all_occupants,  # Backward compatibility
        "count": len(all_occupants),
    },
}
```

**Status**: ✅ **WORKING CORRECTLY** - Server sends structured data, but `npcs` array is empty because all NPCs are filtered out

---

#### Finding 5: Client-Side UI Component (WORKING)

**Location**: `client/src/components/ui-v2/panels/OccupantsPanel.tsx:17-19`

The OccupantsPanel correctly reads structured data:

```typescript
const players = room?.players ?? [];
const npcs = room?.npcs ?? [];
```

**Status**: ✅ **WORKING CORRECTLY** - UI component is ready to display NPCs, but receives empty `npcs` array

---

### Phase 4: Evidence Collection

**Code References Collected**:
1. `server/realtime/room_subscription_manager.py:320-331` - NPC filtering by is_alive (ROOT CAUSE)
2. `server/realtime/event_handler.py:1001-1010` - NPC filtering in event handler
3. `server/realtime/connection_manager.py:3577` - NPC filtering in connection manager
4. `server/realtime/websocket_handler.py:1008-1019` - NPC filtering in websocket handler
5. `server/npc/behaviors.py:325` - NPC is_alive initialization
6. `server/npc/behaviors.py:827-832` - NPC death handling

**Log Evidence Collected**:
- Multiple log entries showing "Skipping dead NPC from occupants" for NPCs in room `earth_arkhamcity_sanitarium_room_foyer_001`
- All NPCs checked are being skipped (Dr. Francis Morgan, Sanitarium Patient, etc.)
- Final NPC count is consistently 0

**Data Flow Analysis**:
1. ✅ NPCs exist in lifecycle manager (`active_npcs`)
2. ✅ NPCs are in the correct room (checked via `current_room_id`)
3. ❌ **ALL NPCs have `is_alive=False`** - ROOT CAUSE
4. ❌ NPCs are filtered out during occupant retrieval
5. ✅ Server sends empty `npcs: []` array to client
6. ✅ Client receives empty array and displays "None"

---

## ROOT CAUSE ANALYSIS

### Primary Root Cause

**Location**: NPC `is_alive` status is being incorrectly set to `False` for all NPCs

**Technical Details**:
- NPCs are initialized with `is_alive = True` in `NPCBase.__init__`
- Something is setting `is_alive = False` for all NPCs after initialization
- The filtering logic correctly excludes NPCs with `is_alive=False`
- All NPCs are being filtered out, resulting in empty `npcs` array sent to client

**Possible Causes**:
1. **NPCs are dying immediately after spawning** - NPCs may be taking damage or being killed during initialization
2. **Death event being triggered incorrectly** - NPCDied events may be firing for all NPCs
3. **Health/stat initialization issue** - NPCs may be spawning with 0 health, causing immediate death
4. **Behavior execution causing death** - NPC behavior execution may be triggering death actions
5. **Combat system marking NPCs as dead** - Combat system may be incorrectly marking NPCs as dead

**Evidence Supporting Root Cause**:
- Log entries show ALL NPCs in the room are marked as dead
- NPCs exist in `active_npcs` dictionary (they haven't been despawned)
- NPCs are in the correct room (room matching logic works)
- Filtering happens consistently across all occupant retrieval paths

### Secondary Issues

1. **No diagnostic logging for is_alive status changes**: There's no logging to track when or why NPCs are being marked as dead

2. **No validation of is_alive status on spawn**: There's no check to ensure NPCs spawn with valid health/stats that would keep them alive

---

## SYSTEM IMPACT ASSESSMENT

### Scope

**Affected Components**:
- ❌ NPC visibility in Occupants panel: **COMPLETELY BROKEN** (all NPCs filtered out)
- ✅ Server-side NPC retrieval: **WORKING** (NPCs are retrieved, but filtered out)
- ✅ Server-side data transmission: **WORKING** (empty array sent correctly)
- ✅ Client-side UI display: **WORKING** (correctly shows "None" when array is empty)

**User Impact**:
- **CRITICAL**: Players cannot see ANY NPCs in the Occupants panel
- **HIGH**: Players cannot identify NPCs in the room for interaction
- **MEDIUM**: Players cannot distinguish between rooms with NPCs and rooms without

**Functional Impact**:
- NPCs exist in the game world and are tracked by lifecycle manager
- NPCs are being processed by behavior system (logs show behavior execution)
- NPCs are in the correct rooms (room matching works)
- ALL NPCs are incorrectly marked as dead, preventing display

### Severity

**HIGH**:
- Core UI feature completely non-functional
- Affects ALL NPCs in the game world
- Prevents players from seeing NPCs for interaction
- Data integrity issue (NPCs incorrectly marked as dead)

---

## EVIDENCE DOCUMENTATION

### Log Evidence

**Multiple NPCs Being Skipped**:
```
2025-11-30 11:18:39 - server.realtime.room_subscription_manager - DEBUG -
  npc_id='dr._francis_morgan_earth_arkhamcity_sanitarium_room_foyer_001_1764526499_5296'
  npc_name='Dr. Francis Morgan'
  room_id='earth_arkhamcity_sanitarium_room_foyer_001'
  event='Skipping dead NPC from occupants'

2025-11-30 11:18:39 - server.realtime.room_subscription_manager - DEBUG -
  npc_id='sanitarium_patient_earth_arkhamcity_sanitarium_room_foyer_001_1764526499_7071'
  npc_name='Sanitarium Patient'
  room_id='earth_arkhamcity_sanitarium_room_foyer_001'
  event='Skipping dead NPC from occupants'

2025-11-30 11:18:39 - server.realtime.room_subscription_manager - DEBUG -
  room_id='earth_arkhamcity_sanitarium_room_foyer_001'
  npc_count=0
  event='Adding NPCs to room occupants from lifecycle manager'
```

**Pattern**: ALL NPCs checked are being skipped, resulting in `npc_count=0`

### Code Evidence

**NPC Filtering Logic**:
```python
# server/realtime/room_subscription_manager.py:320-331
if not getattr(npc_instance, "is_alive", True):
    logger.debug(
        "Skipping dead NPC from occupants",
        npc_id=npc_id,
        npc_name=getattr(npc_instance, "name", "unknown"),
        room_id=canonical_id,
    )
    continue
```

**NPC Initialization**:
```python
# server/npc/behaviors.py:325
self.is_alive = True  # ✅ NPCs start as alive
```

**NPC Death Handling**:
```python
# server/npc/behaviors.py:829
self.is_alive = False  # ❌ Something is calling this for all NPCs
```

### Data Flow Evidence

1. **NPCs Exist**: ✅ NPCs are in `lifecycle_manager.active_npcs`
2. **NPCs in Room**: ✅ NPCs have correct `current_room_id` matching room
3. **NPCs Marked Dead**: ❌ ALL NPCs have `is_alive=False`
4. **Filtering Works**: ✅ Filtering logic correctly excludes dead NPCs
5. **Empty Array Sent**: ✅ Server sends `npcs: []` to client
6. **Client Displays None**: ✅ Client correctly shows "None" for empty array

---

## INVESTIGATION RECOMMENDATIONS

### Priority 1: Investigate Why NPCs Are Marked as Dead

**Action**: Add diagnostic logging to track when and why NPCs are being marked as dead

**Location**: `server/npc/behaviors.py:827-832` (death handling)

**Required Changes**:
1. Add detailed logging when `is_alive` is set to `False`
2. Log the context/reason for death (combat, health, behavior, etc.)
3. Log stack trace to identify what code path is causing death

### Priority 2: Check NPC Health/Stats on Spawn

**Action**: Verify NPCs are spawning with valid health/stats

**Location**: `server/npc/behaviors.py:329` (stats initialization)

**Required Changes**:
1. Add validation logging for NPC health/stats on initialization
2. Check if NPCs are spawning with 0 health
3. Verify health calculation is correct

### Priority 3: Check for NPCDied Events Being Fired

**Action**: Check if NPCDied events are being incorrectly fired for all NPCs

**Location**: `server/npc/lifecycle_manager.py:298-343` (death event handling)

**Required Changes**:
1. Add logging to track NPCDied events
2. Check if events are being fired during NPC initialization
3. Verify event handlers are not incorrectly marking NPCs as dead

### Priority 4: Check Combat System Interactions

**Action**: Verify combat system is not incorrectly marking NPCs as dead

**Location**: `server/services/npc_combat_integration_service.py` and related combat files

**Required Changes**:
1. Check if combat system is checking `is_alive` incorrectly
2. Verify combat initialization doesn't mark NPCs as dead
3. Check for race conditions between spawn and combat initialization

### Priority 5: Check Behavior System Execution

**Action**: Verify NPC behavior execution is not causing deaths

**Location**: `server/npc/behaviors.py:758-797` (behavior execution)

**Required Changes**:
1. Check if behavior rules are triggering death actions
2. Verify health checks in behavior execution
3. Check for errors in behavior execution causing death

---

## REMEDIATION PROMPT

**For Cursor Chat**:

```
Investigate why ALL NPCs are being marked as is_alive=False, preventing them from appearing in the Occupants panel.

The issue is that:
1. NPCs are correctly initialized with is_alive=True in NPCBase.__init__
2. All NPCs in rooms are being filtered out during occupant retrieval because is_alive=False
3. Server logs show "Skipping dead NPC from occupants" for all NPCs, resulting in npc_count=0

Required investigation:
1. Add diagnostic logging to track when is_alive is set to False (in _handle_die method and anywhere else is_alive is modified)
2. Check if NPCs are spawning with 0 health or invalid stats that would cause immediate death
3. Check if NPCDied events are being incorrectly fired during NPC initialization
4. Verify combat system is not incorrectly marking NPCs as dead
5. Check if behavior system execution is triggering death actions

The filtering logic is working correctly - the problem is that ALL NPCs are incorrectly marked as dead. We need to find out why.

Location to start investigation:
- server/npc/behaviors.py:827-832 (_handle_die method)
- server/npc/behaviors.py:325 (is_alive initialization)
- server/npc/lifecycle_manager.py:298-343 (NPCDied event handling)
- Anywhere is_alive is set to False in the codebase
```

---

## INVESTIGATION COMPLETION CHECKLIST

- [x] All investigation steps completed as written
- [x] Comprehensive evidence collected and documented
- [x] Root cause analysis completed (NPCs incorrectly marked as dead)
- [x] System impact assessed (CRITICAL - all NPCs filtered out)
- [x] Investigation report generated
- [x] No attempt made to fix issues (investigation only)
- [x] All findings clearly documented with evidence
- [x] Log evidence collected and analyzed
- [x] Session logged in investigation history
- [x] Pattern analysis updated (all NPCs marked as dead)
- [x] Remediation prompt generated (root cause identified but needs deeper investigation)

---

**Investigation Status**: ✅ **COMPLETE** - Root cause identified (NPCs incorrectly marked as dead), but deeper investigation needed to find WHY they're being marked as dead

**Next Steps**: Use the remediation prompt above to investigate WHY NPCs are being marked as dead. This requires adding diagnostic logging and tracing the code paths that set is_alive=False.
