#!/usr/bin/env python3
"""
Error Monitoring Utilities for MythosMUD

This script provides real-time error monitoring capabilities, including error rate
calculation, categorization, and trend analysis. As documented in the restricted
archives, continuous monitoring of anomalous events is essential for maintaining
the delicate balance between order and chaos in our digital realm.

Author: Professor of Occult Studies, Miskatonic University
"""

import argparse
import json
import os
import sys
import time
from collections import defaultdict, deque
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

# Add the server directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "server"))


class ErrorMonitor:
    """
    Real-time error monitoring system for MythosMUD.

    This monitor can track error rates, detect spikes, and provide
    real-time alerts for critical error conditions.
    """

    def __init__(self, log_dir: str, window_size: int = 300):
        """
        Initialize the error monitor.

        Args:
            log_dir: Directory containing log files
            window_size: Time window in seconds for rate calculations
        """
        self.log_dir = Path(log_dir)
        self.window_size = window_size
        self.error_history = deque(maxlen=1000)  # Keep last 1000 errors
        self.rate_history = deque(maxlen=100)  # Keep last 100 rate measurements
        self.last_check_time = None
        self.alert_thresholds = {
            "error_rate": 10,  # errors per minute
            "error_spike": 50,  # errors in 5 minutes
            "critical_errors": 5,  # critical errors in 5 minutes
        }

    def calculate_error_rate(self, log_dir: str) -> dict[str, Any]:
        """
        Calculate current error rate from log files.

        Returns error rate statistics.
        """
        current_time = datetime.now()
        window_start = current_time - timedelta(seconds=self.window_size)

        # Find recent error log files
        error_files = self._find_recent_error_logs(log_dir, window_start)

        error_count = 0
        error_categories = defaultdict(int)
        error_severity = defaultdict(int)

        for log_file in error_files:
            errors = self._parse_recent_errors(log_file, window_start)
            error_count += len(errors)

            for error in errors:
                # Categorize error
                category = self._categorize_error(error)
                error_categories[category] += 1

                # Determine severity
                severity = self._determine_severity(error)
                error_severity[severity] += 1

        # Calculate rate (errors per minute)
        rate = (error_count / self.window_size) * 60 if self.window_size > 0 else 0

        # Store in history
        self.rate_history.append(
            {
                "timestamp": current_time,
                "rate": rate,
                "count": error_count,
                "categories": dict(error_categories),
                "severity": dict(error_severity),
            }
        )

        return {
            "timestamp": current_time.isoformat(),
            "error_rate": rate,
            "error_count": error_count,
            "window_size_seconds": self.window_size,
            "categories": dict(error_categories),
            "severity": dict(error_severity),
            "files_checked": len(error_files),
        }

    def detect_error_trends(self, log_dir: str) -> dict[str, Any]:
        """
        Detect error trends over time.

        Returns trend analysis results.
        """
        if len(self.rate_history) < 6:  # Need at least 6 measurements for reliable trend
            return {"trend": "insufficient_data", "message": "Need at least 6 rate measurements for trend analysis"}

        # Calculate trend from recent measurements
        recent_rates = [entry["rate"] for entry in list(self.rate_history)[-3:]]
        older_rates = [entry["rate"] for entry in list(self.rate_history)[:-3]]

        if len(older_rates) < 3:
            return {"trend": "insufficient_data", "message": "Need more historical data for comparison"}

        recent_avg = sum(recent_rates) / len(recent_rates)
        older_avg = sum(older_rates) / len(older_rates)

        if recent_avg > older_avg * 1.5:
            trend = "increasing"
            trend_strength = "strong"
        elif recent_avg > older_avg * 1.2:
            trend = "increasing"
            trend_strength = "moderate"
        elif recent_avg < older_avg * 0.5:
            trend = "decreasing"
            trend_strength = "strong"
        elif recent_avg < older_avg * 0.8:
            trend = "decreasing"
            trend_strength = "moderate"
        else:
            trend = "stable"
            trend_strength = "none"

        return {
            "trend": trend,
            "trend_strength": trend_strength,
            "recent_average": recent_avg,
            "older_average": older_avg,
            "measurements_analyzed": len(self.rate_history),
        }

    def check_alerts(self, log_dir: str) -> list[dict[str, Any]]:
        """
        Check for alert conditions.

        Returns list of active alerts.
        """
        alerts = []
        current_time = datetime.now()

        # Calculate current error rate
        rate_data = self.calculate_error_rate(log_dir)
        current_rate = rate_data["error_rate"]

        # Check error rate threshold
        if current_rate > self.alert_thresholds["error_rate"]:
            alerts.append(
                {
                    "type": "high_error_rate",
                    "severity": "warning",
                    "message": f"High error rate detected: {current_rate:.1f} errors/minute",
                    "threshold": self.alert_thresholds["error_rate"],
                    "current_value": current_rate,
                    "timestamp": current_time.isoformat(),
                }
            )

        # Check for error spike (high count in recent window)
        if rate_data["error_count"] > self.alert_thresholds["error_spike"]:
            alerts.append(
                {
                    "type": "error_spike",
                    "severity": "critical",
                    "message": f"Error spike detected: {rate_data['error_count']} errors in {self.window_size}s",
                    "threshold": self.alert_thresholds["error_spike"],
                    "current_value": rate_data["error_count"],
                    "timestamp": current_time.isoformat(),
                }
            )

        # Check for critical errors
        critical_count = rate_data["severity"].get("critical", 0)
        if critical_count > self.alert_thresholds["critical_errors"]:
            alerts.append(
                {
                    "type": "critical_errors",
                    "severity": "critical",
                    "message": f"Multiple critical errors: {critical_count} in {self.window_size}s",
                    "threshold": self.alert_thresholds["critical_errors"],
                    "current_value": critical_count,
                    "timestamp": current_time.isoformat(),
                }
            )

        # Check trend alerts
        trend_data = self.detect_error_trends(log_dir)
        if trend_data["trend"] == "increasing" and trend_data["trend_strength"] == "strong":
            alerts.append(
                {
                    "type": "increasing_trend",
                    "severity": "warning",
                    "message": "Strong increasing error trend detected",
                    "trend_data": trend_data,
                    "timestamp": current_time.isoformat(),
                }
            )

        return alerts

    def monitor_continuously(self, log_dir: str, interval: int = 60, duration: int = 3600):
        """
        Monitor errors continuously for a specified duration.

        Args:
            log_dir: Directory containing log files
            interval: Check interval in seconds
            duration: Total monitoring duration in seconds
        """
        print("🔍 Starting continuous error monitoring...")
        print(f"   Log directory: {log_dir}")
        print(f"   Check interval: {interval}s")
        print(f"   Duration: {duration}s")
        print(f"   Alert thresholds: {self.alert_thresholds}")
        print("-" * 60)

        start_time = time.time()
        check_count = 0

        try:
            while time.time() - start_time < duration:
                check_count += 1
                current_time = datetime.now()

                print(f"[{current_time.strftime('%H:%M:%S')}] Check #{check_count}")

                # Calculate error rate
                rate_data = self.calculate_error_rate(log_dir)
                print(f"   Error rate: {rate_data['error_rate']:.1f} errors/minute")
                print(f"   Error count: {rate_data['error_count']} in {self.window_size}s")

                # Check for alerts
                alerts = self.check_alerts(log_dir)
                if alerts:
                    print(f"   🚨 {len(alerts)} alert(s) detected:")
                    for alert in alerts:
                        severity_icon = "🔴" if alert["severity"] == "critical" else "🟡"
                        print(f"      {severity_icon} {alert['message']}")
                else:
                    print("   ✅ No alerts")

                # Show trend if available
                if len(self.rate_history) > 1:
                    trend_data = self.detect_error_trends(log_dir)
                    if trend_data["trend"] != "insufficient_data":
                        trend_icon = (
                            "📈"
                            if trend_data["trend"] == "increasing"
                            else "📉"
                            if trend_data["trend"] == "decreasing"
                            else "➡️"
                        )
                        print(f"   {trend_icon} Trend: {trend_data['trend']} ({trend_data['trend_strength']})")

                print()

                # Wait for next check
                time.sleep(interval)

        except KeyboardInterrupt:
            print("\n⏹️  Monitoring stopped by user")

        print(f"📊 Monitoring completed after {check_count} checks")

        # Generate summary
        if self.rate_history:
            rates = [entry["rate"] for entry in self.rate_history]
            print(f"   Average error rate: {sum(rates) / len(rates):.1f} errors/minute")
            print(f"   Peak error rate: {max(rates):.1f} errors/minute")
            print(f"   Minimum error rate: {min(rates):.1f} errors/minute")

    def _find_recent_error_logs(self, log_dir: str, since: datetime) -> list[Path]:
        """Find error log files that have been modified since the given time."""
        log_path = Path(log_dir)
        recent_files = []

        # Look for common error log patterns
        patterns = ["**/errors.log", "**/error.log", "**/*error*.log", "**/server.log", "**/console.log"]

        for pattern in patterns:
            for log_file in log_path.glob(pattern):
                try:
                    # Check if file was modified since the given time
                    if log_file.stat().st_mtime >= since.timestamp():
                        recent_files.append(log_file)
                except OSError:
                    # File might not exist or be accessible
                    continue

        return recent_files

    def _parse_recent_errors(self, log_file: Path, since: datetime) -> list[dict[str, Any]]:
        """Parse recent errors from a log file."""
        errors = []

        try:
            with open(log_file, encoding="utf-8") as f:
                for line_num, line in enumerate(f, 1):
                    error = self._parse_log_line(line.strip(), log_file.name, line_num)
                    if error and error.get("timestamp") and error["timestamp"] >= since:
                        errors.append(error)
        except Exception:
            # Silently skip files that can't be read
            pass

        return errors

    def _parse_log_line(self, line: str, filename: str, line_num: int) -> dict[str, Any] | None:
        """Parse a single log line and extract error information."""
        if not line:
            return None

        # Try to parse structured log format
        import re

        structured_match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - ([^-]+) - (\w+) - (.+)", line)

        if structured_match:
            timestamp_str, logger, level, message = structured_match.groups()
            try:
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                return None

            # Only process ERROR and WARNING levels
            if level in ["ERROR", "WARNING"]:
                return {
                    "timestamp": timestamp,
                    "logger": logger,
                    "level": level,
                    "message": message,
                    "filename": filename,
                    "line_number": line_num,
                }

        return None

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

    def _determine_severity(self, error: dict[str, Any]) -> str:
        """Determine the severity of an error."""
        message = error["message"].lower()
        level = error.get("level", "").upper()

        # Critical keywords
        if any(keyword in message for keyword in ["fatal", "critical", "crash", "abort"]):
            return "critical"

        # Error level
        if level == "ERROR":
            return "error"
        elif level == "WARNING":
            return "warning"

        # Default to info
        return "info"


