"""Unit tests for auth invite endpoints and current-user info."""

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.user import User

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard for unit testing


@pytest.mark.asyncio
async def test_get_current_user_info():
    """Test getting current user info."""
    from server.auth.endpoints import get_current_user_info

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    response = await get_current_user_info(current_user=user)
    # Function returns a dict, not an object
    assert isinstance(response, dict)
    assert response["id"] == str(user.id)
    assert response["username"] == user.username
    assert response["email"] == user.email
    assert response["is_superuser"] == user.is_superuser


@pytest.mark.asyncio
async def test_list_invites():
    """Test listing invites."""
    from server.auth.endpoints import list_invites
    from server.schemas.auth import InviteRead

    mock_invite_manager = MagicMock()
    mock_invite = MagicMock()
    mock_invite.id = str(uuid.uuid4())
    mock_invite.invite_code = "test_invite"
    mock_invite.is_active = True
    mock_invite.used_by_user_id = None
    mock_invite.created_at = datetime.now(UTC)
    mock_invite.expires_at = datetime.now(UTC)
    list_invites_mock: AsyncMock = AsyncMock(return_value=[mock_invite])
    mock_invite_manager.list_invites = list_invites_mock

    admin_user = User(
        id=str(uuid.uuid4()),
        username="admin",
        email="admin@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )

    # _current_user is injected via Depends, so we pass it as a parameter
    response = await list_invites(
        _current_user=admin_user,
        invite_manager=mock_invite_manager,
    )

    assert len(response) == 1
    assert isinstance(response[0], InviteRead)
    assert response[0].invite_code == "test_invite"
    list_invites_mock.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_invite():
    """Test creating an invite."""
    from server.auth.endpoints import create_invite
    from server.schemas.auth import InviteRead

    mock_invite_manager = MagicMock()
    mock_invite = MagicMock()
    # InviteRead expects id as string
    invite_id = uuid.uuid4()
    mock_invite.id = str(invite_id)  # Must be string for InviteRead
    mock_invite.invite_code = "new_invite"
    mock_invite.is_active = True
    mock_invite.used_by_user_id = None
    mock_invite.created_at = datetime.now(UTC)
    mock_invite.expires_at = datetime.now(UTC)
    create_invite_mock: AsyncMock = AsyncMock(return_value=mock_invite)
    mock_invite_manager.create_invite = create_invite_mock

    admin_user = User(
        id=str(uuid.uuid4()),
        username="admin",
        email="admin@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )

    # _current_user is injected via Depends, so we pass it as a parameter
    response = await create_invite(
        _current_user=admin_user,
        invite_manager=mock_invite_manager,
    )

    assert isinstance(response, InviteRead)
    assert response.invite_code == "new_invite"
    create_invite_mock.assert_awaited_once()


@pytest.mark.asyncio
async def test_list_invites_empty_list():
    """Test listing invites when list is empty."""
    from server.auth.endpoints import list_invites

    mock_invite_manager = MagicMock()
    list_invites_mock: AsyncMock = AsyncMock(return_value=[])
    mock_invite_manager.list_invites = list_invites_mock

    admin_user = User(
        id=str(uuid.uuid4()),
        username="admin",
        email="admin@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )

    response = await list_invites(
        _current_user=admin_user,
        invite_manager=mock_invite_manager,
    )

    assert response == []
    list_invites_mock.assert_awaited_once()


@pytest.mark.asyncio
async def test_list_invites_with_used_invite():
    """Test listing invites with a used invite."""
    from server.auth.endpoints import list_invites

    mock_invite_manager = MagicMock()
    mock_invite = MagicMock()
    mock_invite.id = str(uuid.uuid4())
    mock_invite.invite_code = "used_invite"
    mock_invite.is_active = False
    mock_invite.used_by_user_id = str(uuid.uuid4())
    mock_invite.created_at = datetime.now(UTC)
    mock_invite.expires_at = datetime.now(UTC)
    mock_invite_manager.list_invites = AsyncMock(return_value=[mock_invite])

    admin_user = User(
        id=str(uuid.uuid4()),
        username="admin",
        email="admin@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )

    response = await list_invites(
        _current_user=admin_user,
        invite_manager=mock_invite_manager,
    )

    assert len(response) == 1
    assert response[0].is_active is False
    assert response[0].used_by_user_id is not None


@pytest.mark.asyncio
async def test_list_invites_with_expired_invite():
    """Test listing invites with an expired invite."""
    from server.auth.endpoints import list_invites

    mock_invite_manager = MagicMock()
    mock_invite = MagicMock()
    mock_invite.id = str(uuid.uuid4())
    mock_invite.invite_code = "expired_invite"
    mock_invite.is_active = True
    mock_invite.used_by_user_id = None
    mock_invite.created_at = datetime.now(UTC) - timedelta(days=10)
    mock_invite.expires_at = datetime.now(UTC) - timedelta(days=1)  # Expired
    mock_invite_manager.list_invites = AsyncMock(return_value=[mock_invite])

    admin_user = User(
        id=str(uuid.uuid4()),
        username="admin",
        email="admin@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )

    response = await list_invites(
        _current_user=admin_user,
        invite_manager=mock_invite_manager,
    )

    assert len(response) == 1
    assert response[0].invite_code == "expired_invite"
    assert response[0].expires_at is not None


@pytest.mark.asyncio
async def test_create_invite_success():
    """Test creating an invite successfully."""
    from server.auth.endpoints import create_invite
    from server.schemas.auth import InviteRead

    mock_invite_manager = MagicMock()
    mock_invite = MagicMock()
    invite_id = uuid.uuid4()
    mock_invite.id = str(invite_id)
    mock_invite.invite_code = "new_invite_code"
    mock_invite.is_active = True
    mock_invite.used_by_user_id = None
    mock_invite.created_at = datetime.now(UTC)
    mock_invite.expires_at = datetime.now(UTC)
    create_invite_mock: AsyncMock = AsyncMock(return_value=mock_invite)
    mock_invite_manager.create_invite = create_invite_mock

    admin_user = User(
        id=str(uuid.uuid4()),
        username="admin",
        email="admin@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )

    response = await create_invite(
        _current_user=admin_user,
        invite_manager=mock_invite_manager,
    )

    assert isinstance(response, InviteRead)
    assert response.invite_code == "new_invite_code"
    assert response.is_active is True
    create_invite_mock.assert_awaited_once()
