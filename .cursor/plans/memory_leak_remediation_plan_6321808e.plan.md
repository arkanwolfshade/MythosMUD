---
name: Memory Leak Remediation Plan
overview: Comprehensive plan to remediate all memory leak findings identified in the audit report, including fixes for unbounded set growth, event subscriber cleanup, cache expiration handling, and monitoring implementation.
todos:
  - id: task1-1
    content: Replace _closed_websockets set with collections.deque(maxlen=1000) in ConnectionManager.__init__()
    status: completed
  - id: task1-2
    content: Update mark_websocket_closed() to use deque.append() instead of set.add()
    status: completed
  - id: task1-3
    content: Update is_websocket_closed() to check membership in deque (O(n) but acceptable with maxlen=1000)
    status: completed
  - id: task1-4
    content: Add import for collections.deque at top of connection_manager.py
    status: completed
  - id: task1-5
    content: Write unit test to verify closed websocket tracking works with deque
    status: completed
  - id: task1-6
    content: Write integration test with 10,000+ connection cycles to verify bounded growth
    status: completed
  - id: task2-1
    content: Add _subscriber_tracking dict to EventBus.__init__() to track subscribers by service
    status: completed
  - id: task2-2
    content: Update EventBus.subscribe() to optionally accept service_id parameter for tracking
    status: completed
  - id: task2-3
    content: "Implement unsubscribe_all_for_service(service_id: str) method in EventBus"
    status: completed
  - id: task2-4
    content: Add get_subscriber_stats() method to EventBus for monitoring subscriber counts
    status: completed
  - id: task2-5
    content: Review server/app/lifespan_shutdown.py to identify shutdown hook integration point
    status: completed
  - id: task2-6
    content: Add EventBus cleanup call in shutdown lifecycle before service destruction
    status: completed
  - id: task2-7
    content: Add logging of subscriber counts on shutdown for verification
    status: completed
  - id: task2-8
    content: Document service cleanup pattern for event subscriptions
    status: completed
  - id: task2-9
    content: Write unit test to verify subscribers are removed on service shutdown
    status: completed
  - id: task2-10
    content: Write integration test with multiple services subscribing to same events
    status: completed
  - id: task3-1
    content: Add _evict_expired_entries() helper method to LRUCache class
    status: completed
  - id: task3-2
    content: Implement expiration check logic in _evict_expired_entries() (iterate cache, check TTL, remove expired)
    status: completed
  - id: task3-3
    content: Update LRUCache.put() to call _evict_expired_entries() before checking cache capacity
    status: completed
  - id: task3-4
    content: Ensure LRU eviction only happens if cache still full after removing expired entries
    status: completed
  - id: task3-5
    content: Add optimization to only check expiration if ttl_seconds is not None
    status: completed
  - id: task3-6
    content: Consider limiting expiration check to when cache is 90% full for performance
    status: completed
  - id: task3-7
    content: Track count of expired entries evicted in _evict_expired_entries()
    status: completed
  - id: task3-8
    content: Add expired entry count to LRUCache.get_stats() return value
    status: completed
  - id: task3-9
    content: Write unit test with TTL-enabled cache to verify expired entries removed before LRU eviction
    status: completed
  - id: task3-10
    content: Write performance test to measure impact of expiration checking
    status: completed
  - id: task3-11
    content: Verify cache size stays within bounds after expiration cleanup
    status: completed
  - id: task4-1
    content: Audit all places where nats_service.subscribe() is called in codebase
    status: completed
  - id: task4-2
    content: Document subscription lifecycle for each service that creates NATS subscriptions
    status: completed
  - id: task4-3
    content: Verify NATSService.disconnect() properly unsubscribes all subscriptions
    status: completed
  - id: task4-4
    content: Verify NATSMessageHandler cleanup on shutdown removes all subscriptions
    status: completed
  - id: task4-5
    content: Add get_active_subscriptions() method to NATSService returning list of active subscription subjects
    status: completed
  - id: task4-6
    content: Add logging in NATSService.disconnect() to log active subscriptions before cleanup
    status: completed
  - id: task4-7
    content: Add warning log if subscriptions remain after cleanup in disconnect()
    status: completed
  - id: task4-8
    content: Verify NATS service cleanup is called in shutdown lifecycle
    status: completed
  - id: task4-9
    content: "Ensure cleanup order: unsubscribe subscriptions, then disconnect connection"
    status: completed
  - id: task4-10
    content: Write test to verify all subscriptions removed on service shutdown
    status: completed
  - id: task4-11
    content: Write test to verify service restart doesn't create duplicate subscriptions
    status: completed
  - id: task5-1
    content: Audit all components using Zustand stores (connectionStore, gameStore)
    status: completed
  - id: task5-2
    content: Verify all components have useEffect cleanup functions that unsubscribe from stores
    status: completed
  - id: task5-3
    content: Identify components that subscribe but don't unsubscribe
    status: completed
  - id: task5-4
    content: Review event history arrays in stores for size limits
    status: completed
  - id: task5-5
    content: Review message arrays in stores for unbounded growth
    status: completed
  - id: task5-6
    content: Implement max size limits for event history arrays if missing
    status: completed
  - id: task5-7
    content: Add trimming logic to keep arrays bounded (remove oldest entries when limit reached)
    status: completed
  - id: task5-8
    content: Consider using circular buffers for fixed-size history if appropriate
    status: completed
  - id: task5-9
    content: Document cleanup patterns for store subscriptions in code comments
    status: completed
  - id: task5-10
    content: Write test to verify component unmount cleans up store subscriptions
    status: completed
  - id: task5-11
    content: Write test to verify arrays don't grow unbounded with long-running sessions
    status: completed
  - id: task6-1
    content: Create new file server/monitoring/memory_leak_monitor.py
    status: completed
  - id: task6-2
    content: Implement MemoryLeakMonitor class with methods to query metrics from ConnectionManager
    status: completed
  - id: task6-3
    content: Add method to query EventBus subscriber counts per event type
    status: completed
  - id: task6-4
    content: Add method to query cache sizes and expiration rates from CacheManager
    status: completed
  - id: task6-5
    content: Add method to query TaskRegistry active task counts
    status: completed
  - id: task6-6
    content: Add method to query connection manager dict sizes
    status: completed
  - id: task6-7
    content: Implement periodic logging task (every 5-10 minutes) using TaskRegistry
    status: completed
  - id: task6-8
    content: Add alerting threshold for _closed_websockets (warn if exceeds 5000 entries)
    status: completed
  - id: task6-9
    content: Add alerting threshold for subscriber count growth (warn if grows unexpectedly)
    status: completed
  - id: task6-10
    content: Add alerting threshold for cache sizes (warn if exceeds expected bounds)
    status: completed
  - id: task6-11
    content: Integrate memory leak metrics into server/api/metrics.py if it exists
    status: completed
  - id: task6-12
    content: Add memory leak metrics to connection statistics endpoints
    status: completed
  - id: task6-13
    content: Write unit tests to verify metrics are accurate
    status: completed
  - id: task6-14
    content: Write test to verify alerting thresholds trigger correctly
    status: completed
  - id: task6-15
    content: Verify metrics collection doesn't impact performance
    status: completed
