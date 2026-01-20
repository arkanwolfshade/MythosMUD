"""
Unit tests for schedule service.

Tests the ScheduleService class for managing NPC and environmental schedules.
"""

from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from server.schemas.calendar import ScheduleEntry
from server.services.schedule_service import ScheduleService


class TestScheduleService:
    """Test suite for ScheduleService class."""

    def test_init_with_collections(self):
        """Test ScheduleService initialization with collections parameter."""
        collections = []
        service = ScheduleService(collections=collections, environment="test")
        assert not service.entries
        # Accessing protected member to verify initialization state
        assert service._environment == "test"  # pylint: disable=protected-access

    def test_init_without_persistence_raises(self):
        """Test ScheduleService initialization without persistence raises ValueError."""
        with pytest.raises(ValueError, match="async_persistence is required"):
            ScheduleService(environment="test")

    @patch("server.services.schedule_service.get_calendar_paths_for_environment")
    def test_init_loads_from_database(self, mock_get_paths):
        """Test ScheduleService loads entries from database."""
        mock_get_paths.return_value = (Path("/holidays"), Path("/schedules"))
        mock_persistence = MagicMock()

        # Mock the database loading
        with patch.object(ScheduleService, "_load_from_database") as mock_load:
            mock_load.return_value = [
                ScheduleEntry(
                    id="test_schedule_1",
                    name="Test Schedule",
                    category="npc",
                    start_hour=9,
                    end_hour=17,
                    days=["Monday", "Tuesday"],
                    applies_to=[],
                    effects=[],
                    notes="Test notes",
                )
            ]
            service = ScheduleService(async_persistence=mock_persistence, environment="test")
            assert len(service.entries) == 1
            assert service.entries[0].id == "test_schedule_1"

    def test_get_active_entries_no_matches(self):
        """Test get_active_entries returns empty list when no matches."""
        service = ScheduleService(collections=[], environment="test")
        mythos_dt = datetime(2024, 1, 1, 12, 0, 0)  # Monday, noon
        active = service.get_active_entries(mythos_dt=mythos_dt, day_name="Monday")
        assert active == []

    def test_get_active_entries_with_matches(self):
        """Test get_active_entries returns matching entries."""
        entry1 = ScheduleEntry(
            id="schedule_1",
            name="Morning Schedule",
            category="npc",
            start_hour=9,
            end_hour=12,
            days=["Monday"],
            applies_to=[],
            effects=[],
            notes="",
        )
        entry2 = ScheduleEntry(
            id="schedule_2",
            name="Afternoon Schedule",
            category="npc",
            start_hour=12,
            end_hour=17,
            days=["Monday"],
            applies_to=[],
            effects=[],
            notes="",
        )
        service = ScheduleService(collections=[], environment="test")
        # Accessing protected member to inject test data
        service._entries = [entry1, entry2]  # pylint: disable=protected-access

        # Test at 10:00 (should match entry1)
        mythos_dt = datetime(2024, 1, 1, 10, 0, 0)  # Monday, 10 AM
        active = service.get_active_entries(mythos_dt=mythos_dt, day_name="Monday")
        assert len(active) == 1
        assert active[0].id == "schedule_1"

        # Test at 15:00 (should match entry2)
        mythos_dt = datetime(2024, 1, 1, 15, 0, 0)  # Monday, 3 PM
        active = service.get_active_entries(mythos_dt=mythos_dt, day_name="Monday")
        assert len(active) == 1
        assert active[0].id == "schedule_2"

    def test_get_active_entries_boundary_conditions(self):
        """Test get_active_entries handles boundary conditions correctly."""
        entry = ScheduleEntry(
            id="schedule_1",
            name="Boundary Schedule",
            category="npc",
            start_hour=9,
            end_hour=17,
            days=["Monday"],
            applies_to=[],
            effects=[],
            notes="",
        )
        service = ScheduleService(collections=[], environment="test")
        # Accessing protected member to inject test data
        service._entries = [entry]  # pylint: disable=protected-access

        # Test at start hour (should match)
        mythos_dt = datetime(2024, 1, 1, 9, 0, 0)
        active = service.get_active_entries(mythos_dt=mythos_dt, day_name="Monday")
        assert len(active) == 1

        # Test at end hour (should NOT match - end is exclusive)
        mythos_dt = datetime(2024, 1, 1, 17, 0, 0)
        active = service.get_active_entries(mythos_dt=mythos_dt, day_name="Monday")
        assert len(active) == 0

        # Test just before end hour (should match)
        mythos_dt = datetime(2024, 1, 1, 16, 59, 0)
        active = service.get_active_entries(mythos_dt=mythos_dt, day_name="Monday")
        assert len(active) == 1

    def test_get_active_entries_wrong_day(self):
        """Test get_active_entries returns empty for wrong day."""
        entry = ScheduleEntry(
            id="schedule_1",
            name="Monday Schedule",
            category="npc",
            start_hour=9,
            end_hour=17,
            days=["Monday"],
            applies_to=[],
            effects=[],
            notes="",
        )
        service = ScheduleService(collections=[], environment="test")
        # Accessing protected member to inject test data
        service._entries = [entry]  # pylint: disable=protected-access

        mythos_dt = datetime(2024, 1, 1, 12, 0, 0)  # Monday, but querying Tuesday
        active = service.get_active_entries(mythos_dt=mythos_dt, day_name="Tuesday")
        assert active == []

    def test_entries_property(self):
        """Test entries property returns copy of entries list."""
        entry = ScheduleEntry(
            id="schedule_1",
            name="Test Schedule",
            category="npc",
            start_hour=9,
            end_hour=17,
            days=["Monday"],
            applies_to=[],
            effects=[],
            notes="",
        )
        service = ScheduleService(collections=[], environment="test")
        # Accessing protected member to inject test data
        service._entries = [entry]  # pylint: disable=protected-access

        entries = service.entries
        assert entries == [entry]
        # Verify it's a copy, not the same list
        # Accessing protected member to verify property returns a copy
        assert entries is not service._entries  # pylint: disable=protected-access

    def test_entry_count_property(self):
        """Test entry_count property returns count."""
        entry1 = ScheduleEntry(
            id="schedule_1",
            name="Schedule 1",
            category="npc",
            start_hour=9,
            end_hour=17,
            days=["Monday"],
            applies_to=[],
            effects=[],
            notes="",
        )
        entry2 = ScheduleEntry(
            id="schedule_2",
            name="Schedule 2",
            category="npc",
            start_hour=9,
            end_hour=17,
            days=["Tuesday"],
            applies_to=[],
            effects=[],
            notes="",
        )
        service = ScheduleService(collections=[], environment="test")
        # Accessing protected member to inject test data
        service._entries = [entry1, entry2]  # pylint: disable=protected-access
        assert service.entry_count == 2
