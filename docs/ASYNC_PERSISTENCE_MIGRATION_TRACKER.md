# Async Persistence Migration Tracker

**Created**: December 3, 2025
**Status**: Phase 2 - In Progress
**Estimated Effort**: 24-40 hours

---

## Overview

This document tracks the migration from synchronous `PersistenceLayer` methods to asynchronous `AsyncPersistenceLayer` or `asyncio.to_thread()` wrapped methods to eliminate event loop blocking.

## Current Status

**Files with Sync Persistence Calls**: 12 files
**Total Sync Method Calls**: 48 instances

### Files Requiring Migration

| File | Instances | Priority | Notes |
|------|-----------|----------|-------|
| `server/services/passive_lucidity_flux_service.py` | 1 | ✅ DONE | Fixed - using async_get_room with cache |
| `server/services/container_service.py` | 15 | 🔴 HIGH | Many sync calls |
| `server/services/npc_combat_integration_service.py` | 6 | 🟡 MEDIUM | Combat-related |
| `server/services/wearable_container_service.py` | 7 | 🟡 MEDIUM | Inventory operations |
| `server/services/user_manager.py` | 5 | 🟡 MEDIUM | User data |
| `server/services/npc_startup_service.py` | 3 | 🟢 LOW | Startup only |
| `server/services/player_position_service.py` | 2 | 🟡 MEDIUM | Movement |
| `server/services/environmental_container_loader.py` | 2 | 🟢 LOW | Startup only |
| `server/services/corpse_lifecycle_service.py` | 4 | 🟢 LOW | Death handling |
| `server/services/player_death_service.py` | 1 | 🟡 MEDIUM | Death handling |
| `server/services/player_combat_service.py` | 1 | 🟡 MEDIUM | Combat |
| `server/services/health_service.py` | 1 | 🟡 MEDIUM | HP management |

## Migration Strategy

### Phase 1: High Priority (✅ COMPLETE)
- [x] passive_lucidity_flux_service.py - Fixed with async_get_room + caching

### Phase 2: Service Layer Migration (Next)
1. container_service.py (15 instances) - Inventory management
2. wearable_container_service.py (7 instances) - Equipment
3. npc_combat_integration_service.py (6 instances) - NPC combat

### Phase 3: Supporting Services
4. user_manager.py (5 instances)
5. player_position_service.py (2 instances)
6. player_death_service.py (1 instance)
7. player_combat_service.py (1 instance)
8. health_service.py (1 instance)

### Phase 4: Startup Services (Low Priority)
9. npc_startup_service.py (3 instances) - Only runs at startup
10. environmental_container_loader.py (2 instances) - Only runs at startup
11. corpse_lifecycle_service.py (4 instances) - Infrequent operations

## Migration Pattern

### Template for Migration

```python
# ❌ BEFORE (Blocking)
async def some_method(self, item_id: str):
    item = self.persistence.get_item(item_id)  # BLOCKS EVENT LOOP
    return item

# ✅ AFTER (Non-blocking) - Option 1: Use AsyncPersistenceLayer
async def some_method(self, item_id: str):
    item = await self.async_persistence.get_item(item_id)  # Non-blocking
    return item

# ✅ AFTER (Non-blocking) - Option 2: Use asyncio.to_thread (temporary)
async def some_method(self, item_id: str):
    item = await asyncio.to_thread(self.persistence.get_item, item_id)
    return item
```

### Decision Tree

1. **Does AsyncPersistenceLayer have this method?**
   - YES → Use `await async_persistence.method()`
   - NO → Use `await asyncio.to_thread(persistence.method, args)`

2. **Is this a frequently called method?**
   - YES → Prioritize adding async method to AsyncPersistenceLayer
   - NO → asyncio.to_thread() is acceptable

3. **Is this in a critical path?**
   - YES → HIGH priority
   - NO → MEDIUM/LOW priority

## Progress Tracking

- [ ] Phase 2.1: container_service.py (15 instances)
- [ ] Phase 2.2: wearable_container_service.py (7 instances)
- [ ] Phase 2.3: npc_combat_integration_service.py (6 instances)
- [ ] Phase 3.1: user_manager.py (5 instances)
- [ ] Phase 3.2: player_position_service.py (2 instances)
- [ ] Phase 3.3: player_death_service.py (1 instance)
- [ ] Phase 3.4: player_combat_service.py (1 instance)
- [ ] Phase 3.5: health_service.py (1 instance)
- [ ] Phase 4.1: npc_startup_service.py (3 instances)
- [ ] Phase 4.2: environmental_container_loader.py (2 instances)
- [ ] Phase 4.3: corpse_lifecycle_service.py (4 instances)

## Testing Requirements

For each migrated file:
1. Run existing unit tests to ensure no regressions
2. Add performance tests to verify no event loop blocking
3. Test error handling (connection failures, etc.)
4. Test concurrent operations

## Success Criteria

- [ ] All async functions use async persistence methods or asyncio.to_thread()
- [ ] No event loop blocking detected in profiling
- [ ] All tests pass
- [ ] Performance metrics show <100ms for all operations
- [ ] No connection pool exhaustion under load

---

**Last Updated**: December 3, 2025
**Owner**: Development Team
**Estimated Completion**: 2-3 weeks (based on audit)
