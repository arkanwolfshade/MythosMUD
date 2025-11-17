"""
Security tests for SQL injection prevention.

These tests verify that all database operations use parameterized queries
and are protected against SQL injection attacks.
"""

import pytest

from server.exceptions import DatabaseError, ValidationError
from server.models.player import Player
from server.persistence import PersistenceLayer


class TestSQLInjectionPrevention:
    """Test SQL injection prevention in database operations."""

    def test_update_player_stat_field_whitelist_validation(self, persistence: PersistenceLayer):
        """Test that update_player_stat_field validates field_name against whitelist."""
        # Create a test player
        player = Player(
            player_id="test-player-123",
            user_id="test-user-123",
            name="TestPlayer",
        )
        persistence.save_player(player)

        # Test valid field names
        valid_fields = [
            "current_health",
            "experience_points",
            "sanity",
            "occult_knowledge",
            "fear",
            "corruption",
            "cult_affiliation",
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
        ]

        for field_name in valid_fields:
            # Should not raise ValueError
            persistence.update_player_stat_field(str(player.player_id), field_name, 10, "test")

        # Test invalid field names (SQL injection attempts)
        invalid_fields = [
            "'; DROP TABLE players; --",
            "1=1",
            "admin' OR '1'='1",
            "../etc/passwd",
            "'; DELETE FROM players; --",
            "field_name; SELECT * FROM users; --",
            "field_name' UNION SELECT * FROM users; --",
        ]

        for field_name in invalid_fields:
            with pytest.raises(ValueError, match="Invalid stat field name"):
                persistence.update_player_stat_field(str(player.player_id), field_name, 10, "test")

    def test_update_player_stat_field_parameterized_query(self, persistence: PersistenceLayer):
        """Test that update_player_stat_field uses parameterized queries."""
        # Create a test player
        player = Player(
            player_id="test-player-456",
            user_id="test-user-456",
            name="TestPlayer2",
        )
        persistence.save_player(player)

        # Attempt SQL injection via delta parameter
        # The delta is parameterized, so this should be safe
        # (field_name is already validated by whitelist)
        malicious_delta = "10; DROP TABLE players; --"

        # This should fail with a type error, not execute SQL
        with pytest.raises((TypeError, ValueError)):
            persistence.update_player_stat_field(
                str(player.player_id), "current_health", malicious_delta, "test"  # type: ignore[arg-type]
            )

    def test_get_player_by_name_parameterized(self, persistence: PersistenceLayer):
        """Test that get_player_by_name uses parameterized queries."""
        # Create a test player
        player = Player(
            player_id="test-player-789",
            user_id="test-user-789",
            name="SafePlayer",
        )
        persistence.save_player(player)

        # Attempt SQL injection via name parameter
        malicious_names = [
            "SafePlayer'; DROP TABLE players; --",
            "SafePlayer' OR '1'='1",
            "SafePlayer' UNION SELECT * FROM users; --",
        ]

        for malicious_name in malicious_names:
            # Should return None (player not found), not execute malicious SQL
            result = persistence.get_player_by_name(malicious_name)
            assert result is None, f"SQL injection attempt should not find player: {malicious_name}"

        # Valid name should still work
        result = persistence.get_player_by_name("SafePlayer")
        assert result is not None
        assert result.name == "SafePlayer"

    def test_get_player_by_id_parameterized(self, persistence: PersistenceLayer):
        """Test that get_player uses parameterized queries."""
        # Create a test player
        player = Player(
            player_id="test-player-abc",
            user_id="test-user-abc",
            name="TestPlayer3",
        )
        persistence.save_player(player)

        # Attempt SQL injection via player_id parameter
        malicious_ids = [
            "test-player-abc'; DROP TABLE players; --",
            "test-player-abc' OR '1'='1",
            "test-player-abc' UNION SELECT * FROM users; --",
        ]

        for malicious_id in malicious_ids:
            # Should return None (player not found), not execute malicious SQL
            result = persistence.get_player(malicious_id)
            assert result is None, f"SQL injection attempt should not find player: {malicious_id}"

        # Valid ID should still work
        result = persistence.get_player("test-player-abc")
        assert result is not None
        assert result.player_id == "test-player-abc"

    def test_f_string_sql_uses_constants_only(self):
        """Test that f-string SQL construction only uses compile-time constants."""
        # This test verifies that PLAYER_COLUMNS and PROFESSION_COLUMNS
        # are compile-time constants, not user input

        from server.async_persistence import PLAYER_COLUMNS, PROFESSION_COLUMNS

        # Verify these are strings (compile-time constants)
        assert isinstance(PLAYER_COLUMNS, str)
        assert isinstance(PROFESSION_COLUMNS, str)

        # Verify they don't contain user input patterns
        assert "%" not in PLAYER_COLUMNS
        assert "$" not in PLAYER_COLUMNS
        assert ";" not in PLAYER_COLUMNS
        assert "--" not in PLAYER_COLUMNS

        # Verify they contain expected column names
        assert "player_id" in PLAYER_COLUMNS
        assert "name" in PLAYER_COLUMNS
        assert "stats" in PLAYER_COLUMNS

    def test_player_name_validation(self, persistence: PersistenceLayer):
        """Test that player names are validated to prevent injection."""
        # Attempt to create player with SQL injection in name
        malicious_names = [
            "'; DROP TABLE players; --",
            "Player' OR '1'='1",
            "Player'; DELETE FROM players; --",
        ]

        for malicious_name in malicious_names:
            # Should fail validation or be sanitized
            # The exact behavior depends on validation rules
            player = Player(
                player_id=f"test-{malicious_name[:10]}",
                user_id="test-user",
                name=malicious_name,
            )

            # Save should either succeed with sanitized name or fail validation
            # The important thing is that it doesn't execute malicious SQL
            try:
                persistence.save_player(player)
                # If it succeeds, verify the name was sanitized
                saved_player = persistence.get_player_by_name(malicious_name)
                if saved_player:
                    # Name should be sanitized, not contain SQL
                    assert "DROP" not in saved_player.name
                    assert "DELETE" not in saved_player.name
                    assert ";" not in saved_player.name
            except (DatabaseError, ValidationError):
                # Validation error is acceptable - prevents injection
                pass
