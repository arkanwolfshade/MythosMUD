"""
Tests for ValidationError import handling and error propagation.

This module tests the proper handling of ValidationError imports to ensure
no namespace collisions and correct error propagation across the system.

As noted in the Pnakotic Manuscripts, proper error handling is essential
for maintaining the delicate balance between order and chaos in our digital realm.
"""

import pytest
from pydantic import ValidationError as PydanticValidationError

from ..exceptions import ValidationError as MythosValidationError
from ..models.command import SayCommand
from ..utils.command_parser import CommandParser
from ..utils.command_processor import CommandProcessor


class TestValidationErrorImports:
    """Test ValidationError import handling and namespace resolution."""

    def test_pydantic_validation_error_import(self):
        """Test that Pydantic ValidationError can be imported without conflicts."""
        # This test ensures we can import Pydantic's ValidationError
        # without namespace collisions
        from pydantic import ValidationError as PydanticValidationError

        # Verify it's the correct type
        assert PydanticValidationError is not None
        assert issubclass(PydanticValidationError, Exception)

    def test_mythos_validation_error_import(self):
        """Test that custom ValidationError can be imported without conflicts."""
        # This test ensures we can import our custom ValidationError
        # without namespace collisions
        from ..exceptions import ValidationError as MythosValidationError

        # Verify it's the correct type
        assert MythosValidationError is not None
        assert issubclass(MythosValidationError, Exception)

    def test_both_validation_errors_distinct(self):
        """Test that both ValidationError types are distinct and can coexist."""
        # Verify they are different classes
        assert PydanticValidationError is not MythosValidationError

        # Verify they have different inheritance hierarchies
        assert PydanticValidationError.__module__ != MythosValidationError.__module__

    def test_pydantic_validation_error_creation(self):
        """Test that Pydantic ValidationError can be created and raised."""
        # Test creating a Pydantic ValidationError
        with pytest.raises(PydanticValidationError) as exc_info:
            # This should raise a Pydantic ValidationError
            SayCommand(message="")  # Empty message should fail validation

        # Verify it's the correct exception type
        assert isinstance(exc_info.value, PydanticValidationError)
        assert not isinstance(exc_info.value, MythosValidationError)

    def test_mythos_validation_error_creation(self):
        """Test that custom ValidationError can be created and raised."""
        # Test creating a custom ValidationError
        with pytest.raises(MythosValidationError):
            # This should raise our custom ValidationError
            raise MythosValidationError("Test error message")

    def test_command_processor_error_handling(self):
        """Test that CommandProcessor handles both error types correctly."""
        processor = CommandProcessor()

        # Test with invalid command - should return error message, not raise exception
        result = processor.process_command_string("say", "test_user")
        validated_command, error_message, command_type = result

        # Should return None for command and error message
        assert validated_command is None
        assert error_message is not None
        assert "Unexpected error processing command" in error_message
        assert command_type is None

        # Test with unknown command
        result = processor.process_command_string("invalid_command", "test_user")
        validated_command, error_message, command_type = result

        # Should return None for command and error message
        assert validated_command is None
        assert error_message is not None
        assert command_type is None

    def test_command_parser_error_handling(self):
        """Test that CommandParser handles both error types correctly."""
        parser = CommandParser()

        # Test with invalid command that should raise MythosValidationError (our custom error)
        with pytest.raises(MythosValidationError):
            parser.parse_command("say")  # Missing message should fail validation

        # Test with unknown command
        with pytest.raises(MythosValidationError):
            parser.parse_command("invalid_command")

    def test_error_propagation_chain(self):
        """Test that errors propagate correctly through the command processing chain."""
        processor = CommandProcessor()

        # Test error propagation from parser to processor - should return error, not raise
        result = processor.process_command_string("say", "test_user")
        validated_command, error_message, command_type = result

        # Error should be properly handled and returned as message
        assert validated_command is None
        assert error_message is not None
        assert len(error_message) > 0
        assert command_type is None

    def test_import_resolution_consistency(self):
        """Test that imports resolve consistently across modules."""
        # Test that all modules can import both error types without conflicts
        from server.exceptions import ValidationError as MythosValidationError
        from server.utils.command_parser import CommandParser
        from server.utils.command_processor import CommandProcessor

        # Verify imports work without raising ImportError
        assert CommandProcessor is not None
        assert CommandParser is not None
        assert MythosValidationError is not None

    def test_error_type_checking(self):
        """Test that error type checking works correctly with both error types."""
        # Test isinstance checks work correctly - create errors properly
        try:
            SayCommand(message="")  # This will raise PydanticValidationError
        except PydanticValidationError as pydantic_error:
            # Verify isinstance checks work correctly
            assert isinstance(pydantic_error, PydanticValidationError)
            assert not isinstance(pydantic_error, MythosValidationError)

        # Test custom error
        mythos_error = MythosValidationError("test")
        assert isinstance(mythos_error, MythosValidationError)
        assert not isinstance(mythos_error, PydanticValidationError)

    def test_error_attributes_access(self):
        """Test that error attributes can be accessed correctly for both types."""
        # Test PydanticValidationError attributes
        try:
            SayCommand(message="")
        except PydanticValidationError as e:
            # Verify Pydantic-specific attributes are accessible
            assert hasattr(e, "errors")
            assert callable(getattr(e, "errors", None))
            # Note: 'model' attribute may not be available in all Pydantic versions

        # Test MythosValidationError attributes
        mythos_error = MythosValidationError("test")
        assert hasattr(mythos_error, "message")
        assert hasattr(mythos_error, "context")
        assert mythos_error.message == "test"


