# Asynchronous Code Audit - December 3, 2025

**Auditor**: AI Assistant (Untenured Professor of Occult Studies)
**Branch**: Current working branch
**Audit Date**: December 3, 2025
**Audit Scope**: Full codebase async/await patterns against AnyIO and asyncio best practices
**Referenced Guidelines**:

- `.cursor/rules/anyio.mdc`
- `.cursor/rules/asyncio.mdc`
- Previous code reviews (ASYNCIO_CODE_REVIEW.md, NATS_CODE_REVIEW.md)
- Performance investigation (2025-11-30_session-001_passive-sanity-flux-performance.md)

---

## Executive Summary

This comprehensive audit identified **27 findings** across four severity levels:

| Severity                | Count | Status                        |
| ----------------------- | ----- | ----------------------------- |
| 🔴 **Critical**          | 6     | Requires immediate attention  |
| 🟡 **High Priority**     | 8     | Address within current sprint |
| 🟢 **Medium Priority**   | 7     | Plan for next sprint          |
| ✅ **Positive Findings** | 6     | Good patterns to maintain     |

**Overall Assessment**: The codebase demonstrates strong architectural patterns (task tracking, structured concurrency,
error boundaries) but has several critical anti-patterns that significantly impact performance and reliability.
Progressive performance degradation in passive lucidity flux processing (3.4s → 17.4s over 4 ticks) indicates severe
blocking operations in async contexts.

**Risk Level**: ⚠️ **HIGH** - Blocking operations causing 1,639% overhead, progressive degradation, and potential event
loop starvation.

---

## 🔴 CRITICAL ISSUES

### 1. Synchronous Blocking Operations in Async Context (CONFIRMED PERFORMANCE ISSUE)

**Location**: Multiple files

- `server/services/passive_lucidity_flux_service.py` line 242
- `server/persistence.py` (partially mitigated with asyncio.to_thread)
- `server/realtime/nats_message_handler.py` lines 605-633

**Issue**: Synchronous database and I/O operations called directly from async functions without asyncio.to_thread(),
blocking the event loop.

**Evidence**:

- Performance investigation shows 17.4s delays in passive lucidity flux processing
- Root cause: `self._persistence.get_room()` called synchronously from async function
- Progressive degradation: 3.4s → 6.4s → 15.1s → 17.4s (1,639% overhead)

**Code Example**:

```python
# ❌ WRONG - Blocks event loop

async def _resolve_context(self, player, timestamp):
    room = self._persistence.get_room(player.room_id)  # SYNCHRONOUS BLOCKING CALL
    # ...

```

**Impact**:
**Event Loop Blocking**: Each synchronous call blocks ALL async operations

**Progressive Degradation**: Performance degrades over time (resource accumulation)

**Cascading Delays**: One slow operation delays all concurrent operations

**User Experience**: 17-second lags during game ticks

**Scalability**: Issue worsens linearly with player count

**Fix**:

```python
# ✅ CORRECT - Non-blocking

async def _resolve_context(self, player, timestamp):
    room = await self._persistence.async_get_room(player.room_id)
    # OR if async method not available:

    room = await asyncio.to_thread(self._persistence.get_room, player.room_id)
    # ...

```

**Files Requiring Immediate Fixes**:

1. `server/services/passive_lucidity_flux_service.py` - Replace sync room lookups
2. `server/realtime/nats_message_handler.py` - Replace sync mute data loading
3. Any other service calling sync persistence methods from async contexts

**Priority**: 🔴 **CRITICAL** - Blocking issue #1
**Estimated Effort**: 8-16 hours (requires testing)
**Dependencies**: AsyncPersistenceLayer must support all required methods

---

### 2. asyncio.run() Called from Existing Event Loop Context

**Location**:

- `server/services/exploration_service.py` line 379
- Previously in `server/realtime/connection_manager.py` (may be fixed)

**Issue**: `asyncio.run()` creates a new event loop, which fails if called from within an existing event loop context.

**Code**:

