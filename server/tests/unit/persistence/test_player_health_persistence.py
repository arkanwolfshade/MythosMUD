"""
Test for player health persistence bug.

This test reproduces the issue where player health changes during combat
are not persisted to the database.

Root Cause Analysis:
====================
The persistence layer is missing the following methods that are being called by the game mechanics:
- damage_player(player, amount, damage_type) - Called by GameMechanicsService.damage_player()
- heal_player(player, amount) - Called by GameMechanicsService.heal_player()
- async_damage_player(player, amount, damage_type) - Called by PlayerService.damage_player()
- async_heal_player(player, amount) - Called by PlayerService.heal_player()

When these methods are called, they raise AttributeError, which is caught by error handlers
in the calling code, causing health changes to update in memory but never persist to the database.
"""

import pytest

from server.database import get_database_url
from server.models.player import Player
from server.persistence import PersistenceLayer


class TestPlayerHealthPersistence:
    """
    Simplified tests for player health persistence methods.

    These tests verify that the required methods exist and work correctly
    without requiring complex database setup with users and relationships.
    """

    @pytest.fixture
    def test_player(self):
        """Create a simple test player without database dependencies."""
        # Create a minimal player object with just the fields we need
        # Use proper UUID format for player_id (PostgreSQL requires valid UUID)
        from uuid import uuid4

        player = Player(
            player_id=str(uuid4()),
            name="TestPlayer",
            level=1,
            experience_points=0,
        )
        # Set initial health
        stats = player.get_stats()
        stats["current_health"] = 100
        stats["max_health"] = 100
        player.set_stats(stats)
        return player

    @pytest.fixture
    def persistence(self):
        """Create a PersistenceLayer instance using PostgreSQL from environment."""
        database_url = get_database_url()
        if not database_url or not database_url.startswith("postgresql"):
            pytest.skip("DATABASE_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")
        # Don't pass db_path - let it use DATABASE_URL from environment
        return PersistenceLayer()

    def test_damage_player_method_exists(self, persistence):
        """Test that PersistenceLayer has damage_player() method."""
        assert hasattr(persistence, "damage_player"), "PersistenceLayer missing damage_player() method"
        assert callable(persistence.damage_player), "damage_player must be callable"

    def test_heal_player_method_exists(self, persistence):
        """Test that PersistenceLayer has heal_player() method."""
        assert hasattr(persistence, "heal_player"), "PersistenceLayer missing heal_player() method"
        assert callable(persistence.heal_player), "heal_player must be callable"

    def test_async_damage_player_method_exists(self, persistence):
        """Test that PersistenceLayer has async_damage_player() method."""
        assert hasattr(persistence, "async_damage_player"), "PersistenceLayer missing async_damage_player() method"
        assert callable(persistence.async_damage_player), "async_damage_player must be callable"

    def test_async_heal_player_method_exists(self, persistence):
        """Test that PersistenceLayer has async_heal_player() method."""
        assert hasattr(persistence, "async_heal_player"), "PersistenceLayer missing async_heal_player() method"
        assert callable(persistence.async_heal_player), "async_heal_player must be callable"

    def test_damage_player_updates_health(self, test_player, persistence):
        """Test that damage_player() correctly updates player health in memory."""
        from unittest.mock import Mock, patch

        # Get initial health
        initial_health = test_player.get_stats().get("current_health", 100)

        # Mock update_player_health (atomic field update) to avoid database writes
        with patch.object(persistence, "update_player_health", Mock()):
            # Damage the player
            persistence.damage_player(test_player, 30, "physical")

        # Check that health was reduced in memory
        new_health = test_player.get_stats().get("current_health", 0)
        expected_health = initial_health - 30

        assert new_health == expected_health, (
            f"Health not updated correctly. Expected: {expected_health}, Got: {new_health}, Initial: {initial_health}"
        )

    def test_heal_player_updates_health(self, test_player, persistence):
        """Test that heal_player() correctly updates player health in memory."""
        from unittest.mock import Mock, patch

        # Set player to damaged state
        stats = test_player.get_stats()
        stats["current_health"] = 50
        test_player.set_stats(stats)

        # Mock update_player_health (atomic field update) to avoid database writes
        with patch.object(persistence, "update_player_health", Mock()):
            # Heal the player
            persistence.heal_player(test_player, 20)

        # Check that health was increased in memory
        new_health = test_player.get_stats().get("current_health", 0)

        assert new_health == 70, f"Health not updated correctly. Expected: 70, Got: {new_health}"

    def test_damage_player_handles_negative_values(self, test_player, persistence):
        """Test that damage_player() rejects negative damage amounts."""
        from unittest.mock import Mock, patch

        with patch.object(persistence, "update_player_health", Mock()):
            # Patch logger to avoid Unicode encoding issues on Windows
            with patch.object(persistence._logger, "error", Mock()):
                with pytest.raises(ValueError, match="Damage amount must be positive"):
                    persistence.damage_player(test_player, -10, "physical")

    def test_heal_player_handles_negative_values(self, test_player, persistence):
        """Test that heal_player() rejects negative heal amounts."""
        from unittest.mock import Mock, patch

        with patch.object(persistence, "update_player_health", Mock()):
            # Patch logger to avoid Unicode encoding issues on Windows
            with patch.object(persistence._logger, "error", Mock()):
                with pytest.raises(ValueError, match="Healing amount must be positive"):
                    persistence.heal_player(test_player, -10)

    def test_damage_player_caps_at_zero(self, test_player, persistence):
        """Test that damage_player() doesn't reduce health below zero in memory."""
        from unittest.mock import Mock, patch

        # Set player to low health
        stats = test_player.get_stats()
        stats["current_health"] = 10
        test_player.set_stats(stats)

        # Mock update_player_health (atomic field update) to avoid database writes
        with patch.object(persistence, "update_player_health", Mock()):
            # Apply massive damage
            persistence.damage_player(test_player, 1000, "physical")

        # Health should be capped at 0 in memory
        new_health = test_player.get_stats().get("current_health", -1)
        assert new_health == 0, f"Health should be capped at 0, got: {new_health}"

    def test_heal_player_caps_at_max_health(self, test_player, persistence):
        """Test that heal_player() doesn't exceed max health in memory."""
        from unittest.mock import Mock, patch

        # Set player to damaged state
        stats = test_player.get_stats()
        stats["current_health"] = 50
        stats["max_health"] = 100
        test_player.set_stats(stats)

        # Mock update_player_health (atomic field update) to avoid database writes
        with patch.object(persistence, "update_player_health", Mock()):
            # Apply massive healing
            persistence.heal_player(test_player, 1000)

        # Health should be capped at max_health in memory
        new_health = test_player.get_stats().get("current_health", -1)
        max_health = test_player.get_stats().get("max_health", 100)
        assert new_health == max_health, f"Health should be capped at {max_health}, got: {new_health}"

    @pytest.mark.asyncio
    async def test_async_damage_player_updates_health(self, test_player, persistence):
        """Test that async_damage_player() correctly updates player health in memory."""
        from unittest.mock import Mock, patch

        # Get initial health
        initial_health = test_player.get_stats().get("current_health", 100)

        # Mock update_player_health since async methods delegate to sync versions
        with patch.object(persistence, "update_player_health", Mock()):
            # Damage the player asynchronously
            await persistence.async_damage_player(test_player, 25, "physical")

        # Check that health was reduced in memory
        new_health = test_player.get_stats().get("current_health", 0)
        expected_health = initial_health - 25

        assert new_health == expected_health, (
            f"Health not updated correctly. Expected: {expected_health}, Got: {new_health}"
        )

    @pytest.mark.asyncio
    async def test_async_heal_player_updates_health(self, test_player, persistence):
        """Test that async_heal_player() correctly updates player health in memory."""
        from unittest.mock import Mock, patch

        # Set player to damaged state
        stats = test_player.get_stats()
        stats["current_health"] = 60
        test_player.set_stats(stats)

        # Mock update_player_health since async methods delegate to sync versions
        with patch.object(persistence, "update_player_health", Mock()):
            # Heal the player asynchronously
            await persistence.async_heal_player(test_player, 15)

        # Check that health was increased in memory
        new_health = test_player.get_stats().get("current_health", 0)

        assert new_health == 75, f"Health not updated correctly. Expected: 75, Got: {new_health}"
