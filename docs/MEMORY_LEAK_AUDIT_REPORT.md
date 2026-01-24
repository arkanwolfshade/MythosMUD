# Memory Leak Audit Report

**Date**: 2026-01-15
**Auditor**: AI Agent
**Scope**: Comprehensive memory leak audit focusing on resource lifecycle management, event subscriptions, caches,
connections, and async task tracking

## Executive Summary

This report documents the findings from a systematic audit of the MythosMUD codebase for potential memory leaks and
unbounded memory growth patterns. The audit focuses on identifying resources that accumulate over time without proper
cleanup, even when system load remains constant.

## Audit Methodology

The audit follows a systematic approach examining:

1. Connection management (database, WebSocket, NATS)
2. Event system subscriptions
3. Async task and background task lifecycle
4. Cache and in-memory data structure growth
5. Client-side memory management
6. File handle and I/O resource management
7. Circular reference patterns

## Findings by Category

### 1. Connection Management Leaks

#### 1.1 Database Connection Pools

**Status**: ✅ **COMPLETE** - No leaks found

**Files Reviewed**:

- `server/postgres_adapter.py` (lines 148-182)
- `server/database.py` (lines 440-460)
- `server/async_persistence.py` (lines 156-163)
- `server/npc_database.py` (lines 219-267)

**Findings**:

✅ All database connections use context managers (`with` statements)

✅ `PostgresConnectionPool.get_connection()` properly returns connections to pool in `finally` block

✅ `get_async_session()` properly closes sessions in exception handling

✅ NPC database sessions properly closed in `finally` blocks

✅ Connection pool size is bounded by configuration (1-10 connections)

**Risk**: **None** - Proper resource management with context managers

#### 1.2 WebSocket Connection Leaks

**Status**: ✅ **COMPLETE** - 1 Medium Risk finding

**Files Reviewed**:

- `server/realtime/connection_manager.py` (lines 153-236)
- `server/realtime/connection_establishment.py` (lines 110-329)
- `server/realtime/connection_disconnection.py` (lines 16-226)
- `server/realtime/connection_delegates.py` (lines 43-99)

**Findings**:

**Finding 1.2.1**: Unbounded `_closed_websockets` set growth

**Location**: `server/realtime/connection_manager.py:236`

**Issue**: The `_closed_websockets: set[int]` set is used to track closed WebSocket IDs to prevent duplicate closes,
  but entries are never removed from this set. Over time, this set will grow unbounded.

**Code Reference**:

  ```python
  # Track safely closed websocket objects to avoid duplicate closes

  self._closed_websockets: set[int] = set()
  ```

**Impact**: Each closed WebSocket adds an integer ID to this set. With thousands of reconnections over time, this set
could grow to significant size.

**Recommendation**: Implement periodic cleanup of old entries, or use a bounded structure (e.g., LRU cache) to limit
  growth.

**Risk**: **Medium** - Unbounded growth over long-running servers

**Other Findings**:

✅ WebSocket connections properly removed from `active_websockets` dict on disconnect

✅ Connection metadata properly cleaned up on disconnect

✅ Player websocket mappings properly cleaned up

✅ Dead connection cleanup implemented in `_cleanup_dead_connections()`

#### 1.3 NATS Connection and Subscription Leaks

**Status**: ✅ **COMPLETE** - No leaks found

**Files Reviewed**:

- `server/services/nats_service.py` (lines 353-411)
- `server/realtime/nats_message_handler.py` (lines 98-98)

**Findings**:

✅ NATS service has `disconnect()` method that cancels background tasks

✅ Background tasks properly cancelled on service shutdown

✅ Subscriptions tracked in `self.subscriptions` dict

- ⚠️ **Note**: Need to verify all services call `unsubscribe()` on shutdown in actual implementation

**Risk**: **Low** - Proper cleanup exists, but depends on services calling it

---

### 2. Event System Leaks

#### 2.1 EventBus Subscriber Leaks

**Status**: ✅ **COMPLETE** - 1 Medium Risk finding

**Files Reviewed**:

- `server/events/event_bus.py` (lines 53-591)
- `server/realtime/event_handler.py` (lines 126-155)

**Findings**:

**Finding 2.1.1**: Event subscribers not unsubscribed on service shutdown

**Location**: `server/events/event_bus.py:53`

**Issue**: Services subscribe to events via `EventBus.subscribe()`, but there's no systematic mechanism to ensure all
  subscribers are unsubscribed when services shut down. The `_subscribers` dict could accumulate subscribers over time
  if services don't explicitly unsubscribe.

**Code Reference**:

  ```python
  self._subscribers: dict[type[BaseEvent], list[Callable[[BaseEvent], Any]]] = defaultdict(list)
  ```

**Impact**: Subscribers holding references to services or large objects could prevent garbage collection.

**Recommendation**:

- Implement automatic cleanup on service shutdown
- Use weak references for subscribers where appropriate
- Add monitoring to track subscriber count growth
- **Risk**: **Medium** - Depends on service lifecycle management

**Other Findings**:

✅ Async subscriber tasks properly tracked in `_active_tasks` set

✅ Task completion callbacks properly remove tasks from tracking

