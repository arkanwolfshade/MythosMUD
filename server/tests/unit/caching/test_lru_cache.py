"""
Unit tests for LRU cache expiration and eviction.

Tests the LRUCache class, focusing on expiration handling and proactive cleanup.
"""

import time

import pytest

from server.caching.lru_cache import LRUCache

# pylint: disable=redefined-outer-name  # Reason: pytest fixtures are used as function parameters, which triggers this warning


@pytest.fixture
def cache_with_ttl():
    """Create an LRUCache with TTL enabled."""
    return LRUCache[str, str](max_size=10, ttl_seconds=1)


@pytest.fixture
def cache_without_ttl():
    """Create an LRUCache without TTL."""
    return LRUCache[str, str](max_size=10, ttl_seconds=None)


def test_cache_put_expired_entries_removed_before_lru_eviction(cache_with_ttl):
    """Test that expired entries are removed before LRU eviction."""
    # Fill cache to capacity
    for i in range(10):
        cache_with_ttl.put(f"key{i}", f"value{i}")

    # Wait for entries to expire (TTL=1s; sleep well past to avoid CI timing flakiness)
    time.sleep(2.0)

    # Add new entry - should evict expired entries first, not LRU
    cache_with_ttl.put("new_key", "new_value")

    # All old entries should be expired and removed
    stats = cache_with_ttl.get_stats()
    assert stats["size"] == 1
    assert stats["expired_count"] >= 10  # All old entries expired
    assert cache_with_ttl.get("new_key") == "new_value"
    # Old entries should not be retrievable
    assert cache_with_ttl.get("key0") is None


def test_cache_put_expired_entries_removed_before_capacity_check(cache_with_ttl):
    """Test that expired entries are removed before checking if cache is full."""
    # Fill cache to capacity
    for i in range(10):
        cache_with_ttl.put(f"key{i}", f"value{i}")

    # Wait for entries to expire (TTL=1s; sleep well past to avoid CI timing flakiness)
    time.sleep(2.0)

    # Add multiple new entries - should fill cache with new entries
    for i in range(5):
        cache_with_ttl.put(f"new_key{i}", f"new_value{i}")

    stats = cache_with_ttl.get_stats()
    # All expired entries should be removed, new entries added
    assert stats["size"] == 5
    assert stats["expired_count"] >= 10  # All old entries expired
    # Verify new entries are present
    for i in range(5):
        assert cache_with_ttl.get(f"new_key{i}") == f"new_value{i}"


def test_cache_expired_entries_not_counted_in_evictions(cache_with_ttl):
    """Test that expired entries are not counted as LRU evictions."""
    # Fill cache to capacity
    for i in range(10):
        cache_with_ttl.put(f"key{i}", f"value{i}")

    initial_evictions = cache_with_ttl.get_stats()["evictions"]

    # Wait for entries to expire (TTL=1s; sleep well past to avoid CI timing flakiness)
    time.sleep(2.0)

    # Add new entry - should remove expired entries, not evict LRU
    cache_with_ttl.put("new_key", "new_value")

    stats = cache_with_ttl.get_stats()
    # Evictions should not increase (expired entries removed, not evicted)
    assert stats["evictions"] == initial_evictions
    assert stats["expired_count"] >= 10


def test_cache_expiration_check_only_when_ttl_enabled(cache_without_ttl):
    """Test that expiration check is skipped when TTL is None."""
    # Fill cache to capacity
    for i in range(10):
        cache_without_ttl.put(f"key{i}", f"value{i}")

    # Add new entry - should evict LRU, not check expiration
    cache_without_ttl.put("new_key", "new_value")

    stats = cache_without_ttl.get_stats()
    assert stats["size"] == 10  # Still at capacity
    assert stats["evictions"] == 1  # LRU evicted
    assert stats["expired_count"] == 0  # No expiration check


def test_cache_expired_count_tracked_in_stats(cache_with_ttl):
    """Test that expired entry count is tracked in cache stats."""
    # Add entries
    for i in range(5):
        cache_with_ttl.put(f"key{i}", f"value{i}")

    # Wait for entries to expire (TTL=1s; sleep well past to avoid CI timing flakiness)
    time.sleep(2.0)

    # Try to get expired entry - should increment expired_count
    result = cache_with_ttl.get("key0")
    assert result is None

    stats = cache_with_ttl.get_stats()
    assert stats["expired_count"] >= 1


