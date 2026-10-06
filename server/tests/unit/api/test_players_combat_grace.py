"""Unit tests for the login-grace combat exit in server.api.players (#833: leave the fight, don't end it for all)."""

# pyright: reportPrivateUsage=false
# Reason: _end_combat_for_grace_period is the unit under test.

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.api.players import _end_combat_for_grace_period

_GET_SERVICE = "server.services.combat_service.get_combat_service"


def _service(combat: MagicMock | None, remove_participant: AsyncMock) -> MagicMock:
    service: MagicMock = MagicMock()
    service.get_combat_by_participant = AsyncMock(return_value=combat)
    service.remove_participant = remove_participant
    return service


def _combat() -> tuple[MagicMock, uuid.UUID]:
    combat_id = uuid.uuid4()
    combat: MagicMock = MagicMock()
    combat.combat_id = combat_id
    return combat, combat_id


@pytest.mark.asyncio
async def test_grace_period_removes_only_that_player_from_combat() -> None:
    player_id = uuid.uuid4()
    combat, combat_id = _combat()
    remove_participant: AsyncMock = AsyncMock(return_value=True)

    with patch(_GET_SERVICE, return_value=_service(combat, remove_participant)):
        await _end_combat_for_grace_period(player_id)

    remove_participant.assert_awaited_once_with(combat_id, player_id, "Player entered login grace period")


@pytest.mark.asyncio
async def test_grace_period_is_a_no_op_without_a_combat() -> None:
    remove_participant: AsyncMock = AsyncMock()
    with patch(_GET_SERVICE, return_value=_service(None, remove_participant)):
        await _end_combat_for_grace_period(uuid.uuid4())
    remove_participant.assert_not_awaited()


@pytest.mark.asyncio
async def test_grace_period_is_a_no_op_without_a_combat_service() -> None:
    with patch(_GET_SERVICE, return_value=None):
        await _end_combat_for_grace_period(uuid.uuid4())


@pytest.mark.asyncio
async def test_grace_period_swallows_cleanup_errors() -> None:
    """Combat cleanup is best effort: a failing removal must not break the grace-period flow."""
    combat, _ = _combat()
    remove_participant: AsyncMock = AsyncMock(side_effect=RuntimeError("boom"))

    with patch(_GET_SERVICE, return_value=_service(combat, remove_participant)):
        await _end_combat_for_grace_period(uuid.uuid4())

    remove_participant.assert_awaited_once()
