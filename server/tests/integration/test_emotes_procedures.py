"""
Integration tests for db/procedures/emotes.sql (#633). Replace raw SQL previously inline in
server/persistence/repositories/emote_repository.py.
"""

import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


@pytest.fixture
async def emote_row(session_factory: async_sessionmaker[AsyncSession]):
    """Create one emote with one alias. Yields (stable_id, alias)."""
    emote_id = uuid.uuid4()
    stable_id = f"test_emote_{uuid.uuid4().hex[:8]}"
    alias = f"te{uuid.uuid4().hex[:6]}"
    async with session_factory() as session:
        await session.execute(
            text(
                "INSERT INTO emotes (id, stable_id, self_message, other_message) "
                "VALUES (:id, :stable_id, 'You test.', '{name} tests.')"
            ),
            {"id": emote_id, "stable_id": stable_id},
        )
        await session.execute(
            text("INSERT INTO emote_aliases (emote_id, alias) VALUES (:emote_id, :alias)"),
            {"emote_id": emote_id, "alias": alias},
        )
        await session.commit()
    yield stable_id, alias


@pytest.mark.asyncio
async def test_get_emotes_includes_the_new_row(
    session_factory: async_sessionmaker[AsyncSession], emote_row: tuple[str, str]
) -> None:
    stable_id, _alias = emote_row
    async with session_factory() as session:
        rows = (
            (
                await session.execute(
                    text("SELECT stable_id, self_message, other_message FROM get_emotes() WHERE stable_id = :id"),
                    {"id": stable_id},
                )
            )
            .mappings()
            .all()
        )
        assert len(rows) == 1
        assert rows[0]["self_message"] == "You test."
        assert rows[0]["other_message"] == "{name} tests."


@pytest.mark.asyncio
async def test_get_emote_aliases_joins_owning_emote(
    session_factory: async_sessionmaker[AsyncSession], emote_row: tuple[str, str]
) -> None:
    stable_id, alias = emote_row
    async with session_factory() as session:
        rows = (
            (
                await session.execute(
                    text("SELECT stable_id, alias FROM get_emote_aliases() WHERE stable_id = :id"),
                    {"id": stable_id},
                )
            )
            .mappings()
            .all()
        )
        assert len(rows) == 1
        assert rows[0]["alias"] == alias
