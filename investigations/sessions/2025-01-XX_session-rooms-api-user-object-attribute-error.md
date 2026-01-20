# Bug Investigation Report: Rooms API AttributeError

**Investigation Date**: 2025-11-27
**Investigator**: AI Assistant (GPT-4)
**Session ID**: 2025-01-XX_session-rooms-api-user-object-attribute-error
**Bug Type**: Server-Side API Error
**Severity**: Medium (Non-blocking but causes incorrect behavior)

---

## Executive Summary

An `AttributeError` occurs in the `/api/rooms/list` endpoint when attempting to filter rooms by exploration status. The error `'User' object has no attribute 'get'` indicates that the code is incorrectly treating a `User` SQLAlchemy model object as a dictionary. The error is caught and handled gracefully (returns all rooms instead of failing), but the exploration filtering feature does not work as intended.

**Root Cause**: Type mismatch - `current_user` is a `User` object (SQLAlchemy model) but the code attempts to use dictionary-style `.get()` method access.

**Impact**: Exploration-based room filtering is non-functional when `filter_explored=true` is used. The API falls back to returning all rooms, which may expose unexplored room data to clients.

---

## Detailed Findings

### 1. Error Log Analysis

**Source**: `logs/local/warnings.log` (line 1)

```
2025-11-27 19:57:38 - server.api.rooms - WARNING -
error="'User' object has no attribute 'get'"
error_type='AttributeError'
event='Error filtering by explored rooms, returning all rooms'
correlation_id='7a2fff5b-f308-45e2-89bc-94fa834f8f4a'
timestamp='2025-11-28T02:57:38.415250Z'
request_id='24202108-ebe6-41ad-96a7-9d0069351801'
path='/api/rooms/list'
method='GET'
```

**Key Observations**:

- Error occurs in `server.api.rooms` module
- Error type: `AttributeError`
- Error message: `'User' object has no attribute 'get'`
- Event: "Error filtering by explored rooms, returning all rooms"
- Request path: `/api/rooms/list`
- Error is caught and handled (warning level, not error)
- API continues execution and returns all rooms as fallback

### 2. Code Analysis

**File**: `server/api/rooms.py`

**Problematic Code** (lines 45, 81):

```python
@room_router.get("/list")
async def list_rooms(
    ...
    current_user: dict | None = Depends(get_current_user),  # Line 45 - INCORRECT TYPE ANNOTATION
    ...
) -> dict[str, Any]:
    ...
    if filter_explored and current_user:
        try:
            persistence = get_persistence()
            user_id = str(current_user.get("id", ""))  # Line 81 - ATTRIBUTE ERROR HERE
            ...
```

**Root Cause Analysis**:

1. **Type Annotation Mismatch**: Line 45 declares `current_user: dict | None`, but `get_current_user` from `fastapi-users` returns a `User` SQLAlchemy model object, not a dictionary.

2. **Incorrect Attribute Access**: Line 81 attempts to use `current_user.get("id", "")`, which is dictionary-style access. `User` objects have an `id` attribute (not a method), so this should be `current_user.id`.

3. **Evidence from User Model**:

   - `server/models/user.py` shows `User` extends `SQLAlchemyBaseUserTableUUID`
   - The `id` field is provided by the base class as a UUID attribute
   - User objects have attributes like `id`, `username`, `is_active`, etc., not dictionary keys

4. **Correct Usage Pattern**: Other files in the codebase correctly access `current_user.id`:

   - `server/api/players.py`: Uses `current_user.id` (attribute access)
   - `server/api/game.py`: Uses `current_user.id` and `current_user.username` (attribute access)
   - `server/auth/endpoints.py`: Uses `current_user.id` (attribute access)

### 3. Similar Issues Found

**Additional Files with Similar Problems**:

1. **`server/api/metrics.py`** (lines 39, 42):

   ```python
   is_admin = current_user.get("is_admin", False) or current_user.get("is_superuser", False)
   username=current_user.get("username")
   ```

   - Same issue: treating `User` object as dictionary
   - Should use: `current_user.is_admin`, `current_user.is_superuser`, `current_user.username`

2. **`server/api/admin/npc.py`** (multiple lines):

   ```python
   user=current_user.get("username")
   ```

   - Same issue: treating `User` object as dictionary
   - Should use: `current_user.username`

**Note**: These files may not have triggered errors yet if they haven't been called, or if the errors are being caught elsewhere.

### 4. Correct Implementation Pattern

**Reference Implementation**: `server/services/admin_auth_service.py` (lines 128-158)

This file demonstrates the correct pattern for safely accessing user attributes:

