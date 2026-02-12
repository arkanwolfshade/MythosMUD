"""
Unit tests for user schemas.

Tests the Pydantic models in user.py module.
"""

import uuid
from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from server.schemas.auth import UserBase, UserCreate, UserRead, UserUpdate


def test_user_base():
    """Test UserBase can be instantiated."""
    user = UserBase(username="testuser")

    assert user.username == "testuser"
    assert user.is_active is True
    assert user.is_superuser is False


def test_user_base_defaults():
    """Test UserBase has correct default values."""
    user = UserBase(username="testuser", is_active=False, is_superuser=True)

    assert user.is_active is False
    assert user.is_superuser is True


def test_user_create():
    """Test UserCreate can be instantiated."""
    user = UserCreate(username="testuser", password="password123")

    assert user.username == "testuser"
    assert user.password == "password123"
    assert user.is_active is True
    assert user.is_superuser is False


def test_user_create_password_validation():
    """Test UserCreate validates password length."""
    with pytest.raises(ValidationError):
        UserCreate(username="testuser", password="short")


def test_user_read():
    """Test UserRead can be instantiated."""
    user_id = uuid.uuid4()
    created_at = datetime.now(UTC)
    updated_at = datetime.now(UTC)

    user = UserRead(
        user_id=user_id,
        username="testuser",
        created_at=created_at,
        updated_at=updated_at,
    )

    assert user.user_id == user_id
    assert user.username == "testuser"
    assert user.is_active is True
    assert user.is_superuser is False


def test_user_update():
    """Test UserUpdate can be instantiated with optional fields."""
    user = UserUpdate(username="newuser")

    assert user.username == "newuser"
    assert user.password is None
    assert user.is_active is None
    assert user.is_superuser is None


def test_user_update_all_optional():
    """Test UserUpdate can be instantiated with all fields optional."""
    user = UserUpdate()

    assert user.username is None
    assert user.password is None
    assert user.is_active is None
    assert user.is_superuser is None


def test_user_update_password_validation():
    """Test UserUpdate validates password length when provided."""
    with pytest.raises(ValidationError):
        UserUpdate(password="short")
