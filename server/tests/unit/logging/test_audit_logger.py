"""
Tests for security audit logging.

As noted in the security protocols established by Dr. Armitage's
research division, all security-sensitive operations must be logged.

AI: Tests for structured audit logging of security events.
"""

import json
import tempfile

import pytest

from server.utils.audit_logger import AuditLogger


@pytest.fixture
def temp_log_dir():
    """Create a temporary directory for audit logs."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def audit_logger(temp_log_dir):
    """Create an AuditLogger instance with temporary log directory."""
    return AuditLogger(log_directory=temp_log_dir)


class TestAuditLogger:
    """Test suite for security audit logging."""

    def test_initialization(self, temp_log_dir):
        """Audit logger initializes correctly."""
        logger = AuditLogger(log_directory=temp_log_dir)

        assert logger.log_directory.exists()
        assert logger.log_directory.is_dir()

    def test_log_command_success(self, audit_logger):
        """Successfully executed security command is logged."""
        audit_logger.log_command(
            player_name="admin",
            command="teleport player1 earth_arkhamcity",
            success=True,
            result="Teleported player1",
        )

        # Read log file
        log_file = audit_logger._get_log_file_path()
        with open(log_file, encoding="utf-8") as f:
            log_entry = json.loads(f.readline())

        assert log_entry["player"] == "admin"
        assert log_entry["command"] == "teleport player1 earth_arkhamcity"
        assert log_entry["success"] is True
        assert log_entry["result"] == "Teleported player1"
        assert "ip_address" not in log_entry  # IP addresses are not logged (PII)
        assert log_entry["event_type"] == "command_execution"

    def test_log_command_failure(self, audit_logger):
        """Failed security command is logged."""
        audit_logger.log_command(
            player_name="hacker",
            command="admin_nuke_server",
            success=False,
            result="insufficient_permissions",
        )

        log_file = audit_logger._get_log_file_path()
        with open(log_file, encoding="utf-8") as f:
            log_entry = json.loads(f.readline())

        assert log_entry["success"] is False
        assert log_entry["result"] == "insufficient_permissions"

    def test_log_permission_change(self, audit_logger):
        """Permission changes are logged."""
        audit_logger.log_permission_change(
            admin_name="superadmin",
            target_player="player1",
            permission="moderator",
            action="grant",
            success=True,
            reason="Promoted to moderator",
        )

        log_file = audit_logger._get_log_file_path()
        with open(log_file, encoding="utf-8") as f:
            log_entry = json.loads(f.readline())

        assert log_entry["event_type"] == "permission_change"
        assert log_entry["admin"] == "superadmin"
        assert log_entry["target_player"] == "player1"
        assert log_entry["permission"] == "moderator"
        assert log_entry["action"] == "grant"
        assert log_entry["success"] is True

    def test_log_player_action(self, audit_logger):
        """Player actions are logged."""
        audit_logger.log_player_action(
            admin_name="admin", target_player="player1", action="ban", success=True, reason="Spamming"
        )

        log_file = audit_logger._get_log_file_path()
        with open(log_file, encoding="utf-8") as f:
            log_entry = json.loads(f.readline())

        assert log_entry["event_type"] == "player_action"
        assert log_entry["action"] == "ban"
        assert log_entry["target_player"] == "player1"

    def test_log_security_event(self, audit_logger):
        """Security events are logged with correct severity."""
        audit_logger.log_security_event(
            event_type="rate_limit_exceeded",
            player_name="spammer",
            description="Player exceeded command rate limit",
            severity="high",
            metadata={"commands_per_second": 100},
        )

        log_file = audit_logger._get_log_file_path()
        with open(log_file, encoding="utf-8") as f:
            log_entry = json.loads(f.readline())

        # Event type is always "security_event", specific type is in metadata
        assert log_entry["event_type"] == "security_event"
        assert log_entry["player"] == "spammer"
        assert log_entry["severity"] == "high"
        assert log_entry["description"] == "Player exceeded command rate limit"

    def test_log_alias_expansion(self, audit_logger):
        """Alias expansions are logged for security auditing."""
        audit_logger.log_alias_expansion(
            player_name="player1",
            alias_name="attack",
            expanded_command="cast fireball; cast lightning",
            cycle_detected=False,
            expansion_depth=2,
        )

        log_file = audit_logger._get_log_file_path()
        with open(log_file, encoding="utf-8") as f:
            log_entry = json.loads(f.readline())

        assert log_entry["event_type"] == "alias_expansion"
        assert log_entry["alias_name"] == "attack"
        assert log_entry["expansion_depth"] == 2
        assert log_entry["cycle_detected"] is False

    def test_multiple_log_entries(self, audit_logger):
        """Multiple log entries are appended correctly."""
        audit_logger.log_command("player1", "test1", success=True)
        audit_logger.log_command("player2", "test2", success=True)
        audit_logger.log_command("player3", "test3", success=False)

        log_file = audit_logger._get_log_file_path()
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()

        assert len(lines) == 3

        entry1 = json.loads(lines[0])
        entry2 = json.loads(lines[1])
        entry3 = json.loads(lines[2])

        assert entry1["player"] == "player1"
        assert entry2["player"] == "player2"
        assert entry3["player"] == "player3"

    def test_get_recent_entries(self, audit_logger):
        """Get recent entries returns recent entries."""
        for i in range(10):
            audit_logger.log_command(f"player{i}", "test", success=True)

        recent = audit_logger.get_recent_entries(hours=24)

        assert len(recent) == 10  # All entries within 24 hours
        # Entries should be returned
        assert all("player" in entry for entry in recent)

    def test_get_recent_entries_with_player_filter(self, audit_logger):
        """Get recent entries can be filtered by player."""
        audit_logger.log_command("player1", "test1", success=True)
        audit_logger.log_command("player2", "test2", success=True)
        audit_logger.log_command("player1", "test3", success=True)

        player1_entries = audit_logger.get_recent_entries(hours=24, player_name="player1")

        assert len(player1_entries) == 2
        assert all(e["player"] == "player1" for e in player1_entries)

    def test_get_recent_entries_with_event_type_filter(self, audit_logger):
        """Get recent entries can be filtered by event type."""
        audit_logger.log_command("player1", "test", success=True)
        audit_logger.log_permission_change("admin", "player1", "moderator", "grant", success=True)
        audit_logger.log_command("player2", "test", success=True)

        commands = audit_logger.get_recent_entries(hours=24, event_type="command_execution")

        assert len(commands) == 2
        assert all(e["event_type"] == "command_execution" for e in commands)

    def test_get_statistics(self, audit_logger):
        """Get statistics returns correct counts."""
        audit_logger.log_command("player1", "test", success=True)
        audit_logger.log_command("player2", "test", success=False)
        audit_logger.log_permission_change("admin", "player1", "mod", "grant", success=True)
        audit_logger.log_security_event("rate_limit_exceeded", "player3", "Rate limit hit", "warning")

        stats = audit_logger.get_statistics(hours=24)

        assert stats["total_entries"] == 4
        assert "command_execution" in stats["event_types"]
        assert "permission_change" in stats["event_types"]
        assert "security_event" in stats["event_types"]  # Not the specific type!

    def test_truncates_very_long_results(self, audit_logger):
        """Very long command results are truncated."""
        long_result = "x" * 2000

        audit_logger.log_command(player_name="player1", command="test", success=True, result=long_result)

        log_file = audit_logger._get_log_file_path()
        with open(log_file, encoding="utf-8") as f:
            log_entry = json.loads(f.readline())

        # Result is truncated to 500 chars
        assert len(log_entry["result"]) == 500

    def test_jsonl_format(self, audit_logger):
        """Log file is in JSON Lines format."""
        audit_logger.log_command("player1", "test1", success=True)
        audit_logger.log_command("player2", "test2", success=True)

        log_file = audit_logger._get_log_file_path()
        # Each line should be valid JSON
        with open(log_file, encoding="utf-8") as f:
            for line in f:
                entry = json.loads(line)  # Should not raise exception
                assert "timestamp" in entry
                assert "event_type" in entry
                assert "player" in entry

    def test_log_security_event_critical_severity(self, audit_logger):
        """Test logging security event with critical severity."""
        audit_logger.log_security_event(
            event_type="injection_attempt",
            player_name="attacker",
            description="SQL injection attempt detected",
            severity="critical",
            metadata={"payload": "' OR '1'='1"},
        )

        log_file = audit_logger._get_log_file_path()
        with open(log_file, encoding="utf-8") as f:
            log_entry = json.loads(f.readline())

        assert log_entry["severity"] == "critical"
        assert log_entry["security_event_type"] == "injection_attempt"

    def test_log_alias_expansion_with_cycle(self, audit_logger):
        """Test logging alias expansion when cycle is detected."""
        audit_logger.log_alias_expansion(
            player_name="player1",
            alias_name="bad_alias",
            expanded_command="bad_alias",
            cycle_detected=True,
            expansion_depth=10,
        )

        log_file = audit_logger._get_log_file_path()
        with open(log_file, encoding="utf-8") as f:
            log_entry = json.loads(f.readline())

        assert log_entry["cycle_detected"] is True
        assert log_entry["alias_name"] == "bad_alias"

    def test_get_recent_entries_invalid_json_line(self, audit_logger):
        """Test get_recent_entries handles invalid JSON lines gracefully."""
        # Write a valid entry
        audit_logger.log_command("player1", "test", success=True)

        # Manually write an invalid JSON line
        log_file = audit_logger._get_log_file_path()
        with open(log_file, "a", encoding="utf-8") as f:
            f.write("invalid json line\n")

        # Write another valid entry
        audit_logger.log_command("player2", "test", success=True)

        # Should still return the valid entries
        recent = audit_logger.get_recent_entries(hours=24)
        assert len(recent) == 2  # Only valid entries

    def test_get_recent_entries_with_corrupted_timestamp(self, audit_logger):
        """Test get_recent_entries handles corrupted timestamp."""
        # Manually write an entry with invalid timestamp
        log_file = audit_logger._get_log_file_path()
        corrupted_entry = '{"timestamp":"invalid","event_type":"test","player":"player1"}\n'
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(corrupted_entry)

        # Should handle gracefully
        recent = audit_logger.get_recent_entries(hours=24)
        # Entry with invalid timestamp should be skipped
        assert isinstance(recent, list)

    def test_get_recent_entries_missing_required_field(self, audit_logger):
        """Test get_recent_entries handles missing required fields."""
        # Manually write an entry without timestamp
        log_file = audit_logger._get_log_file_path()
        corrupted_entry = '{"event_type":"test","player":"player1"}\n'
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(corrupted_entry)

        # Should handle gracefully
        recent = audit_logger.get_recent_entries(hours=24)
        assert isinstance(recent, list)
