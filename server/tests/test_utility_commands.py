"""
Tests for utility commands and functions.

This module tests utility functions used by the command handler.
"""

import pytest

from server.command_handler_unified import get_username_from_user


class TestGetUsernameFromUser:
    """Test the get_username_from_user utility function."""

    def test_get_username_from_user_dict(self):
        """Test extracting username from dictionary."""
        user_dict = {"username": "testuser"}
        assert get_username_from_user(user_dict) == "testuser"

    def test_get_username_from_user_object(self):
        """Test extracting username from object with username attribute."""

        # Create a simple object with username attribute
        class UserObject:
            def __init__(self, username):
                self.username = username

        user_obj = UserObject("testuser")
        result = get_username_from_user(user_obj)
        assert result == "testuser"

    def test_get_username_from_user_name_key(self):
        """Test extracting username using name key."""
        user_dict = {"name": "testuser"}
        assert get_username_from_user(user_dict) == "testuser"

    def test_get_username_from_user_name_attr(self):
        """Test extracting username from object with name attribute."""

        # Create a simple object with name attribute
        class UserObject:
            def __init__(self, name):
                self.name = name

        user_obj = UserObject("testuser")
        result = get_username_from_user(user_obj)
        assert result == "testuser"

    def test_get_username_from_user_invalid_dict(self):
        """Test extracting username from invalid dictionary."""
        user_dict = {"email": "test@example.com"}

        with pytest.raises(ValueError, match="User object must have username or name attribute or key"):
            get_username_from_user(user_dict)

    def test_get_username_from_user_invalid_object(self):
        """Test extracting username from invalid object."""

        # Create a simple object without username or name attributes
        class InvalidUserObject:
            def __init__(self):
                self.email = "test@example.com"  # Different attribute

        user_obj = InvalidUserObject()
        with pytest.raises(ValueError, match="User object must have username or name attribute or key"):
            get_username_from_user(user_obj)

    def test_get_username_from_user_none(self):
        """Test extracting username from None."""
        with pytest.raises(ValueError, match="User object must have username or name attribute or key"):
            get_username_from_user(None)
