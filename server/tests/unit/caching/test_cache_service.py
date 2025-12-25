"""
Tests for Cache Service implementation.

This module tests the caching services that integrate with the persistence layer
to cache frequently accessed data like rooms, NPCs, and professions.

AI Agent: Tests for cache services covering initialization, cache operations,
         and invalidation with mocked persistence and NPC service dependencies.
"""


# pylint: disable=redefined-outer-name,protected-access
# Justification: pytest fixtures redefine names, protected access needed for testing internals

from unittest.mock import AsyncMock, Mock, patch

import pytest

from server.caching.cache_service import (
    CacheService,
    NPCCacheService,
    ProfessionCacheService,
    RoomCacheService,
)


@pytest.fixture
def mock_persistence():
    """Provide mock persistence layer."""
    persistence = Mock()
    persistence.async_get_room = AsyncMock()
    persistence.get_room = Mock()
    persistence.get_room_by_id = Mock()
    persistence.get_all_professions = Mock()
    return persistence


@pytest.fixture
def mock_npc_service():
    """Provide mock NPC service."""
    service = Mock()
    service.get_npc_definitions = AsyncMock()
    service.get_npc_definition = AsyncMock()
    service.get_spawn_rules = AsyncMock()
    return service


@pytest.fixture
def mock_cache_manager():
    """Provide mock cache manager."""
    from server.caching.lru_cache import LRUCache

    manager = Mock()
    # Create real LRUCache instances for testing
    manager.get_cache = Mock(return_value=None)
    manager.create_cache = Mock(side_effect=lambda name, **kwargs: LRUCache(**kwargs))
    manager.get_all_stats = Mock(return_value={"total_hits": 100, "total_misses": 50})
    manager.clear_all_caches = Mock()
    return manager


class TestRoomCacheServiceInit:
    """Test RoomCacheService initialization."""

    @patch("server.caching.cache_service.get_cache_manager")
    def test_initialization_creates_cache(self, mock_get_cache_manager, mock_persistence, mock_cache_manager):
        """Test RoomCacheService initializes and creates cache if not exists."""
        mock_get_cache_manager.return_value = mock_cache_manager

        service = RoomCacheService(mock_persistence)

        assert service.persistence == mock_persistence
        assert service.cache_manager == mock_cache_manager
        assert service.rooms_cache is not None
        mock_cache_manager.get_cache.assert_called_with("rooms")
        mock_cache_manager.create_cache.assert_called_once()

    @patch("server.caching.cache_service.get_cache_manager")
    def test_initialization_handles_concurrent_creation(
        self, mock_get_cache_manager, mock_persistence, mock_cache_manager
    ):
        """Test RoomCacheService handles concurrent cache creation gracefully."""
        from server.caching.lru_cache import LRUCache

        # Simulate concurrent creation: first call returns None, create raises ValueError,
        # second call returns the cache created by another thread
        existing_cache = LRUCache(max_size=5000)
        mock_cache_manager.get_cache = Mock(side_effect=[None, existing_cache])
        mock_cache_manager.create_cache = Mock(side_effect=ValueError("Cache already exists"))
        mock_get_cache_manager.return_value = mock_cache_manager

        service = RoomCacheService(mock_persistence)

        # Verify cache is assigned after handling concurrent creation
        assert service.rooms_cache.max_size == existing_cache.max_size
        mock_cache_manager.create_cache.assert_called_once()


