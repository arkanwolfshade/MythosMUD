"""Unit tests for hallucination-related services (fake tells, frequency, phantoms)."""

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.fake_hallucination_service import (
    FAKE_NPC_NAMES,
    FAKE_NPC_TELL_MESSAGES,
    ROOM_TEXT_OVERLAYS,
    FakeHallucinationService,
)
from server.services.hallucination_frequency_service import HallucinationFrequencyService
from server.services.phantom_hostile_service import PHANTOM_HOSTILE_NAMES, PhantomHostileService


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


def test_fake_hallucination_select_type() -> None:
    """Selection returns one of the two hallucination types."""
    service = FakeHallucinationService()
    with patch("server.services.fake_hallucination_service.random.choice", return_value="fake_npc_tell"):
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
    with patch("server.services.hallucination_frequency_service.random.random", return_value=0.05):
        assert await service.should_trigger_hallucination(player_id, "uneasy", "room_entry") is True
    with patch("server.services.hallucination_frequency_service.random.random", return_value=0.99):
        assert await service.should_trigger_hallucination(player_id, "uneasy", "room_entry") is False


@pytest.mark.asyncio
async def test_hallucination_frequency_time_based_requires_session() -> None:
    """Time-based checks return False when session is missing."""
    service = HallucinationFrequencyService()
    assert await service.should_trigger_hallucination(uuid.uuid4(), "fractured", "time_based") is False


@pytest.mark.asyncio
async def test_hallucination_frequency_time_based_cooldown_active() -> None:
    """Active cooldown blocks time-based trigger."""
    service = HallucinationFrequencyService()
    player_id = uuid.uuid4()
    session = MagicMock()
    cooldown = MagicMock()
    cooldown.cooldown_expires_at = datetime.now(UTC) + timedelta(minutes=5)

    mock_lucidity = MagicMock()
    mock_lucidity.get_cooldown = AsyncMock(return_value=cooldown)

    with patch("server.services.hallucination_frequency_service.LucidityService", return_value=mock_lucidity):
        assert await service.should_trigger_hallucination(player_id, "fractured", "time_based", session) is False


@pytest.mark.asyncio
async def test_hallucination_frequency_time_based_triggers_and_sets_cooldown() -> None:
    """Expired cooldown allows roll; trigger sets new cooldown."""
    service = HallucinationFrequencyService()
    player_id = uuid.uuid4()
    session = MagicMock()
    mock_lucidity = MagicMock()
    mock_lucidity.get_cooldown = AsyncMock(return_value=None)
    mock_lucidity.set_cooldown = AsyncMock()

    with (
        patch("server.services.hallucination_frequency_service.LucidityService", return_value=mock_lucidity),
        patch("server.services.hallucination_frequency_service.random.random", return_value=0.01),
    ):
        assert await service.should_trigger_hallucination(player_id, "fractured", "time_based", session) is True
    mock_lucidity.set_cooldown.assert_awaited_once()


@pytest.mark.asyncio
async def test_hallucination_frequency_handles_lucidity_errors() -> None:
    """Lucidity service errors are swallowed and return False."""
    service = HallucinationFrequencyService()
    session = MagicMock()
    with patch(
        "server.services.hallucination_frequency_service.LucidityService",
        side_effect=RuntimeError("db down"),
    ):
        assert await service.should_trigger_hallucination(uuid.uuid4(), "fractured", "time_based", session) is False


@pytest.mark.asyncio
async def test_check_room_entry_delegates_to_should_trigger() -> None:
    """Room entry helper resolves tier and delegates."""
    service = HallucinationFrequencyService()
    player_id = uuid.uuid4()
    with patch.object(service, "should_trigger_hallucination", AsyncMock(return_value=True)) as mock_trigger:
        result = await service.check_room_entry_hallucination(player_id, current_lcd=45)
    assert result is True
    mock_trigger.assert_awaited_once()
    assert mock_trigger.await_args.args[2] == "room_entry"


@pytest.mark.asyncio
async def test_check_time_based_delegates_to_should_trigger() -> None:
    """Time-based helper resolves tier and delegates."""
    service = HallucinationFrequencyService()
    player_id = uuid.uuid4()
    session = MagicMock()
    with patch.object(service, "should_trigger_hallucination", AsyncMock(return_value=False)) as mock_trigger:
        result = await service.check_time_based_hallucination(player_id, current_lcd=15, session=session)
    assert result is False
    mock_trigger.assert_awaited_once()
    assert mock_trigger.await_args.args[2] == "time_based"


def test_phantom_should_spawn_fractured() -> None:
    """Fractured tier uses 15% spawn chance."""
    service = PhantomHostileService()
    with patch("server.services.phantom_hostile_service.random.random", return_value=0.10):
        assert service.should_spawn_phantom_hostile("fractured") is True
    with patch("server.services.phantom_hostile_service.random.random", return_value=0.99):
        assert service.should_spawn_phantom_hostile("fractured") is False


def test_phantom_should_spawn_deranged() -> None:
    """Deranged tier always allows phantom spawn."""
    service = PhantomHostileService()
    assert service.should_spawn_phantom_hostile("deranged") is True
    assert service.should_spawn_phantom_hostile("lucid") is False


def test_phantom_generate_name() -> None:
    """Generated name comes from phantom name pool."""
    service = PhantomHostileService()
    with patch("server.services.phantom_hostile_service.random.choice", return_value=PHANTOM_HOSTILE_NAMES[0]):
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
