# Caching Lru Cache

> 26 nodes · cohesion 0.08

## Key Concepts

- **test_lru_cache.py** (14 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **cache_with_ttl()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **cache_without_ttl()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expiration_check_only_when_ttl_enabled()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expiration_performance_impact()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expiration_rate_calculated()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expired_count_tracked_in_stats()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expired_entries_not_counted_in_evictions()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_expired_entries_removed_efficiently()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_mixed_expired_and_valid_entries()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_put_expired_entries_removed_before_capacity_check()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_put_expired_entries_removed_before_lru_eviction()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **test_cache_size_stays_within_bounds_after_expiration()** (2 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **Unit tests for LRU cache expiration and eviction.  Tests the LRUCache class, foc** (1 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **Test that expired entry count is tracked in cache stats.** (1 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **Test that expiration rate is calculated in stats.** (1 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **Test that cache size stays within bounds after expiration cleanup.** (1 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **Test that expiration checking doesn't significantly impact performance.** (1 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **Create an LRUCache with TTL enabled.** (1 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **Test that expired entries are removed efficiently in bulk.** (1 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **Test cache behavior with mix of expired and valid entries.** (1 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **Create an LRUCache without TTL.** (1 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **Test that expired entries are removed before LRU eviction.** (1 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **Test that expired entries are removed before checking if cache is full.** (1 connections) — `server/tests/unit/caching/test_lru_cache.py`
- **Test that expired entries are not counted as LRU evictions.** (1 connections) — `server/tests/unit/caching/test_lru_cache.py`
- *... and 1 more nodes in this community*

## Relationships

- [[LRU Cache Manager]] (1 shared connections)

## Source Files

- `server/tests/unit/caching/test_lru_cache.py`

## Audit Trail

- EXTRACTED: 51 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
