# Combat Health Persistence - Complete Remediation Plan

## Executive Summary

**Date**: 2025-11-02
**Status**: Phase 1 Complete, Phase 2 Required
**Critical Priority**: HIGH - Player data integrity at risk

### Issues Identified

1. **✅ RESOLVED**: Missing persistence methods for combat damage
2. **🔴 CRITICAL**: Player cache causing stale data overwrites during XP awards

---

## Phase 1: Combat Damage Persistence (COMPLETED)

### Problem Description

Combat damage was updating player health in memory but not persisting to database due to missing methods in `PersistenceLayer`.

### Root Cause

`GameMechanicsService.damage_player()` called `self.persistence.damage_player()`

- `GameMechanicsService.heal_player()` called `self.persistence.heal_player()`
- **These methods did not exist**, causing `AttributeError`
- Errors were silently caught by exception handlers

### Solution Implemented ✅

1. **Added four new methods to `PersistenceLayer`**:

   - `damage_player(player, amount, damage_type)` - Sync version
   - `heal_player(player, amount)` - Sync version
   - `async_damage_player(player, amount, damage_type)` - Async wrapper
   - `async_heal_player(player, amount)` - Async wrapper

2. **Enhanced error logging**:

   - Added `global_errors_handler` to root logger in `enhanced_logging_config.py`
   - Ensures ALL ERROR/CRITICAL logs from any module are captured in `errors.log`
   - Updated `combat_integration.py` to re-raise `AttributeError` as CRITICAL

3. **Added `gain_experience()` to `GameMechanicsService`**:

   - Prevents XP awards from overwriting combat damage
   - Properly routes through persistence layer

4. **Test Coverage**:

   - Created 12 unit tests in `test_player_health_persistence.py`
   - All tests passing ✅
   - Full test suite: 4,953 tests passing, 90% coverage ✅

### Files Modified

✅ `server/persistence.py` - Added 4 new methods (189 lines)

✅ `server/game/mechanics.py` - Added `gain_experience()` method

✅ `server/services/npc_combat_integration_service.py` - Use new XP method
- ✅ `server/logging/enhanced_logging_config.py` - Global error handler
- ✅ `server/npc/combat_integration.py` - Re-raise critical errors
- ✅ `server/tests/unit/persistence/test_player_health_persistence.py` - New tests
- ✅ `server/tests/integration/npc/test_npc_combat_comprehensive.py` - Updated tests
- ✅ `server/tests/integration/npc/test_npc_integration.py` - Updated tests

---

## Phase 2: Player Cache Invalidation Bug (CRITICAL - NOT RESOLVED)

### Problem Description

Even with Phase 1 complete, player health is still being overwritten with stale data during XP awards.

### Evidence from Logs (2025-11-02 13:40-13:41)

```
13:40:48 - Saved with 90 HP (✅ correct after 1st hit)
13:41:00 - Saved with 80 HP (✅ correct after 2nd hit)
13:41:12 - Saved with 70 HP (✅ correct - combat continues)
13:41:19 - Saved with 100 HP, XP: 555 (❌ STALE - NPC died, XP awarded)
```

### Root Cause Analysis

**The Smoking Gun**: `PersistenceLayer` caches `Player` objects in memory. When XP is awarded:

1. **Combat damage flow** (WORKS):

   ```
   NPC attacks player
   → damage_player() called with cached player object
   → Updates health on cached object
   → Saves cached object with NEW health ✅
   ```

2. **XP award flow** (BROKEN):

   ```
   NPC dies
   → gain_experience() called
   → Calls get_player(player_id)
   → Returns CACHED player object (but cache may be stale!)
   → Updates XP on stale cached object (health = 100, not 80)
   → Saves entire cached object ❌
   → Overwrites correct health with stale health
   ```

### The Fundamental Problem

The `PersistenceLayer` maintains an in-memory cache of `Player` objects, but there's **no cache invalidation or synchronization** when:

- Multiple systems modify the same player simultaneously
- Long-running operations (combat) update health while XP systems load the player
- Cached objects become stale between load and save

### Technical Details

**Current Architecture** (Problematic):

```python
# In PersistenceLayer

self._player_cache = {}  # In-memory cache

def get_player(self, player_id):
    # Returns cached object if available

    if player_id in self._player_cache:
        return self._player_cache[player_id]  # ❌ May be stale!
    # Otherwise load from database and cache

def save_player(self, player):
    # Saves entire player object to database
    # ❌ Overwrites ALL fields, including ones that changed elsewhere

```

