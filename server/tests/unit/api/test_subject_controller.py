"""
Tests for NATS Subject Management API endpoints.

This module tests the subject management API endpoints which provide
observability and control over NATS subject patterns and validation.

Following the academic rigor outlined in the Pnakotic Manuscripts of Testing Methodology.

AI: Tests written following TDD approach - before implementation.
AI: Tests cover health endpoints, admin endpoints, and error handling.
"""

import uuid
from types import MethodType
from unittest.mock import Mock

import pytest

from server.exceptions import LoggedHTTPException
from server.services.nats_subject_manager import NATSSubjectManager


def _mock_getitem(self, key):
    """Helper function to make mock support dictionary access for all attributes."""
    return getattr(self, key)


@pytest.fixture
def mock_current_user():
    """Mock authenticated user for testing."""
    user = Mock()
    user.id = str(uuid.uuid4())
    user.username = "testuser"
    user.is_admin = False
    # Make the mock support dictionary access for all attributes
    user.__getitem__ = MethodType(_mock_getitem, user)
    return user


@pytest.fixture
def mock_admin_user():
    """Mock admin user for testing."""
    user = Mock()
    user.id = str(uuid.uuid4())
    user.username = "admin"
    user.is_admin = True
    user.__getitem__ = MethodType(_mock_getitem, user)
    return user


@pytest.fixture
def mock_subject_manager():
    """Mock NATSSubjectManager for testing."""
    manager = Mock(spec=NATSSubjectManager)
    manager.get_performance_metrics = Mock()
    manager.validate_subject = Mock()
    manager.get_all_patterns = Mock()
    manager.register_pattern = Mock()
    manager.patterns = {}  # Add patterns attribute for health endpoint
    manager._cache_enabled = True
    manager._strict_validation = False
    return manager


class TestSubjectHealthEndpoint:
    """Test suite for GET /api/health/nats/subjects endpoint."""

    @pytest.mark.asyncio
    async def test_get_subject_statistics_success(self, mock_subject_manager):
        """Test successful retrieval of subject statistics."""
        # Arrange
        mock_metrics = {
            "validation": {
                "total_count": 100,
                "success_count": 95,
                "failure_count": 5,
                "success_rate": 0.95,
                "avg_time_ms": 0.5,
                "p95_time_ms": 1.2,
            },
            "cache": {"hits": 80, "misses": 20, "hit_rate": 0.8},
            "build": {
                "total_count": 50,
                "success_count": 48,
                "failure_count": 2,
                "success_rate": 0.96,
                "avg_time_ms": 0.3,
                "p95_time_ms": 0.8,
            },
            "errors": {
                "pattern_not_found": 1,
                "missing_parameter": 1,
                "validation_errors": 3,
                "total_errors": 5,
            },
        }
        mock_subject_manager.get_performance_metrics.return_value = mock_metrics

        # Import endpoint function
        from server.api.admin.subject_controller import get_subject_statistics

        # Act
        response = await get_subject_statistics(subject_manager=mock_subject_manager)

        # Assert
        assert response["status"] == "healthy"
        assert response["metrics"] == mock_metrics
        assert "patterns_registered" in response
        mock_subject_manager.get_performance_metrics.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_subject_statistics_with_no_metrics(self, mock_subject_manager):
        """Test endpoint when metrics are disabled."""
        # Arrange
        mock_subject_manager.get_performance_metrics.return_value = None

        from server.api.admin.subject_controller import get_subject_statistics

        # Act
        response = await get_subject_statistics(subject_manager=mock_subject_manager)

        # Assert
        assert response["status"] == "healthy"
        assert response["metrics"] is None
        assert "patterns_registered" in response

    @pytest.mark.asyncio
    async def test_get_subject_statistics_error_handling(self, mock_subject_manager):
        """Test error handling when metrics retrieval fails."""
        # Arrange
        mock_subject_manager.get_performance_metrics.side_effect = Exception("Metrics error")

        from server.api.admin.subject_controller import get_subject_statistics

        # Act & Assert
        with pytest.raises(LoggedHTTPException) as exc_info:
            await get_subject_statistics(subject_manager=mock_subject_manager)

        assert exc_info.value.status_code == 500


