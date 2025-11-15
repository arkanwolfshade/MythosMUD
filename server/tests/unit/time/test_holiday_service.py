from __future__ import annotations

from datetime import UTC, datetime, timedelta

from server.schemas.calendar import HolidayCollection, HolidayEntry
from server.services.holiday_service import HolidayService


class StubChronicle:
    def __init__(self, dt: datetime) -> None:
        self._dt = dt

    def get_current_mythos_datetime(self) -> datetime:
        return self._dt


def _collection() -> HolidayCollection:
    return HolidayCollection(
        holidays=[
            HolidayEntry(
                id="innsmouth_tide_offering",
                name="Innsmouth Tide Offering",
                tradition="mythos",
                month=3,
                day=3,
                duration_hours=24,
                season="spring",
                bonus_tags=["oceanic"],
            ),
            HolidayEntry(
                id="feast_of_yig",
                name="Feast of Yig",
                tradition="mythos",
                month=3,
                day=5,
                duration_hours=48,
                season="spring",
                bonus_tags=["serpent"],
            ),
        ]
    )


def test_holiday_refresh_and_expiration() -> None:
    chronicle = StubChronicle(datetime(1930, 3, 3, 10, tzinfo=UTC))
    service = HolidayService(chronicle=chronicle, collection=_collection(), data_path="unused")

    active = service.refresh_active(chronicle.get_current_mythos_datetime())
    assert [entry.id for entry in active] == ["innsmouth_tide_offering"]

    # Advance beyond 48 hours so even extended holidays expire
    later = chronicle.get_current_mythos_datetime() + timedelta(hours=50)
    service.refresh_active(later)
    assert service.get_active_holiday_names() == ["Feast of Yig"]


def test_upcoming_summary_rolls_over_calendar() -> None:
    chronicle = StubChronicle(datetime(1930, 3, 6, 1, tzinfo=UTC))
    service = HolidayService(chronicle=chronicle, collection=_collection(), data_path="unused")
    summary = service.get_upcoming_summary(2)
    assert "Innsmouth Tide Offering" in summary[0]
