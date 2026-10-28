"""Unit tests for the shared instance-room constants."""

from server.constants.instance_rooms import (
    INSTANCE_ROOM_PREFIX,
    PENDING_INSTANCE_ID,
    is_instance_room_id,
    template_room_id_of,
)

CLONE_ID = "instance_e4857769-81a3-40dd-bf65-b1811a1904ee_earth_arkhamcity_downtown_001"


def test_instance_room_ids_carry_the_prefix_an_instance_id_and_a_stable_id() -> None:
    assert is_instance_room_id(CLONE_ID)
    assert CLONE_ID.startswith(INSTANCE_ROOM_PREFIX)


def test_world_and_template_ids_are_not_instance_rooms() -> None:
    assert not is_instance_room_id("earth_arkhamcity_downtown_001")
    assert not is_instance_room_id("")
    assert not is_instance_room_id("instance_")  # the prefix alone names no instance and no room


def test_the_pending_marker_is_set_but_never_mistaken_for_a_live_instance_room() -> None:
    """A player waiting for their first instance carries this id; it must be truthy and resolve to no room."""
    assert PENDING_INSTANCE_ID
    assert not is_instance_room_id(PENDING_INSTANCE_ID)


def test_an_instance_room_id_maps_back_to_the_template_room_it_was_cloned_from() -> None:
    """The database only knows the template, so maps and exploration look rooms up by this id (#1108)."""
    assert template_room_id_of(CLONE_ID) == "earth_arkhamcity_downtown_001"


def test_ids_that_are_not_instance_rooms_come_back_unchanged() -> None:
    for room_id in ("earth_arkhamcity_downtown_001", "", PENDING_INSTANCE_ID, "instance_", "instance_not-a-uuid_x_y"):
        assert template_room_id_of(room_id) == room_id
