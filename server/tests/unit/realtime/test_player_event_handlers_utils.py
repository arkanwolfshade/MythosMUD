"""
Unit tests for player event handler utilities.

Tests the PlayerEventHandlerUtils class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.player_event_handlers_utils import PlayerEventHandlerUtils


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    return MagicMock()


@pytest.fixture
def mock_name_extractor():
    """Create a mock name extractor."""
    return MagicMock()


@pytest.fixture
def mock_logger():
    """Create a mock logger."""
    return MagicMock()


@pytest.fixture
def player_event_handler_utils(mock_connection_manager, mock_name_extractor, mock_logger):
    """Create a PlayerEventHandlerUtils instance."""
    return PlayerEventHandlerUtils(mock_connection_manager, mock_name_extractor, mock_logger)


def test_player_event_handler_utils_init(
    player_event_handler_utils, mock_connection_manager, mock_name_extractor, mock_logger
):
    """Test PlayerEventHandlerUtils initialization."""
    assert player_event_handler_utils.connection_manager == mock_connection_manager
    assert player_event_handler_utils.name_extractor == mock_name_extractor
    assert player_event_handler_utils._logger == mock_logger


def test_normalize_player_id_uuid(player_event_handler_utils):
    """Test normalize_player_id() with UUID."""
    player_id = uuid.uuid4()
    result = player_event_handler_utils.normalize_player_id(player_id)
    assert result == player_id


def test_normalize_player_id_string(player_event_handler_utils):
    """Test normalize_player_id() with string UUID."""
    player_id_str = str(uuid.uuid4())
    result = player_event_handler_utils.normalize_player_id(player_id_str)
    assert isinstance(result, uuid.UUID)
    assert str(result) == player_id_str


def test_normalize_player_id_invalid_string(player_event_handler_utils, mock_logger):
    """Test normalize_player_id() with invalid string."""
    result = player_event_handler_utils.normalize_player_id("invalid_uuid")
    assert result is None
    mock_logger.warning.assert_called_once()


def test_normalize_player_id_invalid_type(player_event_handler_utils):
    """Test normalize_player_id() with None returns None without warning."""
    # When None is passed, isinstance(None, str) is False, so it returns None directly
    # without raising an exception, so no warning is logged
    result = player_event_handler_utils.normalize_player_id(None)
    assert result is None


@pytest.mark.asyncio
async def test_get_player_info_success(player_event_handler_utils, mock_connection_manager, mock_name_extractor):
    """Test get_player_info() successfully retrieves player info."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_name_extractor.extract_player_name.return_value = "TestPlayer"
    mock_name_extractor.validate_player_name_not_uuid.return_value = "TestPlayer"
    result = await player_event_handler_utils.get_player_info(player_id)
    assert result is not None
    player, player_name = result
    assert player == mock_player
    assert player_name == "TestPlayer"


@pytest.mark.asyncio
async def test_get_player_info_no_connection_manager(player_event_handler_utils, mock_logger):
    """Test get_player_info() returns None when connection manager not available."""
    player_event_handler_utils.connection_manager = None
    result = await player_event_handler_utils.get_player_info(uuid.uuid4())
    assert result is None
    mock_logger.debug.assert_called_once()


@pytest.mark.asyncio
async def test_get_player_info_invalid_player_id(player_event_handler_utils, mock_logger):
    """Test get_player_info() returns None for invalid player_id."""
    result = await player_event_handler_utils.get_player_info("invalid_uuid")
    assert result is None


@pytest.mark.asyncio
async def test_get_player_info_player_not_found(player_event_handler_utils, mock_connection_manager, mock_logger):
    """Test get_player_info() returns None when player not found."""
    player_id = uuid.uuid4()
    mock_connection_manager.get_player = AsyncMock(return_value=None)
    result = await player_event_handler_utils.get_player_info(player_id)
    assert result is None
    mock_logger.warning.assert_called_once()