```python
# ❌ DANGEROUS - Can cause RuntimeError

try:
    loop = asyncio.get_running_loop()
    loop.create_task(_mark_explored_async())
except RuntimeError:
    # No running loop - run in a new event loop

    asyncio.run(_mark_explored_async())  # ❌ MAY STILL BE IN LOOP CONTEXT
```

**Impact**:

- RuntimeError: "asyncio.run() cannot be called from a running event loop"
- Unpredictable behavior if error handling is inadequate
- Potential deadlocks or nested event loop issues

**Fix**:

```python
# ✅ CORRECT - Handle all cases

try:
    loop = asyncio.get_running_loop()
    loop.create_task(_mark_explored_async())
except RuntimeError:
    # No running loop - defer execution or use thread-safe scheduling

    logger.warning("No event loop available, deferring operation")
    # Option 1: Use a queue for deferred execution
    # Option 2: Use asyncio.run_coroutine_threadsafe if you have loop reference
    # Option 3: Make calling code fully async

```

**Priority**: 🔴 **CRITICAL** - Can cause crashes
**Estimated Effort**: 4-8 hours
**Recommendation**: Eliminate all `asyncio.run()` calls from library code; use only in entry points

---

### 3. Connection Pool Resource Leak Risk

**Location**: `server/async_persistence.py` lines 125-143

**Issue**: asyncpg connection pool created but no guarantee it's closed during shutdown or error conditions.

**Code**:

```python
async def _get_pool(self) -> asyncpg.Pool:
    if self._pool is None:
        self._pool = await asyncpg.create_pool(...)  # Created
    return self._pool

async def close(self) -> None:
    if self._pool is not None:
        await self._pool.close()  # Closed only if explicitly called
        self._pool = None
```

**Impact**:

- Connection pools may not close during application shutdown
- Database connections exhausted over time
- Memory leaks from unclosed pools
- "too many connections" errors from PostgreSQL

**Fix**:

```python
# In server/app/container.py shutdown method

async def shutdown(self):
    """Cleanup resources on shutdown."""
    if hasattr(self, 'async_persistence') and self.async_persistence:
        logger.info("Closing async persistence connection pool")
        await self.async_persistence.close()
    # ... other shutdown operations

```

**Verification Required**:

- Check that `ApplicationContainer.shutdown()` calls `async_persistence.close()`
- Check that lifespan manager calls `container.shutdown()`
- Add tests to verify pool closure

**Priority**: 🔴 **CRITICAL** - Resource leak
**Estimated Effort**: 2-4 hours (verification + testing)

---

### 4. Missing Exception Handling in Pool Creation

**Location**: `server/async_persistence.py` line 129

**Issue**: `asyncpg.create_pool()` can raise exceptions that aren't caught, causing unhandled exceptions.

**Code**:

```python
async def _get_pool(self) -> asyncpg.Pool:
    if self._pool is None:
        url = self._normalize_url()
        self._pool = await asyncpg.create_pool(...)  # ❌ No exception handling
        self._logger.info("Created asyncpg connection pool")
    return self._pool
```

**Impact**:

- Unhandled exceptions crash the application
- No retry logic for transient connection failures
- Poor error messages for debugging
- Application won't start if database is temporarily unavailable

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
        except (asyncpg.PostgresError, ConnectionError, OSError) as e:
            context = create_error_context()
            context.metadata["operation"] = "create_connection_pool"
            log_and_raise(
                DatabaseError,
                f"Failed to create database connection pool: {e}",
                context=context,
                details={
                    "database_url": url[:50],  # Truncate for security
                    "error": str(e),
                    "error_type": type(e).__name__
                },
                user_friendly="Database connection failed. Please check database configuration.",
            )
    return self._pool
```

**Priority**: 🔴 **CRITICAL** - Crashes on connection failure
**Estimated Effort**: 2-3 hours

---

### 5. Blocking Operations in NATS Message Handlers

**Location**: `server/realtime/nats_message_handler.py` lines 605-633

**Issue**: Synchronous database operations in message handlers cause message processing delays and queue buildup.

**Code**:

```python
# ❌ WRONG - Synchronous operation in async handler

for receiver_id in receiver_ids:
    try:
        user_manager.load_player_mutes(receiver_id)  # SYNCHRONOUS DATABASE CALL
