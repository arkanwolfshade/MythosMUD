"""
Unit tests for room_utils.

Tests utility functions for room operations.
"""

import warnings

from server.utils.room_utils import (
    extract_subzone_from_room_id,
    get_local_channel_subject,
    get_plane_from_room_id,
    get_subzone_local_channel_subject,
    get_zone_from_room_id,
    is_valid_room_id_format,
)


def test_extract_subzone_from_room_id():
    """Test extract_subzone_from_room_id() extracts subzone."""
    room_id = "earth_arkhamcity_northside_intersection_derby_high"
    result = extract_subzone_from_room_id(room_id)
    assert result == "northside"


def test_extract_subzone_from_room_id_downtown():
    """Test extract_subzone_from_room_id() extracts different subzone."""
    room_id = "earth_arkhamcity_downtown_market_square"
    result = extract_subzone_from_room_id(room_id)
    assert result == "downtown"


def test_extract_subzone_from_room_id_invalid():
    """Test extract_subzone_from_room_id() returns None for invalid format."""
    assert extract_subzone_from_room_id("invalid_room_id") is None
    assert extract_subzone_from_room_id("") is None
    assert extract_subzone_from_room_id("earth_zone") is None


def test_get_zone_from_room_id():
    """Test get_zone_from_room_id() extracts zone."""
    room_id = "earth_arkhamcity_northside_intersection_derby_high"
    result = get_zone_from_room_id(room_id)
    assert result == "arkhamcity"


def test_get_zone_from_room_id_innsmouth():
    """Test get_zone_from_room_id() extracts different zone."""
    room_id = "earth_innsmouth_docks_warehouse_1"
    result = get_zone_from_room_id(room_id)
    assert result == "innsmouth"


def test_get_zone_from_room_id_invalid():
    """Test get_zone_from_room_id() returns None for invalid format."""
    assert get_zone_from_room_id("invalid") is None
    assert get_zone_from_room_id("") is None


def test_get_plane_from_room_id():
    """Test get_plane_from_room_id() extracts plane."""
    room_id = "earth_arkhamcity_northside_intersection_derby_high"
    result = get_plane_from_room_id(room_id)
    assert result == "earth"


def test_get_plane_from_room_id_dream():
    """Test get_plane_from_room_id() extracts different plane."""
    room_id = "dream_innsmouth_docks_warehouse_1"
    result = get_plane_from_room_id(room_id)
    assert result == "dream"


def test_get_plane_from_room_id_invalid():
    """Test get_plane_from_room_id() returns None for invalid format."""
    assert get_plane_from_room_id("invalid") is None
    assert get_plane_from_room_id("") is None


def test_is_valid_room_id_format():
    """Test is_valid_room_id_format() validates room ID format."""
    assert is_valid_room_id_format("earth_arkhamcity_northside_intersection_derby_high") is True
    assert is_valid_room_id_format("earth_zone_subzone_room") is True
    assert is_valid_room_id_format("invalid_room_id") is False
    assert is_valid_room_id_format("") is False


def test_get_local_channel_subject():
    """Test get_local_channel_subject() generates subject (deprecated)."""
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        result = get_local_channel_subject("earth_arkhamcity_northside_intersection_derby_high")
        assert result == "chat.local.earth_arkhamcity_northside_intersection_derby_high"


def test_get_local_channel_subject_invalid():
    """Test get_local_channel_subject() returns None for invalid room ID."""
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        assert get_local_channel_subject("invalid") is None


def test_get_subzone_local_channel_subject():
    """Test get_subzone_local_channel_subject() generates subject."""
    room_id = "earth_arkhamcity_northside_intersection_derby_high"
    result = get_subzone_local_channel_subject(room_id)
    assert result == "chat.local.subzone.northside"


def test_get_subzone_local_channel_subject_invalid():
    """Test get_subzone_local_channel_subject() returns None for invalid room ID."""
    assert get_subzone_local_channel_subject("invalid") is None
    assert get_subzone_local_channel_subject("") is None