def test_normalize_event_ids_both_provided(player_event_handler_utils):
    """Test normalize_event_ids() with both player_id and room_id."""
    player_id = uuid.uuid4()
    room_id = uuid.uuid4()
    exclude_player_id, room_id_str = player_event_handler_utils.normalize_event_ids(player_id, room_id)
    assert exclude_player_id == str(player_id)
    assert room_id_str == str(room_id)


def test_normalize_event_ids_string_ids(player_event_handler_utils):
    """Test normalize_event_ids() with string IDs."""
    player_id = str(uuid.uuid4())
    room_id = str(uuid.uuid4())
    exclude_player_id, room_id_str = player_event_handler_utils.normalize_event_ids(player_id, room_id)
    assert exclude_player_id == player_id
    assert room_id_str == room_id


def test_normalize_event_ids_none_values(player_event_handler_utils):
    """Test normalize_event_ids() with None values."""
    exclude_player_id, room_id_str = player_event_handler_utils.normalize_event_ids(None, None)
    assert exclude_player_id is None
    assert room_id_str is None


def test_extract_name_from_occupant_dict_with_player_name(player_event_handler_utils):
    """Test _extract_name_from_occupant() with dict containing player_name."""
    occ = {"player_name": "TestPlayer"}
    result = player_event_handler_utils._extract_name_from_occupant(occ)
    assert result == "TestPlayer"


def test_extract_name_from_occupant_dict_with_npc_name(player_event_handler_utils):
    """Test _extract_name_from_occupant() with dict containing npc_name."""
    occ = {"npc_name": "TestNPC"}
    result = player_event_handler_utils._extract_name_from_occupant(occ)
    assert result == "TestNPC"


def test_extract_name_from_occupant_dict_with_name(player_event_handler_utils):
    """Test _extract_name_from_occupant() with dict containing name."""
    occ = {"name": "TestName"}
    result = player_event_handler_utils._extract_name_from_occupant(occ)
    assert result == "TestName"


def test_extract_name_from_occupant_string(player_event_handler_utils):
    """Test _extract_name_from_occupant() with string."""
    occ = "TestPlayer"
    result = player_event_handler_utils._extract_name_from_occupant(occ)
    assert result == "TestPlayer"


def test_extract_name_from_occupant_invalid_type(player_event_handler_utils):
    """Test _extract_name_from_occupant() with invalid type."""
    occ = 123
    result = player_event_handler_utils._extract_name_from_occupant(occ)
    assert result is None


def test_extract_occupant_names_valid_names(player_event_handler_utils, mock_name_extractor):
    """Test extract_occupant_names() with valid names."""
    mock_name_extractor.is_valid_name_for_occupant.return_value = True
    occupants_info = [{"player_name": "Player1"}, {"npc_name": "NPC1"}, "Player2"]
    result = player_event_handler_utils.extract_occupant_names(occupants_info)
    assert len(result) == 3
    assert "Player1" in result
    assert "NPC1" in result
    assert "Player2" in result


def test_extract_occupant_names_invalid_names(player_event_handler_utils, mock_name_extractor):
    """Test extract_occupant_names() filters invalid names."""
    mock_name_extractor.is_valid_name_for_occupant.side_effect = lambda name: name != "InvalidUUID"
    occupants_info = [{"player_name": "ValidPlayer"}, {"player_name": "InvalidUUID"}]
    result = player_event_handler_utils.extract_occupant_names(occupants_info)
    assert len(result) == 1
    assert "ValidPlayer" in result


def test_extract_occupant_names_empty_list(player_event_handler_utils):
    """Test extract_occupant_names() with empty list."""
    result = player_event_handler_utils.extract_occupant_names([])
    assert result == []


def test_extract_occupant_names_none(player_event_handler_utils):
    """Test extract_occupant_names() with None."""
    result = player_event_handler_utils.extract_occupant_names(None)
    assert result == []


