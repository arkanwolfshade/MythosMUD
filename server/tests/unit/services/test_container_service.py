"""
Tests for container service.

This module tests the ContainerService class and its methods for managing
container operations including open/close, transfers, and access control.
"""

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.exceptions import ValidationError
from server.models.container import ContainerLockState
from server.services.container_service import (
    ContainerAccessDeniedError,
    ContainerLockedError,
    ContainerNotFoundError,
    ContainerService,
    ContainerServiceError,
    _filter_container_data,
    _get_enum_value,
)


class TestGetEnumValue:
    """Test _get_enum_value helper function."""

    def test_get_enum_value_with_enum(self):
        """Test getting enum value from enum instance."""
        result = _get_enum_value(ContainerLockState.LOCKED)
        assert result == "locked"

    def test_get_enum_value_with_string(self):
        """Test getting enum value from string."""
        result = _get_enum_value("unlocked")
        assert result == "unlocked"

    def test_get_enum_value_with_none(self):
        """Test getting enum value from None."""
        result = _get_enum_value(None)
        assert result == "None"


class TestFilterContainerData:
    """Test _filter_container_data helper function."""

    def test_filter_container_data_removes_timestamps(self):
        """Test that created_at and updated_at are removed."""
        container_data = {
            "container_id": str(uuid4()),
            "items": [],
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z",
        }

        result = _filter_container_data(container_data)

        assert "created_at" not in result
        assert "updated_at" not in result
        assert "container_id" in result

    def test_filter_container_data_converts_items_json(self):
        """Test that items_json is converted to items."""
        container_data = {
            "container_id": str(uuid4()),
            "items_json": [{"item_id": "item-1"}],
            "metadata_json": {"name": "Chest"},
        }

        result = _filter_container_data(container_data)

        assert "items_json" not in result
        assert "items" in result
        assert result["items"] == [{"item_id": "item-1"}]

    def test_filter_container_data_converts_metadata_json(self):
        """Test that metadata_json is converted to metadata."""
        container_data = {
            "container_id": str(uuid4()),
            "items": [],
            "metadata_json": {"name": "Chest"},
        }

        result = _filter_container_data(container_data)

        assert "metadata_json" not in result
        assert "metadata" in result
        assert result["metadata"] == {"name": "Chest"}

    def test_filter_container_data_preserves_other_fields(self):
        """Test that other fields are preserved."""
        container_data = {
            "container_id": str(uuid4()),
            "items": [],
            "capacity_slots": 10,
            "lock_state": "unlocked",
        }

        result = _filter_container_data(container_data)

        assert result["container_id"] == container_data["container_id"]
        assert result["capacity_slots"] == 10
        assert result["lock_state"] == "unlocked"


class TestContainerServiceInit:
    """Test ContainerService initialization."""

    def test_container_service_init_defaults(self):
        """Test ContainerService initialization with defaults."""
        mock_persistence = MagicMock()

        service = ContainerService(persistence=mock_persistence)

        assert service.persistence == mock_persistence
        assert service.inventory_service is not None
        assert service.mutation_guard is not None
        assert service._open_containers == {}

    def test_container_service_init_custom_services(self):
        """Test ContainerService initialization with custom services."""
        from server.services.inventory_mutation_guard import InventoryMutationGuard
        from server.services.inventory_service import InventoryService

        mock_persistence = MagicMock()
        custom_inventory = InventoryService(max_slots=30)
        custom_guard = InventoryMutationGuard()

        service = ContainerService(
            persistence=mock_persistence, inventory_service=custom_inventory, mutation_guard=custom_guard
        )

        assert service.inventory_service == custom_inventory
        assert service.mutation_guard == custom_guard


