# NPC spawning only occurs at server startup - no periodic respawning or dynamic spawning

**Labels:** `bug`, `high-priority`, `npc-system`

## Problem Description

NPCs currently spawn **only once at server startup** based on their configured `spawn_probability`. This creates several critical gameplay issues:

- **Optional NPCs that fail their spawn probability check never appear** until the server is restarted
- **Dead NPCs never respawn** - they remain permanently dead
- **No dynamic spawning** based on game state, player activity, or time of day
- **Static world population** that cannot adapt to gameplay conditions

## Observed Behavior (Current Session)

**Startup Spawn Results (20:33:25):**
- ✅ **Dr. Francis Morgan** (required) - spawned successfully
- ✅ **Sanitarium Patient** (70% probability) - spawned successfully
- ❌ **Nightgaunt** (20% probability) - **skipped, never appeared**
- ❌ **Cultist of the Yellow Sign** (30% probability) - **skipped**
- ❌ **Deep One Hybrid** (40% probability) - **skipped**

**Result:** Players will never encounter these NPCs until the next server restart, regardless of how long they play.

## Root Cause Analysis

### 1. Startup-Only Spawning
**Location:** `server/app/lifespan.py` line 182
```python
startup_results = await startup_service.spawn_npcs_on_startup()
```
This is called **once** during server initialization and never again.

### 2. Disabled Event-Based Spawning
**Location:** `server/npc/spawning_service.py` lines 148-151
```python
# NOTE: Removed PlayerEnteredRoom subscription to prevent duplicate spawning
# The population controller is the sole authority for spawn decisions
# self.event_bus.subscribe(PlayerEnteredRoom, self._handle_player_entered_room)
```
Event-based spawning was disabled to fix NPC duplication bugs (documented in `docs/archive/NPC_DUPLICATION_BUG_FIX_PLAN.md`), but **no periodic system replaced it**.

### 3. Orphaned Respawn System
**Location:** `server/npc/lifecycle_manager.py` line 649
```python
def periodic_maintenance(self) -> dict[str, Any]:
    """Perform periodic maintenance tasks."""
    # Process respawn queue
    respawned_count = self.process_respawn_queue()
    # Cleanup old records
    cleaned_count = self.cleanup_old_records()
```

This method exists with full respawn logic but is **never called** - it only appears in unit tests!

### 4. No NPC Maintenance in Game Tick Loop
**Location:** `server/app/lifespan.py` line 349 (`game_tick_loop`)

The game tick processes:
- ✅ Combat auto-progression (line 367-371)
- ✅ HP decay for mortally wounded players (line 374-428)
- ❌ **NPC lifecycle maintenance - MISSING**

## Current vs Expected Behavior

### Current (Broken)
| NPC Type | Startup Behavior | Death Behavior | Dynamic Spawning |
|----------|-----------------|----------------|------------------|
| Required NPCs | ✅ Always spawn | ❌ Never respawn | ❌ None |
| Optional NPCs | ⚠️ Probability-based (one-time) | ❌ Never respawn | ❌ None |
| All NPCs | 🎲 RNG at startup only | 💀 Permanent death | 🚫 Static world |

### Expected (Correct)
| NPC Type | Startup Behavior | Death Behavior | Dynamic Spawning |
|----------|-----------------|----------------|------------------|
| Required NPCs | ✅ Always spawn | ✅ Respawn after delay | ✅ Ensure minimum population |
| Optional NPCs | ✅ Probability-based | ✅ Respawn after delay | ✅ Re-roll periodically |
| All NPCs | 🎲 Initial RNG | ⏰ Auto-respawn (5 min default) | 📊 Population management |

## Implementation Plan

### Phase 1: Integrate NPC Maintenance into Game Tick ⚙️
**File:** `server/app/lifespan.py`

Add to `game_tick_loop()` after combat/HP decay processing:
```python
# Process NPC lifecycle maintenance (every 60 ticks = 1 minute)
if tick_count % 60 == 0 and hasattr(app.state.container, 'npc_lifecycle_manager'):
    try:
        maintenance_results = app.state.container.npc_lifecycle_manager.periodic_maintenance()
        if maintenance_results.get('respawned_npcs', 0) > 0:
            logger.info("NPC maintenance completed", **maintenance_results)
    except Exception as e:
        logger.error("Error during NPC maintenance", tick_count=tick_count, error=str(e))
```

**Configuration:**
- `default_respawn_delay = 300.0` (5 minutes) - already configured in lifecycle_manager.py line 192
- `cleanup_interval = 3600.0` (1 hour) - already configured in lifecycle_manager.py line 195

### Phase 2: Implement Periodic Spawn Checks 🎲
**File:** `server/npc/lifecycle_manager.py`

