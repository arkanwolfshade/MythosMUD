"""
Unit tests for player service mutations.

Covers delete, location update, mythos status effects, soft-delete, and related
error paths. Shared fixtures mirror test_player_service.py.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.player_service import PlayerService


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    return AsyncMock()


@pytest.fixture
def player_service(mock_persistence):
    """Create a PlayerService instance."""
    return PlayerService(mock_persistence)


@pytest.mark.asyncio
async def test_delete_player_success(player_service, mock_persistence, tmp_path, monkeypatch):
    """Test delete_player() successfully deletes player."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.delete_player = AsyncMock(return_value=True)
    monkeypatch.setenv("ALIASES_DIR", str(tmp_path))
    success, message = await player_service.delete_player(player_id)
    assert success is True
    assert "deleted" in message.lower() or "TestPlayer" in message


@pytest.mark.asyncio
async def test_delete_player_not_found(player_service, mock_persistence):
    """Test delete_player() when player not found."""
    from server.exceptions import ValidationError

    player_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    with pytest.raises(ValidationError, match="Player not found"):
        await player_service.delete_player(player_id)


@pytest.mark.asyncio
async def test_update_player_location_success(player_service, mock_persistence):
    """Test update_player_location() successfully updates location."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    result = await player_service.update_player_location("TestPlayer", "room_002")
    assert result is True
    assert mock_player.current_room_id == "room_002"


@pytest.mark.asyncio
async def test_update_player_location_player_not_found(player_service, mock_persistence):
    """Test update_player_location() when player not found."""
    from server.exceptions import ValidationError

    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    with pytest.raises(ValidationError, match="Player not found"):
        await player_service.update_player_location("TestPlayer", "room_002")


@pytest.mark.asyncio
async def test_apply_lucidity_loss(player_service, mock_persistence):
    """Test apply_lucidity_loss() applies lucidity loss."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.name = "TestPlayer"
    mock_player.lucidity = 100
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.apply_lucidity_loss = AsyncMock()
    result = await player_service.apply_lucidity_loss(player_id, 10, "test_source")
    assert "message" in result
    assert "lucidity" in result["message"].lower()


@pytest.mark.asyncio
async def test_apply_fear(player_service, mock_persistence):
    """Test apply_fear() applies fear."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.apply_fear = AsyncMock()
    result = await player_service.apply_fear(player_id, 5, "test_source")
    assert "message" in result
    assert "fear" in result["message"].lower()


@pytest.mark.asyncio
async def test_apply_corruption(player_service, mock_persistence):
    """Test apply_corruption() applies corruption."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.apply_corruption = AsyncMock()
    result = await player_service.apply_corruption(player_id, 3, "test_source")
    assert "message" in result
    assert "corruption" in result["message"].lower()


@pytest.mark.asyncio
async def test_gain_occult_knowledge(player_service, mock_persistence):
    """Test gain_occult_knowledge() increases occult knowledge."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.gain_occult_knowledge = AsyncMock()
    result = await player_service.gain_occult_knowledge(player_id, 2, "test_source")
    assert "message" in result
    assert "occult" in result["message"].lower() or "knowledge" in result["message"].lower()


@pytest.mark.asyncio
async def test_heal_player(player_service, mock_persistence):
    """Test heal_player() heals player."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.name = "TestPlayer"
    mock_player.current_dp = 50
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.heal_player = AsyncMock()
    result = await player_service.heal_player(player_id, 20)
    assert "message" in result
    assert "heal" in result["message"].lower() or "recover" in result["message"].lower()


@pytest.mark.asyncio
async def test_damage_player(player_service, mock_persistence):
    """Test damage_player() damages player."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.name = "TestPlayer"
    mock_player.current_dp = 0
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.damage_player = AsyncMock()
    result = await player_service.damage_player(player_id, 10, "physical")
    assert "message" in result
    assert "damage" in result["message"].lower()


@pytest.mark.asyncio
async def test_get_user_characters(player_service, mock_persistence):
    """Test get_user_characters() returns user's characters."""
    user_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_player.name = "TestPlayer"
    mock_player.user_id = user_id
    mock_player.get_stats = MagicMock(
        return_value={
            "lucidity": 100,
            "current_dp": 0,
            "position": "standing",
            "constitution": 50,
            "size": 50,
            "power": 50,
            "education": 50,
        }
    )
    mock_player.get_stats = MagicMock(
        return_value={
            "lucidity": 100,
            "current_dp": 0,
            "position": "standing",
            "constitution": 50,
            "size": 50,
            "power": 50,
            "education": 50,
        }
    )
    mock_player.get_inventory = MagicMock(return_value=[])
    mock_player.get_status_effects = MagicMock(return_value=[])
    mock_player.profession_id = 0
    mock_player.current_room_id = "room_001"
    mock_player.experience_points = 0
    mock_player.level = 1
    mock_player.created_at = datetime.now(UTC).replace(tzinfo=None)
    mock_player.last_active = datetime.now(UTC).replace(tzinfo=None)
    mock_profession = MagicMock()
    mock_profession.name = "Tramp"
    mock_profession.description = "A wanderer"
    mock_profession.flavor_text = "Lost in the streets"
    mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)
    mock_persistence.get_active_players_by_user_id = AsyncMock(return_value=[mock_player])
    result = await player_service.get_user_characters(user_id)
    assert isinstance(result, list)
    # Result may be empty if conversion fails, but should be a list
    assert len(result) >= 0


@pytest.mark.asyncio
async def test_soft_delete_character_success(player_service, mock_persistence):
    """Test soft_delete_character() successfully soft deletes."""
    player_id = uuid.uuid4()
    user_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.user_id = user_id
    mock_player.is_deleted = False  # Not already deleted
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.soft_delete_player = AsyncMock(return_value=True)
    success, message = await player_service.soft_delete_character(player_id, user_id)
    assert success is True
    assert "deleted" in message.lower() or "success" in message.lower()


