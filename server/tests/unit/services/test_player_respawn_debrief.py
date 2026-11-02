"""Respawn after delirium or sanitarium failover leaves a pending debrief for the player to spend (ADR-028)."""

from __future__ import annotations

import uuid
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import cast

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from server.constants.spawn_defaults import DEFAULT_RESPAWN_ROOM, RECOVERY_WARD_ROOM_ID
from server.game.player_registry import LucidityData
from server.models.lucidity import LucidityActionCode
from server.models.player import Player
from server.services.player_respawn_service import PlayerRespawnService
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry


@dataclass
class Rig:
    player: Player
    lucidity: LucidityHarness
    commits: int = 0

    def debrief_pending_until(self) -> datetime | None:
        return self.lucidity.cooldowns(uuid.UUID(str(self.player.player_id))).expires_at(
            LucidityActionCode.DEBRIEF_PENDING
        )


class FakeSession:
    _rig: Rig

    def __init__(self, rig: Rig) -> None:
        self._rig = rig

    async def get(self, model: type[object], player_id: uuid.UUID, options: Sequence[object] = ()) -> object | None:
        _ = (player_id, options)
        _ = model
        return self._rig.player

    async def commit(self) -> None:
        self._rig.commits += 1

    async def rollback(self) -> None:  # pragma: no cover - only on failure paths
        return None


@pytest.fixture(name="rig")
def _rig() -> Rig:
    player = Player(player_id=str(uuid.uuid4()), name="Tester")
    player.current_room_id = "somewhere_in_the_tutorial"
    player.set_stats({"current_dp": 1, "max_dp": 100, "position": "lying"})
    lucidity = lucidity_registry({uuid.UUID(str(player.player_id)): LucidityData(-10, "catatonic")})
    rig = Rig(player, lucidity)

    return rig


def _session(rig: Rig) -> AsyncSession:
    return cast(AsyncSession, cast(object, FakeSession(rig)))


@pytest.mark.asyncio
async def test_a_delirium_respawn_leaves_a_pending_debrief(rig: Rig) -> None:
    respawned = await PlayerRespawnService(player_registry=rig.lucidity.registry).respawn_player_from_delirium(
        uuid.UUID(str(rig.player.player_id)), _session(rig)
    )

    assert respawned is True
    expires_at = rig.debrief_pending_until()
    assert expires_at is not None
    assert expires_at > datetime.now(UTC) + timedelta(days=300)  # a long-lived flag, cleared by the debrief itself


@pytest.mark.asyncio
async def test_a_sanitarium_respawn_still_leaves_a_pending_debrief(rig: Rig) -> None:
    async with rig.lucidity.registry.mutate(uuid.UUID(str(rig.player.player_id))) as player:
        _ = player.lucidity.set(lcd=-100)

    respawned = await PlayerRespawnService(player_registry=rig.lucidity.registry).respawn_player_from_sanitarium(
        uuid.UUID(str(rig.player.player_id)), _session(rig)
    )

    assert respawned is True
    assert rig.debrief_pending_until() is not None


@pytest.mark.asyncio
async def test_a_delirium_respawn_wakes_the_player_in_the_recovery_ward(rig: Rig) -> None:
    respawned = await PlayerRespawnService(player_registry=rig.lucidity.registry).respawn_player_from_delirium(
        uuid.UUID(str(rig.player.player_id)), _session(rig)
    )

    assert respawned is True
    assert rig.player.current_room_id == RECOVERY_WARD_ROOM_ID


@pytest.mark.asyncio
async def test_a_sanitarium_respawn_wakes_the_player_in_the_recovery_ward(rig: Rig) -> None:
    async with rig.lucidity.registry.mutate(uuid.UUID(str(rig.player.player_id))) as player:
        _ = player.lucidity.set(lcd=-100)

    respawned = await PlayerRespawnService(player_registry=rig.lucidity.registry).respawn_player_from_sanitarium(
        uuid.UUID(str(rig.player.player_id)), _session(rig)
    )

    assert respawned is True
    assert rig.player.current_room_id == RECOVERY_WARD_ROOM_ID


def test_death_still_respawns_at_the_main_foyer_not_the_ward() -> None:
    assert DEFAULT_RESPAWN_ROOM != RECOVERY_WARD_ROOM_ID
    assert DEFAULT_RESPAWN_ROOM.endswith("foyer_001")
