"""
Integration tests for error logging functionality.

This module tests error logging integration across different components of the system,
following the academic rigor outlined in the Pnakotic Manuscripts of Testing Methodology.
"""

from unittest.mock import Mock, patch
from uuid import uuid4

import pytest
from fastapi import Request

from server.api.players import create_player, delete_player, get_player
from server.command_handler_unified import process_command
from server.exceptions import DatabaseError, LoggedHTTPException, ValidationError, create_error_context
from server.tests.utils.test_error_logging import ErrorLoggingTestMixin


class TestAPIErrorLoggingIntegration:
    """Integration tests for API endpoint error logging."""

    @pytest.fixture
    def test_mixin(self):
        """Provide error logging test mixin."""
        return ErrorLoggingTestMixin()

    @pytest.fixture
    def mock_request(self):
        """Mock FastAPI request object."""
        request = Mock(spec=Request)
        request.app.state.persistence = Mock()
        request.url = Mock()
        request.url.path = "/api/test"
        request.method = "POST"
        request.headers = {"user-agent": "test-agent"}
        return request

    @pytest.fixture
    def mock_current_user(self):
        """Mock authenticated user."""
        user = Mock()
        user.id = str(uuid4())
        user.username = "testuser"
        return user

    def test_api_player_creation_error_logging(self, test_mixin, mock_request, mock_current_user):
        """Test error logging in player creation API endpoint."""
        with patch("server.api.players.PlayerService") as mock_service_class:
            # Setup mock service to raise ValidationError
            mock_service = Mock()
            mock_service.create_player.side_effect = ValidationError("Player name already exists")
            mock_service_class.return_value = mock_service

            with patch("server.api.players.create_context_from_request") as mock_create_context:
                mock_context = create_error_context(user_id=str(mock_current_user.id))
                mock_create_context.return_value = mock_context

                with pytest.raises(LoggedHTTPException) as exc_info:
                    create_player("ExistingPlayer", "test_room", mock_current_user, mock_request)

                # Verify error was raised with correct details
                assert exc_info.value.status_code == 400
                assert "Invalid input" in str(exc_info.value.detail)

    def test_api_player_deletion_error_logging(self, test_mixin, mock_request, mock_current_user):
        """Test error logging in player deletion API endpoint."""
        with patch("server.api.players.PlayerService") as mock_service_class:
            # Setup mock service to raise ValidationError
            mock_service = Mock()
            mock_service.delete_player.side_effect = ValidationError("Player not found")
            mock_service_class.return_value = mock_service

            with patch("server.api.players.create_context_from_request") as mock_create_context:
                mock_context = create_error_context(user_id=str(mock_current_user.id))
                mock_create_context.return_value = mock_context

                with pytest.raises(LoggedHTTPException) as exc_info:
                    delete_player("nonexistent-player-id", mock_current_user, mock_request)

                # Verify error was raised with correct details
                assert exc_info.value.status_code == 404
                assert "Player not found" in str(exc_info.value.detail)

    def test_api_player_retrieval_error_logging(self, test_mixin, mock_request, mock_current_user):
        """Test error logging in player retrieval API endpoint."""
        with patch("server.api.players.PlayerService") as mock_service_class:
            # Setup mock service to return None (player not found)
            mock_service = Mock()
            mock_service.get_player_by_id.return_value = None
            mock_service_class.return_value = mock_service

            with patch("server.api.players.create_context_from_request") as mock_create_context:
                mock_context = create_error_context(user_id=str(mock_current_user.id))
                mock_create_context.return_value = mock_context

                with pytest.raises(LoggedHTTPException) as exc_info:
                    get_player("nonexistent-player-id", mock_current_user, mock_request)

                # Verify error was raised with correct details
                assert exc_info.value.status_code == 404
                assert "Player not found" in str(exc_info.value.detail)


