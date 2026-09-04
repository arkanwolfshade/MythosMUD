# Investigation Report: Heal Spell Never Finishes Casting

**Session ID**: `2025-12-14_session-004_heal-spell-casting-failure`
**Date**: 2025-12-14
**Investigator**: AI Debugging Agent
**Status**: Root Cause Identified

## Executive Summary

The heal spell (Minor Heal) is not completing its casting cycle despite having a 1-second cast time. The spell begins casting successfully ("You begin casting Minor Heal... (1 seconds)") but never completes, leaving the player in a perpetual casting state. Investigation revealed a **SQLAlchemy session management error** in the `record_spell_cast` method that prevents spell completion.

## Bug Description

**User Report**: "Heal spell is still never finishing casting"

**Observed Behavior**:

- Player casts "Minor Heal" spell
- Casting begins: "You begin casting Minor Heal... (1 seconds)"
- Casting never completes - no completion message, no health update
- Player remains in casting state indefinitely
- Player health remains unchanged (7/27, WOUNDED status)
- Player has sufficient MP (15/15)

**Expected Behavior**:

- Spell should complete after 1 second
- Health should be restored
- Casting state should be cleared
- Completion message should appear in game log

## Root Cause Analysis

### Primary Issue: SQLAlchemy Session Management Error

**Error Location**: `server/persistence/repositories/player_spell_repository.py:202-242` (`record_spell_cast` method)

**Error Message** (from `logs/local/errors.log`):

```
Database error recording spell cast: Instance '<PlayerSpell at 0x27b6afa97c0>' is not persistent within this Session
```

**Technical Analysis**:

1. **Session Boundary Violation**: The `record_spell_cast` method calls `get_player_spell(player_id, spell_id)` which creates its own database session context (line 223).

2. **Cross-Session Object Usage**: The `get_player_spell` method returns a `PlayerSpell` object that is attached to its own session. When `record_spell_cast` then tries to modify this object in a different session (line 228-230), SQLAlchemy throws the error because the object is not attached to the current session.

3. **Error Propagation**: The error is caught by the exception handler in `_complete_casting` (line 416-424 in `magic_service.py`), which logs the error and clears the casting state in the `finally` block. However, the spell effect has already been processed (line 401), so the healing may have occurred, but the casting state is cleared without proper completion.

4. **Code Flow**:

   ```
   _complete_casting()
   → process_effect() [SUCCESS - healing occurs]
   → record_spell_cast() [FAILS - session error]
   → Exception caught
   → Casting state cleared in finally block
   → No completion message sent to player
   ```

### Code Evidence

**File**: `server/persistence/repositories/player_spell_repository.py`

**Problematic Code** (lines 202-242):

```python
async def record_spell_cast(self, player_id: uuid.UUID, spell_id: str) -> PlayerSpell | None:
    try:
        async for session in get_async_session():
            player_spell = await self.get_player_spell(player_id, spell_id)  # ❌ Creates different session
            if not player_spell:
                return None

            # ❌ Trying to modify object from different session

            player_spell.times_cast += 1
            player_spell.last_cast_at = datetime.now(UTC).replace(tzinfo=None)
            await session.commit()  # ❌ Object not in this session
            ...
```

**Root Cause**: `get_player_spell` uses its own session context (`async for session in get_async_session()`), so the returned `PlayerSpell` object is attached to that session. When `record_spell_cast` creates a new session and tries to modify the object, SQLAlchemy correctly rejects it because the object belongs to a different session.

## System Impact Assessment

### Severity: HIGH

**Affected Systems**:

- Spell casting completion mechanism
- Player spell mastery tracking
- Spell cast history recording

**User Impact**:

