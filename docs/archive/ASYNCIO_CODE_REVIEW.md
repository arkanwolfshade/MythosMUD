# Asyncio Code Review - feature/sqlite-to-postgresql Branch

**Review Date**: 2025-11-17
**Branch**: `feature/sqlite-to-postgresql`
**Reviewer**: AI Assistant (Auto)
**Scope**: Asyncio anti-patterns, errors, inefficiencies, and critical code issues

## Executive Summary

This review identified **4 critical issues**, **3 high-priority issues**, and **2 medium-priority improvements** in the
asyncio code patterns. The migration from SQLite to PostgreSQL has introduced several async/await anti-patterns that
need immediate attention.

---

## 🔴 CRITICAL ISSUES

### 1. Blocking Synchronous Operations in Async Methods

**Location**: `server/persistence.py` lines 1312-1351

**Issue**: The async wrapper methods (`async_damage_player`, `async_heal_player`, `async_gain_experience`) directly call
synchronous methods without using `asyncio.to_thread()`, which blocks the event loop.

**Code**:

```python
async def async_damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
    """..."""
    # Since the underlying operations are synchronous (psycopg2),
    # we call the sync version directly

    self.damage_player(player, amount, damage_type)  # ❌ BLOCKS EVENT LOOP
```

**Impact**:

- Blocks the entire event loop during database operations
- Prevents other async operations from executing
- Degrades performance under load
- Violates asyncio best practices

**Fix**:

```python
async def async_damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
    """Async wrapper for damage_player."""
    # Use asyncio.to_thread() to run blocking operations in thread pool

    await asyncio.to_thread(self.damage_player, player, amount, damage_type)
```

**Files Affected**:

- `server/persistence.py` lines 1312, 1333, 1422

---

### 2. asyncio.run() Called from Context with Existing Event Loop

**Location**: `server/realtime/connection_manager.py` line 1156

**Issue**: `asyncio.run()` is called as a fallback when no event loop is detected, but this can fail if called from
within an existing event loop context.

**Code**:

```python
try:
    loop = asyncio.get_running_loop()
    loop.create_task(self._check_and_process_disconnect(player_id))
except RuntimeError:
    # No running loop in this thread; execute synchronously

    asyncio.run(self._check_and_process_disconnect(player_id))  # ❌ DANGEROUS
```

**Impact**:

- Can raise `RuntimeError: asyncio.run() cannot be called from a running event loop`
- Creates nested event loops which are not supported
- Can cause deadlocks or unexpected behavior

**Fix**:

```python
try:
    loop = asyncio.get_running_loop()
    loop.create_task(self._check_and_process_disconnect(player_id))
except RuntimeError:
    # No running loop - schedule for execution when loop is available
    # Or use a thread-safe queue to defer execution

    logger.warning(
        "No event loop available for disconnect processing",
        player_id=player_id
    )
    # Schedule for later execution via a background task or queue

```

**Alternative Fix**: Use `asyncio.run_coroutine_threadsafe()` if you have access to the loop from another thread.

---

### 3. Connection Pool Resource Leak Risk

**Location**: `server/async_persistence.py` lines 125-143

**Issue**: The asyncpg connection pool is created but there's no guarantee it's properly closed during application
shutdown or error conditions.

**Code**:

```python
async def _get_pool(self) -> asyncpg.Pool:
    """Get or create connection pool for async database operations."""
    if self._pool is None:
        url = self._normalize_url()
        self._pool = await asyncpg.create_pool(
            url,
            min_size=1,
            max_size=10,
            command_timeout=60,
        )
        self._logger.info("Created asyncpg connection pool", pool_size=10)
    return self._pool

async def close(self) -> None:
    """Close connection pool and cleanup resources."""
    if self._pool is not None:
        await self._pool.close()
        self._pool = None
        self._logger.info("Closed asyncpg connection pool")
```

**Impact**:

- Connection pools may not be closed during application shutdown
- Database connections remain open, exhausting connection limits
- Memory leaks from unclosed pools
- No integration with application lifespan management

**Fix**: Ensure `close()` is called in application shutdown lifecycle:

```python
# In server/app/lifespan.py or ApplicationContainer (server/container/main.py)

async def shutdown(self):
    """Cleanup resources on shutdown."""
    if hasattr(self, 'async_persistence') and self.async_persistence:
        await self.async_persistence.close()
```

**Verification**: Check that `ApplicationContainer` or lifespan manager calls `async_persistence.close()`.

---

### 4. Missing Exception Handling in Pool Creation

**Location**: `server/async_persistence.py` line 129

**Issue**: `asyncpg.create_pool()` can raise exceptions (connection errors, authentication failures) that aren't caught,
causing unhandled exceptions.

**Code**:

```python
async def _get_pool(self) -> asyncpg.Pool:
    if self._pool is None:
        url = self._normalize_url()
        self._pool = await asyncpg.create_pool(...)  # ❌ No exception handling
        self._logger.info("Created asyncpg connection pool", pool_size=10)
    return self._pool
```

**Impact**:

- Unhandled exceptions crash the application
- No retry logic for transient connection failures
- Poor error messages for debugging

**Fix**:

```python
async def _get_pool(self) -> asyncpg.Pool:
    """Get or create connection pool for async database operations."""
    if self._pool is None:
        url = self._normalize_url()
        try:
            self._pool = await asyncpg.create_pool(
                url,
                min_size=1,
                max_size=10,
                command_timeout=60,
            )
            self._logger.info("Created asyncpg connection pool", pool_size=10)
        except asyncpg.PostgresError as e:
            context = create_error_context()
            context.metadata["operation"] = "create_connection_pool"
            log_and_raise(
                DatabaseError,
                f"Failed to create database connection pool: {e}",
                context=context,
                details={"database_url": url[:50], "error": str(e)},
                user_friendly="Database connection failed",
            )
    return self._pool
```

