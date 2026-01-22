"""
Container component model for the unified container system.

As documented in the restricted archives of Miskatonic University, container
components represent secure storage for investigator artifacts, wearable gear,
and the remains of fallen entities. These components require careful validation
to ensure proper handling of forbidden artifacts.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

if TYPE_CHECKING:
    from ..services.inventory_service import InventoryStack
else:
    # Use dict[str, Any] at runtime to avoid circular import
    InventoryStack = dict[str, Any]


class ContainerSourceType(str, Enum):
    """Source type for container instances."""

    ENVIRONMENT = "environment"
    EQUIPMENT = "equipment"
    CORPSE = "corpse"


class ContainerLockState(str, Enum):
    """Lock state for container instances."""

    UNLOCKED = "unlocked"
    LOCKED = "locked"
    SEALED = "sealed"


class ContainerComponent(BaseModel):
    """
    Container component model for unified container system.

    Represents environmental props, wearable gear, and corpses as secure
    storage containers with auditable interactions.

    As noted in the Pnakotic Manuscripts, containers must maintain strict
    validation to prevent dimensional anomalies and item corruption.
    """

    __slots__ = ()  # Performance optimization

    model_config = ConfigDict(
        # Security: Prevent field injection
        extra="forbid",
        # Runtime validation for assignment
        validate_assignment=True,
        # Use enum values for consistency
        use_enum_values=True,
        # Validate default values
        validate_default=True,
        # Pydantic v2 automatically serializes UUID to str and datetime to ISO format
        # No need for json_encoders (deprecated in v2)
    )

    # Identifiers
    container_id: UUID = Field(..., description="Unique container instance identifier")
    source_type: ContainerSourceType = Field(..., description="Type of container (environment, equipment, corpse)")

    # Ownership and location
    owner_id: UUID | None = Field(
        default=None,
        description="UUID of player/NPC who owns the container (NULL for shared environmental containers)",
    )
    room_id: str | None = Field(
        default=None,
        description="Room identifier for environmental and corpse containers",
    )
    entity_id: UUID | None = Field(
        default=None,
        description="Player/NPC UUID when container is wearable equipment",
    )

    # State
    lock_state: ContainerLockState = Field(
        default=ContainerLockState.UNLOCKED,
        description="Lock state: unlocked, locked, or sealed",
    )
    capacity_slots: int = Field(
        ...,
        ge=1,
        le=20,
        description="Maximum number of inventory slots (1-20)",
    )
    weight_limit: int | None = Field(
        default=None,
        gt=0,
        description="Optional maximum weight capacity",
    )
    decay_at: datetime | None = Field(
        default=None,
        description="Timestamp when corpse container should decay and be cleaned up",
    )

    # Access control
    allowed_roles: list[str] = Field(
        default_factory=list,
        description="List of role names allowed to access container",
    )

    # Contents
    items: list[InventoryStack] = Field(
        default_factory=list,
        description="List of InventoryStack items stored in container",
    )

    # Metadata
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Optional metadata for container-specific configuration",
    )

    @field_validator("metadata", mode="after")
    @classmethod
    def validate_metadata_no_personal_data(cls, v: dict[str, Any]) -> dict[str, Any]:
        """
        Validate that metadata does not contain personal information (COPPA compliance).

        As documented in the restricted archives, container metadata must never contain
        personal information to ensure compliance with Children's Online Privacy Protection Act.

        Args:
            v: Metadata dictionary to validate

        Returns:
            Validated metadata dictionary

        Raises:
            ValueError: If personal data fields are detected in metadata
        """
        # Personal information fields that must never be stored in container metadata
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
            "personal_info",
            "pii",
        ]

        # Check for personal data fields (case-insensitive)
        metadata_keys_lower = {k.lower(): k for k in v.keys()}
        for field in personal_data_fields:
            if field.lower() in metadata_keys_lower:
                raise ValueError(
                    f"Container metadata must not contain personal information. "
                    f"Found prohibited field: {metadata_keys_lower[field.lower()]}"
                )

        return v

    @field_validator("source_type", mode="before")
    @classmethod
    def validate_source_type(cls, v: Any) -> ContainerSourceType:
        """Validate and convert source_type to enum."""
        if isinstance(v, ContainerSourceType):
            return v
        if isinstance(v, str):
            try:
                return ContainerSourceType(v.lower())
            except ValueError as err:
                raise ValueError(f"Invalid source_type: {v}. Must be 'environment', 'equipment', or 'corpse'") from err
        raise ValueError(f"Invalid source_type type: {type(v)}")

    @field_validator("lock_state", mode="before")
    @classmethod
    def validate_lock_state(cls, v: Any) -> ContainerLockState:
        """Validate and convert lock_state to enum."""
        if isinstance(v, ContainerLockState):
            return v
        if isinstance(v, str):
            try:
                return ContainerLockState(v.lower())
            except ValueError as err:
                raise ValueError(f"Invalid lock_state: {v}. Must be 'unlocked', 'locked', or 'sealed'") from err
        raise ValueError(f"Invalid lock_state type: {type(v)}")

    @field_validator("room_id", mode="after")
    @classmethod
    def validate_room_id(cls, v: str | None, info) -> str | None:
        """Validate that room_id is provided for environment and corpse containers."""
        source_type = info.data.get("source_type")
        # Handle both enum and string values during validation
        source_type_value = source_type.value if hasattr(source_type, "value") else str(source_type)
        if source_type in (ContainerSourceType.ENVIRONMENT, ContainerSourceType.CORPSE) or source_type_value in (
            "environment",
            "corpse",
        ):
            if not v:
                raise ValueError(f"{source_type_value} containers must have a room_id")
        return v

    @field_validator("entity_id", mode="after")
    @classmethod
    def validate_entity_id(cls, v: UUID | None, info) -> UUID | None:
        """Validate that entity_id is provided for equipment containers."""
        source_type = info.data.get("source_type")
        # Handle both enum and string values during validation
        source_type_value = source_type.value if hasattr(source_type, "value") else str(source_type)
        if source_type == ContainerSourceType.EQUIPMENT or source_type_value == "equipment":
            if not v:
                raise ValueError("Equipment containers must have an entity_id")
        return v

    def is_locked(self) -> bool:
        """Check if container is locked or sealed."""
        return self.lock_state in (ContainerLockState.LOCKED, ContainerLockState.SEALED)

    def is_unlocked(self) -> bool:
        """Check if container is unlocked."""
        return self.lock_state == ContainerLockState.UNLOCKED

    def has_capacity(self) -> bool:
        """Check if container has available capacity."""
        return len(self.items) < self.capacity_slots

    def get_used_slots(self) -> int:
        """Get number of used inventory slots."""
        return len(self.items)

    def get_available_slots(self) -> int:
        """Get number of available inventory slots."""
        return self.capacity_slots - len(self.items)

    def is_decayed(self, current_time: datetime | None = None) -> bool:
        """Check if container has decayed (for corpse containers)."""
        if self.decay_at is None:
            return False
        if current_time is None:
            from datetime import UTC

            current_time = datetime.now(UTC)
        return current_time >= self.decay_at

    @classmethod
    def create_environment(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Container creation requires many parameters to capture complete container state
        cls,
        container_id: UUID,
        room_id: str,
        capacity_slots: int = 8,
        lock_state: ContainerLockState = ContainerLockState.UNLOCKED,
        weight_limit: int | None = None,
        allowed_roles: list[str] | None = None,
        items: list[InventoryStack] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> ContainerComponent:
        """
        Factory method to create an environmental container.

        Args:
            container_id: Unique container identifier
            room_id: Room identifier where container is located
            capacity_slots: Maximum number of inventory slots (default: 8)
            lock_state: Lock state (default: unlocked)
            weight_limit: Optional maximum weight capacity
            allowed_roles: List of role names allowed to access container
            items: Initial items in container
            metadata: Optional metadata dictionary

        Returns:
            ContainerComponent: New environmental container instance
        """
        return cls(
            container_id=container_id,
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id=room_id,
            capacity_slots=capacity_slots,
            lock_state=lock_state,
            weight_limit=weight_limit,
            allowed_roles=allowed_roles or [],
            items=items or [],
            metadata=metadata or {},
        )

    @classmethod
    def create_equipment(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Container creation requires many parameters to capture complete container state
        cls,
        container_id: UUID,
        entity_id: UUID,
        capacity_slots: int = 10,
        lock_state: ContainerLockState = ContainerLockState.UNLOCKED,
        weight_limit: int | None = None,
        allowed_roles: list[str] | None = None,
        items: list[InventoryStack] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> ContainerComponent:
        """
        Factory method to create a wearable equipment container.

        Args:
            container_id: Unique container identifier
            entity_id: Player/NPC UUID who owns the equipment
            capacity_slots: Maximum number of inventory slots (default: 10)
            lock_state: Lock state (default: unlocked)
            weight_limit: Optional maximum weight capacity
            allowed_roles: List of role names allowed to access container
            items: Initial items in container
            metadata: Optional metadata dictionary

        Returns:
            ContainerComponent: New equipment container instance
        """
        return cls(
            container_id=container_id,
            source_type=ContainerSourceType.EQUIPMENT,
            entity_id=entity_id,
            capacity_slots=capacity_slots,
            lock_state=lock_state,
            weight_limit=weight_limit,
            allowed_roles=allowed_roles or [],
            items=items or [],
            metadata=metadata or {},
        )

    @classmethod
    def create_corpse(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Container creation requires many parameters to capture complete container state
        cls,
        container_id: UUID,
        owner_id: UUID,
        room_id: str,
        decay_at: datetime,
        capacity_slots: int = 20,
        lock_state: ContainerLockState = ContainerLockState.UNLOCKED,
        weight_limit: int | None = None,
        allowed_roles: list[str] | None = None,
        items: list[InventoryStack] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> ContainerComponent:
        """
        Factory method to create a corpse container.

        Args:
            container_id: Unique container identifier
            owner_id: UUID of player/NPC who owned the corpse
            room_id: Room identifier where corpse is located
            decay_at: Timestamp when corpse should decay
            capacity_slots: Maximum number of inventory slots (default: 20)
            lock_state: Lock state (default: unlocked)
            weight_limit: Optional maximum weight capacity
            allowed_roles: List of role names allowed to access container
            items: Initial items in container (loot from corpse)
            metadata: Optional metadata dictionary

        Returns:
            ContainerComponent: New corpse container instance
        """
        return cls(
            container_id=container_id,
            source_type=ContainerSourceType.CORPSE,
            owner_id=owner_id,
            room_id=room_id,
            decay_at=decay_at,
            capacity_slots=capacity_slots,
            lock_state=lock_state,
            weight_limit=weight_limit,
            allowed_roles=allowed_roles or [],
            items=items or [],
            metadata=metadata or {},
        )

    def to_dict(self) -> dict[str, Any]:
        """
        Convert container component to dictionary representation.

        Backward compatibility method that delegates to model_dump().
        This allows tests and legacy code to continue using to_dict().

        Note: Uses mode="python" to preserve enum types instead of converting
        them to strings, which allows code to access .value on enums.

        Returns:
            Dictionary representation of the container component
        """
        return self.model_dump(mode="python", exclude_none=False, by_alias=False)
