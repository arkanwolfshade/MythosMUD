"""
Unit tests for player occupant processor.

Tests the PlayerOccupantProcessor class for querying and processing player occupants.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.player_occupant_processor import PlayerOccupantProcessor

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_connection_manager():
    """Create mock connection manager."""
    return MagicMock()


@pytest.fixture
def mock_name_extractor():
    """Create mock name extractor."""
    extractor = MagicMock()
    extractor.extract_and_validate_player_name = MagicMock(return_value="TestPlayer")
    return extractor


@pytest.fixture
def processor(mock_connection_manager, mock_name_extractor):
    """Create PlayerOccupantProcessor instance."""
    return PlayerOccupantProcessor(mock_connection_manager, mock_name_extractor)


def test_processor_init(processor, mock_connection_manager, mock_name_extractor):
    """Test PlayerOccupantProcessor initialization."""
    assert processor.connection_manager == mock_connection_manager
    assert processor.name_extractor == mock_name_extractor


def test_ensure_player_included_in_list(processor):
    """Test _ensure_player_included_in_list adds player to list."""
    player_ids = ["player_001"]
    processor._ensure_player_included_in_list("room_001", player_ids, "player_002")
    assert "player_002" in player_ids


def test_ensure_player_included_in_list_already_present(processor):
    """Test _ensure_player_included_in_list doesn't duplicate existing player."""
    player_ids = ["player_001"]
    processor._ensure_player_included_in_list("room_001", player_ids, "player_001")
    assert player_ids.count("player_001") == 1


def test_convert_player_ids_to_uuids(processor):
    """Test _convert_player_ids_to_uuids converts IDs."""
    player_ids = ["550e8400-e29b-41d4-a716-446655440000", "invalid"]
    uuids, mapping = processor._convert_player_ids_to_uuids(player_ids)
    assert len(uuids) == 1
    assert len(mapping) == 1


def test_create_player_occupant_info(processor, mock_name_extractor):
    """Test _create_player_occupant_info creates occupant info."""
    player_id_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_name_extractor.extract_and_validate_player_name.return_value = "TestPlayer"
    result = processor._create_player_occupant_info(player_id_uuid, str(player_id_uuid), mock_player)
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_process_players_for_occupants(processor, mock_connection_manager):
    """Test process_players_for_occupants processes players."""
    mock_connection_manager._get_players_batch = AsyncMock(return_value={})
    result = await processor.process_players_for_occupants("room_001", ["player_001"], None)
    assert isinstance(result, list)


def test_ensure_player_included_in_list_none(processor):
    """Test _ensure_player_included_in_list does nothing when ensure_player_included is None."""
    player_ids = ["player_001"]
    processor._ensure_player_included_in_list("room_001", player_ids, None)
    assert len(player_ids) == 1
    assert "player_001" in player_ids


def test_convert_player_ids_to_uuids_value_error(processor):
    """Test _convert_player_ids_to_uuids handles ValueError."""
    player_ids = ["invalid-uuid-format"]
    uuids, mapping = processor._convert_player_ids_to_uuids(player_ids)
    assert len(uuids) == 0
    assert len(mapping) == 0


def test_convert_player_ids_to_uuids_mixed_types(processor):
    """Test _convert_player_ids_to_uuids handles mixed string and UUID types."""
    # Test with a mix of valid UUID string, UUID object, and invalid string
    uuid1 = uuid.uuid4()
    uuid2 = uuid.uuid4()
    uuid1_str = str(uuid1)
    player_ids = [uuid1_str, uuid2, "invalid-uuid"]
    uuids, mapping = processor._convert_player_ids_to_uuids(player_ids)
    # Should have 2 valid UUIDs (the string and the UUID object)
    assert len(uuids) == 2
    assert len(mapping) == 2
    assert uuid1 in uuids
    assert uuid2 in uuids


def test_convert_player_ids_to_uuids_already_uuid(processor):
    """Test _convert_player_ids_to_uuids handles UUID objects."""
    player_id_uuid = uuid.uuid4()
    player_ids = [player_id_uuid]
    uuids, mapping = processor._convert_player_ids_to_uuids(player_ids)
    assert len(uuids) == 1
    assert uuids[0] == player_id_uuid
    assert mapping[player_id_uuid] == player_id_uuid


def test_create_player_occupant_info_invalid_name(processor, mock_name_extractor):
    """Test _create_player_occupant_info returns None for invalid name."""
    player_id_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_name_extractor.extract_and_validate_player_name.return_value = None
    result = processor._create_player_occupant_info(player_id_uuid, str(player_id_uuid), mock_player)
    assert result is None


def test_create_player_occupant_info_linkdead(processor, mock_connection_manager, mock_name_extractor):
    """Test _create_player_occupant_info adds (linkdead) indicator."""
    player_id_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.level = 5
    mock_name_extractor.extract_and_validate_player_name.return_value = "TestPlayer"
    mock_connection_manager.player_websockets = {}

    with (
        patch("server.realtime.player_occupant_processor.is_player_in_grace_period", return_value=True),
        patch("server.realtime.player_occupant_processor.is_player_in_login_grace_period", return_value=False),
    ):
        result = processor._create_player_occupant_info(player_id_uuid, str(player_id_uuid), mock_player)
        assert result is not None
        assert result["player_name"] == "TestPlayer (linkdead)"
        assert result["online"] is False


