"""
Unit tests for player preferences service.

Tests the PlayerPreferencesService for managing player channel preferences.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock

import pytest
from sqlalchemy.engine import Result
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from server.models.player import PlayerChannelPreferences
from server.services.player_preferences_service import PlayerPreferencesService


@pytest.fixture
def preferences_service():
    """Create a PlayerPreferencesService instance."""
    return PlayerPreferencesService()


@pytest.fixture
def mock_session():
    """Create a mock async session."""
    session = MagicMock()
    session.execute = AsyncMock()
    session.add = MagicMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    session.delete = AsyncMock()
    return session


@pytest.fixture
def sample_player_id():
    """Create a sample player ID."""
    return uuid.uuid4()


@pytest.fixture
def sample_preferences(sample_player_id):
    """Create sample player preferences."""
    prefs = MagicMock(spec=PlayerChannelPreferences)
    prefs.player_id = sample_player_id
    prefs.default_channel = "local"
    prefs.muted_channels = []
    prefs.created_at = datetime.now(UTC)
    prefs.updated_at = datetime.now(UTC)
    return prefs


def test_preferences_service_initialization(preferences_service):
    """Test PlayerPreferencesService initializes correctly."""
    assert preferences_service._valid_channels == {"local", "global", "whisper", "system"}


def test_is_valid_player_id_uuid(preferences_service):
    """Test _is_valid_player_id with UUID object."""
    player_id = uuid.uuid4()
    assert preferences_service._is_valid_player_id(player_id) is True


def test_is_valid_player_id_string(preferences_service):
    """Test _is_valid_player_id with UUID string."""
    player_id = str(uuid.uuid4())
    assert preferences_service._is_valid_player_id(player_id) is True


def test_is_valid_player_id_invalid_string(preferences_service):
    """Test _is_valid_player_id with invalid string."""
    assert preferences_service._is_valid_player_id("not-a-uuid") is False


def test_is_valid_player_id_empty(preferences_service):
    """Test _is_valid_player_id with empty value."""
    assert preferences_service._is_valid_player_id("") is False
    assert preferences_service._is_valid_player_id(None) is False


def test_is_valid_channel_valid(preferences_service):
    """Test _is_valid_channel with valid channel."""
    assert preferences_service._is_valid_channel("local") is True
    assert preferences_service._is_valid_channel("global") is True
    assert preferences_service._is_valid_channel("whisper") is True
    assert preferences_service._is_valid_channel("system") is True


def test_is_valid_channel_invalid(preferences_service):
    """Test _is_valid_channel with invalid channel."""
    assert preferences_service._is_valid_channel("invalid") is False
    assert preferences_service._is_valid_channel("") is False
    assert preferences_service._is_valid_channel(None) is False


def test_is_valid_json_array_valid(preferences_service):
    """Test _is_valid_json_array with valid JSON array."""
    assert preferences_service._is_valid_json_array('["local", "global"]') is True
    assert preferences_service._is_valid_json_array("[]") is True


def test_is_valid_json_array_invalid(preferences_service):
    """Test _is_valid_json_array with invalid JSON."""
    assert preferences_service._is_valid_json_array("not json") is False
    assert preferences_service._is_valid_json_array('{"key": "value"}') is False
    assert preferences_service._is_valid_json_array("") is False
    assert preferences_service._is_valid_json_array(None) is False


@pytest.mark.asyncio
async def test_create_player_preferences_success(preferences_service, mock_session, sample_player_id):
    """Test creating player preferences successfully."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.create_player_preferences(mock_session, sample_player_id)

    assert result["success"] is True
    mock_session.add.assert_called_once()
    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_player_preferences_with_string_id(preferences_service, mock_session, sample_player_id):
    """Test creating player preferences with string UUID."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.create_player_preferences(mock_session, str(sample_player_id))

    assert result["success"] is True
    mock_session.add.assert_called_once()


@pytest.mark.asyncio
async def test_create_player_preferences_already_exists(
    preferences_service, mock_session, sample_player_id, sample_preferences
):
    """Test creating player preferences when they already exist."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.create_player_preferences(mock_session, sample_player_id)

    assert result["success"] is False
    assert "already exist" in result["error"]
    mock_session.add.assert_not_called()


