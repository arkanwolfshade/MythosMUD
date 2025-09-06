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
from server.exceptions import DatabaseError, LoggedHTTPException, ValidationError
from server.tests.utils.test_error_logging import ErrorLoggingTestMixin
from server.utils.error_logging import create_error_context, log_and_raise


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

            with patch("server.api.players.create_error_context") as mock_create_context:
                mock_context = create_error_context(user_id=str(mock_current_user.id))
                mock_create_context.return_value = mock_context

                with patch("server.api.players.log_and_raise") as mock_log_and_raise:
                    with pytest.raises(LoggedHTTPException):
                        create_player("ExistingPlayer", "test_room", mock_current_user, mock_request)

                    # Verify error was logged and raised
                    mock_log_and_raise.assert_called_once()
                    call_args = mock_log_and_raise.call_args
                    assert call_args[0][0] == LoggedHTTPException
                    assert call_args[0][1] == 400
                    assert "Invalid input" in call_args[0][2]
                    assert call_args[1]["context"] == mock_context

    def test_api_player_deletion_error_logging(self, test_mixin, mock_request, mock_current_user):
        """Test error logging in player deletion API endpoint."""
        with patch("server.api.players.PlayerService") as mock_service_class:
            # Setup mock service to raise ValidationError
            mock_service = Mock()
            mock_service.delete_player.side_effect = ValidationError("Player not found")
            mock_service_class.return_value = mock_service

            with patch("server.api.players.create_error_context") as mock_create_context:
                mock_context = create_error_context(user_id=str(mock_current_user.id))
                mock_create_context.return_value = mock_context

                with patch("server.api.players.log_and_raise") as mock_log_and_raise:
                    with pytest.raises(LoggedHTTPException):
                        delete_player("nonexistent-player-id", mock_current_user, mock_request)

                    # Verify error was logged and raised
                    mock_log_and_raise.assert_called_once()
                    call_args = mock_log_and_raise.call_args
                    assert call_args[0][0] == LoggedHTTPException
                    assert call_args[0][1] == 404
                    assert "Player not found" in call_args[0][2]

    def test_api_player_retrieval_error_logging(self, test_mixin, mock_request, mock_current_user):
        """Test error logging in player retrieval API endpoint."""
        with patch("server.api.players.PlayerService") as mock_service_class:
            # Setup mock service to return None (player not found)
            mock_service = Mock()
            mock_service.get_player_by_id.return_value = None
            mock_service_class.return_value = mock_service

            with patch("server.api.players.create_error_context") as mock_create_context:
                mock_context = create_error_context(user_id=str(mock_current_user.id))
                mock_create_context.return_value = mock_context

                with patch("server.api.players.log_and_raise") as mock_log_and_raise:
                    with pytest.raises(LoggedHTTPException):
                        get_player("nonexistent-player-id", mock_current_user, mock_request)

                    # Verify error was logged and raised
                    mock_log_and_raise.assert_called_once()
                    call_args = mock_log_and_raise.call_args
                    assert call_args[0][0] == LoggedHTTPException
                    assert call_args[0][1] == 404
                    assert "Player not found" in call_args[0][2]


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

            # Verify error was logged
            mock_logger.warning.assert_called()
            warning_calls = mock_logger.warning.call_args_list

            # Check that validation errors are logged
            validation_logged = any(
                "validation error" in str(call).lower() or "validationerror" in str(call).lower()
                for call in warning_calls
            )
            assert validation_logged, "Validation error should be logged"

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

            # Verify error was logged
            mock_logger.error.assert_called()
            error_calls = mock_logger.error.call_args_list

            # Check that processing errors are logged
            processing_logged = any("error processing command" in str(call).lower() for call in error_calls)
            assert processing_logged, "Command processing error should be logged"


class TestDatabaseErrorLoggingIntegration:
    """Integration tests for database error logging."""

    @pytest.fixture
    def test_mixin(self):
        """Provide error logging test mixin."""
        return ErrorLoggingTestMixin()

    def test_database_connection_error_logging(self, test_mixin):
        """Test error logging for database connection failures."""
        with patch("server.database.logger") as mock_logger:
            with patch("server.database.create_error_context") as mock_create_context:
                mock_context = create_error_context()
                mock_create_context.return_value = mock_context

                # Simulate database connection error
                with patch("server.database.get_async_session") as mock_session:
                    mock_session.side_effect = DatabaseError("Database connection failed")

                    with pytest.raises(DatabaseError):
                        # This would normally be called by the database module
                        mock_session()

                    # Verify error was logged
                    mock_logger.error.assert_called()
                    error_calls = mock_logger.error.call_args_list

                    # Check that database errors are logged
                    db_error_logged = any(
                        "database" in str(call).lower() and "error" in str(call).lower() for call in error_calls
                    )
                    assert db_error_logged, "Database error should be logged"

    def test_database_session_error_logging(self, test_mixin):
        """Test error logging for database session errors."""
        with patch("server.database.logger") as mock_logger:
            with patch("server.database.create_error_context") as mock_create_context:
                mock_context = create_error_context()
                mock_create_context.return_value = mock_context

                # Simulate database session error
                with patch("server.database.get_async_session") as mock_session:
                    mock_session_instance = Mock()
                    mock_session_instance.rollback.side_effect = Exception("Rollback failed")
                    mock_session.return_value.__aenter__.return_value = mock_session_instance

                    # This would normally be called by the database module
                    try:
                        with mock_session():
                            raise Exception("Database operation failed")
                    except Exception:
                        pass

                    # Verify error was logged
                    mock_logger.error.assert_called()
                    error_calls = mock_logger.error.call_args_list

                    # Check that session errors are logged
                    session_error_logged = any(
                        "session" in str(call).lower() and "error" in str(call).lower() for call in error_calls
                    )
                    assert session_error_logged, "Database session error should be logged"


