#!/usr/bin/env python3
"""
Enhanced Logging Compliance Verification Script

This script verifies that all server production code uses the enhanced logging system
as required by .cursor/rules/structlog.mdc and the project's logging standards.

As documented in the restricted archives of Miskatonic University, proper logging
is the foundation upon which all system observability and debugging capabilities rest.
"""

import ast
import re
import sys
from pathlib import Path

# Colors for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"


class LoggingComplianceChecker(ast.NodeVisitor):
    """AST visitor to check logging compliance."""

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.violations: list[tuple[int, str, str]] = []  # (line, type, message)
        self.uses_enhanced_logging = False
        self.has_logger = False
        self.imports_logging = False

    def visit_Import(self, node: ast.Import) -> None:  # noqa: N802, N815
        """Check for deprecated logging imports. Name required by ast.NodeVisitor API."""
        for alias in node.names:
            if alias.name == "logging":
                # Check if this is an allowed exception (logging module itself or formatter)
                if "logging" not in str(self.file_path):
                    # Only violation if not in logging module directory
                    self.violations.append(
                        (
                            node.lineno,
                            "FORBIDDEN_IMPORT",
                            "Found 'import logging' - Use 'from server.logging.enhanced_logging_config import get_logger' instead",
                        )
                    )
                    self.imports_logging = True
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:  # noqa: N802, N815
        """Check for deprecated logging imports. Name required by ast.NodeVisitor API."""
        if node.module == "logging":
            # Direct imports from logging module (forbidden)
            if "logging" not in str(self.file_path):
                self.violations.append(
                    (
                        node.lineno,
                        "FORBIDDEN_IMPORT",
                        "Found 'from logging import ...' - Use 'from server.logging.enhanced_logging_config import get_logger' instead",
                    )
                )
                self.imports_logging = True
        elif node.module and "enhanced_logging_config" in node.module:
            # Check if importing get_logger
            for alias in node.names:
                if alias.name == "get_logger":
                    self.uses_enhanced_logging = True
        self.generic_visit(node)

    def _check_getlogger_call(self, node: ast.Call) -> None:
        """Record violation if node is a logging.getLogger() call in non-infra code."""
        if not isinstance(node.func, ast.Attribute):
            return
        if not isinstance(node.func.value, ast.Name) or node.func.value.id != "logging":
            return
        if node.func.attr != "getLogger":
            return
        if "logging" in str(self.file_path) or "test" in str(self.file_path):
            return
        self.violations.append(
            (
                node.lineno,
                "FORBIDDEN_GETLOGGER",
                "Found 'logging.getLogger()' - Use 'get_logger()' from enhanced_logging_config instead",
            )
        )

    def _check_fstring_logging(self, node: ast.Call) -> None:
        """Record violation if node is a logger.*(f\"...\") style call."""
        if not isinstance(node.func, ast.Attribute):
            return
        if node.func.attr not in ("info", "debug", "warning", "error", "critical", "exception"):
            return
        if not isinstance(node.func.value, ast.Name) or node.func.value.id != "logger":
            return
        if not node.args or not isinstance(node.args[0], ast.JoinedStr):
            return
        self.violations.append(
            (
                node.lineno,
                "FSTRING_LOGGING",
                "Found f-string in logger call - Use structured logging with key-value pairs instead",
            )
        )

    def _check_deprecated_context_param(self, node: ast.Call) -> None:
        """Record violation if node is an error_logging call with context= keyword."""
        if not isinstance(node.func, ast.Name):
            return
        func_name = node.func.id
        if func_name not in (
            "log_and_raise",
            "log_and_raise_http",
            "log_error_with_context",
            "create_logged_http_exception",
            "wrap_third_party_exception",
        ):
            return
        for keyword in node.keywords:
            if keyword.arg == "context":
                self.violations.append(
                    (
                        node.lineno,
                        "DEPRECATED_CONTEXT_PARAMETER",
                        f"Found deprecated 'context=' parameter in {func_name}() - Use **kwargs instead",
                    )
                )
                break

    def visit_Call(self, node: ast.Call) -> None:  # noqa: N802, N815
        """Check for deprecated getLogger/f-string/context. Name required by ast.NodeVisitor API."""
        self._check_getlogger_call(node)
        self._check_fstring_logging(node)
        self._check_deprecated_context_param(node)
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> None:  # noqa: N802, N815  # pylint: disable=invalid-name
        """Check for logger assignment patterns. Name required by ast.NodeVisitor API."""
        # Check if assigning logger = logging.getLogger(...)
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "logger":
                self.has_logger = True
                if isinstance(node.value, ast.Call):
                    if isinstance(node.value.func, ast.Attribute):
                        if (
                            isinstance(node.value.func.value, ast.Name)
                            and node.value.func.value.id == "logging"
                            and node.value.func.attr == "getLogger"
                        ):
                            if "logging" not in str(self.file_path) and "test" not in str(self.file_path):
                                self.violations.append(
                                    (
                                        node.lineno,
                                        "FORBIDDEN_LOGGER_ASSIGNMENT",
                                        "Found 'logger = logging.getLogger(...)' - Use 'logger = get_logger(__name__)' instead",
                                    )
                                )
        self.generic_visit(node)


