"""
Unit tests for schedule service.

Tests the ScheduleService class for managing NPC and environmental schedules.
"""

from datetime import datetime
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.schemas.calendar import ScheduleCollection, ScheduleEntry
from server.services.schedule_service import (
    ScheduleService,
    _DatabaseLoadResult,
    normalize_weekday_names,
)

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions

# pyright: reportPrivateUsage=false
# Reason: unit tests patch and assert ScheduleService private state by design.


class TestScheduleService:
    """Test suite for ScheduleService class."""

    def test_init_with_collections(self):
        """Test ScheduleService initialization with collections parameter."""
        collections: list[tuple[Path, ScheduleCollection]] = []
        service = ScheduleService(collections=collections, environment="test")
        assert not service.entries
        # Accessing protected member to verify initialization state
        assert service._environment == "test"

    def test_init_without_persistence_raises(self):
        """Test ScheduleService initialization without persistence raises ValueError."""
        with pytest.raises(ValueError, match="async_persistence is required"):
            _ = ScheduleService(environment="test")

    @pytest.mark.asyncio
    async def test_async_load_from_database_passes_search_path_for_mythos_e2e(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Regression: tables live in schema mythos_e2e; raw asyncpg must set search_path like SQLAlchemy."""
        monkeypatch.setenv(
            "DATABASE_URL",
            "postgresql+asyncpg://postgres:secret@127.0.0.1:5432/mythos_e2e",
        )
        monkeypatch.delenv("POSTGRES_SEARCH_PATH", raising=False)

        settings_seen: dict[str, object] = {}

        mock_conn = MagicMock()
        mock_conn.fetch = AsyncMock(return_value=[])
        mock_conn.close = AsyncMock()

        async def fake_connect(url: str, *, server_settings: dict[str, str] | None = None) -> MagicMock:
            settings_seen["url"] = url
            settings_seen["server_settings"] = server_settings
            return mock_conn

        monkeypatch.setattr("server.services.schedule_service.asyncpg.connect", fake_connect)

        svc = object.__new__(ScheduleService)
        result_container: _DatabaseLoadResult = {"entries": None, "error": None}
        await ScheduleService._async_load_from_database(svc, result_container)

        assert result_container.get("error") is None
        assert settings_seen["server_settings"] == {"search_path": "mythos_e2e"}

    @patch("server.services.schedule_service.get_calendar_paths_for_environment")
    def test_init_loads_from_database(self, mock_get_paths: MagicMock) -> None:
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
            assert len(service.entries) == 1  # nosec B101  # Reason: pytest uses assert statements for test assertions
            assert service.entries[0].id == "test_schedule_1"  # nosec B101  # Reason: pytest uses assert statements for test assertions

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
        assert entries == [entry]  # nosec B101  # Reason: pytest uses assert statements for test assertions
        # Verify it's a copy, not the same list
        # Accessing protected member to verify property returns a copy
        assert entries is not service._entries  # pylint: disable=protected-access  # nosec B101  # Reason: pytest uses assert statements for test assertions

    def test_normalize_weekday_names_latin_to_standard(self):
        """Latin weekday names from DB are normalized to standard names (regression for errors.log)."""
        assert normalize_weekday_names(["Primus", "Sextus"]) == ["Monday", "Saturday"]
        assert normalize_weekday_names(["Primus", "Secundus", "Tertius", "Quartus", "Quintus", "Sextus"]) == [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]
        assert normalize_weekday_names(["Monday", "Tuesday"]) == ["Monday", "Tuesday"]
        # ScheduleEntry accepts normalized days
        entry = ScheduleEntry(
            id="test_latin",
            name="Test",
            category="npc",
            start_hour=0,
            end_hour=24,
            days=normalize_weekday_names(["Primus", "Sextus"]),
            applies_to=[],
            effects=[],
            notes=None,
        )
        assert entry.days == ["Monday", "Saturday"]

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
