"""Unit tests for server.api.admin.subject_controller."""

from __future__ import annotations

import uuid
from unittest.mock import MagicMock

import pytest
from pydantic import ValidationError

from server.api.admin.subject_controller import (
    RegisterPatternRequest,
    ValidateSubjectRequest,
    get_patterns,
    get_subject_statistics,
    register_pattern,
    require_admin_user,
    validate_subject,
)
from server.exceptions import LoggedHTTPException
from server.schemas.shared.base import SecureBaseModel
from server.services.nats_subject_manager import InvalidPatternError


@pytest.mark.parametrize(
    "model_cls,payload",
    [
        (ValidateSubjectRequest, {"subject": "some.subject"}),
        (
            RegisterPatternRequest,
            {"name": "pattern", "pattern": "some.{param}", "required_params": ["param"]},
        ),
    ],
)
def test_request_schemas_reject_unknown_field(model_cls: type[SecureBaseModel], payload: dict[str, object]) -> None:
    """#755: an extra field must be rejected, not silently discarded."""
    with pytest.raises(ValidationError):
        _ = model_cls.model_validate({**payload, "unexpected_field": "nope"})


def _admin_user() -> MagicMock:
    user = MagicMock()
    user.id = uuid.uuid4()
    user.is_admin = True
    user.username = "admin"
    return user


def test_require_admin_user_rejects_non_admin() -> None:
    user = MagicMock(is_admin=False, id=uuid.uuid4(), username="player")
    with pytest.raises(LoggedHTTPException) as ei:
        require_admin_user(current_user=user)
    assert ei.value.status_code == 403


def test_require_admin_user_allows_admin() -> None:
    user = _admin_user()
    assert require_admin_user(current_user=user) is user


@pytest.mark.asyncio
async def test_get_subject_statistics() -> None:
    mgr = MagicMock()
    mgr.get_performance_metrics.return_value = {"validations": 1}
    mgr.patterns = {"chat": MagicMock()}
    mgr._cache_enabled = True
    mgr._strict_validation = False
    result = await get_subject_statistics(subject_manager=mgr)
    assert result.status == "healthy"
    assert result.patterns_registered == 1


@pytest.mark.asyncio
async def test_validate_subject_valid() -> None:
    mgr = MagicMock()
    mgr.validate_subject.return_value = True
    req = ValidateSubjectRequest(subject="game.chat")
    result = await validate_subject(req, current_user=_admin_user(), subject_manager=mgr)
    assert result.is_valid is True
    assert result.details is None


@pytest.mark.asyncio
async def test_validate_subject_invalid() -> None:
    mgr = MagicMock()
    mgr.validate_subject.return_value = False
    req = ValidateSubjectRequest(subject="bad.subject")
    result = await validate_subject(req, current_user=_admin_user(), subject_manager=mgr)
    assert result.is_valid is False
    assert result.details is not None


@pytest.mark.asyncio
async def test_get_patterns() -> None:
    mgr = MagicMock()
    mgr.get_all_patterns.return_value = {"chat": {"pattern": "game.chat.{id}"}}
    result = await get_patterns(current_user=_admin_user(), subject_manager=mgr)
    assert result.total_count == 1


@pytest.mark.asyncio
async def test_register_pattern_success() -> None:
    mgr = MagicMock()
    req = RegisterPatternRequest(name="chat", pattern="game.chat.{id}", required_params=["id"])
    result = await register_pattern(req, current_user=_admin_user(), subject_manager=mgr)
    assert result.success is True
    mgr.register_pattern.assert_called_once()


@pytest.mark.asyncio
async def test_register_pattern_invalid() -> None:
    mgr = MagicMock()
    mgr.register_pattern.side_effect = InvalidPatternError("bad pattern")
    req = RegisterPatternRequest(name="bad", pattern="{", required_params=[])
    with pytest.raises(LoggedHTTPException) as ei:
        await register_pattern(req, current_user=_admin_user(), subject_manager=mgr)
    assert ei.value.status_code == 400
