"""
Unit tests for calendar models.

Tests the HolidayModel and NPCScheduleModel SQLAlchemy models.
"""

from uuid import uuid4

from server.models.calendar import HolidayModel, NPCScheduleModel

# --- Tests for HolidayModel ---


def test_holiday_model_creation():
    """Test HolidayModel can be instantiated with required fields."""
    holiday_id = str(uuid4())
    holiday = HolidayModel(
        id=holiday_id,
        stable_id="test_holiday_001",
        name="Test Holiday",
        tradition="Mythos",
        month=10,
        day=31,
        duration_hours=24,
        season="autumn",
        bonus_tags=[],
    )

    assert holiday.id == holiday_id
    assert holiday.stable_id == "test_holiday_001"
    assert holiday.name == "Test Holiday"
    assert holiday.tradition == "Mythos"
    assert holiday.month == 10
    assert holiday.day == 31
    assert holiday.duration_hours == 24
    assert holiday.season == "autumn"
    assert holiday.bonus_tags == []


def test_holiday_model_with_bonus_tags():
    """Test HolidayModel can have bonus_tags."""
    holiday_id = str(uuid4())
    holiday = HolidayModel(
        id=holiday_id,
        stable_id="test_holiday_002",
        name="Festival",
        tradition="Ancient",
        month=6,
        day=21,
        duration_hours=48,
        season="summer",
        bonus_tags=["celebration", "feast"],
    )

    assert holiday.bonus_tags == ["celebration", "feast"]


def test_holiday_model_table_name():
    """Test HolidayModel has correct table name."""
    assert HolidayModel.__tablename__ == "calendar_holidays"


def test_holiday_model_repr():
    """Test HolidayModel __repr__ method."""
    holiday_id = str(uuid4())
    holiday = HolidayModel(
        id=holiday_id,
        stable_id="test_holiday_003",
        name="Test",
        tradition="Mythos",
        month=1,
        day=1,
        duration_hours=12,
        season="winter",
        bonus_tags=[],
    )

    repr_str = repr(holiday)
    assert "HolidayModel" in repr_str


# --- Tests for NPCScheduleModel ---


def test_npc_schedule_model_creation():
    """Test NPCScheduleModel can be instantiated with required fields."""
    schedule_id = str(uuid4())
    schedule = NPCScheduleModel(
        id=schedule_id,
        stable_id="test_schedule_001",
        name="Morning Shift",
        category="work",
        start_hour=8,
        end_hour=16,
        days=["monday", "tuesday", "wednesday", "thursday", "friday"],
        applies_to=["npc_guard_001"],
        effects=["patrol"],
        notes=None,
    )

    assert schedule.id == schedule_id
    assert schedule.stable_id == "test_schedule_001"
    assert schedule.name == "Morning Shift"
    assert schedule.category == "work"
    assert schedule.start_hour == 8
    assert schedule.end_hour == 16
    assert schedule.days == ["monday", "tuesday", "wednesday", "thursday", "friday"]
    assert schedule.applies_to == ["npc_guard_001"]
    assert schedule.effects == ["patrol"]
    assert schedule.notes is None


def test_npc_schedule_model_with_notes():
    """Test NPCScheduleModel can have optional notes."""
    schedule_id = str(uuid4())
    schedule = NPCScheduleModel(
        id=schedule_id,
        stable_id="test_schedule_002",
        name="Night Watch",
        category="security",
        start_hour=20,
        end_hour=6,
        days=["saturday", "sunday"],
        applies_to=["npc_guard_002"],
        effects=["watch", "patrol"],
        notes="Special night shift with increased vigilance",
    )

    assert schedule.notes == "Special night shift with increased vigilance"


def test_npc_schedule_model_table_name():
    """Test NPCScheduleModel has correct table name."""
    assert NPCScheduleModel.__tablename__ == "calendar_npc_schedules"


def test_npc_schedule_model_repr():
    """Test NPCScheduleModel __repr__ method."""
    schedule_id = str(uuid4())
    schedule = NPCScheduleModel(
        id=schedule_id,
        stable_id="test_schedule_003",
        name="Test Schedule",
        category="test",
        start_hour=0,
        end_hour=23,
        days=["monday"],
        applies_to=["npc_test"],
        effects=["test"],
        notes=None,
    )

    repr_str = repr(schedule)
    assert "NPCScheduleModel" in repr_str


def test_npc_schedule_model_empty_arrays():
    """Test NPCScheduleModel can have empty arrays."""
    schedule_id = str(uuid4())
    schedule = NPCScheduleModel(
        id=schedule_id,
        stable_id="test_schedule_004",
        name="Empty Schedule",
        category="inactive",
        start_hour=0,
        end_hour=0,
        days=[],
        applies_to=[],
        effects=[],
        notes=None,
    )

    assert schedule.days == []
    assert schedule.applies_to == []
    assert schedule.effects == []
