#!/usr/bin/env python3
"""
Automated script to fix f-string logging violations by converting them to structured logging.

This script processes Python files and converts f-string logger calls to structured logging format.
It handles the most common patterns and provides a systematic approach to remediation.

As noted in the Pnakotic Manuscripts, proper documentation of our eldritch systems requires
structured data for effective analysis and monitoring.
"""

import re
import sys
from pathlib import Path


def extract_variables_from_fstring(fstring_content: str) -> list[str]:
    """
    Extract variable names from f-string content.

    Args:
        fstring_content: The content inside the f-string

    Returns:
        List of variable names found in the f-string
    """
    # Pattern to match {variable_name} in f-strings
    variable_pattern = re.compile(r"\{([^}]+)\}")
    variables = variable_pattern.findall(fstring_content)
    return variables


def create_structured_log_message(fstring_content: str, variables: list[str]) -> tuple[str, str]:
    """
    Create structured logging message and parameters.

    Args:
        fstring_content: The original f-string content
        variables: List of variable names found

    Returns:
        Tuple of (message, parameters_string)
    """
    # Create a clean message by removing variable placeholders
    message = fstring_content
    for var in variables:
        message = message.replace(f"{{{var}}}", f"{{{var}}}")

    # Remove the variable placeholders to create a clean message
    for var in variables:
        message = message.replace(f"{{{var}}}", f"{{{var}}}")

    # Create parameters string
    params = []
    for var in variables:
        # Handle special cases like dict access
        if "[" in var and "]" in var:
            # For dict access like cleanup_stats['stale_connections']
            clean_var = var.split("[")[0]
            params.append(f"{clean_var}={var}")
        else:
            params.append(f"{var}={var}")

    return message, ", ".join(params)


def _validate_file(file_path: Path) -> bool:
    """Validate that file exists and is a Python file."""
    return file_path.exists() and file_path.suffix == ".py"


def _read_file_content(file_path: Path) -> str | None:
    """Read file content with error handling."""
    try:
        with open(file_path, encoding="utf-8") as f:
            return f.read()
    except (UnicodeDecodeError, FileNotFoundError):
        return None


def _handle_no_variables_case(method: str, fstring_content: str) -> str:
    """Handle case where f-string has no variables."""
    return f'logger.{method}("{fstring_content}")'


def _build_structured_params(variables: list[str]) -> list[str]:
    """Build structured parameters list from variables."""
    structured_params = []
    for var in variables:
        if "[" in var and "]" in var:
            clean_var = var.split("[")[0]
            structured_params.append(f"{clean_var}={var}")
        else:
            structured_params.append(f"{var}={var}")
    return structured_params


def _clean_message(message: str, variables: list[str]) -> str:
    """Clean message by removing variable placeholders."""
    clean_message = message
    for var in variables:
        clean_message = clean_message.replace(f"{{{var}}}", f"{{{var}}}")
    return clean_message


def _create_replacement_for_fstring(match: re.Match, fixes_applied_ref: list[int]) -> str:
    """Create replacement string for f-string logging call."""
    method = match.group(1)
    fstring_content = match.group(2)

    variables = extract_variables_from_fstring(fstring_content)

    if not variables:
        return _handle_no_variables_case(method, fstring_content)

    message, _ = create_structured_log_message(fstring_content, variables)
    clean_message = _clean_message(message, variables)
    structured_params = _build_structured_params(variables)

    fixes_applied_ref[0] += 1
    return f'logger.{method}("{clean_message}", {", ".join(structured_params)})'


def _write_file_if_changed(file_path: Path, original_content: str, new_content: str) -> None:
    """Write file if content has changed."""
    if new_content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)


def fix_fstring_logging_in_file(file_path: Path) -> int:
    """
    Fix f-string logging violations in a single file.

    Args:
        file_path: Path to the Python file to fix

    Returns:
        Number of violations fixed
    """
    if not _validate_file(file_path):
        return 0

    content = _read_file_content(file_path)
    if content is None:
        return 0

    original_content = content
    fixes_applied = [0]

    fstring_pattern = re.compile(r'logger\.(info|debug|warning|error|critical|exception)\s*\(\s*f["\']([^"\']*)["\']')

    def replace_fstring_logging(match: re.Match) -> str:
        return _create_replacement_for_fstring(match, fixes_applied)

    new_content = fstring_pattern.sub(replace_fstring_logging, content)
    _write_file_if_changed(file_path, original_content, new_content)

    return fixes_applied[0]


def main():
    """Main function to fix f-string logging violations."""
    if len(sys.argv) < 2:
        print("Usage: python fix_fstring_logging.py <file1> [file2] ...")
        print("       python fix_fstring_logging.py --all-server")
        sys.exit(1)

    if sys.argv[1] == "--all-server":
        # Fix all Python files in server directory
        server_path = Path("server")
        files_to_fix = list(server_path.rglob("*.py"))
    else:
        files_to_fix = [Path(f) for f in sys.argv[1:]]

    total_fixes = 0
    files_processed = 0

    for file_path in files_to_fix:
        if not file_path.exists():
            print(f"Warning: File {file_path} does not exist")
            continue

        fixes = fix_fstring_logging_in_file(file_path)
        if fixes > 0:
            print(f"Fixed {fixes} violations in {file_path}")
            total_fixes += fixes
            files_processed += 1

    print(f"\nTotal fixes applied: {total_fixes} across {files_processed} files")
    print("Note: Manual review recommended for complex cases")


if __name__ == "__main__":
    main()