```

**Impact**:

- Message processing delays under high traffic
- Message queue buildup
- Violates NATS best practice: "Don't use blocking operations in message handlers"
- Cascading delays across all NATS subscribers

**Fix**:

```python
# ✅ CORRECT - Async batch loading with caching
# Option 1: Batch load all mute data at once

mute_data = await asyncio.gather(
    *[asyncio.to_thread(user_manager.load_player_mutes, rid) for rid in receiver_ids],
    return_exceptions=True
)

# Option 2: Cache mute data with TTL (better)

async def _get_player_mutes_cached(self, player_id: str) -> set:
    if player_id in self._mute_cache and not self._is_cache_expired(player_id):
        return self._mute_cache[player_id]

    mutes = await asyncio.to_thread(user_manager.load_player_mutes, player_id)
    self._mute_cache[player_id] = (mutes, time.time())
    return mutes
```

**Priority**: 🔴 **CRITICAL** - Performance bottleneck
**Estimated Effort**: 4-6 hours (implement caching)

---

### 6. F-String Logging Destroying Structured Logging

**Location**: Throughout codebase (detected in examples)

**Issue**: Using f-strings in logging calls destroys structured logging benefits.

**Code**:

```python
# ❌ WRONG - Destroys structured logging

logger.info(f"Starting combat between {attacker} and {target}")
logger.error(f"Failed to process: {error}")
logger.debug(f"Message data: {message_data}")
```

**Impact**:
**Cannot search by specific fields**: Logs become plain text

**Cannot create alerts**: No structured data for monitoring

**Cannot correlate events**: Lost relationships between log entries

**Reduced performance**: String formatting slower than structured data

**Breaks log aggregation**: Cannot analyze or filter effectively

**Fix**:

```python
# ✅ CORRECT - Structured logging

logger.info("Starting combat", attacker=attacker, target=target, room_id=room_id)
logger.error("Failed to process", error=str(error), operation="combat_start")
logger.debug("NATS message received", message_data=message_data, message_type=type(message_data))
```

**Detection**:

```bash
# Find all f-string logging (requires manual review)

rg 'logger\.(debug|info|warning|error|critical)\(f"' server/
```

**Priority**: 🔴 **CRITICAL** - Affects monitoring and debugging
**Estimated Effort**: 16-24 hours (widespread issue)
**Note**: This is a coding standard violation that impacts operations

---

## 🟡 HIGH PRIORITY ISSUES

### 7. Missing Room Lookup Caching

**Location**: `server/services/passive_lucidity_flux_service.py`

**Issue**: Room data looked up for every player on every tick, even if:

- Players are in the same room
- Room data hasn't changed
- Room was recently looked up

**Impact**:

- Unnecessary database/IO operations
- Contributes to 17-second tick delays
- Scales poorly with player count

**Fix**:

```python
# Add room cache with TTL

class PassiveLucidityFluxService:
    def __init__(self, ...):
        self._room_cache: dict[str, tuple[Room, float]] = {}
        self._room_cache_ttl = 60.0  # 60 second TTL

    async def _get_room_cached(self, room_id: str) -> Room:
        if room_id in self._room_cache:
            room, timestamp = self._room_cache[room_id]
            if time.time() - timestamp < self._room_cache_ttl:
                return room

        room = await self._persistence.async_get_room(room_id)
        self._room_cache[room_id] = (room, time.time())
        return room
```

**Priority**: 🟡 **HIGH** - Performance optimization
**Estimated Effort**: 3-4 hours

---

### 8. Incomplete Migration to Async Persistence

**Location**: Throughout codebase

**Issue**: Many async functions still call synchronous `PersistenceLayer` methods instead of `AsyncPersistenceLayer`
methods.

**Impact**:

- Event loop blocking across application
- Degraded performance
- Confusion about which layer to use

**Fix**:

1. Audit all async functions for sync persistence calls
2. Migrate to `async_persistence.method()` or wrap with `asyncio.to_thread()`
3. Add deprecation warnings to sync methods when called from async contexts

**Priority**: 🟡 **HIGH** - Architectural debt
**Estimated Effort**: 24-40 hours (large refactor)

---

### 9. Multiple Database Flushes Before Commit

**Location**: `server/services/passive_lucidity_flux_service.py`

**Issue**: Each `apply_lucidity_adjustment()` calls `flush()` before the final `commit()`.

**Impact**:

- Multiple round-trips to database
- Potential lock contention
- Increased transaction overhead
- Contributes to progressive degradation

**Fix**:

```python
# Batch all adjustments, flush once before commit

