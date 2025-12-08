#!/usr/bin/env python3
"""
Helper script to analyze errors.log and warnings.log files from load test.

This script reads the log files, categorizes errors and warnings, and generates
a summary report of issues found during the load test.
"""

import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


def parse_log_line(line: str) -> dict[str, Any] | None:
    """
    Parse a log line into structured data.

    Expected format: YYYY-MM-DD HH:MM:SS - logger_name - LEVEL - message
    """
    # Pattern: timestamp - logger - level - message
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - ([^-]+) - (\w+) - (.+)"
    match = re.match(pattern, line.strip())

    if not match:
        return None

    timestamp_str, logger, level, message = match.groups()

    try:
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        timestamp = None

    return {
        "timestamp": timestamp,
        "logger": logger.strip(),
        "level": level.strip(),
        "message": message.strip(),
    }


def categorize_error(message: str) -> str:
    """Categorize an error message by type."""
    message_lower = message.lower()

    if "connection" in message_lower or "websocket" in message_lower:
        return "Connection Issues"
    elif "timeout" in message_lower:
        return "Timeout Errors"
    elif "database" in message_lower or "sql" in message_lower:
        return "Database Errors"
    elif "authentication" in message_lower or "auth" in message_lower:
        return "Authentication Errors"
    elif "command" in message_lower:
        return "Command Processing Errors"
    elif "rate limit" in message_lower:
        return "Rate Limiting"
    elif "validation" in message_lower:
        return "Validation Errors"
    else:
        return "Other Errors"


def categorize_warning(message: str) -> str:
    """Categorize a warning message by type."""
    message_lower = message.lower()

    if "connection" in message_lower or "websocket" in message_lower:
        return "Connection Warnings"
    elif "timeout" in message_lower:
        return "Timeout Warnings"
    elif "rate limit" in message_lower:
        return "Rate Limiting Warnings"
    elif "validation" in message_lower:
        return "Validation Warnings"
    elif "deprecated" in message_lower:
        return "Deprecation Warnings"
    else:
        return "Other Warnings"


def analyze_log_file(log_path: Path, is_error_log: bool = True) -> dict[str, Any]:
    """Analyze a log file and return statistics."""
    if not log_path.exists():
        return {
            "exists": False,
            "total_lines": 0,
            "entries": [],
            "categories": {},
            "unique_messages": set(),
        }

    entries = []
    categories: defaultdict[str, int] = defaultdict(int)
    unique_messages = set()

    with open(log_path, encoding="utf-8") as f:
        for line in f:
            parsed = parse_log_line(line)
            if not parsed:
                continue

            entries.append(parsed)
            unique_messages.add(parsed["message"])

            if is_error_log:
                category = categorize_error(parsed["message"])
            else:
                category = categorize_warning(parsed["message"])

            categories[category] += 1

    return {
        "exists": True,
        "total_lines": len(entries),
        "entries": entries,
        "categories": dict(categories),
        "unique_messages": unique_messages,
    }


def generate_report(errors_data: dict[str, Any], warnings_data: dict[str, Any]) -> str:
    """Generate a formatted report from log analysis."""
    report_lines = []
    report_lines.append("=" * 80)
    report_lines.append("LOAD TEST LOG ANALYSIS REPORT")
    report_lines.append("=" * 80)
    report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("")

    # Errors section
    report_lines.append("ERRORS LOG ANALYSIS")
    report_lines.append("-" * 80)
    if not errors_data["exists"]:
        report_lines.append("ERROR: errors.log file not found!")
    else:
        report_lines.append(f"Total Error Entries: {errors_data['total_lines']}")
        report_lines.append(f"Unique Error Messages: {len(errors_data['unique_messages'])}")
        report_lines.append("")
        report_lines.append("Errors by Category:")
        for category, count in sorted(
            errors_data["categories"].items(), key=lambda x: x[1], reverse=True
        ):
            report_lines.append(f"  {category}: {count}")

        if errors_data["entries"]:
            report_lines.append("")
            report_lines.append("Sample Errors (first 10):")
            for entry in errors_data["entries"][:10]:
                report_lines.append(
                    f"  [{entry['timestamp']}] {entry['logger']} - {entry['message'][:100]}"
                )

    report_lines.append("")
    report_lines.append("")

    # Warnings section
    report_lines.append("WARNINGS LOG ANALYSIS")
    report_lines.append("-" * 80)
    if not warnings_data["exists"]:
        report_lines.append("WARNING: warnings.log file not found!")
    else:
        report_lines.append(f"Total Warning Entries: {warnings_data['total_lines']}")
        report_lines.append(f"Unique Warning Messages: {len(warnings_data['unique_messages'])}")
        report_lines.append("")
        report_lines.append("Warnings by Category:")
        for category, count in sorted(
            warnings_data["categories"].items(), key=lambda x: x[1], reverse=True
        ):
            report_lines.append(f"  {category}: {count}")

        if warnings_data["entries"]:
            report_lines.append("")
            report_lines.append("Sample Warnings (first 10):")
            for entry in warnings_data["entries"][:10]:
                report_lines.append(
                    f"  [{entry['timestamp']}] {entry['logger']} - {entry['message'][:100]}"
                )

    report_lines.append("")
    report_lines.append("=" * 80)
    report_lines.append("END OF REPORT")
    report_lines.append("=" * 80)

    return "\n".join(report_lines)


def main():
    """Main entry point."""
    # Determine log directory (default: logs/local)
    log_base = Path("logs")
    environment = "local"
    log_dir = log_base / environment

    errors_log = log_dir / "errors.log"
    warnings_log = log_dir / "warnings.log"

    print(f"Analyzing log files in: {log_dir}")
    print(f"  Errors log: {errors_log}")
    print(f"  Warnings log: {warnings_log}")
    print()

    # Analyze both log files
    errors_data = analyze_log_file(errors_log, is_error_log=True)
    warnings_data = analyze_log_file(warnings_log, is_error_log=False)

    # Generate and print report
    report = generate_report(errors_data, warnings_data)
    print(report)

    # Also write to file
    report_file = log_dir / "load_test_analysis_report.txt"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\nReport also saved to: {report_file}")

    # Exit with error code if errors found
    if errors_data.get("total_lines", 0) > 0:
        print("\n⚠️  Errors found in log files - review required!")
        sys.exit(1)
    elif warnings_data.get("total_lines", 0) > 0:
        print("\n⚠️  Warnings found in log files - review recommended.")
        sys.exit(0)
    else:
        print("\n✅ No errors or warnings found in log files!")
        sys.exit(0)


if __name__ == "__main__":
    main()
