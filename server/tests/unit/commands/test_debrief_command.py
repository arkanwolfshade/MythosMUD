"""Unit tests for debrief command handlers."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.debrief_command import (
    _check_debrief_availability,
    _generate_narrative_recap,
    _get_catatonia_registry_from_app,
    _get_persistence_from_app,
    _perform_therapy_if_requested,
    _validate_debrief_context,
    handle_debrief_command,
)
from server.services.active_lucidity_service import LucidityActionOnCooldownError


@pytest.mark.asyncio
async def test_validate_debrief_context_no_persistence():
    """Debrief validation fails when persistence is missing."""
    player, error = await _validate_debrief_context(None, "alice", "alice")
    assert player is None
    assert error is not None
    assert "inaccessible" in error["result"]


@pytest.mark.asyncio
async def test_validate_debrief_context_player_missing():
    """Debrief validation fails when player is not found."""
    persistence = AsyncMock()
    persistence.get_player_by_name = AsyncMock(return_value=None)
    player, error = await _validate_debrief_context(persistence, "ghost", "ghost")
    assert player is None
    assert "identity wavers" in error["result"]


def test_get_persistence_from_app_container():
    """Reads async_persistence from app container."""
    app = MagicMock()
    app.state.container.async_persistence = MagicMock()
    assert _get_persistence_from_app(app) is app.state.container.async_persistence


def test_get_catatonia_registry_from_state_fallback():
    """Reads catatonia registry from app.state when container absent."""
    app = MagicMock()
    app.state.container = None
    app.state.catatonia_registry = MagicMock()
    assert _get_catatonia_registry_from_app(app) is app.state.catatonia_registry


@pytest.mark.asyncio
async def test_check_debrief_availability_not_pending():
    """Debrief unavailable when cooldown is missing."""
    lucidity_service = AsyncMock()
    lucidity_service.get_cooldown = AsyncMock(return_value=None)
    result = await _check_debrief_availability(lucidity_service, uuid.uuid4())
    assert result is not None
    assert "No debrief session" in result["result"]


@pytest.mark.asyncio
async def test_perform_therapy_if_not_requested():
    """Therapy branch skipped when player does not request it."""
    result = await _perform_therapy_if_requested(False, MagicMock(), uuid.uuid4(), MagicMock(), None, "recap")
    assert result == "recap"


@pytest.mark.asyncio
async def test_perform_therapy_success():
    """Therapy appends stability message on success."""
    player = MagicMock()
    player.current_room_id = "room-1"
    session = MagicMock()
    active_service = AsyncMock()
    therapy_result = MagicMock()
    therapy_result.delta = 5
    therapy_result.new_lcd = 55
    active_service.perform_recovery_action = AsyncMock(return_value=therapy_result)

    with patch("server.commands.debrief_command.ActiveLucidityService", return_value=active_service):
        result = await _perform_therapy_if_requested(True, player, uuid.uuid4(), session, None, "recap")

    assert "immediate therapy" in result
    assert "55/100" in result


@pytest.mark.asyncio
async def test_perform_therapy_on_cooldown():
    """Therapy on cooldown appends unavailable message."""
    active_service = AsyncMock()
    active_service.perform_recovery_action = AsyncMock(side_effect=LucidityActionOnCooldownError("cooldown"))

    with patch("server.commands.debrief_command.ActiveLucidityService", return_value=active_service):
        result = await _perform_therapy_if_requested(True, MagicMock(), uuid.uuid4(), MagicMock(), None, "recap")

    assert "Therapy is currently unavailable" in result


def test_generate_narrative_recap_no_adjustments():
    """Recap returns fallback text when no adjustment logs exist."""
    session = MagicMock()
    execute_result = MagicMock()
    execute_result.scalars.return_value.all.return_value = []
    session.execute.return_value = execute_result

    recap = _generate_narrative_recap(uuid.uuid4(), session, MagicMock())
    assert "records are incomplete" in recap


def test_generate_narrative_recap_with_adjustments():
    """Recap summarizes recent lucidity adjustments."""
    session = MagicMock()
    adj = MagicMock()
    adj.reason_code = "combat_stress"
    adj.delta = -10
    execute_result = MagicMock()
    execute_result.scalars.return_value.all.return_value = [adj]
    session.execute.return_value = execute_result

    recap = _generate_narrative_recap(uuid.uuid4(), session, MagicMock())
    assert "Combat Stress" in recap
    assert "-10 LCD" in recap


def test_generate_narrative_recap_exception_fallback():
    """Recap returns generic message when query fails."""
    session = MagicMock()
    session.execute.side_effect = RuntimeError("query failed")
    recap = _generate_narrative_recap(uuid.uuid4(), session, MagicMock())
    assert "lucidity crisis" in recap


@pytest.mark.asyncio
async def test_handle_debrief_command_no_persistence():
    """handle_debrief_command returns error when persistence unavailable."""
    request = MagicMock()
    request.app = None
    result = await handle_debrief_command({}, {"username": "alice"}, request, None, "alice")
    assert "inaccessible" in result["result"]


@pytest.mark.asyncio
async def test_handle_debrief_command_not_available():
    """handle_debrief_command rejects when debrief cooldown absent."""
    player_id = uuid.uuid4()
    player = MagicMock()
    player.player_id = player_id
    persistence = AsyncMock()
    persistence.get_player_by_name = AsyncMock(return_value=player)

    request = MagicMock()
    app = MagicMock()
    app.state.container = None
    app.state.persistence = persistence
    request.app = app

    session = AsyncMock()

    async def session_gen():
        yield session

    lucidity_service = AsyncMock()
    lucidity_service.get_cooldown = AsyncMock(return_value=None)

    with patch("server.commands.debrief_command._get_persistence_from_app", return_value=persistence):
        with patch("server.commands.debrief_command.get_async_session", return_value=session_gen()):
            with patch("server.commands.debrief_command.LucidityService", return_value=lucidity_service):
                result = await handle_debrief_command({}, {"username": "alice"}, request, None, "alice")

    assert "No debrief session" in result["result"]


@pytest.mark.asyncio
async def test_handle_debrief_command_success():
    """handle_debrief_command completes debrief and clears cooldown."""
    player_id = uuid.uuid4()
    player = MagicMock()
    player.player_id = player_id
    player.current_room_id = "sanitarium"
    persistence = AsyncMock()
    persistence.get_player_by_name = AsyncMock(return_value=player)

    request = MagicMock()
    request.app = MagicMock()

    session = AsyncMock()
    lucidity_service = AsyncMock()
    lucidity_service.get_cooldown = AsyncMock(return_value=object())
    lucidity_service._repo.delete_cooldowns_by_action_code_pattern = AsyncMock()

    async def session_gen():
        yield session

    with patch("server.commands.debrief_command._get_persistence_from_app", return_value=persistence):
        with patch("server.commands.debrief_command.get_async_session", return_value=session_gen()):
            with patch("server.commands.debrief_command.LucidityService", return_value=lucidity_service):
                with patch(
                    "server.commands.debrief_command._generate_narrative_recap",
                    return_value="Staff recap.",
                ):
                    result = await handle_debrief_command(
                        {"args": "yes"}, {"username": "alice"}, request, None, "alice"
                    )

    assert "Staff recap." in result["result"]
    assert "debrief session concludes" in result["result"]
    session.commit.assert_awaited()