def test_create_player_occupant_info_warded(processor, mock_connection_manager, mock_name_extractor):
    """Test _create_player_occupant_info adds (warded) indicator."""
    player_id_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.level = 5
    mock_name_extractor.extract_and_validate_player_name.return_value = "TestPlayer"
    mock_connection_manager.player_websockets = {}

    with (
        patch("server.realtime.player_occupant_processor.is_player_in_grace_period", return_value=False),
        patch("server.realtime.player_occupant_processor.is_player_in_login_grace_period", return_value=True),
    ):
        result = processor._create_player_occupant_info(player_id_uuid, str(player_id_uuid), mock_player)
        assert result is not None
        assert result["player_name"] == "TestPlayer (warded)"
        assert result["online"] is False


def test_create_player_occupant_info_both_indicators(processor, mock_connection_manager, mock_name_extractor):
    """Test _create_player_occupant_info adds both (linkdead) and (warded) indicators."""
    player_id_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.level = 5
    mock_name_extractor.extract_and_validate_player_name.return_value = "TestPlayer"
    mock_connection_manager.player_websockets = {}

    with (
        patch("server.realtime.player_occupant_processor.is_player_in_grace_period", return_value=True),
        patch("server.realtime.player_occupant_processor.is_player_in_login_grace_period", return_value=True),
    ):
        result = processor._create_player_occupant_info(player_id_uuid, str(player_id_uuid), mock_player)
        assert result is not None
        assert "(linkdead)" in result["player_name"]
        assert "(warded)" in result["player_name"]
        assert result["online"] is False


def test_create_player_occupant_info_grace_period_exception(processor, mock_connection_manager, mock_name_extractor):
    """Test _create_player_occupant_info handles grace period check exceptions."""
    player_id_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.level = 5
    mock_name_extractor.extract_and_validate_player_name.return_value = "TestPlayer"
    mock_connection_manager.player_websockets = {}

    with patch(
        "server.realtime.player_occupant_processor.is_player_in_grace_period", side_effect=AttributeError("Test error")
    ):
        result = processor._create_player_occupant_info(player_id_uuid, str(player_id_uuid), mock_player)
        assert result is not None
        assert result["player_name"] == "TestPlayer"  # Should use name as-is on exception
        assert result["online"] is False


def test_create_player_occupant_info_online(processor, mock_connection_manager, mock_name_extractor):
    """Test _create_player_occupant_info marks player as online."""
    player_id_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.level = 5
    mock_name_extractor.extract_and_validate_player_name.return_value = "TestPlayer"
    mock_connection_manager.player_websockets = {player_id_uuid: MagicMock()}

    with (
        patch("server.realtime.player_occupant_processor.is_player_in_grace_period", return_value=False),
        patch("server.realtime.player_occupant_processor.is_player_in_login_grace_period", return_value=False),
    ):
        result = processor._create_player_occupant_info(player_id_uuid, str(player_id_uuid), mock_player)
        assert result is not None
        assert result["online"] is True


def test_create_player_occupant_info_default_level(processor, mock_connection_manager, mock_name_extractor):
    """Test _create_player_occupant_info uses default level when not present."""
    player_id_uuid = uuid.uuid4()
    mock_player = MagicMock()
    del mock_player.level  # Remove level attribute
    mock_name_extractor.extract_and_validate_player_name.return_value = "TestPlayer"
    mock_connection_manager.player_websockets = {}

    with (
        patch("server.realtime.player_occupant_processor.is_player_in_grace_period", return_value=False),
        patch("server.realtime.player_occupant_processor.is_player_in_login_grace_period", return_value=False),
    ):
        result = processor._create_player_occupant_info(player_id_uuid, str(player_id_uuid), mock_player)
        assert result is not None
        assert result["level"] == 1  # Default level


@pytest.mark.asyncio
async def test_process_players_for_occupants_with_player_not_found(processor, mock_connection_manager):
    """Test process_players_for_occupants handles player not found in batch load."""
    player_id_uuid = uuid.uuid4()
    player_id_str = str(player_id_uuid)
    mock_connection_manager._get_players_batch = AsyncMock(return_value={})  # Empty batch
    processor.name_extractor = MagicMock()
    processor.name_extractor.extract_and_validate_player_name = MagicMock(return_value="TestPlayer")

    result = await processor.process_players_for_occupants("room_001", [player_id_str], None)
    assert isinstance(result, list)
    assert len(result) == 0  # Player not found, so no occupants


@pytest.mark.asyncio
async def test_process_players_for_occupants_with_invalid_name(processor, mock_connection_manager):
    """Test process_players_for_occupants skips players with invalid names."""
    player_id_uuid = uuid.uuid4()
    player_id_str = str(player_id_uuid)
    mock_player = MagicMock()
    mock_connection_manager._get_players_batch = AsyncMock(return_value={player_id_uuid: mock_player})
    processor.name_extractor = MagicMock()
    processor.name_extractor.extract_and_validate_player_name = MagicMock(return_value=None)  # Invalid name

    result = await processor.process_players_for_occupants("room_001", [player_id_str], None)
    assert isinstance(result, list)
    assert len(result) == 0  # Invalid name, so no occupants


@pytest.mark.asyncio
async def test_process_players_for_occupants_with_uuid_ensure_player(processor, mock_connection_manager):
    """Test process_players_for_occupants with UUID ensure_player_included."""
    player_id_uuid = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.level = 5
    mock_connection_manager._get_players_batch = AsyncMock(return_value={player_id_uuid: mock_player})
    processor.name_extractor = MagicMock()
    processor.name_extractor.extract_and_validate_player_name = MagicMock(return_value="TestPlayer")

    with (
        patch("server.realtime.player_occupant_processor.is_player_in_grace_period", return_value=False),
        patch("server.realtime.player_occupant_processor.is_player_in_login_grace_period", return_value=False),
    ):
        mock_connection_manager.player_websockets = {}
        result = await processor.process_players_for_occupants("room_001", [], player_id_uuid)
        assert isinstance(result, list)
        assert len(result) == 1  # Should include the ensured player
