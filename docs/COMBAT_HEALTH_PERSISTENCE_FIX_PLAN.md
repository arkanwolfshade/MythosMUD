# Combat Health Persistence Bug - Investigation Report and Fix Plan

**Date:** November 2, 2025
**Investigator:** Assistant (Untenured Professor of Occult Studies)
**Requester:** Professor Wolfshade

---

## Executive Summary

A critical persistence bug has been identified where player health changes during combat are **NOT** saved to the database. The player's health updates correctly in the client UI (in-memory state), but the database retains the original health value, causing state inconsistency across game sessions.

---

## Investigation Findings

### Test Scenario
1. ✅ Started local server successfully
2. ✅ Logged in as player "Ithaqua" with password "Cthulhu1"
3. ✅ Engaged in combat with "Dr. Francis Morgan" (NPC)
4. ✅ Combat concluded with Ithaqua victorious
5. ✅ Recorded Ithaqua's final health: **70 HP** (down from 100 HP)
6. ✅ Shut down server and client
7. ✅ Queried database for Ithaqua's stats

### Database Verification Results

**Client Display (In-Memory):**
```
Health: 70 HP
```

**Database Query Result:**
```sql
SELECT name, stats FROM players WHERE name = 'Ithaqua';
```

**Database Output:**
```json
{
  "strength": 10,
  "dexterity": 10,
  "constitution": 10,
  "intelligence": 10,
  "wisdom": 10,
  "charisma": 10,
  "sanity": 100,
  "occult_knowledge": 0,
  "fear": 0,
  "corruption": 0,
  "cult_affiliation": 0,
  "current_health": 100  ← SHOULD BE 70!
}
```

**Result:** ❌ MISMATCH CONFIRMED - Database shows 100 HP, client showed 70 HP

---

## Root Cause Analysis

### Missing Persistence Methods

The `PersistenceLayer` class (`server/persistence.py`) is missing **FOUR CRITICAL METHODS** that are being called throughout the codebase:

#### 1. `damage_player(player, amount, damage_type)` - **MISSING**
**Called by:** `GameMechanicsService.damage_player()` at line 152 in `server/game/mechanics.py`

```python
# server/game/mechanics.py:152
self.persistence.damage_player(player, amount, damage_type)  # ← AttributeError!
```

#### 2. `heal_player(player, amount)` - **MISSING**
**Called by:** `GameMechanicsService.heal_player()` at line 130 in `server/game/mechanics.py`

```python
# server/game/mechanics.py:130
self.persistence.heal_player(player, amount)  # ← AttributeError!
```

#### 3. `async_damage_player(player, amount, damage_type)` - **MISSING**
**Called by:** `PlayerService.damage_player()` at line 728 in `server/game/player_service.py`

```python
# server/game/player_service.py:728
await self.persistence.async_damage_player(player, amount, damage_type)  # ← AttributeError!
```

#### 4. `async_heal_player(player, amount)` - **MISSING**
**Called by:** `PlayerService.heal_player()` at line 693 in `server/game/player_service.py`

```python
# server/game/player_service.py:693
await self.persistence.async_heal_player(player, amount)  # ← AttributeError!
```

### Error Handling Path

When combat damage is applied:

1. **NPC attacks player** → `NPCCombatIntegration.apply_combat_effects()` (line 108 in `combat_integration.py`)
2. **Calls** → `GameMechanicsService.damage_player()`
3. **Calls** → `persistence.damage_player()` ← **AttributeError raised here**
4. **Error caught** → `except Exception as e:` at line 130-132 in `combat_integration.py`
5. **Logged** → `logger.error("Error applying combat effects", ...)`
6. **Returns** → `False` (silent failure)
7. **Game continues** → Player's in-memory stats update via other mechanisms
8. **Database** → Never updated!

### Why the Client Shows Updated Health

The client receives updated health through the `PlayerHPUpdated` event and real-time WebSocket updates, which rely on the **in-memory** player object. The game state manager maintains the current health in memory, but this is never flushed to the database because the persistence methods don't exist.

---

## Test Coverage

Created comprehensive test suite: `server/tests/unit/persistence/test_player_health_persistence.py`

**Tests included:**
1. ✅ `test_damage_player_method_exists()` - Verify method exists
2. ✅ `test_heal_player_method_exists()` - Verify method exists
3. ✅ `test_damage_player_persists_to_database()` - Test persistence flow
4. ✅ `test_heal_player_persists_to_database()` - Test persistence flow
5. ✅ `test_combat_damage_flow()` - End-to-end combat damage test
6. ✅ `test_async_damage_player_method_exists()` - Verify async method exists
7. ✅ `test_async_heal_player_method_exists()` - Verify async method exists

