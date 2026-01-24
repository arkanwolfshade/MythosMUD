"""
Unit tests for authentication utilities.
"""

from datetime import timedelta
from typing import Any

import pytest
from jose import JWTError

from server.auth_utils import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)
from server.exceptions import AuthenticationError


@pytest.fixture(autouse=True)
def setup_jwt_secret(monkeypatch):
    """Set JWT secret for tests."""
    monkeypatch.setenv("MYTHOSMUD_JWT_SECRET", "test-secret-key-for-testing-only")


def test_hash_password_success():
    """Test successful password hashing."""
    password = "test_password_123"
    hashed = hash_password(password)

    assert isinstance(hashed, str)
    assert hashed != password
    assert len(hashed) > 0


def test_verify_password_success():
    """Test successful password verification."""
    password = "test_password_123"
    hashed = hash_password(password)

    result = verify_password(password, hashed)
    assert result is True


def test_verify_password_failure():
    """Test password verification with wrong password."""
    password = "test_password_123"
    hashed = hash_password(password)

    result = verify_password("wrong_password", hashed)
    assert result is False


def test_hash_password_raises_on_error(monkeypatch):
    """Test that hash_password raises AuthenticationError on error."""
    # Mock argon2_hash_password to raise an error
    from unittest.mock import patch

    with patch("server.auth_utils.argon2_hash_password", side_effect=ValueError("test error")):
        with pytest.raises(AuthenticationError):
            hash_password("test")


def test_verify_password_returns_false_on_error(monkeypatch):
    """Test that verify_password returns False on error."""
    # Mock argon2_verify_password to raise an error
    from unittest.mock import patch

    with patch("server.auth_utils.argon2_verify_password", side_effect=ValueError("test error")):
        result = verify_password("test", "hash")
        assert result is False


def test_create_access_token_success():
    """Test successful access token creation."""
    data = {"sub": "testuser", "username": "testuser"}
    token = create_access_token(data)

    assert isinstance(token, str)
    assert len(token) > 0


def test_create_access_token_with_expires_delta():
    """Test access token creation with custom expiration."""
    data = {"sub": "testuser", "username": "testuser"}
    expires_delta = timedelta(minutes=30)
    token = create_access_token(data, expires_delta=expires_delta)

    assert isinstance(token, str)
    assert len(token) > 0


def test_decode_access_token_success():
    """Test successful access token decoding."""
    data = {"sub": "testuser", "username": "testuser"}
    token = create_access_token(data)

    decoded = decode_access_token(token)
    assert decoded is not None
    assert decoded.get("sub") == "testuser"
    assert decoded.get("username") == "testuser"


def test_decode_access_token_invalid():
    """Test decoding invalid access token returns None."""
    result = decode_access_token("invalid_token")
    assert result is None


def test_decode_access_token_expired():
    """Test decoding expired access token returns None."""
    data = {"sub": "testuser", "username": "testuser"}
    # Create token with very short expiration
    expires_delta = timedelta(seconds=-1)  # Already expired
    token = create_access_token(data, expires_delta=expires_delta)

    # decode_access_token returns None on error, doesn't raise
    result = decode_access_token(token)
    assert result is None


def test_create_access_token_with_custom_secret():
    """Test access token creation with custom secret key."""
    data = {"sub": "testuser", "username": "testuser"}
    custom_secret = "custom-secret-key"
    token = create_access_token(data, secret_key=custom_secret)

    # Should decode with same secret
    decoded = decode_access_token(token, secret_key=custom_secret)
    assert decoded is not None
    assert decoded.get("sub") == "testuser"


def test_create_access_token_with_none_secret():
    """Test create_access_token raises AuthenticationError when secret is None."""
    data = {"sub": "testuser"}
    with pytest.raises(AuthenticationError, match="JWT secret key is not configured"):
        create_access_token(data, secret_key=None)


def test_decode_access_token_none_token():
    """Test decode_access_token with None token returns None."""
    result = decode_access_token(None)
    assert result is None


def test_decode_access_token_none_secret():
    """Test decode_access_token with None secret returns None."""
    token = create_access_token({"sub": "testuser"})
    result = decode_access_token(token, secret_key=None)
    assert result is None


