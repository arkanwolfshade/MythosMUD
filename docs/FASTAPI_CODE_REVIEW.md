# FastAPI Code Review - Branch: feature/sqlite-to-postgresql

**Review Date:** 2025-11-17
**Reviewer:** AI Code Review Agent
**Scope:** Code changed in `feature/sqlite-to-postgresql` branch vs `main`

## Executive Summary

This review identifies FastAPI anti-patterns, errors, inefficiencies, and critical code issues based on FastAPI best practices. The review focused on API endpoints, database interactions, dependency injection, and async/await patterns.

## Critical Issues

### 1. Returning Pydantic Models Directly (Anti-Pattern)

**Severity:** Medium
**Location:** Multiple files

**Issue:** FastAPI best practices recommend returning dictionaries instead of Pydantic objects directly. While FastAPI can serialize Pydantic models, returning dicts is more efficient and avoids unnecessary conversions.

**Affected Files:**

- `server/api/players.py` - Lines 50, 60, 70, 77, 101, 117, 120, 136, 521, 611
- `server/auth/endpoints.py` - Line 445

**Example:**

```python
# ❌ ANTI-PATTERN: Returning Pydantic model directly
@player_router.post("/", response_model=PlayerRead)
async def create_player(...) -> PlayerRead:
    return await player_service.create_player(...)  # Returns PlayerRead directly
```

**Recommendation:**

```python
# ✅ CORRECT: Return dict or use model_dump()
@player_router.post("/", response_model=PlayerRead)
async def create_player(...) -> PlayerRead:
    player = await player_service.create_player(...)
    return player.model_dump()  # Convert to dict
```

**Note:** Some routes already use `model_dump()` correctly (e.g., lines 483, 499 in `players.py`), but consistency is needed.

### 2. Using Assert Statements in Production Code

**Severity:** High
**Location:** `server/api/players.py`

**Issue:** Assert statements can be disabled with Python's `-O` flag, causing silent failures in production.

**Affected Lines:**

- Line 78: `assert isinstance(result, list)`
- Lines 178, 200, 222, 244, 265, 287: `assert isinstance(result, dict)`

**Example:**

```python
# ❌ ANTI-PATTERN: Assert can be disabled
result = await player_service.list_players()
assert isinstance(result, list)
return result
```

**Recommendation:**

```python
# ✅ CORRECT: Use proper type checking or validation
result = await player_service.list_players()
if not isinstance(result, list):
    raise RuntimeError("Expected list from player_service.list_players()")
return result
```

### 3. Complex Exception Handling in Route Handlers

**Severity:** Medium
**Location:** `server/api/players.py`, `server/auth/endpoints.py`

**Issue:** Route handlers contain complex nested exception handling that could be simplified with centralized error handling or service layer exceptions.

**Affected Areas:**

- `server/api/players.py` - Lines 59-67, 109-115, 129-134, 147-162, etc.
- `server/auth/endpoints.py` - Lines 206-218

**Example:**

```python
# ❌ ANTI-PATTERN: Complex nested exception handling
try:
    return await player_service.create_player(...)
except ValidationError:
    context = create_context_from_request(request)
    if current_user:
        context.user_id = str(current_user.id)
    context.metadata["player_name"] = name
    raise LoggedHTTPException(...) from None
```

**Recommendation:** Move exception handling to service layer or use FastAPI exception handlers.

### 4. Direct Database Session Access in Route Handlers

**Severity:** Medium
**Location:** `server/api/players.py` - Line 325

**Issue:** Route handlers directly access database sessions instead of using service layer abstraction.

**Example:**

```python
# ❌ ANTI-PATTERN: Direct database access in route handler
async for session in get_async_session():
    from sqlalchemy import select
    result = await session.execute(select(Player).where(...))
```

**Recommendation:** Move database operations to service layer.

### 5. Inefficient Database Query Patterns

**Severity:** Low
**Location:** `server/async_persistence.py`

**Issue:** Some queries use f-strings for column names, though these are compile-time constants (safe per comments). However, the pattern could be improved.

**Note:** The code correctly uses parameterized queries for values (`$1`, `$2`), which is good. The f-strings for column names are compile-time constants, so they're safe from SQL injection.

### 6. Missing Input Validation

**Severity:** Medium
**Location:** `server/api/players.py`

**Issue:** Some route handlers accept query parameters without Pydantic validation.

**Example:**

```python
# ❌ ANTI-PATTERN: No validation on query parameters
@player_router.post("/{player_id}/sanity-loss")
async def apply_sanity_loss(
    player_id: str,
    amount: int,  # No validation for range
    ...
):
```