---

## Proposed Fix Plan

### Phase 1: Implement Missing Synchronous Methods

**File:** `server/persistence.py`

Add these methods to the `PersistenceLayer` class:

```python
def damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
    """
    Damage a player and persist health changes to the database.

    Args:
        player: The player object to damage
        amount: Amount of damage to apply
        damage_type: Type of damage (for future extension)
    """
    try:
        # Get current stats
        stats = player.get_stats()
        current_health = stats.get("current_health", 100)

        # Calculate new health (minimum 0)
        new_health = max(0, current_health - amount)

        # Update stats
        stats["current_health"] = new_health
        player.set_stats(stats)

        # Persist to database
        self.save_player(player)

        logger.info(
            "Player health reduced and persisted",
            player_id=player.player_id,
            player_name=player.name,
            damage=amount,
            old_health=current_health,
            new_health=new_health,
            damage_type=damage_type
        )
    except Exception as e:
        logger.error(
            "Error damaging player",
            player_id=player.player_id,
            amount=amount,
            error=str(e),
            exc_info=True
        )
        raise


def heal_player(self, player: Player, amount: int) -> None:
    """
    Heal a player and persist health changes to the database.

    Args:
        player: The player object to heal
        amount: Amount of healing to apply
    """
    try:
        # Get current stats
        stats = player.get_stats()
        current_health = stats.get("current_health", 100)
        max_health = 100  # TODO: Make this configurable or player-specific

        # Calculate new health (capped at max)
        new_health = min(max_health, current_health + amount)

        # Update stats
        stats["current_health"] = new_health
        player.set_stats(stats)

        # Persist to database
        self.save_player(player)

        logger.info(
            "Player health increased and persisted",
            player_id=player.player_id,
            player_name=player.name,
            healing=amount,
            old_health=current_health,
            new_health=new_health
        )
    except Exception as e:
        logger.error(
            "Error healing player",
            player_id=player.player_id,
            amount=amount,
            error=str(e),
            exc_info=True
        )
        raise
```

### Phase 2: Implement Missing Asynchronous Methods

**File:** `server/persistence.py`

Add async wrapper methods for the PlayerService:

```python
async def async_damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
    """
    Async wrapper for damage_player to support async contexts.

    Args:
        player: The player object to damage
        amount: Amount of damage to apply
        damage_type: Type of damage
    """
    # Since the underlying operations are synchronous (SQLite),
    # we can call the sync version directly
    # In the future, this could use asyncio.to_thread() for true async
    self.damage_player(player, amount, damage_type)


async def async_heal_player(self, player: Player, amount: int) -> None:
    """
    Async wrapper for heal_player to support async contexts.

    Args:
        player: The player object to heal
        amount: Amount of healing to apply
    """
    # Since the underlying operations are synchronous (SQLite),
    # we can call the sync version directly
    # In the future, this could use asyncio.to_thread() for true async
    self.heal_player(player, amount)
```

### Phase 3: Add Import Statement

**File:** `server/persistence.py`

Ensure proper import at the top of the file:

```python
from .logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)
```

### Phase 4: Update Tests

Run the new test suite to verify the fix:

```bash
make test-server
```

Expected results:
- All tests in `test_player_health_persistence.py` should PASS
- Combat damage should persist to database
- No regressions in existing tests

---

## Files to Modify

### Primary Changes
1. **server/persistence.py**
   - Add `damage_player()` method (sync)
   - Add `heal_player()` method (sync)
   - Add `async_damage_player()` method (async wrapper)
   - Add `async_heal_player()` method (async wrapper)

### Test Files
2. **server/tests/unit/persistence/test_player_health_persistence.py** (CREATED)
   - Comprehensive test coverage for the new methods

---

## Risk Assessment

### Low Risk
- ✅ Adding new methods to existing class (no breaking changes)
- ✅ Following established patterns in codebase
- ✅ Using existing `save_player()` method (already tested)
- ✅ Using existing `get_stats()` and `set_stats()` methods

### Medium Risk
- ⚠️ Tests are currently mocking these methods (expecting them to exist)
- ⚠️ Combat system depends on these methods working correctly
- ⚠️ May need to update existing mock objects in tests