---

## 🟡 HIGH PRIORITY ISSUES

### 5. Event Loop Change Detection May Not Handle All Cases

**Location**: `server/database.py` lines 205-241

**Issue**: Complex logic for detecting event loop changes and recreating the engine, but edge cases may exist where the
engine is used in a different loop without detection.

**Code**:

```python
# CRITICAL: Check if we're in a different event loop than when engine was created

try:
    current_loop = asyncio.get_running_loop()
    current_loop_id = id(current_loop)
    if self._creation_loop_id is not None and current_loop_id != self._creation_loop_id:
        # Dispose and recreate...

except RuntimeError:
    # No running loop - that's okay, engine will be created when needed

    pass
```

**Impact**:

- asyncpg connections are tied to specific event loops
- Using connections from wrong loop causes errors
- Detection may miss some edge cases (e.g., loop replacement)

**Recommendation**: Add more defensive checks and logging to catch edge cases.

---

### 6. Synchronous Database Operations in Async Context

**Location**: `server/persistence.py` throughout

**Issue**: The synchronous `PersistenceLayer` uses `psycopg2` (blocking driver) but is called from async contexts via
wrapper methods.

**Impact**:

- All sync persistence operations block the event loop
- Should migrate to fully async operations using `AsyncPersistenceLayer`
- Current pattern is a temporary migration state

**Recommendation**:

- Prioritize migration to `AsyncPersistenceLayer` for all async code paths
- Document which methods should use async persistence vs sync persistence
- Add deprecation warnings to sync methods when called from async contexts

---

### 7. Missing Transaction Management in Batch Operations

**Location**: `server/async_persistence.py` lines 403-461

**Issue**: `save_players()` uses explicit transaction, but error handling may not properly rollback on all failure
paths.

**Code**:

```python
async with pool.acquire() as conn:
    async with conn.transaction():  # Explicit transaction for atomicity
        for player in players:
            try:
                # ... save player ...

            except (ValueError, TypeError, KeyError) as e:
                self._logger.warning(...)
                continue  # ⚠️ Continues loop but transaction still active
```

**Impact**:

- Partial failures may not rollback correctly
- Some players saved, others not, violating atomicity
- Error handling could be clearer

**Recommendation**: Review error handling to ensure proper rollback on critical failures.

---

## 🟢 MEDIUM PRIORITY IMPROVEMENTS

### 8. Connection Pool Size Configuration

**Location**: `server/async_persistence.py` line 132

**Issue**: Connection pool size is hardcoded (max_size=10) instead of being configurable.

**Recommendation**: Make pool size configurable via config system:

```python
from .config import get_config

config = get_config()
self._pool = await asyncpg.create_pool(
    url,
    min_size=config.database.pool_min_size or 1,
    max_size=config.database.pool_max_size or 10,
    command_timeout=config.database.command_timeout or 60,
)
```

---

### 9. F-String SQL Queries (Minor Security Concern)

**Location**: `server/async_persistence.py` throughout

**Issue**: F-strings are used for SQL queries with column names, which is safe but could be more explicit.

**Code**:

```python
row = await conn.fetchrow(f"SELECT {PLAYER_COLUMNS} FROM players WHERE name = $1", name)
```

**Note**: This is actually safe because `PLAYER_COLUMNS` is a constant, not user input. However, the pattern could be
clearer.

**Recommendation**: Consider using SQLAlchemy Core or a query builder for better type safety, or at least document that
column names are constants.

---

## ✅ POSITIVE FINDINGS

1. **Good Use of Connection Pooling**: `async_persistence.py` properly uses asyncpg connection pools
2. **Proper Async Context Managers**: Connection acquisition uses `async with pool.acquire()`
3. **Explicit Column Lists**: Avoids `SELECT *` anti-pattern with `PLAYER_COLUMNS` constant
4. **Transaction Management**: Batch operations use explicit transactions
5. **Error Context**: Good use of error context and structured logging

---

## 📋 RECOMMENDATIONS SUMMARY

### Immediate Actions (Critical)

1. ✅ Fix blocking operations in async methods (Issue #1)
2. ✅ Fix `asyncio.run()` usage (Issue #2)
3. ✅ Ensure connection pool cleanup (Issue #3)
4. ✅ Add exception handling for pool creation (Issue #4)

### Short-term (High Priority)

1. Review event loop change detection logic
2. Plan migration from sync to async persistence
3. Review transaction error handling

### Long-term (Medium Priority)

1. Make connection pool sizes configurable
2. Consider query builder for type safety

---

## 🔍 TESTING RECOMMENDATIONS

1. **Add tests for event loop changes**: Test database operations when event loop changes
2. **Test connection pool cleanup**: Verify pools are closed during shutdown
3. **Test blocking operations**: Verify `asyncio.to_thread()` fixes don't block event loop
4. **Load testing**: Test under high concurrency to catch blocking issues

---

## 📚 REFERENCES

[asyncio Best Practices](./.cursor/rules/asyncio.mdc)

- [PostgreSQL asyncpg Documentation](https://magicstack.github.io/asyncpg/)
- [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)

---

**Review Status**: ⚠️ **REQUIRES IMMEDIATE ATTENTION**

**Next Steps**:

1. Address critical issues #1-4 before merging to main
2. Create GitHub issues for high-priority items
3. Schedule code review session to discuss migration strategy
