"""
Unit tests for corpse lifecycle service.

Tests the CorpseLifecycleService class.
"""
# pylint: disable=redefined-outer-name,too-many-lines  # Reason: Pytest fixtures use fixture names as parameters. Comprehensive test file with many test cases.
# pyright: reportAny=false
# TEST_MOCK: MagicMock/AsyncMock attribute and call chains (mock_persistence.get_containers_by_entity_id,
# .assert_awaited_once, ...) resolve to Any throughout this file.

import json
import uuid
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.player_registry import DbSession, PlayerAggregate, PlayerRegistry
from server.models.container import ContainerComponent, ContainerLockState, ContainerSourceType
from server.persistence.container_create_params import ContainerCreateParams
from server.services.corpse_lifecycle_service import (
    CorpseLifecycleService,
    CorpseNotFoundError,
    CorpseServiceError,
    _get_enum_value,
)
from server.tests.fixtures.shared.player_registry import FakeDatabase, aggregate, raw_row


@pytest.fixture
def mock_persistence() -> MagicMock:
    """Create a mock persistence layer: no worn containers, and row deletes succeed."""
    persistence = MagicMock()
    persistence.get_containers_by_entity_id = AsyncMock(return_value=[])
    persistence.delete_container = AsyncMock(return_value=True)
    return persistence


@pytest.fixture
def corpse_service(mock_persistence):
    """Create a CorpseLifecycleService instance."""
    return CorpseLifecycleService(persistence=mock_persistence)


def test_get_enum_value_enum():
    """Test _get_enum_value() with enum instance."""
    from enum import Enum

    class TestEnum(Enum):
        """Test enum for _get_enum_value() tests."""

        VALUE1 = "value1"

    result = _get_enum_value(TestEnum.VALUE1)
    assert result == "value1"


def test_get_enum_value_string():
    """Test _get_enum_value() with string."""
    result = _get_enum_value("test_string")
    assert result == "test_string"


def test_corpse_lifecycle_service_init(corpse_service, mock_persistence):
    """Test CorpseLifecycleService initialization."""
    assert corpse_service.persistence == mock_persistence


def test_corpse_lifecycle_service_init_no_persistence():
    """Test CorpseLifecycleService initialization fails without persistence."""
    with pytest.raises(ValueError, match="persistence.*required"):
        CorpseLifecycleService(persistence=None)


def test_corpse_service_error():
    """Test CorpseServiceError exception."""
    error = CorpseServiceError("Test error")
    assert str(error) == "Test error"


def test_corpse_not_found_error():
    """Test CorpseNotFoundError exception."""
    error = CorpseNotFoundError("Corpse not found")
    assert isinstance(error, CorpseServiceError)
    assert str(error) == "Corpse not found"


_MODULE = "server.services.corpse_lifecycle_service"


@dataclass
class _Death:
    """A death against a real PlayerRegistry over the in-memory FakeDatabase; corpse creates and worn deletes are
    recorded (their SQL is covered by tests/integration/test_registry_corpse_death.py)."""

    service: CorpseLifecycleService
    registry: PlayerRegistry
    db: FakeDatabase
    player_id: uuid.UUID
    created: list[tuple[uuid.UUID, ContainerCreateParams]] = field(default_factory=list)
    deleted: list[uuid.UUID] = field(default_factory=list)
    create_error: Exception | None = None

    def created_items(self, n: int = 0) -> list[dict[str, object]]:
        return self.created[n][1].items_json or []

    def saved(self) -> tuple[object, object] | None:
        """(carried, equipped) the death committed for the player, or None if it committed none."""
        write = self.db.last_inventory_write()
        if write is None:
            return None
        return json.loads(str(write["inventory_json"])), json.loads(str(write["equipped_json"]))


