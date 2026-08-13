"""
Unit tests for audit_logger utilities.

Tests the AuditLogger class.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from unittest.mock import mock_open, patch

from server.utils.audit_logger import AuditLogger


def _logger() -> AuditLogger:
    with patch("server.utils.audit_logger.get_config") as mock_config:
        mock_config.return_value.logging.environment = "test"
        mock_config.return_value.logging.log_base = "logs"
        return AuditLogger()


def test_audit_logger_init():
    """Test AuditLogger initialization."""
    logger = _logger()
    assert logger.log_directory is not None


def test_audit_logger_log_command():
    """Test AuditLogger.log_command() logs command execution."""
    with patch("builtins.open", mock_open()) as mock_file:
        logger = _logger()
        logger.log_command("player1", "test_command", True, "result")
        mock_file.assert_called()


def test_audit_logger_log_permission_change():
    """Test AuditLogger.log_permission_change() logs permission change."""
    with patch("builtins.open", mock_open()) as mock_file:
        logger = _logger()
        logger.log_permission_change("admin1", "player1", "admin", "grant", True)
        mock_file.assert_called()


def test_audit_logger_log_player_action():
    """Test AuditLogger.log_player_action() logs player action."""
    with patch("builtins.open", mock_open()) as mock_file:
        logger = _logger()
        logger.log_player_action("admin1", "player1", "ban", 60, "reason", True)
        mock_file.assert_called()


def test_audit_logger_log_security_event_severity_branches():
    with patch("builtins.open", mock_open()) as mock_file:
        logger = _logger()
        logger.log_security_event("rate_limit", "p1", "too fast", severity="critical")
        logger.log_security_event("injection", None, "bad input", severity="medium")
        assert mock_file.call_count >= 2


def test_audit_logger_log_alias_expansion_cycle():
    with patch("builtins.open", mock_open()) as mock_file:
        logger = _logger()
        logger.log_alias_expansion("p1", "loop", "look", cycle_detected=True, expansion_depth=3)
        mock_file.assert_called()


def test_audit_logger_log_container_interaction():
    with patch("builtins.open", mock_open()) as mock_file:
        logger = _logger()
        logger.log_container_interaction(
            player_id="pid",
            player_name="p1",
            container_id="cid",
            event_type="container_open",
            room_id="r1",
        )
        mock_file.assert_called()


def test_audit_logger_write_entry_swallows_io_error():
    logger = _logger()
    with patch.object(logger, "_get_log_file_path", side_effect=OSError("disk full")):
        logger._write_entry({"event_type": "command", "player": "p1"})


def test_audit_logger_get_recent_entries():
    """Test AuditLogger.get_recent_entries() retrieves recent entries."""
    with patch("pathlib.Path.glob", return_value=[]):
        logger = _logger()
        entries = logger.get_recent_entries(hours=24)
        assert isinstance(entries, list)


def test_audit_logger_get_recent_entries_filters_and_bad_lines(tmp_path: Path):
    logger = _logger()
    logger.log_directory = tmp_path
    now = datetime.now(UTC).isoformat()
    log_file = tmp_path / "audit_test.jsonl"
    lines = [
        "",
        "not-json",
        json.dumps({"timestamp": now, "event_type": "command", "player": "alice", "success": False}),
        json.dumps({"timestamp": now, "event_type": "security_event", "player": "bob", "severity": "high"}),
        json.dumps({"timestamp": "2000-01-01T00:00:00+00:00", "event_type": "command", "player": "old"}),
    ]
    log_file.write_text("\n".join(lines) + "\n", encoding="utf-8")

    all_entries = logger.get_recent_entries(hours=24)
    assert len(all_entries) == 2
    alice = logger.get_recent_entries(hours=24, player_name="alice")
    assert len(alice) == 1
    cmds = logger.get_recent_entries(hours=24, event_type="command")
    assert len(cmds) == 1


def test_audit_logger_get_statistics(tmp_path: Path):
    logger = _logger()
    logger.log_directory = tmp_path
    now = datetime.now(UTC).isoformat()
    log_file = tmp_path / "audit_stats.jsonl"
    entries = [
        {"timestamp": now, "event_type": "command", "player": "alice", "success": False},
        {"timestamp": now, "event_type": "security_event", "player": "bob", "severity": "critical"},
        {"timestamp": now, "event_type": "command", "player": "alice", "success": True},
    ]
    log_file.write_text("\n".join(json.dumps(e) for e in entries) + "\n", encoding="utf-8")

    stats = logger.get_statistics(hours=24)
    assert stats["total_entries"] == 3
    assert stats["failed_commands"] == 1
    assert stats["event_types"]["command"] == 2
    assert stats["security_events_by_severity"]["critical"] == 1
    assert stats["top_players"]["alice"] == 2
