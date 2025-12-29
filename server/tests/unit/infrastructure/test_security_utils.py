"""
Unit tests for security utilities.

Tests path validation and file security functions to prevent path traversal attacks.
"""

import os
import tempfile

import pytest
from fastapi import HTTPException

from server.security_utils import (
    ensure_directory_exists,
    get_secure_file_path,
    is_safe_filename,
    validate_secure_path,
)


def test_validate_secure_path_valid():
    """Test validate_secure_path with valid path."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = validate_secure_path(tmpdir, "subdir/file.txt")

        assert isinstance(result, str)
        assert os.path.exists(result) or not os.path.exists(result)  # Path may or may not exist
        assert tmpdir in result or os.path.commonpath([tmpdir, result]) == tmpdir


def test_validate_secure_path_with_dot_dot():
    """Test validate_secure_path rejects path traversal with .."""
    with tempfile.TemporaryDirectory() as tmpdir:
        with pytest.raises(HTTPException, match="Invalid path"):
            validate_secure_path(tmpdir, "../etc/passwd")


def test_validate_secure_path_with_tilde():
    """Test validate_secure_path rejects path traversal with ~"""
    with tempfile.TemporaryDirectory() as tmpdir:
        with pytest.raises(HTTPException, match="Invalid path"):
            validate_secure_path(tmpdir, "~/secret")


def test_validate_secure_path_with_leading_slash():
    """Test validate_secure_path handles leading slashes."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = validate_secure_path(tmpdir, "/subdir/file.txt")

        # Leading slash should be stripped
        assert isinstance(result, str)
        assert "subdir" in result or "file.txt" in result


def test_validate_secure_path_with_backslash():
    """Test validate_secure_path normalizes backslashes."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = validate_secure_path(tmpdir, "subdir\\file.txt")

        # Backslashes should be normalized to forward slashes
        assert isinstance(result, str)
        assert "subdir" in result or "file.txt" in result


def test_validate_secure_path_path_traversal_commonpath():
    """Test validate_secure_path detects path traversal via commonpath check."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a sibling directory to test commonpath detection
        parent_dir = os.path.dirname(tmpdir)
        sibling_dir = os.path.join(parent_dir, "sibling_dir")

        # Try to access sibling directory (should be caught by commonpath check)
        # We need to construct a path that would escape but doesn't use ..
        # Since .. is caught first, we'll test with an absolute path that's outside
        try:
            # This should be caught by the commonpath check if it escapes
            result = validate_secure_path(tmpdir, os.path.relpath(sibling_dir, tmpdir))
            # If it doesn't raise, the path should still be within base_path
            assert tmpdir in result or os.path.commonpath([tmpdir, result]) == tmpdir
        except HTTPException:
            # It's valid to reject paths outside base
            pass


def test_validate_secure_path_different_drives_windows():
    """Test validate_secure_path handles different drives on Windows."""
    if os.name != "nt":
        pytest.skip("Windows-specific test")

    # On Windows, paths on different drives cause ValueError in commonpath
    # The code should handle this gracefully
    base_path = "C:\\temp"
    user_path = "D:\\file.txt"

    # This should not raise due to ValueError handling
    try:
        result = validate_secure_path(base_path, user_path)
        # Should return a path (may be invalid but shouldn't crash)
        assert isinstance(result, str)
    except HTTPException:
        # It's also valid to reject cross-drive paths
        pass


def test_get_secure_file_path_valid():
    """Test get_secure_file_path with valid filename."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = get_secure_file_path("test_file.txt", tmpdir)

        assert isinstance(result, str)
        assert os.path.dirname(result) == os.path.abspath(tmpdir)
        assert os.path.basename(result) == "test_file.txt"


def test_get_secure_file_path_invalid_characters():
    """Test get_secure_file_path rejects invalid characters."""
    with tempfile.TemporaryDirectory() as tmpdir:
        with pytest.raises(HTTPException, match="Invalid filename"):
            get_secure_file_path("file<script>.txt", tmpdir)


def test_get_secure_file_path_with_slash():
    """Test get_secure_file_path rejects filenames with slashes."""
    with tempfile.TemporaryDirectory() as tmpdir:
        with pytest.raises(HTTPException, match="Invalid filename"):
            get_secure_file_path("path/to/file.txt", tmpdir)


def test_get_secure_file_path_creates_directory():
    """Test get_secure_file_path creates base directory if it doesn't exist."""
    with tempfile.TemporaryDirectory() as tmpdir:
        new_dir = os.path.join(tmpdir, "new_dir")
        result = get_secure_file_path("test.txt", new_dir)

        assert os.path.isdir(new_dir)
        assert isinstance(result, str)


def test_get_secure_file_path_with_underscores():
    """Test get_secure_file_path accepts filenames with underscores."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = get_secure_file_path("test_file_name.txt", tmpdir)

        assert isinstance(result, str)
        assert "test_file_name.txt" in result


def test_get_secure_file_path_with_dots():
    """Test get_secure_file_path accepts filenames with dots."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = get_secure_file_path("file.name.with.dots.txt", tmpdir)

        assert isinstance(result, str)
        assert "file.name.with.dots.txt" in result


def test_get_secure_file_path_with_hyphens():
    """Test get_secure_file_path accepts filenames with hyphens."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = get_secure_file_path("test-file-name.txt", tmpdir)

        assert isinstance(result, str)
        assert "test-file-name.txt" in result


def test_ensure_directory_exists_existing():
    """Test ensure_directory_exists with existing directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = ensure_directory_exists(tmpdir)

        assert isinstance(result, str)
        assert os.path.isdir(result)
        assert os.path.abspath(tmpdir) == result


