"""
Unit tests for rescue command handlers.

Tests the rescue command functionality.
"""

import asyncio
import uuid
from collections.abc import Callable
from dataclasses import dataclass
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.rescue_commands import handle_ground_command, handle_rescue_command
from server.models.lucidity import PlayerLucidity
from server.tests.unit.commands.ground_commands_test_support import (
    FakeConnectionManager,
    FakeLucidityService,
    FakePersistence,
    FakePlayer,
    FakeSession,
    RescueEventRecorder,
    catatonic_record,
    ground_request,
)


@pytest.mark.asyncio
@patch("server.commands.rescue_commands.RescueService")
async def test_handle_rescue_command(mock_rescue_service_cls):
    """Test handle_rescue_command() delegates to RescueService."""
    mock_service = AsyncMock()
    mock_service.rescue.return_value = {"result": "rescued"}
    mock_rescue_service_cls.return_value = mock_service

    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock(), catatonia_registry=None)

    result = await handle_rescue_command(
        {"target": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )

    mock_rescue_service_cls.assert_called_once()
    mock_service.rescue.assert_awaited_once_with("OtherPlayer", {"name": "TestPlayer"}, "TestPlayer")
    assert result == {"result": "rescued"}


@pytest.mark.asyncio
async def test_handle_rescue_command_no_target():
    """Test handle_rescue_command() handles missing target."""
    result = await handle_rescue_command({}, {}, MagicMock(), None, "TestPlayer")
    assert "result" in result
    assert "target" in result["result"].lower() or "usage" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rescue_command_no_persistence():
    """Test handle_rescue_command() handles missing persistence."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_rescue_command({"target": "OtherPlayer"}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower() or "error" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rescue_command_target_player_key():
    """Test handle_rescue_command() accepts target_player key."""
    mock_service = AsyncMock()
    mock_service.rescue.return_value = {"result": "rescued"}
    with patch("server.commands.rescue_commands.RescueService", return_value=mock_service):
        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = MagicMock(persistence=MagicMock(), catatonia_registry=None)
        result = await handle_rescue_command(
            {"target_player": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
        )
        mock_service.rescue.assert_awaited_once_with("OtherPlayer", {"name": "TestPlayer"}, "TestPlayer")
        assert result == {"result": "rescued"}


@pytest.mark.asyncio
async def test_handle_rescue_command_no_app():
    """Test handle_rescue_command() handles missing app."""
    mock_request = MagicMock()
    mock_request.app = None
    result = await handle_rescue_command({"target": "OtherPlayer"}, {}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rescue_command_no_state():
    """Test handle_rescue_command() handles missing app.state."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = None
    result = await handle_rescue_command({"target": "OtherPlayer"}, {}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_no_persistence():
    """Test handle_ground_command() handles missing persistence."""
    mock_request = MagicMock()
    mock_request.app = None
    result = await handle_ground_command({}, {}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "anchor to reality" in result["result"].lower() or "falters" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_no_target():
    """Test handle_ground_command() handles missing target."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_persistence.get_player_by_name = AsyncMock(return_value=MagicMock())
    result = await handle_ground_command({}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "whom" in result["result"].lower() or "target" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_rescuer_not_found():
    """Test handle_ground_command() handles rescuer not found."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    result = await handle_ground_command(
        {"target": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "identity drifts" in result["result"].lower() or "bearings" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_target_not_found():
    """Test handle_ground_command() handles target not found."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_rescuer = MagicMock()
    mock_rescuer.current_room_id = uuid.uuid4()
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[mock_rescuer, None])
    result = await handle_ground_command(
        {"target": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "echoes" in result["result"].lower() or "not found" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_different_rooms():
    """Test handle_ground_command() handles different rooms."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_rescuer = MagicMock()
    mock_rescuer.current_room_id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.current_room_id = uuid.uuid4()  # Different room
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[mock_rescuer, mock_target])
    result = await handle_ground_command(
        {"target": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "not within reach" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_no_rescuer_room():
    """Test handle_ground_command() handles rescuer with no room."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_rescuer = MagicMock()
    mock_rescuer.current_room_id = None
    mock_target = MagicMock()
    mock_target.current_room_id = uuid.uuid4()
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[mock_rescuer, mock_target])
    result = await handle_ground_command(
        {"target": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "not within reach" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_lucidity_record_not_found():
    """Test handle_ground_command() handles missing lucidity record."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_rescuer = MagicMock()
    mock_rescuer.player_id = uuid.uuid4()
    mock_rescuer.current_room_id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.player_id = uuid.uuid4()
    mock_target.current_room_id = mock_rescuer.current_room_id
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[mock_rescuer, mock_target])
    mock_session = MagicMock()
    mock_session.get = AsyncMock(return_value=None)
    with patch("server.commands.rescue_commands.get_async_session") as mock_session_factory:

        async def session_gen():
            yield mock_session

        mock_session_factory.return_value = session_gen()
        result = await handle_ground_command(
            {"target": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
        )
        assert "result" in result
        assert "aura cannot be located" in result["result"].lower() or "lucidity" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_ground_command_not_catatonic():
    """Test handle_ground_command() handles target not catatonic."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock())
    mock_persistence = mock_request.app.state.persistence
    mock_rescuer = MagicMock()
    mock_rescuer.player_id = uuid.uuid4()
    mock_rescuer.current_room_id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.player_id = uuid.uuid4()
    mock_target.current_room_id = mock_rescuer.current_room_id
    mock_persistence.get_player_by_name = AsyncMock(side_effect=[mock_rescuer, mock_target])
    mock_lucidity_record = MagicMock(spec=PlayerLucidity)
    mock_lucidity_record.current_tier = "stable"  # Not catatonic
    mock_session = MagicMock()
    mock_session.get = AsyncMock(return_value=mock_lucidity_record)
    with patch("server.commands.rescue_commands.get_async_session") as mock_session_factory:

        async def session_gen():
            yield mock_session

        mock_session_factory.return_value = session_gen()
        result = await handle_ground_command(
            {"target": "OtherPlayer"}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
        )
        assert "result" in result
        assert "isn't catatonic" in result["result"].lower()


@dataclass
class _GroundRig:
    """Typed fakes wired the way `handle_ground_command` resolves them."""

    request: SimpleNamespace
    manager: FakeConnectionManager
    persistence: FakePersistence
    target: FakePlayer
    session: FakeSession
    service: FakeLucidityService


def _ground_rig(*, tier: str = "catatonic", apply_error: Exception | None = None) -> _GroundRig:
    manager = FakeConnectionManager()
    rescuer = FakePlayer(uuid.uuid4(), "room_a")
    target = FakePlayer(uuid.uuid4(), "room_a")
    persistence = FakePersistence({"TestPlayer": rescuer, "OtherPlayer": target})
    return _GroundRig(
        request=ground_request(persistence, manager),
        manager=manager,
        persistence=persistence,
        target=target,
        session=FakeSession(catatonic_record(tier)),
        service=FakeLucidityService(error=apply_error),
    )


async def _run_ground(
    rig: _GroundRig, *, key: str = "target", after_start: Callable[[], None] | None = None
) -> tuple[dict[str, str], RescueEventRecorder]:
    """Run /ground with a short channel, call `after_start` once it is running, wait for it to finish."""
    events = RescueEventRecorder()
    with (
        patch("server.commands.rescue_commands.get_async_session", side_effect=rig.session.factory),
        patch("server.commands.rescue_commands.LucidityService", return_value=rig.service),
        patch("server.commands.ground_channel.ground_channel_seconds", return_value=0.05),
        patch("server.commands.rescue_commands.send_rescue_update_event", new=events),
    ):
        result = await handle_ground_command(
            {key: "OtherPlayer"}, {"username": "TestPlayer"}, rig.request, None, "TestPlayer"
        )
        if after_start:
            after_start()
        tasks = [c.task for c in rig.manager.grounding_channels.values() if c.task]
        _ = await asyncio.gather(*tasks)
    return result, events


@pytest.mark.asyncio
async def test_handle_ground_command_success():
    """ground starts a channel (channeling to both), then success events with role after the eta."""
    rig = _ground_rig()
    result, events = await _run_ground(rig)

    assert "begin the grounding ritual" in result["result"]
    channeling = events.with_status("channeling")
    assert {e.role for e in channeling} == {"target", "rescuer"} and len(channeling) == 2
    assert all(e.eta_seconds == 0.05 for e in channeling)
    assert rig.service.calls == [(rig.target.player_id, "ground_rescue")]
    assert {("success", "target"), ("success", "rescuer")} <= events.status_roles()
    assert rig.manager.grounding_channels == {} and rig.manager.grounding_by_rescuer == {}


@pytest.mark.asyncio
async def test_handle_ground_command_target_player_key():
    """handle_ground_command() accepts the target_player key."""
    rig = _ground_rig()
    result, _ = await _run_ground(rig, key="target_player")

    assert "begin the grounding ritual" in result["result"]
    assert rig.service.calls == [(rig.target.player_id, "ground_rescue")]


@pytest.mark.asyncio
async def test_handle_ground_command_apply_lucidity_error():
    """A failing adjustment rolls back and sends failed (not success) to both participants."""
    rig = _ground_rig(apply_error=Exception("Database error"))
    _, events = await _run_ground(rig)

    assert rig.session.rollbacks == 1
    assert {("failed", "target"), ("failed", "rescuer")} <= events.status_roles()
    assert not events.with_status("success")


@pytest.mark.asyncio
async def test_handle_ground_command_target_left_room_during_channel_is_interrupted():
    """If the target is no longer in the rescuer's room when the channel elapses, no adjustment is applied."""
    rig = _ground_rig()

    def target_moves() -> None:
        rig.target.current_room_id = "room_b"

    result, events = await _run_ground(rig, after_start=target_moves)

    assert "begin the grounding ritual" in result["result"]
    assert rig.service.calls == []
    assert not events.with_status("success") and not events.with_status("failed")
    assert {("interrupted", "target"), ("interrupted", "rescuer")} <= events.status_roles()


@pytest.mark.asyncio
async def test_handle_ground_command_rejects_while_in_combat():
    """The ritual cannot start during combat, mirroring /rest."""
    rig = _ground_rig()
    with (
        patch("server.commands.rescue_commands.get_async_session", side_effect=rig.session.factory),
        patch("server.commands.rescue_commands.check_player_in_combat", new=AsyncMock(return_value=True)),
    ):
        result = await handle_ground_command(
            {"target": "OtherPlayer"}, {"username": "TestPlayer"}, rig.request, None, "TestPlayer"
        )

    assert "during combat" in result["result"]
    assert rig.manager.grounding_channels == {}
