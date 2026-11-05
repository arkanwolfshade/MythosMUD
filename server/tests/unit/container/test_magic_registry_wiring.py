"""MP's services get the player registry at startup (ADR-029 step 6b): without it nothing regenerates or can be spent."""

# pyright: reportPrivateUsage=false
# Reason: the startup helpers under test are private to the bundle and the lifespan.

from __future__ import annotations

import uuid
from types import SimpleNamespace
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI

from server.app.lifespan_magic import _initialize_mp_regeneration_service, _initialize_spell_effects
from server.container.bundles.magic import (
    MagicBundle,
    _create_learning_mp_regen_and_magic,
    _create_registry_and_targeting,
)
from server.container.main import ApplicationContainer
from server.game.magic.magic_service import MagicService
from server.game.magic.mp_regeneration_service import MPRegenerationService
from server.game.magic.spell_effects import SpellEffects
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

PLAYER_ID = uuid.uuid4()


def _container(harness: LucidityHarness) -> ApplicationContainer:
    container = SimpleNamespace(
        player_service=MagicMock(),
        combat_service=None,
        player_combat_service=None,
        async_persistence=None,
        item_granter=None,
        player_registry=harness.registry,
    )
    return cast(ApplicationContainer, cast(object, container))


def _harness() -> LucidityHarness:
    return lucidity_registry({PLAYER_ID: None}, stats={"magic_points": 2, "max_magic_points": 10})


async def _rest_restored_mp(service: MPRegenerationService, harness: LucidityHarness) -> None:
    result = await service.restore_mp_from_rest(PLAYER_ID, 60)
    assert result["success"] is True
    assert harness.stats(PLAYER_ID)["magic_points"] == 3


@pytest.mark.asyncio
async def test_the_bundle_wires_regeneration_and_spell_costs_onto_the_registry() -> None:
    harness = _harness()
    bundle = MagicBundle()

    with patch("server.game.magic.spell_learning_service.SpellLearningService"):
        _create_learning_mp_regen_and_magic(bundle, _container(harness), MagicMock())

    await _rest_restored_mp(cast(MPRegenerationService, bundle.mp_regeneration_service), harness)
    # Spell costs and restores go through MagicService's own SpellCostsService.
    _ = await cast(MagicService, bundle.magic_service).restore_mp(PLAYER_ID, 1)
    assert harness.stats(PLAYER_ID)["magic_points"] == 4


@pytest.mark.asyncio
async def test_the_lifespan_wires_regeneration_onto_the_registry() -> None:
    harness = _harness()
    app = FastAPI()

    _initialize_mp_regeneration_service(app, _container(harness))

    await _rest_restored_mp(cast(MPRegenerationService, app.state.mp_regeneration_service), harness)


@pytest.mark.asyncio
async def test_the_bundle_gives_spell_effects_the_registry() -> None:
    """Power Drain's MP change needs it: without it the spell only reports a failure."""
    harness = _harness()
    bundle = MagicBundle()

    with (
        patch("server.persistence.repositories.spell_repository.SpellRepository"),
        patch("server.persistence.repositories.player_spell_repository.PlayerSpellRepository"),
        patch("server.game.magic.spell_registry.SpellRegistry", return_value=MagicMock(load_spells=AsyncMock())),
        patch("server.game.magic.spell_targeting.SpellTargetingService"),
        patch("server.services.target_resolution_service.TargetResolutionService"),
    ):
        _ = await _create_registry_and_targeting(bundle, _container(harness))

    assert cast(SpellEffects, bundle.spell_effects).player_registry is harness.registry


def test_the_lifespan_gives_spell_effects_the_registry() -> None:
    harness = _harness()
    app = FastAPI()

    _initialize_spell_effects(app, _container(harness))

    assert cast(SpellEffects, app.state.spell_effects).player_registry is harness.registry