---

# Memory Leak Remediation Plan

## Overview

This plan addresses all findings from the memory leak audit report, prioritizing medium-risk issues first, followed by low-risk verification tasks and monitoring improvements.

## Remediation Tasks

### Task 1: Fix `_closed_websockets` Unbounded Growth (Finding 1.2.1)

**Priority**: Medium

**File**: `server/realtime/connection_manager.py`

**Implementation Approach**: Replace unbounded set with a bounded structure that automatically evicts old entries.

**Steps**:

1. **Replace set with bounded tracking structure**

   - Change `_closed_websockets: set[int]` to use a time-based bounded structure
   - Options:
     - Use `collections.deque` with maxlen to keep only recent N entries
     - Use a dict mapping `ws_id -> timestamp` and periodically clean old entries
     - Use LRU cache with small max_size (e.g., 1000 entries)
   - **Recommended**: Use `collections.deque` with `maxlen=1000` for simplicity and automatic eviction

2. **Update `mark_websocket_closed()` method**

   - Modify to append to deque instead of adding to set
   - Ensure thread-safety if needed (ConnectionManager may be accessed from multiple threads)

3. **Update `is_websocket_closed()` method**

   - Change from `ws_id in self._closed_websockets` to checking deque membership
   - Note: `deque` membership check is O(n), but with maxlen=1000 this is acceptable

4. **Add periodic cleanup (alternative approach)**

   - If using dict with timestamps, add cleanup method called during connection cleanup cycles
   - Remove entries older than 1 hour

**Code Changes**:

