"""
Unit tests for calendar schemas.

Tests the Pydantic models in calendar.py module.
"""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from pydantic import ValidationError

from server.schemas.calendar import (
    HolidayCollection,
    HolidayEntry,
    ScheduleCollection,
    ScheduleEntry,
    extract_observance_ids,
    slugify_observance,
)


def test_holiday_entry():
    """Test HolidayEntry can be instantiated."""
    holiday = HolidayEntry(
        id="test_holiday",
        name="Test Holiday",
        tradition="mythos",
        month=1,
        day=1,
        season="winter",
    )

    assert holiday.id == "test_holiday"
    assert holiday.name == "Test Holiday"
    assert holiday.tradition == "mythos"
    assert holiday.month == 1
    assert holiday.day == 1
    assert holiday.season == "winter"
    assert holiday.duration_hours == 24
    assert holiday.bonus_tags == []


def test_holiday_entry_validation_tradition():
    """Test HolidayEntry validates tradition."""
    with pytest.raises(ValidationError):
        HolidayEntry(
            id="test_holiday",
            name="Test Holiday",
            tradition="invalid",
            month=1,
            day=1,
            season="winter",
        )


def test_holiday_entry_validation_season():
    """Test HolidayEntry validates season."""
    with pytest.raises(ValidationError):
        HolidayEntry(
            id="test_holiday",
            name="Test Holiday",
            tradition="mythos",
            month=1,
            day=1,
            season="invalid",
        )


def test_holiday_entry_validation_bonus_tags():
    """Test HolidayEntry validates bonus_tags format."""
    with pytest.raises(ValidationError):
        HolidayEntry(
            id="test_holiday",
            name="Test Holiday",
            tradition="mythos",
            month=1,
            day=1,
            season="winter",
            bonus_tags=["Invalid Tag"],
        )


def test_holiday_collection():
    """Test HolidayCollection can be instantiated."""
    holidays = [
        HolidayEntry(
            id="holiday1",
            name="Holiday 1",
            tradition="mythos",
            month=1,
            day=1,
            season="winter",
        ),
        HolidayEntry(
            id="holiday2",
            name="Holiday 2",
            tradition="catholic",
            month=12,
            day=25,
            season="winter",
        ),
    ]
    collection = HolidayCollection(holidays=holidays)

    assert len(collection.holidays) == 2
    assert "holiday1" in collection.id_map
    assert "holiday2" in collection.id_map


def test_holiday_collection_id_map():
    """Test HolidayCollection.id_map property."""
    holiday = HolidayEntry(
        id="test_holiday",
        name="Test Holiday",
        tradition="mythos",
        month=1,
        day=1,
        season="winter",
    )
    collection = HolidayCollection(holidays=[holiday])

    assert collection.id_map["test_holiday"] == holiday


def test_holiday_collection_load_file():
    """Test HolidayCollection.load_file() loads from JSON."""
    with TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "holidays.json"
        data = {
            "holidays": [
                {
                    "id": "test_holiday",
                    "name": "Test Holiday",
                    "tradition": "mythos",
                    "month": 1,
                    "day": 1,
                    "season": "winter",
                }
            ]
        }
        file_path.write_text(json.dumps(data), encoding="utf-8")

        collection = HolidayCollection.load_file(file_path)

        assert len(collection.holidays) == 1
        assert collection.holidays[0].id == "test_holiday"


def test_holiday_collection_ensure_unique_ids():
    """Test HolidayCollection.ensure_unique_ids() detects duplicates."""
    holidays = [
        HolidayEntry(
            id="duplicate",
            name="Holiday 1",
            tradition="mythos",
            month=1,
            day=1,
            season="winter",
        ),
        HolidayEntry(
            id="duplicate",
            name="Holiday 2",
            tradition="catholic",
            month=12,
            day=25,
            season="winter",
        ),
    ]
    collection = HolidayCollection(holidays=holidays)

    with pytest.raises(ValueError, match="Duplicate holiday ids"):
        collection.ensure_unique_ids()


def test_schedule_entry():
    """Test ScheduleEntry can be instantiated."""
    schedule = ScheduleEntry(
        id="test_schedule",
        name="Test Schedule",
        category="routine",
        start_hour=9,
        end_hour=17,
    )

    assert schedule.id == "test_schedule"
    assert schedule.name == "Test Schedule"
    assert schedule.category == "routine"
    assert schedule.start_hour == 9
    assert schedule.end_hour == 17
    assert schedule.days == []
    assert schedule.applies_to == []
    assert schedule.effects == []


def test_schedule_entry_validation_days():
    """Test ScheduleEntry validates days."""
    with pytest.raises(ValidationError):
        ScheduleEntry(
            id="test_schedule",
            name="Test Schedule",
            category="routine",
            start_hour=9,
            end_hour=17,
            days=["InvalidDay"],
        )


def test_schedule_collection():
    """Test ScheduleCollection can be instantiated."""
    schedules = [
        ScheduleEntry(
            id="schedule1",
            name="Schedule 1",
            category="routine",
            start_hour=9,
            end_hour=17,
        ),
    ]
    collection = ScheduleCollection(schedules=schedules)

    assert len(collection.schedules) == 1


def test_schedule_collection_load_file():
    """Test ScheduleCollection.load_file() loads from JSON."""
    with TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "schedule.json"
        data = {
            "schedules": [
                {
                    "id": "test_schedule",
                    "name": "Test Schedule",
                    "category": "routine",
                    "start_hour": 9,
                    "end_hour": 17,
                }
            ]
        }
        file_path.write_text(json.dumps(data), encoding="utf-8")

        collection = ScheduleCollection.load_file(file_path)

        assert len(collection.schedules) == 1
        assert collection.schedules[0].id == "test_schedule"


def test_slugify_observance():
    """Test slugify_observance() converts name to slug."""
    result = slugify_observance("Test Holiday Name")
    assert result == "test_holiday_name"


def test_extract_observance_ids():
    """Test extract_observance_ids() extracts IDs from markdown table lines."""
    lines = [
        "| Observance | Date |",
        "|------------|------|",
        "| Holiday Name 1 | 1/1 |",
        "| Holiday Name 2 | 12/25 |",
        "# comment",
        "",
    ]
    result = extract_observance_ids(lines)

    assert "holiday_name_1" in result
    assert "holiday_name_2" in result
