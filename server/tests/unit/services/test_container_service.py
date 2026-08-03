"""Unit tests for container service helpers and validation."""

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.exceptions import ValidationError
from server.models.container import ContainerComponent, ContainerLockState, ContainerSourceType
from server.services.container_service import (
    ContainerAccessDeniedError,
    ContainerCapacityError,
    ContainerLockedError,
    ContainerNotFoundError,
    ContainerService,
    ContainerServiceError,
    _filter_container_data,
    _get_enum_value,
)
from server.services.environmental_container_loader import EnvironmentalContainerLoader


def test_get_enum_value_from_enum():
    assert _get_enum_value(ContainerSourceType.CORPSE) == "corpse"


def test_get_enum_value_from_string():
    assert _get_enum_value("environment") == "environment"


def test_filter_container_data_removes_timestamps_and_renames_json_fields():
    raw = {
        "container_id": str(uuid.uuid4()),
        "source_type": "environment",
        "capacity_slots": 5,
        "created_at": "2026-01-01",
        "updated_at": "2026-01-02",
        "items_json": [{"item_id": "torch"}],
        "metadata_json": {"key": "value"},
    }
    filtered = _filter_container_data(raw)
    assert "created_at" not in filtered
    assert filtered["items"] == [{"item_id": "torch"}]
    assert filtered["metadata"] == {"key": "value"}


def _container(**overrides) -> ContainerComponent:
    data = {
        "container_id": uuid.uuid4(),
        "source_type": ContainerSourceType.ENVIRONMENT,
        "capacity_slots": 5,
        "room_id": "earth_arkham_downtown_001",
    }
    data.update(overrides)
    return ContainerComponent(**data)


@pytest.fixture
def service():
    return ContainerService(persistence=MagicMock())