- Line 236: Change `self._closed_websockets: set[int] = set()` to `self._closed_websockets: deque[int] = deque(maxlen=1000)`
- Update `mark_websocket_closed()` to use `append()` instead of `add()`
- Update `is_websocket_closed()` to use `in` operator (works with deque)

**Testing**:

- Verify closed websocket tracking still works correctly
- Verify memory doesn't grow unbounded with many connections
- Test with 10,000+ connection cycles

---

### Task 2: Implement Event Subscriber Cleanup (Finding 2.1.1)

**Priority**: Medium

**File**: `server/events/event_bus.py`

**Implementation Approach**: Add subscriber tracking and automatic cleanup on service shutdown.

**Steps**:

1. **Add subscriber tracking with weak references**

   - Create a new dict to track subscribers by service/component identifier
   - Use `weakref.WeakSet` or `weakref.WeakKeyDictionary` where appropriate
   - Track which services/components have subscribed to which events

2. **Implement `unsubscribe_all_for_service()` method**

   - Add method to EventBus to unsubscribe all handlers for a specific service
   - Accept service identifier or weak reference to service object
   - Remove all subscribers registered by that service

3. **Add shutdown hook integration**

   - Integrate with application shutdown lifecycle in `server/app/lifespan_shutdown.py`
   - Call cleanup for all services during shutdown
   - Ensure EventBus cleanup happens before service destruction

4. **Add monitoring method**

   - Add `get_subscriber_stats()` method to track subscriber counts per event type
   - Log subscriber counts periodically or on shutdown

5. **Update service initialization patterns**

   - Document pattern: services should register cleanup callbacks
   - Consider adding context manager pattern for event subscriptions

**Code Changes**:

- Add `_subscriber_tracking: dict[str, list[tuple[type[BaseEvent], Callable]]]` to track subscribers by service
- Add `unsubscribe_all_for_service(service_id: str)` method
- Add `get_subscriber_stats()` method for monitoring
- Update `subscribe()` to optionally accept `service_id` parameter for tracking
- Add cleanup call in shutdown lifecycle

**Testing**:

- Verify subscribers are removed on service shutdown
- Verify no memory leaks when services are recreated
- Test with multiple services subscribing to same events

---

### Task 3: Proactively Clean Expired Cache Entries (Finding 4.1.1)

**Priority**: Medium

**File**: `server/caching/lru_cache.py`

**Implementation Approach**: Check for expired entries before evicting LRU items in `put()` method.

**Steps**:

1. **Add `_evict_expired_entries()` helper method**

   - Iterate through cache entries
   - Check TTL expiration for each entry
   - Remove expired entries
   - Return count of expired entries removed

2. **Update `put()` method**

   - Before checking if cache is full, call `_evict_expired_entries()`
   - Only evict LRU item if cache is still full after removing expired entries
   - This ensures expired entries are removed first, preserving valid entries

3. **Optimize expiration check**

   - Only check expiration if `ttl_seconds` is not None
   - Use efficient iteration (OrderedDict supports iteration)
   - Consider limiting expiration check to when cache is near capacity (e.g., 90% full) for performance

4. **Add expiration statistics**

   - Track count of expired entries evicted
   - Add to cache stats for monitoring

**Code Changes**:

- Add `_evict_expired_entries() -> int` method (lines ~108-120)
- Modify `put()` method to call `_evict_expired_entries()` before LRU eviction (line ~99)
- Update cache stats to include expired entry counts

**Code Structure**:

```python
def _evict_expired_entries(self) -> int:
    """Remove expired entries from cache. Returns count of removed entries."""
    if self.ttl_seconds is None:
        return 0
    # Implementation

def put(self, key: K, value: V) -> None:
    with self._lock:
        current_time = time.time()
        # ... existing update logic ...

        # Evict expired entries before checking capacity
        expired_count = self._evict_expired_entries()

        # If cache is still full after removing expired entries, evict LRU
        if len(self._cache) >= self.max_size:
            # ... existing LRU eviction ...
```

**Testing**:

- Test with TTL-enabled cache (player data cache)
- Verify expired entries are removed before LRU eviction
- Test performance impact of expiration checking
- Verify cache size stays within bounds

---

### Task 4: Verify NATS Subscription Cleanup (Finding 1.3)

**Priority**: Low

**Files**: `server/services/nats_service.py`, `server/realtime/nats_message_handler.py`

**Implementation Approach**: Audit and ensure all NATS subscriptions are properly cleaned up.

**Steps**:

1. **Audit NATS subscription points**

   - Review all places where `nats_service.subscribe()` is called
   - Identify services that create subscriptions
   - Document subscription lifecycle for each service