def test_decode_access_token_wrong_secret():
    """Test decode_access_token with wrong secret returns None."""
    token = create_access_token({"sub": "testuser"})
    result = decode_access_token(token, secret_key="wrong-secret")
    assert result is None


def test_create_access_token_jwt_error():
    """Test create_access_token handles JWTError."""
    from unittest.mock import patch

    data = {"sub": "testuser"}
    with patch("jose.jwt.encode") as mock_encode:
        mock_encode.side_effect = JWTError("JWT error")
        with pytest.raises(AuthenticationError, match="Failed to create access token"):
            create_access_token(data)


def test_create_access_token_value_error():
    """Test create_access_token handles ValueError."""
    from unittest.mock import patch

    data = {"sub": "testuser"}
    with patch("jose.jwt.encode") as mock_encode:
        mock_encode.side_effect = ValueError("Value error")
        with pytest.raises(AuthenticationError, match="Failed to create access token"):
            create_access_token(data)


def test_decode_access_token_value_error():
    """Test decode_access_token handles ValueError and returns None."""
    from unittest.mock import patch

    token = create_access_token({"sub": "testuser"})
    with patch("jose.jwt.decode") as mock_decode:
        mock_decode.side_effect = ValueError("Value error")
        result = decode_access_token(token)
        assert result is None


def test_decode_access_token_type_error():
    """Test decode_access_token handles TypeError and returns None."""
    from unittest.mock import patch

    token = create_access_token({"sub": "testuser"})
    with patch("jose.jwt.decode") as mock_decode:
        mock_decode.side_effect = TypeError("Type error")
        result = decode_access_token(token)
        assert result is None


def test_decode_access_token_runtime_error():
    """Test decode_access_token handles RuntimeError and returns None."""
    from unittest.mock import patch

    token = create_access_token({"sub": "testuser"})
    with patch("jose.jwt.decode") as mock_decode:
        mock_decode.side_effect = RuntimeError("Runtime error")
        result = decode_access_token(token)
        assert result is None


def test_hash_password_authentication_error():
    """Test hash_password raises AuthenticationError on AuthenticationError from argon2."""
    from unittest.mock import patch

    from server.exceptions import AuthenticationError as AuthError

    with patch("server.auth_utils.argon2_hash_password", side_effect=AuthError("Auth error")):
        with pytest.raises(AuthenticationError):
            hash_password("test")


def test_hash_password_value_error():
    """Test hash_password raises AuthenticationError on ValueError."""
    from unittest.mock import patch

    with patch("server.auth_utils.argon2_hash_password", side_effect=ValueError("Value error")):
        with pytest.raises(AuthenticationError):
            hash_password("test")


def test_hash_password_type_error():
    """Test hash_password raises AuthenticationError on TypeError."""
    from unittest.mock import patch

    with patch("server.auth_utils.argon2_hash_password", side_effect=TypeError("Type error")):
        with pytest.raises(AuthenticationError):
            hash_password("test")


def test_hash_password_runtime_error():
    """Test hash_password raises AuthenticationError on RuntimeError."""
    from unittest.mock import patch

    with patch("server.auth_utils.argon2_hash_password", side_effect=RuntimeError("Runtime error")):
        with pytest.raises(AuthenticationError):
            hash_password("test")


def test_verify_password_attribute_error():
    """Test verify_password handles AttributeError and returns False."""
    from unittest.mock import patch

    with patch("server.auth_utils.argon2_verify_password", side_effect=AttributeError("Attr error")):
        result = verify_password("test", "hash")
        assert result is False


def test_verify_password_runtime_error():
    """Test verify_password handles RuntimeError and returns False."""
    from unittest.mock import patch

    with patch("server.auth_utils.argon2_verify_password", side_effect=RuntimeError("Runtime error")):
        result = verify_password("test", "hash")
        assert result is False


def test_create_access_token_with_empty_data():
    """Test create_access_token with empty data dict."""
    data: dict[str, Any] = {}
    token = create_access_token(data)
    assert isinstance(token, str)
    assert len(token) > 0


def test_create_access_token_with_custom_algorithm():
    """Test create_access_token with custom algorithm."""
    data = {"sub": "testuser"}
    token = create_access_token(data, algorithm="HS256")
    assert isinstance(token, str)
    assert len(token) > 0


