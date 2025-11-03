"""
Caching module for MythosMUD server.

This module provides comprehensive caching functionality including LRU caches
for room data, NPC definitions, and profession data to improve performance.
"""

from .cache_service import (
    CacheService,
    NPCCacheService,
    ProfessionCacheService,
    RoomCacheService,
    cached,
)
from .lru_cache import CacheManager, LRUCache, get_cache_manager, reset_cache_manager

__all__ = [
    "LRUCache",
    "CacheManager",
    "get_cache_manager",
    "reset_cache_manager",
    "CacheService",
    "RoomCacheService",
    "NPCCacheService",
    "ProfessionCacheService",
    "cached",
]
