"""
Tests for ContainerComponent Pydantic model.

As documented in the restricted archives of Miskatonic University, container
components require thorough validation to ensure proper representation of
investigator artifacts and forbidden containers.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta

import pytest
from pydantic import ValidationError

from server.models.container import ContainerComponent, ContainerLockState, ContainerSourceType


class TestContainerComponentValidation:
    """Test ContainerComponent validation."""

    def test_create_environment_container(self):
        """Test creating an environmental container component."""
        container = ContainerComponent(
            container_id=uuid.uuid4(),
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            capacity_slots=8,
        )

        assert container.source_type == ContainerSourceType.ENVIRONMENT
        assert container.room_id == "earth_arkhamcity_sanitarium_room_foyer_001"
        assert container.capacity_slots == 8
        assert container.lock_state == ContainerLockState.UNLOCKED
        assert container.items == []
        assert container.owner_id is None
        assert container.entity_id is None

    def test_create_corpse_container(self):
        """Test creating a corpse container component."""
        owner_id = uuid.uuid4()
        decay_at = datetime.now(UTC) + timedelta(hours=1)

        container = ContainerComponent(
            container_id=uuid.uuid4(),
            source_type=ContainerSourceType.CORPSE,
            owner_id=owner_id,
            room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            capacity_slots=20,
            decay_at=decay_at,
        )

        assert container.source_type == ContainerSourceType.CORPSE
        assert container.owner_id == owner_id
        assert container.decay_at == decay_at
        assert container.capacity_slots == 20

    def test_create_equipment_container(self):
        """Test creating a wearable equipment container component."""
        entity_id = uuid.uuid4()

        container = ContainerComponent(
            container_id=uuid.uuid4(),
            source_type=ContainerSourceType.EQUIPMENT,
            entity_id=entity_id,
            capacity_slots=10,
        )

        assert container.source_type == ContainerSourceType.EQUIPMENT
        assert container.entity_id == entity_id
        assert container.room_id is None
        assert container.owner_id is None

    def test_container_with_items(self):
        """Test creating a container with initial items."""
        items = [
            {
                "item_instance_id": "inst_001",
                "prototype_id": "elder_sign",
                "item_id": "elder_sign",
                "item_name": "Elder Sign",
                "slot_type": "backpack",
                "quantity": 1,
            },
            {
                "item_instance_id": "inst_002",
                "prototype_id": "tome_of_forbidden_knowledge",
                "item_id": "tome_of_forbidden_knowledge",
                "item_name": "Tome of Forbidden Knowledge",
                "slot_type": "backpack",
                "quantity": 1,
            },
        ]

        container = ContainerComponent(
            container_id=uuid.uuid4(),
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            capacity_slots=8,
            items=items,
        )

        assert len(container.items) == 2
        assert container.items[0]["item_id"] == "elder_sign"
        assert container.items[1]["item_id"] == "tome_of_forbidden_knowledge"

    def test_container_invalid_capacity_slots(self):
        """Test that invalid capacity_slots is rejected."""
        # Too high
        with pytest.raises(ValidationError) as exc_info:
            ContainerComponent(
                container_id=uuid.uuid4(),
                source_type=ContainerSourceType.ENVIRONMENT,
                room_id="test_room",
                capacity_slots=25,
            )
        assert "capacity_slots" in str(exc_info.value).lower()

        # Too low
        with pytest.raises(ValidationError) as exc_info:
            ContainerComponent(
                container_id=uuid.uuid4(),
                source_type=ContainerSourceType.ENVIRONMENT,
                room_id="test_room",
                capacity_slots=0,
            )
        assert "capacity_slots" in str(exc_info.value).lower()

    def test_container_invalid_weight_limit(self):
        """Test that invalid weight_limit is rejected."""
        with pytest.raises(ValidationError) as exc_info:
            ContainerComponent(
                container_id=uuid.uuid4(),
                source_type=ContainerSourceType.ENVIRONMENT,
                room_id="test_room",
                capacity_slots=8,
                weight_limit=-1,
            )
        assert "weight_limit" in str(exc_info.value).lower()

    def test_container_required_fields(self):
        """Test that required fields are enforced."""
        # Missing container_id
        with pytest.raises(ValidationError):
            ContainerComponent(
                source_type=ContainerSourceType.ENVIRONMENT,
                room_id="test_room",
                capacity_slots=8,
            )

        # Missing source_type
        with pytest.raises(ValidationError):
            ContainerComponent(
                container_id=uuid.uuid4(),
                room_id="test_room",
                capacity_slots=8,
            )

        # Missing capacity_slots
        with pytest.raises(ValidationError):
            ContainerComponent(
                container_id=uuid.uuid4(),
                source_type=ContainerSourceType.ENVIRONMENT,
                room_id="test_room",
            )

    def test_container_defaults(self):
        """Test that default values are applied correctly."""
        container = ContainerComponent(
            container_id=uuid.uuid4(),
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id="test_room",
            capacity_slots=8,
        )

        assert container.lock_state == ContainerLockState.UNLOCKED
        assert container.items == []
        assert container.allowed_roles == []
        assert container.metadata == {}
        assert container.weight_limit is None
        assert container.decay_at is None


class TestContainerComponentSerialization:
    """Test ContainerComponent serialization."""

    def test_serialize_to_dict(self):
        """Test serializing container to dictionary."""
        container_id = uuid.uuid4()
        owner_id = uuid.uuid4()
        decay_at = datetime.now(UTC) + timedelta(hours=1)

        container = ContainerComponent(
            container_id=container_id,
            source_type=ContainerSourceType.CORPSE,
            owner_id=owner_id,
            room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            capacity_slots=20,
            lock_state=ContainerLockState.LOCKED,
            decay_at=decay_at,
            allowed_roles=["admin", "moderator"],
            metadata={"key_item_id": "arkham_library_key"},
        )

        data = container.model_dump(mode="json")

        assert data["container_id"] == str(container_id)
        assert data["source_type"] == "corpse"
        assert data["owner_id"] == str(owner_id)
        assert data["room_id"] == "earth_arkhamcity_sanitarium_room_foyer_001"
        assert data["capacity_slots"] == 20
        assert data["lock_state"] == "locked"
        assert data["decay_at"] == decay_at.isoformat()
        assert data["allowed_roles"] == ["admin", "moderator"]
        assert data["metadata"] == {"key_item_id": "arkham_library_key"}

    def test_serialize_to_json(self):
        """Test serializing container to JSON."""
        container = ContainerComponent(
            container_id=uuid.uuid4(),
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id="test_room",
            capacity_slots=8,
        )

        json_str = container.model_dump_json()
        assert isinstance(json_str, str)
        assert "container_id" in json_str
        assert "source_type" in json_str
        assert "environment" in json_str

    def test_deserialize_from_dict(self):
        """Test deserializing container from dictionary."""
        container_id = uuid.uuid4()
        owner_id = uuid.uuid4()

        data = {
            "container_id": str(container_id),
            "source_type": "corpse",
            "owner_id": str(owner_id),
            "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
            "capacity_slots": 20,
            "lock_state": "locked",
            "items": [],
            "allowed_roles": [],
            "metadata": {},
        }

        container = ContainerComponent.model_validate(data)

        assert container.container_id == container_id
        assert container.source_type == ContainerSourceType.CORPSE
        assert container.owner_id == owner_id
        assert container.lock_state == ContainerLockState.LOCKED

    def test_deserialize_from_json(self):
        """Test deserializing container from JSON string."""
        container_id = uuid.uuid4()

        json_str = f"""
        {{
            "container_id": "{container_id}",
            "source_type": "environment",
            "room_id": "test_room",
            "capacity_slots": 8,
            "lock_state": "unlocked",
            "items": [],
            "allowed_roles": [],
            "metadata": {{}}
        }}
        """

        container = ContainerComponent.model_validate_json(json_str)

        assert container.container_id == container_id
        assert container.source_type == ContainerSourceType.ENVIRONMENT
        assert container.capacity_slots == 8


class TestContainerComponentFactoryMethods:
    """Test ContainerComponent factory methods."""

    def test_create_environment_container_factory(self):
        """Test factory method for environmental containers."""
        container = ContainerComponent.create_environment(
            container_id=uuid.uuid4(),
            room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            capacity_slots=8,
        )

        assert container.source_type == ContainerSourceType.ENVIRONMENT
        assert container.room_id == "earth_arkhamcity_sanitarium_room_foyer_001"
        assert container.capacity_slots == 8
        assert container.owner_id is None
        assert container.entity_id is None

    def test_create_corpse_container_factory(self):
        """Test factory method for corpse containers."""
        owner_id = uuid.uuid4()
        decay_at = datetime.now(UTC) + timedelta(hours=1)

        container = ContainerComponent.create_corpse(
            container_id=uuid.uuid4(),
            owner_id=owner_id,
            room_id="earth_arkhamcity_sanitarium_room_foyer_001",
            decay_at=decay_at,
        )

        assert container.source_type == ContainerSourceType.CORPSE
        assert container.owner_id == owner_id
        assert container.decay_at == decay_at
        assert container.capacity_slots == 20  # Default for corpses

    def test_create_equipment_container_factory(self):
        """Test factory method for equipment containers."""
        entity_id = uuid.uuid4()

        container = ContainerComponent.create_equipment(
            container_id=uuid.uuid4(),
            entity_id=entity_id,
            capacity_slots=10,
        )

        assert container.source_type == ContainerSourceType.EQUIPMENT
        assert container.entity_id == entity_id
        assert container.room_id is None
        assert container.owner_id is None

    def test_factory_methods_with_optional_params(self):
        """Test factory methods with optional parameters."""
        container_id = uuid.uuid4()
        owner_id = uuid.uuid4()

        # Environment with lock state
        env_container = ContainerComponent.create_environment(
            container_id=container_id,
            room_id="test_room",
            capacity_slots=8,
            lock_state=ContainerLockState.LOCKED,
            metadata={"key_item_id": "test_key"},
        )

        assert env_container.lock_state == ContainerLockState.LOCKED
        assert env_container.metadata == {"key_item_id": "test_key"}

        # Corpse with items
        items = [
            {
                "item_instance_id": "inst_001",
                "prototype_id": "elder_sign",
                "item_id": "elder_sign",
                "item_name": "Elder Sign",
                "slot_type": "backpack",
                "quantity": 1,
            },
        ]

        decay_at = datetime.now(UTC) + timedelta(hours=1)
        corpse_container = ContainerComponent.create_corpse(
            container_id=uuid.uuid4(),
            owner_id=owner_id,
            room_id="test_room",
            decay_at=decay_at,
            items=items,
        )

        assert len(corpse_container.items) == 1
        assert corpse_container.items[0]["item_id"] == "elder_sign"
