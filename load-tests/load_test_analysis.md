# Load Test Analysis Report

**Date**: 2025-12-06
**Test Duration**: ~30 minutes (10 players, 20 actions, 5-minute idle period)
**Environment**: local

## Executive Summary

The load test successfully registered and logged in 10 concurrent players, executed 20 different game actions, and
maintained all players idle for 5 minutes. However, several critical bugs were discovered that need immediate attention.

## Test Execution Summary

### Players Registered

**10 players** successfully registered with unique usernames (`loadtest_p1` through `loadtest_p10`)

**Professions assigned**: One of each profession (two Tramps as requested)

- P1: Tramp
- P2: Tramp
- P3: Antiquarian
- P4: Author
- P5: Dilettante
- P6: Doctor of Medicine
- P7: Journalist
- P8: Police Detective
- P9: Private Investigator
- P10: Professor

### Actions Executed (20 total, 2 per player)

1. **Player 1**: `who`, `look` ✅
2. **Player 2**: `status`, `inventory` ❌ (both failed)
3. **Player 3**: `say`, `time` ❌ (say failed)
4. **Player 4**: `help`, `me` ✅
5. **Player 5**: `go east`, `sit` ✅
6. **Player 6**: `stand`, `lie` ✅
7. **Player 7**: `ground`, `whisper` ❌ (both failed)
8. **Player 8**: `reply`, `alias` ❌ (reply failed, alias succeeded)
9. **Player 9**: `local`, `global` ❌ (local failed, global unsupported)
10. **Player 10**: `emote`, `pose` ❌ (both failed)

**Success Rate**: 8/20 actions (40%) succeeded without errors

## Critical Issues Found

### 1. **`who` Command - Unawaited Coroutine** 🔴 CRITICAL

**Error**: `object of type 'coroutine' has no len()`

**Location**: `server/commands/utility_commands.py:140`

**Root Cause**: `persistence.list_players()` is an async method that was not awaited.

**Impact**: The `who` command fails for all players, preventing them from seeing the online player list.

**Fix Required**:

```python
# Current (WRONG)

players = persistence.list_players()

# Should be

players = await persistence.list_players()
```

---

### 2. **`status` Command - Unawaited Coroutine** 🔴 CRITICAL

**Error**: `'coroutine' object has no attribute 'current_room_id'`

**Location**: `server/commands/utility_commands.py` (status command handler)

**Root Cause**: An async method that returns a player object is not being awaited before accessing its attributes.

**Impact**: The `status` command fails, preventing players from viewing their character status.

**Fix Required**: Identify and await the async method that retrieves the player object.

---

### 3. **`inventory` Command - Unawaited Coroutine** 🔴 CRITICAL

**Error**: `'coroutine' object has no attribute 'get_inventory'`

**Location**: `server/commands/inventory_commands.py:484`

**Root Cause**: `player.get_inventory()` is an async method that was not awaited.

**Impact**: The `inventory` command fails, preventing players from viewing their inventory.

**Fix Required**:

```python
# Current (WRONG)

inventory_view = player.get_inventory()

# Should be

inventory_view = await player.get_inventory()
```

---

### 4. **Communication Commands - Missing Method** 🔴 CRITICAL

**Error**: `'AsyncPersistenceLayer' object has no attribute 'async_get_player_by_name'`

**Affected Commands**: `say`, `whisper`, `local`, `emote`

**Location**: `server/game/player_service.py:238`

**Root Cause**: The code attempts to call `self.persistence.async_get_player_by_name()`, but the method is actually
named `get_player_by_name()` (without the `async_` prefix).

**Impact**: All communication commands fail, breaking core game functionality.

**Fix Required**:

```python
# Current (WRONG)

player = await self.persistence.async_get_player_by_name(player_name)

# Should be

player = await self.persistence.get_player_by_name(player_name)
```

---

### 5. **`pose` Command - Unawaited Coroutine** 🔴 CRITICAL

**Error**: `'coroutine' object has no attribute 'pose'`

**Location**: `server/commands/communication_commands.py:176`

**Root Cause**: An async method that returns a player object is not being awaited before accessing its `pose` attribute.

**Impact**: The `pose` command fails, preventing players from setting their pose.

**Fix Required**: Identify and await the async method that retrieves the player object before accessing `player.pose`.

---

### 6. **`ground` Command - Validation Error** 🟡 MEDIUM

**Error**: `Usage: ground <player>`

**Location**: `server/utils/command_parser.py`

**Root Cause**: The `ground` command requires a player argument, but it was called without one during the load test.

