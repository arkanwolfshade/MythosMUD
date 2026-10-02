"""
Unit tests for InstanceManager.

Tests instance creation, destruction, room cloning, and exit remapping.
"""

import uuid

import pytest

from server.game.instance_manager import (
    InstanceManager,
    TemplateRoomEntryError,
    is_template_room,
    template_exit_room_id,
    template_id_of,
)
from server.models.room import Room

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def tutorial_room() -> Room:
    """Create tutorial bedroom template room."""
    return Room(
        {
            "id": "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001",
            "name": "Patient Bedroom",
            "description": "A spartan room.",
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "sanitarium",
            "exits": {"down": "earth_arkhamcity_sanitarium_room_foyer_001"},
            # rest_location mirrors what async_persistence_room_loader promotes from
            # attributes.rest_location onto the room payload's top level (#297) -- Room itself
            # only reads the top-level key.
            "rest_location": True,
            "attributes": {
                "is_instanced": True,
                "instance_template_id": "tutorial_sanitarium",
                "instance_exit_room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
                "rest_location": True,
            },
        },
        event_bus=None,
    )


@pytest.fixture
def room_cache(tutorial_room: Room) -> dict[str, Room]:
    """Room cache with tutorial template."""
    return {"earth_arkhamcity_sanitarium_room_tutorial_bedroom_001": tutorial_room}


@pytest.fixture
def instance_manager(room_cache: dict[str, Room]) -> InstanceManager:
    """Create InstanceManager with tutorial template in cache."""
    return InstanceManager(room_cache=room_cache, event_bus=None)


def test_create_instance(instance_manager: InstanceManager):
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
    assert "down" in room.exits
    assert room.exits["down"] == "earth_arkhamcity_sanitarium_room_foyer_001"


def test_create_instance_clones_rest_location_flag(instance_manager: InstanceManager):
    """#297: cloning a rest-location template (e.g. the tutorial Patient Bedroom) must carry
    rest_location onto the instance-scoped room, or /rest there silently falls back to the
    10s countdown instead of the instant disconnect the template promises."""
    instance = instance_manager.create_instance(
        template_id="tutorial_sanitarium",
        owner_player_id=uuid.uuid4(),
    )

    room = next(iter(instance.rooms.values()))
    assert room.rest_location is True


def test_create_instance_raises_when_no_templates(instance_manager: InstanceManager):
    """Test create_instance raises when no template rooms found."""
    with pytest.raises(ValueError, match="No template rooms found"):
        instance_manager.create_instance(
            template_id="nonexistent_template",
            owner_player_id=uuid.uuid4(),
        )


def test_destroy_instance(instance_manager: InstanceManager):
    """Test destroy_instance removes instance from store."""
    instance = instance_manager.create_instance(
        template_id="tutorial_sanitarium",
        owner_player_id=uuid.uuid4(),
    )
    instance_id = instance.instance_id

    assert instance_manager.get_instance(instance_id) is not None
    instance_manager.destroy_instance(instance_id)
    assert instance_manager.get_instance(instance_id) is None


def test_get_first_room_id(instance_manager: InstanceManager):
    """Test get_first_room_id returns first room of instance."""
    instance = instance_manager.create_instance(
        template_id="tutorial_sanitarium",
        owner_player_id=uuid.uuid4(),
    )
    first_room_id = instance_manager.get_first_room_id(instance.instance_id)

    assert first_room_id is not None
    assert first_room_id in instance.rooms


def test_get_exit_room_id(instance_manager: InstanceManager):
    """Test get_exit_room_id returns fixed exit room."""
    instance = instance_manager.create_instance(
        template_id="tutorial_sanitarium",
        owner_player_id=uuid.uuid4(),
    )
    exit_room_id = instance_manager.get_exit_room_id(instance.instance_id)

    assert exit_room_id == "earth_arkhamcity_sanitarium_room_foyer_001"


def test_get_room_by_id_returns_none_for_non_instance(instance_manager: InstanceManager):
    """Test get_room_by_id returns None for non-instance room IDs."""
    result = instance_manager.get_room_by_id("earth_arkhamcity_sanitarium_room_foyer_001")
    assert result is None


def test_get_room_by_id_returns_room_when_in_instance(instance_manager: InstanceManager):
    """Test get_room_by_id returns room when room is in an instance."""
    instance = instance_manager.create_instance(
        template_id="tutorial_sanitarium",
        owner_player_id=uuid.uuid4(),
    )
    room_id = next(iter(instance.rooms))

    result = instance_manager.get_room_by_id(room_id)
    assert result is not None
    assert result.id == room_id


def test_is_template_room_true_for_template(tutorial_room: Room):
    """The tutorial bedroom template must never be entered directly."""
    assert is_template_room(tutorial_room) is True


def test_is_template_room_false_for_instance_clone(instance_manager: InstanceManager):
    """Clones copy instance_template_id from the template but are the rooms players enter."""
    instance = instance_manager.create_instance(template_id="tutorial_sanitarium", owner_player_id=uuid.uuid4())
    clone = next(iter(instance.rooms.values()))
    assert clone.attributes.get("instance_template_id") == "tutorial_sanitarium"
    assert is_template_room(clone) is False


def test_is_template_room_false_for_ordinary_room_and_none():
    """Rooms without instance_template_id (and a missing room) are not templates."""
    foyer = Room({"id": "earth_arkhamcity_sanitarium_room_foyer_001", "attributes": {"rest_location": True}})
    assert is_template_room(foyer) is False
    assert is_template_room(None) is False


def test_template_id_of_and_exit_room(tutorial_room: Room, instance_manager: InstanceManager):
    """Only the template itself reports a template id; its exit room comes from attributes."""
    assert template_id_of(tutorial_room) == "tutorial_sanitarium"
    clone = next(iter(instance_manager.create_instance("tutorial_sanitarium", uuid.uuid4()).rooms.values()))
    assert template_id_of(clone) is None
    assert template_id_of(None) is None
    assert template_exit_room_id(tutorial_room) == "earth_arkhamcity_sanitarium_room_foyer_001"
    assert template_exit_room_id(Room({"id": "x", "attributes": {}})) == "earth_arkhamcity_sanitarium_room_foyer_001"


def test_template_room_entry_error_message():
    """The refusal message is what admins see from teleport/goto."""
    error = TemplateRoomEntryError("room_x")
    assert isinstance(error, ValueError)
    assert error.room_id == "room_x"
    assert "instance template" in str(error)
