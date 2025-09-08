#!/usr/bin/env python3
"""
Tests for log analysis tools.

These tests verify the functionality of the log analysis and monitoring
utilities, ensuring they can properly parse logs, detect patterns, and
generate accurate reports.
"""

import os
import sys
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import patch

# Add the scripts directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "scripts"))

from analyze_error_logs import LogAnalyzer
from error_monitoring import ErrorMonitor


class TestLogAnalyzer(unittest.TestCase):
    """Test cases for the LogAnalyzer class."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.analyzer = LogAnalyzer(self.temp_dir)

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_analyzer_initialization(self):
        """Test that the analyzer initializes correctly."""
        self.assertEqual(self.analyzer.log_dir, Path(self.temp_dir))
        self.assertEqual(len(self.analyzer.error_patterns), 0)
        self.assertEqual(len(self.analyzer.error_timeline), 0)

    def test_extract_error_pattern(self):
        """Test error pattern extraction."""
        # Test UUID removal
        message = "Connection failed for user 123e4567-e89b-12d3-a456-426614174000"
        pattern = self.analyzer._extract_error_pattern(message)
        self.assertIn("<UUID>", pattern)
        self.assertNotIn("123e4567-e89b-12d3-a456-426614174000", pattern)

        # Test ID removal
        message = "Player 12345 not found"
        pattern = self.analyzer._extract_error_pattern(message)
        self.assertIn("<ID>", pattern)
        self.assertNotIn("12345", pattern)

        # Test path removal
        message = "File not found: C:\\Users\\test\\file.txt"
        pattern = self.analyzer._extract_error_pattern(message)
        self.assertIn("<PATH>", pattern)
        self.assertNotIn("C:\\Users\\test\\file.txt", pattern)

    def test_categorize_error(self):
        """Test error categorization."""
        # Database error
        error = {"message": "Database connection failed", "logger": "db"}
        category = self.analyzer._categorize_error(error)
        self.assertEqual(category, "Database")

        # Authentication error
        error = {"message": "Invalid login credentials", "logger": "auth"}
        category = self.analyzer._categorize_error(error)
        self.assertEqual(category, "Authentication")

        # Network error
        error = {"message": "WebSocket connection timeout", "logger": "network"}
        category = self.analyzer._categorize_error(error)
        self.assertEqual(category, "Network")

        # Validation error
        error = {"message": "Invalid input validation failed", "logger": "validation"}
        category = self.analyzer._categorize_error(error)
        self.assertEqual(category, "Validation")

        # Game logic error
        error = {"message": "Player movement failed", "logger": "game"}
        category = self.analyzer._categorize_error(error)
        self.assertEqual(category, "Game Logic")

        # Other error
        error = {"message": "Unknown error occurred", "logger": "unknown"}
        category = self.analyzer._categorize_error(error)
        self.assertEqual(category, "Other")

    def test_parse_log_line_structured(self):
        """Test parsing of structured log lines."""
        line = "2025-09-06 10:05:09 - server.error_handlers - WARNING - HTTP exception handled"
        error = self.analyzer._parse_log_line(line, "test.log", 1)

        self.assertIsNotNone(error)
        self.assertEqual(error["level"], "WARNING")
        self.assertEqual(error["logger"], "server.error_handlers")
        self.assertEqual(error["message"], "HTTP exception handled")
        self.assertEqual(error["filename"], "test.log")
        self.assertEqual(error["line_number"], 1)

    def test_parse_log_line_unstructured(self):
        """Test parsing of unstructured log lines with error keywords."""
        line = "Error: Something went wrong"
        error = self.analyzer._parse_log_line(line, "test.log", 1)

        self.assertIsNotNone(error)
        self.assertEqual(error["level"], "UNKNOWN")
        self.assertEqual(error["message"], "Error: Something went wrong")

    def test_parse_log_line_no_error(self):
        """Test parsing of non-error log lines."""
        line = "2025-09-06 10:05:09 - server.main - INFO - Server started"
        error = self.analyzer._parse_log_line(line, "test.log", 1)

        self.assertIsNone(error)

    def test_generate_recommendations(self):
        """Test recommendation generation."""
        # High error volume
        analysis = {
            "total_errors": 150,
            "most_common_errors": {"Connection failed": 50},
            "error_categories": {"Database": 30, "Network": 20},
            "error_timeline": {},
        }

        recommendations = self.analyzer._generate_recommendations(analysis)
        self.assertGreater(len(recommendations), 0)
        self.assertIn("High error volume", recommendations[0])

    @patch("analyze_error_logs.Path.glob")
    def test_analyze_error_patterns_no_files(self, mock_glob):
        """Test error pattern analysis with no log files."""
        mock_glob.return_value = []

        result = self.analyzer.analyze_error_patterns(self.temp_dir)

        self.assertEqual(result["total_errors"], 0)
        self.assertEqual(result["unique_error_patterns"], 0)

    def test_generate_error_report(self):
        """Test error report generation."""
        # Mock the analyze_error_patterns method
        with patch.object(self.analyzer, "analyze_error_patterns") as mock_analyze:
            mock_analyze.return_value = {
                "total_errors": 10,
                "unique_error_patterns": 3,
                "most_common_errors": {"Test error": 5},
                "error_categories": {"Database": 5, "Network": 3},
                "error_timeline": {},
                "analysis_timestamp": "2025-09-06T10:00:00",
            }

            report = self.analyzer.generate_error_report(self.temp_dir)

            self.assertIn("MYTHOSMUD ERROR ANALYSIS REPORT", report)
            self.assertIn("Total Errors: 10", report)
            self.assertIn("Test error", report)


class TestErrorMonitor(unittest.TestCase):
    """Test cases for the ErrorMonitor class."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.monitor = ErrorMonitor(self.temp_dir, window_size=60)

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_monitor_initialization(self):
        """Test that the monitor initializes correctly."""
        self.assertEqual(self.monitor.log_dir, Path(self.temp_dir))
        self.assertEqual(self.monitor.window_size, 60)
        self.assertEqual(len(self.monitor.error_history), 0)
        self.assertEqual(len(self.monitor.rate_history), 0)

    def test_determine_severity(self):
        """Test error severity determination."""
        # Critical error
        error = {"message": "Fatal system crash", "level": "ERROR"}
        severity = self.monitor._determine_severity(error)
        self.assertEqual(severity, "critical")

        # Error level
        error = {"message": "Database connection failed", "level": "ERROR"}
        severity = self.monitor._determine_severity(error)
        self.assertEqual(severity, "error")

        # Warning level
        error = {"message": "Low memory warning", "level": "WARNING"}
        severity = self.monitor._determine_severity(error)
        self.assertEqual(severity, "warning")

        # Info level
        error = {"message": "Server started", "level": "INFO"}
        severity = self.monitor._determine_severity(error)
        self.assertEqual(severity, "info")

    def test_categorize_error(self):
        """Test error categorization in monitor."""
        # Database error
        error = {"message": "SQL query failed", "logger": "database"}
        category = self.monitor._categorize_error(error)
        self.assertEqual(category, "Database")

        # Authentication error
        error = {"message": "Invalid token", "logger": "auth"}
        category = self.monitor._categorize_error(error)
        self.assertEqual(category, "Authentication")

    def test_detect_error_trends_insufficient_data(self):
        """Test trend detection with insufficient data."""
        result = self.monitor.detect_error_trends(self.temp_dir)
        self.assertEqual(result["trend"], "insufficient_data")

    def test_detect_error_trends_increasing(self):
        """Test trend detection for increasing errors."""
        # Add some rate history (need at least 6 measurements)
        base_time = datetime.now()
        self.monitor.rate_history.extend(
            [
                {"timestamp": base_time - timedelta(minutes=12), "rate": 4.0},
                {"timestamp": base_time - timedelta(minutes=10), "rate": 5.0},
                {"timestamp": base_time - timedelta(minutes=8), "rate": 6.0},
                {"timestamp": base_time - timedelta(minutes=6), "rate": 7.0},
                {"timestamp": base_time - timedelta(minutes=4), "rate": 8.0},
                {"timestamp": base_time - timedelta(minutes=2), "rate": 9.0},
            ]
        )

        result = self.monitor.detect_error_trends(self.temp_dir)
        self.assertEqual(result["trend"], "increasing")

    def test_detect_error_trends_decreasing(self):
        """Test trend detection for decreasing errors."""
        # Add some rate history (need at least 6 measurements)
        base_time = datetime.now()
        self.monitor.rate_history.extend(
            [
                {"timestamp": base_time - timedelta(minutes=12), "rate": 12.0},
                {"timestamp": base_time - timedelta(minutes=10), "rate": 10.0},
                {"timestamp": base_time - timedelta(minutes=8), "rate": 9.0},
                {"timestamp": base_time - timedelta(minutes=6), "rate": 8.0},
                {"timestamp": base_time - timedelta(minutes=4), "rate": 7.0},
                {"timestamp": base_time - timedelta(minutes=2), "rate": 6.0},
            ]
        )

        result = self.monitor.detect_error_trends(self.temp_dir)
        self.assertEqual(result["trend"], "decreasing")

    def test_check_alerts_no_alerts(self):
        """Test alert checking with no alert conditions."""
        # Mock calculate_error_rate to return low error rate
        with patch.object(self.monitor, "calculate_error_rate") as mock_calculate:
            mock_calculate.return_value = {"error_rate": 2.0, "error_count": 5, "severity": {"error": 3, "warning": 2}}

            alerts = self.monitor.check_alerts(self.temp_dir)
            self.assertEqual(len(alerts), 0)

    def test_check_alerts_high_error_rate(self):
        """Test alert checking for high error rate."""
        # Mock calculate_error_rate to return high error rate
        with patch.object(self.monitor, "calculate_error_rate") as mock_calculate:
            mock_calculate.return_value = {"error_rate": 15.0, "error_count": 5, "severity": {"error": 3, "warning": 2}}

            alerts = self.monitor.check_alerts(self.temp_dir)
            self.assertEqual(len(alerts), 1)
            self.assertEqual(alerts[0]["type"], "high_error_rate")
            self.assertEqual(alerts[0]["severity"], "warning")

    def test_check_alerts_error_spike(self):
        """Test alert checking for error spike."""
        # Mock calculate_error_rate to return high error count
        with patch.object(self.monitor, "calculate_error_rate") as mock_calculate:
            mock_calculate.return_value = {
                "error_rate": 5.0,
                "error_count": 60,
                "severity": {"error": 30, "warning": 30},
            }

            alerts = self.monitor.check_alerts(self.temp_dir)
            self.assertEqual(len(alerts), 1)
            self.assertEqual(alerts[0]["type"], "error_spike")
            self.assertEqual(alerts[0]["severity"], "critical")

    def test_check_alerts_critical_errors(self):
        """Test alert checking for critical errors."""
        # Mock calculate_error_rate to return critical errors
        with patch.object(self.monitor, "calculate_error_rate") as mock_calculate:
            mock_calculate.return_value = {
                "error_rate": 5.0,
                "error_count": 10,
                "severity": {"critical": 6, "error": 4},
            }

            alerts = self.monitor.check_alerts(self.temp_dir)
            self.assertEqual(len(alerts), 1)
            self.assertEqual(alerts[0]["type"], "critical_errors")
            self.assertEqual(alerts[0]["severity"], "critical")

    @patch("error_monitoring.Path.glob")
    def test_calculate_error_rate_no_files(self, mock_glob):
        """Test error rate calculation with no log files."""
        mock_glob.return_value = []

        result = self.monitor.calculate_error_rate(self.temp_dir)

        self.assertEqual(result["error_rate"], 0.0)
        self.assertEqual(result["error_count"], 0)
        self.assertEqual(result["files_checked"], 0)