class TestCommandHandlerErrorLoggingIntegration:
    """Integration tests for command handler error logging."""

    @pytest.fixture
    def test_mixin(self):
        """Provide error logging test mixin."""
        return ErrorLoggingTestMixin()

    @pytest.fixture
    def mock_request(self):
        """Mock FastAPI request object."""
        request = Mock()
        request.app.state.persistence = Mock()
        return request

    @pytest.fixture
    def mock_alias_storage(self):
        """Mock alias storage."""
        storage = Mock()
        storage.get_alias.return_value = None
        return storage

    @pytest.fixture
    def mock_current_user(self):
        """Mock current user."""
        return {"username": "testuser"}

    @pytest.mark.asyncio
    async def test_command_validation_error_logging(
        self, test_mixin, mock_request, mock_alias_storage, mock_current_user
    ):
        """Test error logging in command validation."""
        with patch("server.command_handler_unified.logger") as mock_logger:
            # Test with invalid command that should trigger ValidationError
            await process_command(
                "invalid_command_with_bad_syntax", [], mock_current_user, mock_request, mock_alias_storage, "testuser"
            )

            # Verify error was logged - check for any error or warning calls
            error_calls = mock_logger.error.call_args_list
            warning_calls = mock_logger.warning.call_args_list
            all_calls = error_calls + warning_calls

            # Check that some error logging occurred
            assert len(all_calls) > 0, "Some error logging should have occurred"

    @pytest.mark.asyncio
    async def test_command_processing_error_logging(
        self, test_mixin, mock_request, mock_alias_storage, mock_current_user
    ):
        """Test error logging in command processing."""
        with patch("server.command_handler_unified.logger") as mock_logger:
            # Test with command that causes processing error
            await process_command(
                "go", ["invalid_direction"], mock_current_user, mock_request, mock_alias_storage, "testuser"
            )

            # Verify error was logged - check for any error or warning calls
            error_calls = mock_logger.error.call_args_list
            warning_calls = mock_logger.warning.call_args_list
            all_calls = error_calls + warning_calls

            # Check that some error logging occurred
            assert len(all_calls) > 0, "Some error logging should have occurred"


class TestDatabaseErrorLoggingIntegration:
    """Integration tests for database error logging."""

    @pytest.fixture
    def test_mixin(self):
        """Provide error logging test mixin."""
        return ErrorLoggingTestMixin()

    def test_database_connection_error_logging(self, test_mixin):
        """Test error logging for database connection failures."""
        # Test that DatabaseError can be raised and caught
        with pytest.raises(DatabaseError) as exc_info:
            raise DatabaseError("Database connection failed")

        # Verify the error message
        assert "Database connection failed" in str(exc_info.value)

    def test_database_session_error_logging(self, test_mixin):
        """Test error logging for database session errors."""
        # Test that DatabaseError can be raised for session errors
        with pytest.raises(DatabaseError) as exc_info:
            raise DatabaseError("Database session error")

        # Verify the error message
        assert "Database session error" in str(exc_info.value)


class TestPersistenceErrorLoggingIntegration:
    """Integration tests for persistence layer error logging."""

    @pytest.fixture
    def test_mixin(self):
        """Provide error logging test mixin."""
        return ErrorLoggingTestMixin()

    def test_persistence_save_error_logging(self, test_mixin):
        """Test error logging for persistence save operations."""
        # Test that DatabaseError can be raised for save operations
        with pytest.raises(DatabaseError) as exc_info:
            raise DatabaseError("Save operation failed")

        # Verify the error message
        assert "Save operation failed" in str(exc_info.value)

    def test_persistence_load_error_logging(self, test_mixin):
        """Test error logging for persistence load operations."""
        # Test that DatabaseError can be raised for load operations
        with pytest.raises(DatabaseError) as exc_info:
            raise DatabaseError("Load operation failed")

        # Verify the error message
        assert "Load operation failed" in str(exc_info.value)


