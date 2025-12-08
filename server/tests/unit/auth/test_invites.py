"""
Tests for Invite Management System.

This module tests the invite-only registration system including invite creation,
validation, and tracking functionality.

AI Agent: Tests for InviteManager covering invite lifecycle, validation logic,
         and error handling. Created for fresh session execution.
"""

# pylint: disable=redefined-outer-name,protected-access
# Justification: pytest fixtures redefine names, protected access needed for testing internals

from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, Mock, patch

import pytest


# Note: These imports will trigger bcrypt in same session as other tests
# Run in fresh terminal: uv run pytest server/tests/unit/auth/test_invites.py -v
@pytest.fixture
def invites_module():
    """Lazily import invites module."""
    from server.auth import invites

    return invites


@pytest.fixture
def mock_session():
    """Provide mock database session."""
    session = AsyncMock()
    session.add = Mock()
    session.commit = AsyncMock()
    session.refresh = AsyncMock()
    session.execute = AsyncMock()
    return session


@pytest.fixture
def mock_valid_invite():
    """Provide mock valid invite."""
    invite = Mock()
    invite.invite_code = "VALID-CODE-123"
    invite.is_active = True
    invite.expires_at = datetime.now(UTC) + timedelta(days=30)
    invite.used_at = None
    invite.used_by_player_id = None
    invite.is_valid = Mock(return_value=True)
    return invite


@pytest.fixture
def mock_expired_invite():
    """Provide mock expired invite."""
    invite = Mock()
    invite.invite_code = "EXPIRED-CODE-456"
    invite.is_active = True
    invite.expires_at = datetime.now(UTC) - timedelta(days=1)
    invite.used_at = None
    invite.is_valid = Mock(return_value=False)
    return invite


@pytest.fixture
def mock_used_invite():
    """Provide mock used invite."""
    invite = Mock()
    invite.invite_code = "USED-CODE-789"
    invite.is_active = False
    invite.expires_at = datetime.now(UTC) + timedelta(days=30)
    invite.used_at = datetime.now(UTC)
    invite.used_by_player_id = "player123"
    invite.is_valid = Mock(return_value=False)
    return invite


class TestInviteManagerInit:
    """Test InviteManager initialization."""

    def test_initialization(self, invites_module, mock_session):
        """Test InviteManager initializes with session."""
        manager = invites_module.InviteManager(mock_session)

        assert manager.session == mock_session


class TestCreateInvite:
    """Test invite creation."""

    @pytest.mark.asyncio
    @patch("server.auth.invites.Invite._generate_invite_code")
    async def test_create_invite_with_default_expiration(self, mock_generate_code, invites_module, mock_session):
        """Test creating invite with default 30-day expiration."""
        mock_generate_code.return_value = "GEN-CODE-123"

        manager = invites_module.InviteManager(mock_session)
        _ = await manager.create_invite()

        # Verify invite was added and committed
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once()

    @pytest.mark.asyncio
    @patch("server.auth.invites.Invite._generate_invite_code")
    async def test_create_invite_with_custom_expiration(self, mock_generate_code, invites_module, mock_session):
        """Test creating invite with custom expiration."""
        mock_generate_code.return_value = "CUSTOM-CODE"

        manager = invites_module.InviteManager(mock_session)
        _ = await manager.create_invite(expires_in_days=7)

        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()


class TestListInvites:
    """Test invite listing."""

    @pytest.mark.asyncio
    async def test_list_invites_returns_all(self, invites_module, mock_session, mock_valid_invite):
        """Test list_invites returns all invites."""
        mock_result = Mock()
        mock_scalars = Mock()
        mock_scalars.all.return_value = [mock_valid_invite]
        mock_result.scalars.return_value = mock_scalars
        mock_session.execute.return_value = mock_result

        manager = invites_module.InviteManager(mock_session)
        invites = await manager.list_invites()

        assert len(invites) == 1
        assert invites[0] == mock_valid_invite
        mock_session.execute.assert_called_once()

    @pytest.mark.asyncio
    async def test_list_invites_returns_empty_list(self, invites_module, mock_session):
        """Test list_invites returns empty list when no invites."""
        mock_result = Mock()
        mock_scalars = Mock()
        mock_scalars.all.return_value = []
        mock_result.scalars.return_value = mock_scalars
        mock_session.execute.return_value = mock_result

        manager = invites_module.InviteManager(mock_session)
        invites = await manager.list_invites()

        assert invites == []


class TestValidateInvite:
    """Test invite validation."""

    @pytest.mark.asyncio
    async def test_validate_invite_rejects_none_code(self, invites_module, mock_session):
        """Test validation rejects None invite code."""
        from server.exceptions import LoggedHTTPException

        manager = invites_module.InviteManager(mock_session)

        with pytest.raises(LoggedHTTPException) as exc_info:
            await manager.validate_invite(None)

        assert exc_info.value.status_code == 400
        assert "required" in exc_info.value.detail.lower()

    @pytest.mark.asyncio
    async def test_validate_invite_rejects_empty_code(self, invites_module, mock_session):
        """Test validation rejects empty string invite code."""
        from server.exceptions import LoggedHTTPException

        manager = invites_module.InviteManager(mock_session)

        with pytest.raises(LoggedHTTPException) as exc_info:
            await manager.validate_invite("")

        assert exc_info.value.status_code == 400

    @pytest.mark.asyncio
    async def test_validate_invite_rejects_nonexistent_code(self, invites_module, mock_session):
        """Test validation rejects non-existent invite code."""
        from server.exceptions import LoggedHTTPException

        mock_result = Mock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_result

        manager = invites_module.InviteManager(mock_session)

        with pytest.raises(LoggedHTTPException) as exc_info:
            await manager.validate_invite("NONEXISTENT")

        assert exc_info.value.status_code == 400
        assert "Invalid invite code" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_validate_invite_rejects_expired_invite(self, invites_module, mock_session, mock_expired_invite):
        """Test validation rejects expired invite."""
        from server.exceptions import LoggedHTTPException

        mock_result = Mock()
        mock_result.scalar_one_or_none.return_value = mock_expired_invite
        mock_session.execute.return_value = mock_result

        manager = invites_module.InviteManager(mock_session)

        with pytest.raises(LoggedHTTPException) as exc_info:
            await manager.validate_invite("EXPIRED-CODE")

        assert exc_info.value.status_code == 400
        assert "expired" in exc_info.value.detail.lower() or "used" in exc_info.value.detail.lower()

    @pytest.mark.asyncio
    async def test_validate_invite_rejects_used_invite(self, invites_module, mock_session, mock_used_invite):
        """Test validation rejects used invite."""
        from server.exceptions import LoggedHTTPException

        mock_result = Mock()
        mock_result.scalar_one_or_none.return_value = mock_used_invite
        mock_session.execute.return_value = mock_result

        manager = invites_module.InviteManager(mock_session)

        with pytest.raises(LoggedHTTPException) as exc_info:
            await manager.validate_invite("USED-CODE")

        assert exc_info.value.status_code == 400

    @pytest.mark.asyncio
    async def test_validate_invite_accepts_valid_invite(self, invites_module, mock_session, mock_valid_invite):
        """Test validation accepts valid invite."""
        mock_result = Mock()
        mock_result.scalar_one_or_none.return_value = mock_valid_invite
        mock_session.execute.return_value = mock_result

        manager = invites_module.InviteManager(mock_session)
        result = await manager.validate_invite("VALID-CODE")

        assert result == mock_valid_invite
        mock_valid_invite.is_valid.assert_called_once()
