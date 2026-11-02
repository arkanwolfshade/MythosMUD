"""Unit tests for hallucination-related services (fake tells, frequency, phantoms)."""

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.lucidity import LucidityActionCode
from server.services.fake_hallucination_service import (
    FAKE_NPC_NAMES,
    FAKE_NPC_TELL_MESSAGES,
    ROOM_TEXT_OVERLAYS,
    FakeHallucinationService,
)
from server.services.hallucination_frequency_service import HallucinationFrequencyService
from server.services.phantom_hostile_service import PHANTOM_HOSTILE_NAMES, PhantomHostileService
from server.tests.fixtures.shared.player_registry import lucidity_registry


def test_fake_hallucination_generate_npc_tell() -> None:
    """Fake tell includes npc name, message, room, and hallucination id."""
    service = FakeHallucinationService()
    player_id = uuid.uuid4()
    result = service.generate_fake_npc_tell(player_id, "room_001")

    assert result["room_id"] == "room_001"
    assert result["npc_name"] in FAKE_NPC_NAMES
    assert result["message"] in FAKE_NPC_TELL_MESSAGES
    assert result["hallucination_id"].startswith(f"fake_tell_{player_id}_")


def test_fake_hallucination_generate_room_overlay() -> None:
    """Room overlay includes text, room, and hallucination id."""
    service = FakeHallucinationService()
    player_id = uuid.uuid4()
    result = service.generate_room_text_overlay(player_id, "room_002")

    assert result["room_id"] == "room_002"
    assert result["overlay_text"] in ROOM_TEXT_OVERLAYS
    assert result["hallucination_id"].startswith(f"room_overlay_{player_id}_")


def _mock_rng(**method_return_values: object) -> MagicMock:
    """A MagicMock standing in for `hallucination_rng.get()`'s `random.Random`."""
    rng = MagicMock()
    for method, value in method_return_values.items():
        setattr(rng, method, MagicMock(return_value=value))
    return rng


def test_fake_hallucination_select_type() -> None:
    """Selection returns one of the two hallucination types."""
    service = FakeHallucinationService()
    with patch(
        "server.services.hallucination_rng.hallucination_rng.get",
        return_value=_mock_rng(choice="fake_npc_tell"),
    ):
        assert service.select_hallucination_type() == "fake_npc_tell"


@pytest.mark.asyncio
async def test_hallucination_frequency_unknown_tier() -> None:
    """Unknown tier never triggers."""
    service = HallucinationFrequencyService()
    assert await service.should_trigger_hallucination(uuid.uuid4(), "lucid", "room_entry") is False


@pytest.mark.asyncio
async def test_hallucination_frequency_wrong_trigger_type() -> None:
    """Tier with mismatched trigger type never triggers."""
    service = HallucinationFrequencyService()
    assert await service.should_trigger_hallucination(uuid.uuid4(), "uneasy", "time_based") is False


@pytest.mark.asyncio
async def test_hallucination_frequency_room_entry_roll() -> None:
    """Room entry uses probability roll without session."""
    service = HallucinationFrequencyService()
    player_id = uuid.uuid4()
    with patch("server.services.hallucination_rng.hallucination_rng.get", return_value=_mock_rng(random=0.05)):
        assert await service.should_trigger_hallucination(player_id, "uneasy", "room_entry") is True
    with patch("server.services.hallucination_rng.hallucination_rng.get", return_value=_mock_rng(random=0.99)):
        assert await service.should_trigger_hallucination(player_id, "uneasy", "room_entry") is False


@pytest.mark.asyncio
async def test_hallucination_frequency_time_based_requires_session() -> None:
    """Time-based checks return False when session is missing."""
    service = HallucinationFrequencyService()
    assert await service.should_trigger_hallucination(uuid.uuid4(), "fractured", "time_based") is False


@pytest.mark.asyncio
async def test_hallucination_frequency_time_based_cooldown_active() -> None:
    """A running hallucination timer blocks the time-based trigger, and nothing commits."""
    player_id = uuid.uuid4()
    harness = lucidity_registry(
        {player_id: None}, cooldowns={LucidityActionCode.HALLUCINATION_TIMER: datetime.now(UTC) + timedelta(minutes=5)}
    )

    with patch("server.services.hallucination_rng.hallucination_rng.get", return_value=_mock_rng(random=0.01)):
        assert (
            await HallucinationFrequencyService().should_trigger_hallucination(
                player_id, "fractured", "time_based", harness.registry
            )
            is False
        )
    assert harness.db.commits == 0


@pytest.mark.asyncio
async def test_hallucination_frequency_time_based_triggers_and_sets_cooldown() -> None:
    """With no timer running a hit starts the timer, committed in the same unit."""
    player_id = uuid.uuid4()
    harness = lucidity_registry({player_id: None})

    with patch("server.services.hallucination_rng.hallucination_rng.get", return_value=_mock_rng(random=0.01)):
        assert (
            await HallucinationFrequencyService().should_trigger_hallucination(
                player_id, "fractured", "time_based", harness.registry
            )
            is True
        )
    expires_at = harness.cooldowns(player_id).expires_at(LucidityActionCode.HALLUCINATION_TIMER)
    assert expires_at is not None and expires_at > datetime.now(UTC)
    assert harness.db.commits == 1


@pytest.mark.asyncio
async def test_hallucination_frequency_a_miss_starts_no_timer() -> None:
    player_id = uuid.uuid4()
    harness = lucidity_registry({player_id: None})

    with patch("server.services.hallucination_rng.hallucination_rng.get", return_value=_mock_rng(random=0.99)):
        assert (
            await HallucinationFrequencyService().should_trigger_hallucination(
                player_id, "fractured", "time_based", harness.registry
            )
            is False
        )
    assert harness.cooldowns(player_id).expires_at(LucidityActionCode.HALLUCINATION_TIMER) is None
    assert harness.db.commits == 0


