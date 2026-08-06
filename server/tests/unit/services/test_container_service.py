"""Unit tests for container service helpers and validation."""

# pylint: disable=protected-access  # Reason: White-box unit tests exercise internal guards
# pyright: reportPrivateUsage=false

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
    filter_container_data,
    get_enum_value,
)
from server.services.inventory_service import InventoryStack


def _stack(
    *,
    item_id: str = "torch",
    quantity: int = 1,
    slot_type: str = "backpack",
    item_instance_id: str = "inst-1",
    prototype_id: str | None = None,
    item_name: str | None = None,
) -> InventoryStack:
    """Minimal InventoryStack for unit tests (all required TypedDict keys)."""
    return {
        "item_instance_id": item_instance_id,
        "prototype_id": prototype_id or item_id,
        "item_id": item_id,
        "item_name": item_name or item_id.replace("_", " ").title(),
        "slot_type": slot_type,
        "quantity": quantity,
    }


def _container_data(
    container_id: uuid.UUID | str,
    *,
    source_type: str = "environment",
    capacity_slots: int = 5,
    room_id: str = "earth_arkham_downtown_001",
    lock_state: str = "unlocked",
    items_json: list[object] | None = None,
    metadata_json: dict[str, object] | None = None,
) -> dict[str, object]:
    """Dict-shaped container row for persistence mocks (avoids Unknown empty list/dict)."""
    return {
        "container_id": str(container_id),
        "source_type": source_type,
        "capacity_slots": capacity_slots,
        "room_id": room_id,
        "lock_state": lock_state,
        "items_json": list[object]() if items_json is None else items_json,
        "metadata_json": dict[str, object]() if metadata_json is None else metadata_json,
    }


def test_get_enum_value_from_enum():

    assert get_enum_value(ContainerSourceType.CORPSE) == "corpse"


def test_get_enum_value_from_string():
    assert get_enum_value("environment") == "environment"


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
    filtered = filter_container_data(raw)
    assert "created_at" not in filtered
    assert filtered["items"] == [{"item_id": "torch"}]
    assert filtered["metadata"] == {"key": "value"}


def _container(**overrides: object) -> ContainerComponent:
    # Build with typed kwargs first; **union dict into __init__ confuses basedpyright on UUID.
    base = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.ENVIRONMENT,
        capacity_slots=5,
        room_id="earth_arkham_downtown_001",
    )
    if not overrides:
        return base
    return base.model_copy(update=dict(overrides))


@pytest.fixture
def service() -> ContainerService:
    return ContainerService(persistence=MagicMock())