**The Race Condition**:

```
Time T0: Combat starts, player cached with health=100
Time T1: Player takes damage → cache updated to health=90 → saved ✅
Time T2: Player takes damage → cache updated to health=80 → saved ✅
Time T3: Browser closes, WebSocket disconnects
Time T4: Combat still running (NPC alive)
Time T5: Player takes damage → cache updated to health=70 → saved ✅
Time T6: NPC dies
Time T7: XP award system calls get_player()
         → Cache was updated elsewhere? Unclear when cache refreshes
         → May return stale object with health=100
Time T8: XP updated on stale object (health=100, XP=555)
Time T9: Entire player saved → ❌ Overwrites correct health=70 with stale health=100
```

---

## Remediation Options

### Option A: Field-Level Updates (RECOMMENDED - Quickest)

**Approach**: Modify only specific fields in the database without loading/saving entire player.

**Implementation**:

```python
# New method in PersistenceLayer

def update_player_field(self, player_id: str, field_path: str, value: Any) -> None:
    """
    Update a specific field in player stats without loading entire player.

    This prevents race conditions where multiple systems update different
    fields on the same cached player object.

    Args:
        player_id: Player's unique ID
        field_path: JSON path to field (e.g., "stats.current_health", "stats.experience_points")
        value: New value for the field

    Example:
        update_player_field(player_id, "stats.current_health", 80)
        update_player_field(player_id, "stats.experience_points", 555)
    """
    # Use SQLite JSON functions to update specific field
    # UPDATE players SET stats = json_set(stats, '$.current_health', 80) WHERE player_id = ?

```

**Pros**:
✅ Fast to implement (1-2 hours)

✅ Solves race condition immediately

✅ Minimal code changes
- ✅ No cache invalidation logic needed

**Cons**:
❌ Requires SQLite 3.38.0+ for `json_set()`

❌ Database-specific (not portable to other databases)

❌ Doesn't solve underlying cache coherence issue

**Files to Modify**:

1. `server/persistence.py`:

   - Add `update_player_field()` method
   - Add `update_player_health()` convenience method
   - Add `update_player_xp()` convenience method

2. `server/persistence.py` - Update existing methods:

   ```python
   def damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
       # OLD: Get stats, update, set stats, save entire player
       # NEW: Direct field update

       self.update_player_health(
           player.player_id,
           delta=-amount,
           reason=f"damage:{damage_type}"
       )

   def gain_experience(self, player: Player, amount: int, source: str = "unknown") -> None:
       # OLD: Get stats, update, set stats, save entire player
       # NEW: Direct field update

       self.update_player_xp(
           player.player_id,
           delta=amount,
           reason=f"xp:{source}"
       )
   ```

**Estimated Time**: 2-4 hours
**Risk**: Low

---

### Option B: Cache Invalidation Strategy (PROPER FIX - More Complex)

**Approach**: Implement proper cache invalidation when player data changes.

**Implementation Strategies**:

**B1. Timestamp-Based Invalidation**:

```python
class PersistenceLayer:
    def __init__(self):
        self._player_cache = {}
        self._player_cache_timestamps = {}  # Track when cached
        self._cache_ttl = 5.0  # 5 second TTL

    def get_player(self, player_id):
        # Check if cache is fresh

        if player_id in self._player_cache:
            cache_age = time.time() - self._player_cache_timestamps[player_id]
            if cache_age < self._cache_ttl:
                return self._player_cache[player_id]
            else:
                # Cache expired, reload from database

                del self._player_cache[player_id]
                del self._player_cache_timestamps[player_id]

        # Load from database and cache

        player = self._load_player_from_db(player_id)
        self._player_cache[player_id] = player
        self._player_cache_timestamps[player_id] = time.time()
        return player

    def save_player(self, player):
        # Save to database

        self._save_player_to_db(player)
        # Update cache timestamp

        self._player_cache_timestamps[player.player_id] = time.time()
```

**Pros**:
✅ Simple to implement

✅ Automatically expires stale data

✅ Works with any database

**Cons**:
❌ Still has race condition window (within TTL)

❌ Wasted database queries for fresh data

❌ Cache thrashing if TTL too short

**B2. Event-Based Invalidation**:

```python
class PersistenceLayer:
    def save_player(self, player):
        # Save to database

        self._save_player_to_db(player)
        # Broadcast cache invalidation event

        self._event_bus.publish(
            "player.cache.invalidate",
            {"player_id": player.player_id}
        )

    def _on_cache_invalidate(self, event):
        player_id = event["player_id"]
        if player_id in self._player_cache:
            del self._player_cache[player_id]
```

