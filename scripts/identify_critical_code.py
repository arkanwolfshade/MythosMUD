#!/usr/bin/env python3
"""
Identify critical and complex code sections requiring enhanced documentation.

Scans the codebase to find files and functions that are:
- Security-sensitive (auth, validation, command processing)
- Business-critical (combat, inventory, persistence)
- Complex (high cyclomatic complexity, state machines, async coordination)
- Performance-critical (game tick processing, message handling)

As documented in the restricted archives, critical code paths require
comprehensive documentation to ensure maintainability and prevent regressions.
"""

from __future__ import annotations

import ast
import json
from pathlib import Path
from typing import Any

# Keywords indicating critical code
SECURITY_KEYWORDS = [
    "auth",
    "authentication",
    "authorization",
    "security",
    "validator",
    "validation",
    "sanitize",
    "sanitization",
    "command",
    "injection",
    "csrf",
    "password",
    "hash",
    "encrypt",
]

BUSINESS_CRITICAL_KEYWORDS = [
    "combat",
    "inventory",
    "persistence",
    "database",
    "death",
    "respawn",
    "corpse",
    "player",
    "character",
    "spell",
    "magic",
    "economy",
    "transaction",
]

COMPLEXITY_KEYWORDS = [
    "state_machine",
    "state machine",
    "async",
    "coordination",
    "lock",
    "mutex",
    "guard",
    "mutation",
    "concurrency",
    "thread",
    "event",
    "handler",
    "dispatcher",
]

PERFORMANCE_KEYWORDS = [
    "tick",
    "game_tick",
    "message",
    "handler",
    "broadcast",
    "sync",
    "cache",
    "optimize",
    "performance",
]


def calculate_complexity(node: ast.AST) -> int:
    """
    Calculate cyclomatic complexity of an AST node.

    Args:
        node: AST node to analyze

    Returns:
        Complexity score
    """
    complexity = 1  # Base complexity

    for child in ast.walk(node):
        if isinstance(child, (ast.If, ast.While, ast.For, ast.AsyncFor)):
            complexity += 1
        elif isinstance(child, ast.Try):
            complexity += len(child.handlers)
        elif isinstance(child, (ast.And, ast.Or)):
            complexity += 1

    return complexity


def check_file_keywords(file_path: Path) -> dict[str, list[str]]:
    """
    Check file path and name for keyword matches.

    Args:
        file_path: Path to file to check

    Returns:
        Dictionary with keyword categories as keys and matched keywords as values
    """
    file_path_str = str(file_path).lower()
    file_name = file_path.name.lower()

    indicators = {
        "security_indicators": [],
        "business_critical_indicators": [],
        "complexity_indicators": [],
        "performance_indicators": [],
    }

    for keyword in SECURITY_KEYWORDS:
        if keyword in file_path_str or keyword in file_name:
            indicators["security_indicators"].append(keyword)

    for keyword in BUSINESS_CRITICAL_KEYWORDS:
        if keyword in file_path_str or keyword in file_name:
            indicators["business_critical_indicators"].append(keyword)

    for keyword in COMPLEXITY_KEYWORDS:
        if keyword in file_path_str or keyword in file_name:
            indicators["complexity_indicators"].append(keyword)

    for keyword in PERFORMANCE_KEYWORDS:
        if keyword in file_path_str or keyword in file_name:
            indicators["performance_indicators"].append(keyword)

    return indicators


def check_function_keywords(func_name: str) -> list[str]:
    """
    Check function name for keyword matches.

    Args:
        func_name: Function name to check

    Returns:
        List of matched keyword indicators
    """
    func_name_lower = func_name.lower()
    indicators = []

    for keyword in SECURITY_KEYWORDS:
        if keyword in func_name_lower:
            indicators.append(f"security:{keyword}")

    for keyword in BUSINESS_CRITICAL_KEYWORDS:
        if keyword in func_name_lower:
            indicators.append(f"business:{keyword}")

    for keyword in COMPLEXITY_KEYWORDS:
        if keyword in func_name_lower:
            indicators.append(f"complexity:{keyword}")

    for keyword in PERFORMANCE_KEYWORDS:
        if keyword in func_name_lower:
            indicators.append(f"performance:{keyword}")

    return indicators


def analyze_function(node: ast.FunctionDef | ast.AsyncFunctionDef) -> dict[str, Any] | None:
    """
    Analyze a single function node for critical indicators.

    Args:
        node: Function AST node to analyze

    Returns:
        Dictionary with function analysis data, or None if not critical
    """
    func_name = node.name
    complexity = calculate_complexity(node)
    func_indicators = check_function_keywords(func_name)
    is_critical = bool(func_indicators)

    # High complexity functions are critical
    if complexity > 10:
        is_critical = True
        func_indicators.append(f"high_complexity:{complexity}")

    if is_critical or complexity > 10:
        return {
            "name": func_name,
            "line": node.lineno,
            "complexity": complexity,
            "indicators": func_indicators,
            "is_async": isinstance(node, ast.AsyncFunctionDef),
        }

    return None


