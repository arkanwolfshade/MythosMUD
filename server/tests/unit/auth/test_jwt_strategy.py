"""Unit tests for restart-invalidating JWT strategy."""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.auth.jwt_strategy import RestartInvalidatingJWTStrategy
from server.auth.token_epoch import get_auth_epoch, set_auth_epoch


@pytest.mark.asyncio
async def test_read_token_rejects_wrong_epoch():
    """Tokens with srv claim different from current epoch are rejected."""
    set_auth_epoch("current-epoch")

    strategy = RestartInvalidatingJWTStrategy(
        secret="test-secret",
        lifetime_seconds=3600,
        token_audience=["fastapi-users:auth"],
    )

    # Create a valid JWT payload but with wrong epoch (simulate pre-restart token)
    from fastapi_users.jwt import generate_jwt

    wrong_epoch_data = {
        "sub": str(uuid.uuid4()),
        "aud": ["fastapi-users:auth"],
        "srv": "old-epoch-from-before-restart",
    }
    token = generate_jwt(wrong_epoch_data, "test-secret", 3600)

    user_manager = MagicMock()
    user_manager.parse_id = MagicMock(return_value=uuid.uuid4())
    user_manager.get = AsyncMock(return_value=MagicMock())

    result = await strategy.read_token(token, user_manager)

    assert result is None
    user_manager.get.assert_not_awaited()


@pytest.mark.asyncio
async def test_read_token_rejects_missing_epoch():
    """Tokens without srv claim (issued before restart invalidation) are rejected."""
    set_auth_epoch("current-epoch")

    strategy = RestartInvalidatingJWTStrategy(
        secret="test-secret",
        lifetime_seconds=3600,
        token_audience=["fastapi-users:auth"],
    )

    from fastapi_users.jwt import generate_jwt

    no_epoch_data = {"sub": str(uuid.uuid4()), "aud": ["fastapi-users:auth"]}
    token = generate_jwt(no_epoch_data, "test-secret", 3600)

    user_manager = MagicMock()
    result = await strategy.read_token(token, user_manager)

    assert result is None


@pytest.mark.asyncio
async def test_read_token_accepts_matching_epoch():
    """Tokens with srv matching current epoch are accepted (user lookup proceeds)."""
    set_auth_epoch("matching-epoch")

    strategy = RestartInvalidatingJWTStrategy(
        secret="test-secret",
        lifetime_seconds=3600,
        token_audience=["fastapi-users:auth"],
    )

    from fastapi_users.jwt import generate_jwt

    user_id = uuid.uuid4()
    correct_data = {
        "sub": str(user_id),
        "aud": ["fastapi-users:auth"],
        "srv": get_auth_epoch(),
    }
    token = generate_jwt(correct_data, "test-secret", 3600)

    mock_user = MagicMock()
    user_manager = MagicMock()
    user_manager.parse_id = MagicMock(return_value=user_id)
    user_manager.get = AsyncMock(return_value=mock_user)

    result = await strategy.read_token(token, user_manager)

    assert result is mock_user
    user_manager.get.assert_awaited_once()
