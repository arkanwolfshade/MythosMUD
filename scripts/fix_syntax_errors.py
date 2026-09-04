#!/usr/bin/env python3
"""
Syntax Error Fixer for Automated F-String Remediation

This script fixes the syntax errors introduced by the automated f-string fixer.
It handles the most common malformed patterns and restores proper syntax.

As noted in the Pnakotic Manuscripts, proper remediation requires precision and
careful attention to syntax correctness.
"""

import re
import sys
from pathlib import Path


class SyntaxErrorFixer:
    """Tool to fix syntax errors introduced by automated f-string remediation."""

    def __init__(self, dry_run: bool = False, verbose: bool = False):
        self.dry_run = dry_run
        self.verbose = verbose
        self.fixes_applied = 0
        self.files_processed = 0

    def fix_malformed_logger_calls(self, content: str) -> str:
        """Fix malformed logger calls with broken syntax."""
        fixes_applied = 0

        # Pattern 1: Fix malformed logger calls with broken quotes and brackets
        # Example: logger.info("message: {results[")spawned']}")
        # pattern1 = re.compile(r'logger\.(\w+)\s*\(\s*"([^"]*\{[^}]*\["\)[^"]*)"\s*\)')

        def fix_pattern1(match):
            nonlocal fixes_applied
            # This is a complex malformed pattern - skip for now
            return match.group(0)  # Return unchanged

        # Pattern 2: Fix logger calls with extra closing parentheses
        # Example: logger.info("message", param=value))
        pattern2 = re.compile(r'logger\.(\w+)\s*\(\s*"([^"]*)"\s*,\s*([^)]+)\)\)')

        def fix_pattern2(match):
            nonlocal fixes_applied
            method = match.group(1)
            message = match.group(2)
            params = match.group(3)

            fixes_applied += 1
            return f'logger.{method}("{message}", {params})'

        # Pattern 3: Fix logger calls with malformed parameters
        # Example: logger.info("message", param=param))
        pattern3 = re.compile(r'logger\.(\w+)\s*\(\s*"([^"]*)"\s*,\s*([^)]+)\)\)')

        def fix_pattern3(match):
            nonlocal fixes_applied
            method = match.group(1)
            message = match.group(2)
            params = match.group(3)

            # Clean up malformed parameters
            clean_params = params.replace("=param)", "").replace("=e)", "")
            if clean_params.endswith(","):
                clean_params = clean_params[:-1]

            fixes_applied += 1
            return f'logger.{method}("{message}", {clean_params})'

        # Apply fixes
        new_content = pattern2.sub(fix_pattern2, content)
        new_content = pattern3.sub(fix_pattern3, new_content)

        return new_content, fixes_applied

    def fix_specific_file(self, file_path: Path) -> int:
        """Fix syntax errors in a specific file."""
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
        new_content, fixes_applied = self.fix_malformed_logger_calls(content)

        # Only write if changes were made and not in dry run mode
        if new_content != original_content and not self.dry_run:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            if self.verbose:
                print(f"Fixed {fixes_applied} syntax errors in {file_path}")
        elif self.dry_run and new_content != original_content:
            if self.verbose:
                print(f"Would fix {fixes_applied} syntax errors in {file_path}")

        return fixes_applied

    def process_files(self, file_paths: list[Path]) -> dict:
        """Process multiple files and return statistics."""
        results = {"total_fixes": 0, "files_processed": 0, "files_with_fixes": 0, "errors": []}

        for file_path in file_paths:
            if not file_path.exists():
                results["errors"].append(f"File {file_path} does not exist")
                continue

            try:
                fixes = self.fix_specific_file(file_path)
                results["total_fixes"] += fixes
                results["files_processed"] += 1

                if fixes > 0:
                    results["files_with_fixes"] += 1
                    if self.verbose:
                        print(f"Fixed {fixes} syntax errors in {file_path}")

            except Exception as e:
                results["errors"].append(f"Error processing {file_path}: {e}")

        return results


def main():
    """Main function to run the syntax error fixer."""
    import argparse

    parser = argparse.ArgumentParser(description="Syntax Error Fixer for Automated F-String Remediation")
    parser.add_argument("files", nargs="*", help="Files to process")
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
        print("No files specified. Use --all-server or provide file paths.")
        sys.exit(1)

    if not files_to_process:
        print("No Python files found to process")
        sys.exit(1)

    # Create fixer instance
    fixer = SyntaxErrorFixer(dry_run=args.dry_run, verbose=args.verbose)

    # Process files
    results = fixer.process_files(files_to_process)

    # Display results
    print(f"Processed {results['files_processed']} files")
    print(f"Fixed {results['total_fixes']} syntax errors in {results['files_with_fixes']} files")

    if results["errors"]:
        print("Errors:")
        for error in results["errors"]:
            print(f"  {error}")
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
