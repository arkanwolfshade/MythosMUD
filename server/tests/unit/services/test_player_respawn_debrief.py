"""Respawn after delirium or sanitarium failover leaves a pending debrief for the player to spend (ADR-028)."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import cast

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from server.models.lucidity import LucidityActionCode, PlayerLucidity
from server.models.player import Player
from server.services import player_respawn_service as module
from server.services.player_respawn_service import PlayerRespawnService


@dataclass
class Rig:
    player: Player
    lucidity: PlayerLucidity
    cooldowns: list[tuple[uuid.UUID, str, datetime]] = field(
        default_factory=lambda: cast(list[tuple[uuid.UUID, str, datetime]], [])
    )
    commits: int = 0


class FakeSession:
    _rig: Rig

    def __init__(self, rig: Rig) -> None:
        self._rig = rig

    async def get(self, model: type[object], player_id: uuid.UUID) -> object | None:
        _ = player_id
        return self._rig.player if model is Player else self._rig.lucidity

    async def commit(self) -> None:
        self._rig.commits += 1

    async def rollback(self) -> None:  # pragma: no cover - only on failure paths
        return None


@pytest.fixture(name="rig")
def _rig(monkeypatch: pytest.MonkeyPatch) -> Rig:
    player = Player(player_id=str(uuid.uuid4()), name="Tester")
    player.current_room_id = "somewhere_in_the_tutorial"
    player.set_stats({"current_dp": 1, "max_dp": 100, "position": "lying"})
    lucidity = PlayerLucidity(player_id=player.player_id, current_lcd=-10, current_tier="delirious", liabilities="[]")
    rig = Rig(player, lucidity)

    class FakeLucidityService:
        def __init__(self, session: FakeSession) -> None:
            _ = session

        async def set_cooldown(self, player_id: uuid.UUID, action_code: str, expires_at: datetime) -> None:
            rig.cooldowns.append((player_id, action_code, expires_at))

        async def add_liability(self, player_id: uuid.UUID, liability_code: str) -> None:  # pragma: no cover
            _ = player_id, liability_code

    monkeypatch.setattr(module, "LucidityService", FakeLucidityService)
    return rig


def _session(rig: Rig) -> AsyncSession:
    return cast(AsyncSession, cast(object, FakeSession(rig)))


@pytest.mark.asyncio
async def test_a_delirium_respawn_leaves_a_pending_debrief(rig: Rig) -> None:
    respawned = await PlayerRespawnService().respawn_player_from_delirium(
        uuid.UUID(str(rig.player.player_id)), _session(rig)
    )

    assert respawned is True
    [(player_id, action_code, expires_at)] = rig.cooldowns
    assert player_id == uuid.UUID(str(rig.player.player_id))
    assert action_code == LucidityActionCode.DEBRIEF_PENDING
    assert expires_at > datetime.now() + timedelta(days=300)  # a long-lived flag, cleared by the debrief itself


@pytest.mark.asyncio
async def test_a_sanitarium_respawn_still_leaves_a_pending_debrief(rig: Rig) -> None:
    rig.lucidity.current_lcd = -100

    respawned = await PlayerRespawnService().respawn_player_from_sanitarium(
        uuid.UUID(str(rig.player.player_id)), _session(rig)
    )

    assert respawned is True
    assert [code for _, code, _ in rig.cooldowns] == [LucidityActionCode.DEBRIEF_PENDING]
