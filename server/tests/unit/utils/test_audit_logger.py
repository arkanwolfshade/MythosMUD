"""
Unit tests for audit_logger utilities.

Tests the AuditLogger class.
"""

from unittest.mock import mock_open, patch

from server.utils.audit_logger import AuditLogger


def test_audit_logger_init():
    """Test AuditLogger initialization."""
    with patch("server.utils.audit_logger.get_config") as mock_config:
        mock_config.return_value.logging.environment = "test"
        mock_config.return_value.logging.log_base = "logs"
        logger = AuditLogger()
        assert logger.log_directory is not None


def test_audit_logger_log_command():
    """Test AuditLogger.log_command() logs command execution."""
    with patch("server.utils.audit_logger.get_config") as mock_config, patch("builtins.open", mock_open()) as mock_file:
        mock_config.return_value.logging.environment = "test"
        mock_config.return_value.logging.log_base = "logs"
        logger = AuditLogger()
        logger.log_command("player1", "test_command", True, "result")
        mock_file.assert_called()


def test_audit_logger_log_permission_change():
    """Test AuditLogger.log_permission_change() logs permission change."""
    with patch("server.utils.audit_logger.get_config") as mock_config, patch("builtins.open", mock_open()) as mock_file:
        mock_config.return_value.logging.environment = "test"
        mock_config.return_value.logging.log_base = "logs"
        logger = AuditLogger()
        logger.log_permission_change("admin1", "player1", "admin", "grant", True)
        mock_file.assert_called()


def test_audit_logger_log_player_action():
    """Test AuditLogger.log_player_action() logs player action."""
    with patch("server.utils.audit_logger.get_config") as mock_config, patch("builtins.open", mock_open()) as mock_file:
        mock_config.return_value.logging.environment = "test"
        mock_config.return_value.logging.log_base = "logs"
        logger = AuditLogger()
        logger.log_player_action("admin1", "player1", "ban", 60, "reason", True)
        mock_file.assert_called()


def test_audit_logger_get_recent_entries():
    """Test AuditLogger.get_recent_entries() retrieves recent entries."""
    with patch("server.utils.audit_logger.get_config") as mock_config, patch("pathlib.Path.glob", return_value=[]):
        mock_config.return_value.logging.environment = "test"
        mock_config.return_value.logging.log_base = "logs"
        logger = AuditLogger()
        entries = logger.get_recent_entries(hours=24)
        assert isinstance(entries, list)
