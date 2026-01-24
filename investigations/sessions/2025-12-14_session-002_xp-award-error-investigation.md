# BUG INVESTIGATION REPORT: XP Award Error After Mob Defeat

**Investigation Date**: 2025-12-14
**Investigator**: AI Assistant (Cursor)
**Session ID**: 2025-12-14_session-002_xp-award-error-investigation
**Bug Type**: Server-Side Error - Method Not Found
**Severity**: High (Blocks XP rewards after combat)

---

## EXECUTIVE SUMMARY

A critical error occurs when attempting to award experience points (XP) to players after defeating NPCs/mobs. The error is caused by `PlayerCombatService` calling a non-existent method `async_get_player` on the `AsyncPersistenceLayer` object. The correct method name is `get_player_by_id`, which is used successfully by other services in the codebase.

**Root Cause**: Method name mismatch - `player_combat_service.py` calls `async_get_player()` but `AsyncPersistenceLayer` only provides `get_player_by_id()`.

**Impact**: Players do not receive XP rewards after defeating NPCs, affecting game progression and player experience.

---

## DETAILED FINDINGS

### 1. Error Log Analysis

**Error Location**: `logs/local/errors.log:1`

**Error Details**:

```
2025-12-14 14:56:15 - server.services.player_combat_service - ERROR -
player_id=UUID('9a2a5560-fb0e-471a-8652-aad7043d7dc6')
error="'AsyncPersistenceLayer' object has no attribute 'async_get_player'"
event='Error awarding XP to player'
correlation_id='64ca5f14-9f5d-496c-ac4e-f4d5ddb6e750'
timestamp='2025-12-14T21:56:15.307280Z'
logger_name='error'
request_id='218e07ff-b907-4ea0-8431-f43642156b66'
logger='server.services.player_combat_service'
level='error'
```

**Key Information**:
**Timestamp**: 2025-12-14 14:56:15 (21:56:15 UTC)

**Affected Player**: UUID('9a2a5560-fb0e-471a-8652-aad7043d7dc6')

**Error Type**: AttributeError
- **Missing Attribute**: `async_get_player`
- **Service**: `server.services.player_combat_service`
- **Event**: Error awarding XP to player

### 2. Code Analysis

#### 2.1 Faulty Code Location

**File**: `server/services/player_combat_service.py`
**Line**: 273
**Method**: `award_xp_on_npc_death()`

**Faulty Code**:

```python
async def award_xp_on_npc_death(
    self,
    player_id: UUID,
    npc_id: UUID,
    xp_amount: int,
) -> None:
    """
    Award XP to a player for defeating an NPC.
    ...
    """
    try:
        # Get player from persistence

        player = await self._persistence.async_get_player(player_id)  # LINE 273 - ERROR HERE
        if not player:
            logger.warning("Player not found for XP award", player_id=player_id)
            return
        # ... rest of method

```

#### 2.2 Correct Interface Definition

**File**: `server/async_persistence.py`
**Lines**: 401-403

**Available Method**:

```python
async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
    """Get a player by ID. Delegates to PlayerRepository."""
    return await self._player_repo.get_player_by_id(player_id)
```

**Confirmed**: `AsyncPersistenceLayer` does NOT have an `async_get_player` method. It provides:

- `get_player_by_id(player_id: uuid.UUID)` - ✅ Available
- `get_player_by_name(name: str)` - ✅ Available
- `get_player_by_user_id(user_id: str)` - ✅ Available
- `async_get_player(...)` - ❌ Does NOT exist

#### 2.3 Correct Usage Pattern in Other Services

**File**: `server/services/target_resolution_service.py`
**Lines**: 72-80

**Correct Implementation**:

```python
# Check if persistence layer has async method (AsyncPersistenceLayer uses get_player_by_id)

if hasattr(self.persistence, "get_player_by_id"):
    method = self.persistence.get_player_by_id
    if inspect.iscoroutinefunction(method):
        logger.debug("Using async get_player_by_id", player_id=player_id_uuid)
        player = await method(player_id_uuid)
    else:
        logger.debug("Using sync get_player_by_id", player_id=player_id_uuid)
        player = method(player_id_uuid)
```

**File**: `server/game/player_service.py`
**Lines**: 218

**Correct Implementation**:

```python
player = await self.persistence.get_player_by_id(player_id)
```

### 3. Execution Flow Analysis

**Trigger Path**:

