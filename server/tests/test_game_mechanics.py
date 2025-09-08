"""
Tests for the game/mechanics module.

This module tests the GameMechanicsService class which handles all game mechanics
including sanity, fear, corruption, healing, and damage mechanics.
"""

import uuid
from unittest.mock import Mock

import pytest

from ..exceptions import ValidationError
from ..game.mechanics import GameMechanicsService


class TestGameMechanicsService:
    """Test cases for GameMechanicsService."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create a mock persistence object with the required methods
        self.mock_persistence = Mock()
        self.mock_persistence.get_player = Mock()
        self.mock_persistence.apply_sanity_loss = Mock()
        self.mock_persistence.apply_fear = Mock()
        self.mock_persistence.apply_corruption = Mock()
        self.mock_persistence.gain_occult_knowledge = Mock()
        self.mock_persistence.heal_player = Mock()
        self.mock_persistence.damage_player = Mock()

        # Create the service instance
        self.mechanics_service = GameMechanicsService(self.mock_persistence)

        # Create a mock player for testing
        self.mock_player = Mock()
        self.mock_player.name = "TestPlayer"
        self.mock_player.player_id = str(uuid.uuid4())

    def test_apply_sanity_loss_success(self):
        """Test successful sanity loss application."""
        # Setup
        player_id = str(uuid.uuid4())
        amount = 10
        source = "eldritch tome"

        self.mock_persistence.get_player.return_value = self.mock_player

        # Execute
        success, message = self.mechanics_service.apply_sanity_loss(player_id, amount, source)

        # Verify
        assert success is True
        assert f"Applied {amount} sanity loss to {self.mock_player.name}" in message
        self.mock_persistence.get_player.assert_called_once_with(player_id)
        self.mock_persistence.apply_sanity_loss.assert_called_once_with(self.mock_player, amount, source)

    def test_apply_sanity_loss_player_not_found(self):
        """Test sanity loss application when player is not found."""
        # Setup
        player_id = str(uuid.uuid4())
        amount = 10
        source = "eldritch tome"

        self.mock_persistence.get_player.return_value = None

        # Execute & Verify
        with pytest.raises(ValidationError, match="Player not found for sanity loss"):
            self.mechanics_service.apply_sanity_loss(player_id, amount, source)
        self.mock_persistence.get_player.assert_called_once_with(player_id)
        self.mock_persistence.apply_sanity_loss.assert_not_called()

    def test_apply_sanity_loss_default_source(self):
        """Test sanity loss application with default source."""
        # Setup
        player_id = str(uuid.uuid4())
        amount = 10

        self.mock_persistence.get_player.return_value = self.mock_player

        # Execute
        success, message = self.mechanics_service.apply_sanity_loss(player_id, amount)

        # Verify
        assert success is True
        self.mock_persistence.apply_sanity_loss.assert_called_once_with(self.mock_player, amount, "unknown")

    def test_apply_fear_success(self):
        """Test successful fear application."""
        # Setup
        player_id = str(uuid.uuid4())
        amount = 15
        source = "dark ritual"

        self.mock_persistence.get_player.return_value = self.mock_player

        # Execute
        success, message = self.mechanics_service.apply_fear(player_id, amount, source)

        # Verify
        assert success is True
        assert f"Applied {amount} fear to {self.mock_player.name}" in message
        self.mock_persistence.get_player.assert_called_once_with(player_id)
        self.mock_persistence.apply_fear.assert_called_once_with(self.mock_player, amount, source)

    def test_apply_fear_player_not_found(self):
        """Test fear application when player is not found."""
        # Setup
        player_id = str(uuid.uuid4())
        amount = 15
        source = "dark ritual"

        self.mock_persistence.get_player.return_value = None

        # Execute & Verify
        with pytest.raises(ValidationError, match="Player not found for fear application"):
            self.mechanics_service.apply_fear(player_id, amount, source)
        self.mock_persistence.get_player.assert_called_once_with(player_id)
        self.mock_persistence.apply_fear.assert_not_called()

    def test_apply_corruption_success(self):
        """Test successful corruption application."""
        # Setup
        player_id = str(uuid.uuid4())
        amount = 5
        source = "forbidden knowledge"

        self.mock_persistence.get_player.return_value = self.mock_player

        # Execute
        success, message = self.mechanics_service.apply_corruption(player_id, amount, source)

        # Verify
        assert success is True
        assert f"Applied {amount} corruption to {self.mock_player.name}" in message
        self.mock_persistence.get_player.assert_called_once_with(player_id)
        self.mock_persistence.apply_corruption.assert_called_once_with(self.mock_player, amount, source)

    def test_apply_corruption_player_not_found(self):
        """Test corruption application when player is not found."""
        # Setup
        player_id = str(uuid.uuid4())
        amount = 5
        source = "forbidden knowledge"

        self.mock_persistence.get_player.return_value = None

        # Execute & Verify
        with pytest.raises(ValidationError, match="Player not found for corruption application"):
            self.mechanics_service.apply_corruption(player_id, amount, source)
        self.mock_persistence.get_player.assert_called_once_with(player_id)
        self.mock_persistence.apply_corruption.assert_not_called()

    def test_gain_occult_knowledge_success(self):
        """Test successful occult knowledge gain."""
        # Setup
        player_id = str(uuid.uuid4())
        amount = 20
        source = "necronomicon"

        self.mock_persistence.get_player.return_value = self.mock_player

        # Execute
        success, message = self.mechanics_service.gain_occult_knowledge(player_id, amount, source)

        # Verify
        assert success is True
        assert f"Gained {amount} occult knowledge for {self.mock_player.name}" in message
        self.mock_persistence.get_player.assert_called_once_with(player_id)
        self.mock_persistence.gain_occult_knowledge.assert_called_once_with(self.mock_player, amount, source)

    def test_gain_occult_knowledge_player_not_found(self):
        """Test occult knowledge gain when player is not found."""
        # Setup
        player_id = str(uuid.uuid4())
        amount = 20
        source = "necronomicon"

        self.mock_persistence.get_player.return_value = None

        # Execute & Verify
        with pytest.raises(ValidationError, match="Player not found for occult knowledge gain"):
            self.mechanics_service.gain_occult_knowledge(player_id, amount, source)
        self.mock_persistence.get_player.assert_called_once_with(player_id)
        self.mock_persistence.gain_occult_knowledge.assert_not_called()

    def test_heal_player_success(self):
        """Test successful player healing."""
        # Setup
        player_id = str(uuid.uuid4())
        amount = 25

        self.mock_persistence.get_player.return_value = self.mock_player

        # Execute
        success, message = self.mechanics_service.heal_player(player_id, amount)

        # Verify
        assert success is True
        assert f"Healed {self.mock_player.name} for {amount} health" in message
        self.mock_persistence.get_player.assert_called_once_with(player_id)
        self.mock_persistence.heal_player.assert_called_once_with(self.mock_player, amount)

    def test_heal_player_not_found(self):
        """Test healing when player is not found."""
        # Setup
        player_id = str(uuid.uuid4())
        amount = 25

        self.mock_persistence.get_player.return_value = None

        # Execute & Verify
        with pytest.raises(ValidationError, match="Player not found for healing"):
            self.mechanics_service.heal_player(player_id, amount)
        self.mock_persistence.get_player.assert_called_once_with(player_id)
        self.mock_persistence.heal_player.assert_not_called()

    def test_damage_player_success(self):
        """Test successful player damage."""
        # Setup
        player_id = str(uuid.uuid4())
        amount = 30
        damage_type = "psychic"

        self.mock_persistence.get_player.return_value = self.mock_player

        # Execute
        success, message = self.mechanics_service.damage_player(player_id, amount, damage_type)

        # Verify
        assert success is True
        assert f"Damaged {self.mock_player.name} for {amount} {damage_type} damage" in message
        self.mock_persistence.get_player.assert_called_once_with(player_id)
        self.mock_persistence.damage_player.assert_called_once_with(self.mock_player, amount, damage_type)

    def test_damage_player_default_type(self):
        """Test player damage with default damage type."""
        # Setup
        player_id = str(uuid.uuid4())
        amount = 30

        self.mock_persistence.get_player.return_value = self.mock_player

        # Execute
        success, message = self.mechanics_service.damage_player(player_id, amount)

        # Verify
        assert success is True
        assert f"Damaged {self.mock_player.name} for {amount} physical damage" in message
        self.mock_persistence.damage_player.assert_called_once_with(self.mock_player, amount, "physical")

    def test_damage_player_not_found(self):
        """Test damage when player is not found."""
        # Setup
        player_id = str(uuid.uuid4())
        amount = 30
        damage_type = "psychic"

        self.mock_persistence.get_player.return_value = None

        # Execute & Verify
        with pytest.raises(ValidationError, match="Player not found for damage"):
            self.mechanics_service.damage_player(player_id, amount, damage_type)
        self.mock_persistence.get_player.assert_called_once_with(player_id)
        self.mock_persistence.damage_player.assert_not_called()

    def test_zero_amount_operations(self):
        """Test operations with zero amounts."""
        # Setup
        player_id = str(uuid.uuid4())

        self.mock_persistence.get_player.return_value = self.mock_player

        # Test all operations with zero amounts
        operations = [
            ("apply_sanity_loss", 0, "test"),
            ("apply_fear", 0, "test"),
            ("apply_corruption", 0, "test"),
            ("gain_occult_knowledge", 0, "test"),
            ("heal_player", 0),
            ("damage_player", 0, "physical"),
        ]

        for operation, amount, *args in operations:
            method = getattr(self.mechanics_service, operation)
            if operation == "heal_player":
                success, message = method(player_id, amount)
            else:
                success, message = method(player_id, amount, *args)

            assert success is True
            assert str(amount) in message

    def test_negative_amount_operations(self):
        """Test operations with negative amounts."""
        # Setup
        player_id = str(uuid.uuid4())

        self.mock_persistence.get_player.return_value = self.mock_player

        # Test all operations with negative amounts
        operations = [
            ("apply_sanity_loss", -10, "test"),
            ("apply_fear", -15, "test"),
            ("apply_corruption", -5, "test"),
            ("gain_occult_knowledge", -20, "test"),
            ("heal_player", -25),
            ("damage_player", -30, "physical"),
        ]

        for operation, amount, *args in operations:
            method = getattr(self.mechanics_service, operation)
            if operation == "heal_player":
                success, message = method(player_id, amount)
            else:
                success, message = method(player_id, amount, *args)

            assert success is True
            assert str(amount) in message

    def test_large_amount_operations(self):
        """Test operations with large amounts."""
        # Setup
        player_id = str(uuid.uuid4())

        self.mock_persistence.get_player.return_value = self.mock_player

        # Test all operations with large amounts
        operations = [
            ("apply_sanity_loss", 1000, "test"),
            ("apply_fear", 1500, "test"),
            ("apply_corruption", 500, "test"),
            ("gain_occult_knowledge", 2000, "test"),
            ("heal_player", 2500),
            ("damage_player", 3000, "physical"),
        ]

        for operation, amount, *args in operations:
            method = getattr(self.mechanics_service, operation)
            if operation == "heal_player":
                success, message = method(player_id, amount)
            else:
                success, message = method(player_id, amount, *args)

            assert success is True
            assert str(amount) in message

    def test_service_initialization(self):
        """Test GameMechanicsService initialization."""
        # Test that the service is properly initialized
        assert self.mechanics_service.persistence == self.mock_persistence
        assert hasattr(self.mechanics_service, "apply_sanity_loss")
        assert hasattr(self.mechanics_service, "apply_fear")
        assert hasattr(self.mechanics_service, "apply_corruption")
        assert hasattr(self.mechanics_service, "gain_occult_knowledge")
        assert hasattr(self.mechanics_service, "heal_player")
        assert hasattr(self.mechanics_service, "damage_player")

    def test_persistence_method_calls(self):
        """Test that all persistence methods are called correctly."""
        # Setup
        player_id = str(uuid.uuid4())

        self.mock_persistence.get_player.return_value = self.mock_player

        # Test all methods to ensure persistence calls are made
        test_cases = [
            ("apply_sanity_loss", [10, "test"], "apply_sanity_loss"),
            ("apply_fear", [15, "test"], "apply_fear"),
            ("apply_corruption", [5, "test"], "apply_corruption"),
            ("gain_occult_knowledge", [20, "test"], "gain_occult_knowledge"),
            ("heal_player", [25], "heal_player"),
            ("damage_player", [30, "psychic"], "damage_player"),
        ]

        for method_name, args, persistence_method in test_cases:
            # Reset mock
            self.mock_persistence.reset_mock()

            # Call the method
            method = getattr(self.mechanics_service, method_name)
            method(player_id, *args)

            # Verify persistence method was called
            persistence_method_obj = getattr(self.mock_persistence, persistence_method)
            persistence_method_obj.assert_called_once()

            # Verify the call arguments
            call_args = persistence_method_obj.call_args[0]
            assert call_args[0] == self.mock_player  # First arg should be the player
            assert call_args[1] == args[0]  # Second arg should be the amount
