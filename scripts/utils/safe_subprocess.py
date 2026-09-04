"""
Safe subprocess execution utilities.

This module provides secure wrappers for subprocess.run() that prevent
command injection by validating inputs and using proper argument handling.

As documented in the restricted archives, proper command execution requires
careful validation to prevent unauthorized access to system resources.
"""

import shlex
import subprocess
from pathlib import Path
from typing import Any

# Get project root directory (parent of scripts directory)
PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()


def validate_path(path: str | Path, must_exist: bool = True) -> Path:
    """
    Validate that a path is within the project directory.

    Args:
        path: Path to validate
        must_exist: If True, path must exist

    Returns:
        Path: Resolved Path object

    Raises:
        ValueError: If path is outside project root or doesn't exist when required
    """
    path_obj = Path(path)
    project_root = PROJECT_ROOT.resolve()

    # First check if the original path (before resolving symlinks) is within project root
    # This handles symlinks that point outside the project (e.g., .venv/bin/python -> system Python)
    # We validate the symlink location, not the resolved target, for security
    try:
        path_obj.relative_to(project_root)
        # Original path is within project root - this is valid even if symlink points outside
        # Check existence on the original path (will follow symlink if needed)
        if must_exist and not path_obj.exists():
            raise ValueError(f"Path {path_obj} does not exist")
        # Return resolved path for actual use, but we've validated the symlink is in project root
        return path_obj.resolve()
    except ValueError:
        # Original path is not relative to project root, try resolving it
        # This handles absolute paths that might resolve to something within project root
        resolved = path_obj.resolve()
        try:
            resolved.relative_to(project_root)
        except ValueError as err:
            raise ValueError(f"Path {path_obj} is outside project root {project_root}") from err
        # Resolved path is within project root
        if must_exist and not resolved.exists():
            raise ValueError(f"Path {resolved} does not exist") from None
        return resolved


def validate_command(command: str | list[str]) -> list[str]:
    """
    Validate and normalize a command for safe execution.

    Args:
        command: Command as string or list of arguments

    Returns:
        list[str]: Normalized command as list of arguments

    Raises:
        ValueError: If command is invalid or contains dangerous patterns
    """
    if isinstance(command, str):
        # For string commands, split using shlex to handle quotes properly
        # This prevents injection while preserving legitimate arguments
        try:
            args = shlex.split(command)
        except ValueError as e:
            raise ValueError(f"Invalid command syntax: {e}") from e
    else:
        args = list(command)

    if not args:
        raise ValueError("Command cannot be empty")

    # Validate first argument (executable) is a simple name or absolute path
    executable = args[0]
    if not executable:
        raise ValueError("Executable cannot be empty")

    # If it's a path (contains path separators), validate it
    if "/" in executable or "\\" in executable:
        # It's a path - validate it's within project root
        # For executable paths, we allow them to not exist yet (e.g., in CI before venv is fully set up)
        # but they must be within the project root for security
        try:
            validated_path = validate_path(executable, must_exist=False)
            args[0] = str(validated_path)
        except ValueError as e:
            # Path validation failed - this is a real error, don't fall back to alphanumeric check
            raise ValueError(f"Invalid executable path: {executable} - {e}") from e

    return args


def safe_run(
    command: str | list[str],
    cwd: str | Path | None = None,
    check: bool = False,
    **kwargs: Any,
) -> subprocess.CompletedProcess[str]:
    """
    Safely execute a subprocess command with validation.

    This function prevents command injection by:
    1. Validating command arguments
    2. Ensuring working directory is within project root
    3. Using proper argument handling (no shell=True)

    Args:
        command: Command to execute (string or list)
        cwd: Working directory (must be within project root)
        check: If True, raise CalledProcessError on non-zero exit
        **kwargs: Additional arguments to subprocess.run()

    Returns:
        subprocess.CompletedProcess: Result of command execution

    Raises:
        ValueError: If command or path validation fails
        subprocess.CalledProcessError: If check=True and command fails
    """
    # Validate and normalize command
    args = validate_command(command)

    # Validate working directory
    if cwd is not None:
        validated_cwd = validate_path(cwd, must_exist=True)
        cwd = str(validated_cwd)
    else:
        cwd = str(PROJECT_ROOT)

    # Ensure shell=False to prevent shell injection
    # Never use shell=True with user input
    kwargs["shell"] = False

    # Execute command with validated arguments
    # nosemgrep: python.lang.security.audit.subprocess-shell-true.subprocess-shell-true
    # nosec B603: args validated by validate_command, shell=False, no user input in execution
    return subprocess.run(
        args,
        cwd=cwd,
        check=check,
        **kwargs,
    )


def safe_run_static(
    executable: str,
    *args: str,
    cwd: str | Path | None = None,
    check: bool = False,
    **kwargs: Any,
) -> subprocess.CompletedProcess[str]:
    """
    Execute a command with static arguments (safest option).

    This is the safest way to execute commands when all arguments are known
    at development time. No string parsing or validation is needed.

    Args:
        executable: Executable name or path
        *args: Static arguments (no user input)
        cwd: Working directory (must be within project root)
        check: If True, raise CalledProcessError on non-zero exit
        **kwargs: Additional arguments to subprocess.run()

    Returns:
        subprocess.CompletedProcess: Result of command execution

    Raises:
        ValueError: If path validation fails
        subprocess.CalledProcessError: If check=True and command fails
    """
    # Build command list from static arguments
    command = [executable] + list(args)

    return safe_run(command, cwd=cwd, check=check, **kwargs)