def _death(
    monkeypatch: pytest.MonkeyPatch,
    persistence: MagicMock,
    carried: list[dict[str, object]] | None,
    equipped: dict[str, dict[str, object]] | None = None,
    *,
    connection_manager: MagicMock | None = None,
) -> _Death:
    """``carried=None`` means there is no such player."""
    db = FakeDatabase()

    async def load(_session: DbSession, pid: uuid.UUID) -> PlayerAggregate | None:
        if carried is None:
            return None
        row = raw_row(pid, name="Wolfshade", inventory=json.dumps(carried), equipped_json=json.dumps(equipped or {}))
        return aggregate(row)

    registry = PlayerRegistry(db.session, loader=load)
    service = CorpseLifecycleService(
        persistence=persistence, connection_manager=connection_manager, player_registry=registry
    )
    death = _Death(service, registry, db, uuid.uuid4())

    async def create(_session: object, source_type: str, params: ContainerCreateParams) -> uuid.UUID:
        assert source_type == "corpse"
        if death.create_error is not None:
            raise death.create_error
        container_id = uuid.uuid4()
        death.created.append((container_id, params))
        return container_id

    async def delete(_session: object, container_id: uuid.UUID) -> None:
        death.deleted.append(container_id)

    monkeypatch.setattr(f"{_MODULE}.create_container_in_transaction_async", create)
    monkeypatch.setattr(f"{_MODULE}.delete_container_in_transaction_async", delete)
    return death


def _stack(item_id: str, instance_id: str | None = None, slot_type: str = "inventory") -> dict[str, object]:
    return {
        "item_id": item_id,
        "item_name": item_id.title(),
        "slot_type": slot_type,
        "quantity": 1,
        "item_instance_id": instance_id or f"inst-{item_id}",
    }


def _worn_container_row(
    container_instance_id: str, item_instance_id: str, items: list[dict[str, object]]
) -> dict[str, object]:
    """A worn-container row exactly as persistence returns it: items_json/metadata_json, not items/metadata."""
    return {
        "container_id": container_instance_id,
        "source_type": "equipment",
        "owner_id": None,
        "room_id": None,
        "entity_id": str(uuid.uuid4()),
        "lock_state": "unlocked",
        "capacity_slots": 8,
        "weight_limit": None,
        "decay_at": None,
        "allowed_roles": [],
        "items_json": items,
        "metadata_json": {"item_instance_id": item_instance_id, "item_name": "Backpack"},
        "created_at": "2026-09-30T00:00:00+00:00",
        "updated_at": "2026-09-30T00:00:00+00:00",
    }


@pytest.mark.asyncio
async def test_create_corpse_on_death_returns_the_corpse_with_the_new_rows_id(
    monkeypatch: pytest.MonkeyPatch, mock_persistence: MagicMock
) -> None:
    death = _death(monkeypatch, mock_persistence, [_stack("sling")])

    corpse = await death.service.create_corpse_on_death(death.player_id, "room_001")

    [(created_id, params)] = death.created
    assert corpse.container_id == created_id  # the procedure's id, not the placeholder the component was built with
    assert corpse.source_type == ContainerSourceType.CORPSE
    assert corpse.owner_id == params.owner_id == death.player_id
    assert corpse.room_id == params.room_id == "room_001"
    assert corpse.metadata["player_name"] == "Wolfshade"


@pytest.mark.asyncio
async def test_create_corpse_on_death_moves_carried_and_equipped_items_off_the_player_in_one_transaction(
    monkeypatch: pytest.MonkeyPatch, mock_persistence: MagicMock
) -> None:
    """Items are moved, not copied: the corpse and the emptied player commit together (#917, ADR-029)."""
    death = _death(monkeypatch, mock_persistence, [_stack("sling")], {"head": _stack("hat", slot_type="head")})

    _ = await death.service.create_corpse_on_death(death.player_id, "room_001")

    assert [i["item_id"] for i in death.created_items()] == ["sling", "hat"]
    assert death.saved() == ([], {})
    assert death.db.commits == 1
    # Never a whole-row save: it rewrote stats from a Player loaded before the death's DP write
    # landed, reviving the dead player and re-triggering death in a loop (#917).
    mock_persistence.save_player.assert_not_called()


