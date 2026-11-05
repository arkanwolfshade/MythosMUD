"""Unit tests for SpellCostsService: MP is spent through the player registry (ADR-029 step 6b)."""

import uuid
from dataclasses import dataclass
from types import SimpleNamespace
from typing import cast
from unittest.mock import AsyncMock, patch

import pytest

from server.game.magic.spell_costs import SpellCostsService
from server.game.player_service import PlayerService
from server.models.player import Player
from server.models.spell import Spell, SpellEffectType, SpellRangeType, SpellSchool, SpellTargetType
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

PLAYER_ID = uuid.uuid4()


def _spell(**kwargs) -> Spell:
    base = {
        "spell_id": "test",
        "name": "Test",
        "description": "Test spell",
        "school": SpellSchool.ELEMENTAL,
        "mp_cost": 5,
        "target_type": SpellTargetType.SELF,
        "range_type": SpellRangeType.TOUCH,
        "effect_type": SpellEffectType.HEAL,
    }
    base.update(kwargs)
    return Spell(**base)


class _Persistence:
    """The persistence layer as spell costs use it: this player's row, and what it was asked to do."""

    def __init__(self, player: Player | None) -> None:
        self.player: Player | None = player
        self.lucidity_losses: list[tuple[Player, int, str]] = []
        self.corruption: list[tuple[uuid.UUID, int, str, object]] = []
        self.saves: int = 0

    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        _ = player_id
        return self.player

    async def apply_lucidity_loss(self, player: Player, amount: int, source: str = "unknown") -> None:
        self.lucidity_losses.append((player, amount, source))

    async def adjust_corruption(self, player_id: uuid.UUID, delta: int, *, reason_code: str, metadata: object) -> None:
        self.corruption.append((player_id, delta, reason_code, metadata))

    async def save_player(self, player: Player) -> None:
        _ = player
        self.saves += 1


@dataclass
class Rig:
    """A service on a real registry, and its persistence layer."""

    service: SpellCostsService
    harness: LucidityHarness
    persistence: _Persistence


def _player_service(persistence: _Persistence) -> PlayerService:
    return cast(PlayerService, cast(object, SimpleNamespace(persistence=persistence)))


def _rig(stats: dict[str, object] | None) -> Rig:
    """``stats`` is what the player's row and the registry hold (None: no such player)."""
    harness = lucidity_registry({PLAYER_ID: None} if stats is not None else {}, stats=stats)
    player = None
    if stats is not None:
        player = Player(player_id=str(PLAYER_ID), name="Tester")
        player.set_stats(dict(stats))
    persistence = _Persistence(player)
    return Rig(SpellCostsService(_player_service(persistence), harness.registry), harness, persistence)


@pytest.mark.asyncio
async def test_apply_costs_no_player() -> None:
    rig = _rig(None)

    await rig.service.apply_costs(PLAYER_ID, _spell())

    assert rig.harness.db.commits == 0


@pytest.mark.asyncio
async def test_apply_costs_spends_mp_through_the_registry() -> None:
    rig = _rig({"magic_points": 10, "max_magic_points": 10, "current_dp": 5, "max_dp": 10})

    with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock) as send:
        await rig.service.apply_costs(PLAYER_ID, _spell(mp_cost=3))

    assert rig.harness.stats(PLAYER_ID)["magic_points"] == 7
    assert rig.harness.db.commits == 1
    assert rig.persistence.saves == 0
    assert send.await_args is not None
    assert send.await_args.args[2]["stats"]["magic_points"] == 7


@pytest.mark.asyncio
async def test_apply_costs_never_goes_below_zero() -> None:
    rig = _rig({"magic_points": 2, "max_magic_points": 10})

    with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock):
        await rig.service.apply_costs(PLAYER_ID, _spell(mp_cost=5))

    assert rig.harness.stats(PLAYER_ID)["magic_points"] == 0


@pytest.mark.asyncio
async def test_apply_costs_mythos_lucidity_and_corruption() -> None:
    rig = _rig({"magic_points": 10, "corruption": 1, "max_magic_points": 10, "current_dp": 5, "max_dp": 10})
    spell = _spell(school=SpellSchool.MYTHOS, lucidity_cost=10, corruption_on_cast=2)

    with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock):
        await rig.service.apply_costs(PLAYER_ID, spell)

    assert rig.harness.stats(PLAYER_ID)["magic_points"] == 5
    assert rig.persistence.player is not None
    assert rig.persistence.lucidity_losses == [(rig.persistence.player, 10, f"spell_cast:{spell.spell_id}")]
    # Corruption goes through CorruptionService on the registry (the layer's adjust_corruption, ADR-029 step 5c).
    assert rig.persistence.corruption == [(PLAYER_ID, 2, "spell_cast", {"spell_id": spell.spell_id})]


@pytest.mark.asyncio
async def test_apply_costs_send_event_failure_is_non_fatal() -> None:
    rig = _rig({"magic_points": 10, "max_magic_points": 10, "current_dp": 0, "max_dp": 10})

    with patch(
        "server.realtime.connection_manager_api.send_game_event",
        new_callable=AsyncMock,
        side_effect=RuntimeError("no ws"),
    ):
        await rig.service.apply_costs(PLAYER_ID, _spell(mp_cost=1))

    assert rig.harness.stats(PLAYER_ID)["magic_points"] == 9


@pytest.mark.asyncio
async def test_apply_costs_without_a_registry_refuses() -> None:
    """No fallback to writing stats directly: upsert_player no longer writes an existing player's MP."""
    player = Player(player_id=str(PLAYER_ID), name="Tester")
    player.set_stats({"magic_points": 10})

    with pytest.raises(RuntimeError, match="registry not wired"):
        await SpellCostsService(_player_service(_Persistence(player))).apply_costs(PLAYER_ID, _spell())


@pytest.mark.asyncio
async def test_restore_mp_player_not_found() -> None:
    assert (await _rig(None).service.restore_mp(PLAYER_ID, 5))["success"] is False


@pytest.mark.asyncio
async def test_restore_mp_caps_at_max() -> None:
    rig = _rig({"magic_points": 8, "max_magic_points": 10})

    result = await rig.service.restore_mp(PLAYER_ID, 5)

    assert result["success"] is True
    assert result["current_mp"] == 10
    assert result["message"] == "Restored 2 MP"
    assert rig.harness.stats(PLAYER_ID)["magic_points"] == 10


@pytest.mark.asyncio
async def test_restore_mp_computes_max_from_power() -> None:
    result = await _rig({"magic_points": 0, "power": 50}).service.restore_mp(PLAYER_ID, 100)

    assert result["success"] is True
    assert result["max_mp"] == 10
    assert result["current_mp"] == 10