async with session.begin():
    for player in players:
        # Apply adjustments (don't flush)

        await lucidity_service.apply_lucidity_adjustment(
            ...,
            auto_flush=False  # Add parameter
        )
    # Flush once before commit

    await session.flush()
    # Commit happens automatically

```

**Priority**: 🟡 **HIGH** - Performance optimization
**Estimated Effort**: 4-6 hours

---

### 10. Loading All Players Instead of Active Only

**Location**: `server/services/passive_lucidity_flux_service.py` line 224

**Issue**: `_load_players()` loads ALL players, not just active/online players.

**Impact**:

- Unnecessary data loading
- Memory overhead
- Processing inactive players wastes CPU

**Fix**:

```python
async def _load_players(self, session: AsyncSession) -> list[Player]:
    """Load only active/online players for processing."""
    result = await session.execute(
        select(Player)
        .where(Player.is_active == True)  # Only active players
        .where(Player.last_seen > datetime.now() - timedelta(hours=1))  # Recently active
    )
    return list(result.scalars().all())
```

**Priority**: 🟡 **HIGH** - Performance + correctness
**Estimated Effort**: 2-3 hours

---

### 11. NATS Connection Pool Not Used by Default

**Location**: `server/services/nats_service.py` line 362

**Issue**: `publish()` method uses single connection instead of connection pool.

**Impact**:

- Connection pooling benefits not realized
- Single connection becomes bottleneck
- Pool initialization overhead wasted

**Fix**:

```python
async def publish(self, subject: str, message: dict[str, Any], **kwargs) -> bool:
    """Publish message using connection pool by default."""
    # Use connection pool for better performance

    return await self.publish_with_pool(subject, message, **kwargs)
```

**Priority**: 🟡 **HIGH** - Performance optimization
**Estimated Effort**: 2-3 hours

---

### 12. No TLS Configuration for NATS

**Location**: `server/config/models.py` lines 139-182

**Issue**: `NATSConfig` class lacks TLS/SSL configuration options.

**Impact**:

- Messages transmitted in plaintext
- Vulnerable to man-in-the-middle attacks
- Security compliance violation

**Fix**:

```python
class NATSConfig(BaseSettings):
    url: str = Field(default="nats://localhost:4222", ...)
    # Add TLS fields

    tls_cert: str | None = Field(default=None, description="Path to TLS certificate")
    tls_key: str | None = Field(default=None, description="Path to TLS private key")
    tls_ca: str | None = Field(default=None, description="Path to TLS CA certificate")
    tls_verify: bool = Field(default=True, description="Verify TLS certificates")
