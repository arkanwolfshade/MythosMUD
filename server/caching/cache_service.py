"""
Cache service for MythosMUD server.

This module provides caching services that integrate with the existing
persistence layer to cache frequently accessed data like rooms, NPCs, and professions.
"""

import asyncio
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar, cast

from ..structured_logging.enhanced_logging_config import get_logger
from .lru_cache import LRUCache, get_cache_manager

logger = get_logger(__name__)

# Type variables
T = TypeVar("T")


def cached(cache_name: str, key_func: Callable[..., str] | None = None, ttl_seconds: int | None = None) -> Callable:
    """
    Decorator to cache function results.

    Args:
        cache_name: Name of the cache to use
        key_func: Function to generate cache key from function arguments
        ttl_seconds: Override TTL for this specific function

    Returns:
        Decorated function with caching
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
            cache_manager = get_cache_manager()
            cache = cache_manager.get_cache(cache_name)

            if not cache:
                logger.warning("Cache not found, calling function directly", cache_name=cache_name)
                return await func(*args, **kwargs)

            # Generate cache key
            if key_func:
                cache_key = key_func(*args, **kwargs)
            else:
                # Default key generation
                cache_key = f"{func.__name__}:{str(args)}:{str(sorted(kwargs.items()))}"

            # Try to get from cache
            cached_result = cache.get(cache_key)
            if cached_result is not None:
                logger.debug("Cache hit", function=func.__name__, cache_key=cache_key)
                return cached_result

            # Call function and cache result
            logger.debug("Cache miss, calling function", function=func.__name__, cache_key=cache_key)
            result = await func(*args, **kwargs)

            # Cache the result
            cache.put(cache_key, result)
            logger.debug("Result cached", function=func.__name__, cache_key=cache_key)

            return result

        @wraps(func)
        def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            cache_manager = get_cache_manager()
            cache = cache_manager.get_cache(cache_name)

            if not cache:
                logger.warning("Cache not found, calling function directly", cache_name=cache_name)
                return func(*args, **kwargs)

            # Generate cache key
            if key_func:
                cache_key = key_func(*args, **kwargs)
            else:
                # Default key generation
                cache_key = f"{func.__name__}:{str(args)}:{str(sorted(kwargs.items()))}"

            # Try to get from cache
            cached_result = cache.get(cache_key)
            if cached_result is not None:
                logger.debug("Cache hit", function=func.__name__, cache_key=cache_key)
                return cached_result

            # Call function and cache result
            logger.debug("Cache miss, calling function", function=func.__name__, cache_key=cache_key)
            result = func(*args, **kwargs)

            # Cache the result
            cache.put(cache_key, result)
            logger.debug("Result cached", function=func.__name__, cache_key=cache_key)

            return result

        # Return appropriate wrapper based on function type
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper

    return decorator


class RoomCacheService:
    """Service for caching room data."""

    def __init__(self, persistence: Any) -> None:
        """
        Initialize the room cache service.

        Args:
            persistence: Persistence layer instance
        """
        self.persistence = persistence
        self.cache_manager = get_cache_manager()
        cache = self.cache_manager.get_cache("rooms")
        if not cache:
            # Lazily initialize the rooms cache to avoid spurious startup warnings
            try:
                cache = self.cache_manager.create_cache("rooms", max_size=5000, ttl_seconds=None)
                logger.info("Rooms cache created lazily by RoomCacheService")
            except ValueError:
                # Cache was created concurrently; retrieve it now
                cache = self.cache_manager.get_cache("rooms")
                logger.debug("Rooms cache already existed; using existing instance")
        if cache is None:
            # Defensive check for type safety and runtime correctness
            raise RuntimeError("Rooms cache not initialized")
        self.rooms_cache: LRUCache[Any, Any] = cache

        logger.info("RoomCacheService initialized")

    async def get_room(self, room_id: str) -> dict[str, Any] | None:
        """
        Get room data with caching.

        Args:
            room_id: The room ID

        Returns:
            Room data dictionary or None if not found
        """
        # Try cache first
        import time

        start_time = time.perf_counter()
        cached_room = self.rooms_cache.get(room_id)
        if cached_room is not None:
            logger.debug("Room cache hit", room_id=room_id)
            logger.debug(
                "Room cache timing",
                room_id=room_id,
                cache_hit=True,
                duration_ms=round((time.perf_counter() - start_time) * 1000, 3),
            )
            return cast(dict[str, Any], cached_room)

        # Load from persistence
        logger.debug("Room cache miss, loading from persistence", room_id=room_id)
        room = await self.persistence.async_get_room(room_id)

        if room:
            # Convert to dictionary if needed
            if hasattr(room, "to_dict"):
                room_dict: dict[str, Any] = room.to_dict()
            else:
                room_dict = cast(dict[str, Any], room)

            # Cache the result
            self.rooms_cache.put(room_id, room_dict)
            logger.debug(
                "Room cached",
                room_id=room_id,
                cache_hit=False,
                duration_ms=round((time.perf_counter() - start_time) * 1000, 3),
            )
            return room_dict

        return None

    def get_room_sync(self, room_id: str) -> dict[str, Any] | None:
        """
        Get room data with caching (synchronous version).

        Args:
            room_id: The room ID

        Returns:
            Room data dictionary or None if not found
        """
        # Try cache first
        import time

        start_time = time.perf_counter()
        cached_room = self.rooms_cache.get(room_id)
        if cached_room is not None:
            logger.debug(
                "Room cache hit (sync)",
                room_id=room_id,
                cache_hit=True,
                duration_ms=round((time.perf_counter() - start_time) * 1000, 3),
            )
            return cast(dict[str, Any], cached_room)

        # Load from persistence
        logger.debug("Room cache miss, loading from persistence (sync)", room_id=room_id)
        room = self.persistence.get_room_by_id(room_id)

        if room:
            # Convert to dictionary if needed
            if hasattr(room, "to_dict"):
                room_dict: dict[str, Any] = room.to_dict()
            else:
                room_dict = cast(dict[str, Any], room)

            # Cache the result
            self.rooms_cache.put(room_id, room_dict)
            logger.debug(
                "Room cached (sync)",
                room_id=room_id,
                cache_hit=False,
                duration_ms=round((time.perf_counter() - start_time) * 1000, 3),
            )
            return room_dict

        return None

    def invalidate_room(self, room_id: str) -> None:
        """
        Invalidate cached room data.

        Args:
            room_id: The room ID to invalidate
        """
        self.rooms_cache.delete(room_id)
        logger.debug("Room cache invalidated", room_id=room_id)

    def preload_rooms(self, room_ids: list[str]) -> None:
        """
        Preload multiple rooms into cache.

        Args:
            room_ids: List of room IDs to preload
        """
        logger.info("Preloading rooms into cache", count=len(room_ids))

        for room_id in room_ids:
            if room_id not in self.rooms_cache:
                room = self.persistence.get_room_by_id(room_id)
                if room:
                    if hasattr(room, "to_dict"):
                        room_dict = room.to_dict()
                    else:
                        room_dict = room
                    self.rooms_cache.put(room_id, room_dict)

        logger.info("Room preloading completed", requested=len(room_ids), cached=self.rooms_cache.size())


class NPCCacheService:
    """Service for caching NPC definitions and spawn rules."""

    def __init__(self, npc_service: Any) -> None:
        """
        Initialize the NPC cache service.

        Args:
            npc_service: NPC service instance
        """
        self.npc_service = npc_service
        self.cache_manager = get_cache_manager()

        # Lazily initialize NPC definitions cache
        definitions_cache_opt = self.cache_manager.get_cache("npc_definitions")
        if not definitions_cache_opt:
            try:
                definitions_cache_opt = self.cache_manager.create_cache(
                    "npc_definitions", max_size=1000, ttl_seconds=None
                )
                logger.info("NPC definitions cache created lazily by NPCCacheService")
            except ValueError:
                # Cache was created concurrently; retrieve it now
                definitions_cache_opt = self.cache_manager.get_cache("npc_definitions")
                logger.debug("NPC definitions cache already existed; using existing instance")

        # Lazily initialize NPC spawn rules cache
        spawn_rules_cache_opt = self.cache_manager.get_cache("npc_spawn_rules")
        if not spawn_rules_cache_opt:
            try:
                spawn_rules_cache_opt = self.cache_manager.create_cache(
                    "npc_spawn_rules", max_size=500, ttl_seconds=None
                )
                logger.info("NPC spawn rules cache created lazily by NPCCacheService")
            except ValueError:
                # Cache was created concurrently; retrieve it now
                spawn_rules_cache_opt = self.cache_manager.get_cache("npc_spawn_rules")
                logger.debug("NPC spawn rules cache already existed; using existing instance")

        # Assign with precise types (assert non-None after creation/retrieval)
        assert definitions_cache_opt is not None, "NPC definitions cache must exist after initialization"
        assert spawn_rules_cache_opt is not None, "NPC spawn rules cache must exist after initialization"
        self.definitions_cache: LRUCache[Any, Any] = definitions_cache_opt
        self.spawn_rules_cache: LRUCache[Any, Any] = spawn_rules_cache_opt

        logger.info("NPCCacheService initialized")

    async def get_npc_definitions(self, session: Any) -> list[Any]:
        """
        Get NPC definitions with caching.

        Args:
            session: Database session

        Returns:
            List of NPC definitions
        """
        # Try cache first
        cache_key = "all_definitions"
        import time

        start_time = time.perf_counter()
        cached_definitions = self.definitions_cache.get(cache_key)
        if cached_definitions is not None:
            logger.debug(
                "NPC definitions cache hit",
                duration_ms=round((time.perf_counter() - start_time) * 1000, 3),
            )
            return cast(list[Any], cached_definitions)

        # Load from database
        logger.debug("NPC definitions cache miss, loading from database")
        definitions = await self.npc_service.get_npc_definitions(session)

        # Cache individual definitions and the full list
        for definition in definitions:
            self.definitions_cache.put(definition.id, definition)

        self.definitions_cache.put(cache_key, definitions)
        logger.debug(
            "NPC definitions cached",
            count=len(definitions),
            duration_ms=round((time.perf_counter() - start_time) * 1000, 3),
        )

        return cast(list[Any], definitions)

    async def get_npc_definition(self, session: Any, definition_id: int) -> Any | None:
        """
        Get a specific NPC definition with caching.

        Args:
            session: Database session
            definition_id: NPC definition ID

        Returns:
            NPC definition or None if not found
        """
        # Try cache first
        cached_definition = self.definitions_cache.get(definition_id)
        if cached_definition is not None:
            logger.debug("NPC definition cache hit", definition_id=definition_id)
            return cached_definition

        # Load from database
        logger.debug("NPC definition cache miss, loading from database", definition_id=definition_id)
        definition = await self.npc_service.get_npc_definition(session, definition_id)

        if definition:
            self.definitions_cache.put(definition_id, definition)
            logger.debug("NPC definition cached", definition_id=definition_id)

        return definition

    async def get_spawn_rules(self, session: Any) -> list[Any]:
        """
        Get NPC spawn rules with caching.

        Args:
            session: Database session

        Returns:
            List of NPC spawn rules
        """
        # Try cache first
        cache_key = "all_spawn_rules"
        import time

        start_time = time.perf_counter()
        cached_rules = self.spawn_rules_cache.get(cache_key)
        if cached_rules is not None:
            logger.debug(
                "NPC spawn rules cache hit",
                duration_ms=round((time.perf_counter() - start_time) * 1000, 3),
            )
            return cast(list[Any], cached_rules)

        # Load from database
        logger.debug("NPC spawn rules cache miss, loading from database")
        rules = await self.npc_service.get_spawn_rules(session)

        # Cache individual rules and the full list
        for rule in rules:
            self.spawn_rules_cache.put(rule.id, rule)

        self.spawn_rules_cache.put(cache_key, rules)
        logger.debug(
            "NPC spawn rules cached",
            count=len(rules),
            duration_ms=round((time.perf_counter() - start_time) * 1000, 3),
        )

        return cast(list[Any], rules)

    def invalidate_npc_definitions(self) -> None:
        """Invalidate all NPC definition caches."""
        self.definitions_cache.clear()
        logger.debug("NPC definitions cache invalidated")

    def invalidate_spawn_rules(self) -> None:
        """Invalidate all NPC spawn rule caches."""
        self.spawn_rules_cache.clear()
        logger.debug("NPC spawn rules cache invalidated")


class ProfessionCacheService:
    """Service for caching profession data."""

    def __init__(self, persistence: Any) -> None:
        """
        Initialize the profession cache service.

        Args:
            persistence: Persistence layer instance
        """
        self.persistence = persistence
        self.cache_manager = get_cache_manager()
        professions_cache_opt = self.cache_manager.get_cache("professions")

        if not professions_cache_opt:
            # Lazily initialize professions cache to avoid startup warnings
            try:
                professions_cache_opt = self.cache_manager.create_cache("professions", max_size=100, ttl_seconds=None)
                logger.info("Professions cache created lazily by ProfessionCacheService")
            except ValueError:
                # Cache was created concurrently; retrieve it now
                professions_cache_opt = self.cache_manager.get_cache("professions")
                logger.debug("Professions cache already existed; using existing instance")

        # Assign with precise types, asserting non-None for type safety
        if professions_cache_opt is None:
            raise RuntimeError("Professions cache not initialized")
        self.professions_cache: LRUCache[Any, Any] = professions_cache_opt

        logger.info("ProfessionCacheService initialized")

    def get_all_professions(self) -> list[Any]:
        """
        Get all professions with caching.

        Returns:
            List of profession objects
        """
        # Try cache first
        cache_key = "all_professions"
        import time

        start_time = time.perf_counter()
        cached_professions = self.professions_cache.get(cache_key)
        if cached_professions is not None:
            logger.debug(
                "Professions cache hit",
                duration_ms=round((time.perf_counter() - start_time) * 1000, 3),
            )
            return cast(list[Any], cached_professions)

        # Load from persistence
        logger.debug("Professions cache miss, loading from persistence")
        professions = self.persistence.get_all_professions()

        # Cache individual professions and the full list
        for profession in professions:
            self.professions_cache.put(profession.id, profession)

        self.professions_cache.put(cache_key, professions)
        logger.debug(
            "Professions cached",
            count=len(professions),
            duration_ms=round((time.perf_counter() - start_time) * 1000, 3),
        )

        return cast(list[Any], professions)

    def get_profession_by_id(self, profession_id: int) -> Any | None:
        """
        Get a specific profession by ID with caching.

        Args:
            profession_id: The profession ID

        Returns:
            Profession object or None if not found
        """
        # Try cache first
        cached_profession = self.professions_cache.get(profession_id)
        if cached_profession is not None:
            logger.debug("Profession cache hit", profession_id=profession_id)
            return cached_profession

        # Load from persistence (need to get all and find the one we want)
        logger.debug("Profession cache miss, loading from persistence", profession_id=profession_id)
        professions = self.persistence.get_all_professions()

        # Find the specific profession
        profession = next((p for p in professions if p.id == profession_id), None)

        if profession:
            self.professions_cache.put(profession_id, profession)
            logger.debug("Profession cached", profession_id=profession_id)

        return profession

    def invalidate_professions(self) -> None:
        """Invalidate all profession caches."""
        self.professions_cache.clear()
        logger.debug("Professions cache invalidated")


class CacheService:
    """
    Main cache service that coordinates all caching operations.

    This service provides a unified interface for caching operations
    across different data types in the MythosMUD server.
    """

    def __init__(self, persistence: Any, npc_service: Any | None = None) -> None:
        """
        Initialize the cache service.

        Args:
            persistence: Persistence layer instance
            npc_service: NPC service instance (optional)
        """
        self.persistence = persistence
        self.npc_service = npc_service

        # Initialize specialized cache services
        self.room_cache = RoomCacheService(persistence)
        self.profession_cache = ProfessionCacheService(persistence)

        if npc_service:
            self.npc_cache: NPCCacheService | None = NPCCacheService(npc_service)
        else:
            self.npc_cache = None

        self.cache_manager = get_cache_manager()
        logger.info("CacheService initialized")

    def get_cache_stats(self) -> dict[str, Any]:
        """
        Get statistics for all caches.

        Returns:
            Dictionary containing cache statistics
        """
        return self.cache_manager.get_all_stats()

    def clear_all_caches(self) -> None:
        """Clear all caches."""
        self.cache_manager.clear_all_caches()
        logger.info("All caches cleared")

    def preload_frequently_accessed_data(self) -> None:
        """
        Preload frequently accessed data into caches.

        This method loads commonly used data like starting rooms,
        basic professions, and essential NPC definitions.
        """
        logger.info("Preloading frequently accessed data")

        # Preload starting room (if it exists)
        try:
            starting_room_id = "earth_arkhamcity_northside_intersection_derby_high"
            self.room_cache.get_room_sync(starting_room_id)
        except Exception as e:
            logger.warning("Failed to preload starting room", error=str(e))

        # Preload all professions
        try:
            self.profession_cache.get_all_professions()
        except Exception as e:
            logger.warning("Failed to preload professions", error=str(e))

        logger.info("Frequently accessed data preloading completed")
