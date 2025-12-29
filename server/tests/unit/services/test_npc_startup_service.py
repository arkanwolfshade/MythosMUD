"""
Unit tests for NPC startup service.

Tests the NPCStartupService class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.npc_startup_service import NPCStartupService, get_npc_startup_service


@pytest.fixture
def npc_startup_service():
    """Create an NPCStartupService instance."""
    return NPCStartupService()


def test_npc_startup_service_init(npc_startup_service):
    """Test NPCStartupService initialization."""
    assert npc_startup_service is not None


@pytest.mark.asyncio
async def test_spawn_npcs_on_startup(npc_startup_service):
    """Test spawn_npcs_on_startup() processes startup spawning."""
    # This is a complex integration test that would require many mocks
    # For now, just verify the method exists and can be called
    with patch("server.services.npc_startup_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_get_service.return_value = mock_service
        with patch("server.services.npc_startup_service.get_npc_session") as mock_get_session:
            mock_session = AsyncMock()
            mock_get_session.return_value = [mock_session]
            with patch("server.services.npc_startup_service.npc_service") as mock_npc_service:
                mock_npc_service.get_npc_definitions = AsyncMock(return_value=[])
                result = await npc_startup_service.spawn_npcs_on_startup()
                assert "total_attempted" in result
                assert "total_spawned" in result


@pytest.mark.asyncio
async def test_spawn_npcs_on_startup_with_required_npcs(npc_startup_service):
    """Test spawn_npcs_on_startup() spawns required NPCs."""
    mock_npc_def = MagicMock()
    mock_npc_def.required_npc = True
    mock_npc_def.id = "npc_def_001"
    mock_npc_def.name = "RequiredNPC"
    mock_npc_def.room_id = "room_001"
    with patch("server.services.npc_startup_service.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_service.spawn_npc_instance = AsyncMock(
            return_value={"success": True, "npc_id": "npc_001", "definition_name": "RequiredNPC", "room_id": "room_001"}
        )
        mock_get_service.return_value = mock_service
        with patch("server.services.npc_startup_service.get_npc_session") as mock_get_session:
            # get_npc_session is an async generator, so we need to make it async iterable
            async def async_gen():
                mock_session = AsyncMock()
                yield mock_session

            mock_get_session.return_value = async_gen()
            with patch("server.services.npc_startup_service.npc_service") as mock_npc_service:
                mock_npc_service.get_npc_definitions = AsyncMock(return_value=[mock_npc_def])
                with patch.object(npc_startup_service, "_determine_spawn_room", return_value="room_001"):
                    result = await npc_startup_service.spawn_npcs_on_startup()
                    assert result["total_attempted"] == 1
                    assert result["total_spawned"] == 1
                    assert result["required_spawned"] == 1


@pytest.mark.asyncio
async def test_spawn_required_npcs_success(npc_startup_service):
    """Test _spawn_required_npcs() successfully spawns required NPCs."""
    mock_npc_def = MagicMock()
    mock_npc_def.id = "npc_def_001"
    mock_npc_def.name = "RequiredNPC"
    mock_instance_service = MagicMock()
    mock_instance_service.spawn_npc_instance = AsyncMock(
        return_value={"success": True, "npc_id": "npc_001", "definition_name": "RequiredNPC", "room_id": "room_001"}
    )
    with patch.object(npc_startup_service, "_determine_spawn_room", return_value="room_001"):
        result = await npc_startup_service._spawn_required_npcs([mock_npc_def], mock_instance_service)
        assert result["attempted"] == 1
        assert result["spawned"] == 1
        assert result["failed"] == 0


@pytest.mark.asyncio
async def test_spawn_required_npcs_no_spawn_room(npc_startup_service):
    """Test _spawn_required_npcs() handles missing spawn room."""
    mock_npc_def = MagicMock()
    mock_npc_def.id = "npc_def_001"
    mock_npc_def.name = "RequiredNPC"
    mock_instance_service = MagicMock()
    with patch.object(npc_startup_service, "_determine_spawn_room", return_value=None):
        result = await npc_startup_service._spawn_required_npcs([mock_npc_def], mock_instance_service)
        assert result["attempted"] == 1
        assert result["spawned"] == 0
        assert result["failed"] == 1
        assert len(result["errors"]) == 1


@pytest.mark.asyncio
async def test_spawn_required_npcs_spawn_failure(npc_startup_service):
    """Test _spawn_required_npcs() handles spawn failures."""
    mock_npc_def = MagicMock()
    mock_npc_def.id = "npc_def_001"
    mock_npc_def.name = "RequiredNPC"
    mock_instance_service = MagicMock()
    mock_instance_service.spawn_npc_instance = AsyncMock(
        return_value={"success": False, "message": "Population limit reached"}
    )
    with patch.object(npc_startup_service, "_determine_spawn_room", return_value="room_001"):
        result = await npc_startup_service._spawn_required_npcs([mock_npc_def], mock_instance_service)
        assert result["attempted"] == 1
        assert result["spawned"] == 0
        assert result["failed"] == 1


@pytest.mark.asyncio
async def test_spawn_optional_npcs_with_probability(npc_startup_service):
    """Test _spawn_optional_npcs() spawns based on probability."""
    mock_npc_def = MagicMock()
    mock_npc_def.id = "npc_def_001"
    mock_npc_def.name = "OptionalNPC"
    mock_npc_def.spawn_probability = 1.0  # Always spawn
    mock_instance_service = MagicMock()
    mock_instance_service.spawn_npc_instance = AsyncMock(
        return_value={"success": True, "npc_id": "npc_001", "definition_name": "OptionalNPC", "room_id": "room_001"}
    )
    with patch.object(npc_startup_service, "_determine_spawn_room", return_value="room_001"):
        with patch("random.random", return_value=0.5):  # Below 1.0, so should spawn
            result = await npc_startup_service._spawn_optional_npcs([mock_npc_def], mock_instance_service)
            assert result["attempted"] == 1
            assert result["spawned"] == 1


@pytest.mark.asyncio
async def test_spawn_optional_npcs_skips_low_probability(npc_startup_service):
    """Test _spawn_optional_npcs() skips NPCs with low probability."""
    mock_npc_def = MagicMock()
    mock_npc_def.id = "npc_def_001"
    mock_npc_def.name = "OptionalNPC"
    mock_npc_def.spawn_probability = 0.1  # Low probability
    mock_instance_service = MagicMock()
    with patch("random.random", return_value=0.9):  # Above 0.1, so should skip
        result = await npc_startup_service._spawn_optional_npcs([mock_npc_def], mock_instance_service)
        assert result["attempted"] == 0
        assert result["spawned"] == 0


@pytest.mark.asyncio
async def test_determine_spawn_room_with_room_id(npc_startup_service):
    """Test _determine_spawn_room() uses NPC's room_id when available."""
    mock_npc_def = MagicMock()
    mock_npc_def.name = "TestNPC"
    mock_npc_def.room_id = "room_001"
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_persistence = MagicMock()
        mock_persistence.get_room_by_id = MagicMock(return_value=MagicMock())
        mock_instance.async_persistence = mock_persistence
        mock_container.get_instance.return_value = mock_instance
        result = await npc_startup_service._determine_spawn_room(mock_npc_def)
        assert result == "room_001"


