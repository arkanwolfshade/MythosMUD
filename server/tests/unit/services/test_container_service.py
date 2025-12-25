import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.exceptions import ValidationError
from server.models.container import ContainerLockState, ContainerSourceType
from server.services.container_service import (
    ContainerAccessDeniedError,
    ContainerLockedError,
    ContainerNotFoundError,
    ContainerService,
    ContainerServiceError,
    _filter_container_data,
    _get_enum_value,
)
from server.services.inventory_service import InventoryStack


class _FakePlayer:
    def __init__(self, player_id: uuid.UUID, room_id: str, is_admin: bool = False, inventory=None, name="Tester"):
        self.player_id = player_id
        self.current_room_id = room_id
        self.is_admin = is_admin
        self.inventory = inventory or []
        self.name = name


class _FakePersistence:
    def __init__(self, container_data: dict, player: _FakePlayer):
        self.container_data = container_data
        self.player = player
        self.updated_items = None

    async def get_container(self, container_id):
        return self.container_data

    async def get_player_by_id(self, player_id):
        return self.player

    async def update_container(self, container_id, items_json=None, **kwargs):
        self.updated_items = items_json
        return True


def _make_container(
    lock_state: ContainerLockState = ContainerLockState.UNLOCKED,
    metadata: dict | None = None,
    items=None,
) -> dict:
    return {
        "container_id": uuid.uuid4(),
        "source_type": ContainerSourceType.ENVIRONMENT,
        "room_id": "room-1",
        "capacity_slots": 5,
        "lock_state": lock_state,
        "items": items or [],
        "metadata": metadata or {},
    }


@pytest.mark.asyncio
async def test_open_container_unlocked_allows_access() -> None:
    container_data = _make_container()
    player_id = uuid.uuid4()
    player = _FakePlayer(player_id, room_id="room-1", is_admin=True)
    persistence = _FakePersistence(container_data, player)

    service = ContainerService(persistence=persistence)
    result = await service.open_container(container_data["container_id"], player_id)

    assert "mutation_token" in result
    assert service.get_container_token(container_data["container_id"], player_id) == result["mutation_token"]


@pytest.mark.asyncio
async def test_open_container_locked_requires_key_or_admin() -> None:
    container_data = _make_container(lock_state=ContainerLockState.LOCKED)
    player_id = uuid.uuid4()
    player = _FakePlayer(player_id, room_id="room-1", is_admin=False)
    persistence = _FakePersistence(container_data, player)
    service = ContainerService(persistence=persistence)

    with pytest.raises(ContainerLockedError):
        await service.open_container(container_data["container_id"], player_id)


@pytest.mark.asyncio
async def test_open_container_locked_with_key_succeeds() -> None:
    container_data = _make_container(
        lock_state=ContainerLockState.LOCKED,
        metadata={"key_item_id": "skeleton-key"},
    )
    player_id = uuid.uuid4()
    player = _FakePlayer(
        player_id,
        room_id="room-1",
        is_admin=False,
        inventory=[{"item_id": "skeleton-key"}],
    )
    persistence = _FakePersistence(container_data, player)
    service = ContainerService(persistence=persistence)

    result = await service.open_container(container_data["container_id"], player_id)
    assert "mutation_token" in result


@pytest.mark.asyncio
async def test_transfer_to_container_updates_persistence() -> None:
    container_data = _make_container(items=[])
    player_id = uuid.uuid4()
    player = _FakePlayer(player_id, room_id="room-1", is_admin=True)
    persistence = _FakePersistence(container_data, player)
    service = ContainerService(persistence=persistence)

    open_result = await service.open_container(container_data["container_id"], player_id)
    mutation_token = open_result["mutation_token"]

    item_stack_dict = {
        "item_instance_id": "inst-1",
        "prototype_id": "proto-1",
        "item_id": "artifact-1",
        "item_name": "Elder Sign",
        "slot_type": "bag",
        "quantity": 1,
    }
    # Cast dict to InventoryStack TypedDict for type checker
    item_stack = cast(InventoryStack, item_stack_dict)

    transfer_result = await service.transfer_to_container(
        container_id=container_data["container_id"],
        player_id=player_id,
        mutation_token=mutation_token,
        item=item_stack,
        quantity=1,
    )

    assert persistence.updated_items is not None
    # Mypy incorrectly thinks this is unreachable - false positive due to type narrowing
    assert len(persistence.updated_items) == 1  # type: ignore[unreachable]
    # InventoryService normalizes item_id to prototype_id
    assert transfer_result["container"]["items"][0]["item_id"] == "proto-1"
    assert transfer_result["container"]["items"][0]["quantity"] == 1