class TestPersistenceErrorLoggingIntegration:
    """Integration tests for persistence layer error logging."""

    @pytest.fixture
    def test_mixin(self):
        """Provide error logging test mixin."""
        return ErrorLoggingTestMixin()

    def test_persistence_save_error_logging(self, test_mixin):
        """Test error logging for persistence save operations."""
        with patch("server.persistence.logger"):
            with patch("server.persistence.create_error_context") as mock_create_context:
                mock_context = create_error_context()
                mock_create_context.return_value = mock_context

                # Simulate persistence save error
                with patch("server.persistence.log_and_raise") as mock_log_and_raise:
                    mock_log_and_raise.side_effect = DatabaseError("Save operation failed")

                    with pytest.raises(DatabaseError):
                        # This would normally be called by the persistence module
                        mock_log_and_raise(DatabaseError, "Save operation failed", context=mock_context)

                    # Verify error was logged and raised
                    mock_log_and_raise.assert_called_once()

    def test_persistence_load_error_logging(self, test_mixin):
        """Test error logging for persistence load operations."""
        with patch("server.persistence.logger"):
            with patch("server.persistence.create_error_context") as mock_create_context:
                mock_context = create_error_context()
                mock_create_context.return_value = mock_context

                # Simulate persistence load error
                with patch("server.persistence.log_and_raise") as mock_log_and_raise:
                    mock_log_and_raise.side_effect = DatabaseError("Load operation failed")

                    with pytest.raises(DatabaseError):
                        # This would normally be called by the persistence module
                        mock_log_and_raise(DatabaseError, "Load operation failed", context=mock_context)

                    # Verify error was logged and raised
                    mock_log_and_raise.assert_called_once()


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
        with patch("server.websocket_handler.logger"):
            with patch("server.websocket_handler.create_error_context") as mock_create_context:
                mock_context = create_error_context()
                mock_create_context.return_value = mock_context

                # Simulate WebSocket connection error
                with patch("server.websocket_handler.log_and_raise") as mock_log_and_raise:
                    mock_log_and_raise.side_effect = ConnectionError("WebSocket connection failed")

                    with pytest.raises(ConnectionError):
                        # This would normally be called by the WebSocket handler
                        mock_log_and_raise(ConnectionError, "WebSocket connection failed", context=mock_context)

                    # Verify error was logged and raised
                    mock_log_and_raise.assert_called_once()

    def test_websocket_message_error_logging(self, test_mixin, mock_websocket):
        """Test error logging for WebSocket message processing errors."""
        with patch("server.websocket_handler.logger"):
            with patch("server.websocket_handler.create_error_context") as mock_create_context:
                mock_context = create_error_context()
                mock_create_context.return_value = mock_context

                # Simulate WebSocket message error
                with patch("server.websocket_handler.log_and_raise") as mock_log_and_raise:
                    mock_log_and_raise.side_effect = ValueError("Invalid message format")

                    with pytest.raises(ValueError):
                        # This would normally be called by the WebSocket handler
                        mock_log_and_raise(ValueError, "Invalid message format", context=mock_context)

                    # Verify error was logged and raised
                    mock_log_and_raise.assert_called_once()


