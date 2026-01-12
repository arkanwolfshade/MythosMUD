#!/usr/bin/env python3
"""
Compare ruff and pylint linting results.

This script parses output from both ruff and pylint, compares findings,
and generates a report showing:
- Issues found by both tools (overlapping findings)
- Issues found only by ruff (unique to ruff)
- Issues found only by pylint (unique to pylint)
- Statistics and categorization of findings

The script supports both JSON and text output formats from ruff,
and standard text output from pylint.
"""

import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from utils.safe_subprocess import safe_run_static


@dataclass
class Finding:
    """Represents a single linting finding."""

    file_path: str
    line_number: int
    column: int | None
    rule_code: str
    message: str
    tool: str  # 'ruff' or 'pylint'

    def __hash__(self) -> int:
        """Hash based on file, line, and rule code."""
        return hash((self.file_path, self.line_number, self.rule_code, self.tool))

    def __eq__(self, other: object) -> bool:
        """Equality based on file, line, and rule code."""
        if not isinstance(other, Finding):
            return False
        return (
            self.file_path == other.file_path
            and self.line_number == other.line_number
            and self.rule_code == other.rule_code
        )

    def location_key(self) -> tuple[str, int, str]:
        """Create a key for grouping findings by location."""
        return (self.file_path, self.line_number, self.rule_code)


def parse_ruff_json_output(json_data: list[dict[str, Any]]) -> list[Finding]:
    """Parse ruff JSON output format."""
    findings = []
    for item in json_data:
        file_path = item.get("filename", "").replace("\\", "/")
        location = item.get("location", {})
        line_number = location.get("row", 0)
        column = location.get("column", None)
        code = item.get("code", "")
        message = item.get("message", "")

        finding = Finding(
            file_path=file_path,
            line_number=line_number,
            column=column,
            rule_code=code,
            message=message,
            tool="ruff",
        )
        findings.append(finding)

    return findings


def parse_ruff_text_output(text: str) -> list[Finding]:
    """Parse ruff text output format."""
    findings = []
    # Ruff text format: "path/to/file.py:123:45: E501 Line too long (121 > 120 characters)"
    pattern = re.compile(r"^(.+?):(\d+):(\d+):\s+([A-Z]\d{3})\s+(.+)$", re.MULTILINE)

    for match in pattern.finditer(text):
        file_path = match.group(1).replace("\\", "/")
        line_number = int(match.group(2))
        column = int(match.group(3))
        rule_code = match.group(4)
        message = match.group(5).strip()

        finding = Finding(
            file_path=file_path,
            line_number=line_number,
            column=column,
            rule_code=rule_code,
            message=message,
            tool="ruff",
        )
        findings.append(finding)

    return findings


def parse_pylint_text_output(text: str) -> list[Finding]:
    """Parse pylint text output format."""
    findings = []
    # Pylint format: "path/to/file.py:123:8: C0301: Line too long (121/120) (line-too-long)"
    # Also handles: "************* Module module.name" headers
    pattern = re.compile(r"^(.+?):(\d+):(\d+):\s+([A-Z]\d{4}):\s+(.+?)\s+\(([^)]+)\)$", re.MULTILINE)

    for match in pattern.finditer(text):
        file_path = match.group(1).replace("\\", "/")
        line_number = int(match.group(2))
        column = int(match.group(3))
        rule_code = match.group(4)
        message = match.group(5).strip()
        rule_name = match.group(6).strip()

        # Combine message and rule name for clarity
        full_message = f"{message} ({rule_name})"

        finding = Finding(
            file_path=file_path,
            line_number=line_number,
            column=column,
            rule_code=rule_code,
            message=full_message,
            tool="pylint",
        )
        findings.append(finding)

    return findings


def get_ruff_output() -> tuple[str, str]:
    """Get ruff output in both JSON and text formats."""
    # Try JSON format first (more structured)
    try:
        result_json = safe_run_static(
            "uv",
            "run",
            "--active",
            "ruff",
            "check",
            "--output-format=json",
            ".",
            cwd=".",
            capture_output=True,
            text=True,
        )
        json_output = result_json.stdout
    except Exception as e:
        print(f"Warning: Failed to get ruff JSON output: {e}")
        json_output = "[]"

    # Also get text output as fallback
    try:
        result_text = safe_run_static(
            "uv",
            "run",
            "--active",
            "ruff",
            "check",
            ".",
            cwd=".",
            capture_output=True,
            text=True,
        )
        text_output = result_text.stdout
    except Exception as e:
        print(f"Warning: Failed to get ruff text output: {e}")
        text_output = ""

    return json_output, text_output


def load_pylint_output(file_path: Path) -> str:
    """Load pylint output from file."""
    if not file_path.exists():
        print(f"Warning: Pylint output file not found: {file_path}")
        return ""

    with file_path.open("r", encoding="utf-8") as f:
        return f.read()


def _build_file_line_index(findings: list[Finding]) -> dict[tuple[str, int], list[Finding]]:
    """Build an index of findings by file path and line number."""
    index: dict[tuple[str, int], list[Finding]] = defaultdict(list)
    for finding in findings:
        index[(finding.file_path, finding.line_number)].append(finding)
    return index