@pytest.mark.asyncio
async def test_create_player_preferences_invalid_id(preferences_service, mock_session):
    """Test creating player preferences with invalid ID."""
    result = await preferences_service.create_player_preferences(mock_session, "invalid-id")

    assert result["success"] is False
    assert "Invalid player ID" in result["error"]


@pytest.mark.asyncio
async def test_create_player_preferences_integrity_error(preferences_service, mock_session, sample_player_id):
    """Test creating player preferences with integrity error."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock
    mock_session.commit.side_effect = IntegrityError("Integrity error", None, None)

    result = await preferences_service.create_player_preferences(mock_session, sample_player_id)

    assert result["success"] is False
    assert "Database integrity error" in result["error"]
    mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_player_preferences_success(preferences_service, mock_session, sample_player_id, sample_preferences):
    """Test getting player preferences successfully."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.get_player_preferences(mock_session, sample_player_id)

    assert result["success"] is True
    assert "data" in result
    assert result["data"]["player_id"] == sample_player_id
    assert result["data"]["default_channel"] == "local"


@pytest.mark.asyncio
async def test_get_player_preferences_not_found(preferences_service, mock_session, sample_player_id):
    """Test getting player preferences when not found."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.get_player_preferences(mock_session, sample_player_id)

    assert result["success"] is False
    assert "not found" in result["error"]


@pytest.mark.asyncio
async def test_get_player_preferences_database_error(preferences_service, mock_session, sample_player_id):
    """Test getting player preferences with database error."""
    mock_session.execute.side_effect = SQLAlchemyError("Database error", None, None)

    result = await preferences_service.get_player_preferences(mock_session, sample_player_id)

    assert result["success"] is False
    assert "Database error" in result["error"]


@pytest.mark.asyncio
async def test_update_default_channel_success(preferences_service, mock_session, sample_player_id, sample_preferences):
    """Test updating default channel successfully."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.update_default_channel(mock_session, sample_player_id, "global")

    assert result["success"] is True
    assert sample_preferences.default_channel == "global"
    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_default_channel_invalid_channel(preferences_service, mock_session, sample_player_id):
    """Test updating default channel with invalid channel name."""
    result = await preferences_service.update_default_channel(mock_session, sample_player_id, "invalid")

    assert result["success"] is False
    assert "Invalid channel name" in result["error"]


@pytest.mark.asyncio
async def test_update_default_channel_not_found(preferences_service, mock_session, sample_player_id):
    """Test updating default channel when preferences not found."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.update_default_channel(mock_session, sample_player_id, "global")

    assert result["success"] is False
    assert "not found" in result["error"]


@pytest.mark.asyncio
async def test_mute_channel_success(preferences_service, mock_session, sample_player_id, sample_preferences):
    """Test muting a channel successfully."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.mute_channel(mock_session, sample_player_id, "global")

    assert result["success"] is True
    assert "global" in sample_preferences.muted_channels
    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_mute_channel_already_muted(preferences_service, mock_session, sample_player_id, sample_preferences):
    """Test muting a channel that's already muted."""
    sample_preferences.muted_channels = ["global"]
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.mute_channel(mock_session, sample_player_id, "global")

    assert result["success"] is True
    assert sample_preferences.muted_channels.count("global") == 1  # Should not duplicate


@pytest.mark.asyncio
async def test_mute_channel_system_channel(preferences_service, mock_session, sample_player_id):
    """Test muting system channel (should fail)."""
    result = await preferences_service.mute_channel(mock_session, sample_player_id, "system")

    assert result["success"] is False
    assert "cannot be muted" in result["error"]


@pytest.mark.asyncio
async def test_unmute_channel_success(preferences_service, mock_session, sample_player_id, sample_preferences):
    """Test unmuting a channel successfully."""
    sample_preferences.muted_channels = ["global"]
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.unmute_channel(mock_session, sample_player_id, "global")

    assert result["success"] is True
    assert "global" not in sample_preferences.muted_channels
    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_unmute_channel_not_muted(preferences_service, mock_session, sample_player_id, sample_preferences):
    """Test unmuting a channel that's not muted."""
    sample_preferences.muted_channels = []
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.unmute_channel(mock_session, sample_player_id, "global")

    assert result["success"] is True  # Should succeed even if not muted