def test_cache_expiration_rate_calculated(cache_with_ttl):
    """Test that expiration rate is calculated in stats."""
    # Add entries
    for i in range(5):
        cache_with_ttl.put(f"key{i}", f"value{i}")

    # Wait for entries to expire (TTL=1s; sleep well past to avoid CI timing flakiness)
    time.sleep(2.0)

    # Access expired entries
    for i in range(5):
        cache_with_ttl.get(f"key{i}")

    stats = cache_with_ttl.get_stats()
    assert "expiration_rate" in stats
    assert stats["expiration_rate"] >= 0.0
    assert "expired_vs_lru_ratio" in stats


def test_cache_size_stays_within_bounds_after_expiration(cache_with_ttl):
    """Test that cache size stays within bounds after expiration cleanup."""
    # Fill cache to capacity
    for i in range(10):
        cache_with_ttl.put(f"key{i}", f"value{i}")

    # Wait for entries to expire (TTL=1s; sleep well past to avoid CI timing flakiness)
    time.sleep(2.0)

    # Add many new entries
    for i in range(20):
        cache_with_ttl.put(f"new_key{i}", f"new_value{i}")

    stats = cache_with_ttl.get_stats()
    # Cache size should never exceed max_size
    assert stats["size"] <= cache_with_ttl.max_size
    assert stats["size"] == 10  # At capacity


@pytest.mark.asyncio
async def test_cache_expiration_performance_impact():
    """Test that expiration checking doesn't significantly impact performance."""
    cache = LRUCache[str, str](max_size=1000, ttl_seconds=60)

    # Fill cache
    start_time = time.time()
    for i in range(1000):
        cache.put(f"key{i}", f"value{i}")
    _fill_time = time.time() - start_time  # pylint: disable=unused-variable  # Reason: Time measurement kept for potential future debugging/analysis

    # Add entry when cache is full (triggers expiration check)
    start_time = time.time()
    cache.put("new_key", "new_value")
    put_time = time.time() - start_time

    # Expiration check should be fast (< 10ms for 1000 entries)
    # Allow some margin for test environment variability
    assert put_time < 0.1, f"Expiration check took {put_time}s, expected < 0.1s"


def test_cache_expired_entries_removed_efficiently(cache_with_ttl):
    """Test that expired entries are removed efficiently in bulk."""
    # Fill cache to capacity
    for i in range(10):
        cache_with_ttl.put(f"key{i}", f"value{i}")

    # Wait for entries to expire (TTL=1s; sleep well past to avoid CI timing flakiness)
    time.sleep(2.0)

    # Add new entry - should remove all expired entries in one pass
    start_time = time.time()
    cache_with_ttl.put("new_key", "new_value")
    cleanup_time = time.time() - start_time

    stats = cache_with_ttl.get_stats()
    # All expired entries should be removed
    assert stats["expired_count"] >= 10
    # Cleanup should be fast
    assert cleanup_time < 0.1, f"Expiration cleanup took {cleanup_time}s, expected < 0.1s"


def test_cache_mixed_expired_and_valid_entries(cache_with_ttl):
    """Test cache behavior with mix of expired and valid entries."""
    # Add entries at different times (TTL=1s). Use generous sleeps for CI.
    cache_with_ttl.put("key0", "value0")
    time.sleep(1.5)  # key0 expires at t=1.0
    cache_with_ttl.put("key1", "value1")
    time.sleep(1.5)  # key1 expires at t=2.5
    cache_with_ttl.put("key2", "value2")

    # Wait so key0 and key1 are clearly expired, key2 still valid (expires at t=3.5)
    time.sleep(0.8)

    # key0 expired (t=0, exp 1.0); key1 expired (t=1.5, exp 2.5); key2 valid (t=3.0, exp 4.0)
    assert cache_with_ttl.get("key0") is None
    assert cache_with_ttl.get("key1") is None
    assert cache_with_ttl.get("key2") == "value2"

    stats = cache_with_ttl.get_stats()
    assert stats["expired_count"] >= 2  # key0 and key1 expired
    assert stats["size"] == 1  # Only key2 remains (key0 and key1 expired)