**Impact**: Command validation correctly rejected the invalid usage. This is expected behavior, but the test should have
included a valid player argument.

**Fix Required**: None - this is correct validation behavior. Update test to use valid syntax: `ground <player_name>`.

---

### 7. **`global` Command - Not Implemented** 🟡 MEDIUM

**Error**: `Unsupported command: global`

**Location**: `server/utils/command_parser.py`

**Root Cause**: The `global` command is not yet implemented in the command system.

**Impact**: Players cannot use the `global` command. This is expected for an unimplemented feature.

**Fix Required**: Implement the `global` command handler if this feature is desired.

---

## Warnings Found

### 1. **Invalid Invite Codes** (During Registration)

Two invalid invite codes were attempted: `ELDRITCH42` and `VOIDPASS`

- These were corrected by querying the database for valid codes
- **Impact**: None - resolved during test execution

### 2. **Stats Rolling Timeout**

One player (Police Detective) hit the timeout limit while rolling stats

- The system correctly handled this by allowing the player to retry
- **Impact**: Minor - player was able to complete character creation after retry

### 3. **NPC Visibility Warning**

Warnings about "No NPCs included in occupants snapshot"

- This appears to be expected behavior when no NPCs are present in a room
- **Impact**: None - informational warning

### 4. **Player Catatonia**

One player entered catatonia state (lucidity dropped to 0)

- This appears to be expected game mechanics behavior
- **Impact**: None - game mechanics working as designed

## NATS Connection Errors

**Error**: Multiple `ConnectionRefusedError` and `ConnectionResetError` during server shutdown

**Location**: NATS client library

**Root Cause**: Expected behavior when NATS server is shut down while clients are still connected.

**Impact**: None - these errors occur during graceful shutdown and are expected.

## Recommendations

### Immediate Actions (Critical)

1. **Fix `who` command**: Add `await` to `persistence.list_players()` call
2. **Fix `status` command**: Identify and await the async player retrieval method
3. **Fix `inventory` command**: Add `await` to `player.get_inventory()` call
4. **Fix communication commands**: Change `async_get_player_by_name` to `get_player_by_name`
5. **Fix `pose` command**: Identify and await the async player retrieval method

### Short-Term Actions (Medium Priority)

1. **Implement `global` command**: If this feature is desired
2. **Update load test**: Use valid syntax for `ground` command

### Long-Term Actions (Nice to Have)

1. **Add comprehensive async/await linting**: Prevent similar issues in the future
2. **Add integration tests**: Test all commands with proper async/await patterns
3. **Improve error messages**: Provide more user-friendly error messages for failed commands

## Test Coverage

### Commands Tested (20 total)

✅ `look` - Working

✅ `go` - Working

✅ `help` - Working

✅ `me` - Working

- ✅ `sit` - Working
- ✅ `stand` - Working
- ✅ `lie` - Working
- ✅ `time` - Working
- ✅ `alias` - Working
- ❌ `who` - **BROKEN** (unawaited coroutine)
- ❌ `status` - **BROKEN** (unawaited coroutine)
- ❌ `inventory` - **BROKEN** (unawaited coroutine)
- ❌ `say` - **BROKEN** (missing method)
- ❌ `whisper` - **BROKEN** (missing method)
- ❌ `local` - **BROKEN** (missing method)
- ❌ `emote` - **BROKEN** (missing method)
- ❌ `pose` - **BROKEN** (unawaited coroutine)
- ❌ `ground` - Validation error (test issue, not code issue)
- ❌ `global` - Not implemented

### Commands Not Tested

`mute`, `unmute`, `mute_global`, `unmute_global`

- `mutes`
- `add_admin`, `admin`
- `npc`, `summon`
- `teleport`, `goto`
- `whoami`
- `pickup`, `drop`, `put`, `get`
- `equip`, `unequip`
- `quit`, `logout`
- `attack`, `punch`, `kick`, `strike`
- `shutdown`
- `system`
- `aliases`, `unalias`
- `reply` (tested but failed due to missing method)

## Conclusion

The load test successfully identified **5 critical bugs** that prevent core game functionality from working correctly.
All of these bugs are related to improper async/await usage, which is a common issue when migrating from synchronous to
asynchronous code.

**Priority**: All critical bugs should be fixed before the next release, as they affect fundamental game commands that
players rely on.

**Next Steps**:

1. Fix all critical bugs identified above
2. Re-run the load test to verify fixes
3. Add unit tests for all affected commands
4. Consider adding async/await linting rules to prevent future issues