```

**Priority**: 🟡 **HIGH** - Security concern
**Estimated Effort**: 4-6 hours

---

### 13. Event Loop Change Detection Edge Cases

**Location**: `server/database.py` lines 205-241

**Issue**: Complex logic for detecting event loop changes may miss edge cases.

**Impact**:

- asyncpg connections tied to specific event loops
- Using connections from wrong loop causes errors

**Fix**: Add more defensive checks and logging

**Priority**: 🟡 **HIGH** - Stability concern
**Estimated Effort**: 4-6 hours (testing edge cases)

---

### 14. Missing Transaction Rollback on Critical Failures

**Location**: `server/async_persistence.py` lines 403-461

**Issue**: `save_players()` continues loop on individual errors, but transaction may not rollback properly.

**Impact**:

- Partial failures may violate atomicity
- Some players saved, others not

**Fix**: Review error handling to ensure proper rollback

**Priority**: 🟡 **HIGH** - Data integrity
**Estimated Effort**: 4-6 hours

---

## 🟢 MEDIUM PRIORITY IMPROVEMENTS

### 15. Hardcoded Connection Pool Sizes

**Location**: `server/async_persistence.py` line 132

**Issue**: Pool sizes hardcoded instead of configurable.

**Fix**: Make configurable via config system

### Priority**: 🟢**MEDIUM

**Estimated Effort**: 2-3 hours

---

### 16. Deprecated asyncio.get_event_loop() Usage

**Location**:

- `server/services/nats_service.py` line 827
- `server/npc/lifecycle_manager.py` line 476

**Issue**: `asyncio.get_event_loop()` deprecated in Python 3.10+

**Fix**: Use `asyncio.get_running_loop()` instead

### Priority**: 🟢**MEDIUM

**Estimated Effort**: 1-2 hours

---

### 17. Inconsistent Error Handling Patterns

**Location**: Multiple files

**Issue**: Some methods return False on error, others raise exceptions.

**Fix**: Standardize on exception-based error handling

### Priority**: 🟢**MEDIUM

**Estimated Effort**: 8-12 hours

---

### 18. Memory Leak Risk in Metrics Collection

**Location**: `server/services/nats_service.py` lines 45-47

**Issue**: List slicing for metrics creates new objects frequently.

**Fix**: Use `collections.deque` with `maxlen` for automatic rotation

### Priority**: 🟢**MEDIUM

**Estimated Effort**: 1-2 hours

---

### 19. Missing Message Acknowledgment in NATS

**Location**: `server/services/nats_service.py` lines 410-433

**Issue**: No explicit message acknowledgment for reliability.

**Fix**: Add `msg.ack()` after successful processing

### Priority**: 🟢**MEDIUM

**Estimated Effort**: 3-4 hours

---

### 20. Subject Naming Inconsistency

**Location**: `server/realtime/nats_message_handler.py` lines 257-268

**Issue**: Mixed subject patterns (wildcards vs specific).

**Fix**: Complete migration to `NATSSubjectManager` patterns

### Priority**: 🟢**MEDIUM

**Estimated Effort**: 4-6 hours

---

### 21. No Connection Health Monitoring

**Location**: `server/services/nats_service.py` lines 519-526

**Issue**: `is_connected()` doesn't verify connection is actually healthy.

**Fix**: Add periodic health checks (ping/pong)

### Priority**: 🟢**MEDIUM

**Estimated Effort**: 4-6 hours

---

## ✅ POSITIVE FINDINGS

### 1. Excellent Error Boundary Implementation

**Location**: `server/realtime/` directory

**Finding**: Exemplary implementation of:

- `NATSRetryHandler`: Exponential backoff with jitter
- `CircuitBreaker`: Three-state pattern with proper transitions
- `DeadLetterQueue`: File-based storage with metadata

**Impact**: Robust error handling prevents cascading failures

---

### 2. Proper Use of asyncio.gather with return_exceptions=True

**Location**: `server/events/event_bus.py` lines 298-324

**Finding**: Structured concurrency pattern ensures all tasks complete even if some fail.

**Code**:

```python
results = await asyncio.gather(*tasks, return_exceptions=True)
# Log any exceptions from subscribers

for task, result in zip(tasks, results, strict=False):
    if isinstance(result, Exception):
        self._logger.error("Error in async subscriber", ...)
```

**Impact**: Prevents one failing subscriber from canceling others

---

### 3. Task Tracking and Lifecycle Management

**Location**:

- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`

**Finding**: Comprehensive task tracking prevents orphaned tasks and resource leaks.

**Impact**: Proper cleanup during shutdown

---

### 4. Good Connection State Management

**Location**: `server/realtime/connection_state_machine.py`

**Finding**: Robust state tracking with circuit breaker integration.

**Impact**: Prevents invalid state transitions

---

### 5. Proper Async Context Managers

**Location**: `server/async_persistence.py` throughout

**Finding**: Consistent use of `async with pool.acquire()` for connections.

**Impact**: Ensures proper resource cleanup

---

### 6. Enhanced Structured Logging

**Location**: `server/logging/enhanced_logging_config.py`

**Finding**: MDC, correlation IDs, security sanitization, performance monitoring.