Enhance `periodic_maintenance()` to add spawn checks:
```python
def periodic_maintenance(self) -> dict[str, Any]:
    current_time = time.time()
    results = {}

    # Process respawn queue (existing)
    respawned_count = self.process_respawn_queue()
    results["respawned_npcs"] = respawned_count

    # NEW: Check for optional NPCs that should re-roll spawn probability
    spawn_check_results = self._check_optional_npc_spawns()
    results["spawn_checks"] = spawn_check_results

    # Cleanup old records (existing)
    if current_time - self.last_cleanup > self.cleanup_interval:
        cleaned_count = self.cleanup_old_records()
        results["cleaned_records"] = cleaned_count
        self.last_cleanup = current_time

    return results
```

Add new method:
```python
def _check_optional_npc_spawns(self) -> dict[str, int]:
    """Check if optional NPCs should spawn based on periodic probability rolls."""
    # Get all optional NPC definitions from population_controller
    # For each definition:
    #   - Check current population vs max_population
    #   - If under limit, roll spawn probability
    #   - If successful, spawn NPC in configured room
    # Return stats on checks performed and NPCs spawned
```

### Phase 3: Add Configuration 🔧
**File:** Create `server/config/npc_config.py`

```python
class NPCMaintenanceConfig:
    """Configuration for NPC lifecycle maintenance."""

    # How often to run NPC maintenance (in game ticks)
    MAINTENANCE_INTERVAL_TICKS: int = 60  # Every minute

    # How often to re-roll optional NPC spawns (in seconds)
    SPAWN_REROLL_INTERVAL: float = 600.0  # Every 10 minutes

    # Respawn delay overrides per NPC type
    RESPAWN_DELAYS: dict[str, float] = {
        "quest_giver": 600.0,      # 10 minutes
        "shopkeeper": 300.0,        # 5 minutes (default)
        "passive_mob": 180.0,       # 3 minutes
        "aggressive_mob": 300.0,    # 5 minutes
    }

    # Spawn check interval per NPC (prevents spam)
    MIN_SPAWN_CHECK_INTERVAL: float = 300.0  # 5 minutes between checks
```

## Files Affected
- `server/app/lifespan.py` - Add NPC maintenance to game tick loop (~10 lines)
- `server/npc/lifecycle_manager.py` - Enhance periodic_maintenance() and add spawn checking (~80 lines)
- `server/config/npc_config.py` - New configuration file (~30 lines)
- `server/tests/unit/npc/test_npc_lifecycle_manager.py` - Add tests for new functionality (~100 lines)
- `server/tests/integration/npc/test_npc_periodic_spawning.py` - New integration test file (~150 lines)

## Testing Checklist
- [ ] Optional NPCs spawn over time (not just at startup)
- [ ] Dead NPCs respawn after configured delay (300 seconds default)
- [ ] Population limits (`max_population`) are respected
- [ ] No duplicate spawning occurs
- [ ] Performance impact is negligible (< 1ms per maintenance cycle)
- [ ] Spawn probability calculations work correctly over time
- [ ] Configuration values are respected
- [ ] Maintenance runs every 60 ticks (1 minute) as configured
- [ ] Respawn queue is processed correctly
- [ ] Cleanup removes old lifecycle records after 1 hour

## Additional Context

**Related Documentation:**
- `docs/archive/NPC_DUPLICATION_BUG_FIX_PLAN.md` - Why event-based spawning was disabled
- `docs/archive/NPC_STARTUP_DUPLICATION_ANALYSIS.md` - Previous spawning issues

**Configuration Reference (Already Defined):**
- Default respawn delay: 300 seconds (5 minutes) - `lifecycle_manager.py` line 192
- Death suppression: 30 seconds after death - `lifecycle_manager.py` line 193
- Max respawn attempts: 3 - `lifecycle_manager.py` line 194
- Cleanup interval: 3600 seconds (1 hour) - `lifecycle_manager.py` line 195

**Existing Infrastructure Ready to Use:**
- ✅ `lifecycle_manager.process_respawn_queue()` - fully implemented
- ✅ `lifecycle_manager.cleanup_old_records()` - fully implemented
- ✅ `lifecycle_manager.respawn_queue` - data structure ready
- ✅ Population tracking - `population_controller.active_npcs`
- ✅ NPC definitions - `population_controller.npc_definitions`

## Impact
**Severity:** High - Blocks core NPC gameplay features
**Affected Systems:** NPC spawning, combat, quests, world population, player progression
**Workaround:** Restart server to re-roll NPC spawns (not viable for production)

## Next Steps
1. Implement Phase 1 (game tick integration) - **Highest Priority**
2. Write integration tests to verify respawning works
3. Implement Phase 2 (periodic spawn checks) - **Medium Priority**
4. Write unit tests for spawn probability logic
5. Implement Phase 3 (configuration) - **Lower Priority, can use defaults**
6. Performance testing to ensure < 1ms overhead per tick
