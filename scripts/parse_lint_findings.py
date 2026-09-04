#!/usr/bin/env python3
"""Parse lint findings from lint_output.txt and create a structured catalog."""

import json
import re
from pathlib import Path


def parse_lint_findings():
    """Parse C901 complexity findings from lint output."""
    project_root = Path(__file__).parent.parent
    lint_file = project_root / "lint_output.txt"

    if not lint_file.exists():
        print(f"Error: {lint_file} not found")
        return []

    content = lint_file.read_text(encoding="utf-8", errors="ignore")
    # Remove ANSI escape codes
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    content = ansi_escape.sub("", content)
    lines = content.split("\n")

    findings = []
    i = 0

    while i < len(lines):
        line = lines[i]
        if "C901" in line and "too complex" in line:
            # Extract function name - look for backtick-enclosed name
            func_match = re.search(r"`([^`]+)`", line)
            if not func_match:
                i += 1
                continue

            func_name = func_match.group(1)

            # Extract complexity score
            complexity_match = re.search(r"\((\d+) > 11\)", line)
            if not complexity_match:
                i += 1
                continue

            complexity = int(complexity_match.group(1))

            # Find file path and line number (usually on next line with -->)
            file_path = None
            line_num = 0

            # Look ahead for file path
            for j in range(i + 1, min(i + 5, len(lines))):
                if "-->" in lines[j]:
                    # Pattern: --> path:line:
                    path_match = re.search(r"--> (.*?):(\d+):", lines[j])
                    if path_match:
                        file_path = path_match.group(1).strip()
                        line_num = int(path_match.group(2))
                        break

            if file_path:
                findings.append({"function": func_name, "complexity": complexity, "file": file_path, "line": line_num})

        i += 1

    return findings


if __name__ == "__main__":
    findings = parse_lint_findings()
    print(f"Total findings: {len(findings)}")

    # Sort by complexity descending
    sorted_findings = sorted(findings, key=lambda x: x["complexity"], reverse=True)

    # Group by file
    by_file = {}
    for finding in findings:
        file = finding["file"]
        if file not in by_file:
            by_file[file] = []
        by_file[file].append(finding)

    # Print summary
    print("\n=== Findings by Severity ===")
    critical = [f for f in findings if f["complexity"] > 30]
    high = [f for f in findings if 20 < f["complexity"] <= 30]
    medium = [f for f in findings if 15 < f["complexity"] <= 20]
    low = [f for f in findings if 12 <= f["complexity"] <= 15]

    print(f"Critical (>30): {len(critical)}")
    print(f"High (20-30): {len(high)}")
    print(f"Medium (15-19): {len(medium)}")
    print(f"Low (12-14): {len(low)}")

    print("\n=== Top 20 Most Complex ===")
    for i, finding in enumerate(sorted_findings[:20], 1):
        print(f"{i}. {finding['function']} ({finding['complexity']}) - {finding['file']}:{finding['line']}")

    print("\n=== Files with Most Violations ===")
    file_counts = sorted(by_file.items(), key=lambda x: len(x[1]), reverse=True)
    for file, file_findings in file_counts[:10]:
        print(f"{file}: {len(file_findings)} violations")

    # Save to JSON
    output_file = Path(__file__).parent.parent / "lint_findings_catalog.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            {
                "total": len(findings),
                "by_severity": {"critical": critical, "high": high, "medium": medium, "low": low},
                "by_file": by_file,
                "all_findings": sorted_findings,
            },
            f,
            indent=2,
        )

    print(f"\nCatalog saved to: {output_file}")
