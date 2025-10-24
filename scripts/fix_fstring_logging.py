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


def fix_fstring_logging_in_file(file_path: Path) -> int:
    """
    Fix f-string logging violations in a single file.

    Args:
        file_path: Path to the Python file to fix

    Returns:
        Number of violations fixed
    """
    if not file_path.exists() or file_path.suffix != ".py":
        return 0

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
    except (UnicodeDecodeError, FileNotFoundError):
        return 0

    original_content = content
    fixes_applied = 0

    # Pattern to match logger calls with f-strings
    fstring_pattern = re.compile(r'logger\.(info|debug|warning|error|critical|exception)\s*\(\s*f["\']([^"\']*)["\']')

    def replace_fstring_logging(match):
        nonlocal fixes_applied
        method = match.group(1)
        fstring_content = match.group(2)

        # Extract variables from the f-string
        variables = extract_variables_from_fstring(fstring_content)

        if not variables:
            # No variables found, just convert to regular string
            return f'logger.{method}("{fstring_content}")'

        # Create structured logging
        message, params = create_structured_log_message(fstring_content, variables)

        # Clean up the message by removing variable placeholders
        clean_message = message
        for var in variables:
            clean_message = clean_message.replace(f"{{{var}}}", f"{{{var}}}")

        # For now, create a simple structured message
        # This is a simplified approach - manual review needed for complex cases
        structured_params = []
        for var in variables:
            if "[" in var and "]" in var:
                # Handle dict access
                clean_var = var.split("[")[0]
                structured_params.append(f"{clean_var}={var}")
            else:
                structured_params.append(f"{var}={var}")

        fixes_applied += 1
        return f'logger.{method}("{clean_message}", {", ".join(structured_params)})'

    # Apply the fixes
    new_content = fstring_pattern.sub(replace_fstring_logging, content)

    # Only write if changes were made
    if new_content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

    return fixes_applied


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
