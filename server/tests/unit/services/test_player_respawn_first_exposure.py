"""A delirium respawn from inside the First Exposure tutorial ends the tutorial (ADR-028, #1080)."""

from __future__ import annotations

import uuid
from collections.abc import Sequence
from dataclasses import dataclass, field
from datetime import datetime
from typing import cast

import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Load

from server.constants.spawn_defaults import RECOVERY_WARD_ROOM_ID
from server.game.instance_state import INSTANCE_SCOPED_EFFECT_KEY
from server.game.items.constants import INSTANCE_BOUND_FLAG
from server.models.lucidity import PlayerLucidity
from server.models.player import Player
from server.services import player_respawn_service as module
from server.services.player_respawn_service import PlayerRespawnService

INSTANCE_ID = "instance-abc"


@dataclass
class Rig:
    player: Player
    lucidity: PlayerLucidity
    order: list[str] = field(default_factory=lambda: cast(list[str], []))
    finished: list[tuple[uuid.UUID, str]] = field(default_factory=lambda: cast(list[tuple[uuid.UUID, str]], []))
    finish_fails: bool = False
    player_load_options: list[object] = field(default_factory=lambda: cast(list[object], []))


class FakeSession:
    _rig: Rig

    def __init__(self, rig: Rig) -> None:
        self._rig = rig

    async def get(self, model: type[object], player_id: uuid.UUID, options: Sequence[object] = ()) -> object | None:
        _ = player_id
        if model is Player:
            self._rig.player_load_options.extend(options)
        return self._rig.player if model is Player else self._rig.lucidity

    async def commit(self) -> None:
        self._rig.order.append("commit")

    async def rollback(self) -> None:  # pragma: no cover - only on failure paths
        return None


@pytest.fixture(name="rig")
def _rig(monkeypatch: pytest.MonkeyPatch) -> Rig:
    player = Player(player_id=str(uuid.uuid4()), name="Tester")
    player.current_room_id = f"instance_{uuid.uuid4()}_vault"
    player.tutorial_instance_id = INSTANCE_ID
    player.set_stats({"current_dp": 1, "max_dp": 100, "position": "lying"})
    stack: dict[str, object] = {"item_id": "jade_amulet", "prototype_id": "jade_amulet", "quantity": 1}
    stack["flags"] = [INSTANCE_BOUND_FLAG]
    player.set_inventory([stack])
    player.set_status_effects([{"type": "lucidity_drain_over_time", INSTANCE_SCOPED_EFFECT_KEY: True}])
    lucidity = PlayerLucidity(player_id=player.player_id, current_lcd=-10, current_tier="delirious", liabilities="[]")
    rig = Rig(player, lucidity)

    class FakeLucidityService:
        def __init__(self, session: FakeSession) -> None:
            _ = session

        async def set_cooldown(self, player_id: uuid.UUID, action_code: str, expires_at: datetime) -> None:
            _ = player_id, action_code, expires_at

    monkeypatch.setattr(module, "LucidityService", FakeLucidityService)
    return rig


def _service(rig: Rig) -> PlayerRespawnService:
    async def finish(player_id: uuid.UUID, instance_id: str) -> None:
        rig.order.append("finish")
        if rig.finish_fails:
            raise RuntimeError("quest store down")
        rig.finished.append((player_id, instance_id))

    return PlayerRespawnService(first_exposure_finish=finish)


def _session(rig: Rig) -> AsyncSession:
    return cast(AsyncSession, cast(object, FakeSession(rig)))


def _player_id(rig: Rig) -> uuid.UUID:
    return uuid.UUID(str(rig.player.player_id))


@pytest.mark.asyncio
async def test_a_tutorial_delirium_respawn_ends_the_tutorial(rig: Rig) -> None:
    respawned = await _service(rig).respawn_player_from_delirium(_player_id(rig), _session(rig))

    assert respawned is True
    assert rig.player.current_room_id == RECOVERY_WARD_ROOM_ID
    assert rig.lucidity.current_lcd == 70  # not the usual 10
    assert rig.player.tutorial_instance_id is None
    assert rig.player.get_inventory() == []  # the amulet is gone
    assert rig.player.get_status_effects() == []  # and so is the drain
    assert rig.player.get_stats()["current_dp"] == rig.player.get_stats()["max_dp"]


@pytest.mark.asyncio
async def test_the_player_is_loaded_with_the_inventory_record_ready(rig: Rig) -> None:
    """Equipment lives on inventory_record; a lazy load of it fails inside the async session (seen in e2e)."""
    _ = await _service(rig).respawn_player_from_delirium(_player_id(rig), _session(rig))

    assert len(rig.player_load_options) == 1
    assert "Player.inventory_record" in str(cast(Load, rig.player_load_options[0]).path)


@pytest.mark.asyncio
async def test_the_instance_is_finished_only_after_the_respawn_commits(rig: Rig) -> None:
    _ = await _service(rig).respawn_player_from_delirium(_player_id(rig), _session(rig))

    assert rig.order == ["commit", "finish"]
    assert rig.finished == [(_player_id(rig), INSTANCE_ID)]


@pytest.mark.asyncio
async def test_a_failing_finish_does_not_undo_the_respawn(rig: Rig) -> None:
    rig.finish_fails = True

    respawned = await _service(rig).respawn_player_from_delirium(_player_id(rig), _session(rig))

    assert respawned is True
    assert rig.player.current_room_id == RECOVERY_WARD_ROOM_ID


@pytest.mark.asyncio
async def test_the_ending_works_without_a_finisher_wired(rig: Rig) -> None:
    respawned = await PlayerRespawnService().respawn_player_from_delirium(_player_id(rig), _session(rig))

    assert respawned is True
    assert rig.player.tutorial_instance_id is None


@pytest.mark.asyncio
async def test_an_ordinary_delirium_respawn_is_unchanged(rig: Rig) -> None:
    rig.player.tutorial_instance_id = None

    respawned = await _service(rig).respawn_player_from_delirium(_player_id(rig), _session(rig))

    assert respawned is True
    assert rig.lucidity.current_lcd == 10
    assert rig.finished == []
    assert len(rig.player.get_inventory()) == 1  # nothing was stripped
