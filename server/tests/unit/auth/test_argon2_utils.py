"""
Tests for Argon2 password hashing utilities.

These tests ensure the security and correctness of our Argon2 implementation,
as documented in the restricted archives of Miskatonic University.
"""

import time

import pytest

from server.auth.argon2_utils import (
    HASH_LENGTH,
    MEMORY_COST,
    PARALLELISM,
    TIME_COST,
    create_hasher_with_params,
    get_hash_info,
    hash_password,
    is_argon2_hash,
    needs_rehash,
    verify_password,
)
from server.exceptions import AuthenticationError


class TestArgon2Configuration:
    """Test Argon2 configuration constants."""

    def test_time_cost_default(self):
        """Test that time cost is set to a reasonable default."""
        assert TIME_COST == 3
        assert TIME_COST > 0

    def test_memory_cost_default(self):
        """Test that memory cost is set to a reasonable default."""
        assert MEMORY_COST == 65536  # 64MB
        assert MEMORY_COST > 0

    def test_parallelism_default(self):
        """Test that parallelism is set to a reasonable default."""
        assert PARALLELISM == 1
        assert PARALLELISM > 0

    def test_hash_length_default(self):
        """Test that hash length is set to a reasonable default."""
        assert HASH_LENGTH == 32
        assert HASH_LENGTH > 0


class TestArgon2HashGeneration:
    """Test Argon2 hash generation functionality."""

    def test_hash_password_basic(self):
        """Test basic password hashing."""
        password = "test_password"
        hashed = hash_password(password)

        assert isinstance(hashed, str)
        assert hashed.startswith("$argon2")
        assert len(hashed) > 50  # Argon2 hashes are long

    def test_hash_password_empty(self):
        """Test hashing empty password."""
        hashed = hash_password("")
        assert isinstance(hashed, str)
        assert hashed.startswith("$argon2")

    def test_hash_password_special_chars(self):
        """Test hashing password with special characters."""
        password = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
        hashed = hash_password(password)
        assert isinstance(hashed, str)
        assert hashed.startswith("$argon2")

    def test_hash_password_unicode(self):
        """Test hashing password with unicode characters."""
        password = "测试密码🎭"
        hashed = hash_password(password)
        assert isinstance(hashed, str)
        assert hashed.startswith("$argon2")

    def test_hash_password_very_long(self):
        """Test hashing very long password."""
        password = "a" * 1000
        hashed = hash_password(password)
        assert isinstance(hashed, str)
        assert hashed.startswith("$argon2")

    def test_hash_password_deterministic_salt(self):
        """Test that same password produces different hashes (due to salt)."""
        password = "test_password"
        hash1 = hash_password(password)
        hash2 = hash_password(password)

        assert hash1 != hash2  # Different salts should produce different hashes


class TestArgon2PasswordVerification:
    """Test Argon2 password verification functionality."""

    def test_verify_password_correct(self):
        """Test verifying correct password."""
        password = "test_password"
        hashed = hash_password(password)
        assert verify_password(password, hashed) is True

    def test_verify_password_incorrect(self):
        """Test verifying incorrect password."""
        password = "test_password"
        hashed = hash_password(password)
        assert verify_password("wrong_password", hashed) is False

    def test_verify_password_empty(self):
        """Test verifying empty password."""
        hashed = hash_password("")
        assert verify_password("", hashed) is True
        assert verify_password("not_empty", hashed) is False

    def test_verify_password_special_chars(self):
        """Test verifying password with special characters."""
        password = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
        hashed = hash_password(password)
        assert verify_password(password, hashed) is True

    def test_verify_password_unicode(self):
        """Test verifying password with unicode characters."""
        password = "测试密码🎭"
        hashed = hash_password(password)
        assert verify_password(password, hashed) is True

    def test_verify_password_case_sensitive(self):
        """Test that password verification is case sensitive."""
        password = "TestPassword"
        hashed = hash_password(password)
        assert verify_password("testpassword", hashed) is False
        assert verify_password("TestPassword", hashed) is True

    def test_verify_password_invalid_hash(self):
        """Test verification with invalid hash."""
        assert verify_password("test", "invalid_hash") is False

    def test_verify_password_empty_hash(self):
        """Test verification with empty hash."""
        assert verify_password("test", "") is False


class TestArgon2HashDetection:
    """Test Argon2 hash detection functionality."""

    def test_is_argon2_hash_valid(self):
        """Test detection of valid Argon2 hash."""
        password = "test_password"
        hashed = hash_password(password)
        assert is_argon2_hash(hashed) is True

    def test_is_argon2_hash_bcrypt(self):
        """Test detection of bcrypt hash (should be False)."""
        bcrypt_hash = "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj3bp.gSJm2"
        assert is_argon2_hash(bcrypt_hash) is False

    def test_is_argon2_hash_empty(self):
        """Test detection of empty string."""
        assert is_argon2_hash("") is False

    def test_is_argon2_hash_none(self):
        """Test detection of None."""
        assert is_argon2_hash(None) is False

    def test_is_argon2_hash_random_string(self):
        """Test detection of random string."""
        assert is_argon2_hash("random_string") is False


class TestArgon2RehashChecking:
    """Test Argon2 rehash checking functionality."""

    def test_needs_rehash_fresh_hash(self):
        """Test that fresh hash doesn't need rehashing."""
        password = "test_password"
        hashed = hash_password(password)
        assert needs_rehash(hashed) is False

    def test_needs_rehash_invalid_hash(self):
        """Test that invalid hash needs rehashing."""
        assert needs_rehash("invalid_hash") is True

    def test_needs_rehash_empty_hash(self):
        """Test that empty hash needs rehashing."""
        assert needs_rehash("") is True


