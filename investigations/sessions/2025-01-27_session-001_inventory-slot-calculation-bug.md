# Inventory Slot Calculation Bug Investigation

## Session Information
- **Date**: 2025-01-27
- **Session ID**: 001
- **Investigator**: AI Assistant
- **Status**: Investigation Complete - Remediation Planning

## Bug Description

When logged in as "ArkanWolfshade/Cthulhu1" and running the `/inventory` command, the display initially showed "1 of 20 slots in use" even though the item (Phosphor Charm) was in an equipped backpack. The expected behavior is:
- Regular inventory: "0 of 20 slots in use" (items in containers don't count)
- Container: "1 of 20 slots in use" (showing used capacity)

**Current Display:**
```
You are carrying 0 / 20 slots. Remaining capacity: 20.
1. Phosphor Charm (backpack) x1 [components=['component.charge'], lore=Synthesized in the Sanitarium chemical labs]
Equipped:
- backpack: Leather Backpack x1 [container={'lock_state': 'unlocked', 'capacity_slots': 20}]
```

**Expected Display:**
```
You are carrying 0 / 20 slots. Remaining capacity: 20.
1. Phosphor Charm (backpack) x1 [components=['component.charge'], lore=Synthesized in the Sanitarium chemical labs]
Equipped:
- backpack: Leather Backpack x1 [container={'lock_state': 'unlocked', 'capacity_slots': 20, 'slots_in_use': 1}]
```

## Root Cause Analysis

### Primary Issue: Data Synchronization Between Inventory JSON and Container Contents Table

The system uses **two separate storage mechanisms** for container items:

1. **Player Inventory JSON** (`players.inventory` JSONB column):
   - Items are stored here with `slot_type='backpack'` to indicate they're in a container
   - Used by inventory calculation to exclude container items from regular inventory count
   - **Location**: `server/commands/inventory_commands.py:650`

2. **Container Contents Table** (`container_contents` PostgreSQL table):
   - Items should be stored here when placed in containers
   - Queried by `WearableContainerService.get_wearable_containers_for_player()` to get container items
   - **Location**: `server/persistence/container_persistence.py:50-139`

### The Disconnect

**Pickup Command Flow:**
- Line 650: Sets `slot_type='backpack'` in inventory JSON
- Line 700: Adds item to player inventory JSON
- **Missing**: Does NOT add item to `container_contents` table

**Put Command Flow:**
- Line 1645: Uses `container_service.transfer_to_container()`
- Line 477: Adds item to `container_contents` table via `persistence.update_container()`
- **Correct**: Properly synchronizes both storage locations

**Inventory Display Flow:**
- Line 455: Queries `container_contents` table via `get_wearable_containers_for_player()`
- Line 323: Uses `container_contents` to calculate `slots_in_use`
- **Problem**: Returns 0 items because items aren't in the table

### Evidence from Logs

```
container_items_count=0  # Container service found 0 items
items_count=0             # container_contents is empty
slot_type='backpack'      # Item is marked as in backpack in inventory JSON
slots_in_use: 0           # Calculated from empty container_contents
```

## System Architecture

### Capacity Tracking

The system **DOES** track container capacity separately from regular inventory:

1. **Regular Inventory Capacity**:
   - Uses `DEFAULT_SLOT_CAPACITY = 20`
   - Counts items that are NOT equipped and NOT in containers
   - Items with `slot_type='backpack'` are correctly excluded
   - **Status**: ✅ Working correctly

2. **Container Capacity**:
   - Each container has its own `capacity_slots` (default 20)
   - Tracked separately per container
   - Should show: "1/20 slots in use" for backpack
   - **Status**: ❌ Not working - shows 0 because items aren't in container_contents table

### Storage Locations

- **Player Inventory JSON**: Single source for all player items (including container items)
- **Container Contents Table**: Should mirror items that are in containers
- **Current State**: Items with `slot_type='backpack'` exist in inventory JSON but NOT in container_contents table

## Fix Status

### ✅ Fixed: Regular Inventory Slot Calculation
- Items with `slot_type='backpack'` are correctly excluded from regular inventory count
- Shows "0 / 20 slots" when items are in containers

### ✅ Fixed: Container Metadata Display
- `slots_in_use` now appears in container metadata
- Format: `[container={'lock_state': 'unlocked', 'capacity_slots': 20, 'slots_in_use': 0}]`

### ❌ Remaining Issue: Container Contents Synchronization
- `slots_in_use` shows 0 instead of 1
- Items with `slot_type='backpack'` are not in `container_contents` table
- Container service can't find items because they're only in inventory JSON

## Remediation Plan

### Option 1: Auto-Place Picked Items into Equipped Containers (RECOMMENDED)

**Approach**: When items are picked up and have `slot_type='backpack'`, automatically place them into the equipped backpack container if one exists.

**Pros**:
- Maintains single source of truth (container_contents table)
- Consistent with how `put` command works
- No changes needed to inventory display logic

**Cons**:
- Requires finding equipped container during pickup
- May fail if container doesn't exist (need fallback)

**Implementation**:
1. In `handle_pickup_command()` after setting `slot_type='backpack'`:
   - Check if player has equipped backpack container
   - If yes, use `container_service.transfer_to_container()` to add item
   - If no, keep item in inventory JSON with `slot_type='backpack'` (current behavior)

**Files to Modify**:
- `server/commands/inventory_commands.py` (pickup command, ~line 650-730)

### Option 2: Dual-Read Inventory Display

**Approach**: Change inventory display to read from both inventory JSON AND container_contents table.

**Pros**:
- No changes to pickup command
- Handles both storage locations

**Cons**:
- More complex logic
- Potential for inconsistencies
- Two sources of truth

**Implementation**:
1. In `handle_inventory_command()`:
   - Query `container_contents` table (current)
   - Also scan player inventory for items with `slot_type='backpack'`
   - Merge results, deduplicating by item_instance_id

**Files to Modify**:
- `server/commands/inventory_commands.py` (inventory command, ~line 450-560)

### Option 3: Sync Mechanism

**Approach**: Create a background sync that ensures items with `slot_type='backpack'` are also in container_contents.

**Pros**:
- Handles existing data
- Can run periodically

**Cons**:
- Adds complexity
- May cause race conditions
- Doesn't fix root cause

**Implementation**:
1. Create sync function that:
   - Scans player inventory for items with `slot_type='backpack'`
   - Checks if they're in container_contents
   - Adds missing items to container_contents
2. Run sync:
   - On player login
   - Periodically
   - Or on-demand

**Files to Modify**:
- New file: `server/services/inventory_container_sync.py`
- `server/commands/inventory_commands.py` (call sync)

### Recommended Approach: Option 1

**Rationale**:
- Maintains single source of truth (container_contents table)
- Consistent with existing `put` command behavior
- Minimal changes required
- Fixes root cause, not symptoms

**Implementation Steps**:

1. **Modify Pickup Command** (`server/commands/inventory_commands.py:650-730`):
   - After setting `slot_type='backpack'`, check for equipped backpack
   - If equipped backpack exists, use container service to add item
   - If no equipped backpack, keep current behavior (item in inventory JSON)

2. **Handle Edge Cases**:
   - What if player has multiple backpacks? (Use first equipped)
   - What if backpack is full? (Fall back to inventory JSON)
   - What if container doesn't exist? (Create it or fall back)

3. **Migration for Existing Data**:
   - One-time script to sync existing items with `slot_type='backpack'` to container_contents
   - Run on server startup or via admin command

4. **Testing**:
   - Test pickup with equipped backpack
   - Test pickup without equipped backpack
   - Test pickup when backpack is full
   - Test inventory display after pickup
   - Test put/get commands still work

## Technical Details

### Key Code Locations

1. **Pickup Command**: `server/commands/inventory_commands.py:636-750`
   - Line 650: Sets `slot_type='backpack'`
   - Line 700: Adds to inventory JSON
   - **Missing**: Add to container_contents

2. **Put Command**: `server/commands/inventory_commands.py:1645`
   - Uses `container_service.transfer_to_container()`
   - **Correct**: Adds to container_contents

3. **Inventory Display**: `server/commands/inventory_commands.py:455`
   - Queries `container_contents` via `get_wearable_containers_for_player()`
   - **Problem**: Items not in table

4. **Container Service**: `server/services/container_service.py:320`
   - `transfer_to_container()` adds items to container_contents
   - **Correct**: Works as expected

### Data Flow

**Current (Broken) Flow:**
```
Pickup → Set slot_type='backpack' → Add to inventory JSON → ❌ NOT added to container_contents
Inventory Display → Query container_contents → Returns 0 items → slots_in_use = 0
```

**Fixed Flow (Option 1):**
```
Pickup → Set slot_type='backpack' → Find equipped container → Add to container_contents → ✅ Synchronized
Inventory Display → Query container_contents → Returns 1 item → slots_in_use = 1
```

## Next Steps

1. **Implement Option 1** (auto-place in equipped containers)
2. **Create migration script** for existing data
3. **Add comprehensive tests** for all scenarios
4. **Update documentation** with new behavior