def _find_overlapping_findings(
    ruff_by_file_line: dict[tuple[str, int], list[Finding]],
    pylint_by_file_line: dict[tuple[str, int], list[Finding]],
) -> tuple[list[tuple[Finding, Finding]], set[int]]:
    """Find overlapping findings and return matches with ruff item IDs."""
    overlapping: list[tuple[Finding, Finding]] = []
    ruff_matched = set()

    for (file_path, line_num), ruff_items in ruff_by_file_line.items():
        key = (file_path, line_num)
        if key in pylint_by_file_line:
            pylint_items = pylint_by_file_line[key]
            # Consider it overlapping if same file/line
            for ruff_item in ruff_items:
                for pylint_item in pylint_items:
                    overlapping.append((ruff_item, pylint_item))
                ruff_matched.add(id(ruff_item))

    return overlapping, ruff_matched


def _find_unmatched_findings(
    findings: list[Finding],
    matched_ids: set[int],
) -> list[Finding]:
    """Find findings that are not in the matched set."""
    unmatched = []
    for finding in findings:
        if id(finding) not in matched_ids:
            unmatched.append(finding)
    return unmatched


def compare_findings(ruff_findings: list[Finding], pylint_findings: list[Finding]) -> dict[str, Any]:
    """Compare findings from both tools and categorize them."""
    # Build indices by file and line number (since rule codes differ)
    ruff_by_file_line = _build_file_line_index(ruff_findings)
    pylint_by_file_line = _build_file_line_index(pylint_findings)

    # Find overlapping findings
    overlapping, ruff_matched = _find_overlapping_findings(ruff_by_file_line, pylint_by_file_line)

    # Find ruff-only findings
    ruff_only = _find_unmatched_findings(ruff_findings, ruff_matched)

    # Find pylint-only findings
    pylint_matched = set()
    for (file_path, line_num), pylint_items in pylint_by_file_line.items():
        if (file_path, line_num) in ruff_by_file_line:
            for item in pylint_items:
                pylint_matched.add(id(item))

    pylint_only = _find_unmatched_findings(pylint_findings, pylint_matched)

    return {
        "ruff_total": len(ruff_findings),
        "pylint_total": len(pylint_findings),
        "overlapping_count": len(overlapping),
        "ruff_only_count": len(ruff_only),
        "pylint_only_count": len(pylint_only),
        "overlapping": overlapping,
        "ruff_only": ruff_only,
        "pylint_only": pylint_only,
    }


def _categorize_ruff_finding(finding: Finding, categories: dict[str, list[Finding]]) -> None:
    """Categorize a single ruff finding by its rule code prefix."""
    if finding.rule_code.startswith("E"):
        categories["errors"].append(finding)
    elif finding.rule_code.startswith("W"):
        categories["warnings"].append(finding)
    elif finding.rule_code.startswith("F"):
        categories["flakes"].append(finding)
    elif finding.rule_code.startswith("B"):
        categories["bugbear"].append(finding)
    elif finding.rule_code.startswith("C"):
        categories["complexity"].append(finding)
    elif finding.rule_code.startswith("I"):
        categories["imports"].append(finding)
    elif finding.rule_code.startswith("UP"):
        categories["upgrade"].append(finding)
    else:
        categories["other"].append(finding)


def _categorize_pylint_finding(finding: Finding, categories: dict[str, list[Finding]]) -> None:
    """Categorize a single pylint finding by its rule code prefix."""
    if finding.rule_code.startswith("E"):
        categories["errors"].append(finding)
    elif finding.rule_code.startswith("W"):
        categories["warnings"].append(finding)
    elif finding.rule_code.startswith("C"):
        categories["convention"].append(finding)
    elif finding.rule_code.startswith("R"):
        categories["refactor"].append(finding)
    elif finding.rule_code.startswith("F"):
        categories["fatal"].append(finding)
    else:
        categories["other"].append(finding)


def categorize_findings(findings: list[Finding]) -> dict[str, list[Finding]]:
    """Categorize findings by rule type."""
    categories: dict[str, list[Finding]] = defaultdict(list)

    for finding in findings:
        if finding.tool == "ruff":
            _categorize_ruff_finding(finding, categories)
        elif finding.tool == "pylint":
            _categorize_pylint_finding(finding, categories)

    return categories


def _format_summary_statistics(comparison: dict[str, Any]) -> list[str]:
    """Format the summary statistics section of the report."""
    lines = []
    lines.append("SUMMARY STATISTICS")
    lines.append("-" * 80)
    lines.append(f"Total Ruff findings:     {comparison['ruff_total']}")
    lines.append(f"Total Pylint findings:   {comparison['pylint_total']}")
    lines.append(f"Overlapping findings:    {comparison['overlapping_count']}")
    lines.append(f"Ruff-only findings:      {comparison['ruff_only_count']}")
    lines.append(f"Pylint-only findings:    {comparison['pylint_only_count']}")
    lines.append("")
    return lines


