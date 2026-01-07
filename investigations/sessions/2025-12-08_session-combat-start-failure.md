# BUG INVESTIGATION REPORT: Combat Start Failure - AttributeError

**Session ID**: `2025-12-08_session-combat-start-failure`
**Investigation Date**: December 8, 2025
**Investigator**: AI Debugging Agent
**Bug Severity**: High (Blocks core gameplay functionality)

---

## Executive Summary

Combat commands (`/attack`, `/punch`, etc.) are failing with an
`AttributeError: 'coroutine' object has no attribute 'current_room_id'`. The
root cause is a missing `await` keyword when calling the async method
`persistence.get_player_by_name()` in the `handle_attack_command` method. This
causes the `player` variable to be a coroutine object instead of a Player
object, leading to the error when attempting to access `player.current_room_id`.

**Root Cause**: Missing `await` keyword on line 160 of
`server/commands/combat.py` when calling `persistence.get_player_by_name()`.

**Impact**: Players cannot initiate combat with NPCs or other players. All
attack commands fail immediately with an internal error.

---

## Bug Description

**User Report**: "Unable to start combat"
**Error Messages**:

- `AttributeError: 'coroutine' object has no attribute 'current_room_id'`
- Error occurs in `server/commands/combat.py` at line 169

**Symptoms**:

- Attack commands (`/attack`, `/punch`, `/kick`, etc.) fail immediately
- Error messages appear in Game Info panel: "An error occurred during combat:
  'coroutine' object has no attribute 'current_room_id'"
- Combat cannot be initiated with NPCs or other players

**Expected Behavior**: Attack commands should successfully initiate combat
with valid targets.

**Actual Behavior**: Attack commands fail with AttributeError before combat can begin.

---

## Evidence Collection

### Error Log Evidence

**File**: `logs/local/errors.log`
**Timestamp**: 2025-12-08 16:34:58 and 16:35:02

```text
AttributeError: 'coroutine' object has no attribute 'current_room_id'
  File "E:\projects\GitHub\MythosMUD\server\commands\combat.py", line 169, in handle_attack_command
    room_id = player.current_room_id
              ^^^^^^^^^^^^^^^^^^^^^^
```

**Error Frequency**: Error occurs on every attack command attempt (confirmed
by two consecutive errors in logs).

### Code Analysis Evidence

**File**: `server/commands/combat.py`
**Line 160** (Problematic Code):

```python
player = persistence.get_player_by_name(get_username_from_user(current_user))
```

**File**: `server/commands/combat.py`
**Line 169** (Error Location):

```python
room_id = player.current_room_id  # Fails because player is a coroutine, not a Player object
```

### Comparison with Correct Implementation

**File**: `server/commands/exploration_commands.py`
**Line 424** (Correct Usage):

```python
player = await persistence.get_player_by_name(get_username_from_user(current_user))
```

**File**: `server/commands/exploration_commands.py`
**Line 1023** (Correct Usage):

```python
player = await persistence.get_player_by_name(get_username_from_user(current_user))
```

### Method Signature Evidence

**File**: `server/async_persistence.py`
**Line 397**:

```python
async def get_player_by_name(self, name: str) -> Player | None:
```

**File**: `server/persistence/repositories/player_repository.py`
**Line 82**:

```python
async def get_player_by_name(self, name: str) -> Player | None:
```

**Confirmation**: `get_player_by_name` is definitively an async method that
must be awaited.

### Additional Issues Found

**File**: `server/commands/combat.py`
**Line 299** (Same Issue):

```python
player = self.persistence.get_player_by_name(player_name)  # Missing await
```

This is in the `_execute_combat_action` method and will cause the same error
if that code path is executed.

---

## Root Cause Analysis

### Technical Analysis

1. **Async Method Not Awaited**:

   - `persistence.get_player_by_name()` is an async method (coroutine function)
   - Line 160 calls it without `await`, returning a coroutine object instead of
     a Player object
   - When code attempts to access `player.current_room_id` on line 169, Python
     raises `AttributeError` because coroutine objects don't have a
     `current_room_id` attribute

2. **Type Mismatch**:
   - Expected: `Player` object with `current_room_id` attribute
   - Actual: `coroutine` object (result of calling async function without await)

3. **Inconsistency with Other Commands**:

   - Other command handlers (`exploration_commands.py`) correctly use `await`
     when calling `get_player_by_name`
   - Combat command handler is inconsistent with established patterns

### Execution Flow Analysis

