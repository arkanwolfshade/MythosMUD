"""
Tests for security utilities.

This module tests the secure path validation, file operations,
and security checks in security_utils.py.
"""

import os
import tempfile
import unittest.mock as mock
from pathlib import Path

import pytest
from fastapi import HTTPException

from server.security_utils import (
    ensure_directory_exists,
    get_secure_file_path,
    is_safe_filename,
    validate_secure_path,
)


class TestValidateSecurePath:
    """Test secure path validation functionality."""

    def test_validate_secure_path_valid(self):
        """Test validation of a valid path."""
        base_path = "/tmp/test"
        user_path = "subdir/file.txt"

        result = validate_secure_path(base_path, user_path)

        expected = os.path.join(os.path.abspath(base_path), user_path)
        assert Path(result).as_posix() == Path(expected).as_posix()

    def test_validate_secure_path_with_leading_slash(self):
        """Test validation of path with leading slash."""
        base_path = "/tmp/test"
        user_path = "/subdir/file.txt"

        result = validate_secure_path(base_path, user_path)

        expected = os.path.join(os.path.abspath(base_path), "subdir/file.txt")
        assert Path(result).as_posix() == Path(expected).as_posix()

    def test_validate_secure_path_with_backslash(self):
        """Test validation of path with backslash."""
        base_path = "/tmp/test"
        user_path = "\\subdir\\file.txt"

        result = validate_secure_path(base_path, user_path)

        # The function should normalize backslashes to forward slashes
        # Use Path to handle cross-platform normalization
        expected = Path(os.path.join(os.path.abspath(base_path), "subdir/file.txt"))
        assert Path(result).as_posix() == expected.as_posix()

    def test_validate_secure_path_path_traversal_dotdot(self):
        """Test rejection of path traversal with .."""
        base_path = "/tmp/test"
        user_path = "../etc/passwd"

        with pytest.raises(HTTPException) as exc_info:
            validate_secure_path(base_path, user_path)

        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "Invalid path"

    def test_validate_secure_path_path_traversal_tilde(self):
        """Test rejection of path traversal with ~"""
        base_path = "/tmp/test"
        user_path = "~/secret/file.txt"

        with pytest.raises(HTTPException) as exc_info:
            validate_secure_path(base_path, user_path)

        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "Invalid path"

    def test_validate_secure_path_empty_user_path(self):
        """Test validation of empty user path."""
        base_path = "/tmp/test"
        user_path = ""

        result = validate_secure_path(base_path, user_path)

        expected = os.path.abspath(base_path)
        assert result == expected

    def test_validate_secure_path_nested_directories(self):
        """Test validation of nested directory paths."""
        base_path = "/tmp/test"
        user_path = "level1/level2/level3/file.txt"

        result = validate_secure_path(base_path, user_path)

        expected = os.path.join(os.path.abspath(base_path), user_path)
        assert Path(result).as_posix() == Path(expected).as_posix()

    def test_validate_secure_path_with_spaces(self):
        """Test validation of path with spaces."""
        base_path = "/tmp/test"
        user_path = "my file.txt"

        result = validate_secure_path(base_path, user_path)

        expected = os.path.join(os.path.abspath(base_path), user_path)
        assert result == expected


class TestGetSecureFilePath:
    """Test secure file path generation."""

    def test_get_secure_file_path_valid(self):
        """Test getting secure file path with valid filename."""
        filename = "test_file.txt"
        base_dir = "/tmp/test"

        result = get_secure_file_path(filename, base_dir)

        expected = os.path.join(os.path.abspath(base_dir), filename)
        assert result == expected

    def test_get_secure_file_path_with_underscores(self):
        """Test getting secure file path with underscores."""
        filename = "test_file_name.txt"
        base_dir = "/tmp/test"

        result = get_secure_file_path(filename, base_dir)

        expected = os.path.join(os.path.abspath(base_dir), filename)
        assert result == expected

    def test_get_secure_file_path_with_dots(self):
        """Test getting secure file path with dots."""
        filename = "test.file.txt"
        base_dir = "/tmp/test"

        result = get_secure_file_path(filename, base_dir)

        expected = os.path.join(os.path.abspath(base_dir), filename)
        assert result == expected

    def test_get_secure_file_path_with_hyphens(self):
        """Test getting secure file path with hyphens."""
        filename = "test-file.txt"
        base_dir = "/tmp/test"

        result = get_secure_file_path(filename, base_dir)

        expected = os.path.join(os.path.abspath(base_dir), filename)
        assert result == expected

    def test_get_secure_file_path_invalid_characters(self):
        """Test rejection of filename with invalid characters."""
        filename = "test@file.txt"
        base_dir = "/tmp/test"

        with pytest.raises(HTTPException) as exc_info:
            get_secure_file_path(filename, base_dir)

        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "Invalid filename"

    def test_get_secure_file_path_with_spaces(self):
        """Test rejection of filename with spaces."""
        filename = "test file.txt"
        base_dir = "/tmp/test"

        with pytest.raises(HTTPException) as exc_info:
            get_secure_file_path(filename, base_dir)

        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "Invalid filename"

    def test_get_secure_file_path_with_special_chars(self):
        """Test rejection of filename with special characters."""
        filename = "test!file.txt"
        base_dir = "/tmp/test"

        with pytest.raises(HTTPException) as exc_info:
            get_secure_file_path(filename, base_dir)

        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "Invalid filename"

    def test_get_secure_file_path_creates_base_dir(self):
        """Test that base directory is created if it doesn't exist."""
        filename = "test.txt"
        base_dir = "/tmp/nonexistent_dir"

        # Clean up if it exists
        if os.path.exists(base_dir):
            os.rmdir(base_dir)

        result = get_secure_file_path(filename, base_dir)

        assert os.path.exists(base_dir)
        expected = os.path.join(os.path.abspath(base_dir), filename)
        assert result == expected

        # Clean up
        os.rmdir(base_dir)