def _format_category_section(category: str, findings: list[Finding]) -> list[str]:
    """Format a single category section with its findings."""
    lines = []
    lines.append(f"\n{category.upper()} ({len(findings)} findings):")
    for finding in findings[:20]:  # Limit to first 20 per category
        lines.append(
            f"  {finding.file_path}:{finding.line_number}:{finding.column or '?'} "
            f"[{finding.rule_code}] {finding.message}"
        )
    if len(findings) > 20:
        lines.append(f"  ... and {len(findings) - 20} more")
    return lines


def _format_findings_section(title: str, findings: list[Finding]) -> list[str]:
    """Format a complete findings section (ruff-only or pylint-only)."""
    lines = []
    lines.append(title)
    lines.append("-" * 80)
    categories = categorize_findings(findings)
    for category, category_findings in sorted(categories.items()):
        if category_findings:
            lines.extend(_format_category_section(category, category_findings))
    lines.append("")
    return lines


def _format_overlapping_section(overlapping: list[tuple[Finding, Finding]]) -> list[str]:
    """Format the overlapping findings section."""
    lines = []
    lines.append("OVERLAPPING FINDINGS (Sample)")
    lines.append("-" * 80)
    for ruff_find, pylint_find in overlapping[:10]:
        lines.append(
            f"  {ruff_find.file_path}:{ruff_find.line_number} - "
            f"Ruff: [{ruff_find.rule_code}] vs Pylint: [{pylint_find.rule_code}]"
        )
    if len(overlapping) > 10:
        lines.append(f"  ... and {len(overlapping) - 10} more overlaps")
    lines.append("")
    return lines


def generate_report(comparison: dict[str, Any], output_file: Path | None = None) -> str:
    """Generate a formatted comparison report."""
    lines = []
    lines.append("=" * 80)
    lines.append("RUFF vs PYLINT LINTING COMPARISON REPORT")
    lines.append("=" * 80)
    lines.append("")

    # Summary statistics
    lines.extend(_format_summary_statistics(comparison))

    # Ruff-only findings
    if comparison["ruff_only"]:
        lines.extend(_format_findings_section("RUFF-ONLY FINDINGS", comparison["ruff_only"]))

    # Pylint-only findings
    if comparison["pylint_only"]:
        lines.extend(_format_findings_section("PYLINT-ONLY FINDINGS", comparison["pylint_only"]))

    # Overlapping findings (sample)
    if comparison["overlapping"]:
        lines.extend(_format_overlapping_section(comparison["overlapping"]))

    lines.append("=" * 80)
    report = "\n".join(lines)

    if output_file:
        with output_file.open("w", encoding="utf-8") as f:
            f.write(report)
        print(f"Report saved to: {output_file}")

    return report


def main() -> int:
    """Main entry point for the comparison script."""
    print("Comparing ruff and pylint linting results...")
    print("")

    # Get ruff output
    print("Collecting ruff findings...")
    json_output, text_output = get_ruff_output()

    ruff_findings: list[Finding] = []
    if json_output and json_output.strip():
        try:
            json_data = json.loads(json_output)
            if isinstance(json_data, list):
                ruff_findings = parse_ruff_json_output(json_data)
            else:
                print("Warning: Unexpected JSON format from ruff")
        except json.JSONDecodeError:
            print("Warning: Failed to parse ruff JSON output, falling back to text")
            if text_output:
                ruff_findings = parse_ruff_text_output(text_output)

    if not ruff_findings and text_output:
        ruff_findings = parse_ruff_text_output(text_output)

    print(f"  Found {len(ruff_findings)} ruff findings")

    # Get pylint output
    print("Collecting pylint findings...")
    pylint_output_file = Path("pylint_output.txt")
    pylint_text = load_pylint_output(pylint_output_file)
    pylint_findings = parse_pylint_text_output(pylint_text) if pylint_text else []

    print(f"  Found {len(pylint_findings)} pylint findings")

    # Compare findings
    print("Comparing findings...")
    comparison = compare_findings(ruff_findings, pylint_findings)

    # Generate report
    report_file = Path("linting_comparison_report.txt")
    report = generate_report(comparison, output_file=report_file)

    print("")
    print(report)

    # Save detailed JSON comparison
    json_report_file = Path("linting_comparison.json")
    with json_report_file.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "summary": {
                    "ruff_total": comparison["ruff_total"],
                    "pylint_total": comparison["pylint_total"],
                    "overlapping_count": comparison["overlapping_count"],
                    "ruff_only_count": comparison["ruff_only_count"],
                    "pylint_only_count": comparison["pylint_only_count"],
                },
                "ruff_only": [
                    {
                        "file": f.file_path,
                        "line": f.line_number,
                        "column": f.column,
                        "rule": f.rule_code,
                        "message": f.message,
                    }
                    for f in comparison["ruff_only"]
                ],
                "pylint_only": [
                    {
                        "file": f.file_path,
                        "line": f.line_number,
                        "column": f.column,
                        "rule": f.rule_code,
                        "message": f.message,
                    }
                    for f in comparison["pylint_only"]
                ],
            },
            f,
            indent=2,
        )
    print(f"Detailed JSON comparison saved to: {json_report_file}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