1. User executes attack command (e.g., `/attack dr`)
2. `handle_attack_command` is called (async method)
3. Line 160: `player = persistence.get_player_by_name(...)` - **MISSING AWAIT**
4. `player` is assigned a coroutine object, not a Player object
5. Line 169: `room_id = player.current_room_id` - **FAILS HERE**
6. AttributeError is raised and caught by error handler
7. Error message is displayed to user in Game Info panel

### Why This Wasn't Caught Earlier

- The code compiles/runs without syntax errors (missing await is a runtime
  issue)
- The error only occurs when the code path is executed (attack command used)
- Type checking may not have caught this if async/await patterns weren't fully
  enforced
- The method signature suggests async, but the call site doesn't reflect that

---

## System Impact Assessment

### Severity: High

**Affected Functionality**:

- All combat initiation commands (`/attack`, `/punch`, `/kick`, etc.)
- Player vs NPC combat
- Player vs Player combat
- Any combat-related gameplay

**User Impact**:

- Players cannot engage in combat
- Core gameplay mechanic is completely blocked
- Error messages are displayed but don't clearly indicate the issue to users

**System Impact**:

- Error handling works correctly (errors are caught and logged)
- No data corruption or persistence issues
- No server crashes or stability issues
- Performance impact is minimal (error occurs quickly)

**Scope**:

- Affects all players attempting to use combat commands
- Affects all combat scenarios (NPCs, players, all attack types)
- Does not affect other game systems (movement, chat, inventory, etc.)

---

## Affected Components

### Primary Component

- **File**: `server/commands/combat.py`
- **Method**: `CombatCommandHandler.handle_attack_command()`
- **Line**: 160 (missing await)
- **Line**: 169 (error location)

### Secondary Component

- **File**: `server/commands/combat.py`
- **Method**: `CombatCommandHandler._execute_combat_action()`
- **Line**: 299 (missing await - same issue, different code path)

### Related Components

- `server/async_persistence.py` - Provides the async `get_player_by_name`
  method
- `server/persistence/repositories/player_repository.py` - Implements the
  async method
- Error handling system - Correctly catches and logs the error

---

## Investigation Recommendations

### Immediate Priorities

1. **Fix Missing Await (Line 160)**: Add `await` keyword before
   `persistence.get_player_by_name()` call
2. **Fix Missing Await (Line 299)**: Add `await` keyword before
   `self.persistence.get_player_by_name()` call in `_execute_combat_action`
3. **Verify Room Retrieval**: Check if `persistence.get_room()` on line 178
   also needs `await` (may be sync method, needs verification)

### Code Quality Improvements

1. **Add Type Checking**: Consider adding mypy or similar to catch
   async/await mismatches
2. **Code Review Process**: Ensure async methods are always awaited
3. **Unit Tests**: Add tests that verify async methods are properly awaited
4. **Linting Rules**: Add linting rules to detect missing await on async
   calls

### Testing Recommendations

1. **Test Combat Initiation**: Verify attack commands work after fix
2. **Test All Attack Types**: Verify all combat command variants work
3. **Test Error Handling**: Ensure proper error messages if player/target not
   found
4. **Integration Tests**: Add integration tests for combat command flow

---

## Remediation Prompt

**For Cursor Chat**:

```text
Fix the combat start failure bug: Attack commands are failing with
AttributeError: 'coroutine' object has no attribute 'current_room_id'.

The root cause is missing `await` keywords when calling async persistence
methods in `server/commands/combat.py`:

1. Line 160: Change `player = persistence.get_player_by_name(...)` to
   `player = await persistence.get_player_by_name(...)`
2. Line 299: Change `player = self.persistence.get_player_by_name(...)` to
   `player = await self.persistence.get_player_by_name(...)`
3. Verify line 178 (`room = persistence.get_room(room_id)`) - check if
   `get_room` is async and add await if needed

After fixing, test that attack commands work correctly and combat can be
initiated with NPCs and players.

```text

---

## Conclusion

The combat start failure is caused by a missing `await` keyword when calling
the async method `persistence.get_player_by_name()`. This is a straightforward
fix that requires adding `await` in two locations in the combat command
handler. The error is consistently reproducible and blocks all combat
functionality. The fix should be simple and low-risk, requiring only the
addition of `await` keywords to properly handle the async method calls.

**Investigation Status**: Complete
**Root Cause**: Identified
**Remediation**: Clear and straightforward
**Risk Level**: Low (simple fix, minimal code changes)

---

## Investigation Checklist

- [x] Error logs analyzed
- [x] Code paths traced
- [x] Root cause identified
- [x] Evidence collected and documented
- [x] System impact assessed
- [x] Affected components identified
- [x] Comparison with working code completed
- [x] Investigation recommendations provided
- [x] Remediation prompt generated
- [x] Comprehensive report created