@pytest.mark.asyncio
async def test_create_corpse_on_death_nests_worn_container_contents_and_deletes_its_row(
    monkeypatch: pytest.MonkeyPatch, mock_persistence: MagicMock
) -> None:
    """A worn backpack's live contents travel inside its stack; its equipment row is removed in the same unit."""
    row_id = str(uuid.uuid4())
    coins = _stack("coin", slot_type="backpack")
    mock_persistence.get_containers_by_entity_id = AsyncMock(
        return_value=[_worn_container_row(row_id, "pack-1", [coins])]
    )
    death = _death(monkeypatch, mock_persistence, [], {"back": _stack("backpack", "pack-1", slot_type="back")})

    _ = await death.service.create_corpse_on_death(death.player_id, "room_001")

    (backpack,) = death.created_items()
    assert backpack["inner_container"] == {"capacity_slots": 8, "items": [coins], "lock_state": "unlocked"}
    assert death.deleted == [uuid.UUID(row_id)]
    assert death.db.commits == 1


@pytest.mark.asyncio
async def test_create_corpse_on_death_ignores_worn_rows_for_other_items_and_non_equipment(
    monkeypatch: pytest.MonkeyPatch, mock_persistence: MagicMock
) -> None:
    other_row = _worn_container_row(str(uuid.uuid4()), "some-other-pack", [])
    chest_row = {**_worn_container_row(str(uuid.uuid4()), "pack-1", []), "source_type": "environment"}
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[other_row, chest_row])
    death = _death(monkeypatch, mock_persistence, [], {"back": _stack("backpack", "pack-1", slot_type="back")})

    _ = await death.service.create_corpse_on_death(death.player_id, "room_001")

    (backpack,) = death.created_items()
    assert "inner_container" not in backpack
    assert death.deleted == []


@pytest.mark.asyncio
async def test_create_corpse_on_death_keeps_an_unreadable_worn_row_instead_of_deleting_it(
    monkeypatch: pytest.MonkeyPatch, mock_persistence: MagicMock
) -> None:
    """If a worn row cannot be read, its contents cannot be nested, so the row must survive (#917)."""
    unreadable = {**_worn_container_row(str(uuid.uuid4()), "pack-1", []), "capacity_slots": 999}
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[unreadable])
    death = _death(monkeypatch, mock_persistence, [], {"back": _stack("backpack", "pack-1", slot_type="back")})

    _ = await death.service.create_corpse_on_death(death.player_id, "room_001")

    assert death.deleted == []


@pytest.mark.asyncio
async def test_create_corpse_on_death_leaves_a_worn_row_it_did_not_lock(
    monkeypatch: pytest.MonkeyPatch, mock_persistence: MagicMock
) -> None:
    """A worn row first seen under the player's lock was never locked itself, so the death must not touch it."""
    late_row = _worn_container_row(str(uuid.uuid4()), "pack-1", [_stack("coin", slot_type="backpack")])
    mock_persistence.get_containers_by_entity_id = AsyncMock(side_effect=[[], [late_row]])
    death = _death(monkeypatch, mock_persistence, [], {"back": _stack("backpack", "pack-1", slot_type="back")})

    _ = await death.service.create_corpse_on_death(death.player_id, "room_001")

    (backpack,) = death.created_items()
    assert "inner_container" not in backpack
    assert death.deleted == []


@pytest.mark.asyncio
async def test_create_corpse_on_death_spills_past_the_slot_limit_onto_extra_corpses(
    monkeypatch: pytest.MonkeyPatch, mock_persistence: MagicMock
) -> None:
    """A container holds at most 20 stacks, so 25 are split rather than dropped (#917)."""
    death = _death(monkeypatch, mock_persistence, [_stack(f"item{n}") for n in range(25)])

    result = await death.service.create_corpse_on_death(death.player_id, "room_001")

    assert [len(death.created_items(n)) for n in range(2)] == [20, 5]
    assert result.container_id == death.created[0][0]
    assert death.saved() == ([], {})
    assert death.db.commits == 1