```python
def get_username(self, current_user: Any) -> str:
    """Safely get username from current user object."""
    if not current_user:
        return "unknown"

    # Try to get username from User object

    if hasattr(current_user, "username"):
        result = current_user.username
        assert isinstance(result, str)
        return result

    # Try to get username from dictionary

    if hasattr(current_user, "get"):
        result = current_user.get("username", "unknown")
        assert isinstance(result, str)
        return result

    return "unknown"
```

However, since `get_current_user` always returns a `User` object (or `None`), the simpler approach is direct attribute access.

### 5. System Impact Assessment

**Scope**:
**Primary Impact**: `/api/rooms/list` endpoint with `filter_explored=true` parameter

**Secondary Impact**: Potential issues in `metrics.py` and `admin/npc.py` if those endpoints are used

**Severity**:
**Medium**: Feature non-functional but graceful fallback exists

**Security Consideration**: Exploration filtering is a privacy/security feature - when it fails, all rooms are returned, potentially exposing unexplored room data

**User Experience**:

- API request succeeds (does not return 500 error)
- Warning logged but user may not be aware
- Exploration filtering silently fails
- All rooms returned instead of filtered list

**Data Integrity**:

- No data corruption
- No database issues
- Only affects API response filtering

### 6. Error Handling Analysis

**Current Error Handling** (lines 112-118):

```python
except Exception as e:
    # Log error but don't fail the request - just return all rooms

    logger.warning(
        "Error filtering by explored rooms, returning all rooms",
        error=str(e),
        error_type=type(e).__name__,
    )
```

**Assessment**:
✅ Error is caught and logged

✅ Request does not fail (graceful degradation)