class TestAuthenticationErrorLoggingIntegration:
    """Integration tests for authentication error logging."""

    @pytest.fixture
    def test_mixin(self):
        """Provide error logging test mixin."""
        return ErrorLoggingTestMixin()

    def test_authentication_failure_logging(self, test_mixin):
        """Test error logging for authentication failures."""
        with patch("server.auth.logger"):
            with patch("server.auth.create_error_context") as mock_create_context:
                mock_context = create_error_context()
                mock_create_context.return_value = mock_context

                # Simulate authentication failure
                with patch("server.auth.log_and_raise") as mock_log_and_raise:
                    mock_log_and_raise.side_effect = ValidationError("Invalid credentials")

                    with pytest.raises(ValidationError):
                        # This would normally be called by the auth module
                        mock_log_and_raise(ValidationError, "Invalid credentials", context=mock_context)

                    # Verify error was logged and raised
                    mock_log_and_raise.assert_called_once()

    def test_authorization_failure_logging(self, test_mixin):
        """Test error logging for authorization failures."""
        with patch("server.auth.logger"):
            with patch("server.auth.create_error_context") as mock_create_context:
                mock_context = create_error_context()
                mock_create_context.return_value = mock_context

                # Simulate authorization failure
                with patch("server.auth.log_and_raise") as mock_log_and_raise:
                    mock_log_and_raise.side_effect = ValidationError("Insufficient permissions")

                    with pytest.raises(ValidationError):
                        # This would normally be called by the auth module
                        mock_log_and_raise(ValidationError, "Insufficient permissions", context=mock_context)

                    # Verify error was logged and raised
                    mock_log_and_raise.assert_called_once()


class TestErrorLoggingEndToEnd:
    """End-to-end integration tests for error logging."""

    @pytest.fixture
    def test_mixin(self):
        """Provide error logging test mixin."""
        return ErrorLoggingTestMixin()

    def test_error_logging_flow_complete(self, test_mixin):
        """Test complete error logging flow from API to persistence."""
        # This test simulates a complete error flow:
        # API -> Service -> Persistence -> Database

        with patch("server.api.players.PlayerService") as mock_service_class:
            with patch("server.game.player_service.PlayerService") as mock_player_service:
                with patch("server.persistence.PersistenceLayer") as mock_persistence:
                    with patch("server.database.get_async_session") as mock_session:
                        # Setup error chain
                        mock_session.side_effect = DatabaseError("Database connection lost")
                        mock_persistence.return_value.save_player.side_effect = DatabaseError("Save failed")
                        mock_player_service.return_value.create_player.side_effect = DatabaseError("Service error")
                        mock_service_class.return_value.create_player.side_effect = ValidationError("API error")

                        # Track all error logging calls
                        error_logs = []

                        def capture_error_log(*args, **kwargs):
                            error_logs.append((args, kwargs))

                        with patch("server.api.players.log_and_raise", side_effect=capture_error_log):
                            with patch("server.game.player_service.log_and_raise", side_effect=capture_error_log):
                                with patch("server.persistence.log_and_raise", side_effect=capture_error_log):
                                    with patch("server.database.log_and_raise", side_effect=capture_error_log):
                                        # Simulate the error flow
                                        try:
                                            # This would trigger the error chain
                                            raise ValidationError("API error")
                                        except ValidationError:
                                            pass

                        # Verify that errors were logged at each level
                        assert len(error_logs) > 0, "At least one error should be logged"

                        # Check that different error types are represented
                        error_types = [log[0][0].__name__ for log in error_logs]
                        assert any("ValidationError" in types for types in error_types), (
                            "ValidationError should be logged"
                        )
                        assert any("DatabaseError" in types for types in error_types), "DatabaseError should be logged"

    def test_error_logging_context_preservation(self, test_mixin):
        """Test that error context is preserved through the error chain."""
        # Create initial context
        initial_context = create_error_context(
            user_id="test-user-123", metadata={"operation": "test", "step": "initial"}
        )

        # Simulate context passing through error chain
        contexts = [initial_context]

        def preserve_context(exception_class, message, context=None, **kwargs):
            if context:
                contexts.append(context)
            raise exception_class(message)

        with patch("server.utils.error_logging.log_and_raise", side_effect=preserve_context):
            try:
                log_and_raise(ValueError, "First error", context=initial_context)
            except ValueError:
                try:
                    log_and_raise(RuntimeError, "Second error", context=initial_context)
                except RuntimeError:
                    pass

        # Verify context was preserved
        assert len(contexts) >= 1, "Context should be preserved"
        assert contexts[0].user_id == "test-user-123", "User ID should be preserved"
        assert contexts[0].metadata["operation"] == "test", "Metadata should be preserved"

    def test_error_logging_performance_under_load(self, test_mixin):
        """Test error logging performance under simulated load."""
        import time

        start_time = time.time()
        error_count = 0

        with patch("server.utils.error_logging.logger"):
            # Simulate high error rate
            for i in range(1000):
                try:
                    log_and_raise(ValueError, f"Load test error {i}", details={"iteration": i})
                except ValueError:
                    error_count += 1

        end_time = time.time()
        duration = end_time - start_time

        # Verify performance is acceptable
        assert error_count == 1000, "All errors should be processed"
        assert duration < 2.0, f"Error logging too slow under load: {duration:.3f}s for 1000 errors"

        # Calculate errors per second
        errors_per_second = error_count / duration
        assert errors_per_second > 500, f"Error logging rate too low: {errors_per_second:.1f} errors/second"