def test_get_container_token_returns_none_when_not_open(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    assert service.get_container_token(container_id, player_id) is None


def test_get_container_token_returns_stored_token(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    service._open_containers[container_id] = {player_id: "token-123"}
    assert service.get_container_token(container_id, player_id) == "token-123"


def test_verify_container_open_rejects_missing_container(service):
    with pytest.raises(ContainerServiceError):
        service._verify_container_open(uuid.uuid4(), uuid.uuid4(), "token")


def test_verify_container_open_rejects_bad_token(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    service._open_containers[container_id] = {player_id: "good-token"}
    with pytest.raises(ContainerServiceError):
        service._verify_container_open(container_id, player_id, "bad-token")


def test_prepare_transfer_item_reduces_quantity(service):
    item = {"item_id": "torch", "quantity": 5, "slot_type": "backpack"}
    prepared = service._prepare_transfer_item(item, 2)
    assert prepared["quantity"] == 2


def test_validate_proximity_same_room_passes(service):
    container = _container(source_type=ContainerSourceType.ENVIRONMENT, room_id="room_a")
    player = MagicMock(current_room_id="room_a")
    service._validate_proximity(container, player, str(uuid.uuid4()))


def test_validate_proximity_different_room_raises(service):
    container = _container(source_type=ContainerSourceType.ENVIRONMENT, room_id="room_a")
    player = MagicMock(current_room_id="room_b")
    with pytest.raises(ContainerAccessDeniedError):
        service._validate_proximity(container, player, str(uuid.uuid4()))


def test_validate_ownership_equipment_match(service):
    player_id = uuid.uuid4()
    container = _container(source_type=ContainerSourceType.EQUIPMENT, entity_id=player_id)
    service._validate_ownership(container, str(player_id))


def test_validate_ownership_equipment_mismatch_raises(service):
    container = _container(source_type=ContainerSourceType.EQUIPMENT, entity_id=uuid.uuid4())
    with pytest.raises(ContainerAccessDeniedError):
        service._validate_ownership(container, str(uuid.uuid4()))


def test_validate_role_access_denies_player_without_role(service):
    container = _container(allowed_roles=["admin"])
    with pytest.raises(ContainerAccessDeniedError):
        service._validate_role_access(container, str(uuid.uuid4()), is_admin=False)


def test_validate_corpse_grace_period_blocks_non_owner(service):
    owner_id = str(uuid.uuid4())
    container = _container(
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.UUID(owner_id),
        metadata={
            "grace_period_start": datetime.now(UTC).isoformat(),
            "grace_period_seconds": 300,
        },
    )
    with pytest.raises(ContainerAccessDeniedError):
        service._validate_corpse_grace_period(container, str(uuid.uuid4()), is_admin=False)


def test_remove_item_from_container_partial_quantity(service):
    container = _container(
        items=[{"item_id": "torch", "item_instance_id": "inst-1", "quantity": 5, "slot_type": "backpack"}]
    )
    transfer_item = {"item_id": "torch", "item_instance_id": "inst-1", "quantity": 2, "slot_type": "backpack"}
    updated = service._remove_item_from_container(container, transfer_item, container.container_id, uuid.uuid4())
    assert updated[0]["quantity"] == 3


def test_can_unlock_container_admin(service):
    container = _container(lock_state=ContainerLockState.LOCKED)
    player = MagicMock(is_admin=True)
    assert service._can_unlock_container(container, player) is True


def test_can_unlock_container_with_key(service):
    container = _container(lock_state=ContainerLockState.LOCKED, metadata={"key_item_id": "brass_key"})
    player = MagicMock(is_admin=False, inventory=[{"item_id": "brass_key"}])
    assert service._can_unlock_container(container, player) is True


def test_can_unlock_container_locked_without_key(service):
    container = _container(lock_state=ContainerLockState.LOCKED)
    player = MagicMock(is_admin=False, inventory=[])
    assert service._can_unlock_container(container, player) is False


def test_validate_container_access_success(service):
    player_id = uuid.uuid4()
    container = _container(source_type=ContainerSourceType.ENVIRONMENT, room_id="room_a")
    player = MagicMock(spec=["id", "current_room_id", "is_admin"])
    player.id = player_id
    player.current_room_id = "room_a"
    player.is_admin = False
    service._validate_container_access(container, player)


@pytest.mark.asyncio
async def test_open_container_success(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "environment",
        "capacity_slots": 5,
        "room_id": "earth_arkham_downtown_001",
        "lock_state": "unlocked",
        "items_json": [],
        "metadata_json": {},
    }
    player = MagicMock(name="Investigator", current_room_id="earth_arkham_downtown_001", is_admin=False)
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)

    with patch("server.services.container_service.audit_logger.log_container_interaction"):
        result = await service.open_container(container_id, player_id)

    assert "mutation_token" in result
    assert service.get_container_token(container_id, player_id) == result["mutation_token"]


@pytest.mark.asyncio
async def test_open_container_not_found(service):
    service.persistence.get_container = AsyncMock(return_value=None)
    with pytest.raises(ContainerNotFoundError):
        await service.open_container(uuid.uuid4(), uuid.uuid4())


@pytest.mark.asyncio
async def test_open_container_player_not_found(service):
    container_id = uuid.uuid4()
    service.persistence.get_container = AsyncMock(
        return_value={
            "container_id": str(container_id),
            "source_type": "environment",
            "capacity_slots": 5,
            "room_id": "room_a",
            "lock_state": "unlocked",
        }
    )
    service.persistence.get_player_by_id = AsyncMock(return_value=None)
    with pytest.raises(ValidationError):
        await service.open_container(container_id, uuid.uuid4())


@pytest.mark.asyncio
async def test_close_container_audit_failure_still_closes(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "close-token"
    service._open_containers[container_id] = {player_id: token}
    service.persistence.get_container = AsyncMock(return_value=None)

    with patch(
        "server.services.container_service.audit_logger.log_container_interaction",
        side_effect=RuntimeError("audit down"),
    ):
        await service.close_container(container_id, player_id, token)

    assert service.get_container_token(container_id, player_id) is None


@pytest.mark.asyncio
async def test_close_container_logs_audit_when_data_available(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "close-token"
    service._open_containers[container_id] = {player_id: token}
    container_data = {
        "container_id": str(container_id),
        "source_type": "environment",
        "capacity_slots": 5,
        "room_id": "room_a",
        "lock_state": "unlocked",
        "items_json": [],
        "metadata_json": {},
    }
    player = MagicMock(name="Investigator")
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)

    with patch("server.services.container_service.audit_logger.log_container_interaction") as audit_log:
        await service.close_container(container_id, player_id, token)
        audit_log.assert_called_once()

    assert service.get_container_token(container_id, player_id) is None

    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "close-token"
    service._open_containers[container_id] = {player_id: token}
    service.persistence.get_container = AsyncMock(return_value=None)

    await service.close_container(container_id, player_id, token)
    assert service.get_container_token(container_id, player_id) is None


@pytest.mark.asyncio
async def test_close_container_success(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "close-token"
    service._open_containers[container_id] = {player_id: token}
    service.persistence.get_container = AsyncMock(return_value=None)

    await service.close_container(container_id, player_id, token)
    assert service.get_container_token(container_id, player_id) is None


def test_validate_container_close_invalid_token(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    service._open_containers[container_id] = {player_id: "good"}
    with pytest.raises(ContainerServiceError):
        service._validate_container_close(container_id, player_id, "bad")


@pytest.mark.asyncio
async def test_lock_container_updates_state(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "environment",
        "capacity_slots": 5,
        "room_id": "room_a",
        "lock_state": "unlocked",
        "items_json": [],
        "metadata_json": {},
    }
    player = MagicMock(is_admin=True, current_room_id="room_a")
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)
    service.persistence.update_container = AsyncMock(
        return_value={
            "container_id": str(container_id),
            "source_type": "environment",
            "capacity_slots": 5,
            "room_id": "room_a",
            "lock_state": "locked",
            "items_json": [],
            "metadata_json": {},
        }
    )

    with patch("server.services.container_service.audit_logger.log_container_interaction"):
        result = await service.lock_container(container_id, player_id, ContainerLockState.LOCKED)
        assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_open_container_locked_without_key(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "environment",
        "capacity_slots": 5,
        "room_id": "earth_arkham_downtown_001",
        "lock_state": "locked",
        "items_json": [],
        "metadata_json": {},
    }
    player = MagicMock(spec=["name", "current_room_id", "is_admin", "inventory"])
    player.name = "Investigator"
    player.current_room_id = "earth_arkham_downtown_001"
    player.is_admin = False
    player.inventory = []
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)

    with pytest.raises(ContainerLockedError):
        await service.open_container(container_id, player_id)


@pytest.mark.asyncio
async def test_open_container_already_open(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    service._open_containers[container_id] = {player_id: "existing"}
    container_data = {
        "container_id": str(container_id),
        "source_type": "environment",
        "capacity_slots": 5,
        "room_id": "earth_arkham_downtown_001",
        "lock_state": "unlocked",
        "items_json": [],
        "metadata_json": {},
    }
    player = MagicMock(spec=["name", "current_room_id", "is_admin"])
    player.name = "Investigator"
    player.current_room_id = "earth_arkham_downtown_001"
    player.is_admin = False
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)

    with pytest.raises(ContainerServiceError):
        await service.open_container(container_id, player_id)


@pytest.mark.asyncio
async def test_open_container_sealed_non_admin(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "environment",
        "capacity_slots": 5,
        "room_id": "earth_arkham_downtown_001",
        "lock_state": "sealed",
        "items_json": [],
        "metadata_json": {},
    }
    player = MagicMock(spec=["name", "current_room_id", "is_admin"])
    player.name = "Investigator"
    player.current_room_id = "earth_arkham_downtown_001"
    player.is_admin = False
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)

    with pytest.raises(ContainerAccessDeniedError):
        await service.open_container(container_id, player_id)


@pytest.mark.asyncio
async def test_unlock_container_success(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "environment",
        "capacity_slots": 5,
        "room_id": "room_a",
        "lock_state": "locked",
        "items_json": [],
        "metadata_json": {},
    }
    player = MagicMock(spec=["is_admin", "inventory", "id", "current_room_id"])
    player.is_admin = True
    player.inventory = []
    player.id = player_id
    player.current_room_id = "room_a"
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)
    service.persistence.update_container = MagicMock(return_value={**container_data, "lock_state": "unlocked"})

    result = await service.unlock_container(container_id, player_id)
    assert result["lock_state"] == "unlocked"


def test_verify_container_open_success(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    service._open_containers[container_id] = {player_id: "token-ok"}
    service._verify_container_open(container_id, player_id, "token-ok")


def test_remove_container_from_open_list_clears_empty(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    service._open_containers[container_id] = {player_id: "token"}
    service._remove_container_from_open_list(container_id, player_id)
    assert container_id not in service._open_containers


def test_validate_corpse_grace_period_expired_allows_other_player(service):
    owner_id = str(uuid.uuid4())
    container = _container(
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.UUID(owner_id),
        metadata={
            "grace_period_start": (datetime.now(UTC) - timedelta(seconds=600)).isoformat(),
            "grace_period_seconds": 300,
        },
    )
    service._validate_corpse_grace_period(container, str(uuid.uuid4()), is_admin=False)


@pytest.mark.asyncio
async def test_transfer_to_container_success(service):
    from contextlib import asynccontextmanager

    from server.services.inventory_mutation_guard import MutationDecision

    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "transfer-token"
    service._open_containers[container_id] = {player_id: token}

    container_data = {
        "container_id": str(container_id),
        "source_type": "environment",
        "capacity_slots": 5,
        "room_id": "room_a",
        "lock_state": "unlocked",
        "items_json": [],
        "metadata_json": {},
    }
    player = MagicMock(spec=["name", "inventory"])
    player.name = "Investigator"
    player.inventory = []
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)
    service.persistence.update_container = AsyncMock(return_value=container_data)

    item = {"item_id": "torch", "quantity": 1, "slot_type": "backpack", "item_name": "Torch"}

    @asynccontextmanager
    async def fake_acquire(_player_id, _token):
        yield MutationDecision(should_apply=True, duplicate=False)

    service.mutation_guard.acquire_async = fake_acquire

    with patch("server.services.container_service.audit_logger.log_container_interaction"):
        result = await service.transfer_to_container(container_id, player_id, token, item, quantity=1)

    assert "container" in result
    service.persistence.update_container.assert_awaited()


@pytest.mark.asyncio
async def test_transfer_to_container_non_dict_container_data(service):
    from contextlib import asynccontextmanager

    from server.services.inventory_mutation_guard import MutationDecision

    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "transfer-token"
    service._open_containers[container_id] = {player_id: token}
    service.persistence.get_container = AsyncMock(return_value="not-a-dict")
    item = {"item_id": "torch", "quantity": 1, "slot_type": "backpack"}

    @asynccontextmanager
    async def fake_acquire(_player_id, _token):
        yield MutationDecision(should_apply=True, duplicate=False)

    service.mutation_guard.acquire_async = fake_acquire

    with pytest.raises((TypeError, AttributeError, ContainerServiceError)):
        await service.transfer_to_container(container_id, player_id, token, item)


@pytest.mark.asyncio
async def test_transfer_to_container_not_found(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "transfer-token"
    service._open_containers[container_id] = {player_id: token}
    service.persistence.get_container = AsyncMock(return_value=None)
    item = {"item_id": "torch", "quantity": 1, "slot_type": "backpack"}
    with pytest.raises(ContainerNotFoundError):
        await service.transfer_to_container(container_id, player_id, token, item)


@pytest.mark.asyncio
async def test_transfer_to_container_capacity_exceeded(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "transfer-token"
    service._open_containers[container_id] = {player_id: token}
    container_data = {
        "container_id": str(container_id),
        "source_type": "environment",
        "capacity_slots": 1,
        "room_id": "room_a",
        "lock_state": "unlocked",
        "items_json": [{"item_id": "filled", "quantity": 1, "slot_type": "backpack"}],
        "metadata_json": {},
    }
    service.persistence.get_container = AsyncMock(return_value=container_data)
    item = {"item_id": "torch", "quantity": 1, "slot_type": "backpack"}
    with pytest.raises(ContainerCapacityError):
        await service.transfer_to_container(container_id, player_id, token, item)


@pytest.mark.asyncio
async def test_transfer_to_container_mutation_guard_suppressed(service):
    from contextlib import asynccontextmanager

    from server.services.inventory_mutation_guard import MutationDecision

    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "transfer-token"
    service._open_containers[container_id] = {player_id: token}
    container_data = {
        "container_id": str(container_id),
        "source_type": "environment",
        "capacity_slots": 5,
        "room_id": "room_a",
        "lock_state": "unlocked",
        "items_json": [],
        "metadata_json": {},
    }
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=MagicMock(name="Investigator", inventory=[]))
    item = {"item_id": "torch", "quantity": 1, "slot_type": "backpack"}

    @asynccontextmanager
    async def suppressed(_player_id, _token):
        yield MutationDecision(should_apply=False, duplicate=True)

    service.mutation_guard.acquire_async = suppressed
    with pytest.raises(ContainerServiceError):
        await service.transfer_to_container(container_id, player_id, token, item)


def test_validate_container_close_not_open(service):
    with pytest.raises(ContainerServiceError):
        service._validate_container_close(uuid.uuid4(), uuid.uuid4(), "token")


def test_validate_container_close_wrong_player(service):
    container_id = uuid.uuid4()
    service._open_containers[container_id] = {uuid.uuid4(): "token"}
    with pytest.raises(ContainerServiceError):
        service._validate_container_close(container_id, uuid.uuid4(), "token")


@pytest.mark.asyncio
async def test_open_container_audit_failure_still_succeeds(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    container_data = {
        "container_id": str(container_id),
        "source_type": "environment",
        "capacity_slots": 5,
        "room_id": "earth_arkham_downtown_001",
        "lock_state": "unlocked",
        "items_json": [],
        "metadata_json": {},
    }
    player = MagicMock(spec=["name", "current_room_id", "is_admin"])
    player.name = "Investigator"
    player.current_room_id = "earth_arkham_downtown_001"
    player.is_admin = False
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)

    with patch(
        "server.services.container_service.audit_logger.log_container_interaction",
        side_effect=RuntimeError("audit down"),
    ):
        result = await service.open_container(container_id, player_id)

    assert "mutation_token" in result


@pytest.mark.asyncio
async def test_transfer_to_container_player_not_found(service):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "transfer-token"
    service._open_containers[container_id] = {player_id: token}
    container_data = {
        "container_id": str(container_id),
        "source_type": "environment",
        "capacity_slots": 5,
        "room_id": "room_a",
        "lock_state": "unlocked",
        "items_json": [],
        "metadata_json": {},
    }
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=None)
    item = {"item_id": "torch", "quantity": 1, "slot_type": "backpack"}
    with pytest.raises(ValidationError):
        await service.transfer_to_container(container_id, player_id, token, item)


# --- EnvironmentalContainerLoader ---


def test_environmental_loader_requires_persistence() -> None:
    with pytest.raises(ValueError, match="persistence"):
        EnvironmentalContainerLoader()


def test_load_container_from_room_json_none_when_missing() -> None:
    loader = EnvironmentalContainerLoader(persistence=MagicMock())
    assert loader.load_container_from_room_json({}, "room-a") is None


def test_load_container_from_room_json_disabled() -> None:
    loader = EnvironmentalContainerLoader(persistence=MagicMock())
    room_json = {"id": "room-a", "container": {"enabled": False}}
    assert loader.load_container_from_room_json(room_json, "room-a") is None


def test_load_container_from_room_json_success() -> None:
    loader = EnvironmentalContainerLoader(persistence=MagicMock())
    room_json = {
        "id": "room-a",
        "container": {
            "capacity_slots": 10,
            "lock_state": "locked",
            "key_item_id": "key-1",
            "allowed_roles": ["investigator"],
        },
    }
    container = loader.load_container_from_room_json(room_json, "room-a")
    assert container is not None
    assert container.capacity_slots == 10
    assert container.lock_state == ContainerLockState.LOCKED
    assert container.metadata["key_item_id"] == "key-1"


def test_load_container_from_room_json_invalid_capacity() -> None:
    loader = EnvironmentalContainerLoader(persistence=MagicMock())
    room_json = {"id": "room-a", "container": {"capacity_slots": 99}}
    with pytest.raises(ValidationError):
        loader.load_container_from_room_json(room_json, "room-a")


def test_load_container_from_room_json_invalid_lock_state() -> None:
    loader = EnvironmentalContainerLoader(persistence=MagicMock())
    room_json = {"id": "room-a", "container": {"lock_state": "broken"}}
    with pytest.raises(ValidationError):
        loader.load_container_from_room_json(room_json, "room-a")


@pytest.mark.asyncio
async def test_migrate_room_container_existing() -> None:
    existing_id = uuid.uuid4()
    persistence = MagicMock()
    persistence.get_containers_by_room_id = AsyncMock(
        return_value=[{"source_type": "environment", "container_id": str(existing_id)}]
    )
    loader = EnvironmentalContainerLoader(persistence=persistence)
    room_json = {"id": "room-a", "container": {"capacity_slots": 5}}
    result = await loader.migrate_room_container_to_postgresql(room_json, "room-a")
    assert result == existing_id
    persistence.create_container.assert_not_called()


@pytest.mark.asyncio
async def test_migrate_room_container_creates_new() -> None:
    persistence = MagicMock()
    persistence.get_containers_by_room_id = AsyncMock(return_value=[])
    new_id = uuid.uuid4()
    persistence.create_container = AsyncMock(return_value={"container_id": str(new_id)})
    loader = EnvironmentalContainerLoader(persistence=persistence)
    room_json = {"id": "room-a", "container": {"capacity_slots": 5}}
    result = await loader.migrate_room_container_to_postgresql(room_json, "room-a")
    assert result == new_id


@pytest.mark.asyncio
async def test_load_containers_for_room_filters_environment() -> None:
    persistence = MagicMock()
    container_id = uuid.uuid4()
    persistence.get_containers_by_room_id = AsyncMock(
        return_value=[
            {
                "container_id": str(container_id),
                "source_type": "environment",
                "capacity_slots": 5,
                "room_id": "room-a",
                "lock_state": "unlocked",
                "items": [],
                "metadata": {},
            },
            {"container_id": str(uuid.uuid4()), "source_type": "corpse", "capacity_slots": 3},
        ]
    )
    loader = EnvironmentalContainerLoader(persistence=persistence)
    containers = await loader.load_containers_for_room("room-a")
    assert len(containers) == 1
    assert containers[0].container_id == container_id
