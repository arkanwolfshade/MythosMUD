# BUG INVESTIGATION REPORT: Minor Heal Spell Casting Takes More Than 1 Second

**Investigation Date:** 2025-12-14
**Investigator:** AI Assistant
**Session ID:** 2025-12-14_session-003_minor-heal-casting-delay
**Bug Report:** `minor heal` takes more than 1 second to complete casting

---

## Executive Summary

**Root Cause:** IDENTIFIED
**Severity:** HIGH
**Status:** COMPLETE

The spell casting system is failing to complete spell casts because `AsyncPersistenceLayer` is missing the `async_heal_player` method. When a healing spell completes casting, the system attempts to call `persistence.async_heal_player()`, but this method doesn't exist, causing an `AttributeError` on every game tick. This prevents the spell from ever completing, leaving the player stuck in a casting state indefinitely.

---

## Bug Description

### User Report
The user reported that casting "Minor Heal" takes significantly longer than the advertised 1 second. From the screenshot evidence:
- At `17:33:19`, the system reports: "You begin casting Minor Heal... (1 seconds)"
- At `17:33:57` (38 seconds later), the system reports: "You are already casting Minor Heal. Use 'stop' to interrupt."
- The spell never completes, leaving the player stuck in a casting state

### Expected Behavior
- Spell should complete after 1 second (the advertised casting time)
- Player should receive healing effect
- Casting state should be cleared

### Actual Behavior
- Spell never completes
- Player remains in casting state indefinitely
- Error occurs on every game tick (approximately every second)
- No healing effect is applied

---

## Evidence Collection

### Error Logs Analysis

**File:** `logs/local/errors.log`

**Key Error Pattern:**
```
error="'AsyncPersistenceLayer' object has no attribute 'async_heal_player'"
event='Error processing casting progress'
```

**Error Frequency:**
- Errors occur on every game tick starting from tick 161 (17:33:19)
- Error continues through tick 236 (17:34:40)
- Total: 76+ consecutive errors over ~80 seconds

**Sample Error Entries:**
```
2025-12-14 17:33:19 - server.game_tick - ERROR - tick_count=161 error="'AsyncPersistenceLayer' object has no attribute 'async_heal_player'"
2025-12-14 17:33:20 - server.game_tick - ERROR - tick_count=162 error="'AsyncPersistenceLayer' object has no attribute 'async_heal_player'"
...
2025-12-14 17:34:40 - server.game_tick - ERROR - tick_count=236 error="'AsyncPersistenceLayer' object has no attribute 'async_heal_player'"
```

### Code Analysis

**Call Chain:**
1. `server/app/game_tick_processing.py:235` - `process_casting_progress()` calls `magic_service.check_casting_progress()`
2. `server/game/magic/magic_service.py:336` - `check_casting_progress()` processes active castings
3. `server/game/magic/magic_service.py:355` - `_complete_casting()` is called when casting completes
4. `server/game/magic/magic_service.py:398` - `spell_effects.process_effect()` is called
5. `server/game/magic/spell_effects.py:109` - `_process_heal()` calls `player_service.heal_player()`
6. `server/game/player_service.py:710` - `heal_player()` calls `persistence.async_heal_player()` ❌ **METHOD DOES NOT EXIST**

**Missing Method:**
- `AsyncPersistenceLayer.async_heal_player()` is called but does not exist
- `HealthRepository.heal_player()` exists but is not exposed through `AsyncPersistenceLayer`

---

## Root Cause Analysis

### Technical Analysis

**Problem:** The spell casting completion flow attempts to heal the player through `AsyncPersistenceLayer.async_heal_player()`, but this method was never implemented in the persistence layer facade.

**Architecture Context:**
- `AsyncPersistenceLayer` is a facade that delegates to focused repositories
- `HealthRepository` contains the actual `heal_player()` implementation
- `AsyncPersistenceLayer` has a `_health_repo` instance but doesn't expose `async_heal_player()`