def _should_skip_file(file_path: Path) -> bool:
    """Return True if file should be skipped (tests, pycache, missing, or not .py)."""
    path_str = str(file_path)
    if "test" in path_str or "__pycache__" in path_str:
        return True
    if not file_path.exists() or file_path.suffix != ".py":
        return True
    return False


def _read_and_parse(file_path: Path) -> tuple[str, ast.AST] | None:
    """Read file and parse AST. Returns (content, tree) or None if unreadable/empty/syntax error."""
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
    except (UnicodeDecodeError, FileNotFoundError):
        return None
    if not content.strip():
        return None
    try:
        tree = ast.parse(content, filename=str(file_path))
    except SyntaxError:
        return None
    return content, tree


def _run_regex_checks(content: str, file_path: Path, checker: LoggingComplianceChecker) -> None:
    """Run regex-based checks on file lines and append violations to checker."""
    path_str = str(file_path)
    lines = content.split("\n")
    error_logging_func = re.compile(
        r"\b(log_and_raise|log_and_raise_http|log_error_with_context|"
        r"create_logged_http_exception|wrap_third_party_exception)\s*\("
    )
    for line_num, line in enumerate(lines, 1):
        if re.search(r'logger\.(info|debug|warning|error|critical|exception)\s*\(\s*f["\']', line):
            if "logging/README.md" not in path_str:
                checker.violations.append(
                    (
                        line_num,
                        "FSTRING_LOGGING",
                        f"Found f-string in logger call: {line.strip()[:80]}",
                    )
                )
        if re.search(r"\bcontext\s*=\s*(context|create_error_context\s*\(\))", line):
            if "logging" not in path_str and "test" not in path_str and error_logging_func.search(line):
                checker.violations.append(
                    (
                        line_num,
                        "DEPRECATED_CONTEXT_PARAMETER",
                        f"Found deprecated 'context=' parameter: {line.strip()[:80]}",
                    )
                )
        if re.search(r"\bcontext\.metadata\[", line):
            if "logging" not in path_str and "test" not in path_str:
                checker.violations.append(
                    (
                        line_num,
                        "DEPRECATED_CONTEXT_METADATA",
                        f"Found deprecated 'context.metadata[...]' pattern - Use **kwargs instead: {line.strip()[:80]}",
                    )
                )


def check_file(file_path: Path) -> tuple[bool, list[tuple[int, str, str]]]:
    """
    Check a single file for logging compliance.

    Args:
        file_path: Path to the Python file to check

    Returns:
        Tuple of (is_compliant, violations)
    """
    if _should_skip_file(file_path):
        return True, []
    parsed = _read_and_parse(file_path)
    if parsed is None:
        return True, []
    content, tree = parsed
    checker = LoggingComplianceChecker(file_path)
    checker.visit(tree)
    _run_regex_checks(content, file_path, checker)
    return len(checker.violations) == 0, checker.violations


def _find_python_files(server_dir: Path) -> list[Path]:
    """Find all Python files in server directory, excluding tests."""
    python_files = []
    for py_file in server_dir.rglob("*.py"):
        if "test" in str(py_file) or "__pycache__" in str(py_file):
            continue
        python_files.append(py_file)
    return python_files


