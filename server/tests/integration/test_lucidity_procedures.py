"""
Integration test for db/procedures/lucidity.sql's get_lucidity_rate_overrides() (#633). Replaces
the raw UNION ALL previously inline in server/services/passive_lucidity_flux/rate_overrides.py.
"""

import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


@pytest.fixture
async def zone_with_override_and_subzone_without(session_factory: async_sessionmaker[AsyncSession]):
    """A zone with special_rules set, and a subzone under it with special_rules NULL (excluded).
    Yields the zone's stable_id."""
    suffix = uuid.uuid4().hex[:8]
    zone_id = uuid.uuid4()
    zone_stable_id = f"test_zone_{suffix}"
    async with session_factory() as session:
        await session.execute(
            text(
                "INSERT INTO zones (id, stable_id, name, special_rules) "
                "VALUES (:id, :stable_id, 'Test Zone', '{\"lucidity_drain_rate\": 0.5}'::jsonb)"
            ),
            {"id": zone_id, "stable_id": zone_stable_id},
        )
        # special_rules explicitly NULL, same reasoning as the zone fixture below.
        await session.execute(
            text(
                "INSERT INTO subzones (id, zone_id, stable_id, name, special_rules) "
                "VALUES (:id, :zone_id, :stable_id, 'Sub', NULL)"
            ),
            {"id": uuid.uuid4(), "zone_id": zone_id, "stable_id": f"test_subzone_{suffix}"},
        )
        await session.commit()
    yield zone_stable_id


@pytest.mark.asyncio
async def test_get_lucidity_rate_overrides_includes_zone_and_excludes_null_subzone(
    session_factory: async_sessionmaker[AsyncSession], zone_with_override_and_subzone_without: str
) -> None:
    zone_stable_id = zone_with_override_and_subzone_without
    async with session_factory() as session:
        rows = (
            (
                await session.execute(
                    text(
                        "SELECT zone_stable_id, subzone_stable_id, special_rules "
                        "FROM get_lucidity_rate_overrides() WHERE zone_stable_id = :id"
                    ),
                    {"id": zone_stable_id},
                )
            )
            .mappings()
            .all()
        )
        # Only the zone-level row: the subzone has NULL special_rules, filtered by WHERE ... IS NOT NULL.
        assert len(rows) == 1
        assert rows[0]["subzone_stable_id"] is None
        assert rows[0]["special_rules"]["lucidity_drain_rate"] == 0.5


@pytest.fixture
async def subzone_with_override(session_factory: async_sessionmaker[AsyncSession]):
    """A zone with NO override, and a subzone under it WITH special_rules set.
    Yields (zone_stable_id, subzone_stable_id)."""
    suffix = uuid.uuid4().hex[:8]
    zone_id = uuid.uuid4()
    zone_stable_id = f"test_zone_{suffix}"
    subzone_stable_id = f"test_subzone_{suffix}"
    async with session_factory() as session:
        # special_rules explicitly NULL (not the column's '{}' default) -- an empty object is
        # NOT NULL and would itself pass the procedure's WHERE ... IS NOT NULL filter.
        await session.execute(
            text("INSERT INTO zones (id, stable_id, name, special_rules) VALUES (:id, :stable_id, 'Test Zone', NULL)"),
            {"id": zone_id, "stable_id": zone_stable_id},
        )
        await session.execute(
            text(
                "INSERT INTO subzones (id, zone_id, stable_id, name, special_rules) "
                "VALUES (:id, :zone_id, :stable_id, 'Sub', '{\"lucidity_drain_rate\": 1.5}'::jsonb)"
            ),
            {"id": uuid.uuid4(), "zone_id": zone_id, "stable_id": subzone_stable_id},
        )
        await session.commit()
    yield zone_stable_id, subzone_stable_id


@pytest.mark.asyncio
async def test_get_lucidity_rate_overrides_includes_subzone_row(
    session_factory: async_sessionmaker[AsyncSession], subzone_with_override: tuple[str, str]
) -> None:
    zone_stable_id, subzone_stable_id = subzone_with_override
    async with session_factory() as session:
        rows = (
            (
                await session.execute(
                    text(
                        "SELECT zone_stable_id, subzone_stable_id, special_rules "
                        "FROM get_lucidity_rate_overrides() WHERE zone_stable_id = :id"
                    ),
                    {"id": zone_stable_id},
                )
            )
            .mappings()
            .all()
        )
        # Zone itself has no override, so only the subzone row appears.
        assert len(rows) == 1
        assert rows[0]["subzone_stable_id"] == subzone_stable_id
        assert rows[0]["special_rules"]["lucidity_drain_rate"] == 1.5