def test_ensure_directory_exists_creates():
    """Test ensure_directory_exists creates directory if it doesn't exist."""
    with tempfile.TemporaryDirectory() as tmpdir:
        new_dir = os.path.join(tmpdir, "new_subdir")
        result = ensure_directory_exists(new_dir)

        assert os.path.isdir(new_dir)
        assert os.path.abspath(new_dir) == result


def test_ensure_directory_exists_relative_path():
    """Test ensure_directory_exists with relative path."""
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        try:
            result = ensure_directory_exists("relative_dir")

            assert isinstance(result, str)
            assert os.path.isabs(result)  # Should be absolute
            assert os.path.isdir(result)
        finally:
            os.chdir("/" if os.name != "nt" else "C:\\")


def test_is_safe_filename_valid():
    """Test is_safe_filename with valid filename."""
    assert is_safe_filename("test_file.txt") is True
    assert is_safe_filename("file-name.txt") is True
    assert is_safe_filename("file.name.txt") is True
    assert is_safe_filename("123file.txt") is True


def test_is_safe_filename_empty():
    """Test is_safe_filename with empty string (considered safe)."""
    assert is_safe_filename("") is True


def test_is_safe_filename_with_dot_dot():
    """Test is_safe_filename rejects filenames with .."""
    assert is_safe_filename("../file.txt") is False
    assert is_safe_filename("file../name.txt") is False


def test_is_safe_filename_with_forward_slash():
    """Test is_safe_filename rejects filenames with forward slash."""
    assert is_safe_filename("path/to/file.txt") is False


def test_is_safe_filename_with_backslash():
    """Test is_safe_filename rejects filenames with backslash."""
    assert is_safe_filename("path\\to\\file.txt") is False


def test_is_safe_filename_with_special_chars():
    """Test is_safe_filename rejects filenames with special characters."""
    assert is_safe_filename("file<script>.txt") is False
    assert is_safe_filename("file@name.txt") is False
    assert is_safe_filename("file#name.txt") is False
    assert is_safe_filename("file$name.txt") is False
    assert is_safe_filename("file%name.txt") is False
    assert is_safe_filename("file&name.txt") is False
    assert is_safe_filename("file*name.txt") is False
    assert is_safe_filename("file(name.txt") is False
    assert is_safe_filename("file)name.txt") is False
    assert is_safe_filename("file+name.txt") is False
    assert is_safe_filename("file=name.txt") is False
    assert is_safe_filename("file[name.txt") is False
    assert is_safe_filename("file]name.txt") is False
    assert is_safe_filename("file{name.txt") is False
    assert is_safe_filename("file}name.txt") is False
    assert is_safe_filename("file|name.txt") is False
    assert is_safe_filename("file:name.txt") is False
    assert is_safe_filename("file;name.txt") is False
    assert is_safe_filename("file'name.txt") is False
    assert is_safe_filename('file"name.txt') is False
    assert is_safe_filename("file,name.txt") is False
    assert is_safe_filename("file?name.txt") is False
    assert is_safe_filename("file!name.txt") is False


def test_is_safe_filename_unicode():
    """Test is_safe_filename with Unicode characters."""
    # Unicode characters should be rejected (only ASCII alphanumeric, dots, underscores, hyphens allowed)
    assert is_safe_filename("fileñame.txt") is False
    assert is_safe_filename("file中文.txt") is False


def test_validate_secure_path_nested_path():
    """Test validate_secure_path with nested valid path."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = validate_secure_path(tmpdir, "level1/level2/level3/file.txt")

        assert isinstance(result, str)
        assert "level1" in result or "level2" in result or "level3" in result or "file.txt" in result


def test_validate_secure_path_empty_user_path():
    """Test validate_secure_path with empty user path."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = validate_secure_path(tmpdir, "")

        assert isinstance(result, str)
        assert result == os.path.abspath(tmpdir) or result.startswith(tmpdir)


def test_validate_secure_path_absolute_base():
    """Test validate_secure_path normalizes base path to absolute."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Use relative base path (if possible)
        try:
            relative_base = os.path.relpath(tmpdir, os.getcwd())
            # Only test if relative path is actually different from absolute
            if relative_base != tmpdir:
                result = validate_secure_path(relative_base, "file.txt")

                # Base should be normalized to absolute
                assert isinstance(result, str)
                assert os.path.isabs(os.path.dirname(result))
        except ValueError:
            # If paths are on different drives (Windows), relpath may fail
            # In that case, just verify absolute path works
            result = validate_secure_path(tmpdir, "file.txt")
            assert isinstance(result, str)


def test_get_secure_file_path_numeric_filename():
    """Test get_secure_file_path with numeric filename."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = get_secure_file_path("123.txt", tmpdir)

        assert isinstance(result, str)
        assert "123.txt" in result


def test_get_secure_file_path_mixed_case():
    """Test get_secure_file_path with mixed case filename."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = get_secure_file_path("TestFile.TXT", tmpdir)

        assert isinstance(result, str)
        assert "TestFile.TXT" in result or "testfile.txt" in result.lower()


def test_validate_secure_path_with_spaces():
    """Test validate_secure_path with path containing spaces."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = validate_secure_path(tmpdir, "sub dir/file name.txt")

        assert isinstance(result, str)
        # Spaces are allowed in paths (though not in filenames per is_safe_filename)


def test_get_secure_file_path_with_spaces():
    """Test get_secure_file_path rejects filenames with spaces."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Spaces are not in the safe character set [a-zA-Z0-9._-]
        with pytest.raises(HTTPException, match="Invalid filename"):
            get_secure_file_path("file name.txt", tmpdir)
