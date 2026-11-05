"""
Integration test for the player_spells procedures against real PostgreSQL.

``learn_spell`` failed on every call ("column reference player_id is ambiguous"), and nothing caught it because every
unit test mocks the repository; the spellcasting e2e spec found it.
"""

import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.persistence.repositories.player_spell_repository import PlayerSpellRepository
from server.tests.fixtures.integration.players import create_test_player, delete_test_user


@pytest.fixture
async def spell_id(session_factory: async_sessionmaker[AsyncSession]):
    """A spell to learn; deleted afterwards."""
    new_id = f"test_spell_{uuid.uuid4().hex[:12]}"
    async with session_factory() as session:
        _ = await session.execute(
            text(
                """
                INSERT INTO spells (
                    spell_id, name, description, school, mp_cost, target_type, range_type, effect_type
                ) VALUES (:id, :name, 'A test spell', 'clerical', 1, 'self', 'touch', 'heal')
                """
            ),
            {"id": new_id, "name": new_id},
        )
        await session.commit()
    yield new_id
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM spells WHERE spell_id = :id"), {"id": new_id})
        await session.commit()


@pytest.fixture
async def player_id(session_factory: async_sessionmaker[AsyncSession]):
    """A player; deleting their user afterwards cascades to what they learned."""
    user_id = uuid.uuid4()
    yield await create_test_player(session_factory, user_id)
    await delete_test_user(session_factory, user_id)


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_a_player_learns_casts_and_masters_a_spell(player_id: uuid.UUID, spell_id: str) -> None:
    repository = PlayerSpellRepository()

    learned = await repository.learn_spell(player_id, spell_id, 7)

    assert (str(learned.player_id), learned.spell_id, learned.mastery) == (str(player_id), spell_id, 7)
    known = await repository.get_player_spell(player_id, spell_id)
    assert known is not None and known.mastery == 7
    assert [spell.spell_id for spell in await repository.get_player_spells(player_id)] == [spell_id]

    _ = await repository.record_spell_cast(player_id, spell_id)

    cast_once = await repository.get_player_spell(player_id, spell_id)
    assert cast_once is not None and cast_once.times_cast == 1


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_learning_a_known_spell_keeps_its_mastery(player_id: uuid.UUID, spell_id: str) -> None:
    repository = PlayerSpellRepository()
    _ = await repository.learn_spell(player_id, spell_id, 7)

    again = await repository.learn_spell(player_id, spell_id, 0)

    assert again.mastery == 7