class TestValidationErrorNamespaceCollision:
    """Test scenarios that could cause namespace collisions."""

    def test_import_order_independence(self):
        """Test that import order doesn't affect namespace resolution."""
        # Test importing in different orders
        from pydantic import ValidationError as PydanticValidationError

        from ..exceptions import ValidationError as MythosValidationError

        # Verify both are available and distinct
        assert PydanticValidationError is not MythosValidationError

        # Test reverse order
        from pydantic import ValidationError as PydanticValidationError2

        from ..exceptions import ValidationError as MythosValidationError2

        # Verify they're still distinct
        assert PydanticValidationError2 is not MythosValidationError2
        assert PydanticValidationError2 is PydanticValidationError
        assert MythosValidationError2 is MythosValidationError

    def test_module_reload_safety(self):
        """Test that module reloading doesn't cause namespace issues."""
        import importlib

        from server.utils import command_parser, command_processor

        # Reload modules to test namespace stability
        importlib.reload(command_processor)
        importlib.reload(command_parser)

        # Verify imports still work after reload
        from pydantic import ValidationError as PydanticValidationError

        from ..exceptions import ValidationError as MythosValidationError

        assert PydanticValidationError is not MythosValidationError

    def test_circular_import_handling(self):
        """Test that circular imports don't cause namespace conflicts."""
        # Test importing modules that might have circular dependencies
        from server.exceptions import ValidationError as MythosValidationError
        from server.utils.command_parser import CommandParser
        from server.utils.command_processor import CommandProcessor

        # Verify all imports work without conflicts
        assert CommandProcessor is not None
        assert CommandParser is not None
        assert MythosValidationError is not None


class TestValidationErrorErrorHandling:
    """Test error handling patterns with both ValidationError types."""

    def test_exception_handling_patterns(self):
        """Test common exception handling patterns work with both error types."""
        # Test try-except with both error types
        try:
            SayCommand(message="")
        except PydanticValidationError:
            # Should catch Pydantic errors
            pass
        except MythosValidationError:
            # Should not catch Pydantic errors
            pytest.fail("MythosValidationError should not catch PydanticValidationError")

        # Test try-except with custom error
        try:
            raise MythosValidationError("test")
        except MythosValidationError:
            # Should catch custom errors
            pass
        except PydanticValidationError:
            # Should not catch custom errors
            pytest.fail("PydanticValidationError should not catch MythosValidationError")

    def test_error_message_consistency(self):
        """Test that error messages are consistent and informative."""
        # Test Pydantic error message
        try:
            SayCommand(message="")
        except PydanticValidationError as e:
            # Verify error message is informative
            assert str(e) is not None
            assert len(str(e)) > 0
            # Should contain information about the validation failure
            assert "message" in str(e).lower() or "validation" in str(e).lower()

        # Test custom error message
        custom_error = MythosValidationError("Custom validation failed")
        assert str(custom_error) == "Custom validation failed"

    def test_error_context_preservation(self):
        """Test that error context is preserved correctly."""
        # Test Pydantic error context
        try:
            SayCommand(message="")
        except PydanticValidationError as e:
            # Verify error context is accessible
            assert hasattr(e, "errors")
            errors = e.errors()
            assert isinstance(errors, list)
            assert len(errors) > 0

        # Test custom error context - context is automatically created if not provided
        custom_error = MythosValidationError("test")
        assert hasattr(custom_error, "context")
        assert custom_error.context is not None  # Context is auto-created
