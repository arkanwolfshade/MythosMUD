"""
Tests for container access control and locking mechanisms.

As documented in the restricted archives of Miskatonic University, container
access control requires thorough testing to ensure proper security and
compliance with forbidden artifact handling protocols.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

import pytest

from server.models.container import ContainerComponent, ContainerLockState, ContainerSourceType
from server.services.container_service import (
    ContainerAccessDeniedError,
    ContainerLockedError,
    ContainerService,
)


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    return persistence


@pytest.fixture
def container_service(mock_persistence):
    """Create a ContainerService instance for testing."""
    from server.services.inventory_mutation_guard import InventoryMutationGuard
    from server.services.inventory_service import InventoryService

    return ContainerService(
        persistence=mock_persistence,
        inventory_service=InventoryService(max_slots=20),
        mutation_guard=InventoryMutationGuard(),
    )


@pytest.fixture
def sample_player_id():
    """Generate a sample player UUID."""
    return uuid.uuid4()


@pytest.fixture
def sample_other_player_id():
    """Generate another sample player UUID."""
    return uuid.uuid4()


@pytest.fixture
def sample_room_id():
    """Return a sample room ID."""
    return "earth_arkhamcity_sanitarium_room_foyer_001"


@pytest.fixture
def sample_container_id():
    """Generate a sample container UUID."""
    return uuid.uuid4()


class TestContainerProximityValidation:
    """Test container proximity validation."""

    def test_open_container_same_room(
        self, container_service, mock_persistence, sample_container_id, sample_player_id, sample_room_id
    ):
        """Test opening a container when player is in the same room."""
        # Create container in room
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id=sample_room_id,
            capacity_slots=8,
        )

        # Mock player in same room
        player = MagicMock()
        player.player_id = sample_player_id
        player.current_room_id = sample_room_id
        player.is_admin = False

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = player

        result = container_service.open_container(sample_container_id, sample_player_id)

        assert result is not None
        assert "mutation_token" in result

    def test_open_container_different_room(
        self, container_service, mock_persistence, sample_container_id, sample_player_id, sample_room_id
    ):
        """Test opening a container when player is in a different room."""
        # Create container in room
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id=sample_room_id,
            capacity_slots=8,
        )

        # Mock player in different room
        player = MagicMock()
        player.player_id = sample_player_id
        player.current_room_id = "different_room_id"
        player.is_admin = False

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = player

        with pytest.raises(ContainerAccessDeniedError, match="not in same room"):
            container_service.open_container(sample_container_id, sample_player_id)

    def test_open_equipment_container_owned_by_player(
        self, container_service, mock_persistence, sample_container_id, sample_player_id
    ):
        """Test opening an equipment container owned by the player."""
        # Create equipment container
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.EQUIPMENT,
            entity_id=sample_player_id,
            capacity_slots=10,
        )

        # Mock player
        player = MagicMock()
        player.player_id = sample_player_id
        player.is_admin = False

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = player

        result = container_service.open_container(sample_container_id, sample_player_id)

        assert result is not None
        assert "mutation_token" in result

    def test_open_equipment_container_owned_by_other(
        self, container_service, mock_persistence, sample_container_id, sample_player_id, sample_other_player_id
    ):
        """Test opening an equipment container owned by another player."""
        # Create equipment container owned by other player
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.EQUIPMENT,
            entity_id=sample_other_player_id,
            capacity_slots=10,
        )

        # Mock player trying to access
        player = MagicMock()
        player.player_id = sample_player_id
        player.is_admin = False

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = player

        with pytest.raises(ContainerAccessDeniedError, match="does not own"):
            container_service.open_container(sample_container_id, sample_player_id)


class TestContainerRoleBasedAccess:
    """Test container role-based access control."""

    def test_open_container_with_allowed_role(
        self, container_service, mock_persistence, sample_container_id, sample_player_id, sample_room_id
    ):
        """Test opening a container when player has allowed role."""
        # Create container with role restriction
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id=sample_room_id,
            capacity_slots=8,
            allowed_roles=["admin", "moderator"],
        )

        # Mock player with admin role
        player = MagicMock()
        player.player_id = sample_player_id
        player.current_room_id = sample_room_id
        player.is_admin = True

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = player

        result = container_service.open_container(sample_container_id, sample_player_id)

        assert result is not None

    def test_open_container_without_allowed_role(
        self, container_service, mock_persistence, sample_container_id, sample_player_id, sample_room_id
    ):
        """Test opening a container when player doesn't have allowed role."""
        # Create container with role restriction
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id=sample_room_id,
            capacity_slots=8,
            allowed_roles=["admin"],
        )

        # Mock player without admin role
        player = MagicMock()
        player.player_id = sample_player_id
        player.current_room_id = sample_room_id
        player.is_admin = False

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = player

        with pytest.raises(ContainerAccessDeniedError, match="role"):
            container_service.open_container(sample_container_id, sample_player_id)

    def test_open_container_no_role_restriction(
        self, container_service, mock_persistence, sample_container_id, sample_player_id, sample_room_id
    ):
        """Test opening a container with no role restrictions."""
        # Create container without role restrictions
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id=sample_room_id,
            capacity_slots=8,
            allowed_roles=[],
        )

        # Mock player
        player = MagicMock()
        player.player_id = sample_player_id
        player.current_room_id = sample_room_id
        player.is_admin = False

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = player

        result = container_service.open_container(sample_container_id, sample_player_id)

        assert result is not None


