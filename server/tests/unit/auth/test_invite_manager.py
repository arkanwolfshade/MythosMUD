"""Unit tests for InviteManager (server.auth.invites)."""

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.auth.invites import InviteManager, get_invite_manager
from server.exceptions import LoggedHTTPException
from server.models.invite import Invite


@pytest.fixture
def mock_session():
    session = AsyncMock()
    session.commit = AsyncMock()
    session.refresh = AsyncMock()
    session.add = MagicMock()
    session.delete = AsyncMock()
    return session


@pytest.mark.asyncio
async def test_create_invite_with_default_expiry(mock_session):
    manager = InviteManager(mock_session)
    with patch.object(Invite, "_generate_invite_code", return_value="CODE123"):
        invite = await manager.create_invite()
    mock_session.add.assert_called_once()
    mock_session.commit.assert_awaited_once()
    assert invite.invite_code == "CODE123"
    assert invite.is_active is True


@pytest.mark.asyncio
async def test_create_invite_explicit_expiry(mock_session):
    manager = InviteManager(mock_session)
    expires = datetime.now(UTC) + timedelta(days=7)
    with patch.object(Invite, "_generate_invite_code", return_value="CODE456"):
        invite = await manager.create_invite(expires_at=expires)
    assert invite.expires_at == expires.replace(tzinfo=None)


@pytest.mark.asyncio
async def test_list_invites(mock_session):
    invite = MagicMock(spec=Invite)
    result = MagicMock()
    result.scalars.return_value.all.return_value = [invite]
    mock_session.execute = AsyncMock(return_value=result)
    manager = InviteManager(mock_session)
    invites = await manager.list_invites()
    assert invites == [invite]


@pytest.mark.asyncio
async def test_validate_invite_missing_code(mock_session):
    manager = InviteManager(mock_session)
    with pytest.raises(LoggedHTTPException) as exc:
        await manager.validate_invite(None)
    assert exc.value.status_code == 400


@pytest.mark.asyncio
async def test_validate_invite_not_found(mock_session):
    result = MagicMock()
    result.scalar_one_or_none.return_value = None
    mock_session.execute = AsyncMock(return_value=result)
    manager = InviteManager(mock_session)
    with pytest.raises(LoggedHTTPException) as exc:
        await manager.validate_invite("BAD")
    assert "Invalid invite code" in exc.value.detail


@pytest.mark.asyncio
async def test_validate_invite_expired(mock_session):
    invite = MagicMock(spec=Invite)
    invite.is_valid.return_value = False
    invite.is_active = False
    invite.expires_at = datetime.now(UTC)
    result = MagicMock()
    result.scalar_one_or_none.return_value = invite
    mock_session.execute = AsyncMock(return_value=result)
    manager = InviteManager(mock_session)
    with pytest.raises(LoggedHTTPException) as exc:
        await manager.validate_invite("OLD")
    assert "expired or already used" in exc.value.detail


@pytest.mark.asyncio
async def test_validate_invite_success(mock_session):
    invite = MagicMock(spec=Invite)
    invite.is_valid.return_value = True
    result = MagicMock()
    result.scalar_one_or_none.return_value = invite
    mock_session.execute = AsyncMock(return_value=result)
    manager = InviteManager(mock_session)
    assert await manager.validate_invite("GOOD") is invite


@pytest.mark.asyncio
async def test_use_invite(mock_session):
    invite = MagicMock(spec=Invite)
    invite.is_valid.return_value = True
    result = MagicMock()
    result.scalar_one_or_none.return_value = invite
    mock_session.execute = AsyncMock(return_value=result)
    user_id = uuid.uuid4()
    manager = InviteManager(mock_session)
    used = await manager.use_invite("GOOD", user_id)
    invite.use_invite.assert_called_once_with(str(user_id))
    assert used is invite


@pytest.mark.asyncio
async def test_get_user_invites(mock_session):
    invite = MagicMock(spec=Invite)
    result = MagicMock()
    result.scalars.return_value.all.return_value = [invite]
    mock_session.execute = AsyncMock(return_value=result)
    manager = InviteManager(mock_session)
    user_id = uuid.uuid4()
    assert await manager.get_user_invites(user_id) == [invite]


@pytest.mark.asyncio
async def test_get_unused_invites(mock_session):
    invite = MagicMock(spec=Invite)
    result = MagicMock()
    result.scalars.return_value.all.return_value = [invite]
    mock_session.execute = AsyncMock(return_value=result)
    manager = InviteManager(mock_session)
    assert await manager.get_unused_invites() == [invite]


@pytest.mark.asyncio
async def test_cleanup_expired_invites(mock_session):
    expired = MagicMock(spec=Invite)
    result = MagicMock()
    result.scalars.return_value.all.return_value = [expired, MagicMock()]
    mock_session.execute = AsyncMock(return_value=result)
    manager = InviteManager(mock_session)
    removed = await manager.cleanup_expired_invites()
    assert removed == 2
    assert mock_session.delete.await_count == 2


@pytest.mark.asyncio
async def test_get_invite_manager_dependency(mock_session):
    manager = await get_invite_manager(session=mock_session)
    assert isinstance(manager, InviteManager)