### Mitigation
- Run full test suite after implementation
- Test in isolated environment before deployment
- Verify no regressions in combat system
- Check logs for any AttributeError exceptions after fix

---

## Expected Outcomes

### After Fix Implementation

1. **Database Persistence:**
   - Player health changes persist immediately after combat damage
   - Database `current_health` value matches in-game health
   - Health persists across server restarts and player reconnections

2. **Error Resolution:**
   - No more `AttributeError` exceptions for missing methods
   - Combat errors log should no longer show "Error applying combat effects"
   - All combat damage flows work correctly

3. **Test Results:**
   - All 7 tests in `test_player_health_persistence.py` PASS
   - Existing combat tests continue to PASS
   - No regressions in test suite

---

## Additional Discoveries During Investigation

### WebSocket Connection Bug FIXED

During the investigation, a **critical WebSocket connection issue** was discovered and fixed:

**Issue:** WebSocket connections were failing immediately after the client entered the game.

**Root Cause:** Server was not properly negotiating WebSocket subprotocols. The client sends `['bearer', <token>]` as subprotocols, but the server wasn't selecting one during the handshake.

**Files Fixed:**
1. `server/api/real_time.py` (lines 122-125, 321-324)
   - Accept WebSocket before closing on readiness gate failures
2. `server/realtime/connection_manager.py` (line 429)
   - Accept WebSocket with `subprotocol='bearer'` negotiation

**Result:** ✅ WebSocket connections now work correctly

---

## Phase 5: CRITICAL - Fix Silent Error Logging (NEW)

### Problem Identified

During investigation, Professor Wolfshade identified a **critical observability issue**: AttributeError exceptions from missing persistence methods were being caught but **NEVER logged to errors.log**.

**Root Cause:**
The `errors.log` file only captures logs from modules with prefix "errors", not ERROR-level logs from all modules!

**File:** `server/logging/enhanced_logging_config.py` (line 497)

```python
# CURRENT (BROKEN)
log_categories = {
    # ...
    "errors": ["errors"],  # ← Only captures "errors.*" module logs!
    # ...
}
```

This means:
- ❌ `server.npc.combat_integration` errors → NOT in errors.log
- ❌ `server.game.mechanics` errors → NOT in errors.log
- ❌ `server.persistence` errors → NOT in errors.log
- ❌ **ALL critical failures are invisible in errors.log!**

### Solution: Enhanced Error Handler

Add a **global ERROR-level handler** to route ALL ERROR and CRITICAL logs to errors.log, regardless of module:

**File:** `server/logging/enhanced_logging_config.py`

**Location:** After line 620 (after creating the errors_handler)

```python
# CRITICAL FIX: Route ALL ERROR and CRITICAL logs to errors.log
# Current errors.log only captures "errors.*" prefix modules
# This ensures ALL error-level logs from ANY module are captured
errors_handler.setLevel(logging.ERROR)  # Change from WARNING to ERROR
root_logger.addHandler(errors_handler)  # Already exists

# Add a SECOND errors-only handler that captures from ALL modules
critical_errors_handler = handler_class(
    errors_log_path,  # Same file
    maxBytes=max_bytes,
    backupCount=backup_count,
    encoding="utf-8",
)
critical_errors_handler.setLevel(logging.ERROR)  # ERROR and above only
critical_errors_handler.setFormatter(errors_formatter)

# Add to root logger to capture ALL errors
root_logger.addHandler(critical_errors_handler)

logger.info(
    "Enhanced error logging configured",
    errors_log_path=str(errors_log_path),
    captures_all_errors=True
)
```

### Alternative Solution: Module-Level Error Routing

Add NPC and game mechanics modules to errors.log routing:

```python
# ALTERNATIVE: Expand errors.log to include critical modules
log_categories = {
    # ...
    "errors": [
        "errors",
        "npc.combat_integration",  # Add combat errors
        "game.mechanics",           # Add game mechanics errors
        "persistence",              # Add persistence errors
        "combat",                   # Add all combat errors
    ],
    # ...
}
```

**Recommendation:** Use BOTH approaches for comprehensive error capture.

### Enhanced Exception Handling

**File:** `server/npc/combat_integration.py` (lines 130-132)

**CURRENT (SUPPRESSES ERRORS):**
```python
except Exception as e:
    logger.error("Error applying combat effects", target_id=target_id, error=str(e))
    return False  # Silent failure!
```

