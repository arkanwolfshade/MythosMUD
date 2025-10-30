"""
LRU Cache implementation for MythosMUD server.

This module provides thread-safe LRU (Least Recently Used) caching functionality
for frequently accessed data like room data, NPC definitions, and profession data.
"""

import threading
import time
from collections import OrderedDict
from collections.abc import Callable
from typing import Any, TypeVar

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Type variables for generic cache
K = TypeVar("K")
V = TypeVar("V")


class LRUCache[K, V]:
    """
    Thread-safe LRU (Least Recently Used) cache implementation.

    This cache automatically evicts the least recently used items when
    the cache reaches its maximum capacity. All operations are thread-safe.
    """

    def __init__(self, max_size: int = 1000, ttl_seconds: int | None = None):
        """
        Initialize the LRU cache.

        Args:
            max_size: Maximum number of items to store in the cache
            ttl_seconds: Time-to-live in seconds for cached items (None for no expiration)
        """
        self.max_size = max_size
        self.ttl_seconds = ttl_seconds
        self._cache: OrderedDict[K, tuple[V, float]] = OrderedDict()
        self._lock = threading.RLock()
        self._hits = 0
        self._misses = 0
        self._evictions = 0

        logger.info("LRU Cache initialized", max_size=max_size, ttl_seconds=ttl_seconds)

    def get(self, key: K) -> V | None:
        """
        Get an item from the cache.

        Args:
            key: The key to look up

        Returns:
            The cached value if found and not expired, None otherwise
        """
        with self._lock:
            if key not in self._cache:
                self._misses += 1
                logger.debug("Cache miss", key=key)
                return None

            value, timestamp = self._cache[key]

            # Check TTL if set
            if self.ttl_seconds is not None:
                if time.time() - timestamp > self.ttl_seconds:
                    del self._cache[key]
                    self._misses += 1
                    logger.debug("Cache miss due to TTL expiration", key=key, age=time.time() - timestamp)
                    return None

            # Move to end (most recently used)
            self._cache.move_to_end(key)
            self._hits += 1
            logger.debug("Cache hit", key=key)
            return value

    def put(self, key: K, value: V) -> None:
        """
        Put an item into the cache.

        Args:
            key: The key to store
            value: The value to store
        """
        with self._lock:
            current_time = time.time()

            # If key exists, update it and move to end
            if key in self._cache:
                self._cache[key] = (value, current_time)
                self._cache.move_to_end(key)
                logger.debug("Cache update", key=key)
                return

            # If cache is full, remove least recently used item
            if len(self._cache) >= self.max_size:
                oldest_key, _ = self._cache.popitem(last=False)
                self._evictions += 1
                logger.debug("Cache eviction", evicted_key=oldest_key, cache_size=len(self._cache))

            # Add new item
            self._cache[key] = (value, current_time)
            logger.debug("Cache put", key=key, cache_size=len(self._cache))

    def delete(self, key: K) -> bool:
        """
        Delete an item from the cache.

        Args:
            key: The key to delete

        Returns:
            True if the item was deleted, False if it wasn't found
        """
        with self._lock:
            if key in self._cache:
                del self._cache[key]
                logger.debug("Cache delete", key=key)
                return True
            return False

    def clear(self) -> None:
        """Clear all items from the cache."""
        with self._lock:
            self._cache.clear()
            self._hits = 0
            self._misses = 0
            self._evictions = 0
            logger.info("Cache cleared")

    def size(self) -> int:
        """Get the current number of items in the cache."""
        with self._lock:
            return len(self._cache)

    def is_full(self) -> bool:
        """Check if the cache is at maximum capacity."""
        with self._lock:
            return len(self._cache) >= self.max_size

    def get_stats(self) -> dict[str, Any]:
        """
        Get cache statistics.

        Returns:
            Dictionary containing cache statistics
        """
        with self._lock:
            total_requests = self._hits + self._misses
            hit_rate = (self._hits / total_requests) if total_requests > 0 else 0.0

            return {
                "size": len(self._cache),
                "max_size": self.max_size,
                "hits": self._hits,
                "misses": self._misses,
                "evictions": self._evictions,
                "hit_rate": hit_rate,
                "ttl_seconds": self.ttl_seconds,
            }

    def get_or_set(self, key: K, factory: Callable[[], V]) -> V:
        """
        Get an item from the cache, or set it using a factory function if not found.

        Args:
            key: The key to look up
            factory: Function to call if the key is not found

        Returns:
            The cached value or the result of the factory function
        """
        value = self.get(key)
        if value is None:
            value = factory()
            self.put(key, value)
        return value

    def keys(self) -> list[K]:
        """Get all keys in the cache."""
        with self._lock:
            return list(self._cache.keys())

    def values(self) -> list[V]:
        """Get all values in the cache."""
        with self._lock:
            return [value for value, _ in self._cache.values()]

    def items(self) -> list[tuple[K, V]]:
        """Get all key-value pairs in the cache."""
        with self._lock:
            return [(key, value) for key, (value, _) in self._cache.items()]

    def __len__(self) -> int:
        """Get the number of items in the cache."""
        return self.size()

    def __contains__(self, key: K) -> bool:
        """Check if a key exists in the cache."""
        with self._lock:
            if key not in self._cache:
                return False

            # Check TTL if set
            if self.ttl_seconds is not None:
                value, timestamp = self._cache[key]
                if time.time() - timestamp > self.ttl_seconds:
                    del self._cache[key]
                    return False

            return True

    def __repr__(self) -> str:
        """String representation of the cache."""
        stats = self.get_stats()
        return f"LRUCache(size={stats['size']}, max_size={stats['max_size']}, hit_rate={stats['hit_rate']:.2f})"


