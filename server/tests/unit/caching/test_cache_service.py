"""Unit tests for server.caching.cache_service."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.caching.cache_service import (
    CacheService,
    NPCCacheService,
    ProfessionCacheService,
    RoomCacheService,
    cached,
)
from server.caching.lru_cache import get_cache_manager, reset_cache_manager


@pytest.fixture(autouse=True)
def _reset_cache_manager() -> None:
    reset_cache_manager()
    yield
    reset_cache_manager()


@dataclass
class _RoomObj:
    room_id: str
    name: str

    def to_dict(self) -> dict[str, Any]:
        return {"id": self.room_id, "name": self.name}


@dataclass
class _NpcDef:
    id: int
    name: str


@dataclass
class _SpawnRule:
    id: int
    npc_id: int


@dataclass
class _Profession:
    id: int
    name: str


def _seed_players_cache() -> None:
    """Keep players cache truthy; empty LRUCache is bool-false via __len__."""
    players = get_cache_manager().get_cache("players")
    assert players is not None
    if len(players) == 0:
        players.put("_seed", True)


class TestCachedDecorator:
    def test_sync_cache_hit_and_miss(self) -> None:
        _seed_players_cache()
        call_count = 0

        @cached("players")
        def fetch(value: str) -> str:
            nonlocal call_count
            call_count += 1
            return f"result:{value}"

        assert fetch("a") == "result:a"
        assert fetch("a") == "result:a"
        assert call_count == 1

    @pytest.mark.asyncio
    async def test_async_cache_hit_and_miss(self) -> None:
        _seed_players_cache()
        call_count = 0

        @cached("players")
        async def fetch(value: str) -> str:
            nonlocal call_count
            call_count += 1
            return f"async:{value}"

        assert await fetch("x") == "async:x"
        assert await fetch("x") == "async:x"
        assert call_count == 1

    def test_cached_missing_cache_calls_function(self) -> None:
        @cached("nonexistent_cache_name")
        def fetch() -> str:
            return "direct"

        assert fetch() == "direct"

    @pytest.mark.asyncio
    async def test_async_cached_missing_cache_calls_function(self) -> None:
        @cached("nonexistent_async_cache")
        async def fetch() -> str:
            return "async_direct"

        assert await fetch() == "async_direct"

    def test_cached_custom_key_func(self) -> None:
        _seed_players_cache()
        call_count = 0

        @cached("players", key_func=lambda _self, item_id: f"id:{item_id}")
        def fetch(_self: object, item_id: int) -> int:
            nonlocal call_count
            call_count += 1
            return item_id * 2

        assert fetch(object(), 3) == 6
        assert fetch(object(), 3) == 6
        assert call_count == 1


class TestRoomCacheService:
    @pytest.fixture
    def persistence(self) -> MagicMock:
        mock = MagicMock()
        mock.async_get_room = AsyncMock(return_value=_RoomObj("room_1", "Library"))
        mock.get_room_by_id = MagicMock(return_value={"id": "room_2", "name": "Hall"})
        return mock

    def test_init_uses_existing_rooms_cache(self, persistence: MagicMock) -> None:
        service = RoomCacheService(persistence)
        assert service.rooms_cache is get_cache_manager().get_cache("rooms")

    def test_init_lazy_creates_rooms_cache(self, persistence: MagicMock) -> None:
        manager = get_cache_manager()
        manager.delete_cache("rooms")
        service = RoomCacheService(persistence)
        assert service.rooms_cache is manager.get_cache("rooms")

    def test_init_concurrent_create_uses_existing(self, persistence: MagicMock) -> None:
        manager = get_cache_manager()
        manager.delete_cache("rooms")
        existing = manager.create_cache("rooms", max_size=100)

        with patch.object(manager, "create_cache", side_effect=ValueError("exists")):
            service = RoomCacheService(persistence)

        assert service.rooms_cache is existing

    @pytest.mark.asyncio
    async def test_get_room_cache_hit(self, persistence: MagicMock) -> None:
        service = RoomCacheService(persistence)
        service.rooms_cache.put("cached_room", {"id": "cached_room"})
        result = await service.get_room("cached_room")
        assert result == {"id": "cached_room"}
        persistence.async_get_room.assert_not_called()

    @pytest.mark.asyncio
    async def test_get_room_miss_with_to_dict(self, persistence: MagicMock) -> None:
        service = RoomCacheService(persistence)
        result = await service.get_room("room_1")
        assert result == {"id": "room_1", "name": "Library"}
        assert service.rooms_cache.get("room_1") == result

    @pytest.mark.asyncio
    async def test_get_room_miss_returns_none(self, persistence: MagicMock) -> None:
        persistence.async_get_room = AsyncMock(return_value=None)
        service = RoomCacheService(persistence)
        assert await service.get_room("missing") is None

    def test_get_room_sync_cache_hit(self, persistence: MagicMock) -> None:
        service = RoomCacheService(persistence)
        service.rooms_cache.put("sync_room", {"id": "sync_room"})
        assert service.get_room_sync("sync_room") == {"id": "sync_room"}
        persistence.get_room_by_id.assert_not_called()

    def test_get_room_sync_miss_caches_dict(self, persistence: MagicMock) -> None:
        service = RoomCacheService(persistence)
        result = service.get_room_sync("room_2")
        assert result == {"id": "room_2", "name": "Hall"}

    def test_get_room_sync_miss_with_to_dict(self, persistence: MagicMock) -> None:
        persistence.get_room_by_id = MagicMock(return_value=_RoomObj("room_3", "Attic"))
        service = RoomCacheService(persistence)
        result = service.get_room_sync("room_3")
        assert result == {"id": "room_3", "name": "Attic"}

    def test_invalidate_room(self, persistence: MagicMock) -> None:
        service = RoomCacheService(persistence)
        service.rooms_cache.put("room_x", {"id": "room_x"})
        service.invalidate_room("room_x")
        assert service.rooms_cache.get("room_x") is None

    def test_preload_rooms(self, persistence: MagicMock) -> None:
        persistence.get_room_by_id = MagicMock(
            side_effect=lambda room_id: _RoomObj(room_id, "Preloaded") if room_id == "preload_1" else None
        )
        service = RoomCacheService(persistence)
        service.rooms_cache.put("already_cached", {"id": "already_cached"})
        service.preload_rooms(["preload_1", "already_cached", "missing"])
        assert service.rooms_cache.get("preload_1") == {"id": "preload_1", "name": "Preloaded"}
        assert service.rooms_cache.get("missing") is None


class TestNPCCacheService:
    @pytest.fixture
    def npc_service(self) -> MagicMock:
        mock = MagicMock()
        mock.get_npc_definitions = AsyncMock(return_value=[_NpcDef(1, "Ghoul"), _NpcDef(2, "Cultist")])
        mock.get_npc_definition = AsyncMock(return_value=_NpcDef(1, "Ghoul"))
        mock.get_spawn_rules = AsyncMock(return_value=[_SpawnRule(10, 1), _SpawnRule(11, 2)])
        return mock

    @pytest.mark.asyncio
    async def test_get_definitions_cache_hit(self, npc_service: MagicMock) -> None:
        service = NPCCacheService(npc_service)
        cached = [_NpcDef(99, "Cached")]
        service.definitions_cache.put("all_definitions", cached)
        session = MagicMock()
        result = await service.get_npc_definitions(session)
        assert result is cached
        npc_service.get_npc_definitions.assert_not_called()

    @pytest.mark.asyncio
    async def test_get_definitions_cache_miss(self, npc_service: MagicMock) -> None:
        service = NPCCacheService(npc_service)
        session = MagicMock()
        result = await service.get_npc_definitions(session)
        assert len(result) == 2
        assert service.definitions_cache.get("all_definitions") == result
        assert service.definitions_cache.get(1) == result[0]

    @pytest.mark.asyncio
    async def test_get_npc_definition_hit_and_miss(self, npc_service: MagicMock) -> None:
        service = NPCCacheService(npc_service)
        session = MagicMock()
        definition = await service.get_npc_definition(session, 1)
        assert definition == _NpcDef(1, "Ghoul")
        cached = await service.get_npc_definition(session, 1)
        assert cached is definition
        npc_service.get_npc_definition.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_get_spawn_rules_cache_miss(self, npc_service: MagicMock) -> None:
        service = NPCCacheService(npc_service)
        session = MagicMock()
        rules = await service.get_spawn_rules(session)
        assert len(rules) == 2
        assert service.spawn_rules_cache.get("all_spawn_rules") == rules
        assert service.spawn_rules_cache.get(10) == rules[0]

    @pytest.mark.asyncio
    async def test_get_spawn_rules_cache_hit(self, npc_service: MagicMock) -> None:
        service = NPCCacheService(npc_service)
        cached_rules = [_SpawnRule(42, 7)]
        service.spawn_rules_cache.put("all_spawn_rules", cached_rules)
        session = MagicMock()
        rules = await service.get_spawn_rules(session)
        assert rules is cached_rules
        npc_service.get_spawn_rules.assert_not_called()

    def test_invalidate_caches(self, npc_service: MagicMock) -> None:
        service = NPCCacheService(npc_service)
        service.definitions_cache.put("all_definitions", [_NpcDef(1, "x")])
        service.spawn_rules_cache.put("all_spawn_rules", [_SpawnRule(1, 1)])
        service.invalidate_npc_definitions()
        service.invalidate_spawn_rules()
        assert service.definitions_cache.size() == 0
        assert service.spawn_rules_cache.size() == 0


class TestProfessionCacheService:
    @pytest.fixture
    def persistence(self) -> MagicMock:
        mock = MagicMock()
        mock.get_all_professions = MagicMock(return_value=[_Profession(1, "Investigator"), _Profession(2, "Occultist")])
        return mock

    def test_get_all_professions_hit_and_miss(self, persistence: MagicMock) -> None:
        service = ProfessionCacheService(persistence)
        first = service.get_all_professions()
        second = service.get_all_professions()
        assert first == second
        persistence.get_all_professions.assert_called_once()

    def test_get_profession_by_id_hit_and_miss(self, persistence: MagicMock) -> None:
        service = ProfessionCacheService(persistence)
        profession = service.get_profession_by_id(2)
        assert profession == _Profession(2, "Occultist")
        cached = service.get_profession_by_id(2)
        assert cached is profession

    def test_get_profession_by_id_not_found(self, persistence: MagicMock) -> None:
        service = ProfessionCacheService(persistence)
        assert service.get_profession_by_id(999) is None

    def test_invalidate_professions(self, persistence: MagicMock) -> None:
        service = ProfessionCacheService(persistence)
        service.get_all_professions()
        service.invalidate_professions()
        assert service.professions_cache.size() == 0


class TestCacheService:
    @pytest.fixture
    def persistence(self) -> MagicMock:
        mock = MagicMock()
        mock.get_room_by_id = MagicMock(return_value={"id": "earth_arkhamcity_northside_intersection_derby_high"})
        mock.get_all_professions = MagicMock(return_value=[_Profession(1, "Investigator")])
        return mock

    def test_init_without_npc_service(self, persistence: MagicMock) -> None:
        service = CacheService(persistence)
        assert service.npc_cache is None
        assert service.room_cache is not None
        assert service.profession_cache is not None

    def test_init_with_npc_service(self, persistence: MagicMock) -> None:
        npc_service = MagicMock()
        service = CacheService(persistence, npc_service=npc_service)
        assert service.npc_cache is not None

    def test_get_cache_stats_and_clear(self, persistence: MagicMock) -> None:
        service = CacheService(persistence)
        service.room_cache.rooms_cache.put("stat_room", {"id": "stat_room"})
        stats = service.get_cache_stats()
        assert "rooms" in stats
        service.clear_all_caches()
        assert service.room_cache.rooms_cache.get("stat_room") is None

    def test_preload_frequently_accessed_data(self, persistence: MagicMock) -> None:
        service = CacheService(persistence)
        service.preload_frequently_accessed_data()
        assert service.room_cache.rooms_cache.get("earth_arkhamcity_northside_intersection_derby_high") is not None
        assert service.profession_cache.professions_cache.get("all_professions") is not None

    def test_preload_handles_room_failure(self, persistence: MagicMock) -> None:
        persistence.get_room_by_id = MagicMock(side_effect=RuntimeError("db down"))
        service = CacheService(persistence)
        service.preload_frequently_accessed_data()
        persistence.get_all_professions.assert_called_once()

    def test_preload_handles_profession_failure(self, persistence: MagicMock) -> None:
        persistence.get_all_professions = MagicMock(side_effect=RuntimeError("db down"))
        service = CacheService(persistence)
        service.preload_frequently_accessed_data()