def test_add_valid_name_to_lists_player(player_event_handler_utils, mock_name_extractor):
    """Test add_valid_name_to_lists() adds player name."""
    mock_name_extractor.is_valid_name_for_occupant.return_value = True
    players = []
    npcs = []
    all_occupants = []
    player_event_handler_utils.add_valid_name_to_lists("TestPlayer", players, npcs, all_occupants, is_player=True)
    assert "TestPlayer" in players
    assert "TestPlayer" in all_occupants
    assert "TestPlayer" not in npcs


def test_add_valid_name_to_lists_npc(player_event_handler_utils, mock_name_extractor):
    """Test add_valid_name_to_lists() adds NPC name."""
    mock_name_extractor.is_valid_name_for_occupant.return_value = True
    players = []
    npcs = []
    all_occupants = []
    player_event_handler_utils.add_valid_name_to_lists("TestNPC", players, npcs, all_occupants, is_player=False)
    assert "TestNPC" in npcs
    assert "TestNPC" in all_occupants
    assert "TestNPC" not in players


def test_add_valid_name_to_lists_invalid_name(player_event_handler_utils, mock_name_extractor):
    """Test add_valid_name_to_lists() skips invalid name."""
    mock_name_extractor.is_valid_name_for_occupant.return_value = False
    players = []
    npcs = []
    all_occupants = []
    player_event_handler_utils.add_valid_name_to_lists("InvalidUUID", players, npcs, all_occupants, is_player=True)
    assert len(players) == 0
    assert len(npcs) == 0
    assert len(all_occupants) == 0


def test_add_valid_name_to_lists_none_name(player_event_handler_utils):
    """Test add_valid_name_to_lists() skips None name."""
    players = []
    npcs = []
    all_occupants = []
    player_event_handler_utils.add_valid_name_to_lists(None, players, npcs, all_occupants, is_player=True)
    assert len(players) == 0
    assert len(npcs) == 0
    assert len(all_occupants) == 0


def test_process_dict_occupant_with_player_name(player_event_handler_utils, mock_name_extractor):
    """Test process_dict_occupant() processes player occupant."""
    mock_name_extractor.is_valid_name_for_occupant.return_value = True
    occ = {"player_name": "TestPlayer"}
    players = []
    npcs = []
    all_occupants = []
    player_event_handler_utils.process_dict_occupant(occ, players, npcs, all_occupants)
    assert "TestPlayer" in players
    assert "TestPlayer" in all_occupants


def test_process_dict_occupant_with_npc_name(player_event_handler_utils, mock_name_extractor):
    """Test process_dict_occupant() processes NPC occupant."""
    mock_name_extractor.is_valid_name_for_occupant.return_value = True
    occ = {"npc_name": "TestNPC"}
    players = []
    npcs = []
    all_occupants = []
    player_event_handler_utils.process_dict_occupant(occ, players, npcs, all_occupants)
    assert "TestNPC" in npcs
    assert "TestNPC" in all_occupants


def test_process_dict_occupant_with_name(player_event_handler_utils, mock_name_extractor):
    """Test process_dict_occupant() processes generic name."""
    mock_name_extractor.is_valid_name_for_occupant.return_value = True
    occ = {"name": "TestName"}
    players = []
    npcs = []
    all_occupants = []
    player_event_handler_utils.process_dict_occupant(occ, players, npcs, all_occupants)
    assert "TestName" in all_occupants
    assert "TestName" not in players
    assert "TestName" not in npcs


def test_process_dict_occupant_invalid_name(player_event_handler_utils, mock_name_extractor):
    """Test process_dict_occupant() skips invalid name."""
    mock_name_extractor.is_valid_name_for_occupant.return_value = False
    occ = {"name": "InvalidUUID"}
    players = []
    npcs = []
    all_occupants = []
    player_event_handler_utils.process_dict_occupant(occ, players, npcs, all_occupants)
    assert len(all_occupants) == 0


