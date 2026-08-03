"""Unit tests for chat moderation operations."""

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.chat_moderation import ChatModeration, normalize_player_id


@pytest.fixture
def player_service():
    service = MagicMock()
    player = MagicMock()
    player.name = "Armitage"
    player.id = uuid.uuid4()
    service.get_player_by_id = AsyncMock(return_value=player)
    service.resolve_player_name = AsyncMock(return_value=player)
    return service


@pytest.fixture
def user_manager():
    manager = MagicMock()
    manager.mute_channel.return_value = True
    manager.unmute_channel.return_value = True
    manager.is_channel_muted.return_value = False
    manager.mute_player.return_value = True
    manager.unmute_player.return_value = True
    manager.is_player_muted.return_value = False
    manager.mute_global.return_value = True
    manager.unmute_global.return_value = True
    manager.is_globally_muted.return_value = False
    manager.is_admin.return_value = False
    manager.can_send_message.return_value = True
    manager.get_player_mutes.return_value = {"player_mutes": {}, "global_mutes": {}}
    manager.get_system_stats.return_value = {"admins": 1}
    return manager


@pytest.fixture
def moderation(player_service, user_manager):
    return ChatModeration(player_service, user_manager)


def test_normalize_player_id_accepts_uuid():
    player_id = uuid.uuid4()
    assert normalize_player_id(player_id) == str(player_id)


@pytest.mark.asyncio
async def test_mute_channel_delegates_to_user_manager(moderation, user_manager, player_service):
    player_id = uuid.uuid4()
    result = await moderation.mute_channel(player_id, "say")
    assert result is True
    user_manager.mute_channel.assert_called_once()
    player_service.get_player_by_id.assert_awaited_once()


@pytest.mark.asyncio
async def test_mute_player_returns_false_when_target_missing(moderation, player_service):
    player_service.resolve_player_name = AsyncMock(return_value=None)
    result = await moderation.mute_player(uuid.uuid4(), "MissingNPC")
    assert result is False


def test_is_channel_muted(moderation, user_manager):
    player_id = uuid.uuid4()
    user_manager.is_channel_muted.return_value = True
    assert moderation.is_channel_muted(player_id, "global") is True


@pytest.mark.asyncio
async def test_add_admin_returns_true(moderation, user_manager):
    assert await moderation.add_admin(uuid.uuid4()) is True
    user_manager.add_admin.assert_called_once()


def test_can_send_message(moderation, user_manager):
    user_manager.can_send_message.return_value = False
    assert moderation.can_send_message("sender", channel="say") is False


def test_format_mute_duration_permanent(moderation):
    assert moderation._format_mute_duration(None) == " (PERMANENT)"


def test_format_mute_duration_remaining_minutes(moderation):
    expires = datetime.now(UTC) + timedelta(minutes=15)
    text = moderation._format_mute_duration(expires.isoformat())
    assert "minutes remaining" in text


def test_format_mute_duration_expired(moderation):
    expires = datetime.now(UTC) - timedelta(minutes=1)
    assert moderation._format_mute_duration(expires) == " (EXPIRED)"


@pytest.mark.asyncio
async def test_get_mute_status_player_not_found(moderation, player_service):
    player_service.get_player_by_id = AsyncMock(return_value=None)
    result = await moderation.get_mute_status(uuid.uuid4())
    assert result == "Player not found."


@pytest.mark.asyncio
async def test_get_mute_status_invalid_player_id(moderation):
    result = await moderation.get_mute_status("not-a-uuid")
    assert result == "Invalid player ID format."


@pytest.mark.asyncio
async def test_unmute_channel(moderation, user_manager):
    assert await moderation.unmute_channel(uuid.uuid4(), "say") is True
    user_manager.unmute_channel.assert_called_once()


@pytest.mark.asyncio
async def test_mute_player_success(moderation, user_manager):
    assert await moderation.mute_player(uuid.uuid4(), "Target") is True
    user_manager.mute_player.assert_called_once()


@pytest.mark.asyncio
async def test_unmute_player_success(moderation, user_manager):
    assert await moderation.unmute_player(uuid.uuid4(), "Target") is True
    user_manager.unmute_player.assert_called_once()


@pytest.mark.asyncio
async def test_mute_global_success(moderation, user_manager):
    assert await moderation.mute_global(uuid.uuid4(), "Target", 10, "spam") is True
    user_manager.mute_global.assert_called_once()


@pytest.mark.asyncio
async def test_unmute_global_success(moderation, user_manager):
    assert await moderation.unmute_global(uuid.uuid4(), "Target") is True
    user_manager.unmute_global.assert_called_once()


def test_is_player_muted_and_global(moderation, user_manager):
    user_manager.is_player_muted.return_value = True
    user_manager.is_globally_muted.return_value = True
    assert moderation.is_player_muted(uuid.uuid4(), uuid.uuid4()) is True
    assert moderation.is_globally_muted(uuid.uuid4()) is True


@pytest.mark.asyncio
async def test_remove_admin(moderation, user_manager):
    assert await moderation.remove_admin(uuid.uuid4()) is True
    user_manager.remove_admin.assert_called_once()


def test_get_player_mutes_and_stats(moderation, user_manager):
    assert moderation.get_player_mutes(uuid.uuid4()) == {"player_mutes": {}, "global_mutes": {}}
    assert moderation.get_user_management_stats() == {"admins": 1}


def test_format_mute_entry_and_section(moderation):
    entry = moderation._format_mute_entry({"target_name": "Target", "reason": "noise"})
    assert "Target" in entry
    assert "noise" in entry
    section = moderation._format_mute_section("Muted:", {"id": {"target_name": "A"}}, "None")
    assert section[0] == "Muted:"


@pytest.mark.asyncio
async def test_get_mute_status_with_personal_mutes(moderation, user_manager):
    user_manager.get_player_mutes.return_value = {
        "player_mutes": {"1": {"target_name": "QuietOne", "reason": "spam"}},
        "global_mutes": {},
    }
    result = await moderation.get_mute_status(uuid.uuid4())
    assert "QuietOne" in result


@pytest.mark.asyncio
async def test_get_mute_status_includes_player_name(moderation, user_manager):
    player_id = uuid.uuid4()
    user_manager.is_admin.return_value = True
    result = await moderation.get_mute_status(player_id)
    assert "ARMITAGE" in result
    user_manager.load_player_mutes.assert_called_once()


@pytest.mark.asyncio
async def test_get_mute_status_handles_internal_error(moderation, user_manager):
    user_manager.load_player_mutes.side_effect = RuntimeError("boom")
    result = await moderation.get_mute_status(uuid.uuid4())
    assert result == "Error retrieving mute status."