class TestGetContainerToken:
    """Test get_container_token method."""

    def test_get_container_token_when_open(self):
        """Test getting token when container is open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()
        token = "test-token"

        service._open_containers[container_id] = {player_id: token}

        result = service.get_container_token(container_id, player_id)

        assert result == token

    def test_get_container_token_when_not_open(self):
        """Test getting token when container is not open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()

        result = service.get_container_token(container_id, player_id)

        assert result is None

    def test_get_container_token_when_open_by_different_player(self):
        """Test getting token when container is open by different player."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id1 = uuid4()
        player_id2 = uuid4()
        token = "test-token"

        service._open_containers[container_id] = {player_id1: token}

        result = service.get_container_token(container_id, player_id2)

        assert result is None


class TestRemoveContainerFromOpenList:
    """Test _remove_container_from_open_list method."""

    def test_remove_container_from_open_list_single_player(self):
        """Test removing container when only one player has it open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()

        service._open_containers[container_id] = {player_id: "token"}

        service._remove_container_from_open_list(container_id, player_id)

        assert container_id not in service._open_containers

    def test_remove_container_from_open_list_multiple_players(self):
        """Test removing container when multiple players have it open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id1 = uuid4()
        player_id2 = uuid4()

        service._open_containers[container_id] = {player_id1: "token1", player_id2: "token2"}

        service._remove_container_from_open_list(container_id, player_id1)

        assert container_id in service._open_containers
        assert player_id1 not in service._open_containers[container_id]
        assert player_id2 in service._open_containers[container_id]


class TestValidateContainerClose:
    """Test _validate_container_close method."""

    def test_validate_container_close_success(self):
        """Test validation when container is properly open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()
        token = "test-token"
        context = MagicMock()

        service._open_containers[container_id] = {player_id: token}

        # Should not raise
        service._validate_container_close(container_id, player_id, token, context)

    def test_validate_container_close_not_open(self):
        """Test validation when container is not open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()
        token = "test-token"
        context = MagicMock()

        with pytest.raises(ContainerServiceError, match="Container not open"):
            service._validate_container_close(container_id, player_id, token, context)

    def test_validate_container_close_wrong_player(self):
        """Test validation when container is open by different player."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id1 = uuid4()
        player_id2 = uuid4()
        token = "test-token"
        context = MagicMock()

        service._open_containers[container_id] = {player_id1: token}

        with pytest.raises(ContainerServiceError, match="Container not open by player"):
            service._validate_container_close(container_id, player_id2, token, context)

    def test_validate_container_close_invalid_token(self):
        """Test validation when mutation token is invalid."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()
        correct_token = "correct-token"
        wrong_token = "wrong-token"
        context = MagicMock()

        service._open_containers[container_id] = {player_id: correct_token}

        with pytest.raises(ContainerServiceError, match="Invalid mutation token"):
            service._validate_container_close(container_id, player_id, wrong_token, context)


class TestOpenContainer:
    """Test open_container method."""

    @pytest.mark.asyncio
    async def test_open_container_success(self):
        """Test successfully opening a container."""
        mock_persistence = AsyncMock()
        container_id = uuid4()
        player_id = uuid4()

        container_data = {
            "container_id": str(container_id),
            "items": [],
            "capacity_slots": 10,
            "lock_state": "unlocked",
            "source_type": "environment",
            "room_id": "room-123",
        }
        mock_persistence.get_container.return_value = container_data

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "room-123"
        mock_player.is_admin = False
        mock_persistence.get_player_by_id.return_value = mock_player

        service = ContainerService(persistence=mock_persistence)

        with patch("server.services.container_service.audit_logger") as _mock_audit:
            result = await service.open_container(container_id, player_id)

            assert "container" in result
            assert "mutation_token" in result
            assert result["mutation_token"] is not None
            assert container_id in service._open_containers
            assert player_id in service._open_containers[container_id]

    @pytest.mark.asyncio
    async def test_open_container_not_found(self):
        """Test opening a container that doesn't exist."""
        mock_persistence = AsyncMock()
        container_id = uuid4()
        player_id = uuid4()

        mock_persistence.get_container.return_value = None

        service = ContainerService(persistence=mock_persistence)

        with pytest.raises(ContainerNotFoundError, match="Container not found"):
            await service.open_container(container_id, player_id)

    @pytest.mark.asyncio
    async def test_open_container_player_not_found(self):
        """Test opening a container when player doesn't exist."""
        mock_persistence = AsyncMock()
        container_id = uuid4()
        player_id = uuid4()

        container_data = {
            "container_id": str(container_id),
            "items": [],
            "capacity_slots": 10,
            "lock_state": "unlocked",
            "source_type": "environment",
            "room_id": "room-123",
        }
        mock_persistence.get_container.return_value = container_data
        mock_persistence.get_player_by_id.return_value = None

        service = ContainerService(persistence=mock_persistence)

        with pytest.raises(ValidationError, match="Player not found"):
            await service.open_container(container_id, player_id)

    @pytest.mark.asyncio
    async def test_open_container_locked(self):
        """Test opening a locked container."""
        mock_persistence = AsyncMock()
        container_id = uuid4()
        player_id = uuid4()

        container_data = {
            "container_id": str(container_id),
            "items": [],
            "capacity_slots": 10,
            "lock_state": "locked",
            "source_type": "environment",
            "room_id": "room-123",
        }
        mock_persistence.get_container.return_value = container_data

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "room-123"
        mock_player.is_admin = False
        mock_persistence.get_player_by_id.return_value = mock_player

        service = ContainerService(persistence=mock_persistence)

        with pytest.raises(ContainerLockedError, match="Container is locked"):
            await service.open_container(container_id, player_id)

    @pytest.mark.asyncio
    async def test_open_container_sealed(self):
        """Test opening a sealed container."""
        mock_persistence = AsyncMock()
        container_id = uuid4()
        player_id = uuid4()

        container_data = {
            "container_id": str(container_id),
            "items": [],
            "capacity_slots": 10,
            "lock_state": "sealed",
            "source_type": "environment",
            "room_id": "room-123",
        }
        mock_persistence.get_container.return_value = container_data

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "room-123"
        mock_player.is_admin = False
        mock_persistence.get_player_by_id.return_value = mock_player

        service = ContainerService(persistence=mock_persistence)

        with pytest.raises(ContainerAccessDeniedError, match="Container is sealed"):
            await service.open_container(container_id, player_id)

    @pytest.mark.asyncio
    async def test_open_container_already_open(self):
        """Test opening a container that's already open."""
        mock_persistence = AsyncMock()
        container_id = uuid4()
        player_id = uuid4()

        container_data = {
            "container_id": str(container_id),
            "items": [],
            "capacity_slots": 10,
            "lock_state": "unlocked",
            "source_type": "environment",
            "room_id": "room-123",
        }
        mock_persistence.get_container.return_value = container_data

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "room-123"
        mock_player.is_admin = False
        mock_persistence.get_player_by_id.return_value = mock_player

        service = ContainerService(persistence=mock_persistence)
        service._open_containers[container_id] = {player_id: "existing-token"}

        with pytest.raises(ContainerServiceError, match="Container already open"):
            await service.open_container(container_id, player_id)