class TestValidateSubjectEndpoint:
    """Test suite for POST /api/admin/nats/subjects/validate endpoint."""

    @pytest.mark.asyncio
    async def test_validate_subject_valid_subject(self, mock_admin_user, mock_subject_manager):
        """Test validation of a valid subject."""
        # Arrange
        mock_subject_manager.validate_subject.return_value = True
        test_subject = "chat.say.room.arkham_1"

        from server.api.admin.subject_controller import ValidateSubjectRequest, validate_subject

        request = ValidateSubjectRequest(subject=test_subject)

        # Act
        response = await validate_subject(request, current_user=mock_admin_user, subject_manager=mock_subject_manager)

        # Assert
        assert response["subject"] == test_subject
        assert response["is_valid"] is True
        assert "validation_time_ms" in response
        mock_subject_manager.validate_subject.assert_called_once_with(test_subject)

    @pytest.mark.asyncio
    async def test_validate_subject_invalid_subject(self, mock_admin_user, mock_subject_manager):
        """Test validation of an invalid subject."""
        # Arrange
        mock_subject_manager.validate_subject.return_value = False
        test_subject = "invalid..subject"

        from server.api.admin.subject_controller import ValidateSubjectRequest, validate_subject

        request = ValidateSubjectRequest(subject=test_subject)

        # Act
        response = await validate_subject(request, current_user=mock_admin_user, subject_manager=mock_subject_manager)

        # Assert
        assert response["subject"] == test_subject
        assert response["is_valid"] is False
        assert "validation_time_ms" in response

    @pytest.mark.asyncio
    async def test_validate_subject_non_admin_forbidden(self, mock_current_user, _mock_subject_manager):
        """Test that non-admin users cannot validate subjects via dependency check."""
        # Arrange
        from server.api.admin.subject_controller import require_admin_user

        # Act & Assert - Test the dependency function directly
        with pytest.raises(LoggedHTTPException) as exc_info:
            require_admin_user(current_user=mock_current_user)

        assert exc_info.value.status_code == 403

    @pytest.mark.asyncio
    async def test_validate_subject_empty_subject(self, mock_admin_user, mock_subject_manager):
        """Test validation of empty subject string."""
        # Arrange
        mock_subject_manager.validate_subject.return_value = False  # Empty subjects are invalid

        from server.api.admin.subject_controller import ValidateSubjectRequest, validate_subject

        request = ValidateSubjectRequest(subject="")

        # Act
        response = await validate_subject(request, current_user=mock_admin_user, subject_manager=mock_subject_manager)

        # Assert
        assert response["is_valid"] is False


class TestGetPatternsEndpoint:
    """Test suite for GET /api/admin/nats/subjects/patterns endpoint."""

    @pytest.mark.asyncio
    async def test_get_patterns_success(self, mock_admin_user, mock_subject_manager):
        """Test successful retrieval of all patterns."""
        # Arrange
        mock_patterns = {
            "chat_say_room": {
                "name": "chat_say_room",
                "pattern": "chat.say.room.{room_id}",
                "required_params": ["room_id"],
                "description": "Room-level say messages",
            },
            "chat_global": {
                "name": "chat_global",
                "pattern": "chat.global",
                "required_params": [],
                "description": "Global chat messages",
            },
        }
        mock_subject_manager.get_all_patterns.return_value = mock_patterns

        from server.api.admin.subject_controller import get_patterns

        # Act
        response = await get_patterns(current_user=mock_admin_user, subject_manager=mock_subject_manager)

        # Assert
        assert response["patterns"] == mock_patterns
        assert response["total_count"] == 2
        mock_subject_manager.get_all_patterns.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_patterns_non_admin_forbidden(self, mock_current_user, _mock_subject_manager):
        """Test that non-admin users cannot retrieve patterns via dependency check."""
        # Arrange
        from server.api.admin.subject_controller import require_admin_user

        # Act & Assert - Test the dependency function directly
        with pytest.raises(LoggedHTTPException) as exc_info:
            require_admin_user(current_user=mock_current_user)

        assert exc_info.value.status_code == 403

    @pytest.mark.asyncio
    async def test_get_patterns_error_handling(self, mock_admin_user, mock_subject_manager):
        """Test error handling when pattern retrieval fails."""
        # Arrange
        mock_subject_manager.get_all_patterns.side_effect = Exception("Pattern error")

        from server.api.admin.subject_controller import get_patterns

        # Act & Assert
        with pytest.raises(LoggedHTTPException) as exc_info:
            await get_patterns(current_user=mock_admin_user, subject_manager=mock_subject_manager)

        assert exc_info.value.status_code == 500