def test_build_occupants_snapshot_data_mixed(player_event_handler_utils, mock_name_extractor):
    """Test build_occupants_snapshot_data() with mixed occupants."""
    mock_name_extractor.is_valid_name_for_occupant.return_value = True
    occupants_snapshot = [
        {"player_name": "Player1"},
        {"npc_name": "NPC1"},
        "Player2",
    ]
    result = player_event_handler_utils.build_occupants_snapshot_data(occupants_snapshot)
    assert result["players"] == ["Player1"]
    assert result["npcs"] == ["NPC1"]
    assert "Player2" in result["occupants"]
    assert result["count"] == 3


def test_build_occupants_snapshot_data_empty(player_event_handler_utils):
    """Test build_occupants_snapshot_data() with empty list."""
    result = player_event_handler_utils.build_occupants_snapshot_data([])
    assert result["players"] == []
    assert result["npcs"] == []
    assert result["occupants"] == []
    assert result["count"] == 0


def test_build_occupants_snapshot_data_none(player_event_handler_utils):
    """Test build_occupants_snapshot_data() with None."""
    result = player_event_handler_utils.build_occupants_snapshot_data(None)
    assert result["players"] == []
    assert result["npcs"] == []
    assert result["occupants"] == []
    assert result["count"] == 0


def test_count_occupants_by_type_mixed(player_event_handler_utils):
    """Test count_occupants_by_type() with mixed occupants."""
    occupants_snapshot = [
        {"player_name": "Player1"},
        {"player_name": "Player2"},
        {"npc_name": "NPC1"},
    ]
    npc_count, player_count = player_event_handler_utils.count_occupants_by_type(occupants_snapshot)
    assert npc_count == 1
    assert player_count == 2


def test_count_occupants_by_type_empty(player_event_handler_utils):
    """Test count_occupants_by_type() with empty list."""
    npc_count, player_count = player_event_handler_utils.count_occupants_by_type([])
    assert npc_count == 0
    assert player_count == 0


def test_is_player_disconnecting_true(player_event_handler_utils, mock_connection_manager):
    """Test is_player_disconnecting() returns True when player is disconnecting."""
    player_id = uuid.uuid4()
    mock_connection_manager.disconnecting_players = {player_id}
    result = player_event_handler_utils.is_player_disconnecting(player_id)
    assert result is True


def test_is_player_disconnecting_false(player_event_handler_utils, mock_connection_manager):
    """Test is_player_disconnecting() returns False when player is not disconnecting."""
    player_id = uuid.uuid4()
    mock_connection_manager.disconnecting_players = set()
    result = player_event_handler_utils.is_player_disconnecting(player_id)
    assert result is False


def test_is_player_disconnecting_string_id(player_event_handler_utils, mock_connection_manager):
    """Test is_player_disconnecting() handles string player_id."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    mock_connection_manager.disconnecting_players = {player_id}
    result = player_event_handler_utils.is_player_disconnecting(player_id_str)
    assert result is True


def test_is_player_disconnecting_no_connection_manager(player_event_handler_utils):
    """Test is_player_disconnecting() returns False when connection manager not available."""
    player_event_handler_utils.connection_manager = None
    result = player_event_handler_utils.is_player_disconnecting(uuid.uuid4())
    assert result is False


def test_is_player_disconnecting_invalid_id(player_event_handler_utils, mock_connection_manager):
    """Test is_player_disconnecting() handles invalid player_id."""
    mock_connection_manager.disconnecting_players = {}
    result = player_event_handler_utils.is_player_disconnecting("invalid_uuid")
    assert result is False


def test_is_player_disconnecting_no_disconnecting_players_attr(player_event_handler_utils, mock_connection_manager):
    """Test is_player_disconnecting() handles missing disconnecting_players attribute."""
    del mock_connection_manager.disconnecting_players
    result = player_event_handler_utils.is_player_disconnecting(uuid.uuid4())
    assert result is False