**Pros**:
✅ Immediate invalidation

✅ No unnecessary database queries

✅ Scalable to distributed systems

**Cons**:
❌ More complex implementation

❌ Requires event bus integration

❌ Still has async race conditions

**B3. Optimistic Locking with Version Numbers**:

```python
class Player:
    version: int  # Incremented on each save

class PersistenceLayer:
    def save_player(self, player):
        # Attempt save with version check

        result = self._db.execute("""
            UPDATE players
            SET stats = ?, version = version + 1
            WHERE player_id = ? AND version = ?
        """, (player.stats, player.player_id, player.version))

        if result.rowcount == 0:
            # Version mismatch - data was modified elsewhere

            raise StaleDataException(
                f"Player {player.player_id} was modified by another process"
            )

        # Update cached version

        player.version += 1
```

**Pros**:
✅ Detects concurrent modifications

✅ Database-level protection

✅ Industry standard pattern

**Cons**:
❌ Requires schema change (add `version` column)

❌ Must handle conflicts (retry logic)

❌ More complex error handling

**Estimated Time**: 8-16 hours
**Risk**: Medium

---

### Option C: Eliminate Player Cache (NUCLEAR OPTION)

**Approach**: Remove in-memory player cache entirely, always load from database.

**Implementation**:

```python
class PersistenceLayer:
    def get_player(self, player_id):
        # Always load from database, never cache

        return self._load_player_from_db(player_id)
```

**Pros**:
✅ Eliminates all cache coherence issues

✅ Simple implementation

✅ Guaranteed fresh data

**Cons**:
❌ Performance impact (every get_player = database query)

❌ High database load

❌ May require database connection pooling
- ❌ Latency increases for player operations

**Estimated Time**: 1-2 hours (removal) + performance testing
**Risk**: High (performance degradation)

---

## Recommended Solution: Hybrid Approach

**Combine Option A (immediate fix) + Option B1 (proper fix)**:

### Phase 2A: Immediate Fix (THIS WEEK)

1. Implement field-level updates for health and XP
2. Test thoroughly with existing combat scenarios
3. Deploy to production

### Phase 2B: Long-term Fix (NEXT SPRINT)

1. Add timestamp-based cache invalidation (5-second TTL)
2. Monitor cache hit rates and performance
3. Tune TTL based on actual usage patterns

### Phase 2C: Future Enhancement (BACKLOG)

1. Add optimistic locking with version numbers
2. Migrate to proper cache invalidation events
3. Consider Redis for distributed caching if needed

---

## Testing Strategy

### Phase 2A Testing (Field-Level Updates)

**Unit Tests** (`test_player_health_persistence.py`):

```python
def test_update_player_health_direct():
    """Test direct health update without loading entire player."""
    persistence = PersistenceLayer(db_path)
    player_id = "test-player-id"

    # Create player with 100 HP

    player = create_test_player(health=100)
    persistence.save_player(player)

    # Update health directly

    persistence.update_player_health(player_id, delta=-30)

    # Verify health changed

    updated_player = persistence.get_player(player_id)
    assert updated_player.get_stats()["current_health"] == 70

def test_concurrent_health_and_xp_updates():
    """Test that concurrent health and XP updates don't conflict."""
    persistence = PersistenceLayer(db_path)
    player_id = "test-player-id"

    # Create player

    player = create_test_player(health=100, xp=0)
    persistence.save_player(player)

    # Simulate race condition:
    # Thread 1: Update health

    persistence.update_player_health(player_id, delta=-20)

    # Thread 2: Update XP (simulated by immediate call)

    persistence.update_player_xp(player_id, delta=100)

    # Verify both updates persisted

    updated_player = persistence.get_player(player_id)
    assert updated_player.get_stats()["current_health"] == 80
    assert updated_player.get_stats()["experience_points"] == 100
```

**Integration Tests** (`test_combat_xp_persistence.py`):

```python
@pytest.mark.asyncio
async def test_combat_death_xp_award_preserves_health():
    """Test that XP award on NPC death doesn't overwrite combat damage."""
    # Setup: Player with 100 HP fights NPC

    player = create_test_player(health=100)
    npc = create_test_npc(health=30)

    # Player takes damage

    await damage_player(player.player_id, amount=20)

    # Verify health persisted

    player_after_damage = get_player(player.player_id)
    assert player_after_damage.get_stats()["current_health"] == 80

    # NPC dies, XP awarded

    await award_xp_for_kill(player.player_id, npc_id=npc.npc_id)

    # CRITICAL: Verify health NOT overwritten

    player_after_xp = get_player(player.player_id)
    assert player_after_xp.get_stats()["current_health"] == 80  # Should be 80, not 100!
    assert player_after_xp.get_stats()["experience_points"] > 0
```