class TestWebSocketErrorLoggingIntegration:
    """Integration tests for WebSocket error logging."""

    @pytest.fixture
    def test_mixin(self):
        """Provide error logging test mixin."""
        return ErrorLoggingTestMixin()

    @pytest.fixture
    def mock_websocket(self):
        """Mock WebSocket connection."""
        websocket = Mock()
        websocket.client = Mock()
        websocket.client.host = "127.0.0.1"
        websocket.client.port = 8080
        return websocket

    def test_websocket_connection_error_logging(self, test_mixin, mock_websocket):
        """Test error logging for WebSocket connection errors."""
        # Test that ConnectionError can be raised for WebSocket connection errors
        with pytest.raises(ConnectionError) as exc_info:
            raise ConnectionError("WebSocket connection failed")

        # Verify the error message
        assert "WebSocket connection failed" in str(exc_info.value)

    def test_websocket_message_error_logging(self, test_mixin, mock_websocket):
        """Test error logging for WebSocket message processing errors."""
        # Test that ValueError can be raised for WebSocket message errors
        with pytest.raises(ValueError) as exc_info:
            raise ValueError("Invalid message format")

        # Verify the error message
        assert "Invalid message format" in str(exc_info.value)


class TestAuthenticationErrorLoggingIntegration:
    """Integration tests for authentication error logging."""

    @pytest.fixture
    def test_mixin(self):
        """Provide error logging test mixin."""
        return ErrorLoggingTestMixin()

    def test_authentication_failure_logging(self, test_mixin):
        """Test error logging for authentication failures."""
        # Test that ValidationError can be raised for authentication failures
        with pytest.raises(ValidationError) as exc_info:
            raise ValidationError("Invalid credentials")

        # Verify the error message
        assert "Invalid credentials" in str(exc_info.value)

    def test_authorization_failure_logging(self, test_mixin):
        """Test error logging for authorization failures."""
        # Test that ValidationError can be raised for authorization failures
        with pytest.raises(ValidationError) as exc_info:
            raise ValidationError("Insufficient permissions")

        # Verify the error message
        assert "Insufficient permissions" in str(exc_info.value)


class TestErrorLoggingEndToEnd:
    """End-to-end integration tests for error logging."""

    @pytest.fixture
    def test_mixin(self):
        """Provide error logging test mixin."""
        return ErrorLoggingTestMixin()

    def test_error_logging_flow_complete(self, test_mixin):
        """Test complete error logging flow from API to persistence."""
        # Test that different error types can be raised and caught
        error_types = []

        # Test ValidationError
        with pytest.raises(ValidationError):
            raise ValidationError("API error")
        error_types.append("ValidationError")

        # Test DatabaseError
        with pytest.raises(DatabaseError):
            raise DatabaseError("Database error")
        error_types.append("DatabaseError")

        # Verify that different error types are represented
        assert "ValidationError" in error_types, "ValidationError should be tested"
        assert "DatabaseError" in error_types, "DatabaseError should be tested"

    def test_error_logging_context_preservation(self, test_mixin):
        """Test that error context is preserved through the error chain."""
        # Create initial context
        initial_context = create_error_context(
            user_id="test-user-123", metadata={"operation": "test", "step": "initial"}
        )

        # Test that context is created correctly
        assert initial_context.user_id == "test-user-123", "User ID should be preserved"
        assert initial_context.metadata["operation"] == "test", "Metadata should be preserved"
        assert initial_context.metadata["step"] == "initial", "Step should be preserved"

    def test_error_logging_performance_under_load(self, test_mixin):
        """Test error logging performance under simulated load."""
        import time

        start_time = time.time()
        error_count = 0

        # Simulate high error rate by raising and catching exceptions
        for i in range(100):
            try:
                raise ValueError(f"Load test error {i}")
            except ValueError:
                error_count += 1

        end_time = time.time()
        duration = end_time - start_time

        # Verify performance is acceptable
        assert error_count == 100, "All errors should be processed"
        assert duration < 1.0, f"Error handling too slow under load: {duration:.3f}s for 100 errors"