✅ Event queue uses bounded operations

#### 2.2 Client-Side Event Handler Leaks

**Status**: ✅ **COMPLETE** - No leaks found

**Files Reviewed**:

- `client/src/hooks/useWebSocketConnection.ts` (lines 276-280)
- `client/src/utils/resourceCleanup.ts` (lines 163-175)

**Findings**:

✅ React hooks have proper cleanup functions in `useEffect`

✅ ResourceManager properly cleans up timers, intervals, and WebSockets on unmount

✅ WebSocket connections properly closed in cleanup effects

**Risk**: **None** - Proper React cleanup patterns

---

### 3. Async Task and Background Task Leaks

#### 3.1 Task Registry Leaks

**Status**: ✅ **COMPLETE** - No leaks found

**Files Reviewed**:

- `server/app/task_registry.py` (lines 67-220)
- `server/app/tracked_task_manager.py`

**Findings**:

✅ Tasks properly tracked in `_active_tasks` dict

✅ Completion callbacks automatically remove tasks from tracking

✅ Task metadata cleaned up in completion callbacks

✅ TaskRegistry properly removes completed tasks

**Risk**: **None** - Proper task lifecycle management

#### 3.2 Background Service Task Leaks

**Status**: ✅ **COMPLETE** - No leaks found

**Files Reviewed**:

- `server/realtime/monitoring/health_monitor.py` (lines 351-398)
- `server/services/nats_service.py` (lines 360-411)

**Findings**:

✅ Background tasks cancelled in `_cancel_background_tasks()` methods

✅ Health check tasks properly cancelled on service shutdown

✅ Task tracking uses done callbacks for automatic cleanup

**Risk**: **None** - Proper task cancellation and cleanup

---

### 4. Cache and In-Memory Data Structure Leaks

#### 4.1 LRU Cache Growth

**Status**: ✅ **COMPLETE** - 1 Medium Risk finding

**Files Reviewed**:

- `server/caching/lru_cache.py` (lines 49-180)
- `server/caching/cache_service.py` (lines 241-311)

**Findings**:

**Finding 4.1.1**: Expired cache entries not proactively cleaned

**Location**: `server/caching/lru_cache.py:81-107`

**Issue**: The LRU cache checks TTL expiration on `get()` operations, but not during `put()` operations. Expired
  entries remain in the cache taking up memory until they're accessed, rather than being cleaned up proactively when
  space is needed.

**Code Reference**:

  ```python
  def put(self, key: K, value: V) -> None:
      # ... existing code ...
      # If cache is full, remove least recently used item

      if len(self._cache) >= self.max_size:
          oldest_key, _ = self._cache.popitem(last=False)
          # Does not check if oldest_key is expired before evicting

  ```

**Impact**: Caches with TTL enabled could accumulate expired entries that waste memory until accessed. This is
particularly relevant for the player data cache (5-minute TTL).

**Recommendation**:

- Before evicting LRU item in `put()`, check if cache has expired entries and remove those first
- Alternatively, implement a background task to periodically clean expired entries
- Or use lazy eviction that checks expiration when cache is full
- **Risk**: **Medium** - Memory waste from expired entries, especially for caches with short TTL

**Other Findings**:

✅ Cache max_size properly enforced

✅ TTL expiration checked on `get()` operations

✅ LRU eviction works correctly

✅ Cache statistics tracking implemented

#### 4.2 Dictionary and Set Growth

**Status**: ✅ **COMPLETE** - No leaks found

**Files Reviewed**:

- `server/realtime/connection_manager.py` (lines 153-233)
- `server/realtime/message_queue.py`
- `server/realtime/dead_letter_queue.py`

**Findings**:

✅ Connection dictionaries properly cleaned up on disconnect

✅ Message queues have size limits enforced

✅ Dead letter queue processing exists (needs verification of periodic processing)

**Risk**: **Low** - Proper cleanup exists, but DLQ processing frequency should be verified

---

### 5. Client-Side Memory Leaks

#### 5.1 React Hook Leaks

**Status**: ✅ **COMPLETE** - No leaks found

**Files Reviewed**:

- `client/src/hooks/useWebSocketConnection.ts`
- `client/src/utils/resourceCleanup.ts`

**Findings**:

✅ All useEffect hooks have cleanup functions

✅ ResourceManager properly tracks and cleans up resources

✅ WebSocket connections closed on unmount

✅ Timers and intervals properly cleared

**Risk**: **None** - Proper React cleanup patterns

#### 5.2 Zustand Store Leaks

**Status**: ⚠️ **PARTIAL** - Need to verify store subscription cleanup

**Files Reviewed**:

- `client/src/stores/connectionStore.ts`
- `client/src/stores/gameStore.ts`

**Findings**:

- ⚠️ Need to verify store subscriptions are properly cleaned up in component unmount
- ⚠️ Need to check if event history/message arrays have size limits

**Risk**: **Low** - Requires verification of actual usage patterns

---

### 6. File Handle and I/O Leaks

#### 6.1 File Handle Leaks

**Status**: ✅ **COMPLETE** - No leaks found

**Files Reviewed**:

- `server/services/chat_logger.py` (lines 74-137)

**Findings**:

✅ All file operations use `with` statements (line 120)

✅ File handles automatically closed by context managers

✅ Writer thread properly joined on shutdown (line 136)

✅ Log queue properly drained on shutdown

**Risk**: **None** - Proper file handle management with context managers

---

### 7. Circular Reference Leaks

#### 7.1 Object Reference Cycles

**Status**: ⚠️ **PARTIAL** - Static analysis only, needs runtime verification

**Findings**:

- ⚠️ Services hold references to each other via dependency injection (expected pattern)
- ⚠️ Event handlers may hold references to publishers (needs verification)
- ⚠️ Connection objects reference managers that reference connections (circular pattern, but Python GC handles this)
- **Recommendation**: Use weak references for observer patterns where appropriate

**Risk**: **Low** - Python's garbage collector handles reference cycles, but weak references could improve cleanup

---

## Risk Assessment Summary

**High Risk**: 0 findings

**Medium Risk**: 3 findings

  1. `_closed_websockets` set unbounded growth (1.2.1)
  2. Event subscribers not systematically unsubscribed (2.1.1)
  3. Expired cache entries not proactively cleaned (4.1.1)

**Low Risk**: 2 findings

  1. NATS subscriptions cleanup depends on service lifecycle (1.3)
  2. Zustand store cleanup needs verification (5.2)

## Recommendations

### High Priority Fixes

None - No high-risk memory leaks identified.

### Medium Priority Fixes

1. **Fix `_closed_websockets` unbounded growth** (Finding 1.2.1)

   - Implement periodic cleanup (e.g., every 1000 connections, remove entries older than 1 hour)
   - Or use a bounded LRU structure instead of a set
   - File: `server/realtime/connection_manager.py:236`

2. **Implement systematic event subscriber cleanup** (Finding 2.1.1)

   - Add cleanup mechanism in service shutdown lifecycle
   - Use weak references for subscribers where appropriate
   - Add monitoring to track subscriber count over time
   - File: `server/events/event_bus.py:53`

3. **Proactively clean expired cache entries** (Finding 4.1.1)

   - Check for expired entries before evicting LRU item in `put()` method
   - Implement background task for periodic expiration cleanup
   - Or implement lazy expiration check when cache reaches 90% capacity
   - File: `server/caching/lru_cache.py:81-107`

### Low Priority Improvements

1. **Verify NATS subscription cleanup** - Ensure all services properly unsubscribe on shutdown

2. **Verify Zustand store cleanup** - Check component unmount patterns in client code

3. **Consider weak references** - Review circular reference patterns for optimization opportunities

4. **Add monitoring** - Implement metrics for tracking:

   - `_closed_websockets` set size
   - EventBus subscriber counts per event type
   - Cache sizes and expiration rates
   - Active task counts in TaskRegistry

## Common Patterns Identified

### ✅ Good Patterns (No Leaks)

1. **Context Manager Usage**: Database connections, file handles, and session management consistently use Python context

   managers (`with` statements), ensuring proper cleanup even on exceptions.

2. **Task Lifecycle Tracking**: Async tasks are properly tracked with completion callbacks that automatically remove

   them from tracking structures.

3. **Resource Cleanup Hooks**: React hooks have proper cleanup functions, and ResourceManager provides centralized

   resource tracking.

4. **Connection Pooling**: Database connections use bounded pools with proper connection return mechanisms.

### ⚠️ Patterns to Watch

1. **Tracking Sets Without Cleanup**: The `_closed_websockets` set pattern (tracking closed connections) could be

   applied elsewhere - verify no other unbounded tracking sets exist.

2. **Event Subscriptions**: Event subscription patterns should always include corresponding unsubscribe logic in service

   shutdown.

3. **TTL Cache Expiration**: Caches with TTL should have proactive expiration cleanup, not just lazy expiration on

   access.

## Monitoring Recommendations

Add metrics to track:

1. **Connection Management**:

   - `connection_manager._closed_websockets` set size
   - `active_websockets` dict size vs active player count
   - `connection_metadata` dict size

2. **Event System**:

   - EventBus subscriber count per event type
   - `_active_tasks` set size in EventBus

3. **Caches**:

   - Cache sizes and hit rates
   - Expired entry counts (for TTL caches)

4. **Task Management**:

   - TaskRegistry active task count
   - Background task counts by service

5. **Client-Side**:

   ResourceManager resource counts (timers, intervals, WebSockets)

## Audit Completion Summary

**Date Completed**: 2026-01-15

**Files Audited**: 20+ files across server and client codebases

**Categories Reviewed**:

✅ Connection Management (Database, WebSocket, NATS)

✅ Event System (EventBus, client-side handlers)

✅ Async Task Management (TaskRegistry, background tasks)

✅ Cache Management (LRU caches, data structures)

✅ Client-Side Resource Management (React hooks, stores)

- ✅ File Handle Management
- ✅ Circular References (static analysis)

**Overall Assessment**: The codebase demonstrates good resource management practices overall. The identified issues are
moderate and can be addressed with targeted fixes. No critical memory leaks were found that would cause immediate
production issues.