@pytest.mark.asyncio
async def test_create_corpse_on_death_empty_handed_player_still_gets_one_corpse(
    monkeypatch: pytest.MonkeyPatch, mock_persistence: MagicMock
) -> None:
    death = _death(monkeypatch, mock_persistence, [])

    _ = await death.service.create_corpse_on_death(death.player_id, "room_001")

    assert len(death.created) == 1
    assert death.created_items() == []


@pytest.mark.asyncio
async def test_create_corpse_on_death_leaves_the_player_dressed_when_the_corpse_cannot_be_written(
    monkeypatch: pytest.MonkeyPatch, mock_persistence: MagicMock
) -> None:
    """No corpse means nothing may be taken from the player: the whole unit rolls back (#917, ADR-029)."""
    row_id = str(uuid.uuid4())
    mock_persistence.get_containers_by_entity_id = AsyncMock(return_value=[_worn_container_row(row_id, "pack-1", [])])
    connection_manager = MagicMock()
    connection_manager.broadcast_room_event = AsyncMock(return_value={"sent": 1})
    connection_manager.send_personal_message = AsyncMock()
    death = _death(
        monkeypatch,
        mock_persistence,
        [_stack("sling")],
        {"back": _stack("backpack", "pack-1", slot_type="back")},
        connection_manager=connection_manager,
    )
    death.create_error = RuntimeError("db down")

    with pytest.raises(CorpseServiceError, match="Failed to create corpse container"):
        _ = await death.service.create_corpse_on_death(death.player_id, "room_001")

    assert death.db.commits == 0 and death.db.rollbacks == 1
    assert death.deleted == []
    live = death.registry.peek(death.player_id)
    assert live is not None and [s["item_id"] for s in live.inventory.carried] == ["sling"]
    cast(AsyncMock, connection_manager.broadcast_room_event).assert_not_awaited()
    cast(AsyncMock, connection_manager.send_personal_message).assert_not_awaited()


@pytest.mark.asyncio
async def test_create_corpse_on_death_announces_the_corpse_and_the_emptied_inventory(
    monkeypatch: pytest.MonkeyPatch, mock_persistence: MagicMock
) -> None:
    """container.created reaches the room (#711); inventory_updated tells the dead player their hands are empty."""
    connection_manager = MagicMock()
    connection_manager.broadcast_room_event = AsyncMock(return_value={"sent": 1})
    connection_manager.send_personal_message = AsyncMock()
    death = _death(monkeypatch, mock_persistence, [_stack("sling")], connection_manager=connection_manager)

    corpse = await death.service.create_corpse_on_death(death.player_id, "room_001")

    broadcast = cast(AsyncMock, connection_manager.broadcast_room_event)
    broadcast.assert_awaited_once()
    assert broadcast.call_args.kwargs["event_type"] == "container.created"
    assert broadcast.call_args.kwargs["room_id"] == "room_001"
    data = cast(dict[str, object], broadcast.call_args.kwargs["data"])
    # mode="json" so the payload is actually websocket-safe (UUID/datetime -> str); see #711.
    assert cast(dict[str, object], data["container"])["container_id"] == str(corpse.container_id)
    personal = cast(AsyncMock, connection_manager.send_personal_message)
    [(player_id, event)] = [call.args for call in personal.await_args_list]
    assert player_id == death.player_id
    assert event["event_type"] == "inventory_updated"
    assert event["data"] == {"inventory": [], "equipped": {}}


@pytest.mark.asyncio
async def test_create_corpse_on_death_no_connection_manager_skips_emit(
    monkeypatch: pytest.MonkeyPatch, mock_persistence: MagicMock
) -> None:
    death = _death(monkeypatch, mock_persistence, [])

    result = await death.service.create_corpse_on_death(death.player_id, "room_001")

    assert isinstance(result, ContainerComponent)


@pytest.mark.asyncio
async def test_create_corpse_on_death_emit_error_does_not_fail_creation(
    monkeypatch: pytest.MonkeyPatch, mock_persistence: MagicMock
) -> None:
    """A broken connection_manager must not undo or fail a committed death."""
    connection_manager = MagicMock()
    connection_manager.broadcast_room_event = AsyncMock(side_effect=RuntimeError("boom"))
    connection_manager.send_personal_message = AsyncMock(side_effect=RuntimeError("boom"))
    death = _death(monkeypatch, mock_persistence, [_stack("sling")], connection_manager=connection_manager)

    result = await death.service.create_corpse_on_death(death.player_id, "room_001")

    assert isinstance(result, ContainerComponent)
    assert death.saved() == ([], {})