@pytest.mark.asyncio
async def test_determine_spawn_room_with_sub_zone(npc_startup_service):
    """Test _determine_spawn_room() uses sub_zone default when room_id not available."""
    mock_npc_def = MagicMock()
    mock_npc_def.name = "TestNPC"
    mock_npc_def.room_id = None
    mock_npc_def.sub_zone_id = "northside"
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_persistence = MagicMock()
        mock_room = MagicMock()
        mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
        mock_instance.async_persistence = mock_persistence
        mock_container.get_instance.return_value = mock_instance
        with patch("asyncio.to_thread", new_callable=AsyncMock, return_value=mock_room):
            result = await npc_startup_service._determine_spawn_room(mock_npc_def)
            assert result == "earth_arkhamcity_northside_intersection_derby_high"


@pytest.mark.asyncio
async def test_determine_spawn_room_fallback(npc_startup_service):
    """Test _determine_spawn_room() uses fallback room when no other option."""
    mock_npc_def = MagicMock()
    mock_npc_def.name = "TestNPC"
    mock_npc_def.room_id = None
    mock_npc_def.sub_zone_id = None
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_persistence = MagicMock()
        mock_room = MagicMock()
        mock_persistence.get_room_by_id = MagicMock(return_value=None)
        mock_instance.async_persistence = mock_persistence
        mock_container.get_instance.return_value = mock_instance
        with patch("asyncio.to_thread", new_callable=AsyncMock, return_value=mock_room):
            result = await npc_startup_service._determine_spawn_room(mock_npc_def)
            assert result == "earth_arkhamcity_northside_intersection_derby_high"


@pytest.mark.asyncio
async def test_determine_spawn_room_no_persistence(npc_startup_service):
    """Test _determine_spawn_room() returns None when persistence not available."""
    mock_npc_def = MagicMock()
    mock_npc_def.name = "TestNPC"
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_instance.async_persistence = None
        mock_container.get_instance.return_value = mock_instance
        result = await npc_startup_service._determine_spawn_room(mock_npc_def)
        assert result is None


def test_get_default_room_for_sub_zone(npc_startup_service):
    """Test _get_default_room_for_sub_zone() returns correct room for known sub-zone."""
    result = npc_startup_service._get_default_room_for_sub_zone("northside")
    assert result == "earth_arkhamcity_northside_intersection_derby_high"


def test_get_default_room_for_sub_zone_unknown(npc_startup_service):
    """Test _get_default_room_for_sub_zone() returns None for unknown sub-zone."""
    result = npc_startup_service._get_default_room_for_sub_zone("unknown_zone")
    assert result is None


def test_get_default_room_for_sub_zone_case_insensitive(npc_startup_service):
    """Test _get_default_room_for_sub_zone() is case insensitive."""
    result = npc_startup_service._get_default_room_for_sub_zone("NORTHSIDE")
    assert result == "earth_arkhamcity_northside_intersection_derby_high"


def test_get_npc_startup_service():
    """Test get_npc_startup_service() returns service instance."""
    service = get_npc_startup_service()
    assert isinstance(service, NPCStartupService)
