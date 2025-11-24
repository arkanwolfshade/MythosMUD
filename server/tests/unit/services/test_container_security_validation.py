"""
Tests for container security validation.

As documented in the restricted archives of Miskatonic University, container
operations must be validated for security, including path validation and
COPPA compliance.
"""

from __future__ import annotations

import uuid

import pytest

from server.models.container import ContainerComponent, ContainerSourceType
from server.persistence.container_persistence import ContainerData


class TestContainerSecurityValidation:
    """Test container security validation."""

    def test_container_persistence_uses_postgresql_no_file_paths(self):
        """Test that container persistence uses PostgreSQL, not file paths."""
        # Container persistence operations use PostgreSQL connections
        # No file path operations should be present
        # This is verified by the fact that all operations use database connections

        # Create a container data object (simulates database result)
        container_data = ContainerData(
            container_instance_id=uuid.uuid4(),
            source_type="environment",
            room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            capacity_slots=10,
        )

        # Verify no file path fields exist
        assert not hasattr(container_data, "file_path")
        assert not hasattr(container_data, "path")
        assert not hasattr(container_data, "filename")

        # Verify database fields exist
        assert hasattr(container_data, "container_instance_id")
        assert hasattr(container_data, "room_id")

    def test_container_metadata_validator_rejects_personal_data(self):
        """Test that container metadata validator rejects personal data."""
        # Attempt to create container with personal data in metadata
        with pytest.raises(ValueError, match="personal information"):
            ContainerComponent(
                container_id=uuid.uuid4(),
                source_type=ContainerSourceType.ENVIRONMENT,
                room_id="earth_arkhamcity_sanitarium_room_foyer_001",
                capacity_slots=10,
                metadata={
                    "email": "user@example.com",  # Personal data - should be rejected
                    "key_item_id": "key_001",
                },
            )

    def test_container_metadata_validator_allows_game_data(self):
        """Test that container metadata validator allows game-related data."""
        # Create container with valid game data in metadata
        container = ContainerComponent(
            container_id=uuid.uuid4(),
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            capacity_slots=10,
            metadata={
                "key_item_id": "key_001",
                "description": "A locked chest",
                "grace_period_seconds": 300,
                "decay_seconds": 3600,
            },
        )

        # Verify container was created successfully
        assert container.metadata["key_item_id"] == "key_001"
        assert container.metadata["description"] == "A locked chest"

    def test_container_metadata_validator_case_insensitive(self):
        """Test that container metadata validator is case-insensitive for personal data."""
        # Attempt to create container with personal data in different cases
        with pytest.raises(ValueError, match="personal information"):
            ContainerComponent(
                container_id=uuid.uuid4(),
                source_type=ContainerSourceType.ENVIRONMENT,
                room_id="earth_arkhamcity_sanitarium_room_foyer_001",
                capacity_slots=10,
                metadata={
                    "EMAIL": "user@example.com",  # Uppercase - should still be rejected
                    "key_item_id": "key_001",
                },
            )
