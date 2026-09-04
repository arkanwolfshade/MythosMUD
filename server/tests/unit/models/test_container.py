"""
Unit tests for container models.

Tests the ContainerComponent model including enums, validation, and methods.
"""

from datetime import UTC, datetime, timedelta
from typing import cast
from uuid import uuid4

import pytest
from pydantic import ValidationError

from server.models.container import (
    ContainerComponent,
    ContainerLockState,
    ContainerSourceType,
)
from server.services.inventory_service import InventoryStack

# --- Tests for ContainerSourceType enum ---


def test_container_source_type_enum_values():
    """Test ContainerSourceType enum contains expected values."""
    assert ContainerSourceType.ENVIRONMENT.value == "environment"
    assert ContainerSourceType.EQUIPMENT.value == "equipment"
    assert ContainerSourceType.CORPSE.value == "corpse"


def test_container_source_type_enum_all_types():
    """Test ContainerSourceType enum contains all expected types."""
    expected_types = {"environment", "equipment", "corpse"}
    actual_types = {t.value for t in ContainerSourceType}
    assert actual_types == expected_types


# --- Tests for ContainerLockState enum ---


def test_container_lock_state_enum_values():
    """Test ContainerLockState enum contains expected values."""
    assert ContainerLockState.UNLOCKED.value == "unlocked"
    assert ContainerLockState.LOCKED.value == "locked"
    assert ContainerLockState.SEALED.value == "sealed"


def test_container_lock_state_enum_all_states():
    """Test ContainerLockState enum contains all expected states."""
    expected_states = {"unlocked", "locked", "sealed"}
    actual_states = {s.value for s in ContainerLockState}
    assert actual_states == expected_states


# --- Tests for ContainerComponent methods ---


def test_container_component_is_locked_when_locked():
    """Test is_locked returns True when lock_state is LOCKED."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
        lock_state=ContainerLockState.LOCKED,
    )

    assert container.is_locked() is True


def test_container_component_is_locked_when_sealed():
    """Test is_locked returns True when lock_state is SEALED."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
        lock_state=ContainerLockState.SEALED,
    )

    assert container.is_locked() is True


def test_container_component_is_locked_when_unlocked():
    """Test is_locked returns False when lock_state is UNLOCKED."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
        lock_state=ContainerLockState.UNLOCKED,
    )

    assert container.is_locked() is False


def test_container_component_is_unlocked_when_unlocked():
    """Test is_unlocked returns True when lock_state is UNLOCKED."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
        lock_state=ContainerLockState.UNLOCKED,
    )

    assert container.is_unlocked() is True


def test_container_component_is_unlocked_when_locked():
    """Test is_unlocked returns False when lock_state is LOCKED."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
        lock_state=ContainerLockState.LOCKED,
    )

    assert container.is_unlocked() is False


def test_container_component_is_unlocked_when_sealed():
    """Test is_unlocked returns False when lock_state is SEALED."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
        lock_state=ContainerLockState.SEALED,
    )

    assert container.is_unlocked() is False


def test_container_component_has_capacity_when_available():
    """Test has_capacity returns True when slots are available."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
    )
    container.items = []  # Empty items

    assert container.has_capacity() is True


def test_container_component_has_capacity_when_full():
    """Test has_capacity returns False when at capacity."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=2,
    )
    # Fill items to capacity
    # Test uses simplified item structure, not full InventoryStack TypedDict
    container.items = cast(list[InventoryStack], [{"id": "item1"}, {"id": "item2"}])

    assert container.has_capacity() is False


def test_container_component_has_room_for_additional_items():
    """Test has_room_for returns True when container has space for additional items."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
    )
    container.items = cast(list[InventoryStack], [{"id": "item1"}, {"id": "item2"}])
    assert container.has_room_for(3) is True
    assert container.has_room_for(8) is True


def test_container_component_has_room_for_exceeds_capacity():
    """Test has_room_for returns False when adding items would exceed capacity."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=5,
    )
    container.items = cast(list[InventoryStack], [{"id": "item1"}, {"id": "item2"}, {"id": "item3"}])
    assert container.has_room_for(3) is False
    assert container.has_room_for(5) is False


def test_container_component_can_hold_replacement_items():
    """Test can_hold returns True when item_count fits capacity (replacement scenario)."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
    )
    assert container.can_hold(5) is True
    assert container.can_hold(10) is True


def test_container_component_would_exceed_capacity():
    """Test would_exceed_capacity returns True when adding items would exceed capacity."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=3,
    )
    container.items = cast(list[InventoryStack], [{"id": "item1"}, {"id": "item2"}])
    assert container.would_exceed_capacity([{"id": "x"}]) is False
    assert container.would_exceed_capacity([{"id": "x"}, {"id": "y"}]) is True