class TestRegisterPatternEndpoint:
    """Test suite for POST /api/admin/nats/subjects/patterns endpoint."""

    @pytest.mark.asyncio
    async def test_register_pattern_success(self, mock_admin_user, mock_subject_manager):
        """Test successful pattern registration."""
        # Arrange
        from server.api.admin.subject_controller import RegisterPatternRequest, register_pattern

        request = RegisterPatternRequest(
            name="chat_party_group",
            pattern="chat.party.group.{party_id}",
            required_params=["party_id"],
            description="Party group messages",
        )

        # Act
        response = await register_pattern(request, current_user=mock_admin_user, subject_manager=mock_subject_manager)

        # Assert
        assert response["success"] is True
        assert response["pattern_name"] == "chat_party_group"
        assert response["message"] == "Pattern registered successfully"
        mock_subject_manager.register_pattern.assert_called_once_with(
            name="chat_party_group",
            pattern="chat.party.group.{party_id}",
            required_params=["party_id"],
            description="Party group messages",
        )

    @pytest.mark.asyncio
    async def test_register_pattern_non_admin_forbidden(self, mock_current_user, _mock_subject_manager):
        """Test that non-admin users cannot register patterns via dependency check."""
        # Arrange
        from server.api.admin.subject_controller import require_admin_user

        # Act & Assert - Test the dependency function directly
        with pytest.raises(LoggedHTTPException) as exc_info:
            require_admin_user(current_user=mock_current_user)

        assert exc_info.value.status_code == 403

    @pytest.mark.asyncio
    async def test_register_pattern_duplicate_name(self, mock_admin_user, mock_subject_manager):
        """Test that duplicate pattern names are rejected."""
        # Arrange
        from server.services.nats_subject_manager import InvalidPatternError

        mock_subject_manager.register_pattern.side_effect = InvalidPatternError("Pattern already registered")

        from server.api.admin.subject_controller import RegisterPatternRequest, register_pattern

        request = RegisterPatternRequest(
            name="chat_global",  # Already exists
            pattern="chat.global.duplicate",
            required_params=[],
            description="Duplicate",
        )

        # Act & Assert
        with pytest.raises(LoggedHTTPException) as exc_info:
            await register_pattern(request, current_user=mock_admin_user, subject_manager=mock_subject_manager)

        assert exc_info.value.status_code == 400

    @pytest.mark.asyncio
    async def test_register_pattern_invalid_format(self, mock_admin_user, mock_subject_manager):
        """Test that invalid pattern formats are rejected."""
        # Arrange
        from server.services.nats_subject_manager import InvalidPatternError

        mock_subject_manager.register_pattern.side_effect = InvalidPatternError("Invalid pattern format")

        from server.api.admin.subject_controller import RegisterPatternRequest, register_pattern

        request = RegisterPatternRequest(
            name="chat_invalid", pattern="invalid..pattern", required_params=[], description="Invalid"
        )

        # Act & Assert
        with pytest.raises(LoggedHTTPException) as exc_info:
            await register_pattern(request, current_user=mock_admin_user, subject_manager=mock_subject_manager)

        assert exc_info.value.status_code == 400


