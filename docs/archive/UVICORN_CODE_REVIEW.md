# Uvicorn/ASGI Code Review - feature/sqlite-to-postgresql Branch

**Review Date:** 2025-11-17
**Branch:** `feature/sqlite-to-postgresql`
**Reviewer:** AI Code Review Agent
**Scope:** ASGI/Uvicorn anti-patterns, errors, inefficiencies, and critical code issues

## Executive Summary

This review examines the codebase changes in the `feature/sqlite-to-postgresql` branch against Uvicorn/ASGI best
practices. The migration from SQLite to PostgreSQL has been implemented with generally good async patterns, but several
critical issues and anti-patterns were identified that could impact performance, reliability, and maintainability.

**Overall Assessment:** ⚠️ **MODERATE RISK** - Several issues require attention before production deployment.

---

## 🔴 CRITICAL ISSUES

### 1. Deprecated `asyncio.get_event_loop()` Usage

**Location:** `server/realtime/event_handler.py:501, 557, 734`

**Issue:** Using deprecated `asyncio.get_event_loop()` which can cause issues in async contexts and may raise
`RuntimeError` in Python 3.10+.

**Current Code:**

```python
loop = asyncio.get_event_loop()
if loop.is_running():
    # ...

```

**Problem:**

- `asyncio.get_event_loop()` is deprecated in Python 3.10+
- Can return a closed or different loop than the one currently running
- May cause `RuntimeError: There is no current event loop` in some contexts

**Recommendation:**

```python
try:
    loop = asyncio.get_running_loop()
    # Use loop directly or create_task

except RuntimeError:
    # No running loop - handle appropriately

    pass
```

**Priority:** HIGH - Can cause runtime errors in production

---

### 2. SQL Injection Risk in Field Name Construction

**Location:** `server/persistence.py:1543-1548`

**Issue:** Using f-string to construct SQL with field name, even though validated.

**Current Code:**

```python
cursor = conn.execute(
    f"""
    UPDATE players
    SET stats = jsonb_set(
        stats::jsonb,
        ARRAY['{field_name}']::text[],
        to_jsonb((stats->>%s)::integer + %s)
    )::text
    WHERE player_id = %s
    """,
    (field_name, delta, player_id_str),
)
```

**Analysis:**

- Field name is validated against a whitelist (lines 1512-1526)
- However, PostgreSQL's `ARRAY['{field_name}']::text[]` syntax cannot be parameterized
- While the whitelist provides security, the f-string construction is still an anti-pattern

**Recommendation:**

- Consider using a mapping dictionary for field names to array literals
- Or use PostgreSQL's `jsonb_set` with a parameterized path array construction
- Document the security control (whitelist validation) more prominently

**Priority:** MEDIUM - Security control exists but pattern is risky

---

### 3. Connection Pool Cleanup Verification

**Location:** `server/async_persistence.py:167-172`

**Issue:** `AsyncPersistenceLayer.close()` exists but needs verification it's called in all shutdown paths.

**Current Code:**

```python
async def close(self) -> None:
    """Close connection pool and cleanup resources."""
    if self._pool is not None:
        await self._pool.close()
        self._pool = None
        self._logger.info("Closed asyncpg connection pool")
```

**Status:** ✅ **VERIFIED** - Called via `container.shutdown()` in `server/container/main.py`

**Recommendation:** No action needed, but ensure all code paths that create `AsyncPersistenceLayer` instances also call
`close()`.

**Priority:** LOW - Already handled correctly

---

## 🟡 HIGH PRIORITY ISSUES

### 4. Blocking Operations in Async Context

**Location:** `server/utils/retry.py:193`

**Issue:** Using `time.sleep()` in async retry logic.

**Current Code:**

```python
time.sleep(delay)
```

**Problem:**

- `time.sleep()` blocks the event loop
- Should use `await asyncio.sleep(delay)` in async contexts

**Recommendation:**

- Check if this is in an async function
- If async, replace with `await asyncio.sleep(delay)`
- If sync, consider if it should be async

**Priority:** MEDIUM - Can impact performance under load

---

### 5. Event Loop Change Detection Complexity

**Location:** `server/database.py:205-252`

**Issue:** Complex logic for detecting event loop changes and recreating database engine.

**Current Code:**

```python
# CRITICAL: Check if we're in a different event loop than when engine was created

try:
    current_loop = asyncio.get_running_loop()
    current_loop_id = id(current_loop)
    if self._creation_loop_id is not None and current_loop_id != self._creation_loop_id:
        # ... complex disposal and recreation logic

```

**Analysis:**

- This is defensive programming for asyncpg's requirement that connections be created in the same loop
- However, the disposal logic is complex and may not always work correctly
- The comment indicates "asyncpg will handle cleanup when the loop closes" but then tries to dispose anyway

**Recommendation:**

- Simplify the disposal logic
- Consider if this is actually necessary - asyncpg should handle cleanup
- Add more comprehensive tests for this edge case

**Priority:** MEDIUM - Complex code that may not be necessary

---