@pytest.mark.asyncio
async def test_get_muted_channels_success(preferences_service, mock_session, sample_player_id, sample_preferences):
    """Test getting muted channels successfully."""
    sample_preferences.muted_channels = ["global", "whisper"]
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.get_muted_channels(mock_session, sample_player_id)

    assert result["success"] is True
    assert result["data"] == ["global", "whisper"]


@pytest.mark.asyncio
async def test_get_muted_channels_not_found(preferences_service, mock_session, sample_player_id):
    """Test getting muted channels when preferences not found."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.get_muted_channels(mock_session, sample_player_id)

    assert result["success"] is False
    assert "not found" in result["error"]


@pytest.mark.asyncio
async def test_is_channel_muted_true(preferences_service, mock_session, sample_player_id, sample_preferences):
    """Test checking if channel is muted (returns True)."""
    sample_preferences.muted_channels = ["global"]
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.is_channel_muted(mock_session, sample_player_id, "global")

    assert result["success"] is True
    assert result["data"] is True


@pytest.mark.asyncio
async def test_is_channel_muted_false(preferences_service, mock_session, sample_player_id, sample_preferences):
    """Test checking if channel is muted (returns False)."""
    sample_preferences.muted_channels = []
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.is_channel_muted(mock_session, sample_player_id, "global")

    assert result["success"] is True
    assert result["data"] is False


@pytest.mark.asyncio
async def test_is_channel_muted_invalid_channel(preferences_service, mock_session, sample_player_id):
    """Test checking if channel is muted with invalid channel."""
    result = await preferences_service.is_channel_muted(mock_session, sample_player_id, "invalid")

    assert result["success"] is False
    assert "Invalid channel name" in result["error"]


@pytest.mark.asyncio
async def test_delete_player_preferences_success(
    preferences_service, mock_session, sample_player_id, sample_preferences
):
    """Test deleting player preferences successfully."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.delete_player_preferences(mock_session, sample_player_id)

    assert result["success"] is True
    mock_session.delete.assert_called_once_with(sample_preferences)
    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_delete_player_preferences_not_found(preferences_service, mock_session, sample_player_id):
    """Test deleting player preferences when not found."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.delete_player_preferences(mock_session, sample_player_id)

    assert result["success"] is False
    assert "not found" in result["error"]
    mock_session.delete.assert_not_called()


@pytest.mark.asyncio
async def test_delete_player_preferences_database_error(
    preferences_service, mock_session, sample_player_id, sample_preferences
):
    """Test deleting player preferences with database error."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock
    mock_session.commit.side_effect = SQLAlchemyError("Database error", None, None)

    result = await preferences_service.delete_player_preferences(mock_session, sample_player_id)

    assert result["success"] is False
    assert "Database error" in result["error"]
    mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_default_channel_database_error(
    preferences_service, mock_session, sample_player_id, sample_preferences
):
    """Test updating default channel with database error."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock
    mock_session.commit.side_effect = SQLAlchemyError("Database error", None, None)

    result = await preferences_service.update_default_channel(mock_session, sample_player_id, "global")

    assert result["success"] is False
    assert "Database error" in result["error"]
    mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_mute_channel_not_found(preferences_service, mock_session, sample_player_id):
    """Test muting channel when preferences not found."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.mute_channel(mock_session, sample_player_id, "global")

    assert result["success"] is False
    assert "not found" in result["error"]


@pytest.mark.asyncio
async def test_mute_channel_invalid_channel(preferences_service, mock_session, sample_player_id):
    """Test muting channel with invalid channel name."""
    result = await preferences_service.mute_channel(mock_session, sample_player_id, "invalid")

    assert result["success"] is False
    assert "Invalid channel name" in result["error"]