**Why It Fails:**
1. Spell casting completes after 1 second (casting timer works correctly)
2. `_complete_casting()` is called to apply spell effects
3. For healing spells, `spell_effects._process_heal()` calls `player_service.heal_player()`
4. `player_service.heal_player()` calls `persistence.async_heal_player(player, amount)`
5. `AttributeError` is raised because `async_heal_player` doesn't exist
6. Exception is caught by `process_casting_progress()` error handler
7. Casting state is never cleared, so the error repeats on every tick

**Why It Doesn't Complete:**
- The exception prevents `_complete_casting()` from finishing
- `casting_state_manager.complete_casting()` is never called
- Player remains in casting state indefinitely
- Every tick attempts to process the same failed casting

---

## System Impact Assessment

### Affected Systems

1. **Spell Casting System** - CRITICAL
   - All healing spells are broken
   - Casting state management is corrupted
   - Players can get stuck in casting state

2. **Game Tick Processing** - HIGH
   - Error spam on every tick for stuck castings
   - Performance degradation from exception handling
   - Log file bloat from repeated errors

3. **Player Experience** - CRITICAL
   - Healing spells don't work
   - Players can't interrupt stuck castings (without `/stop` command)
   - Confusing error messages (if any shown to player)

### Scope

- **Affected Spells:** All healing spells (Minor Heal, Basic Heal, etc.)
- **Affected Players:** Any player attempting to cast a healing spell
- **System-Wide Impact:** Error spam affects server performance

---

## Code References

### Files Involved

1. **`server/async_persistence.py`**
   - Missing: `async_heal_player()` method
   - Has: `_health_repo` instance with `heal_player()` method

2. **`server/game/player_service.py:710`**
   - Calls: `await self.persistence.async_heal_player(player, amount)`
   - This method doesn't exist

3. **`server/persistence/repositories/health_repository.py:93`**
   - Has: `async def heal_player(self, player: Player, amount: int)`
   - This is the actual implementation that should be called

4. **`server/app/game_tick_processing.py:231-237`**
   - Error handler catches the exception but doesn't clear casting state

5. **`server/game/magic/magic_service.py:357-415`**
   - `_complete_casting()` method that fails when applying healing effects

---

## Investigation Findings

### Confirmed Issues

1. ✅ **Missing Method:** `AsyncPersistenceLayer.async_heal_player()` does not exist
2. ✅ **Error Pattern:** `AttributeError` occurs on every game tick for stuck castings
3. ✅ **Casting State:** Casting state is never cleared due to exception
4. ✅ **Implementation Exists:** `HealthRepository.heal_player()` exists and works correctly

### Related Issues

1. **Error Handling:** The exception handler in `process_casting_progress()` logs the error but doesn't clear the stuck casting state, causing infinite error loops
2. **Method Naming:** The codebase uses `async_heal_player` but the repository method is just `heal_player` (already async)

---

## Recommended Investigation Priorities

### Priority 1: Fix Missing Method (CRITICAL)
- Add `async_heal_player()` method to `AsyncPersistenceLayer`
- Delegate to `_health_repo.heal_player()`
- Ensure method signature matches expected usage

### Priority 2: Improve Error Handling (HIGH)
- Clear casting state when exceptions occur during completion
- Prevent infinite error loops
- Provide user feedback for failed spell casts

### Priority 3: Add Defensive Checks (MEDIUM)
- Verify all required persistence methods exist before use
- Add runtime validation for spell effect processing
- Improve error messages for debugging

---

## Remediation Prompt

**For Cursor Chat:**

```
Fix the missing async_heal_player method in AsyncPersistenceLayer that is preventing healing spells from completing.

The issue:
- player_service.heal_player() calls persistence.async_heal_player() but this method doesn't exist
- HealthRepository has heal_player() method that should be used
- Add async_heal_player() to AsyncPersistenceLayer that delegates to _health_repo.heal_player()

Files to modify:
- server/async_persistence.py - Add async_heal_player() method

Also improve error handling in process_casting_progress() to clear stuck casting states when exceptions occur.
```

---

## Investigation Status

**Status:** COMPLETE
**Root Cause:** IDENTIFIED
**Remediation:** PROMPT GENERATED

---

**Investigation Completed:** 2025-12-14
**Next Steps:** Implement fix for missing `async_heal_player()` method
