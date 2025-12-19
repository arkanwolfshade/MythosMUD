"""
Tests for Container API endpoints and models.

This module tests the container API request/response models and endpoint logic
for the unified container system covering environmental props, wearable gear,
and corpse storage.

AI Agent: Tests for container API models covering validation, field constraints,
         and request model structure. Created for fresh session execution.
"""


# pylint: disable=redefined-outer-name
# Justification: pytest fixtures redefine names

from uuid import UUID, uuid4

import pytest
from pydantic import ValidationError


# Note: These imports will trigger bcrypt in same session as other tests
# Run in fresh terminal: uv run pytest server/tests/unit/api/test_containers.py -v
@pytest.fixture
def containers_module():
    """Lazily import containers module."""
    from server.api import containers

    return containers


@pytest.fixture
def sample_container_id():
    """Provide sample container UUID."""
    return uuid4()


class TestOpenContainerRequest:
    """Test OpenContainerRequest model validation."""

    def test_valid_open_container_request(self, containers_module, sample_container_id):
        """Test valid open container request."""
        request = containers_module.OpenContainerRequest(container_id=sample_container_id)

        assert request.container_id == sample_container_id
        assert isinstance(request.container_id, UUID)

    def test_open_container_request_requires_container_id(self, containers_module):
        """Test open container request requires container_id."""
        with pytest.raises(ValidationError) as exc_info:
            containers_module.OpenContainerRequest()

        errors = exc_info.value.errors()
        assert any(error["loc"] == ("container_id",) for error in errors)

    def test_open_container_request_validates_uuid_format(self, containers_module):
        """Test container_id must be valid UUID."""
        with pytest.raises(ValidationError) as exc_info:
            containers_module.OpenContainerRequest(container_id="not-a-uuid")

        errors = exc_info.value.errors()
        assert any("uuid" in str(error).lower() for error in errors)


class TestTransferContainerRequest:
    """Test TransferContainerRequest model validation."""

    def test_valid_transfer_to_container(self, containers_module, sample_container_id):
        """Test valid transfer to container request."""
        request = containers_module.TransferContainerRequest(
            container_id=sample_container_id,
            mutation_token="token123",
            direction="to_container",
            stack={"item_id": "sword01", "quantity": 1},
            quantity=1,
        )

        assert request.container_id == sample_container_id
        assert request.direction == "to_container"
        assert request.quantity == 1

    def test_valid_transfer_to_player(self, containers_module, sample_container_id):
        """Test valid transfer to player request."""
        request = containers_module.TransferContainerRequest(
            container_id=sample_container_id,
            mutation_token="token456",
            direction="to_player",
            stack={"item_id": "potion01"},
            quantity=2,
        )

        assert request.direction == "to_player"
        assert request.quantity == 2

    def test_transfer_direction_validation_rejects_invalid(self, containers_module, sample_container_id):
        """Test direction field validates allowed values."""
        with pytest.raises(ValidationError) as exc_info:
            containers_module.TransferContainerRequest(
                container_id=sample_container_id,
                mutation_token="token",
                direction="invalid_direction",
                stack={},
                quantity=1,
            )

        assert any("direction must be" in str(error).lower() for error in exc_info.value.errors())

    def test_transfer_quantity_must_be_positive(self, containers_module, sample_container_id):
        """Test quantity must be >= 1."""
        with pytest.raises(ValidationError) as exc_info:
            containers_module.TransferContainerRequest(
                container_id=sample_container_id,
                mutation_token="token",
                direction="to_container",
                stack={},
                quantity=0,
            )

        errors = exc_info.value.errors()
        assert any(error["loc"] == ("quantity",) for error in errors)

    def test_transfer_requires_all_fields(self, containers_module):
        """Test all required fields must be provided."""
        with pytest.raises(ValidationError) as exc_info:
            containers_module.TransferContainerRequest(container_id=uuid4())

        # Should have errors for missing required fields
        errors = exc_info.value.errors()
        field_names = {error["loc"][0] for error in errors}
        assert "mutation_token" in field_names or "direction" in field_names


class TestCloseContainerRequest:
    """Test CloseContainerRequest model validation."""

    def test_valid_close_container_request(self, containers_module, sample_container_id):
        """Test valid close container request."""
        request = containers_module.CloseContainerRequest(container_id=sample_container_id, mutation_token="token789")

        assert request.container_id == sample_container_id
        assert request.mutation_token == "token789"

    def test_close_container_requires_mutation_token(self, containers_module, sample_container_id):
        """Test mutation_token is required."""
        with pytest.raises(ValidationError) as exc_info:
            containers_module.CloseContainerRequest(container_id=sample_container_id)

        errors = exc_info.value.errors()
        assert any(error["loc"] == ("mutation_token",) for error in errors)


class TestLootAllRequest:
    """Test LootAllRequest model validation."""

    def test_valid_loot_all_request(self, containers_module, sample_container_id):
        """Test valid loot all request."""
        request = containers_module.LootAllRequest(container_id=sample_container_id, mutation_token="loot_token")

        assert request.container_id == sample_container_id
        assert request.mutation_token == "loot_token"

    def test_loot_all_requires_container_id(self, containers_module):
        """Test container_id is required."""
        with pytest.raises(ValidationError) as exc_info:
            containers_module.LootAllRequest(mutation_token="token")

        errors = exc_info.value.errors()
        assert any(error["loc"] == ("container_id",) for error in errors)


class TestContainerRateLimiting:
    """Test container rate limiting configuration."""

    def test_rate_limiter_exists(self, containers_module):
        """Test container rate limiter is configured."""
        assert hasattr(containers_module, "container_rate_limiter")
        assert containers_module.container_rate_limiter is not None

    def test_rate_limiter_has_correct_limits(self, containers_module):
        """Test rate limiter configured with correct limits."""
        limiter = containers_module.container_rate_limiter
        assert limiter.max_requests == 20
        assert limiter.window_seconds == 60