def test_container_component_can_hold_exceeds_capacity():
    """Test can_hold returns False when item_count exceeds capacity."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=5,
    )
    assert container.can_hold(6) is False
    assert container.can_hold(10) is False


def test_container_component_get_used_slots():
    """Test get_used_slots returns correct count."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
    )
    # Test uses simplified item structure, not full InventoryStack TypedDict
    container.items = cast(list[InventoryStack], [{"id": "item1"}, {"id": "item2"}, {"id": "item3"}])

    result = container.get_used_slots()

    assert result == 3


def test_container_component_get_used_slots_empty():
    """Test get_used_slots returns 0 for empty items."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
    )
    container.items = []

    result = container.get_used_slots()

    assert result == 0


def test_container_component_get_available_slots():
    """Test get_available_slots returns correct count."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
    )
    # Test uses simplified item structure, not full InventoryStack TypedDict
    container.items = cast(list[InventoryStack], [{"id": "item1"}, {"id": "item2"}])  # 2 used

    result = container.get_available_slots()

    assert result == 8  # 10 - 2


def test_container_component_get_available_slots_full():
    """Test get_available_slots returns 0 when full."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=5,
    )
    # Test uses simplified item structure, not full InventoryStack TypedDict
    container.items = cast(
        list[InventoryStack], [{"id": "item1"}, {"id": "item2"}, {"id": "item3"}, {"id": "item4"}, {"id": "item5"}]
    )  # Full

    result = container.get_available_slots()

    assert result == 0


def test_container_component_is_decayed_when_expired():
    """Test is_decayed returns True when decay_at is in the past."""
    # Use naive datetime for decay_at to match model storage
    past_time = datetime.now(UTC).replace(tzinfo=None) - timedelta(hours=1)
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.CORPSE,
        room_id="room123",
        capacity_slots=10,
        decay_at=past_time,
    )

    # Pass naive current_time to avoid timezone comparison issues
    current_naive = datetime.now(UTC).replace(tzinfo=None)
    assert container.is_decayed(current_time=current_naive) is True


def test_container_component_is_decayed_when_not_expired():
    """Test is_decayed returns False when decay_at is in the future."""
    # Use naive datetime for decay_at to match model storage
    future_time = datetime.now(UTC).replace(tzinfo=None) + timedelta(hours=1)
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.CORPSE,
        room_id="room123",
        capacity_slots=10,
        decay_at=future_time,
    )

    # Pass naive current_time to avoid timezone comparison issues
    current_naive = datetime.now(UTC).replace(tzinfo=None)
    assert container.is_decayed(current_time=current_naive) is False


def test_container_component_is_decayed_with_custom_time():
    """Test is_decayed uses provided current_time parameter."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.CORPSE,
        room_id="room123",
        capacity_slots=10,
        decay_at=datetime(2025, 1, 1, 12, 0, 0),  # Naive datetime
    )

    # Test with time before decay (naive datetime)
    assert container.is_decayed(current_time=datetime(2025, 1, 1, 11, 0, 0)) is False

    # Test with time after decay (naive datetime)
    assert container.is_decayed(current_time=datetime(2025, 1, 1, 13, 0, 0)) is True


def test_container_component_is_decayed_when_no_decay_time():
    """Test is_decayed returns False when decay_at is None."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
    )
    container.decay_at = None

    assert container.is_decayed() is False


def test_container_component_rejects_extra_fields():
    """Test ContainerComponent rejects unknown fields (extra='forbid')."""
    with pytest.raises(ValidationError) as exc_info:
        # Reason: Intentionally testing Pydantic validation with extra='forbid' - extra fields should be rejected
        ContainerComponent(  # type: ignore[call-arg]
            container_id=uuid4(),
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id="room123",
            capacity_slots=10,
            unknown_field="value",
        )

    error_str = str(exc_info.value).lower()
    assert "extra" in error_str and ("not permitted" in error_str or "forbidden" in error_str)


def test_container_component_default_lock_state():
    """Test ContainerComponent defaults to UNLOCKED lock state."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
    )

    assert container.lock_state == ContainerLockState.UNLOCKED


def test_container_component_default_items():
    """Test ContainerComponent defaults to empty items list."""
    container = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,
    )

    assert container.items == []


def test_container_component_capacity_slots_validation_min():
    """Test ContainerComponent validates capacity_slots minimum value."""
    with pytest.raises(ValidationError):
        ContainerComponent(
            container_id=uuid4(),
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id="room123",
            capacity_slots=0,  # Below minimum of 1
        )


def test_container_component_capacity_slots_validation_max():
    """Test ContainerComponent validates capacity_slots maximum value."""
    with pytest.raises(ValidationError):
        ContainerComponent(
            container_id=uuid4(),
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id="room123",
            capacity_slots=21,  # Above maximum of 20
        )


def test_container_component_capacity_slots_valid_range():
    """Test ContainerComponent accepts capacity_slots in valid range."""
    container1 = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=1,  # Minimum
    )
    assert container1.capacity_slots == 1

    container2 = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=20,  # Maximum
    )
    assert container2.capacity_slots == 20

    container3 = ContainerComponent(
        container_id=uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        room_id="room123",
        capacity_slots=10,  # Middle
    )
    assert container3.capacity_slots == 10
