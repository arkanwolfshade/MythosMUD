"""
Tests for authentication utilities.

This module tests the password hashing, verification, and JWT token
creation/decoding functionality in auth_utils.py.
"""

import os
from datetime import timedelta
from unittest.mock import patch

from server.auth_utils import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    SECRET_KEY,
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)


class TestPasswordHashing:
    """Test password hashing and verification functionality."""

    def test_hash_password(self):
        """Test password hashing."""
        password = "test_password_123"
        hashed = hash_password(password)

        assert hashed != password
        assert hashed.startswith("$2b$")
        assert len(hashed) > 20

    def test_verify_password_correct(self):
        """Test password verification with correct password."""
        password = "test_password_123"
        hashed = hash_password(password)

        assert verify_password(password, hashed) is True

    def test_verify_password_incorrect(self):
        """Test password verification with incorrect password."""
        password = "test_password_123"
        wrong_password = "wrong_password_456"
        hashed = hash_password(password)

        assert verify_password(wrong_password, hashed) is False

    def test_verify_password_empty(self):
        """Test password verification with empty password."""
        password = ""
        hashed = hash_password(password)

        assert verify_password(password, hashed) is True
        assert verify_password("not_empty", hashed) is False

    def test_hash_password_special_chars(self):
        """Test password hashing with special characters."""
        password = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
        hashed = hash_password(password)

        assert verify_password(password, hashed) is True


class TestJWTTokenCreation:
    """Test JWT token creation functionality."""

    def test_create_access_token_default_expiry(self):
        """Test access token creation with default expiry."""
        data = {"sub": "test_user", "username": "test"}
        token = create_access_token(data)

        assert isinstance(token, str)
        assert len(token) > 50

    def test_create_access_token_custom_expiry(self):
        """Test access token creation with custom expiry."""
        data = {"sub": "test_user", "username": "test"}
        expires_delta = timedelta(hours=2)
        token = create_access_token(data, expires_delta=expires_delta)

        assert isinstance(token, str)
        assert len(token) > 50

    def test_create_access_token_custom_secret(self):
        """Test access token creation with custom secret key."""
        data = {"sub": "test_user", "username": "test"}
        custom_secret = "custom-secret-key"
        token = create_access_token(data, secret_key=custom_secret)

        assert isinstance(token, str)
        assert len(token) > 50

    def test_create_access_token_custom_algorithm(self):
        """Test access token creation with custom algorithm."""
        data = {"sub": "test_user", "username": "test"}
        token = create_access_token(data, algorithm="HS256")

        assert isinstance(token, str)
        assert len(token) > 50

    def test_create_access_token_empty_data(self):
        """Test access token creation with empty data."""
        data = {}
        token = create_access_token(data)

        assert isinstance(token, str)
        assert len(token) > 50

    def test_create_access_token_nested_data(self):
        """Test access token creation with nested data."""
        data = {
            "sub": "test_user",
            "username": "test",
            "roles": ["user", "admin"],
            "metadata": {"created_at": "2023-01-01"},
        }
        token = create_access_token(data)

        assert isinstance(token, str)
        assert len(token) > 50


class TestJWTTokenDecoding:
    """Test JWT token decoding functionality."""

    def test_decode_access_token_valid(self):
        """Test decoding a valid access token."""
        data = {"sub": "test_user", "username": "test"}
        token = create_access_token(data)
        decoded = decode_access_token(token)

        assert decoded is not None
        assert decoded["sub"] == "test_user"
        assert decoded["username"] == "test"
        assert "exp" in decoded

    def test_decode_access_token_custom_secret(self):
        """Test decoding with custom secret key."""
        data = {"sub": "test_user", "username": "test"}
        custom_secret = "custom-secret-key"
        token = create_access_token(data, secret_key=custom_secret)
        decoded = decode_access_token(token, secret_key=custom_secret)

        assert decoded is not None
        assert decoded["sub"] == "test_user"

    def test_decode_access_token_invalid_token(self):
        """Test decoding an invalid token."""
        invalid_token = "invalid.token.here"
        decoded = decode_access_token(invalid_token)

        assert decoded is None

    def test_decode_access_token_wrong_secret(self):
        """Test decoding with wrong secret key."""
        data = {"sub": "test_user", "username": "test"}
        token = create_access_token(data, secret_key="correct-secret")
        decoded = decode_access_token(token, secret_key="wrong-secret")

        assert decoded is None

    def test_decode_access_token_empty_token(self):
        """Test decoding an empty token."""
        decoded = decode_access_token("")

        assert decoded is None

    def test_decode_access_token_none_token(self):
        """Test decoding a None token."""
        decoded = decode_access_token(None)

        assert decoded is None


class TestConstants:
    """Test module constants."""

    def test_secret_key_default(self):
        """Test SECRET_KEY default value."""
        assert SECRET_KEY == "mythosmud-dev-secret-key-change-in-production"

    def test_algorithm_default(self):
        """Test ALGORITHM default value."""
        assert ALGORITHM == "HS256"

    def test_access_token_expire_minutes_default(self):
        """Test ACCESS_TOKEN_EXPIRE_MINUTES default value."""
        assert ACCESS_TOKEN_EXPIRE_MINUTES == 60

    @patch.dict(os.environ, {"MYTHOSMUD_SECRET_KEY": "test-secret-key"})
    def test_secret_key_from_env(self):
        """Test SECRET_KEY from environment variable."""
        # Re-import to get the updated value
        import importlib

        import server.auth_utils

        importlib.reload(server.auth_utils)

        assert server.auth_utils.SECRET_KEY == "test-secret-key"


class TestTokenExpiry:
    """Test token expiry functionality."""

    def test_token_expiry_default(self):
        """Test that tokens expire with default time."""
        data = {"sub": "test_user"}
        token = create_access_token(data)
        decoded = decode_access_token(token)

        assert decoded is not None
        assert "exp" in decoded

    def test_token_expiry_custom(self):
        """Test that tokens expire with custom time."""
        data = {"sub": "test_user"}
        expires_delta = timedelta(minutes=30)
        token = create_access_token(data, expires_delta=expires_delta)
        decoded = decode_access_token(token)

        assert decoded is not None
        assert "exp" in decoded

    def test_token_expiry_zero(self):
        """Test that tokens can be created with zero expiry."""
        data = {"sub": "test_user"}
        expires_delta = timedelta(seconds=0)
        token = create_access_token(data, expires_delta=expires_delta)
        decoded = decode_access_token(token)

        assert decoded is not None
        assert "exp" in decoded
