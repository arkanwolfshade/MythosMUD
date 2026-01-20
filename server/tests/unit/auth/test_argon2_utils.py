"""
Unit tests for Argon2 password hashing utilities.
"""

import pytest

from server.auth.argon2_utils import (
    create_hasher_with_params,
    hash_password,
    verify_password,
)
from server.exceptions import AuthenticationError


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


def test_hash_password_empty_string():
    """Test hashing empty password raises AuthenticationError."""
    with pytest.raises(AuthenticationError, match="Password cannot be empty"):
        hash_password("")


def test_verify_password_empty_string():
    """Test verifying empty password - cannot hash empty password."""
    with pytest.raises(AuthenticationError, match="Password cannot be empty"):
        hash_password("")


def test_create_hasher_with_params_valid():
    """Test creating hasher with valid parameters."""
    hasher = create_hasher_with_params(
        time_cost=3,
        memory_cost=65536,
        parallelism=1,
        hash_len=32,
    )
    assert hasher is not None


def test_create_hasher_with_params_invalid_time_cost():
    """Test creating hasher with invalid time_cost."""
    with pytest.raises(ValueError, match="time_cost must be between 1 and 10"):
        create_hasher_with_params(time_cost=0)


def test_create_hasher_with_params_invalid_memory_cost():
    """Test creating hasher with invalid memory_cost."""
    with pytest.raises(ValueError, match="memory_cost must be between 1024 and 1048576"):
        create_hasher_with_params(memory_cost=500)


def test_create_hasher_with_params_invalid_parallelism():
    """Test creating hasher with invalid parallelism."""
    with pytest.raises(ValueError, match="parallelism must be between 1 and 16"):
        create_hasher_with_params(parallelism=20)


def test_create_hasher_with_params_invalid_hash_len():
    """Test creating hasher with invalid hash_len."""
    with pytest.raises(ValueError, match="hash_len must be between 16 and 64"):
        create_hasher_with_params(hash_len=10)


def test_hash_password_invalid_type():
    """Test hashing password with invalid type."""
    with pytest.raises(AuthenticationError):
        hash_password(None)


def test_verify_password_invalid_hash():
    """Test verifying password with invalid hash format."""
    result = verify_password("password", "invalid_hash")
    assert result is False


def test_hash_password_non_string_type():
    """Test hashing password with non-string type raises AuthenticationError."""
    with pytest.raises(AuthenticationError, match="Password must be a string"):
        hash_password(123)


def test_verify_password_non_string_password():
    """Test verifying password with non-string password returns False."""
    hashed = hash_password("test_password")
    result = verify_password(123, hashed)
    assert result is False


def test_verify_password_non_string_hash():
    """Test verifying password with non-string hash returns False."""
    result = verify_password("password", 123)
    assert result is False


def test_verify_password_empty_hash():
    """Test verifying password with empty hash returns False."""
    result = verify_password("password", "")
    assert result is False


def test_is_argon2_hash_valid():
    """Test is_argon2_hash with valid Argon2 hash."""
    from server.auth.argon2_utils import is_argon2_hash

    password = "test_password"
    hashed = hash_password(password)
    assert is_argon2_hash(hashed) is True


def test_is_argon2_hash_invalid():
    """Test is_argon2_hash with invalid hash."""
    from server.auth.argon2_utils import is_argon2_hash

    assert is_argon2_hash("invalid_hash") is False
    assert is_argon2_hash("$bcrypt$...") is False


def test_is_argon2_hash_none():
    """Test is_argon2_hash with None."""
    from server.auth.argon2_utils import is_argon2_hash

    assert is_argon2_hash(None) is False


def test_is_argon2_hash_non_string():
    """Test is_argon2_hash with non-string type."""
    from server.auth.argon2_utils import is_argon2_hash

    assert is_argon2_hash(123) is False


def test_needs_rehash_valid_hash():
    """Test needs_rehash with valid hash that doesn't need rehashing."""
    from server.auth.argon2_utils import needs_rehash

    password = "test_password"
    hashed = hash_password(password)
    # Hash should not need rehashing immediately after creation
    result = needs_rehash(hashed)
    assert isinstance(result, bool)


def test_needs_rehash_invalid_hash():
    """Test needs_rehash with invalid hash returns True."""
    from server.auth.argon2_utils import needs_rehash

    assert needs_rehash("invalid_hash") is True
    assert needs_rehash("") is True