**IMPROVED (ESCALATES CRITICAL ERRORS):**
```python
except AttributeError as e:
    # CRITICAL: Missing method in persistence layer
    logger.critical(
        "CRITICAL: Missing persistence method called",
        target_id=target_id,
        error=str(e),
        error_type="AttributeError",
        stacktrace=True,
        exc_info=True
    )
    # Re-raise AttributeError - these are programming errors, not runtime errors
    raise
except ValidationError as e:
    # Expected validation error - log and return False
    logger.warning("Validation error in combat effects", target_id=target_id, error=str(e))
    return False
except Exception as e:
    # Unexpected error - log with full context and re-raise
    logger.error(
        "Unexpected error applying combat effects",
        target_id=target_id,
        error=str(e),
        error_type=type(e).__name__,
        exc_info=True
    )
    # For unexpected errors, we should investigate rather than silently continue
    raise
```

### Add Monitoring Alerts

**File:** `server/logging/enhanced_logging_config.py`

Add a new processor to detect and alert on critical patterns:

```python
def alert_on_critical_errors(_logger: Any, _name: str, event_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Alert on critical error patterns that indicate bugs or system issues.

    Patterns to alert on:
    - AttributeError (usually programming errors)
    - Missing persistence methods
    - Database write failures
    """
    if event_dict.get("level") == "critical":
        # Could integrate with alerting system (Sentry, PagerDuty, etc.)
        # For now, ensure it's prominently logged
        event_dict["ALERT"] = "CRITICAL_ERROR_DETECTED"

    error_msg = str(event_dict.get("error", ""))
    if "AttributeError" in error_msg or "has no attribute" in error_msg:
        event_dict["ALERT"] = "MISSING_METHOD_ERROR"
        event_dict["severity"] = "CRITICAL"

    return event_dict
```

Add to processors list in `configure_enhanced_structlog()`:

```python
base_processors = [
    sanitize_sensitive_data,
    add_correlation_id,
    add_request_context,
    enhance_player_ids,
    alert_on_critical_errors,  # ← NEW: Alert on critical patterns
    merge_contextvars,
    # ... rest of processors
]
```

---

## Updated Risk Assessment

### Critical Observability Gaps (HIGH RISK)

- 🔴 **Silent Failures:** Critical errors not visible in centralized error log
- 🔴 **Missing Method Calls:** AttributeErrors being caught and suppressed
- 🔴 **No Alerting:** No alerts or notifications for critical failures
- 🔴 **Incomplete Logging:** errors.log only captures subset of errors

### Proposed Mitigations

1. ✅ Route ALL ERROR logs to errors.log
2. ✅ Re-raise AttributeError instead of catching it
3. ✅ Add critical error detection and alerting
4. ✅ Use CRITICAL log level for programming errors
5. ✅ Add `exc_info=True` for full stack traces

---

## Next Steps

1. **Await Approval** from Professor Wolfshade
2. **Implement Phase 1-2** (persistence methods)
3. **Implement Phase 5** (error handling improvements) - **CRITICAL**
4. **Run test suite** to verify no regressions
5. **Test combat manually** to confirm persistence works
6. **Verify errors.log** contains all critical errors
7. **Commit changes** with detailed commit message

---

## References

- Player Model: `server/models/player.py` (lines 73-95: get_stats/set_stats methods)
- Combat Integration: `server/npc/combat_integration.py` (lines 90-132: apply_combat_effects)
- Game Mechanics: `server/game/mechanics.py` (lines 134-154: damage_player)
- Persistence Layer: `server/persistence.py` (lines 300-356: save_player)
- Logging Config: `server/logging/enhanced_logging_config.py` (lines 482-620: log routing)

---

## Conclusion

This investigation has revealed **TWO critical issues**:

1. **Health Persistence Bug:** Missing persistence methods prevent health changes from being saved
2. **Observability Gap:** Critical errors are being silently suppressed and not logged to errors.log

The missing persistence methods are a straightforward implementation oversight, but the silent error handling is a **systemic observability issue** that could hide many other bugs. Both must be fixed together to ensure:
- Player state persists correctly
- All critical errors are visible and actionable
- Future bugs are caught early through proper logging

**Priority:** CRITICAL - These issues affect core game functionality and debugging capabilities.

*As noted in Dr. Armitage's research on the persistence of thought-forms, what exists in memory must eventually take physical form in the permanent record... and what errors exist in the code must be made visible to those who would investigate them. The alternative is madness.*