class TestGetEnumValue:
    """Test _get_enum_value helper function."""

    def test_get_enum_value_with_enum(self) -> None:
        """Test getting enum value from enum instance."""
        result = _get_enum_value(ContainerLockState.LOCKED)
        assert result == "locked"

    def test_get_enum_value_with_string(self) -> None:
        """Test getting enum value from string."""
        result = _get_enum_value("unlocked")
        assert result == "unlocked"

    def test_get_enum_value_with_none(self) -> None:
        """Test getting enum value from None."""
        result = _get_enum_value(None)
        assert result == "None"


class TestFilterContainerData:
    """Test _filter_container_data helper function."""

    def test_filter_container_data_removes_timestamps(self) -> None:
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

    def test_filter_container_data_converts_items_json(self) -> None:
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

    def test_filter_container_data_converts_metadata_json(self) -> None:
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

    def test_filter_container_data_preserves_other_fields(self) -> None:
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

    def test_container_service_init_defaults(self) -> None:
        """Test ContainerService initialization with defaults."""
        mock_persistence = MagicMock()

        service = ContainerService(persistence=mock_persistence)

        assert service.persistence == mock_persistence
        assert service.inventory_service is not None
        assert service.mutation_guard is not None
        assert service._open_containers == {}

    def test_container_service_init_custom_services(self) -> None:
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

    def test_get_container_token_when_open(self) -> None:
        """Test getting token when container is open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()
        token = "test-token"

        service._open_containers[container_id] = {player_id: token}

        result = service.get_container_token(container_id, player_id)

        assert result == token

    def test_get_container_token_when_not_open(self) -> None:
        """Test getting token when container is not open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()

        result = service.get_container_token(container_id, player_id)

        assert result is None

    def test_get_container_token_when_open_by_different_player(self) -> None:
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

    def test_remove_container_from_open_list_single_player(self) -> None:
        """Test removing container when only one player has it open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()

        service._open_containers[container_id] = {player_id: "token"}

        service._remove_container_from_open_list(container_id, player_id)

        assert container_id not in service._open_containers

    def test_remove_container_from_open_list_multiple_players(self) -> None:
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

    def test_validate_container_close_success(self) -> None:
        """Test validation when container is properly open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()
        token = "test-token"
        context = MagicMock()

        service._open_containers[container_id] = {player_id: token}

        # Should not raise
        service._validate_container_close(container_id, player_id, token, context)

    def test_validate_container_close_not_open(self) -> None:
        """Test validation when container is not open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()
        token = "test-token"
        context = MagicMock()

        with pytest.raises(ContainerServiceError, match="Container not open"):
            service._validate_container_close(container_id, player_id, token, context)

    def test_validate_container_close_wrong_player(self) -> None:
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

    def test_validate_container_close_invalid_token(self) -> None:
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
    async def test_open_container_success(self) -> None:
        """Test successfully opening a container."""
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
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
        mock_persistence.get_container = AsyncMock(return_value=container_data)

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "room-123"
        mock_player.is_admin = False
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)

        service = ContainerService(persistence=mock_persistence)

        with patch("server.services.container_service.audit_logger") as _mock_audit:
            result = await service.open_container(container_id, player_id)

            assert "container" in result
            assert "mutation_token" in result
            assert result["mutation_token"] is not None
            assert container_id in service._open_containers
            assert player_id in service._open_containers[container_id]

    @pytest.mark.asyncio
    async def test_open_container_not_found(self) -> None:
        """Test opening a container that doesn't exist."""
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        container_id = uuid4()
        player_id = uuid4()

        mock_persistence.get_container = AsyncMock(return_value=None)

        service = ContainerService(persistence=mock_persistence)

        with pytest.raises(ContainerNotFoundError, match="Container not found"):
            await service.open_container(container_id, player_id)

    @pytest.mark.asyncio
    async def test_open_container_player_not_found(self) -> None:
        """Test opening a container when player doesn't exist."""
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
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
        mock_persistence.get_container = AsyncMock(return_value=container_data)
        mock_persistence.get_player_by_id = AsyncMock(return_value=None)

        service = ContainerService(persistence=mock_persistence)

        with pytest.raises(ValidationError, match="Player not found"):
            await service.open_container(container_id, player_id)

    @pytest.mark.asyncio
    async def test_open_container_locked(self) -> None:
        """Test opening a locked container."""
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
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
        mock_persistence.get_container = AsyncMock(return_value=container_data)

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "room-123"
        mock_player.is_admin = False
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)

        service = ContainerService(persistence=mock_persistence)

        with pytest.raises(ContainerLockedError, match="Container is locked"):
            await service.open_container(container_id, player_id)

    @pytest.mark.asyncio
    async def test_open_container_sealed(self) -> None:
        """Test opening a sealed container."""
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
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
        mock_persistence.get_container = AsyncMock(return_value=container_data)

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "room-123"
        mock_player.is_admin = False
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)

        service = ContainerService(persistence=mock_persistence)

        with pytest.raises(ContainerAccessDeniedError, match="Container is sealed"):
            await service.open_container(container_id, player_id)

    @pytest.mark.asyncio
    async def test_open_container_already_open(self) -> None:
        """Test opening a container that's already open."""
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
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
        mock_persistence.get_container = AsyncMock(return_value=container_data)

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "room-123"
        mock_player.is_admin = False
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)

        service = ContainerService(persistence=mock_persistence)
        service._open_containers[container_id] = {player_id: "existing-token"}

        with pytest.raises(ContainerServiceError, match="Container already open"):
            await service.open_container(container_id, player_id)