- Players cannot complete spell casts
- Healing spells do not restore health (or restore health but don't complete)
- Players may be stuck in casting state
- Spell mastery progression is not recorded

**Data Integrity**:

- Spell effects may be applied (healing occurs) but not recorded
- Spell cast statistics are not updated
- Mastery progression tracking is broken

### Affected Components

1. **`server/persistence/repositories/player_spell_repository.py`**

   - `record_spell_cast()` method - session management issue

2. **`server/game/magic/magic_service.py`**

   - `_complete_casting()` method - error handling catches but doesn't prevent state clearing

3. **`server/app/game_tick_processing.py`**

   - `process_casting_progress()` - calls casting completion logic

## Evidence Collection

### Error Logs

**Timestamp**: `2025-12-14 17:55:17`
**Location**: `logs/local/errors.log:1-2`

```
2025-12-14 17:55:17 - server.utils.error_logging - ERROR - error_type='DatabaseError'
error_message="Database error recording spell cast: Instance '<PlayerSpell at 0x27b6afa97c0>' is not persistent within this Session"
details={'player_id': '9a2a5560-fb0e-471a-8652-aad7043d7dc6', 'spell_id': 'clerical_minor_heal',
'error': "Instance '<PlayerSpell at 0x27b6afa97c0>' is not persistent within this Session"}
user_friendly='Failed to record spell cast'
```

### Code References

1. **Error Source**: `server/persistence/repositories/player_spell_repository.py:202-242`
2. **Error Handler**: `server/game/magic/magic_service.py:416-428`
3. **Casting Progress**: `server/app/game_tick_processing.py:231-237`

### User Observation

From game client screenshot:

- Casting message: "You begin casting Minor Heal... (1 seconds)"
- No completion message
- Health unchanged: 7/27 (WOUNDED)
- MP available: 15/15

## Investigation Findings

### Confirmed Issues

1. ✅ **SQLAlchemy Session Error**: Confirmed - `PlayerSpell` object from one session being modified in another session
2. ✅ **Error Handling**: Confirmed - Error is caught but casting state is cleared anyway
3. ✅ **Spell Effect Processing**: Unclear - May succeed before error occurs

### Rejected Hypotheses

1. ❌ **Missing async_heal_player method**: Previously fixed, methods exist
2. ❌ **Insufficient MP**: Player has 15/15 MP, sufficient for spell
3. ❌ **Casting timer issue**: Timer appears to work (1 second cast time)

### Inconclusive Findings

1. ⚠️ **Spell Effect Application**: Cannot determine if healing actually occurs before error
2. ⚠️ **Error Recovery**: Error handling clears state but may not notify player

## Recommended Investigation Priorities

1. **HIGH**: Fix session management in `record_spell_cast` method
2. **MEDIUM**: Verify spell effects are applied before error occurs
3. **MEDIUM**: Improve error handling to notify player of failures
4. **LOW**: Add logging to track spell completion flow

## Remediation Prompt

**For Cursor Chat**:

```
Fix the SQLAlchemy session management error in the spell casting completion flow.

The issue is in `server/persistence/repositories/player_spell_repository.py` in the `record_spell_cast` method. The method calls `get_player_spell()` which creates its own database session, then tries to modify the returned `PlayerSpell` object in a different session, causing SQLAlchemy to throw "Instance is not persistent within this Session" error.

Fix by loading the `PlayerSpell` object within the same session context that will modify it, rather than calling `get_player_spell()` which uses its own session. Use a direct query within the `record_spell_cast` session context instead.

After fixing, verify that:
1. Spell casting completes successfully
2. Spell cast statistics are recorded
3. No session errors occur in logs
4. Player receives completion messages
```

## Technical Details

### Session Management Pattern

**Current (Broken) Pattern**:

```python
async def record_spell_cast(self, player_id, spell_id):
    async for session in get_async_session():
        player_spell = await self.get_player_spell(...)  # Different session
        player_spell.times_cast += 1  # Error: object not in this session
```

**Recommended Pattern**:

```python
async def record_spell_cast(self, player_id, spell_id):
    async for session in get_async_session():
        stmt = select(PlayerSpell).where(...)  # Load in same session
        result = await session.execute(stmt)
        player_spell = result.scalar_one_or_none()
        if player_spell:
            player_spell.times_cast += 1  # OK: object in this session
            await session.commit()
```

### Related Code Patterns

Similar session management issues may exist in:

- `update_mastery()` method (line 155-200) - also calls `get_player_spell()`
- Other repository methods that call each other across session boundaries

## Conclusion

The root cause is a **SQLAlchemy session management error** where a `PlayerSpell` object loaded in one session is modified in a different session. This prevents spell casting from completing properly, even though spell effects may be applied. The fix requires loading the `PlayerSpell` object within the same session context that modifies it.

**Status**: Root cause identified, remediation prompt generated.
