"""
Tests for corpse lifecycle automation.

As documented in the restricted archives of Miskatonic University, corpse
lifecycle automation requires careful testing to ensure proper handling
of player death, grace periods, decay timers, and item redistribution.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.container import ContainerComponent, ContainerLockState, ContainerSourceType
from server.services.corpse_lifecycle_service import (
    CorpseLifecycleService,
    CorpseNotFoundError,
    CorpseServiceError,
)


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    return persistence


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.broadcast_room_event = AsyncMock(return_value={"successful_deliveries": 1})
    return manager


@pytest.fixture
def mock_time_service():
    """Create a mock time service."""
    service = MagicMock()
    service.get_current_mythos_datetime.return_value = datetime.now(UTC)
    return service


@pytest.fixture
def sample_player_id():
    """Generate a sample player UUID."""
    return uuid.uuid4()


@pytest.fixture
def sample_room_id():
    """Return a sample room ID."""
    return "earth_arkhamcity_sanitarium_room_foyer_001"


@pytest.fixture
def sample_corpse_container(sample_player_id, sample_room_id):
    """Create a sample corpse container."""
    grace_period_start = datetime.now(UTC)
    decay_at = grace_period_start + timedelta(hours=1)

    return ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=sample_player_id,
        room_id=sample_room_id,
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=decay_at,
        items=[],
        metadata={
            "grace_period_seconds": 300,  # 5 minutes
            "grace_period_start": grace_period_start.isoformat(),
            "player_name": "TestPlayer",
        },
    )


class TestCorpseCreationOnDeath:
    """Test corpse container creation on player death."""

    def test_create_corpse_container_on_death(
        self, mock_persistence, mock_connection_manager, sample_player_id, sample_room_id
    ):
        """Test creating a corpse container when a player dies."""
        # Mock player with inventory
        player = MagicMock()
        player.player_id = sample_player_id
        player.inventory = [
            {
                "item_instance_id": "inst_001",
                "prototype_id": "elder_sign",
                "item_id": "elder_sign",
                "item_name": "Elder Sign",
                "slot_type": "backpack",
                "quantity": 1,
            },
        ]
        player.name = "TestPlayer"

        mock_persistence.get_player.return_value = player

        # Create service
        service = CorpseLifecycleService(
            persistence=mock_persistence,
            connection_manager=mock_connection_manager,
        )

        # Create corpse
        corpse = service.create_corpse_on_death(
            player_id=sample_player_id,
            room_id=sample_room_id,
            grace_period_seconds=300,
            decay_hours=1,
        )

        # Verify corpse was created
        assert corpse is not None
        assert corpse.source_type == ContainerSourceType.CORPSE
        assert corpse.owner_id == sample_player_id
        assert corpse.room_id == sample_room_id
        assert len(corpse.items) == 1  # Should contain player's inventory
        assert corpse.decay_at is not None

        # Verify persistence was called
        mock_persistence.create_container.assert_called_once()

    def test_create_corpse_with_empty_inventory(
        self, mock_persistence, mock_connection_manager, sample_player_id, sample_room_id
    ):
        """Test creating a corpse container when player has no inventory."""
        player = MagicMock()
        player.player_id = sample_player_id
        player.inventory = []
        player.name = "TestPlayer"

        mock_persistence.get_player.return_value = player

        service = CorpseLifecycleService(
            persistence=mock_persistence,
            connection_manager=mock_connection_manager,
        )

        corpse = service.create_corpse_on_death(
            player_id=sample_player_id,
            room_id=sample_room_id,
            grace_period_seconds=300,
            decay_hours=1,
        )

        assert corpse is not None
        assert len(corpse.items) == 0

    def test_create_corpse_player_not_found(
        self, mock_persistence, mock_connection_manager, sample_player_id, sample_room_id
    ):
        """Test creating a corpse when player doesn't exist."""
        mock_persistence.get_player.return_value = None

        service = CorpseLifecycleService(
            persistence=mock_persistence,
            connection_manager=mock_connection_manager,
        )

        with pytest.raises(CorpseServiceError, match="Player not found"):
            service.create_corpse_on_death(
                player_id=sample_player_id,
                room_id=sample_room_id,
                grace_period_seconds=300,
                decay_hours=1,
            )


class TestCorpseGracePeriod:
    """Test corpse owner grace period logic."""

    def test_grace_period_active_owner_can_access(self, mock_persistence, sample_corpse_container, sample_player_id):
        """Test that owner can access corpse during grace period."""
        service = CorpseLifecycleService(persistence=mock_persistence)

        # Grace period should be active (just created)
        can_access = service.can_access_corpse(sample_corpse_container, sample_player_id)

        assert can_access is True

    def test_grace_period_active_non_owner_cannot_access(self, mock_persistence, sample_corpse_container):
        """Test that non-owner cannot access corpse during grace period."""
        other_player_id = uuid.uuid4()
        service = CorpseLifecycleService(persistence=mock_persistence)

        can_access = service.can_access_corpse(sample_corpse_container, other_player_id)

        assert can_access is False

    def test_grace_period_expired_anyone_can_access(self, mock_persistence, sample_corpse_container):
        """Test that anyone can access corpse after grace period expires."""
        # Set grace period to have expired
        expired_start = datetime.now(UTC) - timedelta(minutes=10)
        sample_corpse_container.metadata["grace_period_start"] = expired_start.isoformat()

        other_player_id = uuid.uuid4()
        service = CorpseLifecycleService(persistence=mock_persistence)

        can_access = service.can_access_corpse(sample_corpse_container, other_player_id)

        assert can_access is True

    def test_grace_period_admin_can_always_access(self, mock_persistence, sample_corpse_container):
        """Test that admin can always access corpse regardless of grace period."""
        other_player_id = uuid.uuid4()
        admin_player = MagicMock()
        admin_player.player_id = other_player_id
        admin_player.is_admin = True

        mock_persistence.get_player.return_value = admin_player

        service = CorpseLifecycleService(persistence=mock_persistence)

        can_access = service.can_access_corpse(sample_corpse_container, other_player_id, is_admin=True)

        assert can_access is True


