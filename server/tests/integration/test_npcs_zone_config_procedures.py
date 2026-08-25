"""
Integration tests for db/procedures/npcs.sql's zone/subzone config read procedures (#633).

get_zone_configs()/get_subzone_configs() replace the raw SQL previously inline in
server/npc/zone_config_loader.py.
"""

import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


@pytest.fixture
async def zone_and_subzone(session_factory: async_sessionmaker[AsyncSession]):
    """Create one zone and one subzone with unique stable_ids. Yields (zone_stable_id, subzone_stable_id)."""
    suffix = uuid.uuid4().hex[:8]
    zone_id = uuid.uuid4()
    zone_stable_id = f"test_zone_{suffix}"
    subzone_stable_id = f"test_subzone_{suffix}"
    async with session_factory() as session:
        await session.execute(
            text(
                "INSERT INTO zones (id, stable_id, name, zone_type, environment, description, "
                "weather_patterns, special_rules) "
                "VALUES (:id, :stable_id, 'Test Zone', 'city', 'outdoors', 'A test zone.', "
                '\'["clear"]\'::jsonb, \'{"note": "zone"}\'::jsonb)'
            ),
            {"id": zone_id, "stable_id": zone_stable_id},
        )
        await session.execute(
            text(
                "INSERT INTO subzones (id, zone_id, stable_id, name, environment, description, special_rules) "
                "VALUES (:id, :zone_id, :stable_id, 'Test Subzone', 'indoors', 'A test subzone.', "
                '\'{"note": "subzone"}\'::jsonb)'
            ),
            {"id": uuid.uuid4(), "zone_id": zone_id, "stable_id": subzone_stable_id},
        )
        await session.commit()
    yield zone_stable_id, subzone_stable_id


@pytest.mark.asyncio
async def test_get_zone_configs_includes_the_zone(
    session_factory: async_sessionmaker[AsyncSession], zone_and_subzone: tuple[str, str]
) -> None:
    zone_stable_id, _subzone_stable_id = zone_and_subzone
    async with session_factory() as session:
        rows = (
            (
                await session.execute(
                    text(
                        "SELECT zone_stable_id, zone_type, environment, description, "
                        "weather_patterns, special_rules FROM get_zone_configs() "
                        "WHERE zone_stable_id = :id"
                    ),
                    {"id": zone_stable_id},
                )
            )
            .mappings()
            .all()
        )
        assert len(rows) == 1
        row = rows[0]
        assert row["zone_type"] == "city"
        assert row["environment"] == "outdoors"
        assert row["weather_patterns"] == ["clear"]
        assert row["special_rules"] == {"note": "zone"}


@pytest.mark.asyncio
async def test_get_subzone_configs_joins_parent_zone(
    session_factory: async_sessionmaker[AsyncSession], zone_and_subzone: tuple[str, str]
) -> None:
    zone_stable_id, subzone_stable_id = zone_and_subzone
    async with session_factory() as session:
        rows = (
            (
                await session.execute(
                    text(
                        "SELECT zone_stable_id, subzone_stable_id, environment, description, "
                        "special_rules, zone_type, weather_patterns FROM get_subzone_configs() "
                        "WHERE subzone_stable_id = :id"
                    ),
                    {"id": subzone_stable_id},
                )
            )
            .mappings()
            .all()
        )
        assert len(rows) == 1
        row = rows[0]
        assert row["zone_stable_id"] == zone_stable_id
        assert row["environment"] == "indoors"
        assert row["special_rules"] == {"note": "subzone"}
        # Inherited-from-zone columns, per zone_config_loader.py's expectations
        assert row["zone_type"] == "city"
        assert row["weather_patterns"] == ["clear"]
