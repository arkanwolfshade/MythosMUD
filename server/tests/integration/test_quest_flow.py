"""
Integration tests for quest subsystem: start, quest log, abandon flow.

Uses real PostgreSQL (session_factory): quest instances go through a real PlayerRegistry (ADR-029 step 5a) with no
idle cache, so every step reloads the player and sees only what the previous step committed. The definition
repository's get_session_maker is patched to the test DB. Seeds leave_the_tutorial definition and offer via
ON CONFLICT DO NOTHING; tests start_quest, get_quest_log, and abandon.
"""

# Ensure quest and player tables are registered on Base.metadata before create_all
import json
import uuid
from typing import cast
from unittest.mock import patch

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.game.player_registry import PlayerRegistry, RegistrySettings, SessionFactory
from server.game.quest import QuestService
from server.models import Player, User  # noqa: F401
from server.models.quest import QuestDefinition, QuestOffer  # noqa: F401
from server.persistence.repositories.quest_definition_repository import QuestDefinitionRepository

# Tutorial bedroom room id used by seed (must match migration / character creation)
TUTORIAL_ROOM_ID = "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001"

# leave_the_tutorial definition JSON (matches seed migration)
LEAVE_THE_TUTORIAL_DEFINITION = {
    "name": "leave_the_tutorial",
    "title": "Leave the tutorial",
    "description": "Find your way out of the tutorial room.",
    "goals": [{"type": "complete_activity", "target": f"exit_{TUTORIAL_ROOM_ID}"}],
    "rewards": [{"type": "xp", "amount": 10}],
    "triggers": [{"type": "room", "entity_id": TUTORIAL_ROOM_ID}],
    "requires_all": [],
    "requires_any": [],
    "auto_complete": True,
    "turn_in_entities": [],
}


def _quest_service(session_factory: async_sessionmaker[AsyncSession]) -> QuestService:
    """A QuestService on the test DB whose registry keeps nothing between units (each one reloads the player)."""
    registry = PlayerRegistry(cast(SessionFactory, session_factory), settings=RegistrySettings(idle_ttl_seconds=0))
    return QuestService(quest_definition_repository=QuestDefinitionRepository(), player_registry=registry)


async def _stored_state(session_factory: async_sessionmaker[AsyncSession], player_id: uuid.UUID) -> str | None:
    async with session_factory() as session:
        row = (
            await session.execute(
                text("SELECT state FROM quest_instances WHERE player_id = :id AND quest_id = 'leave_the_tutorial'"),
                {"id": str(player_id)},
            )
        ).first()
    return str(cast(object, row[0])) if row is not None else None


@pytest.fixture
async def quest_seed_data(session_factory: async_sessionmaker[AsyncSession]):
    """
    Create User, Player, leave_the_tutorial QuestDefinition and QuestOffer.
    Quest definition and offer are inserted only if missing (idempotent for parallel runs).
    Yields (player_id, user_id) for use in tests.
    """
    async with session_factory() as session:
        user_id = uuid.uuid4()
        player_id = uuid.uuid4()
        user = User(
            id=str(user_id),
            email=f"quest_test_{user_id}@example.com",
            username=f"questuser_{str(user_id)[:8]}",
            display_name=f"Quest User {str(user_id)[:8]}",
            hashed_password="hashed",
            is_active=True,
            is_superuser=False,
            is_verified=True,
        )
        player = Player(
            player_id=str(player_id),
            user_id=str(user_id),
            name=f"questplayer_{str(player_id)[:8]}",
            current_room_id=TUTORIAL_ROOM_ID,
        )
        session.add_all([user, player])
        # Insert quest definition and offer with ON CONFLICT DO NOTHING so parallel workers are safe
        _ = await session.execute(
            text(
                """
                INSERT INTO quest_definitions (id, definition, created_at, updated_at)
                VALUES ('leave_the_tutorial', CAST(:defn AS jsonb), NOW(), NOW())
                ON CONFLICT (id) DO NOTHING
                """
            ),
            {"defn": json.dumps(LEAVE_THE_TUTORIAL_DEFINITION)},
        )
        _ = await session.execute(
            text(
                """
                INSERT INTO quest_offers (quest_id, offer_entity_type, offer_entity_id)
                VALUES ('leave_the_tutorial', 'room', :room_id)
                ON CONFLICT (quest_id, offer_entity_type, offer_entity_id) DO NOTHING
                """
            ),
            {"room_id": TUTORIAL_ROOM_ID},
        )
        await session.commit()
    yield (player_id, user_id)
    # Only the user/player rows are per-run leaks; quest_definitions/quest_offers above use a
    # fixed id with ON CONFLICT DO NOTHING and are deliberately shared, idempotent seed data
    # other parallel tests may depend on -- do not delete those.
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": str(user_id)})
        await session.commit()