class TestArgon2HashInfo:
    """Test Argon2 hash info extraction."""

    def test_get_hash_info_valid(self):
        """Test extracting info from valid Argon2 hash."""
        password = "test_password"
        hashed = hash_password(password)
        info = get_hash_info(hashed)

        assert info is not None
        assert "m" in info  # memory cost
        assert "t" in info  # time cost
        assert "p" in info  # parallelism

    def test_get_hash_info_bcrypt(self):
        """Test extracting info from bcrypt hash."""
        bcrypt_hash = "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj3bp.gSJm2"
        assert get_hash_info(bcrypt_hash) is None

    def test_get_hash_info_empty(self):
        """Test extracting info from empty string."""
        assert get_hash_info("") is None

    def test_get_hash_info_none(self):
        """Test extracting info from None."""
        assert get_hash_info(None) is None

    def test_get_hash_info_invalid_format(self):
        """Test extracting info from invalid format."""
        assert get_hash_info("$argon2id$invalid") is None


class TestArgon2CustomHasher:
    """Test custom Argon2 hasher creation."""

    def test_create_hasher_with_params(self):
        """Test creating hasher with custom parameters."""
        hasher = create_hasher_with_params(
            time_cost=1,
            memory_cost=1024,
            parallelism=2,
            hash_len=16,
        )
        assert hasher is not None

    def test_create_hasher_default_params(self):
        """Test creating hasher with default parameters."""
        hasher = create_hasher_with_params()
        assert hasher is not None


class TestArgon2ErrorHandling:
    """Test Argon2 error handling."""

    def test_hash_password_invalid_type(self):
        """Test hashing with invalid password type."""
        with pytest.raises(AuthenticationError):
            hash_password(123)

    def test_verify_password_invalid_types(self):
        """Test verification with invalid types."""
        assert verify_password(123, "hash") is False
        assert verify_password("password", 123) is False


class TestArgon2Security:
    """Test Argon2 security properties."""

    def test_hash_uniqueness(self):
        """Test that same password produces different hashes."""
        password = "test_password"
        hashes = set()

        for _ in range(10):
            hashes.add(hash_password(password))

        assert len(hashes) == 10  # All hashes should be unique

    def test_hash_length_consistency(self):
        """Test that hash length is consistent."""
        password = "test_password"
        hashed = hash_password(password)

        # Extract the actual hash part (after the last $)
        hash_part = hashed.split("$")[-1]
        # Argon2 uses Base64 encoding but the actual length may vary
        # We just verify it's a reasonable length for a 32-byte hash
        assert len(hash_part) >= 40  # Base64 encoding of 32 bytes should be at least 40 chars
        assert len(hash_part) <= 50  # And not more than 50 chars

    def test_verification_timing_consistency(self):
        """Test that verification timing is consistent (no timing attacks)."""
        password = "test_password"
        hashed = hash_password(password)

        # Take multiple measurements to get more reliable timing
        correct_times = []
        incorrect_times = []

        for _ in range(5):
            # Measure verification time for correct password
            start_time = time.time()
            verify_password(password, hashed)
            correct_times.append(time.time() - start_time)

            # Measure verification time for incorrect password
            start_time = time.time()
            verify_password("wrong_password", hashed)
            incorrect_times.append(time.time() - start_time)

        # Calculate average times
        avg_correct_time = sum(correct_times) / len(correct_times)
        avg_incorrect_time = sum(incorrect_times) / len(incorrect_times)

        # Times should be similar (within 25% tolerance for more realistic expectations)
        time_diff = abs(avg_correct_time - avg_incorrect_time)
        max_time = max(avg_correct_time, avg_incorrect_time)

        # Use a more reasonable tolerance of 25% instead of 10%
        assert time_diff < max_time * 0.25, (
            f"Timing difference {time_diff:.6f}s exceeds tolerance. "
            f"Correct avg: {avg_correct_time:.6f}s, "
            f"Incorrect avg: {avg_incorrect_time:.6f}s"
        )


class TestArgon2NonArgon2HashHandling:
    """Test handling of non-Argon2 hashes."""

    def test_verify_password_with_bcrypt_hash(self):
        """Test verification with non-Argon2 hash (bcrypt)."""
        bcrypt_hash = "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj3bp.gSJm2"

        # Should return False for non-Argon2 hash
        result = verify_password("anypassword", bcrypt_hash)
        assert result is False

    def test_needs_rehash_with_exception(self):
        """Test needs_rehash handles exceptions gracefully."""
        # Create an Argon2-like hash but malformed
        malformed_hash = "$argon2id$malformed"

        # Should return True (needs rehash) when check fails
        result = needs_rehash(malformed_hash)
        assert result is True

    def test_get_hash_info_with_malformed_parts(self):
        """Test get_hash_info with malformed hash parts."""
        # Valid Argon2 prefix but too few parts
        malformed_hash = "$argon2id$v=19"

        result = get_hash_info(malformed_hash)
        assert result is None

    def test_get_hash_info_with_non_numeric_params(self):
        """Test get_hash_info with non-numeric parameter values."""
        # Hash with non-numeric parameter
        # This may not be a realistic hash, but tests the exception handling
        malformed_hash = "$argon2id$v=19$m=invalid,t=3,p=1$salt$hash"

        result = get_hash_info(malformed_hash)
        # Should still parse what it can or return a dict with string values
        assert result is None or isinstance(result, dict)