class TestCorpseDecayTimer:
    """Test corpse decay timer and cleanup."""

    def test_corpse_not_decayed_yet(self, mock_persistence, sample_corpse_container, mock_time_service):
        """Test that corpse is not decayed if decay_at is in the future."""
        mock_time_service.get_current_mythos_datetime.return_value = datetime.now(UTC)

        service = CorpseLifecycleService(
            persistence=mock_persistence,
            time_service=mock_time_service,
        )

        is_decayed = service.is_corpse_decayed(sample_corpse_container)

        assert is_decayed is False

    def test_corpse_is_decayed(self, mock_persistence, sample_corpse_container, mock_time_service):
        """Test that corpse is decayed if decay_at is in the past."""
        # Set decay_at to past
        sample_corpse_container.decay_at = datetime.now(UTC) - timedelta(hours=1)

        mock_time_service.get_current_mythos_datetime.return_value = datetime.now(UTC)

        service = CorpseLifecycleService(
            persistence=mock_persistence,
            time_service=mock_time_service,
        )

        is_decayed = service.is_corpse_decayed(sample_corpse_container)

        assert is_decayed is True

    def test_get_decayed_corpses(self, mock_persistence, mock_time_service, sample_room_id):
        """Test getting list of decayed corpses in a room."""
        # Create decayed corpse
        decayed_corpse = ContainerComponent(
            container_id=uuid.uuid4(),
            source_type=ContainerSourceType.CORPSE,
            owner_id=uuid.uuid4(),
            room_id=sample_room_id,
            decay_at=datetime.now(UTC) - timedelta(hours=1),
            items=[],
        )

        # Create non-decayed corpse
        active_corpse = ContainerComponent(
            container_id=uuid.uuid4(),
            source_type=ContainerSourceType.CORPSE,
            owner_id=uuid.uuid4(),
            room_id=sample_room_id,
            decay_at=datetime.now(UTC) + timedelta(hours=1),
            items=[],
        )

        mock_persistence.get_containers_by_room_id.return_value = [
            decayed_corpse.model_dump(),
            active_corpse.model_dump(),
        ]

        mock_time_service.get_current_mythos_datetime.return_value = datetime.now(UTC)

        service = CorpseLifecycleService(
            persistence=mock_persistence,
            time_service=mock_time_service,
        )

        decayed = service.get_decayed_corpses_in_room(sample_room_id)

        assert len(decayed) == 1
        assert decayed[0].container_id == decayed_corpse.container_id


class TestCorpseCleanup:
    """Test corpse cleanup with item redistribution."""

    def test_cleanup_decayed_corpse_with_items(self, mock_persistence, mock_connection_manager, sample_room_id):
        """Test cleaning up a decayed corpse and redistributing items to room."""
        # Create decayed corpse with items
        decayed_corpse = ContainerComponent(
            container_id=uuid.uuid4(),
            source_type=ContainerSourceType.CORPSE,
            owner_id=uuid.uuid4(),
            room_id=sample_room_id,
            decay_at=datetime.now(UTC) - timedelta(hours=1),
            items=[
                {
                    "item_instance_id": "inst_001",
                    "prototype_id": "elder_sign",
                    "item_id": "elder_sign",
                    "item_name": "Elder Sign",
                    "slot_type": "backpack",
                    "quantity": 1,
                },
            ],
        )

        mock_persistence.get_container.return_value = decayed_corpse.model_dump()

        service = CorpseLifecycleService(
            persistence=mock_persistence,
            connection_manager=mock_connection_manager,
        )

        # Cleanup corpse
        service.cleanup_decayed_corpse(decayed_corpse.container_id)

        # Verify container was deleted
        mock_persistence.delete_container.assert_called_once_with(decayed_corpse.container_id)

        # Verify decay event was emitted
        mock_connection_manager.broadcast_room_event.assert_called_once()

    def test_cleanup_corpse_not_found(self, mock_persistence, mock_connection_manager):
        """Test cleanup when corpse doesn't exist."""
        mock_persistence.get_container.return_value = None

        service = CorpseLifecycleService(
            persistence=mock_persistence,
            connection_manager=mock_connection_manager,
        )

        with pytest.raises(CorpseNotFoundError):
            service.cleanup_decayed_corpse(uuid.uuid4())

    def test_cleanup_multiple_decayed_corpses(
        self, mock_persistence, mock_connection_manager, mock_time_service, sample_room_id
    ):
        """Test cleaning up multiple decayed corpses in a room."""
        # Create multiple decayed corpses
        decayed_corpses = [
            ContainerComponent(
                container_id=uuid.uuid4(),
                source_type=ContainerSourceType.CORPSE,
                owner_id=uuid.uuid4(),
                room_id=sample_room_id,
                decay_at=datetime.now(UTC) - timedelta(hours=1),
                items=[],
            )
            for _ in range(3)
        ]

        mock_persistence.get_containers_by_room_id.return_value = [corpse.model_dump() for corpse in decayed_corpses]

        mock_time_service.get_current_mythos_datetime.return_value = datetime.now(UTC)

        service = CorpseLifecycleService(
            persistence=mock_persistence,
            connection_manager=mock_connection_manager,
            time_service=mock_time_service,
        )

        # Cleanup all decayed corpses
        cleaned = service.cleanup_decayed_corpses_in_room(sample_room_id)

        assert cleaned == 3
        assert mock_persistence.delete_container.call_count == 3