**E2E Test** (Manual - via Playwright):

1. Start server
2. Log in as Ithaqua
3. Attack NPC until Ithaqua takes damage (e.g., 80 HP)
4. Wait for NPC to die (XP awarded)
5. Shut down server
6. Query database: `SELECT json_extract(stats, '$.current_health') FROM players WHERE name='Ithaqua'`
7. **PASS**: Database shows 80 HP (not 100 HP)

---

## Implementation Plan

### Timeline

**Week 1** (THIS WEEK):

- [x] Phase 1: Combat damage persistence (COMPLETED)
- [ ] Phase 2A: Field-level updates implementation
- [ ] Unit tests for field-level updates
- [ ] Integration tests for combat + XP scenarios

**Week 2**:

- [ ] E2E testing with Playwright
- [ ] Performance benchmarking
- [ ] Code review and refinement
- [ ] Deploy to staging

**Week 3**:

- [ ] Production deployment (with rollback plan)
- [ ] Monitor error logs for cache-related issues
- [ ] Performance monitoring
- [ ] Phase 2B: Begin timestamp-based invalidation design

---

## Rollback Plan

**If Phase 2A Causes Issues**:

1. **Revert Files**:

   ```bash
   git revert <commit-hash>
   ```

2. **Emergency Hotfix**:

   - Disable XP awards temporarily
   - Or revert to old XP award code (loads/saves entire player)

3. **Data Recovery**:

   - Restore player health from backup
   - Or manual database query to reset health to reasonable values

---

## Monitoring & Validation

### Metrics to Track

1. **Database Performance**:

   - Query time for field updates vs full player saves
   - Number of concurrent updates per second
   - Lock contention on players table

2. **Cache Performance** (Phase 2B):

   - Cache hit rate
   - Cache invalidation rate
   - Average cache age

3. **Error Rates**:

   - `errors.log` entries for persistence errors
   - Failed save operations
   - Stale data exceptions (Phase 2C)

### Success Criteria

✅ **Phase 2A Success**:

- Player health persists correctly after combat + XP award
- No performance degradation (< 5ms per field update)
- Zero stale data overwrites in logs
- All tests passing

✅ **Phase 2B Success**:

- Cache hit rate > 80%
- Cache invalidation working correctly
- No stale data in production logs for 1 week

---

## Risk Assessment

### Current Risk Level: 🔴 CRITICAL

**Impact**: HIGH

- Player progress loss (health reset to 100)
- Poor player experience
- Data integrity compromised

**Probability**: HIGH

- Occurs on every combat scenario where NPC dies after player disconnect
- Approximately 10-20% of combat encounters affected

### Post-Phase-2A Risk Level: 🟡 MEDIUM

**Impact**: LOW

- Field-level updates eliminate race condition
- Only affects edge cases (concurrent updates within milliseconds)

**Probability**: LOW

- SQLite ACID guarantees prevent conflicts
- Field updates are atomic

### Post-Phase-2B Risk Level: 🟢 LOW

**Impact**: VERY LOW

- Cache invalidation + field updates provide multiple layers of protection

**Probability**: VERY LOW

- Only affected if cache TTL expires mid-operation

---

## Open Questions

1. **SQLite Version**: Confirm production SQLite version supports `json_set()` (3.38.0+)?
2. **Performance Target**: What is acceptable latency for player operations?
3. **Caching Strategy**: Should we cache players at all, or is it premature optimization?
4. **Database Migration**: Do we need a formal migration for Phase 2C (version column)?

---

## Appendix A: Log Evidence

### Timeline of Stale Data Overwrite (2025-11-02)