def _check_all_files(python_files: list[Path]) -> tuple[dict[Path, list[tuple[int, str, str]]], int]:
    """Check all files and collect violations. Returns (violations_dict, compliant_count)."""
    all_violations: dict[Path, list[tuple[int, str, str]]] = {}
    compliant_files = 0

    for file_path in sorted(python_files):
        _is_compliant, violations = check_file(file_path)
        if violations:
            all_violations[file_path] = violations
        else:
            compliant_files += 1

    return all_violations, compliant_files


def _group_violations_by_type(violations: list[tuple[int, str, str]]) -> dict[str, list[tuple[int, str, str]]]:
    """Group violations by type."""
    by_type: dict[str, list[tuple[int, str, str]]] = {}
    for line_num, violation_type, message in violations:
        if violation_type not in by_type:
            by_type[violation_type] = []
        by_type[violation_type].append((line_num, violation_type, message))
    return by_type


def _print_violations_for_file(file_path: Path, violations: list[tuple[int, str, str]], project_root: Path) -> None:
    """Print violations for a single file."""
    rel_path = file_path.relative_to(project_root)
    print(f"{YELLOW}File: {rel_path}{RESET}")
    print("-" * 60)

    by_type = _group_violations_by_type(violations)
    for violation_type in sorted(by_type.keys()):
        print(f"  {RED}{violation_type}:{RESET}")
        for line_num, _, message in by_type[violation_type]:
            print(f"    Line {line_num}: {message}")
    print()


def _print_fix_instructions() -> None:
    """Print fix instructions."""
    print("HOW TO FIX:")
    print("1. Replace 'import logging' with 'from server.logging.enhanced_logging_config import get_logger'")
    print("2. Replace 'logging.getLogger(__name__)' with 'get_logger(__name__)'")
    print("3. Replace f-string logging with structured key-value pairs")
    print('   WRONG: logger.info(f"User {user_id} performed {action}")')
    print('   RIGHT: logger.info("User action", user_id=user_id, action=action)')
    print("4. Remove deprecated 'context=' parameter from error_logging functions")
    print("   WRONG: log_and_raise(Error, 'message', context=context)")
    print("   RIGHT: log_and_raise(Error, 'message', operation='op', user_id=user_id)")
    print("5. Remove 'context.metadata[...]' patterns - use **kwargs instead")
    print("   WRONG: context = create_error_context(); context.metadata['key'] = value")
    print("   RIGHT: log_and_raise(Error, 'message', key=value)")
    print()
    print("See .cursor/rules/structlog.mdc and docs/LOGGING_BEST_PRACTICES.md for details.")


def _print_violations_report(
    all_violations: dict[Path, list[tuple[int, str, str]]],
    compliant_files: int,
    python_files: list[Path],
    project_root: Path,
) -> None:
    """Print violations report."""
    print(f"{RED}{BOLD}VIOLATIONS FOUND{RESET}")
    print("=" * 60)
    print()

    total_violations = sum(len(v) for v in all_violations.values())
    print(f"Found {total_violations} violation(s) in {len(all_violations)} file(s):")
    print()

    for file_path, violations in sorted(all_violations.items()):
        _print_violations_for_file(file_path, violations, project_root)

    print(f"{RED}COMPLIANCE FAILED{RESET}")
    print(f"Compliant files: {compliant_files}/{len(python_files)}")
    print()
    _print_fix_instructions()


def _print_compliance_success(compliant_files: int) -> None:
    """Print compliance success message."""
    print(f"{GREEN}{BOLD}ALL FILES COMPLIANT{RESET}")
    print("=" * 60)
    print()
    print(f"All {compliant_files} production files use enhanced logging system")
    print()


def main():
    """Main function to check all server files for logging compliance."""
    project_root = Path(__file__).parent.parent
    server_dir = project_root / "server"

    if not server_dir.exists():
        print(f"{RED}Error: server directory not found at {server_dir}{RESET}")
        sys.exit(1)

    print(f"{BOLD}Enhanced Logging Compliance Verification{RESET}")
    print("=" * 60)
    print()

    python_files = _find_python_files(server_dir)
    print(f"Checking {len(python_files)} production files...")
    print()

    all_violations, compliant_files = _check_all_files(python_files)

    if all_violations:
        _print_violations_report(all_violations, compliant_files, python_files, project_root)
        sys.exit(1)
    else:
        _print_compliance_success(compliant_files)
        sys.exit(0)


if __name__ == "__main__":
    main()
