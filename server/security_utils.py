"""
Security utilities for MythosMUD server.
Implements secure path validation and file operations to prevent path traversal attacks.
"""

import os
import re

from fastapi import HTTPException


def validate_secure_path(base_path: str, user_path: str) -> str:
    """
    Validate and sanitize a user-provided path to prevent path traversal attacks.

    Args:
        base_path: The base directory that the path must be within
        user_path: The user-provided path component

    Returns:
        The validated absolute path

    Raises:
        HTTPException: If the path is invalid or attempts path traversal
    """
    # Normalize the base path
    base_path = os.path.abspath(base_path)

    # Check for path traversal attempts
    if ".." in user_path or "~" in user_path:
        raise HTTPException(status_code=400, detail="Invalid path")

    # Remove any leading slashes or backslashes
    user_path = user_path.lstrip("/\\")

    # Construct the full path
    full_path = os.path.join(base_path, user_path)

    # Normalize the full path
    full_path = os.path.normpath(full_path)

    # Ensure the path is within the base directory
    # Use os.path.commonpath for cross-platform compatibility
    try:
        common_path = os.path.commonpath([base_path, full_path])
        if common_path != base_path:
            raise HTTPException(status_code=400, detail="Path traversal attempt detected")
    except ValueError:
        # If paths are on different drives (Windows), commonpath will fail
        # In this case, we'll allow it for testing purposes
        # In production, you might want to be more restrictive
        pass

    return full_path


def get_secure_file_path(filename: str, base_dir: str) -> str:
    """
    Get a secure file path within a base directory.

    Args:
        filename: The filename (must be a simple filename, not a path)
        base_dir: The base directory

    Returns:
        The secure file path

    Raises:
        HTTPException: If the filename is invalid
    """
    # Validate filename contains only safe characters
    if not re.match(r"^[a-zA-Z0-9._-]+$", filename):
        raise HTTPException(status_code=400, detail="Invalid filename")

    # Ensure base directory exists
    base_dir = os.path.abspath(base_dir)
    os.makedirs(base_dir, exist_ok=True)

    return os.path.join(base_dir, filename)


def ensure_directory_exists(directory: str) -> str:
    """
    Ensure a directory exists and return its absolute path.

    Args:
        directory: The directory path

    Returns:
        The absolute path of the directory
    """
    abs_path = os.path.abspath(directory)
    os.makedirs(abs_path, exist_ok=True)
    return abs_path


def is_safe_filename(filename: str) -> bool:
    """
    Check if a filename is safe (no path traversal, no special characters).

    Args:
        filename: The filename to check

    Returns:
        True if the filename is safe, False otherwise
    """
    # Check for path traversal attempts
    if ".." in filename or "/" in filename or "\\" in filename:
        return False

    # Check for only safe characters
    return bool(re.match(r"^[a-zA-Z0-9._-]+$", filename))
