"""
Tests for room utility functions.

This module tests the room utility functions for sub-zone extraction
and NATS subject generation for the Advanced Chat Channels feature.
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


class TestRoomUtils:
    """Test room utility functions."""

    def test_extract_subzone_from_room_id_valid(self) -> None:
        """Test extracting sub-zone from valid room IDs."""
        # Test northside
        room_id = "earth_arkhamcity_northside_intersection_derby_high"
        subzone = extract_subzone_from_room_id(room_id)
        assert subzone == "northside"

        # Test downtown
        room_id = "earth_arkhamcity_downtown_market_square"
        subzone = extract_subzone_from_room_id(room_id)
        assert subzone == "downtown"

        # Test campus
        room_id = "earth_arkhamcity_campus_library_main"
        subzone = extract_subzone_from_room_id(room_id)
        assert subzone == "campus"

        # Test different zone
        room_id = "earth_innsmouth_docks_warehouse_1"
        subzone = extract_subzone_from_room_id(room_id)
        assert subzone == "docks"

    def test_extract_subzone_from_room_id_invalid(self) -> None:
        """Test extracting sub-zone from invalid room IDs."""
        # Invalid format
        assert extract_subzone_from_room_id("invalid_room_id") is None

        # Empty string
        assert extract_subzone_from_room_id("") is None

        # None
        assert extract_subzone_from_room_id(None) is None  # type: ignore[arg-type]

        # Too few parts
        assert extract_subzone_from_room_id("earth_arkham") is None
        assert extract_subzone_from_room_id("earth_arkhamcity") is None

    def test_get_zone_from_room_id_valid(self) -> None:
        """Test extracting zone from valid room IDs."""
        # Test arkhamcity
        room_id = "earth_arkhamcity_northside_intersection_derby_high"
        zone = get_zone_from_room_id(room_id)
        assert zone == "arkhamcity"

        # Test different zone
        room_id = "earth_innsmouth_docks_warehouse_1"
        zone = get_zone_from_room_id(room_id)
        assert zone == "innsmouth"

    def test_get_zone_from_room_id_invalid(self) -> None:
        """Test extracting zone from invalid room IDs."""
        # Invalid format
        assert get_zone_from_room_id("invalid_room_id") is None

        # Empty string
        assert get_zone_from_room_id("") is None

        # None
        assert get_zone_from_room_id(None) is None  # type: ignore[arg-type]

        # Too few parts
        assert get_zone_from_room_id("earth") is None
        assert get_zone_from_room_id("earth_arkham") is None

    def test_get_plane_from_room_id_valid(self) -> None:
        """Test extracting plane from valid room IDs."""
        # Test earth plane
        room_id = "earth_arkhamcity_northside_intersection_derby_high"
        plane = get_plane_from_room_id(room_id)
        assert plane == "earth"

        # Test dream plane
        room_id = "dream_innsmouth_docks_warehouse_1"
        plane = get_plane_from_room_id(room_id)
        assert plane == "dream"

    def test_get_plane_from_room_id_invalid(self) -> None:
        """Test extracting plane from invalid room IDs."""
        # Invalid format
        assert get_plane_from_room_id("invalid_room_id") is None

        # Empty string
        assert get_plane_from_room_id("") is None

        # None
        assert get_plane_from_room_id(None) is None  # type: ignore[arg-type]

    def test_is_valid_room_id_format_valid(self) -> None:
        """Test room ID format validation with valid IDs."""
        # Valid room IDs
        assert is_valid_room_id_format("earth_arkhamcity_northside_intersection_derby_high") is True
        assert is_valid_room_id_format("earth_innsmouth_docks_warehouse_1") is True
        assert is_valid_room_id_format("dream_arkhamcity_downtown_market_square") is True

        # Room IDs with more parts are also valid
        assert is_valid_room_id_format("earth_arkhamcity_northside_intersection_derby_high_street") is True

    def test_is_valid_room_id_format_invalid(self) -> None:
        """Test room ID format validation with invalid IDs."""
        # Invalid room IDs
        assert is_valid_room_id_format("invalid_room_id") is False
        assert is_valid_room_id_format("earth_arkham") is False
        assert is_valid_room_id_format("earth_arkhamcity") is False

        # Empty string
        assert is_valid_room_id_format("") is False

        # None
        assert is_valid_room_id_format(None) is False  # type: ignore[arg-type]

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_get_local_channel_subject_valid(self) -> None:
        """Test generating local channel NATS subjects with valid room IDs."""
        room_id = "earth_arkhamcity_northside_intersection_derby_high"
        subject = get_local_channel_subject(room_id)
        assert subject == "chat.local.earth_arkhamcity_northside_intersection_derby_high"

        room_id = "earth_innsmouth_docks_warehouse_1"
        subject = get_local_channel_subject(room_id)
        assert subject == "chat.local.earth_innsmouth_docks_warehouse_1"

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_get_local_channel_subject_invalid(self) -> None:
        """Test generating local channel NATS subjects with invalid room IDs."""
        # Invalid room IDs should return None
        assert get_local_channel_subject("invalid_room_id") is None
        assert get_local_channel_subject("") is None
        assert get_local_channel_subject(None) is None  # type: ignore[arg-type]

    def test_get_subzone_local_channel_subject_valid(self) -> None:
        """Test generating sub-zone local channel NATS subjects with valid room IDs."""
        room_id = "earth_arkhamcity_northside_intersection_derby_high"
        subject = get_subzone_local_channel_subject(room_id)
        assert subject == "chat.local.subzone.northside"

        room_id = "earth_arkhamcity_downtown_market_square"
        subject = get_subzone_local_channel_subject(room_id)
        assert subject == "chat.local.subzone.downtown"

        room_id = "earth_innsmouth_docks_warehouse_1"
        subject = get_subzone_local_channel_subject(room_id)
        assert subject == "chat.local.subzone.docks"

    def test_get_subzone_local_channel_subject_invalid(self) -> None:
        """Test generating sub-zone local channel NATS subjects with invalid room IDs."""
        # Invalid room IDs should return None
        assert get_subzone_local_channel_subject("invalid_room_id") is None
        assert get_subzone_local_channel_subject("") is None
        assert get_subzone_local_channel_subject(None) is None  # type: ignore[arg-type]

    def test_room_id_parsing_edge_cases(self) -> None:
        """Test edge cases for room ID parsing."""
        # Room ID with underscores in sub-zone name
        room_id = "earth_arkhamcity_old_town_tavern_main"
        subzone = extract_subzone_from_room_id(room_id)
        assert subzone == "old"

        # Room ID with underscores in zone name
        room_id = "earth_old_innsmouth_docks_warehouse_1"
        zone = get_zone_from_room_id(room_id)
        assert zone == "old"

        # Room ID with many parts
        room_id = "earth_arkhamcity_northside_intersection_derby_high_street_corner"
        subzone = extract_subzone_from_room_id(room_id)
        assert subzone == "northside"
        zone = get_zone_from_room_id(room_id)
        assert zone == "arkhamcity"
        plane = get_plane_from_room_id(room_id)
        assert plane == "earth"

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_nats_subject_generation_consistency(self) -> None:
        """Test that NATS subject generation is consistent."""
        room_id = "earth_arkhamcity_northside_intersection_derby_high"

        # Local channel subject should include the full room ID
        local_subject = get_local_channel_subject(room_id)
        assert local_subject == "chat.local.earth_arkhamcity_northside_intersection_derby_high"

        # Sub-zone subject should only include the sub-zone
        subzone_subject = get_subzone_local_channel_subject(room_id)
        assert subzone_subject == "chat.local.subzone.northside"

        # Both should be different
        assert local_subject != subzone_subject
