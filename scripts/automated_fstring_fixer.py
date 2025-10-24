#!/usr/bin/env python3
"""
Automated F-String Logging Remediation Tool

This script systematically converts f-string logger calls to structured logging format.
It handles the most common patterns and provides detailed reporting on what was fixed.

As noted in the Pnakotic Manuscripts, proper documentation of our eldritch systems requires
systematic remediation of forbidden patterns to maintain structured logging benefits.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Any


class FStringLoggingFixer:
    """Automated tool to fix f-string logging violations."""

    def __init__(self, dry_run: bool = False, verbose: bool = False):
        self.dry_run = dry_run
        self.verbose = verbose
        self.fixes_applied = 0
        self.files_processed = 0
        self.patterns_fixed = {}

    def extract_variables_from_fstring(self, fstring_content: str) -> list[str]:
        """Extract variable names from f-string content."""
        # Pattern to match {variable_name} in f-strings
        variable_pattern = re.compile(r"\{([^}]+)\}")
        variables = variable_pattern.findall(fstring_content)
        return variables

    def create_structured_message(self, fstring_content: str, variables: list[str]) -> tuple[str, str]:
        """
        Create structured logging message and parameters.

        Returns:
            Tuple of (clean_message, parameters_string)
        """
        # Create a clean message by replacing variables with placeholders
        clean_message = fstring_content

        # Remove variable placeholders to create a clean message
        for var in variables:
            # Handle complex expressions like {player_id} or {len(players)}
            clean_message = clean_message.replace(f"{{{var}}}", f"{{{var}}}")

        # Create parameters string
        params = []
        for var in variables:
            # Handle special cases like dict access or method calls
            if "[" in var and "]" in var:
                # For dict access like cleanup_stats['stale_connections']
                clean_var = var.split("[")[0]
                params.append(f"{clean_var}={var}")
            elif "." in var and "(" in var:
                # For method calls like room.get_occupant_count()
                clean_var = var.split(".")[0]
                params.append(f"{clean_var}={var}")
            else:
                params.append(f"{var}={var}")

        return clean_message, ", ".join(params)

    def fix_simple_pattern(self, match) -> str:
        """Fix simple f-string patterns like logger.info with variables."""
        method = match.group(1)
        fstring_content = match.group(2)

        # Extract variables
        variables = self.extract_variables_from_fstring(fstring_content)

        if not variables:
            # No variables found, just convert to regular string
            return f'logger.{method}("{fstring_content}")'

        # Create structured logging
        clean_message, params = self.create_structured_message(fstring_content, variables)

        # Clean up the message by removing variable placeholders
        for var in variables:
            clean_message = clean_message.replace(f"{{{var}}}", f"{{{var}}}")

        self.fixes_applied += 1
        pattern_key = f"simple_{method}"
        self.patterns_fixed[pattern_key] = self.patterns_fixed.get(pattern_key, 0) + 1

        return f'logger.{method}("{clean_message}", {params})'

    def fix_complex_pattern(self, match) -> str:
        """Fix complex f-string patterns with method calls and expressions."""
        method = match.group(1)
        fstring_content = match.group(2)

        # Extract variables and handle complex expressions
        variables = self.extract_variables_from_fstring(fstring_content)

        if not variables:
            return f'logger.{method}("{fstring_content}")'

        # For complex patterns, create a more sophisticated structured message
        clean_message = fstring_content

        # Handle common patterns
        if "DEBUG:" in clean_message:
            clean_message = clean_message.replace("DEBUG:", "").strip()
        if "🔍 DEBUG:" in clean_message:
            clean_message = clean_message.replace("🔍 DEBUG:", "").strip()

        # Create parameters
        params = []
        for var in variables:
            if "[" in var and "]" in var:
                # Dict access
                clean_var = var.split("[")[0]
                params.append(f"{clean_var}={var}")
            elif "." in var and "(" in var:
                # Method call
                clean_var = var.split(".")[0]
                params.append(f"{clean_var}={var}")
            else:
                params.append(f"{var}={var}")

        self.fixes_applied += 1
        pattern_key = f"complex_{method}"
        self.patterns_fixed[pattern_key] = self.patterns_fixed.get(pattern_key, 0) + 1

        return f'logger.{method}("{clean_message}", {", ".join(params)})'

    def fix_fstring_logging_in_file(self, file_path: Path) -> int:
        """Fix f-string logging violations in a single file."""
        if not file_path.exists() or file_path.suffix != ".py":
            return 0

        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()
        except (UnicodeDecodeError, FileNotFoundError):
            if self.verbose:
                print(f"Warning: Could not read {file_path}")
            return 0

        original_content = content
        fixes_applied = 0

        # Pattern 1: Simple f-string patterns
        simple_pattern = re.compile(
            r'logger\.(info|debug|warning|error|critical|exception)\s*\(\s*f["\']([^"\']*)["\']'
        )

        def replace_simple(match):
            nonlocal fixes_applied
            result = self.fix_simple_pattern(match)
            fixes_applied += 1
            return result

        # Pattern 2: Complex patterns with additional parameters
        complex_pattern = re.compile(
            r'logger\.(info|debug|warning|error|critical|exception)\s*\(\s*f["\']([^"\']*)["\']\s*,\s*([^)]+)\)'
        )

        def replace_complex(match):
            nonlocal fixes_applied
            method = match.group(1)
            fstring_content = match.group(2)
            additional_params = match.group(3)

            # Extract variables
            variables = self.extract_variables_from_fstring(fstring_content)

            if not variables:
                return f'logger.{method}("{fstring_content}", {additional_params})'

            # Create structured message
            clean_message = fstring_content
            for var in variables:
                clean_message = clean_message.replace(f"{{{var}}}", f"{{{var}}}")

            # Create parameters
            params = []
            for var in variables:
                if "[" in var and "]" in var:
                    clean_var = var.split("[")[0]
                    params.append(f"{clean_var}={var}")
                else:
                    params.append(f"{var}={var}")

            fixes_applied += 1
            return f'logger.{method}("{clean_message}", {", ".join(params)}, {additional_params})'

        # Apply fixes
        new_content = simple_pattern.sub(replace_simple, content)
        new_content = complex_pattern.sub(replace_complex, new_content)

        # Only write if changes were made and not in dry run mode
        if new_content != original_content and not self.dry_run:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            if self.verbose:
                print(f"Fixed {fixes_applied} violations in {file_path}")
        elif self.dry_run and new_content != original_content:
            if self.verbose:
                print(f"Would fix {fixes_applied} violations in {file_path}")

        return fixes_applied

    def process_files(self, file_paths: list[Path]) -> dict[str, Any]:
        """Process multiple files and return statistics."""
        results = {"total_fixes": 0, "files_processed": 0, "files_with_fixes": 0, "patterns_fixed": {}, "errors": []}

        for file_path in file_paths:
            if not file_path.exists():
                results["errors"].append(f"File {file_path} does not exist")
                continue

            try:
                fixes = self.fix_fstring_logging_in_file(file_path)
                results["total_fixes"] += fixes
                results["files_processed"] += 1

                if fixes > 0:
                    results["files_with_fixes"] += 1
                    if self.verbose:
                        print(f"Fixed {fixes} violations in {file_path}")

            except Exception as e:
                results["errors"].append(f"Error processing {file_path}: {e}")

        results["patterns_fixed"] = self.patterns_fixed
        return results

    def generate_report(self, results: dict[str, Any]) -> str:
        """Generate a detailed report of the remediation process."""
        report = []
        report.append("F-STRING LOGGING REMEDIATION REPORT")
        report.append("=" * 50)
        report.append("")

        if self.dry_run:
            report.append("🔍 DRY RUN MODE - No files were modified")
            report.append("")

        report.append("📊 STATISTICS:")
        report.append(f"  Files processed: {results['files_processed']}")
        report.append(f"  Files with fixes: {results['files_with_fixes']}")
        report.append(f"  Total fixes applied: {results['total_fixes']}")
        report.append("")

        if results["patterns_fixed"]:
            report.append("🔧 PATTERNS FIXED:")
            for pattern, count in results["patterns_fixed"].items():
                report.append(f"  {pattern}: {count} fixes")
            report.append("")

        if results["errors"]:
            report.append("❌ ERRORS:")
            for error in results["errors"]:
                report.append(f"  {error}")
            report.append("")

        report.append("✅ REMEDIATION COMPLETE")
        report.append("")
        report.append("Next steps:")
        report.append("1. Run 'make lint' to verify all fixes")
        report.append("2. Run tests to ensure functionality is preserved")
        report.append("3. Review any remaining violations manually")

        return "\n".join(report)


def main():
    """Main function to run the automated f-string fixer."""
    parser = argparse.ArgumentParser(description="Automated F-String Logging Remediation Tool")
    parser.add_argument("files", nargs="*", help="Files to process (default: all Python files in server/)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be fixed without making changes")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed output")
    parser.add_argument("--all-server", action="store_true", help="Process all Python files in server directory")

    args = parser.parse_args()

    # Determine files to process
    if args.all_server:
        files_to_process = list(Path("server").rglob("*.py"))
    elif args.files:
        files_to_process = [Path(f) for f in args.files]
    else:
        # Default: process all Python files in server directory
        files_to_process = list(Path("server").rglob("*.py"))

    if not files_to_process:
        print("No Python files found to process")
        sys.exit(1)

    # Create fixer instance
    fixer = FStringLoggingFixer(dry_run=args.dry_run, verbose=args.verbose)

    # Process files
    results = fixer.process_files(files_to_process)

    # Generate and display report
    report = fixer.generate_report(results)
    print(report)

    # Exit with appropriate code
    if results["errors"]:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
