"""Unit tests for server.api.player_effects route handlers."""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import Request

from server.api.player_effects import (
    apply_corruption,
    apply_fear,
    apply_lucidity_loss,
    damage_player,
    gain_occult_knowledge,
    heal_player,
)
from server.error_types import ErrorMessages
from server.exceptions import LoggedHTTPException, ValidationError
from server.schemas.players.player_requests import (
    CorruptionRequest,
    DamageRequest,
    FearRequest,
    HealRequest,
    LucidityLossRequest,
    OccultKnowledgeRequest,
)


def _user() -> MagicMock:
    u = MagicMock()
    u.id = uuid.uuid4()
    return u


@pytest.mark.asyncio
async def test_apply_lucidity_loss_success() -> None:
    svc = MagicMock()
    svc.apply_lucidity_loss = AsyncMock(return_value={"message": "ok"})
    pid = uuid.uuid4()
    out = await apply_lucidity_loss(
        pid,
        LucidityLossRequest(amount=1, source="s"),
        MagicMock(spec=Request),
        _user(),
        svc,
    )
    assert out.message == "ok"


@pytest.mark.asyncio
async def test_apply_lucidity_loss_validation_maps_to_404() -> None:
    svc = MagicMock()
    svc.apply_lucidity_loss = AsyncMock(side_effect=ValidationError("player not found"))
    pid = uuid.uuid4()
    with pytest.raises(LoggedHTTPException) as ei:
        _ = await apply_lucidity_loss(
            pid,
            LucidityLossRequest(amount=1, source="s"),
            MagicMock(spec=Request),
            _user(),
            svc,
        )
    assert ei.value.status_code == 404
    assert ErrorMessages.PLAYER_NOT_FOUND in str(ei.value.detail)


@pytest.mark.asyncio
async def test_apply_fear_success() -> None:
    svc = MagicMock()
    svc.apply_fear = AsyncMock(return_value={"message": "fear"})
    pid = uuid.uuid4()
    out = await apply_fear(
        pid,
        FearRequest(amount=2, source="x"),
        MagicMock(spec=Request),
        _user(),
        svc,
    )
    assert out.message == "fear"


@pytest.mark.asyncio
async def test_apply_corruption_success() -> None:
    svc = MagicMock()
    svc.apply_corruption = AsyncMock(return_value={"message": "c"})
    pid = uuid.uuid4()
    out = await apply_corruption(
        pid,
        CorruptionRequest(amount=1, source="y"),
        MagicMock(spec=Request),
        _user(),
        svc,
    )
    assert out.message == "c"


@pytest.mark.asyncio
async def test_gain_occult_knowledge_success() -> None:
    svc = MagicMock()
    svc.gain_occult_knowledge = AsyncMock(return_value={"message": "ok"})
    pid = uuid.uuid4()
    out = await gain_occult_knowledge(
        pid,
        OccultKnowledgeRequest(amount=1, source="z"),
        MagicMock(spec=Request),
        _user(),
        svc,
    )
    assert out.message == "ok"


@pytest.mark.asyncio
async def test_heal_player_success() -> None:
    svc = MagicMock()
    svc.heal_player = AsyncMock(return_value={"message": "healed"})
    pid = uuid.uuid4()
    out = await heal_player(
        pid,
        HealRequest(amount=5),
        MagicMock(spec=Request),
        _user(),
        svc,
    )
    assert out.message == "healed"


@pytest.mark.asyncio
async def test_damage_player_success() -> None:
    svc = MagicMock()
    svc.damage_player = AsyncMock(return_value={"message": "dmg"})
    pid = uuid.uuid4()
    out = await damage_player(
        pid,
        DamageRequest(amount=3, damage_type="physical"),
        MagicMock(spec=Request),
        _user(),
        svc,
    )
    assert out.message == "dmg"