class TestCloseContainer:
    """Test close_container method."""

    @pytest.mark.asyncio
    async def test_close_container_success(self):
        """Test successfully closing a container."""
        mock_persistence = AsyncMock()
        container_id = uuid4()
        player_id = uuid4()
        token = "test-token"

        service = ContainerService(persistence=mock_persistence)
        service._open_containers[container_id] = {player_id: token}

        container_data = {
            "container_id": str(container_id),
            "items": [],
            "capacity_slots": 10,
            "lock_state": "unlocked",
            "source_type": "environment",
            "room_id": "room-123",
        }
        mock_persistence.get_container.return_value = container_data

        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        mock_persistence.get_player_by_id.return_value = mock_player

        with patch("server.services.container_service.audit_logger"):
            await service.close_container(container_id, player_id, token)

            assert container_id not in service._open_containers

    @pytest.mark.asyncio
    async def test_close_container_not_open(self):
        """Test closing a container that's not open."""
        mock_persistence = AsyncMock()
        container_id = uuid4()
        player_id = uuid4()
        token = "test-token"

        service = ContainerService(persistence=mock_persistence)

        with pytest.raises(ContainerServiceError, match="Container not open"):
            await service.close_container(container_id, player_id, token)

    @pytest.mark.asyncio
    async def test_close_container_invalid_token(self):
        """Test closing a container with invalid token."""
        mock_persistence = AsyncMock()
        container_id = uuid4()
        player_id = uuid4()
        correct_token = "correct-token"
        wrong_token = "wrong-token"

        service = ContainerService(persistence=mock_persistence)
        service._open_containers[container_id] = {player_id: correct_token}

        with pytest.raises(ContainerServiceError, match="Invalid mutation token"):
            await service.close_container(container_id, player_id, wrong_token)


class TestVerifyContainerOpen:
    """Test _verify_container_open method."""

    def test_verify_container_open_success(self):
        """Test verification when container is properly open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()
        token = "test-token"

        service._open_containers[container_id] = {player_id: token}

        # Should not raise
        service._verify_container_open(container_id, player_id, token)

    def test_verify_container_open_not_open(self):
        """Test verification when container is not open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()
        token = "test-token"

        with pytest.raises(ContainerServiceError, match="Container not open"):
            service._verify_container_open(container_id, player_id, token)

    def test_verify_container_open_invalid_token(self):
        """Test verification when token is invalid."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()
        correct_token = "correct-token"
        wrong_token = "wrong-token"

        service._open_containers[container_id] = {player_id: correct_token}

        with pytest.raises(ContainerServiceError, match="Invalid mutation token"):
            service._verify_container_open(container_id, player_id, wrong_token)
