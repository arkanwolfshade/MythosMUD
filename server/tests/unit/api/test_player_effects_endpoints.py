"""Unit tests for server.api.player_effects route handlers.

#734: these endpoints are admin-only (no legitimate client ever calls them; real gameplay
effects go through the service layer in-process). Every handler now enforces
AdminAction.APPLY_PLAYER_EFFECT via validate_permission, so callers must be superusers.
"""

import uuid
from collections.abc import Awaitable, Callable
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import HTTPException, Request

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
from server.schemas.players import EffectResponse
from server.schemas.players.player_requests import (
    CorruptionRequest,
    DamageRequest,
    FearRequest,
    HealRequest,
    LucidityLossRequest,
    OccultKnowledgeRequest,
)


def _user(*, is_superuser: bool = True) -> MagicMock:
    u = MagicMock()
    u.id = uuid.uuid4()
    u.username = "test-admin"
    u.is_superuser = is_superuser
    return u


def _request() -> MagicMock:
    req = MagicMock(spec=Request)
    req.client = MagicMock()
    req.client.host = "127.0.0.1"
    return req


@pytest.mark.asyncio
async def test_apply_lucidity_loss_success() -> None:
    svc = MagicMock()
    svc.apply_lucidity_loss = AsyncMock(return_value={"message": "ok"})
    pid = uuid.uuid4()
    out = await apply_lucidity_loss(
        pid,
        LucidityLossRequest(amount=1, source="s"),
        _request(),
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
            _request(),
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
        _request(),
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
        _request(),
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
        _request(),
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
        _request(),
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
        _request(),
        _user(),
        svc,
    )
    assert out.message == "dmg"


EffectHandler = Callable[..., Awaitable[EffectResponse]]

_DENIAL_CASES: list[tuple[EffectHandler, object]] = [
    (apply_lucidity_loss, LucidityLossRequest(amount=1, source="s")),
    (apply_fear, FearRequest(amount=1, source="s")),
    (apply_corruption, CorruptionRequest(amount=1, source="s")),
    (gain_occult_knowledge, OccultKnowledgeRequest(amount=1, source="s")),
    (heal_player, HealRequest(amount=1)),
    (damage_player, DamageRequest(amount=1, damage_type="physical")),
]


@pytest.mark.asyncio
@pytest.mark.parametrize("handler,request_data", _DENIAL_CASES)
async def test_effect_endpoint_rejects_non_superuser(handler: EffectHandler, request_data: object) -> None:
    """#734: a non-superuser (ordinary player) must be denied, not merely logged."""
    svc = MagicMock()
    pid = uuid.uuid4()
    with pytest.raises(HTTPException) as ei:
        _ = await handler(pid, request_data, _request(), _user(is_superuser=False), svc)
    assert ei.value.status_code == 403
    assert svc.mock_calls == []  # denied before the service layer is ever touched
