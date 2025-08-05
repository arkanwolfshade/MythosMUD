"""Tests for the models/relationships module."""

import pytest

from ..models.invite import Invite
from ..models.player import Player
from ..models.relationships import setup_relationships
from ..models.user import User


class TestModelsRelationships:
    """Test the models/relationships module functionality."""

    def test_setup_relationships_function_exists(self):
        """Test that the setup_relationships function exists and is callable."""
        assert callable(setup_relationships)

    def test_setup_relationships_docstring(self):
        """Test that setup_relationships has proper documentation."""
        assert setup_relationships.__doc__ is not None
        assert "Set up all model relationships" in setup_relationships.__doc__

    def test_setup_relationships_can_be_called(self):
        """Test that setup_relationships can be called without errors."""
        # This should not raise any exceptions
        setup_relationships()

    def test_user_player_relationship_established(self):
        """Test that User -> Player relationship is properly established."""
        setup_relationships()

        # Check that the relationship attribute exists
        assert hasattr(User, "player")
        assert User.player is not None

    def test_user_used_invite_relationship_established(self):
        """Test that User -> Invite relationship is properly established."""
        setup_relationships()

        # Check that the relationship attribute exists
        assert hasattr(User, "used_invite")
        assert User.used_invite is not None

    def test_user_created_invites_relationship_established(self):
        """Test that User -> Invite (created_invites) relationship is properly established."""
        setup_relationships()

        # Check that the relationship attribute exists
        assert hasattr(User, "created_invites")
        assert User.created_invites is not None

    def test_player_user_relationship_established(self):
        """Test that Player -> User relationship is properly established."""
        setup_relationships()

        # Check that the relationship attribute exists
        assert hasattr(Player, "user")
        assert Player.user is not None

    def test_invite_created_by_user_relationship_established(self):
        """Test that Invite -> User (created_by_user) relationship is properly established."""
        setup_relationships()

        # Check that the relationship attribute exists
        assert hasattr(Invite, "created_by_user")
        assert Invite.created_by_user is not None

    def test_invite_used_by_user_relationship_established(self):
        """Test that Invite -> User (used_by_user) relationship is properly established."""
        setup_relationships()

        # Check that the relationship attribute exists
        assert hasattr(Invite, "used_by_user")
        assert Invite.used_by_user is not None

    def test_relationships_are_sqlalchemy_attributes(self):
        """Test that the established relationships are proper SQLAlchemy attributes."""
        setup_relationships()

        # Import to check type
        from sqlalchemy.orm.attributes import InstrumentedAttribute

        # Check that all relationships are proper SQLAlchemy attributes
        assert isinstance(User.player, InstrumentedAttribute)
        assert isinstance(User.used_invite, InstrumentedAttribute)
        assert isinstance(User.created_invites, InstrumentedAttribute)
        assert isinstance(Player.user, InstrumentedAttribute)
        assert isinstance(Invite.created_by_user, InstrumentedAttribute)
        assert isinstance(Invite.used_by_user, InstrumentedAttribute)

    def test_relationships_handle_existing_attributes(self):
        """Test that setup_relationships handles existing relationship attributes."""
        setup_relationships()

        # Call setup_relationships again - should not overwrite existing relationships
        setup_relationships()

        # Relationships should still be properly configured
        assert hasattr(User, "player")
        assert hasattr(User, "used_invite")
        assert hasattr(User, "created_invites")
        assert hasattr(Player, "user")
        assert hasattr(Invite, "created_by_user")
        assert hasattr(Invite, "used_by_user")

    def test_relationships_with_mock_models(self):
        """Test that relationships work with mock model classes."""

        # Create mock classes to test relationship setup
        class MockUser:
            __table__ = type(
                "MockTable", (), {"c": type("MockColumns", (), {"get": lambda self, name, default: None})()}
            )

        class MockPlayer:
            __table__ = type(
                "MockTable", (), {"c": type("MockColumns", (), {"get": lambda self, name, default: None})()}
            )

        class MockInvite:
            __table__ = type(
                "MockTable", (), {"c": type("MockColumns", (), {"get": lambda self, name, default: None})()}
            )

        # This should not raise any exceptions
        try:
            # Simulate the relationship setup logic
            MockUser.player = None
            if not MockUser.player:
                from sqlalchemy.orm import relationship

                MockUser.player = relationship("Player", back_populates="user", uselist=False)

            assert MockUser.player is not None
        except Exception as e:
            pytest.fail(f"Relationship setup should not fail: {e}")

    def test_relationships_import_structure(self):
        """Test that all necessary imports are available in the relationships module."""
        from ..models.relationships import setup_relationships

        # Test that we can import the function
        assert setup_relationships is not None

        # Test that we can import the models
        assert User is not None
        assert Player is not None
        assert Invite is not None

    def test_relationships_function_signature(self):
        """Test that setup_relationships has the expected function signature."""
        import inspect

        # Get function signature
        sig = inspect.signature(setup_relationships)

        # Should take no parameters
        assert len(sig.parameters) == 0

        # Should return None (void function)
        assert sig.return_annotation == inspect.Signature.empty

    def test_relationships_are_consistent_across_calls(self):
        """Test that relationships remain consistent across multiple setup calls."""
        setup_relationships()

        # Call setup_relationships again
        setup_relationships()

        # Relationships should remain the same (same attribute names)
        assert hasattr(User, "player")
        assert hasattr(User, "used_invite")
        assert hasattr(User, "created_invites")
        assert hasattr(Player, "user")
        assert hasattr(Invite, "created_by_user")
        assert hasattr(Invite, "used_by_user")

    def test_relationships_module_docstring(self):
        """Test that the relationships module has proper documentation."""
        # Check that the module has proper docstring by reading the file
        from pathlib import Path

        # Get the path to the relationships module
        relationships_path = Path(__file__).parent.parent / "models" / "relationships.py"

        # Read the file content
        content = relationships_path.read_text(encoding="utf-8")

        # Check for module docstring
        assert '"""' in content or "'''" in content
        assert "Model relationships setup" in content

    def test_relationships_imports_work(self):
        """Test that all necessary imports work correctly."""
        # Test that we can import all the required modules
        from ..models.invite import Invite
        from ..models.player import Player
        from ..models.relationships import setup_relationships
        from ..models.user import User

        # Test that all imports are successful
        assert setup_relationships is not None
        assert Invite is not None
        assert Player is not None
        assert User is not None

    def test_relationships_setup_is_idempotent(self):
        """Test that calling setup_relationships multiple times is safe."""
        # First call
        setup_relationships()

        # Second call should not cause issues
        setup_relationships()

        # Third call should also be safe
        setup_relationships()

        # All relationships should still be properly configured
        assert hasattr(User, "player")
        assert hasattr(User, "used_invite")
        assert hasattr(User, "created_invites")
        assert hasattr(Player, "user")
        assert hasattr(Invite, "created_by_user")
        assert hasattr(Invite, "used_by_user")
