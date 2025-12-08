# Bug Investigation Report: SQL Syntax Error in Rooms List API

**Investigation Date**: 2025-12-07
**Investigator**: AI Assistant (GPT-4)
**Session ID**: 2025-12-07_session-sql-syntax-error-rooms-list
**Bug Type**: Server-Side Database Query Error
**Severity**: Medium (Non-blocking but causes incorrect behavior)

---

## Executive Summary

A `ProgrammingError` occurs in the `/api/rooms/list` endpoint when attempting to filter rooms by exploration status. The error `syntax error at or near ":"` indicates that the SQL query mixing SQLAlchemy parameter syntax (`:room_ids`) with PostgreSQL casting syntax (`::uuid[]`) is incompatible with asyncpg's parameter binding mechanism. The error is caught and handled gracefully (returns all rooms instead of failing), but the exploration filtering feature does not work as intended.

**Root Cause**: SQL syntax incompatibility - SQLAlchemy's `text()` parameterized queries using `:parameter` syntax cannot be directly combined with PostgreSQL casting syntax `::type[]` when using asyncpg. The parameter parser interprets the `::` after the colon as part of the parameter name, causing a syntax error.

**Impact**: Exploration-based room filtering is non-functional when `filter_explored=true` is used. The API falls back to returning all rooms, which may expose unexplored room data to clients.

---

## Detailed Findings

### 1. Error Log Analysis

**Source**: `logs/local/warnings.log` (line 1)

```
2025-12-07 20:30:30 - server.api.rooms - WARNING -
error='(sqlalchemy.dialects.postgresql.asyncpg.ProgrammingError)
<class 'asyncpg.exceptions.PostgresSyntaxError'>: syntax error at or near ":"
[SQL: SELECT stable_id FROM rooms WHERE id = ANY(:room_ids::uuid[])]
(Background on this error at: https://sqlalche.me/e/20/f405)'
error_type='ProgrammingError'
event='Error filtering by explored rooms, returning all rooms'
correlation_id='396d2c41-2890-44a6-b6d0-247d2cc1fc7d'
timestamp='2025-12-08T03:30:30.983824Z'
request_id='78ca82f3-950f-460b-a684-893a019d08af'
path='/api/rooms/list'
method='GET'
```

**Key Observations**:

- Error occurs in `server.api.rooms` module
- Error type: `ProgrammingError` (asyncpg `PostgresSyntaxError`)
- Error message: `syntax error at or near ":"`
- SQL query: `SELECT stable_id FROM rooms WHERE id = ANY(:room_ids::uuid[])`
- Event: "Error filtering by explored rooms, returning all rooms"
- Request path: `/api/rooms/list`
- Error is caught and handled (warning level, not error)
- API continues execution and returns all rooms as fallback

### 2. Code Analysis

**File**: `server/api/rooms.py`

**Problematic Code** (line 148):

```python
lookup_query = text("SELECT stable_id FROM rooms WHERE id = ANY(:room_ids::uuid[])")
result = await session.execute(lookup_query, {"room_ids": explored_room_ids})
```

**Code Context** (lines 130-173):

```python
# Filter by explored rooms if requested and user is authenticated
if filter_explored and current_user:
    try:
        # Get player from user
        persistence = request.app.state.persistence
        user_id = str(current_user.id)
        player = await persistence.get_player_by_user_id(user_id)

        if player:
            # Get explored rooms for this player
            exploration_service = get_exploration_service()
            player_id = uuid.UUID(str(player.player_id))
            explored_room_ids = await exploration_service.get_explored_rooms(player_id, session)

            # Convert explored room UUIDs to stable_ids for filtering
            # We need to look up stable_ids from room UUIDs
            if explored_room_ids:
                # Query to get stable_ids from room UUIDs (using PostgreSQL array syntax)
                lookup_query = text("SELECT stable_id FROM rooms WHERE id = ANY(:room_ids::uuid[])")
                result = await session.execute(lookup_query, {"room_ids": explored_room_ids})
                explored_stable_ids = {row[0] for row in result.fetchall()}

                # Filter rooms to only include explored ones
                rooms = [room for room in rooms if room.get("id") in explored_stable_ids]

                # ... logging ...
            else:
                # Player has explored no rooms - return empty list
                rooms = []
        else:
            logger.warning("Player not found for user, cannot filter by exploration", user_id=user_id)
    except Exception as e:
        # Log error but don't fail the request - just return all rooms
        logger.warning(
            "Error filtering by explored rooms, returning all rooms",
            error=str(e),
            error_type=type(e).__name__,
        )
```