### 6. Missing Error Context in Some Exception Handlers

**Location:** `server/api/players.py` (multiple locations)

**Issue:** Some exception handlers don't create proper error context before raising.

**Example:**

```python
except Exception as e:
    logger.error("Unexpected error in respawn endpoint", error=str(e), exc_info=True)
    context = _create_error_context(request, current_user)
    raise LoggedHTTPException(...)
```

**Analysis:**

- The pattern is generally good (using `_create_error_context` helper)
- However, some locations create context after logging, which means the log doesn't have full context

**Recommendation:**

- Create error context before logging
- Ensure all exception handlers follow the same pattern

**Priority:** LOW - Code quality improvement

---

## 🟢 MEDIUM PRIORITY ISSUES

### 7. F-String SQL Construction (Even with Constants)

**Location:** `server/async_persistence.py:186, 223, 256`

**Issue:** Using f-strings for SQL construction, even with compile-time constants.

**Current Code:**

```python
query = f"SELECT {PLAYER_COLUMNS} FROM players WHERE name = $1"
```

**Analysis:**

- `PLAYER_COLUMNS` is a compile-time constant, so this is safe
- However, it's still an anti-pattern that could be improved
- The comment acknowledges this: "Future: Migrate to SQLAlchemy ORM for better query construction"

**Recommendation:**

- Keep as-is for now (it's documented and safe)
- Prioritize migration to SQLAlchemy ORM as noted in comments

**Priority:** LOW - Documented technical debt

---

### 8. Inconsistent Async/Sync Patterns

**Location:** `server/persistence.py:1358, 1381, 1472`

**Issue:** Using `asyncio.to_thread()` to wrap sync operations, which is correct but indicates mixed patterns.

**Current Code:**

```python
await asyncio.to_thread(self.damage_player, player, amount, damage_type)
```

**Analysis:**

- This is the correct pattern for wrapping sync operations
- However, it indicates the codebase has both sync and async persistence layers
- The comments indicate this is intentional for backward compatibility

**Recommendation:**

- Continue migration to fully async patterns
- Document the migration strategy clearly

**Priority:** LOW - Intentional architecture decision

---

### 9. Missing Type Hints in Some Areas

**Location:** Various files

**Issue:** Some functions lack complete type hints, especially in error handling paths.

**Recommendation:**

- Add comprehensive type hints
- Use `mypy --strict` to catch missing types

**Priority:** LOW - Code quality improvement

---

## ✅ POSITIVE FINDINGS

### 1. Proper Connection Pool Management

✅ `AsyncPersistenceLayer` properly manages connection pools

✅ Pool configuration comes from config system

✅ Cleanup is handled in container shutdown

### 2. Good Error Handling Patterns

✅ Consistent use of structured logging

✅ Error context creation helpers

✅ Proper exception chaining

### 3. Async/Await Usage

✅ Generally correct async/await patterns

✅ Proper use of `asyncio.to_thread()` for blocking operations

✅ Good use of async context managers

### 4. Security Considerations

✅ Input validation in place

✅ Whitelist validation for SQL field names

✅ Parameterized queries where possible

---

## 📋 RECOMMENDATIONS SUMMARY

### Immediate Actions (Before Production)

1. **Fix `asyncio.get_event_loop()` usage** - Replace with `asyncio.get_running_loop()`
2. **Review SQL field name construction** - Consider safer alternatives
3. **Verify retry logic** - Ensure `time.sleep()` is not blocking event loop

### Short-term Improvements

1. Simplify event loop change detection logic
2. Standardize error context creation patterns
3. Add comprehensive type hints

### Long-term Improvements

1. Migrate to SQLAlchemy ORM for query construction
2. Complete migration to fully async patterns
3. Add more comprehensive async operation tests

---

## 🔍 TESTING RECOMMENDATIONS

1. **Event Loop Edge Cases:**

   - Test database engine recreation when event loop changes
   - Test connection pool behavior under high concurrency

2. **Error Handling:**

   - Test all exception paths have proper error context
   - Test retry logic doesn't block event loop

3. **Connection Cleanup:**

   - Test all shutdown paths properly close connection pools
   - Test graceful shutdown under load

---

## 📚 REFERENCES

[Uvicorn Best Practices](./.cursor/rules/uvicorn.mdc)

- [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [asyncpg Documentation](https://magicstack.github.io/asyncpg/current/)
- [FastAPI Best Practices](https://fastapi.tiangolo.com/tutorial/)

---

## CONCLUSION

The migration to PostgreSQL has been implemented with generally good async patterns and security considerations. The
main concerns are:

1. **Deprecated asyncio patterns** that need updating
2. **SQL construction patterns** that, while safe, could be improved
3. **Complex event loop handling** that may be unnecessary

These issues should be addressed before production deployment, but the codebase is in good shape overall. The use of
connection pooling, proper error handling, and structured logging demonstrates good engineering practices.

**Next Steps:**

1. Address critical issues (items 1-3)
2. Review and test event loop change detection
3. Continue migration to fully async patterns
4. Add comprehensive async operation tests