1. NPC is defeated in combat
2. `PlayerCombatService.handle_npc_death()` is called
3. `PlayerCombatService.award_xp_on_npc_death()` is invoked
4. Method attempts to retrieve player: `await self._persistence.async_get_player(player_id)`
5. **ERROR**: `AttributeError` - `'AsyncPersistenceLayer' object has no attribute 'async_get_player'`
6. Exception is caught and logged, but XP is not awarded
7. Player does not receive XP reward

**Expected Flow**:

1. NPC is defeated in combat
2. `PlayerCombatService.handle_npc_death()` is called
3. `PlayerCombatService.award_xp_on_npc_death()` is invoked
4. Method retrieves player: `await self._persistence.get_player_by_id(player_id)` ✅
5. Player object is retrieved successfully
6. XP is added to player: `player.add_experience(xp_amount)`
7. Player is saved: `await self._persistence.save_player(player)`
8. XP award event is published
9. Player receives XP reward

### 4. System Impact Assessment

**Affected Systems**:
**Player Combat Service**: Directly affected - XP award functionality broken

**Player Progression**: Affected - Players cannot gain XP from combat

**Combat System**: Indirectly affected - Combat completes but rewards fail
- **Event System**: Affected - XP award events are not published

**Scope**:
**Severity**: High

**Frequency**: Every time a player defeats an NPC

**User Impact**: Players do not receive XP rewards, blocking progression
- **Data Integrity**: No data corruption, but XP awards are silently lost

**Affected Players**:

- All players who defeat NPCs in combat
- Specific instance documented: Player UUID `9a2a5560-fb0e-471a-8652-aad7043d7dc6`

### 5. Code Consistency Analysis

**Inconsistency Found**:

- `PlayerCombatService` uses incorrect method name: `async_get_player`
- Other services correctly use: `get_player_by_id`
- This suggests `PlayerCombatService` was not updated during a refactoring or was written with incorrect method name

**Services Using Correct Pattern**:
✅ `TargetResolutionService` - Uses `get_player_by_id` with proper checks

✅ `PlayerService` - Uses `get_player_by_id` directly

❌ `PlayerCombatService` - Uses non-existent `async_get_player`

### 6. Test Coverage Analysis

**Test File**: `server/tests/integration/services/test_player_combat_integration.py`

**Test Method**: `test_award_xp_on_npc_death` (Line 186)

**Test Implementation**:

```python
@pytest.mark.asyncio
async def test_award_xp_on_npc_death(self, player_combat_service, sample_player):
    # ...
    # Mock persistence to return None (player not found)

    player_combat_service._persistence.async_get_player = AsyncMock(return_value=None)
```

**Issue**: The test mocks `async_get_player`, which suggests the test was written to match the incorrect implementation rather than validating against the actual `AsyncPersistenceLayer` interface.

**Impact**: Tests may pass with mocks but fail in production when using the real `AsyncPersistenceLayer`.

---

## ROOT CAUSE ANALYSIS

### Primary Root Cause

**Method Name Mismatch**: `PlayerCombatService.award_xp_on_npc_death()` calls `self._persistence.async_get_player(player_id)`, but `AsyncPersistenceLayer` does not provide this method. The correct method is `get_player_by_id(player_id)`.

### Contributing Factors

1. **Inconsistent API Usage**: The service was not updated to match the `AsyncPersistenceLayer` interface
2. **Missing Interface Validation**: No compile-time or runtime validation ensures methods exist before calling
3. **Test Mocking**: Tests mock the incorrect method name, masking the issue
4. **Code Review Gap**: The incorrect method name was not caught during code review

### Technical Details

**Error Type**: `AttributeError`
**Python Exception**: `'AsyncPersistenceLayer' object has no attribute 'async_get_player'`
**Location**: `server/services/player_combat_service.py:273`
**Method**: `PlayerCombatService.award_xp_on_npc_death()`
**Called From**: `PlayerCombatService.handle_npc_death()`

**Correct Method Signature**:

```python
async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
```

**Incorrect Call**:

```python
player = await self._persistence.async_get_player(player_id)  # ❌ Method doesn't exist
```

**Correct Call**:

```python
player = await self._persistence.get_player_by_id(player_id)  # ✅ Correct method
```

---

## EVIDENCE DOCUMENTATION

### Error Log Evidence

**File**: `logs/local/errors.log`
**Line**: 1
**Timestamp**: 2025-12-14 14:56:15 (21:56:15 UTC)
**Full Error Entry**:

