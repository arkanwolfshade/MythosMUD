"""
Unit tests for room utility functions.

Tests room-related operations including sub-zone extraction for Advanced Chat Channels.
"""

import pytest

from server.utils.room_utils import (
    extract_subzone_from_room_id,
    get_local_channel_subject,
    get_plane_from_room_id,
    get_subzone_local_channel_subject,
    get_zone_from_room_id,
    is_valid_room_id_format,
)


def test_extract_subzone_from_room_id_valid():
    """Test extract_subzone_from_room_id extracts sub-zone correctly."""
    room_id = "earth_arkhamcity_northside_intersection_derby_high"
    result = extract_subzone_from_room_id(room_id)
    
    assert result == "northside"


def test_extract_subzone_from_room_id_different_subzone():
    """Test extract_subzone_from_room_id extracts different sub-zone."""
    room_id = "earth_arkhamcity_downtown_market_square"
    result = extract_subzone_from_room_id(room_id)
    
    assert result == "downtown"


def test_extract_subzone_from_room_id_empty():
    """Test extract_subzone_from_room_id returns None for empty string."""
    result = extract_subzone_from_room_id("")
    
    assert result is None


def test_extract_subzone_from_room_id_none():
    """Test extract_subzone_from_room_id handles None."""
    result = extract_subzone_from_room_id(None)
    
    assert result is None


def test_extract_subzone_from_room_id_invalid_format():
    """Test extract_subzone_from_room_id returns None for invalid format."""
    result = extract_subzone_from_room_id("invalid_room_id")
    
    assert result is None


def test_extract_subzone_from_room_id_too_few_parts():
    """Test extract_subzone_from_room_id returns None for too few parts."""
    result = extract_subzone_from_room_id("earth_arkhamcity_northside")
    
    assert result is None


def test_get_zone_from_room_id_valid():
    """Test get_zone_from_room_id extracts zone correctly."""
    room_id = "earth_arkhamcity_northside_intersection_derby_high"
    result = get_zone_from_room_id(room_id)
    
    assert result == "arkhamcity"


def test_get_zone_from_room_id_different_zone():
    """Test get_zone_from_room_id extracts different zone."""
    room_id = "earth_innsmouth_docks_warehouse_1"
    result = get_zone_from_room_id(room_id)
    
    assert result == "innsmouth"


def test_get_zone_from_room_id_empty():
    """Test get_zone_from_room_id returns None for empty string."""
    result = get_zone_from_room_id("")
    
    assert result is None


def test_get_zone_from_room_id_invalid_format():
    """Test get_zone_from_room_id returns None for invalid format."""
    result = get_zone_from_room_id("invalid_room_id")
    
    assert result is None


def test_get_plane_from_room_id_valid():
    """Test get_plane_from_room_id extracts plane correctly."""
    room_id = "earth_arkhamcity_northside_intersection_derby_high"
    result = get_plane_from_room_id(room_id)
    
    assert result == "earth"


def test_get_plane_from_room_id_different_plane():
    """Test get_plane_from_room_id extracts different plane."""
    room_id = "dream_innsmouth_docks_warehouse_1"
    result = get_plane_from_room_id(room_id)
    
    assert result == "dream"


def test_get_plane_from_room_id_empty():
    """Test get_plane_from_room_id returns None for empty string."""
    result = get_plane_from_room_id("")
    
    assert result is None


def test_get_plane_from_room_id_invalid_format():
    """Test get_plane_from_room_id returns None for invalid format."""
    result = get_plane_from_room_id("invalid_room_id")
    
    assert result is None


def test_is_valid_room_id_format_valid():
    """Test is_valid_room_id_format returns True for valid format."""
    room_id = "earth_arkhamcity_northside_intersection_derby_high"
    result = is_valid_room_id_format(room_id)
    
    assert result is True


def test_is_valid_room_id_format_invalid():
    """Test is_valid_room_id_format returns False for invalid format."""
    room_id = "invalid_room_id"
    result = is_valid_room_id_format(room_id)
    
    assert result is False


def test_is_valid_room_id_format_empty():
    """Test is_valid_room_id_format returns False for empty string."""
    result = is_valid_room_id_format("")
    
    assert result is False


def test_is_valid_room_id_format_too_few_parts():
    """Test is_valid_room_id_format returns False for too few parts."""
    result = is_valid_room_id_format("earth_arkhamcity_northside")
    
    assert result is False


def test_get_local_channel_subject_valid():
    """Test get_local_channel_subject generates subject for valid room ID."""
    room_id = "earth_arkhamcity_northside_intersection_derby_high"
    result = get_local_channel_subject(room_id)
    
    assert result == "chat.local.earth_arkhamcity_northside_intersection_derby_high"


def test_get_local_channel_subject_invalid():
    """Test get_local_channel_subject returns None for invalid room ID."""
    result = get_local_channel_subject("invalid_room_id")
    
    assert result is None


def test_get_local_channel_subject_deprecation_warning():
    """Test get_local_channel_subject emits deprecation warning."""
    import warnings
    
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        get_local_channel_subject("earth_arkhamcity_northside_intersection_derby_high")
        
        assert len(w) == 1
        assert issubclass(w[0].category, DeprecationWarning)
        assert "deprecated" in str(w[0].message).lower()


def test_get_subzone_local_channel_subject_valid():
    """Test get_subzone_local_channel_subject generates subject for valid room ID."""
    room_id = "earth_arkhamcity_northside_intersection_derby_high"
    result = get_subzone_local_channel_subject(room_id)
    
    assert result == "chat.local.subzone.northside"


def test_get_subzone_local_channel_subject_different_subzone():
    """Test get_subzone_local_channel_subject generates subject for different subzone."""
    room_id = "earth_arkhamcity_downtown_market_square"
    result = get_subzone_local_channel_subject(room_id)
    
    assert result == "chat.local.subzone.downtown"


def test_get_subzone_local_channel_subject_invalid():
    """Test get_subzone_local_channel_subject returns None for invalid room ID."""
    result = get_subzone_local_channel_subject("invalid_room_id")
    
    assert result is None


def test_get_subzone_local_channel_subject_empty():
    """Test get_subzone_local_channel_subject returns None for empty string."""
    result = get_subzone_local_channel_subject("")
    
    assert result is None
