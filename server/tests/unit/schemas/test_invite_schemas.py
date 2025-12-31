"""
Unit tests for invite schemas.

Tests the Pydantic models in invite.py module.
"""

from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from server.schemas.invite import InviteBase, InviteCreate, InviteRead, InviteUpdate


def test_invite_base():
    """Test InviteBase can be instantiated."""
    invite = InviteBase(invite_code="ABC123")

    assert invite.invite_code == "ABC123"
    assert invite.is_active is True


def test_invite_base_defaults():
    """Test InviteBase has correct default values."""
    invite = InviteBase(invite_code="ABC123", is_active=False)

    assert invite.is_active is False


def test_invite_base_validation():
    """Test InviteBase validates invite_code length."""
    with pytest.raises(ValidationError):
        InviteBase(invite_code="")


def test_invite_create():
    """Test InviteCreate can be instantiated."""
    expires_at = datetime.now(UTC)
    invite = InviteCreate(invite_code="ABC123", expires_at=expires_at)

    assert invite.invite_code == "ABC123"
    assert invite.is_active is True
    assert invite.expires_at == expires_at


def test_invite_create_no_expiry():
    """Test InviteCreate can be instantiated without expiry."""
    invite = InviteCreate(invite_code="ABC123")

    assert invite.invite_code == "ABC123"
    assert invite.expires_at is None


def test_invite_read():
    """Test InviteRead can be instantiated."""
    invite_id = "123e4567-e89b-12d3-a456-426614174000"
    created_at = datetime.now(UTC)
    expires_at = datetime.now(UTC)

    invite = InviteRead(
        id=invite_id,
        invite_code="ABC123",
        created_at=created_at,
        expires_at=expires_at,
    )

    assert invite.id == invite_id
    assert invite.invite_code == "ABC123"
    assert invite.is_active is True
    assert invite.used_by_user_id is None


def test_invite_read_with_used_by():
    """Test InviteRead with used_by_user_id."""
    invite_id = "123e4567-e89b-12d3-a456-426614174000"
    user_id = "456e7890-e89b-12d3-a456-426614174000"
    created_at = datetime.now(UTC)

    invite = InviteRead(
        id=invite_id,
        invite_code="ABC123",
        created_at=created_at,
        used_by_user_id=user_id,
    )

    assert invite.used_by_user_id == user_id


def test_invite_update():
    """Test InviteUpdate can be instantiated with optional fields."""
    invite = InviteUpdate(invite_code="NEW123")

    assert invite.invite_code == "NEW123"
    assert invite.is_active is None
    assert invite.used_by_user_id is None
    assert invite.expires_at is None


def test_invite_update_all_optional():
    """Test InviteUpdate can be instantiated with all fields optional."""
    invite = InviteUpdate()

    assert invite.invite_code is None
    assert invite.is_active is None
    assert invite.used_by_user_id is None
    assert invite.expires_at is None


def test_invite_update_validation():
    """Test InviteUpdate validates invite_code length when provided."""
    with pytest.raises(ValidationError):
        InviteUpdate(invite_code="")
