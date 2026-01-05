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
    resolved = Path(path).resolve()
    project_root = PROJECT_ROOT.resolve()

    # Check if path is within project root
    try:
        resolved.relative_to(project_root)
    except ValueError as err:
        raise ValueError(f"Path {resolved} is outside project root {project_root}") from err

    if must_exist and not resolved.exists():
        raise ValueError(f"Path {resolved} does not exist")

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

    # If it's a relative path, resolve it relative to project root
    if "/" in executable or "\\" in executable:
        # It's a path - validate it
        try:
            validated_path = validate_path(executable, must_exist=True)
            args[0] = str(validated_path)
        except ValueError:
            # If validation fails, check if it's a valid executable name
            # (e.g., "python", "npm", etc.)
            if not executable.replace("_", "").replace("-", "").isalnum():
                raise ValueError(f"Invalid executable name: {executable}") from None

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