**Recommendation:** Use Pydantic models for request validation:

```python
# ✅ CORRECT: Use Pydantic for validation
class SanityLossRequest(BaseModel):
    amount: int = Field(..., ge=0, le=100)

@player_router.post("/{player_id}/sanity-loss")
async def apply_sanity_loss(
    player_id: str,
    request: SanityLossRequest,
    ...
):
```

### 7. Inconsistent Error Response Format

**Severity:** Low
**Location:** Multiple files

**Issue:** Some endpoints return different error response formats. Some use `LoggedHTTPException`, others use standard `HTTPException`.

**Recommendation:** Standardize on `LoggedHTTPException` for all error responses to ensure consistent logging.

### 8. Potential Blocking I/O in Async Routes

**Severity:** Low
**Location:** `server/api/players.py` - Line 365

**Issue:** Using synchronous `get_persistence()` in async route handler.

**Example:**

```python
# ⚠️ POTENTIAL ISSUE: Sync call in async route
persistence = get_persistence()  # This might block
room = persistence.get_room(str(respawn_room_id))
```

**Recommendation:** Ensure `get_persistence()` is thread-safe and doesn't block, or use async persistence layer.

## Performance Issues

### 1. Multiple Database Queries in Single Request

**Severity:** Low
**Location:** `server/api/players.py` - Lines 324-389

**Issue:** The `respawn_player` endpoint makes multiple sequential database queries that could potentially be optimized.

**Recommendation:** Consider batching queries or using joins where possible.

### 2. Unnecessary Object Creation

**Severity:** Low
**Location:** `server/api/players.py` - Line 89

**Issue:** Creating `StatsGenerator()` instance on every request instead of reusing.

**Recommendation:** Use dependency injection to provide a singleton or cached instance.

## Code Quality Issues

### 1. Missing Type Hints

**Severity:** Low
**Location:** Various files

**Issue:** Some function parameters and return types lack complete type hints.

**Recommendation:** Add complete type hints for better IDE support and type checking.

### 2. Long Route Handlers

**Severity:** Low
**Location:** `server/api/players.py` - `respawn_player` function (lines 297-414)

**Issue:** Route handler is 117 lines long, violating single responsibility principle.

**Recommendation:** Extract logic to service layer methods.

### 3. Duplicate Code Patterns

**Severity:** Low
**Location:** `server/api/players.py`

**Issue:** Similar error handling patterns repeated across multiple endpoints.

**Recommendation:** Extract to helper function or use decorator pattern.

## Security Considerations

### 1. SQL Injection Prevention ✅

**Status:** Good
**Location:** `server/async_persistence.py`

**Note:** Code correctly uses parameterized queries (`$1`, `$2`) for all user input. F-strings are only used for compile-time column names, which is safe.

### 2. Input Validation ✅

**Status:** Good
**Location:** `server/auth/endpoints.py`

**Note:** Password validation is implemented (lines 57-63).

### 3. Authentication/Authorization ✅

**Status:** Good
**Location:** Multiple files

**Note:** Routes properly use `Depends(get_current_user)` for authentication.

## Positive Patterns Found

1. ✅ **Proper Async/Await Usage:** Routes correctly use `async def` and `await` for I/O operations
2. ✅ **Dependency Injection:** Good use of FastAPI's `Depends()` for dependency injection
3. ✅ **Error Logging:** Comprehensive error logging with context
4. ✅ **Type Safety:** Good use of Pydantic models for request/response validation
5. ✅ **SQL Injection Prevention:** Proper use of parameterized queries

## Recommendations Summary

### High Priority

1. Replace `assert` statements with proper error handling
2. Standardize on returning dicts instead of Pydantic models directly (or document why models are returned)

### Medium Priority

1. Extract complex exception handling to service layer
2. Add Pydantic validation for query parameters
3. Move direct database access from route handlers to service layer
4. Refactor long route handlers (e.g., `respawn_player`)

### Low Priority

1. Optimize database queries (batch operations where possible)
2. Reuse service instances via dependency injection
3. Extract duplicate error handling patterns
4. Add complete type hints

## Conclusion

The codebase generally follows FastAPI best practices, with good use of async/await, dependency injection, and security measures. The main issues are:

1. **Returning Pydantic models directly** (performance optimization)
2. **Using assert statements** (production safety)
3. **Complex exception handling** (maintainability)

These issues are not critical but should be addressed to improve code quality, maintainability, and performance.
