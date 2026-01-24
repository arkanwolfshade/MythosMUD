"""
Unit tests for the User model.

Tests the User model methods including authentication checks and display name retrieval.
"""

import uuid

from server.models.user import User


def test_user_repr() -> None:
    """Test __repr__ returns expected string format."""
    user = User()
    user.id = uuid.uuid4()
    user.username = "testuser"
    user.is_active = True

    repr_str = repr(user)

    assert "User" in repr_str
    assert "testuser" in repr_str
    assert "True" in repr_str or "is_active=True" in repr_str


def test_user_is_authenticated_when_active() -> None:
    """Test is_authenticated returns True when user is active."""
    user = User()
    user.is_active = True

    assert user.is_authenticated is True


def test_user_is_authenticated_when_inactive() -> None:
    """Test is_authenticated returns False when user is inactive."""
    user = User()
    user.is_active = False

    assert user.is_authenticated is False


def test_user_get_display_name_with_display_name() -> None:
    """Test get_display_name returns display_name when set."""
    user = User()
    user.display_name = "DisplayName"
    user.username = "testuser"

    result = user.get_display_name()

    assert result == "DisplayName"


def test_user_get_display_name_with_empty_display_name() -> None:
    """Test get_display_name falls back to username when display_name is empty."""
    user = User()
    user.display_name = ""
    user.username = "testuser"

    result = user.get_display_name()

    assert result == "testuser"


def test_user_get_display_name_without_display_name() -> None:
    """Test get_display_name falls back to username when display_name not set."""
    user = User()
    user.username = "testuser"
    # Don't set display_name

    result = user.get_display_name()

    assert result == "testuser"


def test_user_get_display_name_falls_back_to_id() -> None:
    """Test get_display_name falls back to id when username is not set."""
    user = User()
    user.id = uuid.uuid4()
    # Don't set username or display_name

    result = user.get_display_name()

    assert result == str(user.id)


def test_user_get_display_name_all_empty() -> None:
    """Test get_display_name handles case where all fields are empty/missing."""
    user = User()
    user.id = uuid.uuid4()
    # Don't set username or display_name

    result = user.get_display_name()

    # Should return id as last resort
    assert result == str(user.id)
