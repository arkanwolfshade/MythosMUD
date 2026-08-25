"""
Integration tests for db/procedures/calendar.sql (#633). Replace raw SQL previously inline in
server/services/holiday_service.py and server/services/schedule_service.py.
"""

import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


@pytest.fixture
async def holiday_row(session_factory: async_sessionmaker[AsyncSession]):
    stable_id = f"test_holiday_{uuid.uuid4().hex[:8]}"
    async with session_factory() as session:
        await session.execute(
            text(
                "INSERT INTO calendar_holidays "
                "(id, stable_id, name, tradition, month, day, duration_hours, season, bonus_tags) "
                "VALUES (:id, :stable_id, 'Test Holiday', 'Testing', 3, 15, 24, 'spring', "
                "ARRAY['festive'])"
            ),
            {"id": uuid.uuid4(), "stable_id": stable_id},
        )
        await session.commit()
    yield stable_id


@pytest.mark.asyncio
async def test_get_calendar_holidays_includes_the_new_row(
    session_factory: async_sessionmaker[AsyncSession], holiday_row: str
) -> None:
    async with session_factory() as session:
        rows = (
            (
                await session.execute(
                    text(
                        "SELECT stable_id, name, tradition, month, day, duration_hours, season, "
                        "bonus_tags FROM get_calendar_holidays() WHERE stable_id = :id"
                    ),
                    {"id": holiday_row},
                )
            )
            .mappings()
            .all()
        )
        assert len(rows) == 1
        row = rows[0]
        assert row["name"] == "Test Holiday"
        assert row["month"] == 3
        assert row["season"] == "spring"
        assert row["bonus_tags"] == ["festive"]


@pytest.fixture
async def npc_schedule_row(session_factory: async_sessionmaker[AsyncSession]):
    stable_id = f"test_schedule_{uuid.uuid4().hex[:8]}"
    async with session_factory() as session:
        await session.execute(
            text(
                "INSERT INTO calendar_npc_schedules "
                "(id, stable_id, name, category, start_hour, end_hour, days, applies_to, effects) "
                "VALUES (:id, :stable_id, 'Test Schedule', 'shopkeeper', 8, 18, "
                "ARRAY['Monday'], ARRAY['test_npc'], ARRAY['opens_shop'])"
            ),
            {"id": uuid.uuid4(), "stable_id": stable_id},
        )
        await session.commit()
    yield stable_id


@pytest.mark.asyncio
async def test_get_calendar_npc_schedules_includes_the_new_row(
    session_factory: async_sessionmaker[AsyncSession], npc_schedule_row: str
) -> None:
    async with session_factory() as session:
        rows = (
            (
                await session.execute(
                    text(
                        "SELECT stable_id, name, category, start_hour, end_hour, days, "
                        "applies_to, effects, notes FROM get_calendar_npc_schedules() "
                        "WHERE stable_id = :id"
                    ),
                    {"id": npc_schedule_row},
                )
            )
            .mappings()
            .all()
        )
        assert len(rows) == 1
        row = rows[0]
        assert row["category"] == "shopkeeper"
        assert row["start_hour"] == 8
        assert row["days"] == ["Monday"]