```
2025-12-14 14:56:15 - server.services.player_combat_service - ERROR -
player_id=UUID('9a2a5560-fb0e-471a-8652-aad7043d7dc6')
error="'AsyncPersistenceLayer' object has no attribute 'async_get_player'"
event='Error awarding XP to player'
correlation_id='64ca5f14-9f5d-496c-ac4e-f4d5ddb6e750'
timestamp='2025-12-14T21:56:15.307280Z'
logger_name='error'
request_id='218e07ff-b907-4ea0-8431-f43642156b66'
logger='server.services.player_combat_service'
level='error'
```

### Code Evidence

**Faulty Code**:
**File**: `server/services/player_combat_service.py`

**Line**: 273

**Code**: `player = await self._persistence.async_get_player(player_id)`

**Interface Definition**:
**File**: `server/async_persistence.py`

**Lines**: 401-403

**Available Method**: `async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:`

**Correct Usage Examples**:
**File**: `server/services/target_resolution_service.py` (Lines 72-80)

**File**: `server/game/player_service.py` (Line 218)

### System State Evidence

**Persistence Layer Type**: `AsyncPersistenceLayer`
**Service Type**: `PlayerCombatService`
**Error Context**: XP award after NPC defeat
**Player ID**: `UUID('9a2a5560-fb0e-471a-8652-aad7043d7dc6')`

---

## INVESTIGATION RECOMMENDATIONS

### Priority 1: Immediate Fix Required

1. **Fix Method Call**: Change `async_get_player` to `get_player_by_id` in `player_combat_service.py:273`
2. **Update Tests**: Fix test mocks to use correct method name `get_player_by_id`
3. **Verify Integration**: Test XP award functionality after fix

### Priority 2: Code Quality Improvements

1. **Interface Validation**: Add runtime checks or type hints to validate persistence layer methods
2. **Code Review**: Review all services for consistent use of `AsyncPersistenceLayer` methods
3. **Documentation**: Document the correct `AsyncPersistenceLayer` API methods

### Priority 3: Prevention Measures

1. **Static Analysis**: Add linting rules to catch method name mismatches
2. **Integration Tests**: Add integration tests that use real `AsyncPersistenceLayer` instances
3. **API Documentation**: Generate API documentation from `AsyncPersistenceLayer` interface

### Priority 4: Additional Investigation

1. **Search Codebase**: Check for other instances of `async_get_player` usage
2. **Review History**: Check git history to understand when/why incorrect method was used
3. **Pattern Analysis**: Identify if this is part of a larger pattern of API inconsistencies

---

## REMEDIATION PROMPT

**For Cursor Chat**:

```
Fix the XP award error in PlayerCombatService. The service is calling
`self._persistence.async_get_player(player_id)` but AsyncPersistenceLayer
does not have this method. The correct method is `get_player_by_id(player_id)`.

Change line 273 in server/services/player_combat_service.py from:
    player = await self._persistence.async_get_player(player_id)

To:
    player = await self._persistence.get_player_by_id(player_id)

Also update the test file server/tests/integration/services/test_player_combat_integration.py
to mock the correct method name `get_player_by_id` instead of `async_get_player`.

After the fix, verify:
1. XP awards work correctly after NPC defeat
2. Tests pass with the corrected method name
3. No other services use the incorrect method name
```

---

## INVESTIGATION COMPLETION CHECKLIST

[x] All investigation steps completed as written

- [x] Comprehensive evidence collected and documented
- [x] Root cause analysis completed
- [x] System impact assessed
- [x] Investigation report generated
- [x] No attempt made to fix issues (investigation only)
- [x] All findings clearly documented with evidence
- [x] Session logged in investigation history
- [x] Remediation prompt generated

---

## ADDITIONAL NOTES

### Related Files

`server/services/player_combat_service.py` - Faulty implementation

- `server/async_persistence.py` - Correct interface definition
- `server/services/target_resolution_service.py` - Correct usage example
- `server/game/player_service.py` - Correct usage example
- `server/tests/integration/services/test_player_combat_integration.py` - Test file with incorrect mocks

### Similar Issues to Check

Search codebase for other instances of `async_get_player`

- Review all services using `AsyncPersistenceLayer` for method name consistency
- Check for similar method name mismatches in other persistence layer calls

---

**Investigation Status**: ✅ COMPLETE
**Root Cause**: ✅ IDENTIFIED
**Remediation**: ✅ PROMPT GENERATED