@pytest.mark.asyncio
async def test_create_corpse_on_death_player_not_found(
    monkeypatch: pytest.MonkeyPatch, mock_persistence: MagicMock
) -> None:
    death = _death(monkeypatch, mock_persistence, None)

    with pytest.raises(CorpseServiceError, match="Player not found"):
        _ = await death.service.create_corpse_on_death(death.player_id, "room_001")
    assert death.created == []


@pytest.mark.asyncio
async def test_create_corpse_on_death_without_a_registry_moves_nothing(mock_persistence: MagicMock) -> None:
    service = CorpseLifecycleService(persistence=mock_persistence)

    with pytest.raises(CorpseServiceError, match="No player registry"):
        _ = await service.create_corpse_on_death(uuid.uuid4(), "room_001")


@pytest.mark.asyncio
async def test_create_corpse_on_death_custom_grace_period(
    monkeypatch: pytest.MonkeyPatch, mock_persistence: MagicMock
) -> None:
    death = _death(monkeypatch, mock_persistence, [])

    result = await death.service.create_corpse_on_death(
        death.player_id, "room_001", grace_period_seconds=600, decay_hours=2
    )

    assert result.metadata.get("grace_period_seconds") == 600
    assert result.decay_at is not None
    assert death.created[0][1].metadata_json == result.metadata


def test_can_access_corpse_admin(corpse_service):
    """Test can_access_corpse() allows admin access."""
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
    )
    result = corpse_service.can_access_corpse(corpse, uuid.uuid4(), is_admin=True)
    assert result is True


def test_can_access_corpse_owner(corpse_service):
    """Test can_access_corpse() allows owner access."""
    owner_id = uuid.uuid4()
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=owner_id,
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
    )
    result = corpse_service.can_access_corpse(corpse, owner_id, is_admin=False)
    assert result is True


def test_can_access_corpse_no_owner(corpse_service):
    """Test can_access_corpse() allows access when no owner."""
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=None,
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
    )
    result = corpse_service.can_access_corpse(corpse, uuid.uuid4(), is_admin=False)
    assert result is True


def test_can_access_corpse_grace_period_active(corpse_service):
    """Test can_access_corpse() blocks access during grace period."""
    owner_id = uuid.uuid4()
    other_id = uuid.uuid4()
    now = datetime.now(UTC)
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=owner_id,
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        metadata={
            "grace_period_seconds": 300,
            "grace_period_start": now.isoformat(),
        },
    )
    result = corpse_service.can_access_corpse(corpse, other_id, is_admin=False)
    assert result is False


def test_can_access_corpse_grace_period_expired(corpse_service):
    """Test can_access_corpse() allows access after grace period."""
    owner_id = uuid.uuid4()
    other_id = uuid.uuid4()
    past_time = datetime.now(UTC) - timedelta(seconds=400)
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=owner_id,
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        metadata={
            "grace_period_seconds": 300,
            "grace_period_start": past_time.isoformat(),
        },
    )
    result = corpse_service.can_access_corpse(corpse, other_id, is_admin=False)
    assert result is True


def test_can_access_corpse_invalid_grace_period(corpse_service):
    """Test can_access_corpse() handles invalid grace period gracefully."""
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        metadata={"grace_period_start": "invalid"},
    )
    # Should fail open and allow access
    result = corpse_service.can_access_corpse(corpse, uuid.uuid4(), is_admin=False)
    assert result is True


def test_is_corpse_decayed_not_decayed(corpse_service):
    """Test is_corpse_decayed() returns False for non-decayed corpse."""
    future_time = datetime.now(UTC) + timedelta(hours=1)
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=future_time,
    )
    result = corpse_service.is_corpse_decayed(corpse)
    assert result is False


