"""The combat bundle hands the respawn service a First Exposure finisher bound to its own container (ADR-028)."""

# pyright: reportPrivateUsage=false
# Reason: the wiring under test is the respawn service's private finish hook.

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import cast

import pytest

from server.container.bundles.combat import CombatBundle
from server.container.main import ApplicationContainer
from server.services.player_respawn_service import PlayerRespawnService


@dataclass
class Rig:
    flushed: list[str] = field(default_factory=lambda: cast(list[str], []))


class FakePersistence:
    def get_room_by_id(self, room_id: str) -> None:  # bound by the bundle as the respawn room lookup
        _ = room_id

    async def get_player_by_id(self, player_id: uuid.UUID) -> None:
        _ = player_id

    async def save_player(self, player: object) -> None:  # pragma: no cover - no player is ever found
        _ = player

    def set_lucidity_adjuster(self, adjuster: object) -> None:  # wired by the combat bundle (ADR-029 step 3a)
        _ = adjuster


class FakeFlush:
    _rig: Rig

    def __init__(self, rig: Rig) -> None:
        self._rig = rig

    async def flush(self, instance_id: str) -> int:
        self._rig.flushed.append(instance_id)
        return 0


def _stub(monkeypatch: pytest.MonkeyPatch, target: str) -> None:
    def factory(*args: object, **kwargs: object) -> SimpleNamespace:
        _ = args, kwargs
        return SimpleNamespace()

    monkeypatch.setattr(target, factory)


@pytest.mark.asyncio
async def test_the_respawn_service_gets_a_finisher_that_resolves_services_from_the_container(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    for target in (
        "server.services.player_combat_service.PlayerCombatService",
        "server.services.player_death_service.PlayerDeathService",
        "server.services.catatonia_registry.CatatoniaRegistry",
        "server.services.passive_lucidity_flux_service.PassiveLucidityFluxService",
        "server.services.passive_corruption_flux.service.PassiveCorruptionFluxService",
    ):
        _stub(monkeypatch, target)
    rig = Rig()
    container = SimpleNamespace(
        persistence=object(),
        event_bus=object(),
        performance_monitor=object(),
        connection_manager=None,
        movement_service=None,
        level_service=None,
        async_persistence=FakePersistence(),
        quest_service=None,
        instance_flush_service=None,  # not built yet when the respawn service is constructed
    )
    bundle = CombatBundle()

    await bundle.initialize(cast(ApplicationContainer, cast(object, container)))

    service = cast(PlayerRespawnService | None, bundle.player_respawn_service)
    assert service is not None
    assert service._first_exposure_finish is not None
    await service._first_exposure_finish(uuid.uuid4(), "instance-abc")
    assert rig.flushed == []  # the flush service did not exist yet, so the finish was skipped quietly
    container.instance_flush_service = FakeFlush(rig)  # built later, as in the real startup order
    await service._first_exposure_finish(uuid.uuid4(), "instance-abc")
    assert rig.flushed == ["instance-abc"]
