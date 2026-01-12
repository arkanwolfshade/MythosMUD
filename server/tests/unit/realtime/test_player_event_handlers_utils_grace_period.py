"""
Unit tests for player event handlers utils grace period integration.

Tests the is_player_in_grace_period() utility method.
"""

import uuid
from unittest.mock import MagicMock

import pytest

from server.realtime.player_event_handlers_utils import PlayerEventHandlerUtils


@pytest.fixture
def mock_name_extractor():
    """Create a mock PlayerNameExtractor."""
    return MagicMock()


@pytest.fixture
def mock_logger():
    """Create a mock logger."""
    return MagicMock()


def test_is_player_in_grace_period_true(mock_name_extractor, mock_logger):  # pylint: disable=redefined-outer-name
    """Test is_player_in_grace_period() returns True when player is in grace period."""
    player_id = uuid.uuid4()
    mock_connection_manager = MagicMock()
    mock_connection_manager.grace_period_players = {player_id: MagicMock()}

    utils = PlayerEventHandlerUtils(mock_connection_manager, mock_name_extractor, mock_logger)
    result = utils.is_player_in_grace_period(player_id)

    assert result is True


def test_is_player_in_grace_period_false(mock_name_extractor, mock_logger):  # pylint: disable=redefined-outer-name
    """Test is_player_in_grace_period() returns False when player is not in grace period."""
    player_id = uuid.uuid4()
    mock_connection_manager = MagicMock()
    mock_connection_manager.grace_period_players = {}

    utils = PlayerEventHandlerUtils(mock_connection_manager, mock_name_extractor, mock_logger)
    result = utils.is_player_in_grace_period(player_id)

    assert result is False


def test_is_player_in_grace_period_no_connection_manager(mock_name_extractor, mock_logger):  # pylint: disable=redefined-outer-name
    """Test is_player_in_grace_period() returns False when no connection manager."""
    player_id = uuid.uuid4()
    utils = PlayerEventHandlerUtils(None, mock_name_extractor, mock_logger)

    result = utils.is_player_in_grace_period(player_id)

    assert result is False


def test_is_player_in_grace_period_string_id(mock_name_extractor, mock_logger):  # pylint: disable=redefined-outer-name
    """Test is_player_in_grace_period() handles string player_id."""
    player_id_str = str(uuid.uuid4())
    player_id_uuid = uuid.UUID(player_id_str)
    mock_connection_manager = MagicMock()
    mock_connection_manager.grace_period_players = {player_id_uuid: MagicMock()}

    utils = PlayerEventHandlerUtils(mock_connection_manager, mock_name_extractor, mock_logger)
    result = utils.is_player_in_grace_period(player_id_str)

    assert result is True