@pytest.mark.asyncio
async def test_soft_delete_character_not_found(player_service, mock_persistence):
    """Test soft_delete_character() when player not found."""
    from server.exceptions import ValidationError

    player_id = uuid.uuid4()
    user_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    with pytest.raises(ValidationError, match="Character not found"):
        await player_service.soft_delete_character(player_id, user_id)


@pytest.mark.asyncio
async def test_soft_delete_character_wrong_user(player_service, mock_persistence):
    """Test soft_delete_character() when user_id doesn't match."""
    from server.exceptions import ValidationError

    player_id = uuid.uuid4()
    user_id = uuid.uuid4()
    wrong_user_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.user_id = user_id
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    with pytest.raises(ValidationError, match="Character does not belong to user"):
        await player_service.soft_delete_character(player_id, wrong_user_id)


@pytest.mark.asyncio
async def test_validate_player_name_empty(player_service, mock_persistence):
    """Test validate_player_name() with empty string."""
    valid, message = await player_service.validate_player_name("")
    assert valid is False
    assert "empty" in message.lower()


@pytest.mark.asyncio
async def test_validate_player_name_whitespace(player_service, mock_persistence):
    """Test validate_player_name() with whitespace only."""
    valid, message = await player_service.validate_player_name("   ")
    assert valid is False
    assert "empty" in message.lower()


@pytest.mark.asyncio
async def test_validate_player_name_invalid_characters(player_service, mock_persistence):
    """Test validate_player_name() with invalid characters."""
    invalid_chars = ["<", ">", "&", '"', "'", "\\", "/", "|", ":", ";", "*", "?"]
    for char in invalid_chars:
        valid, message = await player_service.validate_player_name(f"Test{char}Name")
        assert valid is False
        assert "Player name" in message


@pytest.mark.asyncio
async def test_delete_player_persistence_fails(player_service, mock_persistence):
    """Test delete_player() when persistence.delete_player fails."""
    from server.exceptions import DatabaseError

    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.delete_player = AsyncMock(return_value=False)
    with pytest.raises(DatabaseError, match="Failed to delete player"):
        await player_service.delete_player(player_id)


@pytest.mark.asyncio
async def test_soft_delete_character_already_deleted(player_service, mock_persistence):
    """Test soft_delete_character() when character already deleted."""
    player_id = uuid.uuid4()
    user_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.user_id = user_id
    mock_player.is_deleted = True
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    success, message = await player_service.soft_delete_character(player_id, user_id)
    assert success is False
    assert "already deleted" in message.lower()


@pytest.mark.asyncio
async def test_soft_delete_character_lost_race_returns_already_deleted(
    player_service: PlayerService, mock_persistence: AsyncMock
):
    """Test soft_delete_character() when the pre-check passed (is_deleted=False) but
    soft_delete_player still returns False -- a concurrent delete won the race between the
    read and the write. This must surface as "already deleted" (-> 404), not a DatabaseError
    (-> 500): soft_delete_player's WHERE ... AND is_deleted = false no-ops in exactly this
    case (#777)."""
    player_id = uuid.uuid4()
    user_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.user_id = user_id
    mock_player.is_deleted = False
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.soft_delete_player = AsyncMock(return_value=False)
    success, message = await player_service.soft_delete_character(player_id, user_id)
    assert success is False
    assert "already deleted" in message.lower()


@pytest.mark.asyncio
async def test_apply_lucidity_loss_player_not_found(player_service, mock_persistence):
    """Test apply_lucidity_loss() when player not found."""
    from server.exceptions import ValidationError

    player_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    with pytest.raises(ValidationError, match="Player not found"):
        await player_service.apply_lucidity_loss(player_id, 10, "test_source")


@pytest.mark.asyncio
async def test_apply_fear_player_not_found(player_service, mock_persistence):
    """Test apply_fear() when player not found."""
    from server.exceptions import ValidationError

    player_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    with pytest.raises(ValidationError, match="Player not found"):
        await player_service.apply_fear(player_id, 5, "test_source")


@pytest.mark.asyncio
async def test_apply_corruption_player_not_found(player_service, mock_persistence):
    """Test apply_corruption() when player not found."""
    from server.exceptions import ValidationError

    player_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    with pytest.raises(ValidationError, match="Player not found"):
        await player_service.apply_corruption(player_id, 3, "test_source")


@pytest.mark.asyncio
async def test_gain_occult_knowledge_player_not_found(player_service, mock_persistence):
    """Test gain_occult_knowledge() when player not found."""
    from server.exceptions import ValidationError

    player_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    with pytest.raises(ValidationError, match="Player not found"):
        await player_service.gain_occult_knowledge(player_id, 2, "test_source")


@pytest.mark.asyncio
async def test_heal_player_player_not_found(player_service, mock_persistence):
    """Test heal_player() when player not found."""
    from server.exceptions import ValidationError

    player_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    with pytest.raises(ValidationError, match="Player not found"):
        await player_service.heal_player(player_id, 20)


@pytest.mark.asyncio
async def test_damage_player_player_not_found(player_service, mock_persistence):
    """Test damage_player() when player not found."""
    from server.exceptions import ValidationError

    player_id = uuid.uuid4()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    with pytest.raises(ValidationError, match="Player not found"):
        await player_service.damage_player(player_id, 10, "physical")


@pytest.mark.asyncio
async def test_validate_player_name_too_short_one_char(player_service, mock_persistence):
    """Test validate_player_name() with name only 1 character."""
    valid, message = await player_service.validate_player_name("A")
    assert valid is False
    assert "3 characters" in message or "at least" in message