@pytest.mark.asyncio
async def test_unmute_channel_not_found(preferences_service, mock_session, sample_player_id):
    """Test unmuting channel when preferences not found."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.unmute_channel(mock_session, sample_player_id, "global")

    assert result["success"] is False
    assert "not found" in result["error"]


@pytest.mark.asyncio
async def test_unmute_channel_invalid_channel(preferences_service, mock_session, sample_player_id):
    """Test unmuting channel with invalid channel name."""
    result = await preferences_service.unmute_channel(mock_session, sample_player_id, "invalid")

    assert result["success"] is False
    assert "Invalid channel name" in result["error"]


@pytest.mark.asyncio
async def test_unmute_channel_database_error(preferences_service, mock_session, sample_player_id, sample_preferences):
    """Test unmuting channel with database error."""
    sample_preferences.muted_channels = ["global"]
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock
    mock_session.commit.side_effect = SQLAlchemyError("Database error", None, None)

    result = await preferences_service.unmute_channel(mock_session, sample_player_id, "global")

    assert result["success"] is False
    assert "Database error" in result["error"]
    mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_mute_channel_database_error(preferences_service, mock_session, sample_player_id, sample_preferences):
    """Test muting channel with database error."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=sample_preferences)
    mock_session.execute.return_value = result_mock
    mock_session.commit.side_effect = SQLAlchemyError("Database error", None, None)

    result = await preferences_service.mute_channel(mock_session, sample_player_id, "global")

    assert result["success"] is False
    assert "Database error" in result["error"]
    mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_player_preferences_invalid_id(preferences_service, mock_session):
    """Test getting player preferences with invalid ID."""
    result = await preferences_service.get_player_preferences(mock_session, "invalid-id")

    assert result["success"] is False
    assert "Invalid player ID" in result["error"]


@pytest.mark.asyncio
async def test_update_default_channel_invalid_id(preferences_service, mock_session):
    """Test updating default channel with invalid ID."""
    result = await preferences_service.update_default_channel(mock_session, "invalid-id", "global")

    assert result["success"] is False
    assert "Invalid player ID" in result["error"]


@pytest.mark.asyncio
async def test_mute_channel_invalid_id(preferences_service, mock_session):
    """Test muting channel with invalid ID."""
    result = await preferences_service.mute_channel(mock_session, "invalid-id", "global")

    assert result["success"] is False
    assert "Invalid player ID" in result["error"]


@pytest.mark.asyncio
async def test_unmute_channel_invalid_id(preferences_service, mock_session):
    """Test unmuting channel with invalid ID."""
    result = await preferences_service.unmute_channel(mock_session, "invalid-id", "global")

    assert result["success"] is False
    assert "Invalid player ID" in result["error"]


@pytest.mark.asyncio
async def test_get_muted_channels_invalid_id(preferences_service, mock_session):
    """Test getting muted channels with invalid ID."""
    result = await preferences_service.get_muted_channels(mock_session, "invalid-id")

    assert result["success"] is False
    assert "Invalid player ID" in result["error"]


@pytest.mark.asyncio
async def test_is_channel_muted_invalid_id(preferences_service, mock_session):
    """Test checking if channel is muted with invalid ID."""
    result = await preferences_service.is_channel_muted(mock_session, "invalid-id", "global")

    assert result["success"] is False
    assert "Invalid player ID" in result["error"]


@pytest.mark.asyncio
async def test_delete_player_preferences_invalid_id(preferences_service, mock_session):
    """Test deleting player preferences with invalid ID."""
    result = await preferences_service.delete_player_preferences(mock_session, "invalid-id")

    assert result["success"] is False
    assert "Invalid player ID" in result["error"]


@pytest.mark.asyncio
async def test_is_channel_muted_not_found(preferences_service, mock_session, sample_player_id):
    """Test checking if channel is muted when preferences not found."""
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock

    result = await preferences_service.is_channel_muted(mock_session, sample_player_id, "global")

    assert result["success"] is False
    assert "not found" in result["error"]


@pytest.mark.asyncio
async def test_get_muted_channels_database_error(preferences_service, mock_session, sample_player_id):
    """Test getting muted channels with database error."""
    mock_session.execute.side_effect = SQLAlchemyError("Database error", None, None)

    result = await preferences_service.get_muted_channels(mock_session, sample_player_id)

    assert result["success"] is False
    assert "Database error" in result["error"]


@pytest.mark.asyncio
async def test_is_channel_muted_database_error(preferences_service, mock_session, sample_player_id):
    """Test checking if channel is muted with database error."""
    mock_session.execute.side_effect = SQLAlchemyError("Database error", None, None)

    result = await preferences_service.is_channel_muted(mock_session, sample_player_id, "global")

    assert result["success"] is False
    assert "Database error" in result["error"]