def test_is_corpse_decayed_decayed(corpse_service):
    """Test is_corpse_decayed() returns True for decayed corpse."""
    past_time = datetime.now(UTC) - timedelta(hours=1)
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=past_time,
    )
    result = corpse_service.is_corpse_decayed(corpse)
    assert result is True


def test_is_corpse_decayed_no_decay_time(corpse_service):
    """Test is_corpse_decayed() returns False when no decay time."""
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=None,
    )
    result = corpse_service.is_corpse_decayed(corpse)
    assert result is False


def test_is_corpse_decayed_uses_real_time_not_mythos_time(corpse_service):
    """Test is_corpse_decayed() uses real UTC time, not Mythos time, even when time service is available."""
    mock_time_service = MagicMock()
    # Mock Mythos time to be far in the future (simulating accelerated time)
    mock_time_service.get_current_mythos_datetime.return_value = datetime.now(UTC) + timedelta(days=10)
    corpse_service.time_service = mock_time_service

    # Corpse decay_at is 1 hour in the past (real time)
    past_time = datetime.now(UTC) - timedelta(hours=1)
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=past_time,
    )

    # Should use real time, so corpse should be decayed (1 hour past)
    result = corpse_service.is_corpse_decayed(corpse)
    assert result is True

    # Verify time service was NOT called (we use real UTC time, not Mythos time)
    mock_time_service.get_current_mythos_datetime.assert_not_called()


def test_can_access_corpse_no_grace_period_start(corpse_service):
    """Test can_access_corpse() allows access when grace_period_start is missing."""
    owner_id = uuid.uuid4()
    other_id = uuid.uuid4()
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=owner_id,
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        metadata={"grace_period_seconds": 300},  # No grace_period_start
    )
    result = corpse_service.can_access_corpse(corpse, other_id, is_admin=False)
    assert result is True


def test_can_access_corpse_grace_period_type_error(corpse_service):
    """Test can_access_corpse() handles TypeError in grace period parsing."""
    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        metadata={"grace_period_start": None},  # None causes TypeError
    )
    # Should fail open and allow access
    result = corpse_service.can_access_corpse(corpse, uuid.uuid4(), is_admin=False)
    assert result is True


def test_is_corpse_decayed_timezone_aware(corpse_service):
    """Test is_corpse_decayed() works correctly with timezone-aware datetimes."""
    # Create decay_at with timezone-aware UTC datetime
    decay_at = datetime.now(UTC) - timedelta(hours=1)
    assert decay_at.tzinfo is not None, "decay_at should be timezone-aware"

    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=decay_at,
    )

    # Should correctly identify as decayed
    result = corpse_service.is_corpse_decayed(corpse)
    assert result is True


def test_is_corpse_decayed_timezone_naive_vs_aware(corpse_service):
    """Test is_corpse_decayed() handles timezone-aware decay_at correctly."""
    # Even if decay_at is timezone-naive (edge case), comparison should work
    # This tests the robustness of the decay check

    # Create a timezone-naive datetime (shouldn't happen in practice, but test edge case)
    naive_decay_at = datetime.now(UTC).replace(tzinfo=None) - timedelta(hours=1)

    corpse = ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id="room_001",
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=naive_decay_at,
    )

    # Should still work - datetime comparison handles naive vs aware
    result = corpse_service.is_corpse_decayed(corpse)
    assert result is True


def _corpse_component(room_id: str = "room_001") -> ContainerComponent:
    return ContainerComponent(
        container_id=uuid.uuid4(),
        source_type=ContainerSourceType.CORPSE,
        owner_id=uuid.uuid4(),
        room_id=room_id,
        capacity_slots=20,
        lock_state=ContainerLockState.UNLOCKED,
        decay_at=datetime.now(UTC) + timedelta(hours=1),
        items=[],
        metadata={"grace_period_seconds": 300, "player_name": "TestPlayer"},
    )