class TestEnsureDirectoryExists:
    """Test directory existence and creation functionality."""

    def test_ensure_directory_exists_existing(self):
        """Test ensuring directory exists when it already exists."""
        with tempfile.TemporaryDirectory() as temp_dir:
            result = ensure_directory_exists(temp_dir)

            assert result == os.path.abspath(temp_dir)
            assert os.path.exists(temp_dir)

    def test_ensure_directory_exists_nonexistent(self):
        """Test ensuring directory exists when it doesn't exist."""
        temp_dir = tempfile.mkdtemp()
        new_dir = os.path.join(temp_dir, "new_subdir")

        try:
            result = ensure_directory_exists(new_dir)

            assert result == os.path.abspath(new_dir)
            assert os.path.exists(new_dir)
        finally:
            # Clean up
            os.rmdir(new_dir)
            os.rmdir(temp_dir)

    def test_ensure_directory_exists_nested(self):
        """Test ensuring nested directory exists."""
        with tempfile.TemporaryDirectory() as temp_dir:
            nested_dir = os.path.join(temp_dir, "level1", "level2", "level3")

            result = ensure_directory_exists(nested_dir)

            assert result == os.path.abspath(nested_dir)
            assert os.path.exists(nested_dir)

    def test_ensure_directory_exists_relative_path(self):
        """Test ensuring directory exists with relative path."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a relative path within the temp directory
            relative_dir = os.path.join(temp_dir, "relative_dir")

            result = ensure_directory_exists(relative_dir)

            assert result == os.path.abspath(relative_dir)
            assert os.path.exists(relative_dir)


class TestIsSafeFilename:
    """Test filename safety checking."""

    def test_is_safe_filename_valid(self):
        """Test safe filename validation."""
        filename = "test_file.txt"

        assert is_safe_filename(filename) is True

    def test_is_safe_filename_with_underscores(self):
        """Test filename with underscores."""
        filename = "test_file_name.txt"

        assert is_safe_filename(filename) is True

    def test_is_safe_filename_with_dots(self):
        """Test filename with dots."""
        filename = "test.file.txt"

        assert is_safe_filename(filename) is True

    def test_is_safe_filename_with_hyphens(self):
        """Test filename with hyphens."""
        filename = "test-file.txt"

        assert is_safe_filename(filename) is True

    def test_is_safe_filename_with_numbers(self):
        """Test filename with numbers."""
        filename = "test123.txt"

        assert is_safe_filename(filename) is True

    def test_is_safe_filename_path_traversal_dotdot(self):
        """Test rejection of filename with path traversal."""
        filename = "../secret.txt"

        assert is_safe_filename(filename) is False

    def test_is_safe_filename_path_traversal_slash(self):
        """Test rejection of filename with forward slash."""
        filename = "dir/file.txt"

        assert is_safe_filename(filename) is False

    def test_is_safe_filename_path_traversal_backslash(self):
        """Test rejection of filename with backslash."""
        filename = "dir\\file.txt"

        assert is_safe_filename(filename) is False

    def test_is_safe_filename_special_characters(self):
        """Test rejection of filename with special characters."""
        filename = "test@file.txt"

        assert is_safe_filename(filename) is False

    def test_is_safe_filename_spaces(self):
        """Test rejection of filename with spaces."""
        filename = "test file.txt"

        assert is_safe_filename(filename) is False

    def test_is_safe_filename_empty(self):
        """Test empty filename."""
        filename = ""

        assert is_safe_filename(filename) is True

    def test_is_safe_filename_only_extension(self):
        """Test filename with only extension."""
        filename = ".txt"

        assert is_safe_filename(filename) is True

    def test_is_safe_filename_unicode(self):
        """Test filename with unicode characters."""
        filename = "testéfile.txt"

        assert is_safe_filename(filename) is False


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_validate_secure_path_different_drives_windows(self):
        """Test path validation with different drives (Windows scenario)."""
        base_path = "C:\\temp"
        user_path = "D:\\file.txt"

        # This should not raise an exception due to the try/except in the code
        result = validate_secure_path(base_path, user_path)

        # Should return the normalized path
        assert isinstance(result, str)

    def test_get_secure_file_path_very_long_filename(self):
        """Test secure file path with very long filename."""
        filename = "a" * 255 + ".txt"  # Maximum filename length
        base_dir = "/tmp/test"

        result = get_secure_file_path(filename, base_dir)

        expected = os.path.join(os.path.abspath(base_dir), filename)
        assert result == expected

    def test_is_safe_filename_very_long(self):
        """Test safe filename with very long name."""
        filename = "a" * 255 + ".txt"

        assert is_safe_filename(filename) is True

    def test_ensure_directory_exists_empty_string(self):
        """Test ensuring directory exists with empty string."""
        result = ensure_directory_exists("")

        # On Windows, empty string might not work as expected
        # Just check that it returns a string and doesn't raise an exception
        assert isinstance(result, str)
        assert len(result) > 0

    def test_validate_secure_path_path_traversal_commonpath_check(self):
        """Test path traversal detection using commonpath check."""
        # Create a scenario where path appears valid but escapes base directory
        base_path = "/tmp/test"
        # Use a path that normalizes outside the base directory
        # This tests the commonpath check at lines 57-69
        user_path = "../../etc/passwd"

        # First check should catch the ".." pattern
        with pytest.raises(HTTPException) as exc_info:
            validate_secure_path(base_path, user_path)

        assert exc_info.value.status_code == 400

    def test_validate_secure_path_cross_drive_windows(self):
        """Test path validation handles ValueError for cross-drive paths (Windows)."""
        # Simulate Windows cross-drive scenario
        # This tests the ValueError exception handling at lines 70-74
        base_path = "C:\\temp"
        user_path = "file.txt"

        # Should not raise ValueError, should handle gracefully
        result = validate_secure_path(base_path, user_path)
        assert isinstance(result, str)

    def test_validate_secure_path_escapes_base_after_normalization(self):
        """Test path that escapes base directory after normalization."""
        with tempfile.TemporaryDirectory() as temp_dir:
            base_path = temp_dir
            # Create a path that, after normalization, escapes the base
            # This is tricky - we need a path that passes the ".." check
            # but fails the commonpath check
            user_path = "subdir/../../.." + temp_dir.replace(os.sep, "/") + "/escape"

            # The path should be caught by the commonpath check
            # But first it will be caught by the ".." check
            with pytest.raises(HTTPException):
                validate_secure_path(base_path, user_path)

    def test_validate_secure_path_commonpath_failure(self):
        """Test path traversal detection via commonpath check (lines 59-66)."""
        # Test the case where commonpath != base_path
        # This tests the logger.warning and HTTPException at lines 59-66
        base_path = "/tmp/test"
        user_path = "file.txt"

        # Mock os.path.commonpath to return a different path than base_path
        # This simulates a path that escapes the base directory
        with mock.patch("server.security_utils.os.path.commonpath") as mock_commonpath:
            mock_commonpath.return_value = "/tmp"  # Different from base_path

            with pytest.raises(HTTPException) as exc_info:
                validate_secure_path(base_path, user_path)

            assert exc_info.value.status_code == 400
            assert exc_info.value.detail == "Path traversal attempt detected"

    def test_validate_secure_path_valueerror_exception(self):
        """Test ValueError exception handling for cross-drive paths (lines 70-74)."""
        # Test the ValueError exception path which occurs on Windows
        # when paths are on different drives
        base_path = "/tmp/test"
        user_path = "file.txt"

        # Mock os.path.commonpath to raise ValueError (simulating cross-drive scenario)
        with mock.patch("server.security_utils.os.path.commonpath") as mock_commonpath:
            mock_commonpath.side_effect = ValueError("Paths don't have a common prefix")

            # Should not raise an exception, should handle gracefully
            result = validate_secure_path(base_path, user_path)
            assert isinstance(result, str)
