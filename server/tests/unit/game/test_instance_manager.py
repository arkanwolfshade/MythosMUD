"""
Unit tests for InstanceManager.

Tests instance creation, destruction, room cloning, and exit remapping.
"""

import uuid

import pytest

from server.game.instance_manager import InstanceManager
from server.models.room import Room


@pytest.fixture
def tutorial_room():
    """Create tutorial bedroom template room."""
    return Room(
        {
            "id": "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001",
            "name": "Patient Bedroom",
            "description": "A spartan room.",
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "sanitarium",
            "exits": {"out": "earth_arkhamcity_sanitarium_room_foyer_001"},
            "attributes": {
                "is_instanced": True,
                "instance_template_id": "tutorial_sanitarium",
                "instance_exit_room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
            },
        },
        event_bus=None,
    )


@pytest.fixture
def room_cache(tutorial_room):
    """Room cache with tutorial template."""
    return {"earth_arkhamcity_sanitarium_room_tutorial_bedroom_001": tutorial_room}


@pytest.fixture
def instance_manager(room_cache):
    """Create InstanceManager with tutorial template in cache."""
    return InstanceManager(room_cache=room_cache, event_bus=None)


def test_create_instance(instance_manager, room_cache):
    """Test create_instance creates instance with cloned rooms."""
    owner_id = uuid.uuid4()
    instance = instance_manager.create_instance(
        template_id="tutorial_sanitarium",
        owner_player_id=owner_id,
    )

    assert instance is not None
    assert instance.template_id == "tutorial_sanitarium"
    assert instance.owner_player_id == str(owner_id)
    assert instance.instance_id.startswith("instance_")
    assert len(instance.rooms) == 1

    room_id = next(iter(instance.rooms))
    assert room_id.startswith("instance_")
    assert "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001" in room_id

    room = instance.rooms[room_id]
    assert room.name == "Patient Bedroom"
    assert "out" in room.exits
    assert room.exits["out"] == "earth_arkhamcity_sanitarium_room_foyer_001"


def test_create_instance_raises_when_no_templates(instance_manager):
    """Test create_instance raises when no template rooms found."""
    with pytest.raises(ValueError, match="No template rooms found"):
        instance_manager.create_instance(
            template_id="nonexistent_template",
            owner_player_id=uuid.uuid4(),
        )


def test_destroy_instance(instance_manager):
    """Test destroy_instance removes instance from store."""
    instance = instance_manager.create_instance(
        template_id="tutorial_sanitarium",
        owner_player_id=uuid.uuid4(),
    )
    instance_id = instance.instance_id

    assert instance_manager.get_instance(instance_id) is not None
    instance_manager.destroy_instance(instance_id)
    assert instance_manager.get_instance(instance_id) is None


def test_get_first_room_id(instance_manager):
    """Test get_first_room_id returns first room of instance."""
    instance = instance_manager.create_instance(
        template_id="tutorial_sanitarium",
        owner_player_id=uuid.uuid4(),
    )
    first_room_id = instance_manager.get_first_room_id(instance.instance_id)

    assert first_room_id is not None
    assert first_room_id in instance.rooms


def test_get_exit_room_id(instance_manager):
    """Test get_exit_room_id returns fixed exit room."""
    instance = instance_manager.create_instance(
        template_id="tutorial_sanitarium",
        owner_player_id=uuid.uuid4(),
    )
    exit_room_id = instance_manager.get_exit_room_id(instance.instance_id)

    assert exit_room_id == "earth_arkhamcity_sanitarium_room_foyer_001"


def test_get_room_by_id_returns_none_for_non_instance(instance_manager):
    """Test get_room_by_id returns None for non-instance room IDs."""
    result = instance_manager.get_room_by_id("earth_arkhamcity_sanitarium_room_foyer_001")
    assert result is None


def test_get_room_by_id_returns_room_when_in_instance(instance_manager):
    """Test get_room_by_id returns room when room is in an instance."""
    instance = instance_manager.create_instance(
        template_id="tutorial_sanitarium",
        owner_player_id=uuid.uuid4(),
    )
    room_id = next(iter(instance.rooms))

    result = instance_manager.get_room_by_id(room_id)
    assert result is not None
    assert result.id == room_id
