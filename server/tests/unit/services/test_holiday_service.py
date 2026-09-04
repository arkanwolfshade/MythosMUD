"""
Unit tests for holiday service.

Tests the HolidayService class for tracking active Mythos holidays.
"""

from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.schemas.calendar import HolidayCollection, HolidayEntry
from server.services.holiday_service import (
    HolidayService,
    _ensure_utc,
    _holiday_entry_from_row,
    _string_list_from_row,
)


class TestHolidayService:
    """Test suite for HolidayService class."""

    @pytest.fixture
    def mock_chronicle(self):
        """Create a mock chronicle for testing."""
        chronicle = MagicMock()
        chronicle.get_current_mythos_datetime.return_value = datetime(2024, 1, 15, 12, 0, 0, tzinfo=UTC)
        return chronicle

    @pytest.fixture
    def sample_holidays(self):
        """Create sample holiday entries for testing."""
        return [
            HolidayEntry(
                id="new_year",
                name="New Year's Day",
                tradition="mythos",
                month=1,
                day=1,
                duration_hours=24,
                season="winter",
                bonus_tags=[],
            ),
            HolidayEntry(
                id="midwinter",
                name="Midwinter Festival",
                tradition="mythos",
                month=1,
                day=15,
                duration_hours=48,
                season="winter",
                bonus_tags=["celebration"],
            ),
            HolidayEntry(
                id="spring_equinox",
                name="Spring Equinox",
                tradition="mythos",
                month=3,
                day=20,
                duration_hours=24,
                season="spring",
                bonus_tags=[],
            ),
        ]

    def test_init_with_collection(self, mock_chronicle, sample_holidays):
        """Test HolidayService initialization with collection parameter."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")
        assert len(service._collection.holidays) == 3
        assert service._environment == "test"

    def test_init_without_persistence_raises(self, mock_chronicle):
        """Test HolidayService initialization without persistence raises ValueError."""
        with pytest.raises(ValueError, match="async_persistence is required"):
            HolidayService(chronicle=mock_chronicle, environment="test")

    @patch("server.services.holiday_service.get_calendar_paths_for_environment")
    def test_init_loads_from_database(self, mock_get_paths, mock_chronicle):
        """Test HolidayService loads holidays from database."""
        mock_get_paths.return_value = (Path("/holidays"), Path("/schedules"))
        mock_persistence = MagicMock()

        # Mock the database loading
        with patch.object(HolidayService, "_load_from_database") as mock_load:
            sample_holidays = [
                HolidayEntry(
                    id="test_holiday",
                    name="Test Holiday",
                    tradition="mythos",
                    month=1,
                    day=1,
                    duration_hours=24,
                    season="winter",
                    bonus_tags=[],
                )
            ]
            collection = HolidayCollection(holidays=sample_holidays)
            mock_load.return_value = collection
            service = HolidayService(chronicle=mock_chronicle, async_persistence=mock_persistence, environment="test")
            assert len(service._collection.holidays) == 1
            assert service._collection.holidays[0].id == "test_holiday"

    def test_refresh_active_activates_matching_holiday(self, mock_chronicle, sample_holidays):
        """Test refresh_active activates holidays matching current date."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")

        # Set current date to January 15 (matches midwinter)
        mythos_dt = datetime(2024, 1, 15, 12, 0, 0, tzinfo=UTC)
        active = service.refresh_active(mythos_dt=mythos_dt)

        assert len(active) == 1
        assert active[0].id == "midwinter"
        assert service._last_refresh == mythos_dt

    def test_refresh_active_no_matches(self, mock_chronicle, sample_holidays):
        """Test refresh_active returns empty when no holidays match."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")

        # Set current date to February 1 (no matches)
        mythos_dt = datetime(2024, 2, 1, 12, 0, 0, tzinfo=UTC)
        active = service.refresh_active(mythos_dt=mythos_dt)

        assert len(active) == 0

    def test_refresh_active_expires_old_holidays(self, mock_chronicle, sample_holidays):
        """Test refresh_active expires holidays past their duration."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")

        # Activate a holiday
        start_time = datetime(2024, 1, 15, 0, 0, 0, tzinfo=UTC)
        service._active_started["midwinter"] = start_time

        # Refresh after holiday has expired (48 hours + 1 hour)
        expired_time = start_time + timedelta(hours=49)
        active = service.refresh_active(mythos_dt=expired_time)

        assert len(active) == 0
        assert "midwinter" not in service._active_started

    def test_refresh_active_caps_duration(self, mock_chronicle, sample_holidays):
        """Test refresh_active caps holiday duration at 48 hours."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")

        # Use midwinter which has 48 hours duration
        # Activate the holiday
        start_time = datetime(2024, 1, 15, 0, 0, 0, tzinfo=UTC)
        service._active_started["midwinter"] = start_time

        # Refresh after 49 hours (should be expired due to 48-hour cap)
        expired_time = start_time + timedelta(hours=49)
        active = service.refresh_active(mythos_dt=expired_time)

        assert len(active) == 0
        assert "midwinter" not in service._active_started

    def test_get_active_holidays(self, mock_chronicle, sample_holidays):
        """Test get_active_holidays returns currently active holidays."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")

        # Manually set active holidays
        service._active_started["new_year"] = datetime(2024, 1, 1, 0, 0, 0, tzinfo=UTC)
        service._active_started["midwinter"] = datetime(2024, 1, 15, 0, 0, 0, tzinfo=UTC)

        active = service.get_active_holidays()
        assert len(active) == 2
        assert {h.id for h in active} == {"new_year", "midwinter"}

    def test_get_active_holiday_names(self, mock_chronicle, sample_holidays):
        """Test get_active_holiday_names returns names of active holidays."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")

        service._active_started["new_year"] = datetime(2024, 1, 1, 0, 0, 0, tzinfo=UTC)
        names = service.get_active_holiday_names()
        assert "New Year's Day" in names

    def test_get_upcoming_holidays(self, mock_chronicle, sample_holidays):
        """Test get_upcoming_holidays returns next N holidays."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")

        # Set current date to January 10
        current_dt = datetime(2024, 1, 10, 12, 0, 0, tzinfo=UTC)
        upcoming = service.get_upcoming_holidays(count=2, start_dt=current_dt)

        assert len(upcoming) == 2
        # Should include midwinter (Jan 15) and spring_equinox (Mar 20)
        assert upcoming[0].id == "midwinter"
        assert upcoming[1].id == "spring_equinox"

    def test_get_upcoming_holidays_wraps_around(self, mock_chronicle, sample_holidays):
        """Test get_upcoming_holidays wraps around calendar."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")

        # Set current date to March 25 (after all holidays)
        current_dt = datetime(2024, 3, 25, 12, 0, 0, tzinfo=UTC)
        upcoming = service.get_upcoming_holidays(count=2, start_dt=current_dt)

        assert len(upcoming) == 2
        # Should wrap around to next year's holidays

    def test_get_upcoming_summary(self, mock_chronicle, sample_holidays):
        """Test get_upcoming_summary returns formatted strings."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")

        summary = service.get_upcoming_summary(count=1)

        assert len(summary) == 1
        assert "01/15" in summary[0] or "03/20" in summary[0]  # Should contain one of the upcoming dates

    def test_day_ordinal(self, mock_chronicle, sample_holidays):
        """Test _day_ordinal converts month/day to ordinal."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")

        # January 1 should be ordinal 1
        assert service._day_ordinal(1, 1) == 1
        # January 15 should be ordinal 15
        assert service._day_ordinal(1, 15) == 15
        # March 20 should be ordinal (2 * 30) + 20 = 80
        assert service._day_ordinal(3, 20) == 80

    def test_collection_property(self, mock_chronicle, sample_holidays):
        """Test collection property returns the collection."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")
        assert service.collection == collection

    def test_last_refresh_property(self, mock_chronicle, sample_holidays):
        """Test last_refresh property returns last refresh time."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")
        assert service.last_refresh is None

        mythos_dt = datetime(2024, 1, 15, 12, 0, 0, tzinfo=UTC)
        service.refresh_active(mythos_dt=mythos_dt)
        assert service.last_refresh == mythos_dt

    def test_ensure_utc_naive_and_aware(self):
        """Naive datetimes gain UTC; aware datetimes convert to UTC."""
        naive = datetime(2024, 1, 1, 12, 0, 0)
        aware = datetime(2024, 1, 1, 12, 0, 0, tzinfo=UTC)
        assert _ensure_utc(naive).tzinfo == UTC
        assert _ensure_utc(aware).tzinfo == UTC

    def test_string_list_from_row(self):
        """Helper normalizes nullable PostgreSQL array columns."""
        assert _string_list_from_row(None) == []
        assert _string_list_from_row(42) == []
        assert _string_list_from_row(["tag"]) == ["tag"]

    def test_holiday_entry_from_row(self):
        """Row dict maps to HolidayEntry."""
        row = {
            "stable_id": "fest",
            "name": "Festival",
            "tradition": "mythos",
            "month": 3,
            "day": 20,
            "duration_hours": 24,
            "season": "spring",
            "bonus_tags": ["celebration"],
        }
        entry = _holiday_entry_from_row(row)
        assert entry.id == "fest"
        assert entry.bonus_tags == ["celebration"]

    def test_get_serialized_active_holidays(self, mock_chronicle, sample_holidays):
        """Serialized active holidays delegate to refresh_active."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")
        mythos_dt = datetime(2024, 1, 15, 12, 0, 0, tzinfo=UTC)
        active = service.get_serialized_active_holidays(mythos_dt)
        assert len(active) == 1
        assert active[0].id == "midwinter"

    def test_get_serialized_upcoming_holidays(self, mock_chronicle, sample_holidays):
        """Serialized upcoming holidays delegate to get_upcoming_holidays."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")
        upcoming = service.get_serialized_upcoming_holidays(count=2)
        assert len(upcoming) == 2

    def test_refresh_active_removes_unknown_holiday_id(self, mock_chronicle, sample_holidays):
        """Stale active IDs not in collection are removed during refresh."""
        collection = HolidayCollection(holidays=sample_holidays)
        service = HolidayService(chronicle=mock_chronicle, collection=collection, environment="test")
        service._active_started["orphan_id"] = datetime(2024, 1, 15, 0, 0, 0, tzinfo=UTC)
        mythos_dt = datetime(2024, 1, 15, 12, 0, 0, tzinfo=UTC)
        active = service.refresh_active(mythos_dt=mythos_dt)
        assert "orphan_id" not in service._active_started
        assert len(active) == 1

    @pytest.mark.asyncio
    async def test_async_load_from_database(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Regression: asyncpg load builds HolidayCollection from rows."""
        monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://postgres:secret@127.0.0.1:5432/mythos_unit")
        mock_conn = MagicMock()
        mock_conn.fetch = AsyncMock(
            return_value=[
                {
                    "stable_id": "db_holiday",
                    "name": "DB Holiday",
                    "tradition": "mythos",
                    "month": 1,
                    "day": 2,
                    "duration_hours": 12,
                    "season": "winter",
                    "bonus_tags": [],
                }
            ]
        )
        mock_conn.close = AsyncMock()

        async def fake_connect(url: str, *, server_settings: dict[str, str] | None = None) -> MagicMock:
            return mock_conn

        monkeypatch.setattr("server.services.holiday_service.asyncpg.connect", fake_connect)

        svc = object.__new__(HolidayService)
        result_container: dict[str, object] = {"collection": None, "error": None}
        await HolidayService._async_load_from_database(svc, result_container)  # type: ignore[arg-type]
        collection = result_container["collection"]
        assert isinstance(collection, HolidayCollection)
        assert collection.holidays[0].id == "db_holiday"
