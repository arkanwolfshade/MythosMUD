"""
Unit tests for audit logger.

Tests the AuditLogger class for security-sensitive command logging.
"""

import json
import tempfile
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from server.utils.audit_logger import AuditLogger


@pytest.fixture
def temp_log_dir():
    """Create a temporary directory for audit logs."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def audit_logger(temp_log_dir):
    """Create an AuditLogger instance with temp directory."""
    return AuditLogger(log_directory=temp_log_dir)


def test_audit_logger_initialization_with_directory(temp_log_dir):
    """Test AuditLogger initialization with explicit directory."""
    logger = AuditLogger(log_directory=temp_log_dir)
    assert logger.log_directory == Path(temp_log_dir)
    assert logger.log_directory.exists()


def test_audit_logger_initialization_without_directory():
    """Test AuditLogger initialization without directory (uses config)."""
    with patch("server.utils.audit_logger.get_config") as mock_get_config:
        mock_config = MagicMock()
        mock_config.logging.environment = "test"
        mock_config.logging.log_base = "logs"
        mock_get_config.return_value = mock_config
        
        with patch("pathlib.Path.mkdir"):
            logger = AuditLogger()
            assert logger.log_directory is not None


def test_get_log_file_path(audit_logger):
    """Test _get_log_file_path returns correct path."""
    log_path = audit_logger._get_log_file_path()
    today = datetime.now(UTC).strftime("%Y-%m-%d")
    assert log_path.name == f"audit_{today}.jsonl"
    assert log_path.parent == audit_logger.log_directory


def test_log_command_success(audit_logger, temp_log_dir):
    """Test log_command writes entry successfully."""
    audit_logger.log_command(
        player_name="TestPlayer",
        command="admin teleport",
        success=True,
        result="Player teleported",
        session_id="session123",
        metadata={"room_id": "test_room"},
    )
    
    log_file = audit_logger._get_log_file_path()
    assert log_file.exists()
    
    with open(log_file, encoding="utf-8") as f:
        line = f.readline()
        entry = json.loads(line)
        
        assert entry["event_type"] == "command_execution"
        assert entry["player"] == "TestPlayer"
        assert entry["command"] == "admin teleport"
        assert entry["success"] is True
        assert entry["result"] == "Player teleported"
        assert entry["session_id"] == "session123"
        assert entry["metadata"]["room_id"] == "test_room"


def test_log_command_truncates_long_result(audit_logger, temp_log_dir):
    """Test log_command truncates long results."""
    long_result = "x" * 600
    audit_logger.log_command(
        player_name="TestPlayer",
        command="test",
        success=True,
        result=long_result,
    )
    
    log_file = audit_logger._get_log_file_path()
    with open(log_file, encoding="utf-8") as f:
        line = f.readline()
        entry = json.loads(line)
        assert len(entry["result"]) == 500


def test_log_permission_change(audit_logger, temp_log_dir):
    """Test log_permission_change writes entry."""
    audit_logger.log_permission_change(
        admin_name="Admin",
        target_player="TestPlayer",
        permission="admin",
        action="grant",
        success=True,
        reason="Promotion",
    )
    
    log_file = audit_logger._get_log_file_path()
    with open(log_file, encoding="utf-8") as f:
        line = f.readline()
        entry = json.loads(line)
        
        assert entry["event_type"] == "permission_change"
        assert entry["admin"] == "Admin"
        assert entry["target_player"] == "TestPlayer"
        assert entry["permission"] == "admin"
        assert entry["action"] == "grant"
        assert entry["success"] is True
        assert entry["reason"] == "Promotion"


def test_log_container_interaction(audit_logger, temp_log_dir):
    """Test log_container_interaction writes entry."""
    audit_logger.log_container_interaction(
        player_id="player123",
        player_name="TestPlayer",
        container_id="container123",
        event_type="container_open",
        source_type="environment",
        room_id="test_room",
        success=True,
    )
    
    log_file = audit_logger._get_log_file_path()
    with open(log_file, encoding="utf-8") as f:
        line = f.readline()
        entry = json.loads(line)
        
        assert entry["event_type"] == "container_open"
        assert entry["player_id"] == "player123"
        assert entry["player_name"] == "TestPlayer"
        assert entry["container_id"] == "container123"
        assert entry["source_type"] == "environment"
        assert entry["room_id"] == "test_room"
        assert entry["success"] is True


def test_log_player_action(audit_logger, temp_log_dir):
    """Test log_player_action writes entry."""
    audit_logger.log_player_action(
        admin_name="Admin",
        target_player="TestPlayer",
        action="mute",
        duration=60,
        reason="Spam",
        success=True,
    )
    
    log_file = audit_logger._get_log_file_path()
    with open(log_file, encoding="utf-8") as f:
        line = f.readline()
        entry = json.loads(line)
        
        assert entry["event_type"] == "player_action"
        assert entry["admin"] == "Admin"
        assert entry["target_player"] == "TestPlayer"
        assert entry["action"] == "mute"
        assert entry["duration_minutes"] == 60
        assert entry["reason"] == "Spam"
        assert entry["success"] is True


def test_log_security_event(audit_logger, temp_log_dir):
    """Test log_security_event writes entry."""
    audit_logger.log_security_event(
        event_type="rate_limit_violation",
        player_name="TestPlayer",
        description="Too many requests",
        severity="high",
        metadata={"ip": "127.0.0.1"},
    )
    
    log_file = audit_logger._get_log_file_path()
    with open(log_file, encoding="utf-8") as f:
        line = f.readline()
        entry = json.loads(line)
        
        assert entry["event_type"] == "security_event"
        assert entry["security_event_type"] == "rate_limit_violation"
        assert entry["player"] == "TestPlayer"
        assert entry["description"] == "Too many requests"
        assert entry["severity"] == "high"
        assert entry["metadata"]["ip"] == "127.0.0.1"


def test_log_alias_expansion(audit_logger, temp_log_dir):
    """Test log_alias_expansion writes entry."""
    audit_logger.log_alias_expansion(
        player_name="TestPlayer",
        alias_name="n",
        expanded_command="go north",
        cycle_detected=False,
        expansion_depth=1,
    )
    
    log_file = audit_logger._get_log_file_path()
    with open(log_file, encoding="utf-8") as f:
        line = f.readline()
        entry = json.loads(line)
        
        assert entry["event_type"] == "alias_expansion"
        assert entry["player"] == "TestPlayer"
        assert entry["alias_name"] == "n"
        assert entry["expanded_command"] == "go north"
        assert entry["cycle_detected"] is False
        assert entry["expansion_depth"] == 1


def test_get_recent_entries_no_entries(audit_logger):
    """Test get_recent_entries with no entries."""
    entries = audit_logger.get_recent_entries(hours=24)
    assert entries == []


def test_get_recent_entries_with_entries(audit_logger, temp_log_dir):
    """Test get_recent_entries retrieves recent entries."""
    # Log some entries
    audit_logger.log_command("Player1", "command1", True)
    audit_logger.log_command("Player2", "command2", False)
    
    entries = audit_logger.get_recent_entries(hours=24)
    assert len(entries) == 2
    assert entries[0]["player"] == "Player1"
    assert entries[1]["player"] == "Player2"


def test_get_recent_entries_with_filter(audit_logger, temp_log_dir):
    """Test get_recent_entries with event type filter."""
    audit_logger.log_command("Player1", "command1", True)
    audit_logger.log_permission_change("Admin", "Player1", "admin", "grant", True)
    
    entries = audit_logger.get_recent_entries(hours=24, event_type="permission_change")
    assert len(entries) == 1
    assert entries[0]["event_type"] == "permission_change"


def test_get_recent_entries_with_player_filter(audit_logger, temp_log_dir):
    """Test get_recent_entries with player name filter."""
    audit_logger.log_command("Player1", "command1", True)
    audit_logger.log_command("Player2", "command2", True)
    
    entries = audit_logger.get_recent_entries(hours=24, player_name="Player1")
    assert len(entries) == 1
    assert entries[0]["player"] == "Player1"


def test_get_statistics(audit_logger, temp_log_dir):
    """Test get_statistics returns correct statistics."""
    audit_logger.log_command("Player1", "command1", True)
    audit_logger.log_command("Player2", "command2", False)
    audit_logger.log_security_event("rate_limit", "Player1", "Too many requests", "high")
    
    stats = audit_logger.get_statistics(hours=24)
    
    assert stats["total_entries"] == 3
    assert stats["event_types"]["command_execution"] == 2
    assert stats["event_types"]["security_event"] == 1
    assert stats["failed_commands"] == 1
    assert "Player1" in stats["top_players"]
    assert "Player2" in stats["top_players"]