**Impact**: Excellent observability (when not using f-strings!)

---

## 📋 REMEDIATION PLAN

### Phase 1: Critical Fixes (Week 1) - BLOCKING ISSUES

**Goal**: Eliminate event loop blocking and critical resource leaks

#### Task 1.1: Fix Synchronous Blocking in Passive Lucidity Flux Service

**Issue**: #1 - Synchronous blocking operations

**Files**: `server/services/passive_lucidity_flux_service.py`

**Actions**:

  1. Replace `self._persistence.get_room()` with `await self._persistence.async_get_room()`

  2. Add room caching (combines with #7)

  3. Test performance improvements

**Success Criteria**: Tick processing < 1 second

**Estimated Effort**: 8 hours

- **Owner**: TBD

#### Task 1.2: Eliminate asyncio.run() from Library Code

**Issue**: #2 - asyncio.run() in event loop context

**Files**: `server/services/exploration_service.py`

**Actions**:

  1. Remove `asyncio.run()` fallback

  2. Make calling code fully async

  3. Test edge cases

**Success Criteria**: No `asyncio.run()` in library code

**Estimated Effort**: 4 hours

- **Owner**: TBD

#### Task 1.3: Ensure Connection Pool Cleanup

**Issue**: #3 - Connection pool resource leaks

**Files**: `server/app/container.py`, `server/async_persistence.py`

**Actions**:

  1. Verify `container.shutdown()` calls `async_persistence.close()`

  2. Add tests for pool closure

  3. Test shutdown scenarios

**Success Criteria**: All pools closed during shutdown

**Estimated Effort**: 4 hours

- **Owner**: TBD

#### Task 1.4: Add Exception Handling to Pool Creation

**Issue**: #4 - Missing exception handling

**Files**: `server/async_persistence.py`

**Actions**:

  1. Wrap `create_pool()` in try-except

  2. Add proper error context

  3. Test connection failure scenarios

**Success Criteria**: Graceful handling of connection failures

**Estimated Effort**: 3 hours

- **Owner**: TBD

#### Task 1.5: Fix Blocking Operations in NATS Message Handlers

**Issue**: #5 - Synchronous database operations

**Files**: `server/realtime/nats_message_handler.py`

**Actions**:

  1. Implement mute data caching with TTL

  2. Replace sync calls with async/cached versions

  3. Benchmark message processing time

**Success Criteria**: Message processing < 100ms

**Estimated Effort**: 6 hours

- **Owner**: TBD

#### Task 1.6: Audit and Fix F-String Logging

**Issue**: #6 - Destroys structured logging

**Files**: Entire codebase

**Actions**:

  1. Search for `logger.(debug|info|warning|error|critical)(f"`

  2. Replace with structured key-value pairs

  3. Update coding standards documentation

  4. Add pre-commit hook to prevent f-string logging

**Success Criteria**: Zero f-string logging calls

**Estimated Effort**: 24 hours (widespread)

- **Owner**: TBD

**Phase 1 Total Effort**: ~49 hours (~1.25 weeks for 1 person)

---

### Phase 2: High Priority Fixes (Week 2-3) - PERFORMANCE

**Goal**: Optimize performance and complete async migration

#### Task 2.1: Add Room Lookup Caching

**Issue**: #7 - Missing caching

**Actions**: Implement room cache with TTL

**Estimated Effort**: 4 hours

#### Task 2.2: Complete Async Persistence Migration

**Issue**: #8 - Incomplete migration

**Actions**: Audit and migrate all async functions

**Estimated Effort**: 40 hours

#### Task 2.3: Optimize Database Flush Operations

**Issue**: #9 - Multiple flushes

**Actions**: Batch adjustments, flush once

**Estimated Effort**: 6 hours

#### Task 2.4: Load Only Active Players

**Issue**: #10 - Loading all players

**Actions**: Filter by active/online status

**Estimated Effort**: 3 hours

#### Task 2.5: Use NATS Connection Pool by Default

**Issue**: #11 - Pool not used

**Actions**: Make publish() use pool

**Estimated Effort**: 3 hours

#### Task 2.6: Add TLS Configuration

**Issue**: #12 - No TLS

**Actions**: Add TLS config fields

**Estimated Effort**: 6 hours

#### Task 2.7: Improve Event Loop Change Detection

**Issue**: #13 - Edge cases

**Actions**: Add defensive checks

**Estimated Effort**: 6 hours

#### Task 2.8: Review Transaction Error Handling

**Issue**: #14 - Rollback issues

**Actions**: Ensure proper rollback

**Estimated Effort**: 6 hours

**Phase 2 Total Effort**: ~74 hours (~2 weeks for 1 person)

---

### Phase 3: Medium Priority Improvements (Week 4) - POLISH

**Goal**: Address remaining issues and improve code quality

#### Tasks 3.1-3.7: Medium Priority Fixes

Configurable pool sizes

- Fix deprecated get_event_loop()
- Standardize error handling
- Optimize metrics collection
- Add message acknowledgment
- Fix subject naming
- Add connection health monitoring

**Phase 3 Total Effort**: ~30 hours (~1 week for 1 person)

---

## 📊 METRICS AND SUCCESS CRITERIA

### Performance Metrics

| Metric                      | Current   | Target      | Critical |
| --------------------------- | --------- | ----------- | -------- |
| Passive Lucidity Flux Tick  | 17.4s     | <1s         | ✅        |
| NATS Message Processing     | Unknown   | <100ms      | ✅        |
| Event Loop Blocking         | Confirmed | 0 instances | ✅        |
| Room Lookup Cache Hit Rate  | 0%        | >80%        | 🟡        |
| Connection Pool Utilization | 0%        | >50%        | 🟡        |

### Code Quality Metrics

| Metric                        | Current | Target |
| ----------------------------- | ------- | ------ |
| F-String Logging Instances    | Unknown | 0      |
| Sync Calls from Async         | Many    | 0      |
| asyncio.run() in Library Code | 2+      | 0      |
| Uncaught Pool Exceptions      | Yes     | No     |

### Test Coverage

| Area                      | Current | Target    |
| ------------------------- | ------- | --------- |
| Async Operations          | ~75%    | >90%      |
| Connection Pool Lifecycle | Unknown | 100%      |
| Event Loop Handling       | Partial | 100%      |
| NATS Error Boundaries     | Good    | Excellent |

---

## 🔍 TESTING STRATEGY

### Phase 1 Testing (Critical)

1. **Performance Testing**:

   - Measure passive lucidity flux tick time (target: <1s)
   - Measure NATS message processing time (target: <100ms)
   - Run load tests with 10+ concurrent players

2. **Resource Leak Testing**:

   - Start/stop server 100 times, verify no connection leaks
   - Monitor database connection count during operation
   - Check for orphaned tasks after shutdown

3. **Exception Handling Testing**:

   - Simulate database connection failures
   - Test graceful degradation
   - Verify error messages and logging

### Phase 2 Testing (Performance)

1. **Caching Testing**:

   - Verify cache hit rates >80%
   - Test cache invalidation
   - Test concurrent cache access

2. **Async Migration Testing**:

   - Verify no blocking operations remain
   - Test all async paths end-to-end
   - Benchmark performance improvements

3. **Transaction Testing**:

   - Test rollback on errors
   - Test partial failure scenarios
   - Verify data integrity

### Phase 3 Testing (Polish)

1. **Configuration Testing**:

   - Test pool size configurations
   - Test TLS connections
   - Test connection health monitoring

2. **Error Handling Testing**:

   - Test consistent error patterns
   - Test message acknowledgment
   - Test subject name resolution

---

## 📚 REFERENCES AND RESOURCES

### Best Practice Documents

1. `.cursor/rules/anyio.mdc` - AnyIO structured concurrency patterns
2. `.cursor/rules/asyncio.mdc` - asyncio best practices
3. `docs/STRUCTURED_CONCURRENCY_PATTERNS.md` - Project patterns
4. `docs/ASYNCIO_CODE_REVIEW.md` - Previous async review
5. `docs/NATS_CODE_REVIEW.md` - Previous NATS review

### External Resources

1. [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
2. [asyncpg Documentation](https://magicstack.github.io/asyncpg/)
3. [NATS Python Client](https://github.com/nats-io/nats.py)
4. [AnyIO Documentation](https://anyio.readthedocs.io/)

### Investigation Reports

1. `investigations/sessions/2025-11-30_session-001_passive-sanity-flux-performance.md`

---

## 🎯 RISK ASSESSMENT

### Blocking Risks

| Risk                                                   | Probability | Impact   | Mitigation                     |
| ------------------------------------------------------ | ----------- | -------- | ------------------------------ |
| Performance degradation prevents production deployment | High        | Critical | Phase 1 must complete first    |
| Connection leaks cause database outages                | Medium      | Critical | Phase 1 Task 1.3               |
| Event loop blocking causes user-visible lag            | High        | High     | Phase 1 Task 1.1               |
| Async migration introduces bugs                        | Medium      | High     | Comprehensive testing strategy |

### Non-Blocking Risks

| Risk                                          | Probability | Impact | Mitigation                  |
| --------------------------------------------- | ----------- | ------ | --------------------------- |
| Cache implementation introduces stale data    | Low         | Medium | TTL + invalidation strategy |
| TLS configuration breaks existing deployments | Low         | Medium | Backward compatibility      |
| Error handling changes break error reporting  | Low         | Low    | Preserve error context      |

---

## 🚀 DEPLOYMENT STRATEGY

### Pre-Deployment Checklist

[ ] All Phase 1 tasks complete

- [ ] Performance tests pass (<1s tick time)
- [ ] No connection leaks detected
- [ ] No event loop blocking detected
- [ ] All tests pass (including new async tests)
- [ ] Code review complete
- [ ] Documentation updated

### Rollback Plan

1. **Database**: No schema changes, safe to rollback
2. **Code**: Git revert to previous commit
3. **Configuration**: Restore previous config files
4. **Monitoring**: Watch for performance regressions

### Monitoring Post-Deployment

1. **Key Metrics**:

   - Game tick processing time
   - NATS message queue depth
   - Database connection count
   - Error rates

2. **Alerts**:

   - Tick time >2s (warning), >5s (critical)
   - Database connections >80% of max (warning)
   - Event loop blocking detected (critical)

---

## 📞 ESCALATION MATRIX

| Severity                    | Owner     | Escalation Time | Escalation To       |
| --------------------------- | --------- | --------------- | ------------------- |
| Critical (Production Down)  | On-Call   | Immediate       | Professor Wolfshade |
| High (Performance Degraded) | Team Lead | 30 minutes      | Technical Lead      |
| Medium (Non-Blocking Issue) | Developer | 4 hours         | Team Lead           |
| Low (Improvement)           | Developer | Next Sprint     | Backlog             |

---

## ✍️ AUDIT CONCLUSION

Professor Wolfshade,

This audit reveals a codebase with **strong architectural foundations** (structured concurrency, error boundaries, task
tracking) but **critical execution issues** (blocking operations, resource leaks). The progressive performance
degradation (17.4 second tick delays) is a clear indicator of synchronous blocking in async contexts.

**Immediate Action Required**:

1. Phase 1 tasks block production deployment
2. Estimated 1-2 weeks to resolve critical issues
3. Full remediation: 4-5 weeks total effort

**Positive Assessment**:

- Error boundary implementation is exemplary
- Task tracking prevents most resource leaks
- Structured logging (when not using f-strings) is excellent
- Team understands async patterns, just needs consistent application

**Recommendation**: Prioritize Phase 1 (critical fixes) before any new feature work. The performance issues will only
worsen with more users.

### adjusts spectacles grimly

As the Pnakotic Manuscripts warn: "That which blocks the flow of time shall bring madness to all who wait." Our event
loop blocking is indeed bringing madness in the form of 17-second delays.

---

### Audit Status**: ✅**COMPLETE

**Next Steps**: Review with Professor Wolfshade, assign ownership, begin Phase 1

**Date**: December 3, 2025
**Auditor**: AI Assistant (Untenured Professor of Occult Studies, Miskatonic University)