def test_get_container_token_returns_none_when_not_open(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    assert service.get_container_token(container_id, player_id) is None


def test_get_container_token_returns_stored_token(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    _ = service.register_open_session(container_id, player_id, "token-123")
    assert service.get_container_token(container_id, player_id) == "token-123"


def test_verify_container_open_rejects_missing_container(service: ContainerService):
    with pytest.raises(ContainerServiceError):
        service._verify_container_open(uuid.uuid4(), uuid.uuid4(), "token")


def test_verify_container_open_rejects_bad_token(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    _ = service.register_open_session(container_id, player_id, "good-token")
    with pytest.raises(ContainerServiceError):
        service._verify_container_open(container_id, player_id, "bad-token")


def test_prepare_transfer_item_reduces_quantity(service: ContainerService):
    prepared = service._prepare_transfer_item(_stack(quantity=5), 2)
    assert prepared["quantity"] == 2


def test_validate_proximity_same_room_passes(service: ContainerService):
    container = _container(source_type=ContainerSourceType.ENVIRONMENT, room_id="room_a")
    player = MagicMock(current_room_id="room_a")
    service._validate_proximity(container, player, str(uuid.uuid4()))


def test_validate_proximity_different_room_raises(service: ContainerService):
    container = _container(source_type=ContainerSourceType.ENVIRONMENT, room_id="room_a")
    player = MagicMock(current_room_id="room_b")
    with pytest.raises(ContainerAccessDeniedError):
        service._validate_proximity(container, player, str(uuid.uuid4()))


def test_validate_ownership_equipment_match(service: ContainerService):
    player_id = uuid.uuid4()
    container = _container(source_type=ContainerSourceType.EQUIPMENT, entity_id=player_id)
    service._validate_ownership(container, str(player_id))


def test_validate_ownership_equipment_mismatch_raises(service: ContainerService):
    container = _container(source_type=ContainerSourceType.EQUIPMENT, entity_id=uuid.uuid4())
    with pytest.raises(ContainerAccessDeniedError):
        service._validate_ownership(container, str(uuid.uuid4()))


def test_validate_role_access_denies_player_without_role(service: ContainerService):
    container = _container(allowed_roles=["admin"])
    with pytest.raises(ContainerAccessDeniedError):
        service._validate_role_access(container, str(uuid.uuid4()), is_admin=False)


def test_validate_corpse_grace_period_blocks_non_owner(service: ContainerService):
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


def test_remove_item_from_container_partial_quantity(service: ContainerService):
    container = _container(items=[_stack(quantity=5)])
    transfer_item = _stack(quantity=2)
    updated = service._remove_item_from_container(container, transfer_item, container.container_id, uuid.uuid4())
    assert updated[0]["quantity"] == 3


def test_can_unlock_container_admin(service: ContainerService):
    container = _container(lock_state=ContainerLockState.LOCKED)
    player = MagicMock(is_admin=True)
    assert service._can_unlock_container(container, player) is True


def test_can_unlock_container_with_key(service: ContainerService):
    container = _container(lock_state=ContainerLockState.LOCKED, metadata={"key_item_id": "brass_key"})
    player = MagicMock(is_admin=False, inventory=[{"item_id": "brass_key"}])
    assert service._can_unlock_container(container, player) is True


def test_can_unlock_container_locked_without_key(service: ContainerService):
    container = _container(lock_state=ContainerLockState.LOCKED)
    player = MagicMock(is_admin=False, inventory=[])
    assert service._can_unlock_container(container, player) is False


def test_validate_container_access_success(service: ContainerService):
    player_id = uuid.uuid4()
    container = _container(source_type=ContainerSourceType.ENVIRONMENT, room_id="room_a")
    player = MagicMock(spec=["id", "current_room_id", "is_admin"])
    player.id = player_id
    player.current_room_id = "room_a"
    player.is_admin = False
    service._validate_container_access(container, player)


@pytest.mark.asyncio
async def test_open_container_success(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    container_data = _container_data(container_id)
    player = MagicMock(name="Investigator", current_room_id="earth_arkham_downtown_001", is_admin=False)
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)

    with patch("server.services.container_service.audit_logger.log_container_interaction"):
        result = await service.open_container(container_id, player_id)

    assert "mutation_token" in result
    assert service.get_container_token(container_id, player_id) == result["mutation_token"]


@pytest.mark.asyncio
async def test_open_container_not_found(service: ContainerService):
    service.persistence.get_container = AsyncMock(return_value=None)
    with pytest.raises(ContainerNotFoundError):
        _ = await service.open_container(uuid.uuid4(), uuid.uuid4())


@pytest.mark.asyncio
async def test_open_container_player_not_found(service: ContainerService):
    container_id = uuid.uuid4()
    service.persistence.get_container = AsyncMock(return_value=_container_data(container_id, room_id="room_a"))
    service.persistence.get_player_by_id = AsyncMock(return_value=None)
    with pytest.raises(ValidationError):
        _ = await service.open_container(container_id, uuid.uuid4())


@pytest.mark.asyncio
async def test_close_container_audit_failure_still_closes(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "close-token"
    _ = service.register_open_session(container_id, player_id, token)
    service.persistence.get_container = AsyncMock(return_value=None)

    with patch(
        "server.services.container_service.audit_logger.log_container_interaction",
        side_effect=RuntimeError("audit down"),
    ):
        await service.close_container(container_id, player_id, token)

    assert service.get_container_token(container_id, player_id) is None


@pytest.mark.asyncio
async def test_close_container_logs_audit_when_data_available(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "close-token"
    _ = service.register_open_session(container_id, player_id, token)
    container_data = _container_data(container_id, room_id="room_a")
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
    _ = service.register_open_session(container_id, player_id, token)
    service.persistence.get_container = AsyncMock(return_value=None)

    await service.close_container(container_id, player_id, token)
    assert service.get_container_token(container_id, player_id) is None


@pytest.mark.asyncio
async def test_close_container_success(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "close-token"
    _ = service.register_open_session(container_id, player_id, token)
    service.persistence.get_container = AsyncMock(return_value=None)

    await service.close_container(container_id, player_id, token)
    assert service.get_container_token(container_id, player_id) is None


def test_validate_container_close_invalid_token(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    _ = service.register_open_session(container_id, player_id, "good")
    with pytest.raises(ContainerServiceError):
        service._validate_container_close(container_id, player_id, "bad")


@pytest.mark.asyncio
async def test_lock_container_updates_state(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    container_data = _container_data(container_id, room_id="room_a")
    player = MagicMock(is_admin=True, current_room_id="room_a")
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)
    service.persistence.update_container = AsyncMock(
        return_value=_container_data(container_id, room_id="room_a", lock_state="locked")
    )

    with patch("server.services.container_service.audit_logger.log_container_interaction"):
        result = await service.lock_container(container_id, player_id, ContainerLockState.LOCKED)
        assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_open_container_locked_without_key(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    container_data = _container_data(container_id, lock_state="locked")
    player = MagicMock(spec=["name", "current_room_id", "is_admin", "inventory"])
    player.name = "Investigator"
    player.current_room_id = "earth_arkham_downtown_001"
    player.is_admin = False
    player.inventory = []
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)

    with pytest.raises(ContainerLockedError):
        _ = await service.open_container(container_id, player_id)


@pytest.mark.asyncio
async def test_open_container_already_open(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    _ = service.register_open_session(container_id, player_id, "existing")
    container_data = _container_data(container_id)
    player = MagicMock(spec=["name", "current_room_id", "is_admin"])
    player.name = "Investigator"
    player.current_room_id = "earth_arkham_downtown_001"
    player.is_admin = False
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)

    with pytest.raises(ContainerServiceError):
        _ = await service.open_container(container_id, player_id)


@pytest.mark.asyncio
async def test_open_container_sealed_non_admin(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    container_data = _container_data(container_id, lock_state="sealed")
    player = MagicMock(spec=["name", "current_room_id", "is_admin"])
    player.name = "Investigator"
    player.current_room_id = "earth_arkham_downtown_001"
    player.is_admin = False
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)

    with pytest.raises(ContainerAccessDeniedError):
        _ = await service.open_container(container_id, player_id)


@pytest.mark.asyncio
async def test_unlock_container_success(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    container_data = _container_data(container_id, room_id="room_a", lock_state="locked")
    player = MagicMock(spec=["is_admin", "inventory", "id", "current_room_id"])
    player.is_admin = True
    player.inventory = []
    player.id = player_id
    player.current_room_id = "room_a"
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)
    service.persistence.update_container = AsyncMock(return_value={**container_data, "lock_state": "unlocked"})

    result = await service.unlock_container(container_id, player_id)
    assert result["lock_state"] == "unlocked"


def test_verify_container_open_success(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    _ = service.register_open_session(container_id, player_id, "token-ok")
    service._verify_container_open(container_id, player_id, "token-ok")


def test_remove_container_from_open_list_clears_empty(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    _ = service.register_open_session(container_id, player_id, "token")
    service._remove_container_from_open_list(container_id, player_id)
    assert service.get_container_token(container_id, player_id) is None


def test_validate_corpse_grace_period_expired_allows_other_player(service: ContainerService):
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
async def test_transfer_to_container_success(service: ContainerService):
    from contextlib import asynccontextmanager

    from server.services.inventory_mutation_guard import MutationDecision

    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "transfer-token"
    _ = service.register_open_session(container_id, player_id, token)

    container_data = _container_data(container_id, room_id="room_a")
    player = MagicMock(spec=["name", "inventory"])
    player.name = "Investigator"
    player.inventory = []
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=player)
    service.persistence.update_container = AsyncMock(return_value=container_data)

    item = _stack(item_name="Torch")

    @asynccontextmanager
    async def fake_acquire(player_id: str, token: str | None):
        _ = (player_id, token)
        yield MutationDecision(should_apply=True, duplicate=False)

    service.mutation_guard.acquire_async = fake_acquire

    with patch("server.services.container_service.audit_logger.log_container_interaction"):
        result = await service.transfer_to_container(container_id, player_id, token, item, quantity=1)

    assert "container" in result
    service.persistence.update_container.assert_awaited()


@pytest.mark.asyncio
async def test_transfer_to_container_non_dict_container_data(service: ContainerService):
    from contextlib import asynccontextmanager

    from server.services.inventory_mutation_guard import MutationDecision

    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "transfer-token"
    _ = service.register_open_session(container_id, player_id, token)
    service.persistence.get_container = AsyncMock(return_value="not-a-dict")
    item = _stack()

    @asynccontextmanager
    async def fake_acquire(player_id: str, token: str | None):
        _ = (player_id, token)
        yield MutationDecision(should_apply=True, duplicate=False)

    service.mutation_guard.acquire_async = fake_acquire

    with pytest.raises((TypeError, AttributeError, ContainerServiceError)):
        _ = await service.transfer_to_container(container_id, player_id, token, item)


@pytest.mark.asyncio
async def test_transfer_to_container_not_found(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "transfer-token"
    _ = service.register_open_session(container_id, player_id, token)
    service.persistence.get_container = AsyncMock(return_value=None)
    item = _stack()
    with pytest.raises(ContainerNotFoundError):
        _ = await service.transfer_to_container(container_id, player_id, token, item)


@pytest.mark.asyncio
async def test_transfer_to_container_capacity_exceeded(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "transfer-token"
    _ = service.register_open_session(container_id, player_id, token)
    container_data = _container_data(
        container_id,
        capacity_slots=1,
        room_id="room_a",
        items_json=[{"item_id": "filled", "quantity": 1, "slot_type": "backpack"}],
    )
    service.persistence.get_container = AsyncMock(return_value=container_data)
    item = _stack()
    with pytest.raises(ContainerCapacityError):
        _ = await service.transfer_to_container(container_id, player_id, token, item)


@pytest.mark.asyncio
async def test_transfer_to_container_mutation_guard_suppressed(service: ContainerService):
    from contextlib import asynccontextmanager

    from server.services.inventory_mutation_guard import MutationDecision

    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "transfer-token"
    _ = service.register_open_session(container_id, player_id, token)
    container_data = _container_data(container_id, room_id="room_a")
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=MagicMock(name="Investigator", inventory=[]))
    item = _stack()

    @asynccontextmanager
    async def suppressed(player_id: str, token: str | None):
        _ = (player_id, token)
        yield MutationDecision(should_apply=False, duplicate=True)

    service.mutation_guard.acquire_async = suppressed
    with pytest.raises(ContainerServiceError):
        _ = await service.transfer_to_container(container_id, player_id, token, item)


def test_validate_container_close_not_open(service: ContainerService):
    with pytest.raises(ContainerServiceError):
        service._validate_container_close(uuid.uuid4(), uuid.uuid4(), "token")


def test_validate_container_close_wrong_player(service: ContainerService):
    container_id = uuid.uuid4()
    other_player = uuid.uuid4()
    _ = service.register_open_session(container_id, other_player, "token")
    with pytest.raises(ContainerServiceError):
        service._validate_container_close(container_id, uuid.uuid4(), "token")


@pytest.mark.asyncio
async def test_open_container_audit_failure_still_succeeds(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    container_data = _container_data(container_id)
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
async def test_transfer_to_container_player_not_found(service: ContainerService):
    container_id = uuid.uuid4()
    player_id = uuid.uuid4()
    token = "transfer-token"
    _ = service.register_open_session(container_id, player_id, token)
    container_data = _container_data(container_id, room_id="room_a")
    service.persistence.get_container = AsyncMock(return_value=container_data)
    service.persistence.get_player_by_id = AsyncMock(return_value=None)
    item = _stack()
    with pytest.raises(ValidationError):
        _ = await service.transfer_to_container(container_id, player_id, token, item)