def test_decode_access_token_with_custom_algorithm():
    """Test decode_access_token with custom algorithm."""
    data = {"sub": "testuser"}
    token = create_access_token(data, algorithm="HS256")
    decoded = decode_access_token(token, algorithm="HS256")
    assert decoded is not None
    assert decoded.get("sub") == "testuser"


def test_decode_access_token_with_wrong_algorithm():
    """Test decode_access_token with wrong algorithm returns None."""
    data = {"sub": "testuser"}
    token = create_access_token(data, algorithm="HS256")
    # Try to decode with different algorithm
    result = decode_access_token(token, algorithm="HS512")
    assert result is None


def test_create_access_token_attribute_error():
    """Test create_access_token handles AttributeError."""
    from unittest.mock import patch

    data = {"sub": "testuser"}
    with patch("jose.jwt.encode") as mock_encode:
        mock_encode.side_effect = AttributeError("Attribute error")
        with pytest.raises(AuthenticationError, match="Failed to create access token"):
            create_access_token(data)


def test_create_access_token_runtime_error():
    """Test create_access_token handles RuntimeError."""
    from unittest.mock import patch

    data = {"sub": "testuser"}
    with patch("jose.jwt.encode") as mock_encode:
        mock_encode.side_effect = RuntimeError("Runtime error")
        with pytest.raises(AuthenticationError, match="Failed to create access token"):
            create_access_token(data)


def test_decode_access_token_attribute_error():
    """Test decode_access_token handles AttributeError and returns None."""
    from unittest.mock import patch

    token = create_access_token({"sub": "testuser"})
    with patch("jose.jwt.decode") as mock_decode:
        mock_decode.side_effect = AttributeError("Attribute error")
        result = decode_access_token(token)
        assert result is None


def test_hash_password_empty_string():
    """Test hashing empty string password raises AuthenticationError."""
    with pytest.raises(AuthenticationError, match="Password cannot be empty"):
        hash_password("")


def test_verify_password_empty_string():
    """Test verifying empty string password - cannot hash empty password."""
    with pytest.raises(AuthenticationError, match="Password cannot be empty"):
        hash_password("")


def test_create_access_token_with_none_expires_delta():
    """Test create_access_token with None expires_delta uses default."""
    data = {"sub": "testuser"}
    token = create_access_token(data, expires_delta=None)
    assert isinstance(token, str)
    assert len(token) > 0


def test_decode_access_token_with_empty_string():
    """Test decode_access_token with empty string token."""
    result = decode_access_token("")
    assert result is None


def test_decode_access_token_with_malformed_token():
    """Test decode_access_token with malformed token."""
    result = decode_access_token("not.a.valid.token")
    assert result is None


def test_create_access_token_with_audience():
    """Test create_access_token with audience in data."""
    # decode_access_token expects "fastapi-users:auth" audience
    # So we need to include it in the data when creating the token
    data = {"sub": "testuser", "aud": ["fastapi-users:auth"]}
    token = create_access_token(data)
    decoded = decode_access_token(token)
    assert decoded is not None
    assert decoded.get("sub") == "testuser"


def test_hash_password_with_very_long_password():
    """Test hashing a very long password raises AuthenticationError."""
    long_password = "a" * 10000
    with pytest.raises(AuthenticationError, match="Password must not exceed 1024 characters"):
        hash_password(long_password)


def test_verify_password_with_very_long_password():
    """Test verifying a very long password - cannot hash password exceeding limit."""
    long_password = "a" * 10000
    with pytest.raises(AuthenticationError, match="Password must not exceed 1024 characters"):
        hash_password(long_password)


def test_create_access_token_with_custom_expires_delta_zero():
    """Test create_access_token with zero expires_delta."""
    data = {"sub": "testuser"}
    expires_delta = timedelta(seconds=0)
    token = create_access_token(data, expires_delta=expires_delta)
    assert isinstance(token, str)
    assert len(token) > 0


def test_decode_access_token_with_expired_token_immediately():
    """Test decode_access_token with immediately expired token."""
    data = {"sub": "testuser"}
    expires_delta = timedelta(seconds=-1)
    token = create_access_token(data, expires_delta=expires_delta)
    result = decode_access_token(token)
    assert result is None