class TestLogAnalysisIntegration(unittest.TestCase):
    """Integration tests for log analysis tools."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.create_sample_logs()

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def create_sample_logs(self):
        """Create sample log files for testing."""
        # Create errors.log
        errors_log = Path(self.temp_dir) / "errors.log"
        with open(errors_log, "w") as f:
            f.write("2025-09-06 10:05:09 - server.database - ERROR - Database connection failed\n")
            f.write("2025-09-06 10:05:10 - server.auth - WARNING - Invalid login attempt\n")
            f.write("2025-09-06 10:05:11 - server.network - ERROR - WebSocket connection timeout\n")

        # Create server.log
        server_log = Path(self.temp_dir) / "server.log"
        with open(server_log, "w") as f:
            f.write("2025-09-06 10:05:09 - server.main - INFO - Server started\n")
            f.write("2025-09-06 10:05:10 - server.database - ERROR - Query execution failed\n")
            f.write("2025-09-06 10:05:11 - server.game - WARNING - Player movement validation failed\n")

    def test_analyzer_with_real_logs(self):
        """Test analyzer with real log files."""
        analyzer = LogAnalyzer(self.temp_dir)
        result = analyzer.analyze_error_patterns(self.temp_dir)

        self.assertGreater(result["total_errors"], 0)
        self.assertGreater(result["unique_error_patterns"], 0)
        self.assertIn("Database", result["error_categories"])
        self.assertIn("Authentication", result["error_categories"])
        self.assertIn("Network", result["error_categories"])

    def test_monitor_with_real_logs(self):
        """Test monitor with real log files."""
        monitor = ErrorMonitor(self.temp_dir, window_size=300)
        result = monitor.calculate_error_rate(self.temp_dir)

        self.assertGreaterEqual(result["error_rate"], 0.0)
        self.assertGreaterEqual(result["error_count"], 0)
        self.assertGreater(result["files_checked"], 0)

    def test_report_generation(self):
        """Test report generation with real log files."""
        analyzer = LogAnalyzer(self.temp_dir)
        report = analyzer.generate_error_report(self.temp_dir)

        self.assertIn("MYTHOSMUD ERROR ANALYSIS REPORT", report)
        self.assertIn("SUMMARY STATISTICS", report)
        self.assertIn("MOST COMMON ERRORS", report)
        self.assertIn("ERROR CATEGORIES", report)
        self.assertIn("RECOMMENDATIONS", report)


if __name__ == "__main__":
    unittest.main()