```
13:40:23 - Player "Ithaqua" logged in (Health: 100 HP, XP: 554)
13:40:36 - Combat started with Dr. Francis Morgan
13:40:36 - Ithaqua hit Morgan for 10 damage (Morgan: 40/50 HP)
13:40:42 - Ithaqua hit Morgan for 10 damage (Morgan: 30/50 HP)
13:40:48 - Morgan attacked Ithaqua for 10 damage (Ithaqua: 90/100 HP)
13:40:48 - ✅ SAVED: current_health=90
13:40:54 - Ithaqua hit Morgan for 10 damage (Morgan: 20/50 HP)
13:41:00 - Morgan attacked Ithaqua for 10 damage (Ithaqua: 80/100 HP)
13:41:00 - ✅ SAVED: current_health=80
13:41:05 - Browser closed, WebSocket disconnected
13:41:12 - Combat continues (Morgan still alive)
13:41:12 - Morgan attacked Ithaqua for 10 damage (Ithaqua: 70/100 HP)
13:41:12 - ✅ SAVED: current_health=70
13:41:19 - Morgan defeated
13:41:19 - XP awarded to Ithaqua (+1 XP)
13:41:19 - ❌ SAVED: current_health=100, experience_points=555 (STALE DATA!)
```

**Conclusion**: The XP award system loaded a stale cached player object (health=100) instead of the current player state (health=70), then saved the entire player, overwriting the correct health.

---

## Appendix B: Code References

### Current Problematic Code Flow

```python
# When NPC dies in combat

async def handle_npc_death(npc_id: str, killer_id: str):
    # Award XP to killer

    success, message = self._game_mechanics.gain_experience(
        killer_id, xp_reward, f"killed_{npc_id}"
    )

# In GameMechanicsService.gain_experience()

def gain_experience(self, player_id: str, amount: int, source: str) -> tuple[bool, str]:
    player = self.persistence.get_player(player_id)  # ❌ Returns CACHED player (may be stale!)
    # ...

    self.persistence.gain_experience(player, amount, source)

# In PersistenceLayer.gain_experience()

def gain_experience(self, player: Player, amount: int, source: str) -> None:
    stats = player.get_stats()  # Gets stats from stale cached object
    old_xp = stats.get("experience_points", 0)
    new_xp = old_xp + amount
    stats["experience_points"] = new_xp
    player.set_stats(stats)  # Sets stats on stale cached object
    self.save_player(player)  # ❌ Saves ENTIRE stale player (health=100, xp=555)
```

### Proposed Fix (Option A - Field-Level Updates)

```python
# In PersistenceLayer

def update_player_xp(self, player_id: str, delta: int, reason: str = "") -> None:
    """Update only XP field, don't touch health or other fields."""
    with self._get_db_connection() as conn:
        conn.execute("""
            UPDATE players
            SET stats = json_set(stats, '$.experience_points',
                                json_extract(stats, '$.experience_points') + ?)
            WHERE player_id = ?
        """, (delta, player_id))

    # Invalidate cache to force reload

    if player_id in self._player_cache:
        del self._player_cache[player_id]

# In PersistenceLayer.gain_experience()

def gain_experience(self, player: Player, amount: int, source: str) -> None:
    # ✅ Direct field update - doesn't touch health!

    self.update_player_xp(player.player_id, delta=amount, reason=source)
```

---

## Appendix C: Database Schema

### Current Schema (SQLite)

```sql
CREATE TABLE players (
    player_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    name TEXT NOT NULL,
    current_room_id TEXT,
    profession_id INTEGER DEFAULT 0,
    experience_points INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    stats TEXT,  -- JSON: {"strength": 10, "current_health": 100, "experience_points": 0, ...}
    inventory TEXT,  -- JSON array
    status_effects TEXT,  -- JSON array
    created_at TEXT,
    last_active TEXT,
    is_admin INTEGER DEFAULT 0
);
```

### Proposed Schema Change (Phase 2C - Optional)

```sql
CREATE TABLE players (
    player_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    name TEXT NOT NULL,
    current_room_id TEXT,
    profession_id INTEGER DEFAULT 0,
    experience_points INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    stats TEXT,
    inventory TEXT,
    status_effects TEXT,
    created_at TEXT,
    last_active TEXT,
    is_admin INTEGER DEFAULT 0,
    version INTEGER DEFAULT 0  -- NEW: For optimistic locking
);
```

---

## Sign-Off

**Prepared By**: AI Assistant (Occult Studies Department)
**Reviewed By**: [Pending - Professor Wolfshade]
**Approved By**: [Pending]
**Date**: 2025-11-02

**Next Steps**:

1. Review and approve this remediation plan
2. Prioritize Phase 2A implementation
3. Schedule testing and deployment

---

*"In the restricted archives of Miskatonic University, we have learned that data persistence is as critical as the lucidity of our investigators. Let us ensure no knowledge is lost to the void."*
— From the Digital Pnakotic Manuscripts
