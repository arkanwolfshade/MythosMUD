"""
Tests for COPPA compliance in container system.

As documented in the restricted archives of Miskatonic University, container
metadata must never contain personal information to ensure COPPA compliance.
"""

from __future__ import annotations

import uuid

import pytest
from pydantic import ValidationError

from server.models.container import ContainerComponent, ContainerSourceType


class TestContainerCOPPACompliance:
    """Test that container metadata does not contain personal information."""

    def test_container_metadata_no_personal_data(self):
        """Test that container metadata does not contain personal information."""
        # Create container with metadata
        container = ContainerComponent(
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            capacity_slots=10,
            metadata={
                "key_item_id": "key_001",
                "description": "A locked chest",
            },
        )

        # Verify metadata does not contain personal information
        metadata = container.metadata

        # Personal information fields that should NOT be present
        personal_data_fields = [
            "email",
            "phone",
            "address",
            "real_name",
            "birth_date",
            "age",
            "location",
            "ip_address",
            "user_agent",
            "session_id",
        ]

        for field in personal_data_fields:
            assert field not in metadata, f"Container metadata should not contain {field}"

    def test_corpse_metadata_no_personal_data(self):
        """Test that corpse container metadata does not contain personal information."""
        owner_id = uuid.uuid4()

        # Create corpse container
        container = ContainerComponent(
            source_type=ContainerSourceType.CORPSE,
            owner_id=owner_id,
            room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            capacity_slots=10,
            metadata={
                "grace_period_seconds": 300,
                "grace_period_start": "2025-01-01T00:00:00Z",
                "decay_seconds": 3600,
            },
        )

        # Verify metadata does not contain personal information
        metadata = container.metadata

        # Personal information fields that should NOT be present
        personal_data_fields = [
            "email",
            "phone",
            "address",
            "real_name",
            "birth_date",
            "age",
            "location",
            "ip_address",
            "user_agent",
            "session_id",
        ]

        for field in personal_data_fields:
            assert field not in metadata, f"Corpse container metadata should not contain {field}"

        # Verify owner_id is UUID, not personal information
        assert isinstance(container.owner_id, uuid.UUID), "owner_id should be UUID, not personal information"

    def test_wearable_container_metadata_no_personal_data(self):
        """Test that wearable container metadata does not contain personal information."""
        entity_id = uuid.uuid4()

        # Create wearable container
        container = ContainerComponent(
            source_type=ContainerSourceType.EQUIPMENT,
            entity_id=entity_id,
            capacity_slots=8,
            metadata={
                "item_instance_id": "inst_backpack_001",
                "item_id": "backpack",
                "item_name": "Leather Backpack",
            },
        )

        # Verify metadata does not contain personal information
        metadata = container.metadata

        # Personal information fields that should NOT be present
        personal_data_fields = [
            "email",
            "phone",
            "address",
            "real_name",
            "birth_date",
            "age",
            "location",
            "ip_address",
            "user_agent",
            "session_id",
        ]

        for field in personal_data_fields:
            assert field not in metadata, f"Wearable container metadata should not contain {field}"

        # Verify entity_id is UUID, not personal information
        assert isinstance(container.entity_id, uuid.UUID), "entity_id should be UUID, not personal information"

    def test_container_metadata_validation_rejects_personal_data(self):
        """Test that container metadata validation rejects personal data fields."""
        # Attempt to create container with personal data in metadata
        with pytest.raises(ValidationError):
            ContainerComponent(
                source_type=ContainerSourceType.ENVIRONMENT,
                room_id="earth_arkhamcity_sanitarium_room_foyer_001",
                capacity_slots=10,
                metadata={
                    "email": "user@example.com",  # Personal data - should be rejected
                    "key_item_id": "key_001",
                },
            )

    def test_container_items_no_personal_data(self):
        """Test that container items do not contain personal information."""
        # Create container with items
        container = ContainerComponent(
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            capacity_slots=10,
            items=[
                {
                    "item_instance_id": "inst_item_001",
                    "prototype_id": "test_item",
                    "item_id": "test_item",
                    "item_name": "Test Item",
                    "slot_type": "backpack",
                    "quantity": 1,
                }
            ],
        )

        # Verify items do not contain personal information
        for item in container.items:
            # Personal information fields that should NOT be present
            personal_data_fields = [
                "email",
                "phone",
                "address",
                "real_name",
                "birth_date",
                "age",
                "location",
                "ip_address",
                "user_agent",
                "session_id",
            ]

            for field in personal_data_fields:
                assert field not in item, f"Container item should not contain {field}"