### 3. Root Cause Analysis

**Primary Issue**: SQL Syntax Incompatibility

The SQL query attempts to use both SQLAlchemy's parameter binding syntax (`:room_ids`) and PostgreSQL casting syntax (`::uuid[]`) in the same expression:

```sql
SELECT stable_id FROM rooms WHERE id = ANY(:room_ids::uuid[])
```

**Why This Fails**:

1. **SQLAlchemy Parameter Binding**: SQLAlchemy's `text()` function uses `:parameter_name` syntax for parameterized queries. When executed with asyncpg (the async PostgreSQL driver), SQLAlchemy translates this to asyncpg's native parameter syntax.

2. **PostgreSQL Casting Syntax**: PostgreSQL uses `::type` for type casting. However, when this follows immediately after a parameter placeholder (`:room_ids::uuid[]`), asyncpg's parameter parser gets confused.

3. **Parser Conflict**: The `::` after the colon (`:room_ids::`) is interpreted as part of the parameter name or invalid syntax, causing asyncpg to throw a `PostgresSyntaxError` with "syntax error at or near :".

4. **Parameter Value Type**: The `explored_room_ids` parameter is passed as a Python list of UUID strings, which SQLAlchemy/asyncpg needs to convert to a PostgreSQL UUID array. The current approach of trying to cast in the SQL string conflicts with parameter binding.

**Technical Details**:

- **Database Driver**: asyncpg (async PostgreSQL driver)
- **ORM Layer**: SQLAlchemy 2.0+ with async support
- **Query Method**: `text()` wrapper for raw SQL
- **Parameter Binding**: Named parameters (`:parameter_name`)
- **Parameter Value**: Python list of UUID strings

### 4. System Impact Assessment

**Severity**: Medium

**Scope**:

- **Affected Endpoint**: `/api/rooms/list` (GET)
- **Affected Feature**: Exploration-based room filtering (`filter_explored=true`)
- **Affected Users**: Authenticated users attempting to view only explored rooms

**Behavioral Impact**:

- ✅ **No Crash**: Error is caught and handled gracefully
- ✅ **Fallback Behavior**: API returns all rooms instead of failing
- ⚠️ **Feature Degradation**: Exploration filtering does not work
- ⚠️ **Security Impact**: May expose unexplored room data to clients when filtering is expected
- ⚠️ **User Experience**: Users see all rooms even when requesting filtered view

**Performance Impact**: Minimal

- Error occurs only when `filter_explored=true` and user is authenticated
- Exception handling adds minimal overhead
- Fallback behavior (returning all rooms) has same performance as non-filtered query

### 5. Evidence Documentation

**Error Log Entry**:

- **File**: `logs/local/warnings.log`
- **Line**: 1
- **Timestamp**: 2025-12-07 20:30:30 (UTC: 2025-12-08T03:30:30.983824Z)
- **Request ID**: `78ca82f3-950f-460b-a684-893a019d08af`
- **Correlation ID**: `396d2c41-2890-44a6-b6d0-247d2cc1fc7d`
- **Request Path**: `/api/rooms/list`
- **HTTP Method**: GET
- **User Agent**: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0

**Code Location**:

- **File**: `server/api/rooms.py`
- **Line**: 148
- **Function**: `list_rooms()` endpoint handler
- **Code Block**: Exploration filtering logic (lines 130-173)

**SQL Query**:

```sql
SELECT stable_id FROM rooms WHERE id = ANY(:room_ids::uuid[])
```