- ⚠️ Feature silently fails (user may not know filtering didn't work)
- ⚠️ Security/privacy concern: unexplored rooms may be exposed

---

## Root Cause Analysis

### Technical Root Cause

The root cause is a **type annotation mismatch** combined with **incorrect attribute access pattern**:

1. **Type Annotation Error**: `current_user: dict | None` is incorrect. The actual type returned by `get_current_user` is `User | None` (SQLAlchemy model).

2. **Attribute Access Error**: Code attempts dictionary-style access (`current_user.get("id")`) on an object that uses attribute access (`current_user.id`).

3. **Inconsistent Patterns**: The codebase has mixed patterns - some files correctly use attribute access, others incorrectly use dictionary access.

### Why This Happened

1. **Type Annotation Confusion**: The type annotation `dict | None` suggests the developer expected a dictionary, but FastAPI Users returns a SQLAlchemy model object.

2. **Copy-Paste Pattern**: The dictionary-style `.get()` pattern may have been copied from code that actually works with dictionaries, or from an older version of the codebase.

3. **Missing Type Checking**: The type annotation didn't match the actual return type, and this wasn't caught by static type checking or runtime validation.

### Evidence Chain

1. **FastAPI Users Documentation**: `fastapi_users.current_user(optional=True)` returns a `User` model instance, not a dictionary.

2. **Codebase Evidence**:

   - `server/auth/users.py` line 155: `get_current_user = fastapi_users.current_user(optional=True)`
   - `server/models/user.py`: `User` class extends `SQLAlchemyBaseUserTableUUID` with `id` as an attribute
   - Other API files correctly use `current_user.id` (attribute access)

3. **Error Message**: `'User' object has no attribute 'get'` confirms `current_user` is a `User` object, not a dictionary.

---

## System Impact Assessment

### Affected Components

1. **Primary**: `server/api/rooms.py` - `/api/rooms/list` endpoint

   - Impact: Exploration filtering non-functional
   - Frequency: Every request with `filter_explored=true`

2. **Secondary**: `server/api/metrics.py` - Metrics endpoints

   - Impact: Admin checks may fail (if not already failing)
   - Frequency: Unknown (depends on usage)

3. **Tertiary**: `server/api/admin/npc.py` - NPC admin endpoints

   - Impact: Username logging may fail
   - Frequency: Unknown (depends on usage)

### Security Implications

**Privacy Concern**: When exploration filtering fails, the API returns all rooms instead of only explored rooms. This could expose:

- Room names and descriptions for unexplored areas
- Room coordinates and map data
- Exit information for unexplored rooms

**Mitigation**: The error is caught and logged, but the fallback behavior (returning all rooms) may not be the desired security behavior.

### Performance Impact

**Minimal**: Error handling adds negligible overhead

**No Database Impact**: Error occurs before database queries

**No Memory Leaks**: Error is properly caught and handled

---

## Evidence Documentation

### Log Evidence

**File**: `logs/local/warnings.log`

**Timestamp**: 2025-11-27 19:57:38

**Error**: `'User' object has no attribute 'get'`
- **Error Type**: `AttributeError`
- **Location**: `server.api.rooms`
- **Endpoint**: `/api/rooms/list`
- **Request ID**: `24202108-ebe6-41ad-96a7-9d0069351801`
- **Correlation ID**: `7a2fff5b-f308-45e2-89bc-94fa834f8f4a`

### Code Evidence

**File**: `server/api/rooms.py`

**Line 45**: Incorrect type annotation: `current_user: dict | None`

**Line 81**: Incorrect attribute access: `current_user.get("id", "")`

**File**: `server/auth/users.py`

**Line 155**: `get_current_user = fastapi_users.current_user(optional=True)`

- Returns: `User | None` (SQLAlchemy model, not dict)

**File**: `server/models/user.py`

**Line 28**: `class User(SQLAlchemyBaseUserTableUUID, Base)`

**Line 86**: `id` property provided by base class as attribute

### Reference Evidence (Correct Usage)

**File**: `server/api/players.py`

**Line 133**: `context.user_id = str(current_user.id)` ✅

**Line 382**: `user_id=current_user.id` ✅

**File**: `server/api/game.py`

**Line 63**: `admin_id=str(current_user.id)` ✅

**Line 77**: `broadcaster_id=str(current_user.id)` ✅

---

## Investigation Recommendations

### Immediate Priorities

1. **Fix Primary Issue**: Update `server/api/rooms.py` line 81 to use `current_user.id` instead of `current_user.get("id", "")`

2. **Fix Type Annotation**: Update `server/api/rooms.py` line 45 to use correct type: `current_user: User | None`

3. **Audit Similar Issues**: Check and fix similar issues in:

   - `server/api/metrics.py`
   - `server/api/admin/npc.py`

4. **Add Type Safety**: Consider adding runtime type checking or improving static type checking to catch these mismatches

### Further Investigation

1. **Test Exploration Filtering**: Verify that exploration filtering works correctly after fix

2. **Security Review**: Review whether fallback behavior (returning all rooms) is appropriate from a security perspective

3. **Pattern Standardization**: Create a helper function or utility for safely accessing user attributes to prevent future issues

4. **Type Checking**: Enable stricter type checking (mypy) to catch type annotation mismatches

---

## Remediation Prompt

**For Cursor Chat**:

```
Fix the AttributeError in the rooms API endpoint where current_user is incorrectly accessed as a dictionary.

The issue is in server/api/rooms.py:
- Line 45: Type annotation should be `User | None` instead of `dict | None`
- Line 81: Should use `current_user.id` instead of `current_user.get("id", "")`

Also check and fix similar issues in:
- server/api/metrics.py (lines 39, 42, and other uses of current_user.get())
- server/api/admin/npc.py (multiple uses of current_user.get("username"))

The correct pattern is to use attribute access (current_user.id, current_user.username) since get_current_user returns a User SQLAlchemy model object, not a dictionary.

After fixing, verify that:
1. Exploration filtering works correctly when filter_explored=true
2. No similar errors occur in metrics or admin endpoints
3. Type annotations match actual return types
```

---

## Investigation Completion Checklist

[x] All investigation steps completed as written

- [x] Comprehensive evidence collected and documented
- [x] Root cause analysis completed
- [x] System impact assessed
- [x] Investigation report generated
- [x] No attempt made to fix issues (investigation only)
- [x] All findings clearly documented with evidence
- [x] Only official test credentials would be used (not needed for this investigation)
- [x] Session logged in investigation history
- [x] Pattern analysis updated (similar issues found in other files)
- [x] Remediation prompt generated

---

## Additional Notes

### Pattern Detection

This investigation revealed a **recurring pattern** of type annotation mismatches:

- Multiple files incorrectly annotate `current_user` as `dict | None`
- Multiple files use dictionary-style `.get()` access on `User` objects
- This suggests a systematic issue that should be addressed across the codebase

### Knowledge Base Update

**Pattern to Watch For**: When using `get_current_user` from FastAPI Users:
✅ Correct: `current_user: User | None = Depends(get_current_user)`

✅ Correct: `current_user.id`, `current_user.username` (attribute access)

❌ Incorrect: `current_user: dict | None` (wrong type)
- ❌ Incorrect: `current_user.get("id")` (dictionary access on object)

---

*Investigation completed following the methodology from MYTHOSMUD_DEBUGGING_AGENT.mdc and GAME_BUG_INVESTIGATION_PLAYBOOK.mdc*
