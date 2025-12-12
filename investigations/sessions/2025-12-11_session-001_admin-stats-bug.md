# Investigation Report: Admin Stats Display Bug

**Session ID**: `2025-12-11_session-001_admin-stats-bug`
**Date**: 2025-12-11
**Investigator**: AI Debug Agent
**Bug Report**: Unable to retrieve admin display information for a mob when "/look <mob>" is used

---

## Executive Summary

The bug occurs when an admin user attempts to view NPC stats using the `/look <mob>` command. The error `'bool' object is not callable` is raised in `npc_instance_service.py` at line 330, preventing admin stats from being displayed. The root cause is a type mismatch: the code attempts to call `is_alive` as a function, but it is actually a boolean property on NPC instances.

**Root Cause**: Type mismatch in `get_npc_stats()` method - attempting to call `is_alive` as a function when it's a boolean property.

**Severity**: Medium - Admin functionality is broken, but does not affect regular gameplay.

**Status**: Root cause identified, remediation prompt generated.

---

## Detailed Findings

### Phase 1: Initial Bug Report Analysis

**Bug Description**:
- **Command**: `/look <mob>` (e.g., `/look dr` for "Dr. Francis Morgan")
- **User Type**: Admin user
- **Expected Behavior**: Admin stats section should display NPC information
- **Actual Behavior**: Error message "Error retrieving stats" appears, admin stats section is missing

**Affected Systems**:
1. `server/commands/look_npc.py` - Command handler for looking at NPCs
2. `server/services/npc_instance_service.py` - Service responsible for retrieving NPC stats
3. Admin display functionality in the look command

### Phase 2: System State Investigation

**Error Log Analysis** (`logs/local/errors.log:1`):
```
2025-12-11 19:33:59 - server.services.npc_instance_service - ERROR -
error="'bool' object is not callable"
event='Error retrieving NPC stats'
correlation_id='f7131c2a-1939-473d-a87e-33ae506c2f3e'
```

**Warning Log Analysis** (`logs/local/warnings.log:1`):
```
2025-12-11 19:33:59 - server.commands.look_npc - WARNING -
npc_id='dr._francis_morgan_earth_arkhamcity_sanitarium_room_foyer_001_1765506810_7182'
error="'bool' object is not callable"
event='Error formatting NPC stats for admin'
```

**Key Observations**:
- Error occurs in `npc_instance_service.get_npc_stats()` method
- Error is caught and logged in `look_npc._format_npc_stats_for_admin()`
- Error message indicates a boolean value is being called as a function
- NPC ID is valid and accessible

### Phase 3: Code Analysis

**Location**: `server/services/npc_instance_service.py:330`

**Problematic Code**:
```python
"is_alive": getattr(npc_instance, "is_alive", lambda: True)(),
```

**Issue**: The code assumes `is_alive` is a callable method and attempts to invoke it with `()`. However, based on codebase analysis:

1. **NPC Base Implementation** (`server/npc/npc_base.py:47`):
   ```python
   self.is_alive = True  # Boolean property, not a method
   ```

2. **Usage Patterns Throughout Codebase**:
   - `npc_instance.is_alive = True` (direct assignment)
   - `getattr(npc_instance, "is_alive", True)` (property access, not callable)
   - Tests use `npc_instance.is_alive = True/False` (boolean assignment)

3. **Contrast with Player Model** (`server/models/player.py:226`):
   ```python
   def is_alive(self) -> bool:  # Method for players
   ```
   Players have `is_alive()` as a method, but NPCs have `is_alive` as a property.

**Additional Occurrence**: The same pattern exists at line 278 in the same file:
```python
"is_alive": getattr(npc_instance, "is_alive", lambda: True)(),
```

**Execution Flow**:
1. User executes `/look dr` command
2. `look_npc._format_single_npc_result()` is called
3. For admin users, `_format_npc_stats_for_admin()` is invoked
4. `npc_instance_service.get_npc_stats()` is called
5. Line 330 attempts: `getattr(npc_instance, "is_alive", lambda: True)()`
6. If `is_alive` exists and is `True` or `False` (boolean), Python tries to call it
7. Error: `'bool' object is not callable`
8. Exception is caught in `_format_npc_stats_for_admin()` and returns error message

### Phase 4: Evidence Collection

**Code Evidence**:
- **File**: `server/services/npc_instance_service.py`
- **Line 330**: `"is_alive": getattr(npc_instance, "is_alive", lambda: True)(),`
- **Line 278**: `"is_alive": getattr(npc_instance, "is_alive", lambda: True)(),` (same issue)

**Type Definition Evidence**:
- **File**: `server/npc/npc_base.py:47`
- **Definition**: `self.is_alive = True` (boolean property)

