"""
Tests for utility commands and functions.

This module tests utility functions used by the command handler.
"""

from unittest.mock import Mock

import pytest

from server.command_handler_unified import get_username_from_user


class TestGetUsernameFromUser:
    """Test the get_username_from_user utility function."""

    def test_get_username_from_user_dict(self):
        """Test extracting username from dictionary."""
        user_dict = {"username": "testuser"}
        assert get_username_from_user(user_dict) == "testuser"

    def test_get_username_from_user_object(self):
        """Test extracting username from object."""
        user_obj = Mock()
        user_obj.username = "testuser"
        assert get_username_from_user(user_obj) == "testuser"

    def test_get_username_from_user_name_key(self):
        """Test extracting username using name key."""
        user_dict = {"name": "testuser"}
        assert get_username_from_user(user_dict) == "testuser"

    def test_get_username_from_user_name_attr(self):
        """Test extracting username using name attribute."""
        user_obj = Mock()
        # Set name attribute directly to ensure it's a string
        user_obj.name = "testuser"
        # Remove username attribute to ensure it uses name
        del user_obj.username
        assert get_username_from_user(user_obj) == "testuser"

    def test_get_username_from_user_invalid_dict(self):
        """Test extracting username from invalid dictionary."""
        user_dict = {"email": "test@example.com"}

        with pytest.raises(ValueError, match="User object must have username or name attribute or key"):
            get_username_from_user(user_dict)

    def test_get_username_from_user_invalid_object(self):
        """Test extracting username from invalid object."""
        user_obj = Mock()
        # Remove username and name attributes
        del user_obj.username
        del user_obj.name

        with pytest.raises(ValueError, match="User object must have username or name attribute or key"):
            get_username_from_user(user_obj)

    def test_get_username_from_user_none(self):
        """Test extracting username from None."""
        with pytest.raises(ValueError, match="User object must have username or name attribute or key"):
            get_username_from_user(None)