2. **Verify shutdown cleanup**

   - Check that `NATSService.disconnect()` properly unsubscribes all subscriptions
   - Verify `NATSMessageHandler` cleanup on shutdown
   - Ensure subscriptions dict is cleared

3. **Add subscription tracking**

   - Add method to list all active subscriptions
   - Log active subscriptions on shutdown
   - Add assertion/warning if subscriptions remain after cleanup

4. **Update service shutdown**

   - Ensure NATS service cleanup is called in shutdown lifecycle
   - Verify order: unsubscribe subscriptions, then disconnect connection

**Code Changes**:

- Add `get_active_subscriptions()` method to NATSService
- Add logging in `disconnect()` to verify all subscriptions removed
- Add cleanup verification in shutdown lifecycle

**Testing**:

- Verify all subscriptions are removed on service shutdown
- Test service restart doesn't create duplicate subscriptions
- Monitor subscription count over time

---

### Task 5: Verify Zustand Store Cleanup (Finding 5.2)

**Priority**: Low

**Files**: `client/src/stores/connectionStore.ts`, `client/src/stores/gameStore.ts`

**Implementation Approach**: Audit client-side store usage and verify cleanup patterns.

**Steps**:

1. **Audit store subscriptions**

   - Review all components using Zustand stores
   - Verify `useEffect` cleanup functions unsubscribe from stores
   - Check for components that subscribe but don't unsubscribe

2. **Check array growth**

   - Review event history arrays in stores
   - Verify size limits or trimming mechanisms
   - Check message arrays for unbounded growth

3. **Add size limits if needed**

   - Implement max size for event history arrays
   - Add trimming logic to keep arrays bounded
   - Consider using circular buffers for fixed-size history

4. **Document cleanup patterns**

   - Create guidelines for store subscription cleanup
   - Add examples in code comments

**Code Changes**:

- Review and update store implementations if needed
- Add size limits to history arrays
- Add cleanup verification in component unmount

**Testing**:

- Test component unmount cleans up store subscriptions
- Verify arrays don't grow unbounded
- Test with long-running sessions

---

### Task 6: Add Memory Leak Monitoring

**Priority**: Low (but important for ongoing detection)

**Files**: Multiple - create new monitoring module

**Implementation Approach**: Add metrics and logging for memory leak detection.

**Steps**:

1. **Create memory monitoring module**

   - New file: `server/monitoring/memory_monitor.py`
   - Track key metrics:
     - `_closed_websockets` size
     - EventBus subscriber counts per event type
     - Cache sizes and expiration rates
     - TaskRegistry active task counts
     - Connection manager dict sizes

2. **Add periodic logging**

   - Log memory metrics every 5-10 minutes
   - Include in health check endpoints
   - Add to metrics API

3. **Add alerting thresholds**

   - Warn if `_closed_websockets` exceeds 5000 entries
   - Warn if subscriber counts grow unexpectedly
   - Warn if cache sizes exceed expected bounds

4. **Integrate with existing metrics**

   - Add to `server/api/metrics.py` if exists
   - Include in connection statistics endpoints

**Code Changes**:

- Create `server/monitoring/memory_monitor.py`
- Add methods to query metrics from ConnectionManager, EventBus, CacheManager, TaskRegistry
- Add periodic logging task
- Integrate with metrics API

**Testing**:

- Verify metrics are accurate
- Test alerting thresholds
- Verify metrics don't impact performance

---

## Implementation Order

1. **Phase 1 (Critical)**: Tasks 1, 2, 3 (Medium-risk fixes)
2. **Phase 2 (Verification)**: Tasks 4, 5 (Low-risk verification)
3. **Phase 3 (Monitoring)**: Task 6 (Ongoing detection)

## Testing Strategy

For each fix:

1. Write unit tests for the specific fix
2. Add integration tests for resource cleanup
3. Run load tests to verify no memory growth over time
4. Monitor production metrics after deployment

## Success Criteria

- `_closed_websockets` set size remains bounded (< 1000 entries)
- Event subscribers are cleaned up on service shutdown
- Expired cache entries are removed proactively
- NATS subscriptions are verified to clean up properly
- Client-side stores have bounded growth
- Memory metrics are tracked and logged

## Notes

- All fixes should maintain backward compatibility
- Consider performance impact of expiration checks
- Monitoring should be lightweight to avoid overhead
- Document cleanup patterns for future development