@pytest.mark.asyncio
async def test_hallucination_frequency_without_a_registry_or_player_returns_false() -> None:
    """No registry, or a player it does not know: the error is swallowed and nothing triggers."""
    service = HallucinationFrequencyService()

    assert await service.should_trigger_hallucination(uuid.uuid4(), "fractured", "time_based") is False
    assert (
        await service.should_trigger_hallucination(
            uuid.uuid4(), "fractured", "time_based", lucidity_registry({}).registry
        )
        is False
    )


@pytest.mark.asyncio
async def test_check_room_entry_delegates_to_should_trigger() -> None:
    """Room entry helper resolves tier and delegates."""
    service = HallucinationFrequencyService()
    player_id = uuid.uuid4()
    with patch.object(service, "should_trigger_hallucination", AsyncMock(return_value=True)) as mock_trigger:
        result = await service.check_room_entry_hallucination(player_id, current_lcd=45)
    assert result is True
    mock_trigger.assert_awaited_once()
    assert mock_trigger.await_args is not None
    assert mock_trigger.await_args.args[2] == "room_entry"


@pytest.mark.asyncio
async def test_check_time_based_delegates_to_should_trigger() -> None:
    """Time-based helper resolves tier and delegates."""
    service = HallucinationFrequencyService()
    player_id = uuid.uuid4()
    registry = lucidity_registry({player_id: None}).registry
    with patch.object(service, "should_trigger_hallucination", AsyncMock(return_value=False)) as mock_trigger:
        result = await service.check_time_based_hallucination(player_id, current_lcd=15, registry=registry)
    assert result is False
    mock_trigger.assert_awaited_once()
    assert mock_trigger.await_args is not None
    assert mock_trigger.await_args.args[2] == "time_based"


def test_phantom_should_spawn_fractured() -> None:
    """Fractured tier uses 15% spawn chance."""
    service = PhantomHostileService()
    with patch("server.services.hallucination_rng.hallucination_rng.get", return_value=_mock_rng(random=0.10)):
        assert service.should_spawn_phantom_hostile("fractured") is True
    with patch("server.services.hallucination_rng.hallucination_rng.get", return_value=_mock_rng(random=0.99)):
        assert service.should_spawn_phantom_hostile("fractured") is False


def test_phantom_should_spawn_deranged() -> None:
    """Deranged tier always allows phantom spawn."""
    service = PhantomHostileService()
    assert service.should_spawn_phantom_hostile("deranged") is True
    assert service.should_spawn_phantom_hostile("lucid") is False


def test_phantom_generate_name() -> None:
    """Generated name comes from phantom name pool."""
    service = PhantomHostileService()
    with patch(
        "server.services.hallucination_rng.hallucination_rng.get",
        return_value=_mock_rng(choice=PHANTOM_HOSTILE_NAMES[0]),
    ):
        assert service.generate_phantom_name() == PHANTOM_HOSTILE_NAMES[0]


def test_phantom_create_track_remove_clear() -> None:
    """Phantom lifecycle: create tracks, remove clears one, clear_all removes all."""
    service = PhantomHostileService()
    player_id = uuid.uuid4()
    data = service.create_phantom_hostile_data(player_id, "room_003", "fractured")

    assert data["room_id"] == "room_003"
    assert data["tier"] == "fractured"
    assert data["is_non_damaging"] is True
    assert data["phantom_id"] in service.get_active_phantoms(player_id)

    assert service.remove_phantom(player_id, data["phantom_id"]) is True
    assert service.get_active_phantoms(player_id) == []
    assert service.remove_phantom(player_id, "missing") is False

    service.create_phantom_hostile_data(player_id, "room_003", "deranged")
    service.clear_all_phantoms(player_id)
    assert service.get_active_phantoms(player_id) == []


def test_phantom_get_data_and_find_by_name_in_room() -> None:
    """#625: get_phantom_data and find_phantom_by_name_in_room support target resolution."""
    service = PhantomHostileService()
    player_id = uuid.uuid4()
    data = service.create_phantom_hostile_data(player_id, "room_005", "deranged")

    assert service.get_phantom_data(data["phantom_id"]) == data
    assert service.get_phantom_data("missing") is None

    found = service.find_phantom_by_name_in_room(player_id, "room_005", data["name"].upper())
    assert found == data
    assert service.find_phantom_by_name_in_room(player_id, "room_999", data["name"]) is None
    assert service.find_phantom_by_name_in_room(player_id, "room_005", "no such phantom") is None


def test_phantom_remove_clears_phantom_data() -> None:
    """#625: remove_phantom/clear_all_phantoms also drop the full-data registry entry."""
    service = PhantomHostileService()
    player_id = uuid.uuid4()
    data = service.create_phantom_hostile_data(player_id, "room_006", "fractured")

    service.remove_phantom(player_id, data["phantom_id"])
    assert service.get_phantom_data(data["phantom_id"]) is None

    data2 = service.create_phantom_hostile_data(player_id, "room_006", "fractured")
    service.clear_all_phantoms(player_id)
    assert service.get_phantom_data(data2["phantom_id"]) is None


def test_phantom_hostile_service_module_singleton() -> None:
    """#625: the module-level instance persists state across separate call sites."""
    from server.services.phantom_hostile_service import phantom_hostile_service

    player_id = uuid.uuid4()
    data = phantom_hostile_service.create_phantom_hostile_data(player_id, "room_007", "deranged")
    try:
        assert data["phantom_id"] in phantom_hostile_service.get_active_phantoms(player_id)
    finally:
        phantom_hostile_service.clear_all_phantoms(player_id)