@pytest.mark.asyncio
@pytest.mark.integration
async def test_quest_start_log_abandon_flow(
    session_factory: async_sessionmaker[AsyncSession],
    quest_seed_data: tuple[uuid.UUID, uuid.UUID],  # pylint: disable=redefined-outer-name  # pytest injects fixture by param name
):
    """
    Integration: start leave_the_tutorial, get_quest_log shows it, abandon, log empty.

    Patches get_session_maker so repos use integration DB; seeds User, Player,
    QuestDefinition, QuestOffer; then runs QuestService.start_quest, get_quest_log,
    abandon, get_quest_log again.
    """
    player_id, _user_id = quest_seed_data

    with patch(
        "server.persistence.repositories.quest_definition_repository.get_session_maker",
        return_value=session_factory,
    ):
        quest_service = _quest_service(session_factory)

        # Start quest
        start_result = await quest_service.start_quest(player_id, "leave_the_tutorial")
        assert start_result.get("success") is True, start_result.get("message", "start failed")
        assert "started" in cast(str, start_result.get("message", "")).lower()

        # Quest log shows one active entry (same shape as GET /api/players/{id}/quests)
        log = await quest_service.get_quest_log(player_id, include_completed=True)
        assert len(log) == 1
        entry = log[0]
        assert set(entry.keys()) >= {"quest_id", "name", "title", "description", "goals_with_progress", "state"}
        assert entry["quest_id"] == "leave_the_tutorial"
        assert entry["name"] == "leave_the_tutorial"
        assert entry["state"] == "active"
        assert len(cast(list[object], entry["goals_with_progress"])) == 1
        assert entry["goals_with_progress"][0]["goal_type"] == "complete_activity"

        # Abandon by common name
        abandon_result = await quest_service.abandon(player_id, "leave_the_tutorial")
        assert abandon_result.get("success") is True, abandon_result.get("message", "abandon failed")
        assert "abandoned" in cast(str, abandon_result.get("message", "")).lower()

        # Quest log no longer includes abandoned (only active + completed)
        log_after = await quest_service.get_quest_log(player_id, include_completed=True)
        assert len(log_after) == 0
        assert await _stored_state(session_factory, player_id) == "abandoned"


@pytest.mark.asyncio
@pytest.mark.integration
async def test_quest_start_by_trigger_then_abandon(  # pylint: disable=redefined-outer-name
    session_factory: async_sessionmaker[AsyncSession], quest_seed_data: tuple[uuid.UUID, uuid.UUID]
):
    """
    Start quest via start_quest_by_trigger(room), then abandon.
    Verifies trigger-based offer and abandon path.
    """
    player_id, _user_id = quest_seed_data

    with patch(
        "server.persistence.repositories.quest_definition_repository.get_session_maker",
        return_value=session_factory,
    ):
        quest_service = _quest_service(session_factory)

        results = await quest_service.start_quest_by_trigger(player_id, "room", TUTORIAL_ROOM_ID)
        assert len(results) == 1
        assert results[0].get("success") is True

        log = await quest_service.get_quest_log(player_id, include_completed=False)
        assert len(log) == 1 and log[0]["quest_id"] == "leave_the_tutorial"

        abandon_result = await quest_service.abandon(player_id, "leave_the_tutorial")
        assert abandon_result.get("success") is True
        log_after = await quest_service.get_quest_log(player_id, include_completed=True)
        assert len(log_after) == 0

        # Re-accept: start again (avoids UNIQUE violation by updating abandoned row)
        start_again = await quest_service.start_quest(player_id, "leave_the_tutorial")
        assert start_again.get("success") is True, start_again.get("message", "re-start failed")
        log_reaccept = await quest_service.get_quest_log(player_id, include_completed=False)
        assert len(log_reaccept) == 1 and log_reaccept[0]["quest_id"] == "leave_the_tutorial"
        assert log_reaccept[0]["state"] == "active"
        assert await _stored_state(session_factory, player_id) == "active"