class TestRoomCacheServiceOperations:
    """Test RoomCacheService operations."""

    @pytest.mark.asyncio
    @patch("server.caching.cache_service.get_cache_manager")
    async def test_get_room_cache_hit(self, mock_get_cache_manager, mock_persistence, mock_cache_manager):
        """Test get_room returns cached data on cache hit."""
        from server.caching.lru_cache import LRUCache

        cache = LRUCache(max_size=100)
        cached_room = {"id": "room1", "name": "Test Room"}
        cache.put("room1", cached_room)

        mock_cache_manager.get_cache = Mock(return_value=cache)
        mock_get_cache_manager.return_value = mock_cache_manager

        service = RoomCacheService(mock_persistence)
        result = await service.get_room("room1")

        assert result == cached_room
        mock_persistence.async_get_room.assert_not_called()

    @pytest.mark.asyncio
    @patch("server.caching.cache_service.get_cache_manager")
    async def test_get_room_cache_miss_loads_from_persistence(
        self, mock_get_cache_manager, mock_persistence, mock_cache_manager
    ):
        """Test get_room loads from persistence on cache miss."""
        from server.caching.lru_cache import LRUCache

        cache = LRUCache(max_size=5000)
        mock_cache_manager.get_cache = Mock(return_value=cache)
        mock_get_cache_manager.return_value = mock_cache_manager

        room_data = {"id": "room2", "name": "New Room"}
        mock_persistence.async_get_room.return_value = room_data

        service = RoomCacheService(mock_persistence)
        result = await service.get_room("room2")

        assert result == room_data
        mock_persistence.async_get_room.assert_called_once_with("room2")
        # Verify room was cached
        cached_result = service.rooms_cache.get("room2")
        assert cached_result == room_data

    @pytest.mark.asyncio
    @patch("server.caching.cache_service.get_cache_manager")
    async def test_get_room_returns_none_when_not_found(
        self, mock_get_cache_manager, mock_persistence, mock_cache_manager
    ):
        """Test get_room returns None when room not found."""
        from server.caching.lru_cache import LRUCache

        cache = LRUCache(max_size=100)
        mock_cache_manager.get_cache = Mock(return_value=cache)
        mock_get_cache_manager.return_value = mock_cache_manager

        mock_persistence.async_get_room.return_value = None

        service = RoomCacheService(mock_persistence)
        result = await service.get_room("nonexistent")

        assert result is None

    @patch("server.caching.cache_service.get_cache_manager")
    def test_get_room_sync_cache_hit(self, mock_get_cache_manager, mock_persistence, mock_cache_manager):
        """Test synchronous get_room returns cached data."""
        from server.caching.lru_cache import LRUCache

        cache = LRUCache(max_size=100)
        cached_room = {"id": "room3", "name": "Cached Room"}
        cache.put("room3", cached_room)

        mock_cache_manager.get_cache = Mock(return_value=cache)
        mock_get_cache_manager.return_value = mock_cache_manager

        service = RoomCacheService(mock_persistence)
        result = service.get_room_sync("room3")

        assert result == cached_room
        mock_persistence.get_room_by_id.assert_not_called()

    @patch("server.caching.cache_service.get_cache_manager")
    def test_invalidate_room(self, mock_get_cache_manager, mock_persistence, mock_cache_manager):
        """Test room cache invalidation."""
        from server.caching.lru_cache import LRUCache

        cache = LRUCache(max_size=100)
        cache.put("room4", {"id": "room4"})
        mock_cache_manager.get_cache = Mock(return_value=cache)
        mock_get_cache_manager.return_value = mock_cache_manager

        service = RoomCacheService(mock_persistence)
        service.invalidate_room("room4")

        # Verify room was removed from cache
        assert cache.get("room4") is None


class TestNPCCacheServiceInit:
    """Test NPCCacheService initialization."""

    @patch("server.caching.cache_service.get_cache_manager")
    def test_initialization_creates_caches(self, mock_get_cache_manager, mock_npc_service, mock_cache_manager):
        """Test NPCCacheService initializes both definitions and spawn rules caches."""
        mock_get_cache_manager.return_value = mock_cache_manager

        service = NPCCacheService(mock_npc_service)

        assert service.npc_service == mock_npc_service
        assert service.definitions_cache is not None
        assert service.spawn_rules_cache is not None
        # Should create both caches
        assert mock_cache_manager.create_cache.call_count == 2


class TestNPCCacheServiceOperations:
    """Test NPCCacheService operations."""

    @patch("server.caching.cache_service.get_cache_manager")
    def test_invalidate_npc_definitions(self, mock_get_cache_manager, mock_npc_service, mock_cache_manager):
        """Test NPC definitions cache invalidation."""
        from server.caching.lru_cache import LRUCache

        definitions_cache = LRUCache(max_size=1000)
        spawn_rules_cache = LRUCache(max_size=500)

        def get_cache_side_effect(name):
            if name == "npc_definitions":
                return definitions_cache
            elif name == "npc_spawn_rules":
                return spawn_rules_cache
            return None

        def create_cache_side_effect(name, **kwargs):
            if name == "npc_definitions":
                return definitions_cache
            elif name == "npc_spawn_rules":
                return spawn_rules_cache
            return LRUCache(**kwargs)

        mock_cache_manager.get_cache = Mock(side_effect=get_cache_side_effect)
        mock_cache_manager.create_cache = Mock(side_effect=create_cache_side_effect)
        mock_get_cache_manager.return_value = mock_cache_manager

        service = NPCCacheService(mock_npc_service)
        service.definitions_cache.put(1, {"id": 1})

        service.invalidate_npc_definitions()

        # Verify cache was cleared
        assert service.definitions_cache.size() == 0

    @patch("server.caching.cache_service.get_cache_manager")
    def test_invalidate_spawn_rules(self, mock_get_cache_manager, mock_npc_service, mock_cache_manager):
        """Test spawn rules cache invalidation."""
        from server.caching.lru_cache import LRUCache

        definitions_cache = LRUCache(max_size=1000)
        spawn_rules_cache = LRUCache(max_size=500)

        def get_cache_side_effect(name):
            if name == "npc_definitions":
                return definitions_cache
            elif name == "npc_spawn_rules":
                return spawn_rules_cache
            return None

        def create_cache_side_effect(name, **kwargs):
            if name == "npc_definitions":
                return definitions_cache
            elif name == "npc_spawn_rules":
                return spawn_rules_cache
            return LRUCache(**kwargs)

        mock_cache_manager.get_cache = Mock(side_effect=get_cache_side_effect)
        mock_cache_manager.create_cache = Mock(side_effect=create_cache_side_effect)
        mock_get_cache_manager.return_value = mock_cache_manager

        service = NPCCacheService(mock_npc_service)
        service.spawn_rules_cache.put(1, {"id": 1})

        service.invalidate_spawn_rules()

        # Verify cache was cleared
        assert service.spawn_rules_cache.size() == 0


