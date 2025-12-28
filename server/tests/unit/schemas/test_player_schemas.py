"""
Unit tests for player schemas.

Tests the Pydantic models in player.py module.
"""

import uuid
from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from server.models.game import PositionState
from server.schemas.player import CharacterInfo, PlayerBase, PlayerCreate, PlayerRead, PlayerUpdate


def test_player_base():
    """Test PlayerBase can be instantiated."""
    player = PlayerBase(name="TestPlayer")

    assert player.name == "TestPlayer"
    assert player.current_room_id == "earth_arkhamcity_sanitarium_room_foyer_001"
    assert player.experience_points == 0
    assert player.level == 1


def test_player_base_validation():
    """Test PlayerBase validates name length."""
    with pytest.raises(ValidationError):
        PlayerBase(name="")


def test_player_create():
    """Test PlayerCreate can be instantiated."""
    user_id = uuid.uuid4()
    player = PlayerCreate(name="TestPlayer", user_id=user_id)

    assert player.name == "TestPlayer"
    assert player.user_id == user_id
    assert player.stats == {"health": 100, "lucidity": 100, "strength": 50}
    assert player.inventory == []
    assert player.status_effects == []


def test_player_create_custom_stats():
    """Test PlayerCreate can have custom stats."""
    user_id = uuid.uuid4()
    player = PlayerCreate(
        name="TestPlayer",
        user_id=user_id,
        stats={"health": 80, "lucidity": 90},
    )

    assert player.stats == {"health": 80, "lucidity": 90}


def test_player_read():
    """Test PlayerRead can be instantiated."""
    player_id = uuid.uuid4()
    user_id = uuid.uuid4()
    created_at = datetime.now(UTC)
    last_active = datetime.now(UTC)

    player = PlayerRead(
        id=player_id,
        user_id=user_id,
        name="TestPlayer",
        stats={},
        inventory=[],
        status_effects=[],
        created_at=created_at,
        last_active=last_active,
    )

    assert player.id == player_id
    assert player.user_id == user_id
    assert player.name == "TestPlayer"
    assert player.is_admin is False
    assert player.in_combat is False
    assert player.position == PositionState.STANDING


def test_player_read_defaults():
    """Test PlayerRead has correct default values."""
    player_id = uuid.uuid4()
    user_id = uuid.uuid4()
    created_at = datetime.now(UTC)
    last_active = datetime.now(UTC)

    player = PlayerRead(
        id=player_id,
        user_id=user_id,
        name="TestPlayer",
        stats={},
        inventory=[],
        status_effects=[],
        created_at=created_at,
        last_active=last_active,
    )

    assert player.profession_id == 0
    assert player.profession_name is None
    assert player.is_admin is False
    assert player.in_combat is False
    assert player.position == PositionState.STANDING


def test_character_info():
    """Test CharacterInfo can be instantiated."""
    created_at = datetime.now(UTC)
    last_active = datetime.now(UTC)
    character = CharacterInfo(
        player_id=str(uuid.uuid4()),
        name="TestPlayer",
        level=5,
        profession_name="Investigator",
        created_at=created_at,
        last_active=last_active,
    )

    assert character.name == "TestPlayer"
    assert character.level == 5
    assert character.profession_name == "Investigator"


def test_character_info_defaults():
    """Test CharacterInfo has correct default values."""
    created_at = datetime.now(UTC)
    last_active = datetime.now(UTC)
    character = CharacterInfo(
        player_id=str(uuid.uuid4()),
        name="TestPlayer",
        level=1,
        created_at=created_at,
        last_active=last_active,
    )

    assert character.profession_id == 0
    assert character.profession_name is None


def test_player_update():
    """Test PlayerUpdate can be instantiated with optional fields."""
    player = PlayerUpdate(name="NewName")

    assert player.name == "NewName"


def test_player_update_all_optional():
    """Test PlayerUpdate can be instantiated with all fields optional."""
    player = PlayerUpdate()

    assert player.name is None
    assert player.current_room_id is None
    assert player.stats is None