def main():
    """Main entry point for the error monitoring script."""
    parser = argparse.ArgumentParser(
        description="Monitor MythosMUD error logs in real-time",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python error_monitoring.py --log-dir logs/development --rate
  python error_monitoring.py --log-dir logs/development --trends
  python error_monitoring.py --log-dir logs/development --alerts
  python error_monitoring.py --log-dir logs/development --monitor --interval 30 --duration 1800
        """,
    )

    parser.add_argument(
        "--log-dir", default="logs/development", help="Directory containing log files (default: logs/development)"
    )

    parser.add_argument(
        "--window-size", type=int, default=300, help="Time window in seconds for rate calculations (default: 300)"
    )

    parser.add_argument("--rate", action="store_true", help="Calculate current error rate")

    parser.add_argument("--trends", action="store_true", help="Detect error trends")

    parser.add_argument("--alerts", action="store_true", help="Check for alert conditions")

    parser.add_argument("--monitor", action="store_true", help="Monitor continuously")

    parser.add_argument(
        "--interval", type=int, default=60, help="Check interval in seconds for monitoring (default: 60)"
    )

    parser.add_argument("--duration", type=int, default=3600, help="Monitoring duration in seconds (default: 3600)")

    parser.add_argument("--output", help="Output file for results (default: stdout)")

    args = parser.parse_args()

    # Validate log directory
    if not Path(args.log_dir).exists():
        print(f"❌ Error: Log directory '{args.log_dir}' does not exist")
        sys.exit(1)

    monitor = ErrorMonitor(args.log_dir, args.window_size)
    results = []

    try:
        if args.rate:
            print("📊 Calculating error rate...")
            rate_data = monitor.calculate_error_rate(args.log_dir)
            results.append(("Error Rate", rate_data))

        if args.trends:
            print("📈 Detecting error trends...")
            trends = monitor.detect_error_trends(args.log_dir)
            results.append(("Error Trends", trends))

        if args.alerts:
            print("🚨 Checking for alerts...")
            alerts = monitor.check_alerts(args.log_dir)
            results.append(("Alerts", alerts))

        if args.monitor:
            monitor.monitor_continuously(args.log_dir, args.interval, args.duration)
            return  # Don't output results for continuous monitoring

        # Output results
        if results:
            output_content = []
            for title, content in results:
                output_content.append(f"\n{'=' * 60}")
                output_content.append(f"{title.upper()}")
                output_content.append(f"{'=' * 60}")
                output_content.append(json.dumps(content, indent=2, default=str))

            final_output = "\n".join(output_content)

            if args.output:
                with open(args.output, "w", encoding="utf-8") as f:
                    f.write(final_output)
                print(f"✅ Results written to {args.output}")
            else:
                print(final_output)
        else:
            print("ℹ️  No analysis requested. Use --rate, --trends, --alerts, or --monitor")

    except Exception as e:
        print(f"❌ Error during monitoring: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
