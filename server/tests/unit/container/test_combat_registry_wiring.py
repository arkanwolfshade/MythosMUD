"""The combat bundle wires corruption and DP onto the player registry (ADR-029 steps 5c, 6a): the persistence
layer's ``adjust_corruption`` and damage and healing run services on it, and the corruption flux tick gets it too."""

from __future__ import annotations

from types import SimpleNamespace
from typing import cast

import pytest

from server.container.bundles.combat import CombatBundle
from server.container.main import ApplicationContainer
from server.models.corruption import CorruptionAdjusting
from server.models.player_dp import DpAdjusting
from server.services.corruption_service import CorruptionService
from server.services.player_health_service import PlayerHealthService
from server.tests.fixtures.shared.player_registry import lucidity_registry


class RecordingPersistence:
    """What the combat bundle sets on the persistence layer at startup."""

    def __init__(self) -> None:
        self.corruption_service: CorruptionAdjusting | None = None
        self.health_service: DpAdjusting | None = None
        self.wired_lucidity: bool = False

    def get_room_by_id(self, room_id: str) -> None:  # bound by the bundle as the respawn room lookup
        _ = room_id

    def set_lucidity_adjuster(self, adjuster: object) -> None:
        _ = adjuster
        self.wired_lucidity = True

    def set_lucidity_reader(self, reader: object) -> None:
        _ = reader

    def set_corruption_service(self, service: CorruptionAdjusting | None) -> None:
        self.corruption_service = service

    def set_health_service(self, service: DpAdjusting | None) -> None:
        self.health_service = service


@pytest.mark.asyncio
async def test_corruption_is_wired_onto_the_player_registry(monkeypatch: pytest.MonkeyPatch) -> None:
    flux_kwargs: list[dict[str, object]] = []

    def stub(*args: object, **kwargs: object) -> SimpleNamespace:
        _ = args, kwargs
        return SimpleNamespace()

    def corruption_flux(*args: object, **kwargs: object) -> SimpleNamespace:
        _ = args
        flux_kwargs.append(kwargs)
        return SimpleNamespace()

    for target in (
        "server.services.player_combat_service.PlayerCombatService",
        "server.services.player_death_service.PlayerDeathService",
        "server.services.catatonia_registry.CatatoniaRegistry",
        "server.services.passive_lucidity_flux_service.PassiveLucidityFluxService",
    ):
        monkeypatch.setattr(target, stub)
    monkeypatch.setattr("server.services.passive_corruption_flux.service.PassiveCorruptionFluxService", corruption_flux)
    registry = lucidity_registry({}).registry
    persistence = RecordingPersistence()
    container = SimpleNamespace(
        persistence=object(),
        event_bus=object(),
        performance_monitor=object(),
        connection_manager=None,
        movement_service=None,
        level_service=None,
        async_persistence=persistence,
        quest_service=None,
        instance_flush_service=None,
        player_registry=registry,
    )

    await CombatBundle().initialize(cast(ApplicationContainer, cast(object, container)))

    assert persistence.wired_lucidity
    assert isinstance(persistence.corruption_service, CorruptionService)
    assert isinstance(persistence.health_service, PlayerHealthService)  # DP from ticks and mechanics (step 6a)
    [kwargs] = flux_kwargs
    assert kwargs["player_registry"] is registry  # the tick writes room flux through the registry