class CacheManager:
    """
    Centralized cache manager for MythosMUD server.

    Manages multiple LRU caches for different types of data with
    appropriate configurations and monitoring.
    """

    def __init__(self) -> None:
        """Initialize the cache manager."""
        self._caches: dict[str, LRUCache[Any, Any]] = {}
        self._lock = threading.RLock()

        # Initialize default caches
        self._initialize_default_caches()

        logger.info("CacheManager initialized")

    def _initialize_default_caches(self) -> None:
        """Initialize default caches with appropriate configurations."""
        # Room data cache - large capacity, no TTL (rooms are static)
        self._caches["rooms"] = LRUCache[str, Any](
            max_size=5000,  # Large capacity for room data
            ttl_seconds=None,  # No expiration for static room data
        )

        # NPC definitions cache - medium capacity, no TTL (definitions are static)
        self._caches["npc_definitions"] = LRUCache[int, Any](
            max_size=1000,  # Medium capacity for NPC definitions
            ttl_seconds=None,  # No expiration for static definitions
        )

        # NPC spawn rules cache - medium capacity, no TTL (rules are static)
        self._caches["npc_spawn_rules"] = LRUCache[int, Any](
            max_size=1000,  # Medium capacity for spawn rules
            ttl_seconds=None,  # No expiration for static rules
        )

        # Profession data cache - small capacity, no TTL (professions are static)
        self._caches["professions"] = LRUCache[int, Any](
            max_size=100,  # Small capacity for profession data
            ttl_seconds=None,  # No expiration for static profession data
        )

        # Player data cache - medium capacity, short TTL (player data changes frequently)
        self._caches["players"] = LRUCache[str, Any](
            max_size=500,  # Medium capacity for player data
            ttl_seconds=300,  # 5 minutes TTL for player data
        )

        logger.info("Default caches initialized", cache_names=list(self._caches.keys()))

    def get_cache(self, name: str) -> LRUCache[Any, Any] | None:
        """
        Get a cache by name.

        Args:
            name: The name of the cache

        Returns:
            The cache instance or None if not found
        """
        with self._lock:
            return self._caches.get(name)

    def create_cache(self, name: str, max_size: int = 1000, ttl_seconds: int | None = None) -> LRUCache[Any, Any]:
        """
        Create a new cache.

        Args:
            name: The name of the cache
            max_size: Maximum number of items to store
            ttl_seconds: Time-to-live in seconds (None for no expiration)

        Returns:
            The created cache instance

        Raises:
            ValueError: If a cache with the same name already exists
        """
        with self._lock:
            if name in self._caches:
                raise ValueError(f"Cache '{name}' already exists")

            cache: LRUCache[Any, Any] = LRUCache(max_size=max_size, ttl_seconds=ttl_seconds)
            self._caches[name] = cache
            logger.info("Cache created", name=name, max_size=max_size, ttl_seconds=ttl_seconds)
            return cache

    def delete_cache(self, name: str) -> bool:
        """
        Delete a cache.

        Args:
            name: The name of the cache to delete

        Returns:
            True if the cache was deleted, False if it wasn't found
        """
        with self._lock:
            if name in self._caches:
                del self._caches[name]
                logger.info("Cache deleted", name=name)
                return True
            return False

    def clear_all_caches(self) -> None:
        """Clear all caches."""
        with self._lock:
            for cache in self._caches.values():
                cache.clear()
            logger.info("All caches cleared")

    def get_all_stats(self) -> dict[str, dict[str, Any]]:
        """
        Get statistics for all caches.

        Returns:
            Dictionary mapping cache names to their statistics
        """
        with self._lock:
            return {name: cache.get_stats() for name, cache in self._caches.items()}

    def get_cache_names(self) -> list[str]:
        """Get all cache names."""
        with self._lock:
            return list(self._caches.keys())


# Global cache manager instance
_cache_manager: CacheManager | None = None
_cache_manager_lock = threading.Lock()


def get_cache_manager() -> CacheManager:
    """
    Get the global cache manager instance.

    Returns:
        The global cache manager instance
    """
    global _cache_manager
    if _cache_manager is None:
        with _cache_manager_lock:
            if _cache_manager is None:
                _cache_manager = CacheManager()
    return _cache_manager


def reset_cache_manager() -> None:
    """Reset the global cache manager (for testing)."""
    global _cache_manager
    with _cache_manager_lock:
        _cache_manager = None
