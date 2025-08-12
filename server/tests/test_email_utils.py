"""
Tests for email utilities.

This module tests the bogus email generation and validation utilities.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.auth.email_utils import (
    generate_unique_bogus_email,
    is_bogus_email,
    validate_bogus_email_format,
)


class TestEmailUtils:
    """Test email utility functions."""

    def test_is_bogus_email(self):
        """Test bogus email detection."""
        # Valid bogus emails
        assert is_bogus_email("testuser@wolfshade.org")
        assert is_bogus_email("user123@wolfshade.org")
        assert is_bogus_email("test.user@wolfshade.org")
        assert is_bogus_email("user_123@wolfshade.org")

        # Invalid emails
        assert not is_bogus_email("testuser@gmail.com")
        assert not is_bogus_email("testuser@example.com")
        assert not is_bogus_email("testuser@wolfshade.com")
        assert not is_bogus_email("testuser@wolfshade.org.uk")

    def test_validate_bogus_email_format(self):
        """Test bogus email format validation."""
        # Valid formats
        assert validate_bogus_email_format("testuser@wolfshade.org")
        assert validate_bogus_email_format("user123@wolfshade.org")
        assert validate_bogus_email_format("test.user@wolfshade.org")
        assert validate_bogus_email_format("user_123@wolfshade.org")
        assert validate_bogus_email_format("user-123@wolfshade.org")

        # Invalid formats
        assert not validate_bogus_email_format("testuser@gmail.com")  # Wrong domain
        assert not validate_bogus_email_format("test@user@wolfshade.org")  # Multiple @
        assert not validate_bogus_email_format("@wolfshade.org")  # Empty local part
        assert not validate_bogus_email_format("testuser@")  # Empty domain
        assert not validate_bogus_email_format("test user@wolfshade.org")  # Space in local part
        assert not validate_bogus_email_format("testuser@wolfshade.org ")  # Trailing space
        assert not validate_bogus_email_format(" testuser@wolfshade.org")  # Leading space

    @pytest.mark.asyncio
    async def test_generate_unique_bogus_email_new_user(self):
        """Test bogus email generation for new user."""
        # Mock session and query result
        mock_session = AsyncMock()
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None  # No existing user
        mock_session.execute.return_value = mock_result

        email = await generate_unique_bogus_email("testuser", mock_session)

        # Should generate base email format
        assert email == "testuser@wolfshade.org"
        assert validate_bogus_email_format(email)

    @pytest.mark.asyncio
    async def test_generate_unique_bogus_email_existing_user(self):
        """Test bogus email generation when base email exists."""
        # Mock session and query results
        mock_session = AsyncMock()
        mock_result1 = MagicMock()
        mock_result1.scalar_one_or_none.return_value = MagicMock()  # Base email exists
        mock_result2 = MagicMock()
        mock_result2.scalar_one_or_none.return_value = None  # Suffix email doesn't exist
        mock_session.execute.side_effect = [mock_result1, mock_result2]

        email = await generate_unique_bogus_email("testuser", mock_session)

        # Should generate email with suffix
        assert email.endswith("@wolfshade.org")
        assert "testuser." in email
        assert len(email.split(".")[1].split("@")[0]) == 8  # UUID suffix length
        assert validate_bogus_email_format(email)

    @pytest.mark.asyncio
    async def test_generate_unique_bogus_email_username_cleaning(self):
        """Test that usernames are properly cleaned for email generation."""
        mock_session = AsyncMock()
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute.return_value = mock_result

        # Test various username formats
        test_cases = [
            ("TestUser", "testuser@wolfshade.org"),
            ("user123", "user123@wolfshade.org"),
            ("test.user", "test.user@wolfshade.org"),
            ("user_123", "user_123@wolfshade.org"),
            ("user-123", "user-123@wolfshade.org"),
            ("Test User", "testuser@wolfshade.org"),  # Spaces removed
            ("test@user", "testuser@wolfshade.org"),  # @ removed
            ("test!user", "testuser@wolfshade.org"),  # Special chars removed
            ("a" * 25, "a" * 20 + "@wolfshade.org"),  # Length limited
        ]

        for username, expected_base in test_cases:
            email = await generate_unique_bogus_email(username, mock_session)
            assert email == expected_base
            assert validate_bogus_email_format(email)

    @pytest.mark.asyncio
    async def test_generate_unique_bogus_email_collision_handling(self):
        """Test handling of extremely unlikely email collisions."""
        # Mock session where both base and suffix emails exist
        mock_session = AsyncMock()
        mock_result1 = MagicMock()
        mock_result1.scalar_one_or_none.return_value = MagicMock()  # Base email exists
        mock_result2 = MagicMock()
        mock_result2.scalar_one_or_none.return_value = MagicMock()  # Suffix email also exists
        mock_result3 = MagicMock()
        mock_result3.scalar_one_or_none.return_value = None  # Full UUID email doesn't exist
        mock_session.execute.side_effect = [mock_result1, mock_result2, mock_result3]

        email = await generate_unique_bogus_email("testuser", mock_session)

        # Should generate email with full UUID
        assert email.endswith("@wolfshade.org")
        assert "testuser." in email
        assert len(email.split(".")[1].split("@")[0]) > 8  # Full UUID length
        assert validate_bogus_email_format(email)