def process_ast_functions(tree: ast.AST) -> tuple[list[dict[str, Any]], int]:
    """
    Process all functions in the AST and identify critical ones.

    Args:
        tree: AST root node

    Returns:
        Tuple of (list of critical functions, maximum complexity)
    """
    critical_functions = []
    max_complexity = 0

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            func_data = analyze_function(node)
            if func_data:
                critical_functions.append(func_data)
                max_complexity = max(max_complexity, func_data["complexity"])

    return critical_functions, max_complexity


def analyze_file(file_path: Path) -> dict[str, Any]:
    """
    Analyze a file for critical code indicators.

    Args:
        file_path: Path to file to analyze

    Returns:
        Analysis results
    """
    result = {
        "file": str(file_path.relative_to(Path.cwd())),
        "critical_functions": [],
        "security_indicators": [],
        "business_critical_indicators": [],
        "complexity_indicators": [],
        "performance_indicators": [],
        "max_complexity": 0,
    }

    try:
        content = file_path.read_text(encoding="utf-8")
        tree = ast.parse(content, filename=str(file_path))
    except (SyntaxError, UnicodeDecodeError, PermissionError):
        return result

    # Check file path and name for keywords
    file_indicators = check_file_keywords(file_path)
    result.update(file_indicators)

    # Analyze functions in the AST
    critical_functions, max_complexity = process_ast_functions(tree)
    result["critical_functions"] = critical_functions
    result["max_complexity"] = max_complexity

    return result


def calculate_priority(analysis: dict[str, Any]) -> int:
    """
    Calculate priority score for a file (higher = more critical).

    Args:
        analysis: File analysis results

    Returns:
        Priority score
    """
    score = 0

    # Security is highest priority
    score += len(analysis["security_indicators"]) * 10

    # Business critical is high priority
    score += len(analysis["business_critical_indicators"]) * 7

    # Complexity and performance are medium priority
    score += len(analysis["complexity_indicators"]) * 5
    score += len(analysis["performance_indicators"]) * 5

    # High complexity functions add to priority
    score += len(analysis["critical_functions"]) * 3

    # Very high complexity adds significant priority
    if analysis["max_complexity"] > 15:
        score += 20
    elif analysis["max_complexity"] > 10:
        score += 10

    return score


def main() -> None:
    """Main entry point for critical code identification."""
    workspace_root = Path.cwd()
    server_dir = workspace_root / "server"

    all_analyses: list[dict[str, Any]] = []

    # Analyze Python files (TypeScript complexity analysis would require different tools)
    if server_dir.exists():
        for py_file in server_dir.rglob("*.py"):
            # Skip test files for now (focus on production code)
            if "test" in py_file.name.lower() or "tests" in str(py_file):
                continue

            analysis = analyze_file(py_file)
            if (
                analysis["critical_functions"]
                or analysis["security_indicators"]
                or analysis["business_critical_indicators"]
                or analysis["max_complexity"] > 10
            ):
                analysis["priority"] = calculate_priority(analysis)
                all_analyses.append(analysis)

    # Sort by priority
    all_analyses.sort(key=lambda x: x["priority"], reverse=True)

    # Generate report
    report = {
        "summary": {
            "total_critical_files": len(all_analyses),
            "high_priority_files": len([a for a in all_analyses if a["priority"] >= 20]),
            "medium_priority_files": len([a for a in all_analyses if 10 <= a["priority"] < 20]),
            "low_priority_files": len([a for a in all_analyses if a["priority"] < 10]),
        },
        "files": all_analyses,
        "by_category": {
            "security": [a for a in all_analyses if a["security_indicators"]],
            "business_critical": [a for a in all_analyses if a["business_critical_indicators"]],
            "high_complexity": [a for a in all_analyses if a["max_complexity"] > 10],
            "performance": [a for a in all_analyses if a["performance_indicators"]],
        },
    }

    # Write report
    artifacts_dir = workspace_root / "artifacts"
    artifacts_dir.mkdir(exist_ok=True)

    report_path = artifacts_dir / "critical_code_sections.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    # Print summary
    print("Critical Code Identification Complete")
    print(f"Total critical files: {len(all_analyses)}")
    print(f"High priority (>=20): {report['summary']['high_priority_files']}")
    print(f"Medium priority (10-19): {report['summary']['medium_priority_files']}")
    print(f"Low priority (<10): {report['summary']['low_priority_files']}")
    print(f"\nReport written to: {report_path}")


if __name__ == "__main__":
    main()