class _RecordingRoom:
    """Room stand-in with real methods: the service checks rooms with a runtime_checkable Protocol,
    which (on Python 3.12+) uses getattr_static and so does not see MagicMock's dynamic attributes."""

    def __init__(self) -> None:
        self.added: list[dict[str, object]] = []
        self.removed: list[str] = []

    def add_container(self, container: dict[str, object]) -> None:
        self.added.append(container)

    def remove_container(self, container_id: str) -> None:
        self.removed.append(container_id)


def test_register_corpse_on_room_adds_summary(mock_persistence: MagicMock) -> None:
    """#711: the owner is dead when container.created fires, so room_state must carry the corpse."""
    room = _RecordingRoom()
    mock_persistence.get_room_by_id = MagicMock(return_value=room)
    service = CorpseLifecycleService(persistence=mock_persistence)
    corpse = _corpse_component()

    service._register_corpse_on_room(corpse, "room_001")  # pyright: ignore[reportPrivateUsage]

    (summary,) = room.added
    assert summary["container_id"] == str(corpse.container_id)
    assert summary["source_type"] == "corpse"
    assert summary["owner_id"] == str(corpse.owner_id)


def test_register_corpse_on_room_skips_async_room_lookup(mock_persistence: MagicMock) -> None:
    """An awaitable room means this layer is async-only here; skip rather than block."""
    awaitable_room = MagicMock()
    awaitable_room.__await__ = MagicMock()
    mock_persistence.get_room_by_id = MagicMock(return_value=awaitable_room)
    service = CorpseLifecycleService(persistence=mock_persistence)

    service._register_corpse_on_room(_corpse_component(), "room_001")  # pyright: ignore[reportPrivateUsage]

    cast(MagicMock, awaitable_room.add_container).assert_not_called()


def test_register_corpse_on_room_survives_missing_room(mock_persistence: MagicMock) -> None:
    """Registration is best-effort: a missing room must not fail corpse creation."""
    mock_persistence.get_room_by_id = MagicMock(return_value=None)
    service = CorpseLifecycleService(persistence=mock_persistence)

    service._register_corpse_on_room(_corpse_component(), "room_001")  # pyright: ignore[reportPrivateUsage]


def test_unregister_corpse_from_room_removes_by_id(mock_persistence: MagicMock) -> None:
    """Decay cleanup drops the corpse from the in-memory room too."""
    room = _RecordingRoom()
    mock_persistence.get_room_by_id = MagicMock(return_value=room)
    service = CorpseLifecycleService(persistence=mock_persistence)

    service._unregister_corpse_from_room("c1", "room_001")  # pyright: ignore[reportPrivateUsage]

    assert room.removed == ["c1"]


def test_register_corpse_on_room_skips_objects_that_are_not_rooms(mock_persistence: MagicMock) -> None:
    """Anything without the Room container methods is skipped, not called."""
    mock_persistence.get_room_by_id = MagicMock(return_value=object())
    service = CorpseLifecycleService(persistence=mock_persistence)

    service._register_corpse_on_room(_corpse_component(), "room_001")  # pyright: ignore[reportPrivateUsage]
    service._unregister_corpse_from_room("c1", "room_001")  # pyright: ignore[reportPrivateUsage]


def test_live_room_returns_none_when_persistence_has_no_sync_lookup() -> None:
    """A persistence layer without get_room_by_id must not raise -- registration is best-effort.

    Guards the hasattr branch of _live_room (it resolves the lookup through the _SyncRoomLookup
    Protocol, so a missing attribute has to be checked before the cast).
    """

    class _NoRoomLookup:
        """Persistence double that deliberately exposes no room lookup."""

    service = CorpseLifecycleService(persistence=_NoRoomLookup())

    assert service._live_room("room_001") is None  # pyright: ignore[reportPrivateUsage]


def test_register_corpse_on_room_without_sync_lookup_is_a_noop() -> None:
    """The same gap seen from the caller: no lookup means no registration, and no exception."""

    class _NoRoomLookup:
        """Persistence double that deliberately exposes no room lookup."""

    service = CorpseLifecycleService(persistence=_NoRoomLookup())

    service._register_corpse_on_room(_corpse_component(), "room_001")  # pyright: ignore[reportPrivateUsage]