class TestCloseContainer:
    """Test close_container method."""

    @pytest.mark.asyncio
    async def test_close_container_success(self) -> None:
        """Test successfully closing a container."""
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
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
        mock_persistence.get_container = AsyncMock(return_value=container_data)

        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)

        with patch("server.services.container_service.audit_logger"):
            await service.close_container(container_id, player_id, token)

            assert container_id not in service._open_containers

    @pytest.mark.asyncio
    async def test_close_container_not_open(self) -> None:
        """Test closing a container that's not open."""
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        container_id = uuid4()
        player_id = uuid4()
        token = "test-token"

        service = ContainerService(persistence=mock_persistence)

        with pytest.raises(ContainerServiceError, match="Container not open"):
            await service.close_container(container_id, player_id, token)

    @pytest.mark.asyncio
    async def test_close_container_invalid_token(self) -> None:
        """Test closing a container with invalid token."""
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
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

    def test_verify_container_open_success(self) -> None:
        """Test verification when container is properly open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()
        token = "test-token"

        service._open_containers[container_id] = {player_id: token}

        # Should not raise
        service._verify_container_open(container_id, player_id, token)

    def test_verify_container_open_not_open(self) -> None:
        """Test verification when container is not open."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()
        token = "test-token"

        with pytest.raises(ContainerServiceError, match="Container not open"):
            service._verify_container_open(container_id, player_id, token)

    def test_verify_container_open_invalid_token(self) -> None:
        """Test verification when token is invalid."""
        service = ContainerService(persistence=MagicMock())
        container_id = uuid4()
        player_id = uuid4()
        correct_token = "correct-token"
        wrong_token = "wrong-token"

        service._open_containers[container_id] = {player_id: correct_token}

        with pytest.raises(ContainerServiceError, match="Invalid mutation token"):
            service._verify_container_open(container_id, player_id, wrong_token)