**Parameter Binding**:

```python
{"room_ids": explored_room_ids}  # explored_room_ids is list[str] of UUID strings
```

### 6. Related Code Patterns

**Similar Patterns in Codebase**:

- The codebase uses `text()` wrapper for raw SQL queries consistently
- Parameterized queries use `:parameter_name` syntax throughout
- No other instances of mixing parameter syntax with casting syntax found
- PostgreSQL array operations are used elsewhere but with different patterns

**Query Pattern Analysis**:

- ✅ **Correct Pattern** (used elsewhere): Separate casting from parameter binding
- ❌ **Incorrect Pattern** (current bug): Mixing parameter syntax with casting syntax

### 7. Investigation Recommendations

**Priority 1 - Immediate**:

- Fix SQL query syntax to properly handle UUID array parameter binding
- Test exploration filtering feature to ensure it works correctly
- Verify that only explored rooms are returned when `filter_explored=true`

**Priority 2 - Follow-up**:

- Review other SQL queries for similar parameter binding issues
- Consider adding integration tests for exploration filtering
- Document proper pattern for PostgreSQL array parameter binding with asyncpg

**Priority 3 - Enhancement**:

- Consider using SQLAlchemy ORM for this query instead of raw SQL
- Evaluate performance impact of current approach vs. ORM approach
- Add error handling that provides more specific error messages

### 8. Technical Analysis

**SQLAlchemy/asyncpg Compatibility**:

- SQLAlchemy 2.0+ supports async operations through asyncpg
- `text()` wrapper is required for raw SQL in async contexts
- Parameter binding syntax is driver-dependent
- asyncpg uses `$1, $2, ...` for positional parameters, but SQLAlchemy translates named parameters

**PostgreSQL Array Operations**:

- PostgreSQL supports array operations with `ANY(array_parameter)`
- Type casting with `::uuid[]` is valid PostgreSQL syntax
- Parameter binding requires proper type handling

**Correct Approaches** (not implemented, for reference):

1. **Use `bindparam()` with type specification**:

   ```python
   from sqlalchemy import bindparam
   lookup_query = text("SELECT stable_id FROM rooms WHERE id = ANY(:room_ids)").bindparams(
       bindparam("room_ids", explored_room_ids, expanding=True)
   )
   ```

2. **Cast in the WHERE clause differently**:

   ```python
   lookup_query = text("SELECT stable_id FROM rooms WHERE id::text = ANY(:room_ids)")
   ```

3. **Use SQLAlchemy array literal**:

   ```python
   from sqlalchemy import literal
   lookup_query = text("SELECT stable_id FROM rooms WHERE id = ANY(:room_ids::uuid[])")
   ```

---

## Remediation Prompt

**For Cursor Chat**:

```
Fix the SQL syntax error in the rooms list API endpoint. The query
`SELECT stable_id FROM rooms WHERE id = ANY(:room_ids::uuid[])` fails
because SQLAlchemy's parameter binding syntax (`:room_ids`) cannot be
directly combined with PostgreSQL casting syntax (`::uuid[]`) when using
asyncpg.

Location: server/api/rooms.py:148

The query should properly bind a Python list of UUID strings as a
PostgreSQL UUID array parameter. Use SQLAlchemy's bindparam() with
appropriate type handling, or restructure the query to avoid mixing
parameter syntax with casting syntax.

Verify the fix works by testing the /api/rooms/list endpoint with
filter_explored=true parameter.
```

---

## Investigation Completion Checklist

- [x] All investigation steps completed as written
- [x] Comprehensive evidence collected and documented
- [x] Root cause analysis completed
- [x] System impact assessed
- [x] Investigation report generated
- [x] No attempt made to fix issues (investigation only)
- [x] All findings clearly documented with evidence
- [x] Session logged in investigation history
- [x] Remediation prompt generated

---

**Investigation Status**: ✅ COMPLETE

**Next Steps**: Use the remediation prompt above to fix the SQL syntax error.