class TestProfessionCacheServiceInit:
    """Test ProfessionCacheService initialization."""

    @patch("server.caching.cache_service.get_cache_manager")
    def test_initialization_creates_cache(self, mock_get_cache_manager, mock_persistence, mock_cache_manager):
        """Test ProfessionCacheService initializes cache."""
        mock_get_cache_manager.return_value = mock_cache_manager

        service = ProfessionCacheService(mock_persistence)

        assert service.persistence == mock_persistence
        assert service.professions_cache is not None
        mock_cache_manager.create_cache.assert_called_once()


class TestProfessionCacheServiceOperations:
    """Test ProfessionCacheService operations."""

    @patch("server.caching.cache_service.get_cache_manager")
    def test_get_all_professions_cache_hit(self, mock_get_cache_manager, mock_persistence, mock_cache_manager):
        """Test get_all_professions returns cached data."""
        from server.caching.lru_cache import LRUCache

        cache = LRUCache(max_size=100)
        professions = [{"id": 1, "name": "Fighter"}, {"id": 2, "name": "Mage"}]
        cache.put("all_professions", professions)

        mock_cache_manager.get_cache = Mock(return_value=cache)
        mock_get_cache_manager.return_value = mock_cache_manager

        service = ProfessionCacheService(mock_persistence)
        result = service.get_all_professions()

        assert result == professions
        mock_persistence.get_all_professions.assert_not_called()

    @patch("server.caching.cache_service.get_cache_manager")
    def test_invalidate_professions(self, mock_get_cache_manager, mock_persistence, mock_cache_manager):
        """Test professions cache invalidation."""
        from server.caching.lru_cache import LRUCache

        cache = LRUCache(max_size=100)
        cache.put("all_professions", [{"id": 1}])
        mock_cache_manager.get_cache = Mock(return_value=cache)
        mock_get_cache_manager.return_value = mock_cache_manager

        service = ProfessionCacheService(mock_persistence)
        service.invalidate_professions()

        # Verify cache was cleared
        assert service.professions_cache.size() == 0


class TestCacheServiceInit:
    """Test CacheService initialization."""

    @patch("server.caching.cache_service.get_cache_manager")
    def test_initialization_without_npc_service(self, mock_get_cache_manager, mock_persistence, mock_cache_manager):
        """Test CacheService initializes without NPC service."""
        mock_get_cache_manager.return_value = mock_cache_manager

        service = CacheService(mock_persistence, npc_service=None)

        assert service.persistence == mock_persistence
        assert service.npc_service is None
        assert service.room_cache is not None
        assert service.profession_cache is not None
        assert service.npc_cache is None

    @patch("server.caching.cache_service.get_cache_manager")
    def test_initialization_with_npc_service(
        self, mock_get_cache_manager, mock_persistence, mock_npc_service, mock_cache_manager
    ):
        """Test CacheService initializes with NPC service."""
        mock_get_cache_manager.return_value = mock_cache_manager

        service = CacheService(mock_persistence, npc_service=mock_npc_service)

        assert service.npc_cache is not None
        assert isinstance(service.npc_cache, NPCCacheService)


class TestCacheServiceOperations:
    """Test CacheService main operations."""

    @patch("server.caching.cache_service.get_cache_manager")
    def test_get_cache_stats(self, mock_get_cache_manager, mock_persistence, mock_cache_manager):
        """Test cache statistics retrieval."""
        mock_get_cache_manager.return_value = mock_cache_manager

        service = CacheService(mock_persistence)
        stats = service.get_cache_stats()

        assert isinstance(stats, dict)
        assert stats["total_hits"] == 100
        assert stats["total_misses"] == 50
        mock_cache_manager.get_all_stats.assert_called_once()

    @patch("server.caching.cache_service.get_cache_manager")
    def test_clear_all_caches(self, mock_get_cache_manager, mock_persistence, mock_cache_manager):
        """Test clearing all caches."""
        mock_get_cache_manager.return_value = mock_cache_manager

        service = CacheService(mock_persistence)
        service.clear_all_caches()

        mock_cache_manager.clear_all_caches.assert_called_once()

    @patch("server.caching.cache_service.get_cache_manager")
    def test_preload_frequently_accessed_data(self, mock_get_cache_manager, mock_persistence, mock_cache_manager):
        """Test preloading frequently accessed data."""
        from server.caching.lru_cache import LRUCache

        cache = LRUCache(max_size=100)
        mock_cache_manager.get_cache = Mock(return_value=cache)
        mock_get_cache_manager.return_value = mock_cache_manager

        mock_persistence.get_room_by_id.return_value = {"id": "start_room"}
        mock_persistence.get_all_professions.return_value = [{"id": 1}]

        service = CacheService(mock_persistence)
        service.preload_frequently_accessed_data()

        # Verify persistence was called
        assert mock_persistence.get_room_by_id.called
        assert mock_persistence.get_all_professions.called
