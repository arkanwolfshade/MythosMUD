"""Unit tests for passive lucidity flux hallucination triggers."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.passive_lucidity_flux import hallucinations as hall


@pytest.mark.asyncio
async def test_handle_phantom_hostile_hallucination() -> None:
    player_id = uuid.uuid4()
    phantom_data = {"name": "Shadow", "phantom_id": "ph-1", "is_non_damaging": True}
    with patch(
        "server.services.phantom_hostile_service.phantom_hostile_service.create_phantom_hostile_data",
        return_value=phantom_data,
    ):
        with patch(
            "server.services.lucidity_event_dispatcher.send_hallucination_event", new_callable=AsyncMock
        ) as send:
            await hall.handle_phantom_hostile_hallucination(player_id, "room-a", "fractured", -20)
    send.assert_awaited_once()
    assert send.await_args.kwargs["hallucination_type"] == "phantom_hostile_spawn"


@pytest.mark.asyncio
async def test_handle_fake_hallucination_npc_tell() -> None:
    player_id = uuid.uuid4()
    with patch("server.services.fake_hallucination_service.FakeHallucinationService") as svc_cls:
        svc = svc_cls.return_value
        svc.select_hallucination_type.return_value = "fake_npc_tell"
        svc.generate_fake_npc_tell.return_value = {
            "message": "Whisper...",
            "npc_name": "Ghost",
            "hallucination_id": "h1",
        }
        with patch(
            "server.services.lucidity_event_dispatcher.send_hallucination_event", new_callable=AsyncMock
        ) as send:
            await hall.handle_fake_hallucination(player_id, "room-a", "deranged", -30)
    send.assert_awaited_once()
    assert send.await_args.kwargs["hallucination_type"] == "fake_npc_tell"


@pytest.mark.asyncio
async def test_handle_fake_hallucination_room_overlay() -> None:
    player_id = uuid.uuid4()
    with patch("server.services.fake_hallucination_service.FakeHallucinationService") as svc_cls:
        svc = svc_cls.return_value
        svc.select_hallucination_type.return_value = "room_text_overlay"
        svc.generate_room_text_overlay.return_value = {"overlay_text": "Walls bleed.", "hallucination_id": "h2"}
        with patch(
            "server.services.lucidity_event_dispatcher.send_hallucination_event", new_callable=AsyncMock
        ) as send:
            await hall.handle_fake_hallucination(player_id, "room-a", "deranged", -30)
    assert send.await_args.kwargs["hallucination_type"] == "room_text_overlay"


@pytest.mark.asyncio
async def test_handle_hallucination_triggers_no_record() -> None:
    player_id = uuid.uuid4()
    session = MagicMock()
    await hall.handle_hallucination_triggers(player_id, str(player_id), "room-a", {}, session)


@pytest.mark.asyncio
async def test_handle_hallucination_triggers_wrong_tier() -> None:
    player_id = uuid.uuid4()
    record = MagicMock(current_tier="lucid", current_lcd=50)
    await hall.handle_hallucination_triggers(player_id, str(player_id), "room-a", {str(player_id): record}, MagicMock())


@pytest.mark.asyncio
async def test_handle_hallucination_triggers_phantom_path() -> None:
    player_id = uuid.uuid4()
    record = MagicMock(current_tier="fractured", current_lcd=-25)
    with patch("server.services.hallucination_frequency_service.HallucinationFrequencyService") as freq_cls:
        freq_cls.return_value.check_time_based_hallucination = AsyncMock(return_value=True)
        with patch(
            "server.services.phantom_hostile_service.phantom_hostile_service.should_spawn_phantom_hostile",
            return_value=True,
        ):
            with patch.object(hall, "handle_phantom_hostile_hallucination", new_callable=AsyncMock) as phantom:
                await hall.handle_hallucination_triggers(
                    player_id, str(player_id), "room-a", {str(player_id): record}, MagicMock()
                )
    phantom.assert_awaited_once()
