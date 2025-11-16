"""Tests ensuring NPC combat integration applies sanity effects."""

from __future__ import annotations

from types import SimpleNamespace

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.models.base import Base
from server.services.active_sanity_service import UnknownEncounterCategoryError
from server.services.npc_combat_integration_service import NPCCombatIntegrationService


@pytest.fixture
async def session_factory():
    import os
    database_url = os.getenv("DATABASE_URL")
    if not database_url or not database_url.startswith("postgresql"):
        raise ValueError(
            "DATABASE_URL must be set to a PostgreSQL URL. "
            "SQLite is no longer supported."
        )
    engine = create_async_engine(database_url, future=True)
    async with engine.begin() as conn:
        # PostgreSQL always enforces foreign keys - no PRAGMA needed
        await conn.run_sync(Base.metadata.create_all)
    maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        yield maker
    finally:
        await engine.dispose()


class DummyNPCDefinition:
    def __init__(self, *, name: str, npc_type: str = "aggressive_mob", behavior: dict | None = None):
        self.name = name
        self.npc_type = npc_type
        self._behavior = behavior or {}

    def get_base_stats(self) -> dict:
        return {}

    def get_behavior_config(self) -> dict:
        return self._behavior


@pytest.mark.asyncio
async def test_apply_encounter_sanity_effect_invokes_active_service(session_factory, monkeypatch):
    calls: list[SimpleNamespace] = []

    class FakeActiveSanityService:
        def __init__(self, session):
            self.session = session

        async def apply_encounter_sanity_loss(self, player_id, entity_archetype, category, location_id):
            calls.append(SimpleNamespace(player_id=player_id, archetype=entity_archetype, category=category))
            return SimpleNamespace(delta=-6)

    async def session_gen():
        async with session_factory() as session:
            yield session

    monkeypatch.setattr(
        "server.services.npc_combat_integration_service.get_async_session",
        lambda: session_gen(),
    )
    monkeypatch.setattr(
        "server.services.npc_combat_integration_service.ActiveSanityService",
        FakeActiveSanityService,
    )

    service = object.__new__(NPCCombatIntegrationService)
    await service._apply_encounter_sanity_effect(
        "player-1",
        "npc-nightgaunt-001",
        DummyNPCDefinition(name="Nightgaunt", npc_type="aggressive_mob"),
        "earth_arkhamcity_temple",
    )

    assert calls
    record = calls[0]
    assert record.player_id == "player-1"
    assert record.archetype == "Nightgaunt"
    assert record.category == "horrific"


@pytest.mark.asyncio
async def test_apply_encounter_sanity_effect_falls_back_to_disturbing(session_factory, monkeypatch):
    categories: list[str] = []

    class FlakyActiveSanityService:
        def __init__(self, session):
            self.session = session
            self._attempts = 0

        async def apply_encounter_sanity_loss(self, player_id, entity_archetype, category, location_id):
            categories.append(category)
            if self._attempts == 0:
                self._attempts += 1
                raise UnknownEncounterCategoryError(category)
            return SimpleNamespace(delta=-2)

    async def session_gen():
        async with session_factory() as session:
            yield session

    monkeypatch.setattr(
        "server.services.npc_combat_integration_service.get_async_session",
        lambda: session_gen(),
    )
    monkeypatch.setattr(
        "server.services.npc_combat_integration_service.ActiveSanityService",
        FlakyActiveSanityService,
    )

    service = object.__new__(NPCCombatIntegrationService)
    await service._apply_encounter_sanity_effect(
        "player-1",
        "npc-hound-001",
        DummyNPCDefinition(name="Hound of Tindalos", behavior={"sanity_category": "cosmic"}),
        "earth_arkhamcity_labyrinth",
    )

    assert categories[0] == "cosmic"
    assert categories[1] == "disturbing"
