"""Unit tests for GameMechanicsService."""

# pyright: reportAny=false
# TEST_MOCK: `_player()`'s MagicMock attributes (player_id, get_stats) resolve to Any; typing them
# precisely would need a fake Protocol with no runtime value in this mock-driven suite.

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.exceptions import ValidationError
from server.game.mechanics import GameMechanicsService


async def _async_session_gen(session: AsyncMock):
    """Yield a single fake session -- mirrors get_async_session's shape for CorruptionService."""
    yield session


@pytest.fixture
def persistence() -> MagicMock:
    p = MagicMock()
    p.get_player_by_id = AsyncMock()
    p.save_player = AsyncMock()
    p.apply_lucidity_loss = AsyncMock()
    p.apply_fear = AsyncMock()
    p.apply_corruption = AsyncMock()
    p.gain_occult_knowledge = AsyncMock()
    p.heal_player = AsyncMock()
    p.damage_player = AsyncMock()
    return p


@pytest.fixture
def service(persistence: MagicMock) -> GameMechanicsService:
    return GameMechanicsService(persistence)


def _player(name: str = "Armitage") -> MagicMock:
    p = MagicMock()
    p.name = name
    p.player_id = uuid.uuid4()
    stats: dict[str, object] = {"corruption": 0}
    p.get_stats = MagicMock(return_value=stats)
    p.set_stats = MagicMock(side_effect=stats.update)
    return p


@pytest.mark.asyncio
async def test_apply_lucidity_loss_success(service: GameMechanicsService, persistence: MagicMock) -> None:
    player = _player()
    player_id = str(player.player_id)
    persistence.get_player_by_id.return_value = player
    ok, msg = await service.apply_lucidity_loss(player_id, 5, source="test")
    assert ok is True
    assert "5 lucidity loss" in msg
    persistence.apply_lucidity_loss.assert_awaited_once()


@pytest.mark.asyncio
async def test_apply_lucidity_loss_player_not_found(service: GameMechanicsService, persistence: MagicMock) -> None:
    persistence.get_player_by_id.return_value = None
    with pytest.raises(ValidationError):
        await service.apply_lucidity_loss(str(uuid.uuid4()), 5)


@pytest.mark.asyncio
async def test_apply_fear_success(service: GameMechanicsService, persistence: MagicMock) -> None:
    player = _player()
    persistence.get_player_by_id.return_value = player
    ok, msg = await service.apply_fear(str(player.player_id), 3)
    assert ok is True
    assert "fear" in msg


@pytest.mark.asyncio
async def test_apply_corruption_success(service: GameMechanicsService, persistence: MagicMock) -> None:
    player = _player()
    persistence.get_player_by_id.return_value = player
    session = AsyncMock()
    with patch(
        "server.services.corruption_service.get_async_session",
        return_value=_async_session_gen(session),
    ):
        ok, msg = await service.apply_corruption(str(player.player_id), 2)
    assert ok is True
    assert "corruption" in msg
    assert player.get_stats()["corruption"] == 2


@pytest.mark.asyncio
async def test_gain_occult_knowledge_success(service: GameMechanicsService, persistence: MagicMock) -> None:
    player = _player()
    persistence.get_player_by_id.return_value = player
    ok, msg = await service.gain_occult_knowledge(str(player.player_id), 10)
    assert ok is True
    assert "occult knowledge" in msg
    persistence.gain_occult_knowledge.assert_awaited_once_with(player, 10, "unknown")
    persistence.apply_lucidity_loss.assert_awaited_once()


@pytest.mark.asyncio
async def test_heal_player_success(service: GameMechanicsService, persistence: MagicMock) -> None:
    player = _player()
    persistence.get_player_by_id.return_value = player
    ok, msg = await service.heal_player(str(player.player_id), 15)
    assert ok is True
    assert "Healed" in msg


@pytest.mark.asyncio
async def test_damage_player_success(service: GameMechanicsService, persistence: MagicMock) -> None:
    player = _player()
    persistence.get_player_by_id.return_value = player
    ok, msg = await service.damage_player(str(player.player_id), 8, "psychic")
    assert ok is True
    assert "psychic" in msg


def test_gain_experience_removed(service: GameMechanicsService) -> None:
    """#879: XP awards go through LevelService.grant_xp; GameMechanicsService has no such method."""
    assert not hasattr(service, "gain_experience")
