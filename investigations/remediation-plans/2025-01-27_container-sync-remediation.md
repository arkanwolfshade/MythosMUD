# Container Contents Synchronization Remediation Plan

## Executive Summary

**Problem**: Items picked up from the ground are incorrectly marked with `slot_type='backpack'` in inventory JSON, but are NOT added to the `container_contents` PostgreSQL table. This causes `slots_in_use` to show 0 instead of the correct count.

**Root Cause**: The `pickup` command incorrectly sets `slot_type='backpack'` (line 650), making items appear as if they're in a container when they're actually in general inventory. Items should only have `slot_type='backpack'` when explicitly placed into containers via the `put` command.

**Solution**: Remove the incorrect `slot_type='backpack'` assignment from the `pickup` command. Items picked up should go to general inventory (no `slot_type` or `slot_type=None`). Items should only get `slot_type='backpack'` when explicitly put into containers via the `put` command.

## Current State Analysis

### Data Storage Architecture

The system uses **two storage locations** for container items:

1. **Player Inventory JSON** (`players.inventory` JSONB):
   - Stores ALL player items, including those in containers
   - Items in containers have `slot_type='backpack'` (or other container slot)
   - Used for: Inventory capacity calculation, item ownership

2. **Container Contents Table** (`container_contents` PostgreSQL):
   - Stores items that are physically inside containers
   - Used for: Container capacity display, container operations
   - Queried by: `WearableContainerService.get_wearable_containers_for_player()`

### Current Behavior

| Operation         | Inventory JSON                      | Container Contents | Status     |
| ----------------- | ----------------------------------- | ------------------ | ---------- |
| Pickup            | ✅ Added with `slot_type='backpack'` | ❌ NOT added        | **BROKEN** |
| Put               | ✅ Removed                           | ✅ Added            | ✅ Working  |
| Get               | ✅ Added                             | ✅ Removed          | ✅ Working  |
| Inventory Display | ✅ Read                              | ✅ Read (but empty) | ❌ Shows 0  |

### Impact

- **User Experience**: Container shows "0/20 slots" when it should show "1/20"
- **Data Integrity**: Items exist in inventory JSON but not in container_contents (inconsistent state)
- **System Reliability**: Container operations may fail or behave unexpectedly

## Remediation Strategy

### Recommended Approach: Remove Incorrect slot_type Assignment

**Principle**: Items picked up from the ground should go to general inventory (no `slot_type`). Items should only have `slot_type='backpack'` when explicitly placed into containers via the `put` command.

**Benefits**:

- Fixes root cause: items no longer incorrectly marked as being in containers
- Consistent behavior: pickup → general inventory, put → container
- Minimal code changes: remove one line
- Clear separation: general inventory vs container contents

### Implementation Plan

#### Phase 1: Fix Pickup Command

**File**: `server/commands/inventory_commands.py`
**Location**: `handle_pickup_command()` function, line 650

**Changes**:

1. **Remove incorrect `slot_type='backpack'` assignment** (line 650):
   - Items picked up should go to general inventory
   - Do NOT set `slot_type='backpack'` during pickup
   - Items should only get `slot_type='backpack'` when explicitly put into containers via `put` command

2. **Code Change**:

   ```python
   # BEFORE (line 650):
   extracted_stack["slot_type"] = "backpack"

   # AFTER:
   # Do NOT set slot_type - items go to general inventory
   # slot_type is only set when items are explicitly put into containers via 'put' command
   ```

