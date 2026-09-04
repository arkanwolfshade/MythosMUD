#!/usr/bin/env python3
"""
Log Analysis Tools for MythosMUD

This script provides comprehensive analysis of error logs, including pattern detection,
trend analysis, and report generation. As noted in the Pnakotic Manuscripts, proper
analysis of anomalous events is crucial for understanding the deeper patterns that
govern our digital realm.

Author: Professor of Occult Studies, Miskatonic University
"""

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

# Add the server directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "server"))


class LogAnalyzer:
    """
    Comprehensive log analysis tool for MythosMUD error logs.

    This analyzer can process structured and unstructured log files,
    detect patterns, and generate detailed reports on error trends.
    """

    def __init__(self, log_dir: str):
        """Initialize the analyzer with a log directory."""
        self.log_dir = Path(log_dir)
        self.error_patterns = defaultdict(int)
        self.error_timeline = defaultdict(list)
        self.error_contexts = defaultdict(list)
        self.error_categories = defaultdict(int)

    def analyze_error_patterns(self, log_dir: str) -> dict[str, Any]:
        """
        Analyze error patterns in log files.

        Returns a dictionary containing pattern analysis results.
        """
        print("🔍 Analyzing error patterns...")

        error_files = self._find_error_logs(log_dir)
        total_errors = 0
        unique_errors = set()

        for log_file in error_files:
            print(f"  📄 Processing {log_file.name}...")
            errors = self._parse_log_file(log_file)
            total_errors += len(errors)

            for error in errors:
                # Extract error pattern (simplified message)
                pattern = self._extract_error_pattern(error["message"])
                self.error_patterns[pattern] += 1
                unique_errors.add(pattern)

                # Track timeline
                timestamp = error.get("timestamp")
                if timestamp:
                    date_key = timestamp.date().isoformat()
                    self.error_timeline[date_key].append(error)

                # Categorize error
                category = self._categorize_error(error)
                self.error_categories[category] += 1

                # Store context if available
                if "context" in error:
                    self.error_contexts[pattern].append(error["context"])

        return {
            "total_errors": total_errors,
            "unique_error_patterns": len(unique_errors),
            "most_common_errors": dict(Counter(self.error_patterns).most_common(10)),
            "error_categories": dict(self.error_categories),
            "error_timeline": dict(self.error_timeline),
            "analysis_timestamp": datetime.now().isoformat(),
        }

    def generate_error_report(self, log_dir: str) -> str:
        """
        Generate a comprehensive error report.

        Returns a formatted report string.
        """
        print("📊 Generating error report...")

        analysis = self.analyze_error_patterns(log_dir)

        report = []
        report.append("=" * 80)
        report.append("MYTHOSMUD ERROR ANALYSIS REPORT")
        report.append("=" * 80)
        report.append(f"Generated: {analysis['analysis_timestamp']}")
        report.append(f"Log Directory: {log_dir}")
        report.append("")

        # Summary statistics
        report.append("📈 SUMMARY STATISTICS")
        report.append("-" * 40)
        report.append(f"Total Errors: {analysis['total_errors']}")
        report.append(f"Unique Error Patterns: {analysis['unique_error_patterns']}")
        report.append("")

        # Most common errors
        report.append("🔥 MOST COMMON ERRORS")
        report.append("-" * 40)
        for pattern, count in analysis["most_common_errors"].items():
            percentage = (count / analysis["total_errors"]) * 100
            report.append(f"{count:4d} ({percentage:5.1f}%) - {pattern}")
        report.append("")

        # Error categories
        report.append("📂 ERROR CATEGORIES")
        report.append("-" * 40)
        for category, count in analysis["error_categories"].items():
            percentage = (count / analysis["total_errors"]) * 100
            report.append(f"{count:4d} ({percentage:5.1f}%) - {category}")
        report.append("")

        # Timeline analysis
        report.append("📅 ERROR TIMELINE")
        report.append("-" * 40)
        timeline = analysis["error_timeline"]
        if timeline:
            sorted_dates = sorted(timeline.keys())
            for date in sorted_dates[-7:]:  # Last 7 days
                count = len(timeline[date])
                report.append(f"{date}: {count} errors")
        report.append("")

        # Recommendations
        report.append("💡 RECOMMENDATIONS")
        report.append("-" * 40)
        recommendations = self._generate_recommendations(analysis)
        for i, rec in enumerate(recommendations, 1):
            report.append(f"{i}. {rec}")
        report.append("")

        report.append("=" * 80)
        report.append("End of Report")
        report.append("=" * 80)

        return "\n".join(report)

    def detect_error_trends(self, log_dir: str) -> dict[str, Any]:
        """
        Detect error trends over time.

        Returns trend analysis results.
        """
        print("📈 Detecting error trends...")

        analysis = self.analyze_error_patterns(log_dir)
        timeline = analysis["error_timeline"]

        if not timeline:
            return {"trend": "no_data", "message": "No timeline data available"}

        # Calculate daily error counts
        daily_counts = {}
        for date, errors in timeline.items():
            daily_counts[date] = len(errors)

        # Calculate trend
        sorted_dates = sorted(daily_counts.keys())
        if len(sorted_dates) < 2:
            return {"trend": "insufficient_data", "message": "Need at least 2 days of data"}

        recent_avg = sum(daily_counts[date] for date in sorted_dates[-3:]) / 3
        older_avg = sum(daily_counts[date] for date in sorted_dates[:-3]) / max(1, len(sorted_dates) - 3)

        if recent_avg > older_avg * 1.2:
            trend = "increasing"
        elif recent_avg < older_avg * 0.8:
            trend = "decreasing"
        else:
            trend = "stable"

        return {
            "trend": trend,
            "recent_average": recent_avg,
            "older_average": older_avg,
            "daily_counts": daily_counts,
            "trend_strength": abs(recent_avg - older_avg) / older_avg if older_avg > 0 else 0,
        }

    def _find_error_logs(self, log_dir: str) -> list[Path]:
        """Find all error log files in the directory."""
        log_path = Path(log_dir)
        error_files = []

        # Look for common error log patterns
        patterns = ["**/errors.log", "**/error.log", "**/*error*.log", "**/server.log", "**/console.log"]

        for pattern in patterns:
            error_files.extend(log_path.glob(pattern))

        return list(set(error_files))  # Remove duplicates

    def _parse_log_file(self, log_file: Path) -> list[dict[str, Any]]:
        """Parse a log file and extract error information."""
        errors = []

        try:
            with open(log_file, encoding="utf-8") as f:
                for line_num, line in enumerate(f, 1):
                    error = self._parse_log_line(line.strip(), log_file.name, line_num)
                    if error:
                        errors.append(error)
        except Exception as e:
            print(f"    ⚠️  Warning: Could not parse {log_file}: {e}")

        return errors

    def _parse_log_line(self, line: str, filename: str, line_num: int) -> dict[str, Any] | None:
        """Parse a single log line and extract error information."""
        if not line:
            return None

        # Try to parse structured log format first
        structured_match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - ([^-]+) - (\w+) - (.+)", line)

        if structured_match:
            timestamp_str, logger, level, message = structured_match.groups()
            try:
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                timestamp = None

            # Only process ERROR and WARNING levels
            if level in ["ERROR", "WARNING"]:
                return {
                    "timestamp": timestamp,
                    "logger": logger,
                    "level": level,
                    "message": message,
                    "filename": filename,
                    "line_number": line_num,
                    "raw_line": line,
                }

        # Fallback: look for error keywords in unstructured logs
        error_keywords = ["error", "exception", "failed", "critical", "fatal"]
        if any(keyword in line.lower() for keyword in error_keywords):
            return {
                "timestamp": None,
                "logger": "unknown",
                "level": "UNKNOWN",
                "message": line,
                "filename": filename,
                "line_number": line_num,
                "raw_line": line,
            }

        return None

    def _extract_error_pattern(self, message: str) -> str:
        """Extract a simplified error pattern from a message."""
        # Remove timestamps, IDs, and other variable data
        pattern = message

        # Remove UUIDs
        pattern = re.sub(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", "<UUID>", pattern)

        # Remove numbers that might be IDs
        pattern = re.sub(r"\b\d{4,}\b", "<ID>", pattern)

        # Remove file paths
        pattern = re.sub(r"[A-Za-z]:\\[^\\]+\\[^\\]+", "<PATH>", pattern)
        pattern = re.sub(r"/[^/]+/[^/]+", "<PATH>", pattern)

        # Remove IP addresses
        pattern = re.sub(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "<IP>", pattern)

        return pattern

    def _categorize_error(self, error: dict[str, Any]) -> str:
        """Categorize an error based on its content."""
        message = error["message"].lower()
        logger = error.get("logger", "").lower()

        # Network errors (check first to avoid false positives)
        if any(keyword in message for keyword in ["websocket", "network", "timeout"]):
            return "Network"

        # Database errors (more specific keywords)
        if (
            any(keyword in message for keyword in ["database", "sql", "query"])
            or "connection" in message
            and "database" in logger
        ):
            return "Database"

        # Authentication errors
        if any(keyword in message for keyword in ["auth", "login", "password", "token", "unauthorized"]):
            return "Authentication"

        # Validation errors
        if any(keyword in message for keyword in ["validation", "invalid", "required", "missing"]):
            return "Validation"

        # File system errors
        if any(keyword in message for keyword in ["file", "directory", "path", "permission"]):
            return "File System"

        # Game logic errors
        if any(keyword in message for keyword in ["player", "room", "command", "game"]):
            return "Game Logic"

        # System errors
        if any(keyword in message for keyword in ["system", "memory", "cpu", "resource"]):
            return "System"

        return "Other"

    def _generate_recommendations(self, analysis: dict[str, Any]) -> list[str]:
        """Generate recommendations based on analysis results."""
        recommendations = []

        # Check for high error rates
        total_errors = analysis["total_errors"]
        if total_errors > 100:
            recommendations.append("High error volume detected. Consider implementing additional error handling.")

        # Check for common error patterns
        most_common = analysis["most_common_errors"]
        if most_common:
            top_error = list(most_common.keys())[0]
            top_count = most_common[top_error]
            if top_count > total_errors * 0.3:  # More than 30% of errors
                recommendations.append(
                    f"Most common error pattern: '{top_error}' ({top_count} occurrences). Consider addressing this specific issue."
                )

        # Check error categories
        categories = analysis["error_categories"]
        if "Database" in categories and categories["Database"] > total_errors * 0.2:
            recommendations.append(
                "High database error rate. Review database connection handling and query optimization."
            )

        if "Authentication" in categories and categories["Authentication"] > total_errors * 0.1:
            recommendations.append("Authentication errors detected. Review security measures and user validation.")

        if "Network" in categories and categories["Network"] > total_errors * 0.15:
            recommendations.append("Network errors detected. Review connection handling and timeout configurations.")

        # Check timeline trends
        timeline = analysis["error_timeline"]
        if len(timeline) > 1:
            recent_dates = sorted(timeline.keys())[-3:]
            recent_errors = sum(len(timeline[date]) for date in recent_dates)
            if recent_errors > total_errors * 0.5:
                recommendations.append("Recent error spike detected. Monitor system health closely.")

        if not recommendations:
            recommendations.append("No specific issues detected. Continue monitoring error logs.")

        return recommendations


def main():
    """Main entry point for the log analysis script."""
    parser = argparse.ArgumentParser(
        description="Analyze MythosMUD error logs and generate reports",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python analyze_error_logs.py --log-dir logs/development --report
  python analyze_error_logs.py --log-dir logs/development --patterns
  python analyze_error_logs.py --log-dir logs/development --trends
  python analyze_error_logs.py --log-dir logs/development --all --output report.txt
        """,
    )

    parser.add_argument(
        "--log-dir", default="logs/development", help="Directory containing log files (default: logs/development)"
    )

    parser.add_argument("--report", action="store_true", help="Generate comprehensive error report")

    parser.add_argument("--patterns", action="store_true", help="Analyze error patterns")

    parser.add_argument("--trends", action="store_true", help="Detect error trends")

    parser.add_argument("--all", action="store_true", help="Run all analyses")

    parser.add_argument("--output", help="Output file for results (default: stdout)")

    args = parser.parse_args()

    # Validate log directory
    if not Path(args.log_dir).exists():
        print(f"❌ Error: Log directory '{args.log_dir}' does not exist")
        sys.exit(1)

    analyzer = LogAnalyzer(args.log_dir)
    results = []

    try:
        if args.all or args.patterns:
            print("🔍 Analyzing error patterns...")
            patterns = analyzer.analyze_error_patterns(args.log_dir)
            results.append(("Pattern Analysis", patterns))

        if args.all or args.trends:
            print("📈 Detecting error trends...")
            trends = analyzer.detect_error_trends(args.log_dir)
            results.append(("Trend Analysis", trends))

        if args.all or args.report:
            print("📊 Generating error report...")
            report = analyzer.generate_error_report(args.log_dir)
            results.append(("Error Report", report))

        # Output results
        output_content = []
        for title, content in results:
            output_content.append(f"\n{'=' * 60}")
            output_content.append(f"{title.upper()}")
            output_content.append(f"{'=' * 60}")

            if isinstance(content, str):
                output_content.append(content)
            else:
                output_content.append(json.dumps(content, indent=2, default=str))

        final_output = "\n".join(output_content)

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(final_output)
            print(f"✅ Results written to {args.output}")
        else:
            print(final_output)

    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
