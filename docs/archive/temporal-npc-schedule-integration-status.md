# Temporal NPC Schedule Integration Status

**Status**: Partial Implementation (Infrastructure Complete, NPC Integration Missing)

**Last Updated**: 2026-01-02

**Related Documentation**: `docs/TEMPORAL_SYSTEM_RESEARCH.md`

---

## Overview

NPC schedules define when NPCs (particularly shopkeepers) should be active based on Mythos time. The schedule system infrastructure exists and tracks active schedules, but NPCs do not currently respond to schedule state changes (e.g., shops don't open/close based on schedule times).

---

## Current Implementation Status

### ✅ Completed (Infrastructure)

1. **Schedule Data Storage**
   - Database table: `calendar_npc_schedules` (defined in `db/schema/01_world_and_calendar.sql`)
   - Schedule data files: `data/{environment}/calendar/schedules/npc.json`
   - Schedule model: `server/models/calendar.py` (`NPCScheduleModel`)
   - Schedule schema: `server/schemas/calendar.py` (`ScheduleEntry`)

2. **Schedule Service**
   - `server/services/schedule_service.py` - Loads schedules from database
   - `get_active_entries()` method - Determines which schedules are active at given time
   - Schedules include:
     - `start_hour` / `end_hour` - Time window
     - `days` - Days of week when schedule applies
     - `applies_to` - NPC types (e.g., ["shopkeeper", "vendor"])
     - `effects` - Effects when active (e.g., ["shops_open", "discount_minor"])

3. **Time Event Integration**
   - `server/time/time_event_consumer.py` - `MythosTimeEventConsumer` class
   - `_handle_tick()` method calls:
     - `schedule_service.get_active_entries()` to get active schedules
     - `npc_lifecycle_manager.apply_schedule_state(active_schedules)` to update NPC state

4. **NPC Lifecycle Manager Integration**
   - `server/npc/lifecycle_manager.py` - `NPCLifecycleManager.apply_schedule_state()` method
   - Stores active schedule IDs in `self.active_schedule_ids`
   - Logs schedule state updates

### ❌ Not Yet Implemented (NPC Response)

1. **NPC Schedule Checking**
   - NPCs (specifically `ShopkeeperNPC`) do not check if they should be active based on schedules
   - No logic to determine if a shopkeeper should be "open" or "closed"
   - No response to schedule effects like "shops_open"

2. **Shop Open/Close Behavior**
   - `server/npc/shopkeeper_npc.py` - `ShopkeeperNPC` class exists but:
     - Does not check schedule state
     - Does not have "open" / "closed" state
     - Does not respond to schedule effects
     - No logic to prevent transactions when shop is "closed"

3. **Schedule Effect Processing**
   - Schedule effects (e.g., "shops_open", "discount_minor") are defined but not used
   - No system to map schedule effects to NPC behaviors
   - No effect handlers or processors

---

## Schedule Data Example

From `data/local/calendar/schedules/npc.json`:

```json
{
  "id": "arkham_shop_day_shift",
  "name": "Arkham Shop Day Shift",
  "category": "npc",
  "start_hour": 8,
  "end_hour": 20,
  "days": ["Primus", "Secundus", "Tertius", "Quartus", "Quintus"],
  "applies_to": ["shopkeeper", "vendor"],
  "effects": ["shops_open", "discount_minor"],
  "notes": "Standard mercantile hours while the sun provides minimal protection."
}
```

This schedule indicates:

- Shops should be open from 8:00 to 20:00 (8 AM to 8 PM)
- Applies to shopkeepers and vendors
- When active, effects include "shops_open" and "discount_minor"

---

## Required Implementation

### 1. NPC Schedule State Access

NPCs need a way to check if they should be active based on schedules:

**Option A: Direct Access to Schedule Service**

- NPCs have access to `ScheduleService` instance
- NPCs query active schedules matching their type
- NPCs check if "shops_open" effect is active

**Option B: Schedule State in NPC Lifecycle Manager**

- `NPCLifecycleManager` provides method to check schedule state for NPC type
- `is_schedule_active(npc_type: str, effect: str) -> bool`
- NPCs query lifecycle manager for schedule state

**Option C: Schedule State Passed to NPCs**

- Schedule state passed to NPCs during tick/update
- NPCs receive active schedule effects relevant to their type
- NPCs update internal state based on schedules

### 2. Shopkeeper Open/Close State

`ShopkeeperNPC` needs:

```python
class ShopkeeperNPC(NPCBase):
    def __init__(self, ...):
        super().__init__(...)
        self._is_open = True  # Default state

    def is_shop_open(self) -> bool:
        """Check if shop is currently open based on schedule."""
        # Check schedule state via lifecycle manager or schedule service
        # Return True if "shops_open" effect is active for shopkeeper type
        pass

    def buy_from_player(self, player_id: str, item: dict[str, Any]) -> bool:
        """Buy item from player."""
        if not self.is_shop_open():
            # Return False or send message to player
            return False
        # ... existing buy logic ...

    def sell_to_player(self, player_id: str, item_id: str, quantity: int = 1) -> bool:
        """Sell item to player."""
        if not self.is_shop_open():
            # Return False or send message to player
            return False
        # ... existing sell logic ...
```

### 3. Schedule Effect Processing

System to process schedule effects:

```python
# In NPCLifecycleManager or separate service
def process_schedule_effects(active_schedules: list[ScheduleEntry]) -> dict[str, set[str]]:
    """
    Process schedule effects grouped by applies_to type.

    Returns:
        dict mapping NPC type to set of active effects
        e.g., {"shopkeeper": {"shops_open", "discount_minor"}}
    """
    effects_by_type: dict[str, set[str]] = {}
    for schedule in active_schedules:
        for npc_type in schedule.applies_to:
            if npc_type not in effects_by_type:
                effects_by_type[npc_type] = set()
            effects_by_type[npc_type].update(schedule.effects)
    return effects_by_type
```

### 4. NPC Update Cycle

NPCs need periodic updates to check schedule state:

- Option: NPCs check schedule state when processing buy/sell requests
- Option: NPCs receive schedule updates via events/messages
- Option: NPCs poll schedule state during tick/update cycles

---

## Implementation Recommendations

### Phase 1: Basic Shop Open/Close

1. Add schedule state checking to `ShopkeeperNPC`
2. Implement `is_shop_open()` method that checks for "shops_open" effect
3. Prevent buy/sell transactions when shop is closed
4. Add player-facing messages ("The shop is closed. Come back during business hours.")

### Phase 2: Schedule Effect Processing

1. Create schedule effect processor in `NPCLifecycleManager`
2. Group effects by NPC type
3. Provide method for NPCs to query active effects
4. Support multiple effects (e.g., "shops_open" + "discount_minor")

### Phase 3: Advanced Features

1. NPC state transitions (open/closed animations, messages)
2. Discount application based on schedule effects
3. Schedule-dependent NPC behaviors (patrol routes, etc.)
4. Client-side UI indicators (shop open/closed status)

---

## Testing Considerations

### Unit Tests

1. **Schedule Service**
   - Test `get_active_entries()` with various times
   - Test schedule matching (hours, days, applies_to)

2. **Shopkeeper NPC**
   - Test `is_shop_open()` returns correct state
   - Test buy/sell blocked when closed
   - Test buy/sell allowed when open

3. **Schedule Effect Processing**
   - Test effect grouping by NPC type
   - Test multiple effects per NPC type
   - Test effect activation/deactivation

### Integration Tests

1. **Time-Based Shop State**
   - Spawn shopkeeper NPC
   - Advance time past schedule end
   - Verify shop becomes closed
   - Advance time to schedule start
   - Verify shop becomes open

2. **Player Transactions**
   - Player attempts to buy when shop closed
   - Verify transaction fails with appropriate message
   - Player attempts to buy when shop open
   - Verify transaction succeeds

---

## Related Files

### Database/Schema

- `db/schema/01_world_and_calendar.sql` - `calendar_npc_schedules` table
- `data/{environment}/calendar/schedules/npc.json` - Schedule data files

### Server-Side

- `server/services/schedule_service.py` - Schedule service (infrastructure complete)
- `server/time/time_event_consumer.py` - Time event consumer (calls apply_schedule_state)
- `server/npc/lifecycle_manager.py` - NPC lifecycle manager (stores schedule state)
- `server/npc/shopkeeper_npc.py` - Shopkeeper NPC (needs schedule integration)
- `server/models/calendar.py` - Schedule models
- `server/schemas/calendar.py` - Schedule schemas

---

## Summary

**Current State**: The schedule system infrastructure is complete - schedules are loaded, tracked, and active schedules are determined based on time. However, NPCs (specifically shopkeepers) do not respond to schedule state changes. Shops are always "open" and do not close based on schedule times.

**Required Work**: Integrate schedule state checking into NPCs, particularly `ShopkeeperNPC`, so that shops open/close based on schedule times and effects are processed and applied to NPC behaviors.

---

## References

- `docs/TEMPORAL_SYSTEM_RESEARCH.md` - Temporal system documentation
- `server/services/schedule_service.py` - Schedule service implementation
- `server/npc/shopkeeper_npc.py` - Shopkeeper NPC implementation
- `server/npc/lifecycle_manager.py` - NPC lifecycle manager