**Usage Pattern Evidence** (from grep results):
- 126 occurrences of `is_alive` in codebase
- NPC instances use: `npc_instance.is_alive = True/False` (property)
- Player models use: `player.is_alive()` (method)
- Other code uses: `getattr(npc_instance, "is_alive", True)` (property access, no call)

**Test Evidence**:
- `server/tests/unit/services/test_npc_instance_service.py:340`: `mock_npc.is_alive = lambda: True` (test mocks it as callable, but real implementation is boolean)

**Log Evidence**:
- Error timestamp: `2025-12-11 19:33:59`
- Correlation ID: `f7131c2a-1939-473d-a87e-33ae506c2f3e`
- Request ID: `b646d80f-5203-426c-be51-b4af3b4e842e`
- NPC ID: `dr._francis_morgan_earth_arkhamcity_sanitarium_room_foyer_001_1765506810_7182`

### Phase 5: Root Cause Analysis

**Primary Root Cause**:
The code in `npc_instance_service.py` incorrectly assumes `is_alive` is a callable method (like in the Player model), but NPC instances store `is_alive` as a boolean property. When `getattr()` retrieves the boolean value (`True` or `False`), the code attempts to call it with `()`, resulting in the error.

**Why This Happened**:
1. **Inconsistent API Design**: Players use `is_alive()` as a method, NPCs use `is_alive` as a property
2. **Copy-Paste Error**: The code pattern may have been copied from player-related code where `is_alive()` is callable
3. **Test Mocks**: Tests mock `is_alive` as `lambda: True`, which may have misled developers about the actual implementation

**Impact Assessment**:
- **Scope**: Affects all admin users attempting to view NPC stats via `/look` command
- **Severity**: Medium - Admin functionality broken, but regular gameplay unaffected
- **Frequency**: 100% reproduction rate when admin uses `/look <npc>` command
- **User Impact**: Admins cannot view detailed NPC statistics through the look command

**Affected Components**:
1. `server/services/npc_instance_service.py` - `get_npc_stats()` method (lines 278, 330)
2. `server/commands/look_npc.py` - Admin stats display functionality
3. Any code path that calls `get_npc_stats()` for admin display

---

## System Impact Assessment

**Functional Impact**:
- ✅ Regular player look functionality: **Unaffected**
- ❌ Admin stats display: **Broken**
- ✅ NPC lifecycle and combat: **Unaffected** (uses property directly)
- ✅ Other admin commands: **Unaffected**

**Performance Impact**: None - error occurs immediately, no resource leaks

**Security Impact**: None - error is caught and handled gracefully

**Data Integrity**: None - no data corruption, error is in display logic only

---

## Investigation Recommendations

### Immediate Actions Required:
1. **Fix Type Mismatch**: Update `npc_instance_service.py` to treat `is_alive` as a property, not a callable
2. **Fix Both Occurrences**: Update both line 278 and line 330
3. **Update Tests**: Review and update tests that mock `is_alive` as callable

### Code Quality Improvements:
1. **Standardize API**: Consider standardizing `is_alive` usage across Player and NPC models
2. **Type Hints**: Add type hints to clarify expected types
3. **Documentation**: Document that NPC `is_alive` is a property, not a method

### Testing Recommendations:
1. Add integration test for admin look command with NPC stats
2. Verify fix works with both alive and dead NPCs
3. Test with various NPC types to ensure compatibility

---

## Remediation Prompt

**For Cursor Chat**:

```
Fix the admin stats display bug in npc_instance_service.py. The issue is on lines 278 and 330 where the code attempts to call is_alive as a function, but it's actually a boolean property on NPC instances.

The problematic code:
```python
"is_alive": getattr(npc_instance, "is_alive", lambda: True)(),
```

Should be changed to:
```python
"is_alive": getattr(npc_instance, "is_alive", True),
```

This fix should be applied to both occurrences:
1. Line 278 in the `get_all_npc_instances()` method
2. Line 330 in the `get_npc_stats()` method

After fixing, verify:
1. Admin can use `/look <npc>` command successfully
2. Admin stats section displays correctly
3. Both alive and dead NPCs display correctly
4. All tests pass
```

---

## Conclusion

The root cause has been definitively identified as a type mismatch where boolean properties are being called as functions. The fix is straightforward and low-risk. The issue affects only admin functionality and does not impact regular gameplay or system stability.

**Investigation Status**: ✅ **COMPLETE**
**Root Cause**: ✅ **IDENTIFIED**
**Remediation**: ✅ **PROMPT GENERATED**

---

## Appendix: Related Files

- `server/services/npc_instance_service.py` - Primary bug location
- `server/commands/look_npc.py` - Error handling location
- `server/npc/npc_base.py` - NPC base class with `is_alive` property definition
- `server/models/player.py` - Player model with `is_alive()` method (for comparison)
- `logs/local/errors.log` - Error log entry
- `logs/local/warnings.log` - Warning log entry