3. **Error Handling** (for `put` command, not pickup):
   - If container doesn't exist (player targets): Inform player there is no such container
   - If container doesn't exist (server targets): Raise exception with detailed error logs
   - If container is full (player targets): Inform player there is no remaining capacity
   - If container is full (server targets): [To be defined - see question #4]
   - If container service unavailable: Raise exception, terminate operation

#### Phase 2: Data Cleanup (Optional)

**Purpose**: Clean up existing items that were incorrectly marked with `slot_type='backpack'` during pickup

**File**: `server/scripts/cleanup_incorrect_slot_types.py` (new file)

**Logic**:

1. Query all players
2. For each player:
   - Get inventory items with `slot_type='backpack'`
   - Check if item is actually in container_contents table
   - If NOT in container_contents, remove slot_type (item is in general inventory)
3. Log results and errors

**Execution**:

- One-time script
- Run via admin command
- Safe to run multiple times (idempotent)
- **Note**: This may not be necessary if the fix is deployed before significant data corruption

#### Phase 3: Testing

**Test Cases**:

1. **Pickup with Equipped Backpack**:
   - Equip backpack
   - Pick up item
   - Verify: Item in container_contents, `slots_in_use` = 1

2. **Pickup without Equipped Backpack**:
   - No backpack equipped
   - Pick up item
   - Verify: Item in inventory JSON with `slot_type='backpack'`, not in container_contents

3. **Pickup when Backpack is Full**:
   - Fill backpack to capacity
   - Pick up item
   - Verify: Item in inventory JSON (fallback), error message shown

4. **Pickup when Container Service Unavailable**:
   - Simulate container service failure
   - Pick up item
   - Verify: Exception raised, detailed error logs written, operation fails

5. **Existing Put/Get Commands**:
   - Verify put command still works
   - Verify get command still works
   - Verify inventory display shows correct counts

6. **Migration Script**:
   - Run on test data
   - Verify items synced correctly
   - Verify no duplicates created

## Implementation Details

### Code Changes Required

#### 1. Fix `handle_pickup_command()` in `server/commands/inventory_commands.py`

**Location**: Line 650

**Change**: Remove the incorrect `slot_type='backpack'` assignment

**Code Change**:

```python
# BEFORE (line 650):
if isinstance(extracted_stack, dict):
    extracted_stack = dict(extracted_stack)  # Create a copy to avoid mutating the original
    extracted_stack["slot_type"] = "backpack"  # ❌ REMOVE THIS LINE

# AFTER:
if isinstance(extracted_stack, dict):
    extracted_stack = dict(extracted_stack)  # Create a copy to avoid mutating the original
    # Do NOT set slot_type - items go to general inventory
    # slot_type is only set when items are explicitly put into containers via 'put' command
```

**Rationale**: Items picked up from the ground should go to general inventory, not be marked as being in a container. Items should only have `slot_type='backpack'` when explicitly placed into containers via the `put` command.

#### 2. Create Migration Script

**File**: `server/scripts/migrate_container_items.py`

**Structure**:

```python
"""
Migration script to sync items with slot_type='backpack' to container_contents table.

This script fixes the data synchronization issue where items were stored in
inventory JSON but not in container_contents table.
"""

def migrate_player_container_items(persistence, player_id: UUID) -> dict[str, Any]:
    """Migrate a single player's container items."""
    # Implementation here
    pass

def run_migration(persistence) -> dict[str, Any]:
    """Run migration for all players."""
    # Implementation here
    pass
```

### Edge Cases and Error Handling

**For Pickup Command** (items go to general inventory):

- No special error handling needed - items simply go to general inventory
- No container operations involved

**For Put Command** (items placed into containers):

1. **Container Doesn't Exist (Player Targets)**:
   - **Behavior**: Return user-friendly message: "You don't see any '{container_name}' here."
   - **Rationale**: Player-initiated action - inform them the container doesn't exist
   - **Logging**: Debug level log

2. **Container Doesn't Exist (Server Targets)**:
   - **Behavior**: Raise ContainerNotFoundError with full error context
   - **Rationale**: Server-initiated action - indicates data integrity issue
   - **Logging**: Error level with full traceback

3. **Container is Full (Player Targets)**:
   - **Behavior**: Return user-friendly message: "The {container_name} is full."
   - **Rationale**: Player-initiated action - inform them there's no remaining capacity
   - **Logging**: Info level log

4. **Container is Full (Server Targets)**:
   - **Behavior**: [NOT CURRENTLY APPLICABLE - No server-initiated container operations exist]
   - **Rationale**: Investigation shows all container operations are player-initiated (via `put` command or API)
   - **Future-Proofing**: If server-initiated operations are added later, raise ContainerCapacityError with full error context
   - **Logging**: Error level with container capacity details (if implemented)

5. **Container Service Unavailable**:
   - **Behavior**: Raise RuntimeError with full error context, terminate operation
   - **Rationale**: Container service is REQUIRED - failure indicates system misconfiguration
   - **Logging**: Error level with full traceback and system state

**CRITICAL**: All server-initiated errors must be logged with full context (traceback, player_id, container_id, etc.) and operations must FAIL - no silent fallbacks that hide problems.

## Testing Strategy

### Unit Tests

**File**: `server/tests/unit/commands/test_inventory_commands.py`

**Test Cases**:

1. `test_pickup_places_item_in_general_inventory` (no slot_type set)
2. `test_pickup_does_not_set_slot_type_backpack`
3. `test_pickup_item_has_no_slot_type_attribute`

### Integration Tests

**File**: `server/tests/integration/test_container_sync.py` (new file)

**Test Cases**:

1. `test_pickup_syncs_to_container_contents`
2. `test_inventory_display_shows_correct_slots_in_use_after_pickup`
3. `test_put_and_get_still_work_after_pickup_changes`

### Manual Testing Checklist

- [ ] Pick up item → Verify item in general inventory (no slot_type)
- [ ] Pick up item → Verify item does NOT have slot_type='backpack'
- [ ] Put item into container → Verify item has slot_type='backpack' and is in container_contents
- [ ] Run `/inventory` command → Verify correct slot counts
- [ ] Use `put` command → Verify still works
- [ ] Use `get` command → Verify still works
- [ ] Run migration script → Verify existing data synced

## Rollout Plan

### Phase 1: Development (Current)

- [x] Root cause analysis
- [x] Remediation plan
- [ ] Code implementation
- [ ] Unit tests
- [ ] Integration tests

### Phase 2: Testing

- [ ] Run full test suite
- [ ] Manual testing
- [ ] Performance testing
- [ ] Edge case testing

### Phase 3: Data Cleanup (Optional)

- [ ] Create cleanup script (if needed)
- [ ] Test cleanup on staging data
- [ ] Run cleanup on production (if needed)
- [ ] Verify cleanup results

### Phase 4: Deployment

- [ ] Deploy code changes
- [ ] Monitor logs for errors
- [ ] Verify user reports
- [ ] Document changes

## Success Criteria

1. ✅ Items picked up go to general inventory (no slot_type='backpack')
2. ✅ Items only have slot_type='backpack' when explicitly put into containers
3. ✅ `slots_in_use` shows correct count for items in containers
4. ✅ Existing `put` and `get` commands still work
5. ✅ No data loss or corruption
6. ✅ All tests pass
7. ✅ No performance degradation

## Risk Assessment

### Low Risk

- Code changes are isolated to pickup command
- Migration script is idempotent
- Errors are logged with full context for debugging

### Medium Risk

- Container service dependency (fail-fast ensures we catch issues immediately)
- Migration script may take time for large datasets (mitigated by batching)
- Operations will fail if container service unavailable (by design - ensures we fix issues)

### High Risk

- **No graceful degradation**: Operations will fail if container service unavailable
- **Impact**: Players cannot pick up items if container service is down
- **Mitigation**: This is intentional - ensures we fix infrastructure issues immediately

### Mitigation Strategies

- Comprehensive error logging with full tracebacks and context
- Extensive testing before deployment
- Migration script with dry-run mode
- Rollback plan (revert code changes)
- **Fail-fast philosophy**: Better to fail loudly than silently corrupt data

## Timeline Estimate

- **Development**: 30 minutes (remove one line)
- **Testing**: 1-2 hours
- **Data Cleanup Script**: 1 hour (optional)
- **Data Cleanup Execution**: 15 minutes (optional)
- **Total**: 2-4 hours

## Dependencies

- Container service MUST be available (no fallback - operations fail if unavailable)
- Wearable container service for finding equipped containers
- Persistence layer for container operations
- Migration requires database access

## Questions for Review

1. **Question #4**: If the container is full and the server targets it (server-initiated action), what should happen?
   - **Investigation Result**: No server-initiated container operations currently exist in the codebase
   - **Current Status**: Not applicable - all container operations are player-initiated
   - **Future-Proofing**: If server-initiated operations are added, should we:
     - Option A: Raise ContainerCapacityError (fail-fast, operation fails)
     - Option B: Place item in general inventory instead (fallback, operation succeeds)
     - Option C: Return user-friendly error message (operation fails, but message logged)
   - **Status**: Not needed for current implementation, but defined for future-proofing

2. Should we create a cleanup script for existing incorrectly marked items? (Current plan: Optional, only if needed)
3. Should cleanup script run automatically on server startup? (Current plan: Manual)

## Error Handling Philosophy

**Fail-Fast, Fail-Loud**: All errors must:

1. Be logged with full context (traceback, player_id, container_id, system state)
2. Raise exceptions (no silent fallbacks)
3. Terminate the operation (no partial state)
4. Provide detailed error messages for debugging

This ensures that:

- Infrastructure issues are caught immediately
- Data corruption is prevented
- Debugging is straightforward (full error context in logs)
- System state remains consistent (no partial operations)