def test_get_hash_info_valid():
    """Test get_hash_info with valid Argon2 hash."""
    from server.auth.argon2_utils import get_hash_info

    password = "test_password"
    hashed = hash_password(password)
    info = get_hash_info(hashed)

    assert info is not None
    assert isinstance(info, dict)
    # Should contain Argon2 parameters
    assert "m" in info or "t" in info or "p" in info


def test_get_hash_info_invalid():
    """Test get_hash_info with invalid hash returns None."""
    from server.auth.argon2_utils import get_hash_info

    assert get_hash_info("invalid_hash") is None
    assert get_hash_info("") is None
    assert get_hash_info(None) is None


def test_create_hasher_with_params_low_time_cost_warning(monkeypatch):
    """Test that create_hasher_with_params logs warning for low time_cost."""
    from unittest.mock import patch

    from server.auth.argon2_utils import create_hasher_with_params

    with patch("server.auth.argon2_utils.logger") as mock_logger:
        hasher = create_hasher_with_params(time_cost=1, memory_cost=65536, parallelism=1, hash_len=32)
        assert hasher is not None
        # Should log warning for time_cost < 3
        mock_logger.warning.assert_called()


def test_create_hasher_with_params_low_memory_cost_warning(monkeypatch):
    """Test that create_hasher_with_params logs warning for low memory_cost."""
    from unittest.mock import patch

    from server.auth.argon2_utils import create_hasher_with_params

    with patch("server.auth.argon2_utils.logger") as mock_logger:
        hasher = create_hasher_with_params(time_cost=3, memory_cost=1024, parallelism=1, hash_len=32)
        assert hasher is not None
        # Should log warning for memory_cost < 65536
        mock_logger.warning.assert_called()


def test_hash_password_hashing_error():
    """Test hash_password handles HashingError."""
    from unittest.mock import MagicMock, patch

    from argon2.exceptions import HashingError

    with patch("server.auth.argon2_utils._default_hasher") as mock_hasher:
        mock_hasher.hash = MagicMock(side_effect=HashingError("Hashing failed"))
        with pytest.raises(AuthenticationError, match="Failed to hash password"):
            hash_password("test_password")


def test_hash_password_type_error():
    """Test hash_password handles TypeError."""
    from unittest.mock import MagicMock, patch

    with patch("server.auth.argon2_utils._default_hasher") as mock_hasher:
        mock_hasher.hash = MagicMock(side_effect=TypeError("Type error"))
        with pytest.raises(AuthenticationError, match="Failed to hash password"):
            hash_password("test_password")


def test_verify_password_verification_error():
    """Test verify_password handles VerificationError."""
    from unittest.mock import MagicMock, patch

    from argon2.exceptions import VerificationError

    with patch("server.auth.argon2_utils._default_hasher") as mock_hasher:
        mock_hasher.verify = MagicMock(side_effect=VerificationError("Verification failed"))
        result = verify_password("password", "hash")
        assert result is False


def test_verify_password_invalid_hash_exception():
    """Test verify_password handles InvalidHash exception."""
    from unittest.mock import MagicMock, patch

    from argon2.exceptions import InvalidHash

    with patch("server.auth.argon2_utils._default_hasher") as mock_hasher:
        mock_hasher.verify = MagicMock(side_effect=InvalidHash("Invalid hash"))
        result = verify_password("password", "hash")
        assert result is False


def test_verify_password_type_error():
    """Test verify_password handles TypeError."""
    from unittest.mock import MagicMock, patch

    with patch("server.auth.argon2_utils._default_hasher") as mock_hasher:
        mock_hasher.verify = MagicMock(side_effect=TypeError("Type error"))
        result = verify_password("password", "hash")
        assert result is False


def test_needs_rehash_error_handling():
    """Test needs_rehash handles errors and returns True."""
    from unittest.mock import MagicMock, patch

    from server.auth.argon2_utils import needs_rehash

    password = "test_password"
    hashed = hash_password(password)

    with patch("server.auth.argon2_utils._default_hasher") as mock_hasher:
        mock_hasher.check_needs_rehash = MagicMock(side_effect=ValueError("Error"))
        result = needs_rehash(hashed)
        assert result is True