class TestContainerLockUnlock:
    """Test container lock/unlock mechanisms."""

    def test_lock_container(
        self, container_service, mock_persistence, sample_container_id, sample_player_id, sample_room_id
    ):
        """Test locking a container."""
        # Create unlocked container
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id=sample_room_id,
            capacity_slots=8,
            lock_state=ContainerLockState.UNLOCKED,
        )

        # Mock player
        player = MagicMock()
        player.player_id = sample_player_id
        player.current_room_id = sample_room_id
        player.is_admin = False

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = player

        # Lock container
        container_service.lock_container(sample_container_id, sample_player_id, ContainerLockState.LOCKED)

        # Verify container is locked
        call_kwargs = mock_persistence.update_container.call_args.kwargs
        assert call_kwargs.get("lock_state") == ContainerLockState.LOCKED.value

    def test_unlock_container(
        self, container_service, mock_persistence, sample_container_id, sample_player_id, sample_room_id
    ):
        """Test unlocking a container."""
        # Create locked container
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id=sample_room_id,
            capacity_slots=8,
            lock_state=ContainerLockState.LOCKED,
        )

        # Mock player (admin can unlock locked containers without keys)
        player = MagicMock()
        player.player_id = sample_player_id
        player.current_room_id = sample_room_id
        player.is_admin = True

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = player

        # Unlock container
        container_service.unlock_container(sample_container_id, sample_player_id)

        # Verify container is unlocked
        call_kwargs = mock_persistence.update_container.call_args.kwargs
        assert call_kwargs.get("lock_state") == ContainerLockState.UNLOCKED.value

    def test_open_locked_container_without_key(
        self, container_service, mock_persistence, sample_container_id, sample_player_id, sample_room_id
    ):
        """Test opening a locked container without a key."""
        # Create locked container
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id=sample_room_id,
            capacity_slots=8,
            lock_state=ContainerLockState.LOCKED,
            metadata={"key_item_id": "arkham_library_key"},
        )

        # Mock player without key
        player = MagicMock()
        player.player_id = sample_player_id
        player.current_room_id = sample_room_id
        player.is_admin = False
        player.inventory = []  # No key in inventory

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = player

        with pytest.raises(ContainerLockedError):
            container_service.open_container(sample_container_id, sample_player_id)

    def test_open_locked_container_with_key(
        self, container_service, mock_persistence, sample_container_id, sample_player_id, sample_room_id
    ):
        """Test opening a locked container with the correct key."""
        # Create locked container
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id=sample_room_id,
            capacity_slots=8,
            lock_state=ContainerLockState.LOCKED,
            metadata={"key_item_id": "arkham_library_key"},
        )

        # Mock player with key
        player = MagicMock()
        player.player_id = sample_player_id
        player.current_room_id = sample_room_id
        player.is_admin = False
        player.inventory = [
            {
                "item_id": "arkham_library_key",
                "item_name": "Arkham Library Key",
                "slot_type": "backpack",
                "quantity": 1,
            }
        ]

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = player

        result = container_service.open_container(sample_container_id, sample_player_id)

        assert result is not None
        assert "mutation_token" in result

    def test_open_sealed_container(
        self, container_service, mock_persistence, sample_container_id, sample_player_id, sample_room_id
    ):
        """Test that sealed containers cannot be opened."""
        # Create sealed container
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id=sample_room_id,
            capacity_slots=8,
            lock_state=ContainerLockState.SEALED,
        )

        player = MagicMock()
        player.player_id = sample_player_id
        player.current_room_id = sample_room_id
        player.is_admin = False

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = player

        with pytest.raises(ContainerAccessDeniedError, match="sealed"):
            container_service.open_container(sample_container_id, sample_player_id)

    def test_admin_can_open_sealed_container(
        self, container_service, mock_persistence, sample_container_id, sample_player_id, sample_room_id
    ):
        """Test that admins can open sealed containers."""
        # Create sealed container
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.ENVIRONMENT,
            room_id=sample_room_id,
            capacity_slots=8,
            lock_state=ContainerLockState.SEALED,
        )

        # Mock admin player
        player = MagicMock()
        player.player_id = sample_player_id
        player.current_room_id = sample_room_id
        player.is_admin = True

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = player

        result = container_service.open_container(sample_container_id, sample_player_id)

        assert result is not None
        assert "mutation_token" in result


