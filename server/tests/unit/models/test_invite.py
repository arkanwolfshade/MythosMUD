"""
Unit tests for the Invite model.

Tests the Invite model methods including validation, expiration checking, and invite creation.
"""

from datetime import UTC, datetime, timedelta
from unittest.mock import patch

from server.models.invite import Invite


def test_invite_is_expired_with_future_expiry() -> None:
    """Test is_expired returns False for future expiry date."""
    invite = Invite()
    invite.expires_at = (datetime.now(UTC) + timedelta(days=1)).replace(tzinfo=None)

    assert invite.is_expired() is False


def test_invite_is_expired_with_past_expiry() -> None:
    """Test is_expired returns True for past expiry date."""
    invite = Invite()
    invite.expires_at = (datetime.now(UTC) - timedelta(days=1)).replace(tzinfo=None)

    assert invite.is_expired() is True


def test_invite_is_expired_with_aware_datetime() -> None:
    """Test is_expired handles timezone-aware datetime."""
    invite = Invite()
    invite.expires_at = datetime.now(UTC) + timedelta(days=1)

    assert invite.is_expired() is False


def test_invite_is_valid_with_active_and_not_expired() -> None:
    """Test is_valid returns True for active, non-expired invite."""
    invite = Invite()
    invite.is_active = True
    invite.expires_at = (datetime.now(UTC) + timedelta(days=1)).replace(tzinfo=None)

    assert invite.is_valid() is True


def test_invite_is_valid_with_inactive() -> None:
    """Test is_valid returns False for inactive invite."""
    invite = Invite()
    invite.is_active = False
    invite.expires_at = (datetime.now(UTC) + timedelta(days=1)).replace(tzinfo=None)

    assert invite.is_valid() is False


def test_invite_is_valid_with_expired() -> None:
    """Test is_valid returns False for expired invite."""
    invite = Invite()
    invite.is_active = True
    invite.expires_at = (datetime.now(UTC) - timedelta(days=1)).replace(tzinfo=None)

    assert invite.is_valid() is False


def test_invite_is_valid_with_inactive_and_expired() -> None:
    """Test is_valid returns False for inactive and expired invite."""
    invite = Invite()
    invite.is_active = False
    invite.expires_at = (datetime.now(UTC) - timedelta(days=1)).replace(tzinfo=None)

    assert invite.is_valid() is False


def test_invite_use_invite() -> None:
    """Test use_invite marks invite as used and sets user_id."""
    invite = Invite()
    invite.is_active = True
    user_id = "test-user-id-123"

    invite.use_invite(user_id)

    assert invite.is_active is False
    assert invite.used_by_user_id == user_id


def test_invite_create_invite_defaults() -> None:
    """Test create_invite creates invite with default parameters."""
    with patch("server.models.invite.Invite._generate_invite_code", return_value="TESTCODE123"):
        invite = Invite.create_invite()

        assert invite.invite_code == "TESTCODE123"
        assert invite.created_by_user_id is None
        # is_active defaults to True in the column definition
        # With Mapped types, non-nullable fields have default values applied
        assert invite.is_active is True
        assert invite.expires_at is not None
        # Should expire in approximately 30 days
        expected_expiry = (datetime.now(UTC) + timedelta(days=30)).replace(tzinfo=None)
        # Allow 1 second tolerance for timing
        assert abs((invite.expires_at - expected_expiry).total_seconds()) < 1


def test_invite_create_invite_with_creator() -> None:
    """Test create_invite creates invite with creator user_id."""
    with patch("server.models.invite.Invite._generate_invite_code", return_value="TESTCODE456"):
        creator_id = "creator-user-id-456"
        invite = Invite.create_invite(created_by_user_id=creator_id)

        assert invite.invite_code == "TESTCODE456"
        assert invite.created_by_user_id == creator_id


def test_invite_create_invite_with_custom_expiry() -> None:
    """Test create_invite creates invite with custom expiry days."""
    with patch("server.models.invite.Invite._generate_invite_code", return_value="TESTCODE789"):
        invite = Invite.create_invite(expires_in_days=7)

        assert invite.invite_code == "TESTCODE789"
        # Should expire in approximately 7 days
        expected_expiry = (datetime.now(UTC) + timedelta(days=7)).replace(tzinfo=None)
        # Allow 1 second tolerance for timing
        assert abs((invite.expires_at - expected_expiry).total_seconds()) < 1


def test_invite_generate_invite_code_format() -> None:
    """Test _generate_invite_code generates 12-character alphanumeric code."""
    code = Invite._generate_invite_code()

    assert len(code) == 12
    assert code.isalnum()
    assert code.isupper() or any(c.isdigit() for c in code)


def test_invite_generate_invite_code_uniqueness() -> None:
    """Test _generate_invite_code generates different codes on multiple calls."""
    codes = [Invite._generate_invite_code() for _ in range(10)]

    # Should have at least some unique codes (very unlikely all 10 are the same)
    assert len(set(codes)) > 1


def test_invite_repr() -> None:
    """Test __repr__ returns expected string format."""
    invite = Invite()
    invite.id = "test-id-123"
    invite.invite_code = "TESTCODE123"
    invite.is_active = True

    repr_str = repr(invite)

    assert "Invite" in repr_str
    assert "test-id-123" in repr_str
    assert "TESTCODE123" in repr_str
    assert "True" in repr_str or "is_active=True" in repr_str