class TestAdminPermissionValidation:
    """Test suite for admin permission validation across all endpoints."""

    @pytest.mark.asyncio
    async def test_validate_subject_requires_admin(self, mock_current_user, mock_subject_manager):
        """Test that validate endpoint requires admin permissions via dependency."""
        from server.api.admin.subject_controller import require_admin_user

        # Act & Assert - Test the dependency function directly
        with pytest.raises(LoggedHTTPException) as exc_info:
            require_admin_user(current_user=mock_current_user)

        assert exc_info.value.status_code == 403
        assert "admin" in str(exc_info.value.detail).lower()

    @pytest.mark.asyncio
    async def test_get_patterns_requires_admin(self, mock_current_user, mock_subject_manager):
        """Test that get patterns endpoint requires admin permissions via dependency."""
        from server.api.admin.subject_controller import require_admin_user

        # Act & Assert - Test the dependency function directly
        with pytest.raises(LoggedHTTPException) as exc_info:
            require_admin_user(current_user=mock_current_user)

        assert exc_info.value.status_code == 403

    @pytest.mark.asyncio
    async def test_register_pattern_requires_admin(self, mock_current_user, mock_subject_manager):
        """Test that register pattern endpoint requires admin permissions via dependency."""
        from server.api.admin.subject_controller import require_admin_user

        # Act & Assert - Test the dependency function directly
        with pytest.raises(LoggedHTTPException) as exc_info:
            require_admin_user(current_user=mock_current_user)

        assert exc_info.value.status_code == 403


class TestRequestModels:
    """Test suite for API request models."""

    def test_validate_subject_request_model(self) -> None:
        """Test ValidateSubjectRequest model validation."""
        from server.api.admin.subject_controller import ValidateSubjectRequest

        # Valid request
        request = ValidateSubjectRequest(subject="chat.say.room.arkham_1")
        assert request.subject == "chat.say.room.arkham_1"

        # Empty subject
        request = ValidateSubjectRequest(subject="")
        assert request.subject == ""

    def test_register_pattern_request_model(self) -> None:
        """Test RegisterPatternRequest model validation."""
        from server.api.admin.subject_controller import RegisterPatternRequest

        # Valid request
        request = RegisterPatternRequest(
            name="chat_test", pattern="chat.test.{id}", required_params=["id"], description="Test pattern"
        )
        assert request.name == "chat_test"
        assert request.pattern == "chat.test.{id}"
        assert request.required_params == ["id"]
        assert request.description == "Test pattern"

        # Minimal request
        request = RegisterPatternRequest(name="test", pattern="test.pattern", required_params=[])
        assert request.description == ""  # Default value


class TestResponseFormats:
    """Test suite for API response formats."""

    @pytest.mark.asyncio
    async def test_health_endpoint_response_format(self, mock_subject_manager):
        """Test that health endpoint returns correctly formatted response."""
        # Arrange
        mock_subject_manager.get_performance_metrics.return_value = {
            "validation": {"total_count": 0},
            "cache": {"hits": 0},
            "build": {"total_count": 0},
            "errors": {"total_errors": 0},
        }

        from server.api.admin.subject_controller import get_subject_statistics

        # Act
        response = await get_subject_statistics(subject_manager=mock_subject_manager)

        # Assert - Verify response structure
        assert "status" in response
        assert "metrics" in response
        assert "patterns_registered" in response
        assert isinstance(response["status"], str)
        assert isinstance(response["patterns_registered"], int)

    @pytest.mark.asyncio
    async def test_validate_endpoint_response_format(self, mock_admin_user, mock_subject_manager):
        """Test that validate endpoint returns correctly formatted response."""
        # Arrange
        mock_subject_manager.validate_subject.return_value = True

        from server.api.admin.subject_controller import ValidateSubjectRequest, validate_subject

        request = ValidateSubjectRequest(subject="chat.say.room.test")

        # Act
        response = await validate_subject(request, current_user=mock_admin_user, subject_manager=mock_subject_manager)

        # Assert - Verify response structure
        assert "subject" in response
        assert "is_valid" in response
        assert "validation_time_ms" in response
        assert isinstance(response["subject"], str)
        assert isinstance(response["is_valid"], bool)
        assert isinstance(response["validation_time_ms"], float)

    @pytest.mark.asyncio
    async def test_patterns_endpoint_response_format(self, mock_admin_user, mock_subject_manager):
        """Test that patterns endpoint returns correctly formatted response."""
        # Arrange
        mock_subject_manager.get_all_patterns.return_value = {}

        from server.api.admin.subject_controller import get_patterns

        # Act
        response = await get_patterns(current_user=mock_admin_user, subject_manager=mock_subject_manager)

        # Assert - Verify response structure
        assert "patterns" in response
        assert "total_count" in response
        assert isinstance(response["patterns"], dict)
        assert isinstance(response["total_count"], int)

    @pytest.mark.asyncio
    async def test_register_endpoint_response_format(self, mock_admin_user, mock_subject_manager):
        """Test that register endpoint returns correctly formatted response."""
        # Arrange
        from server.api.admin.subject_controller import RegisterPatternRequest, register_pattern

        request = RegisterPatternRequest(name="test", pattern="test.{id}", required_params=["id"])

        # Act
        response = await register_pattern(request, current_user=mock_admin_user, subject_manager=mock_subject_manager)

        # Assert - Verify response structure
        assert "success" in response
        assert "pattern_name" in response
        assert "message" in response
        assert isinstance(response["success"], bool)
        assert isinstance(response["pattern_name"], str)
        assert isinstance(response["message"], str)