class TestCorpseOwnerGracePeriod:
    """Test corpse container owner grace period."""

    def test_open_corpse_before_grace_period(
        self, container_service, mock_persistence, sample_container_id, sample_player_id, sample_room_id
    ):
        """Test opening a corpse container before grace period expires (owner only)."""
        owner_id = sample_player_id
        other_player_id = uuid.uuid4()

        # Create corpse container with grace period
        decay_at = datetime.now(UTC) + timedelta(hours=1)
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.CORPSE,
            owner_id=owner_id,
            room_id=sample_room_id,
            capacity_slots=20,
            decay_at=decay_at,
            metadata={"grace_period_seconds": 300},  # 5 minutes
        )

        # Mock owner player
        owner_player = MagicMock()
        owner_player.player_id = owner_id
        owner_player.current_room_id = sample_room_id
        owner_player.is_admin = False

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = owner_player

        # Owner can open
        result = container_service.open_container(sample_container_id, owner_id)
        assert result is not None

        # Other player cannot open during grace period
        other_player = MagicMock()
        other_player.player_id = other_player_id
        other_player.current_room_id = sample_room_id
        other_player.is_admin = False

        mock_persistence.get_player.return_value = other_player

        with pytest.raises(ContainerAccessDeniedError, match="grace period"):
            container_service.open_container(sample_container_id, other_player_id)

    def test_open_corpse_after_grace_period(
        self, container_service, mock_persistence, sample_container_id, sample_player_id, sample_room_id
    ):
        """Test opening a corpse container after grace period expires (anyone can open)."""
        owner_id = sample_player_id
        other_player_id = uuid.uuid4()

        # Create corpse container with expired grace period
        decay_at = datetime.now(UTC) + timedelta(hours=1)
        container = ContainerComponent(
            container_id=sample_container_id,
            source_type=ContainerSourceType.CORPSE,
            owner_id=owner_id,
            room_id=sample_room_id,
            capacity_slots=20,
            decay_at=decay_at,
            metadata={
                "grace_period_seconds": 300,  # 5 minutes
                "grace_period_start": (datetime.now(UTC) - timedelta(minutes=10)).isoformat(),  # Expired
            },
        )

        # Mock other player
        other_player = MagicMock()
        other_player.player_id = other_player_id
        other_player.current_room_id = sample_room_id
        other_player.is_admin = False

        mock_persistence.get_container.return_value = container.to_dict()
        mock_persistence.get_player.return_value = other_player

        # Other player can now open after grace period
        result = container_service.open_container(sample_container_id, other_player_id)
        assert result is not None