class TestErrorHandling:
    """Test suite for comprehensive error handling."""

    @pytest.mark.asyncio
    async def test_health_endpoint_handles_internal_errors(self, mock_subject_manager):
        """Test that internal errors return 500 status."""
        # Arrange
        mock_subject_manager.get_performance_metrics.side_effect = RuntimeError("Internal error")

        from server.api.admin.subject_controller import get_subject_statistics

        # Act & Assert
        with pytest.raises(LoggedHTTPException) as exc_info:
            await get_subject_statistics(subject_manager=mock_subject_manager)

        assert exc_info.value.status_code == 500

    @pytest.mark.asyncio
    async def test_validate_endpoint_handles_validation_errors(self, mock_admin_user, mock_subject_manager):
        """Test that validation errors are properly handled."""
        # Arrange
        mock_subject_manager.validate_subject.side_effect = Exception("Validation failed")

        from server.api.admin.subject_controller import ValidateSubjectRequest, validate_subject

        request = ValidateSubjectRequest(subject="test")

        # Act & Assert
        with pytest.raises(LoggedHTTPException) as exc_info:
            await validate_subject(request, current_user=mock_admin_user, subject_manager=mock_subject_manager)

        assert exc_info.value.status_code == 500

    @pytest.mark.asyncio
    async def test_register_endpoint_handles_registration_errors(self, mock_admin_user, mock_subject_manager):
        """Test that registration errors are properly handled."""
        # Arrange
        mock_subject_manager.register_pattern.side_effect = Exception("Registration failed")

        from server.api.admin.subject_controller import RegisterPatternRequest, register_pattern

        request = RegisterPatternRequest(name="test", pattern="test.{id}", required_params=["id"])

        # Act & Assert
        with pytest.raises(LoggedHTTPException) as exc_info:
            await register_pattern(request, current_user=mock_admin_user, subject_manager=mock_subject_manager)

        assert exc_info.value.status_code == 500


class TestDependencyInjection:
    """Test suite for dependency injection integration."""

    @pytest.mark.asyncio
    async def test_subject_manager_dependency_injection(self, _mock_admin_user):
        """Test that subject manager can be injected via FastAPI dependency."""
        # This test verifies the dependency function exists and works
        from server.api.admin.subject_controller import get_subject_manager_dependency

        # Act
        manager = get_subject_manager_dependency()

        # Assert
        assert manager is not None
        assert isinstance(manager, NATSSubjectManager)

    @pytest.mark.asyncio
    async def test_admin_user_dependency_injection(self) -> None:
        """Test that admin user validation works via dependency injection."""
        # This test verifies the dependency function exists and enforces admin check
        from server.api.admin.subject_controller import require_admin_user

        # Mock admin user
        admin_user = Mock()
        admin_user.is_admin = True

        # Act - should not raise
        result = require_admin_user(admin_user)

        # Assert
        assert result == admin_user

    @pytest.mark.asyncio
    async def test_admin_user_dependency_rejects_non_admin(self) -> None:
        """Test that admin dependency rejects non-admin users."""
        from server.api.admin.subject_controller import require_admin_user

        # Mock non-admin user
        regular_user = Mock()
        regular_user.is_admin = False

        # Act & Assert
        with pytest.raises(LoggedHTTPException) as exc_info:
            require_admin_user(regular_user)

        assert exc_info.value.status_code == 403
