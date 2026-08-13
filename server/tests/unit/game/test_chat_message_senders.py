"""Unit tests for chat message senders."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.chat_message_senders import (
    normalize_player_id,
    send_global_message,
    send_local_message,
    send_party_message,
    send_predefined_emote,
    send_system_message,
    send_whisper_message,
)


def test_normalize_player_id():
    uid = uuid.uuid4()
    assert normalize_player_id(uid) == str(uid)


def _player(name: str = "Armitage", room: str = "room-1", level: int = 1):
    p = MagicMock()
    p.name = name
    p.current_room_id = room
    p.level = level
    return p


@pytest.mark.asyncio
async def test_send_system_message_validation_and_auth():
    player_service = MagicMock()
    user_manager = MagicMock()
    rate_limiter = MagicMock()
    chat_logger = MagicMock()
    room_messages: dict = {}

    empty = await send_system_message(
        uuid.uuid4(),
        "  ",
        player_service,
        user_manager,
        rate_limiter,
        chat_logger,
        room_messages,
        10,
        MagicMock(),
        None,
    )
    assert empty["success"] is False

    long_msg = await send_system_message(
        uuid.uuid4(),
        "x" * 2001,
        player_service,
        user_manager,
        rate_limiter,
        chat_logger,
        room_messages,
        10,
        MagicMock(),
        None,
    )
    assert long_msg["success"] is False

    player_service.get_player_by_id = AsyncMock(return_value=None)
    missing = await send_system_message(
        uuid.uuid4(),
        "hi",
        player_service,
        user_manager,
        rate_limiter,
        chat_logger,
        room_messages,
        10,
        MagicMock(),
        None,
    )
    assert missing["success"] is False

    player_service.get_player_by_id = AsyncMock(return_value=_player())
    user_manager.is_admin.return_value = False
    not_admin = await send_system_message(
        uuid.uuid4(),
        "hi",
        player_service,
        user_manager,
        rate_limiter,
        chat_logger,
        room_messages,
        10,
        MagicMock(),
        None,
    )
    assert not_admin["success"] is False


@pytest.mark.asyncio
async def test_send_system_message_success():
    player_id = uuid.uuid4()
    player_service = MagicMock()
    player_service.get_player_by_id = AsyncMock(return_value=_player())
    user_manager = MagicMock()
    user_manager.is_admin.return_value = True
    rate_limiter = MagicMock()
    rate_limiter.check_rate_limit.return_value = True
    chat_logger = MagicMock()
    room_messages: dict = {}
    with patch("server.game.chat_message_senders.publish_chat_message_to_nats", new_callable=AsyncMock) as mock_pub:
        mock_pub.return_value = True
        result = await send_system_message(
            player_id,
            "announcement",
            player_service,
            user_manager,
            rate_limiter,
            chat_logger,
            room_messages,
            10,
            MagicMock(),
            None,
        )
    assert result["success"] is True
    assert "system" in room_messages


@pytest.mark.asyncio
async def test_send_whisper_message_validation():
    player_service = MagicMock()
    rate_limiter = MagicMock()
    chat_logger = MagicMock()
    whisper_tracker = MagicMock()
    room_messages: dict = {}

    empty = await send_whisper_message(
        uuid.uuid4(),
        uuid.uuid4(),
        " ",
        player_service,
        rate_limiter,
        chat_logger,
        whisper_tracker,
        room_messages,
        10,
        MagicMock(),
        None,
    )
    assert empty["success"] is False

    player_service.get_player_by_id = AsyncMock(return_value=None)
    missing = await send_whisper_message(
        uuid.uuid4(),
        uuid.uuid4(),
        "psst",
        player_service,
        rate_limiter,
        chat_logger,
        whisper_tracker,
        room_messages,
        10,
        MagicMock(),
        None,
    )
    assert missing["success"] is False


@pytest.mark.asyncio
async def test_send_whisper_message_success():
    sender = uuid.uuid4()
    target = uuid.uuid4()
    player_service = MagicMock()
    player_service.get_player_by_id = AsyncMock(side_effect=[_player("A"), _player("B")])
    rate_limiter = MagicMock()
    rate_limiter.check_rate_limit.return_value = True
    chat_logger = MagicMock()
    whisper_tracker = MagicMock()
    room_messages: dict = {}
    with patch("server.game.chat_message_senders.publish_chat_message_to_nats", new_callable=AsyncMock) as mock_pub:
        mock_pub.return_value = True
        result = await send_whisper_message(
            sender,
            target,
            "secret",
            player_service,
            rate_limiter,
            chat_logger,
            whisper_tracker,
            room_messages,
            10,
            MagicMock(),
            None,
        )
    assert result["success"] is True
    whisper_tracker.store_sender.assert_called_once()


@pytest.mark.asyncio
async def test_send_party_message_paths():
    player_service = MagicMock()
    rate_limiter = MagicMock()
    chat_logger = MagicMock()

    empty = await send_party_message(
        uuid.uuid4(), " ", "party-1", player_service, rate_limiter, chat_logger, MagicMock(), None
    )
    assert empty["success"] is False

    player_service.get_player_by_id = AsyncMock(return_value=_player())
    rate_limiter.check_rate_limit.return_value = True
    with patch("server.game.chat_message_senders.publish_chat_message_to_nats", new_callable=AsyncMock) as mock_pub:
        mock_pub.return_value = True
        ok = await send_party_message(
            uuid.uuid4(), "hello", "party-1", player_service, rate_limiter, chat_logger, MagicMock(), None
        )
    assert ok["success"] is True


@pytest.mark.asyncio
async def test_send_global_message_player_not_found():
    player_service = MagicMock()
    player_service.get_player_by_id = AsyncMock(return_value=None)
    result = await send_global_message(
        uuid.uuid4(), "hello world", player_service, MagicMock(), MagicMock(), MagicMock(), {}, 10, MagicMock(), None
    )
    assert result["success"] is False


@pytest.mark.asyncio
async def test_send_predefined_emote_unknown():
    player_service = MagicMock()
    with patch("server.game.emote_service.EmoteService") as mock_emote_cls:
        mock_emote_cls.return_value.is_emote_alias.return_value = False
        result = await send_predefined_emote(
            uuid.uuid4(), "not_an_emote", player_service, MagicMock(), MagicMock(), MagicMock(), MagicMock(), None
        )
    assert result["success"] is False


@pytest.mark.asyncio
async def test_send_system_message_rate_limit_and_nats_fail():
    player_service = MagicMock()
    player_service.get_player_by_id = AsyncMock(return_value=_player())
    user_manager = MagicMock()
    user_manager.is_admin.return_value = True
    rate_limiter = MagicMock()
    chat_logger = MagicMock()
    room_messages: dict = {}

    rate_limiter.check_rate_limit.return_value = False
    limited = await send_system_message(
        uuid.uuid4(),
        "hi",
        player_service,
        user_manager,
        rate_limiter,
        chat_logger,
        room_messages,
        10,
        MagicMock(),
        None,
    )
    assert limited.get("rate_limited") is True

    rate_limiter.check_rate_limit.return_value = True
    with patch("server.game.chat_message_senders.publish_chat_message_to_nats", new_callable=AsyncMock) as mock_pub:
        mock_pub.return_value = False
        failed = await send_system_message(
            uuid.uuid4(),
            "hi",
            player_service,
            user_manager,
            rate_limiter,
            chat_logger,
            room_messages,
            10,
            MagicMock(),
            None,
        )
    assert failed["success"] is False


@pytest.mark.asyncio
async def test_send_whisper_message_target_missing_and_rate_limit():
    sender = uuid.uuid4()
    target = uuid.uuid4()
    player_service = MagicMock()
    player_service.get_player_by_id = AsyncMock(side_effect=[_player("A"), None])
    rate_limiter = MagicMock()
    rate_limiter.check_rate_limit.return_value = True
    chat_logger = MagicMock()
    whisper_tracker = MagicMock()
    missing_target = await send_whisper_message(
        sender, target, "secret", player_service, rate_limiter, chat_logger, whisper_tracker, {}, 10, MagicMock(), None
    )
    assert "aether" in missing_target["error"]

    player_service.get_player_by_id = AsyncMock(side_effect=[_player("A"), _player("B")])
    rate_limiter.check_rate_limit.return_value = False
    limited = await send_whisper_message(
        sender, target, "secret", player_service, rate_limiter, chat_logger, whisper_tracker, {}, 10, MagicMock(), None
    )
    assert limited["success"] is False


@pytest.mark.asyncio
async def test_send_global_message_success():
    player_service = MagicMock()
    player_service.get_player_by_id = AsyncMock(return_value=_player(level=5))
    user_manager = MagicMock()
    rate_limiter = MagicMock()
    rate_limiter.check_rate_limit.return_value = True
    chat_logger = MagicMock()
    room_messages: dict = {}
    with patch("server.game.chat_message_senders.validate_global_message", return_value=None):
        with patch("server.game.chat_message_senders.check_global_level_requirement", return_value=None):
            with patch("server.game.chat_message_senders.check_channel_permissions", return_value=None):
                with patch("server.game.chat_message_senders.create_and_log_chat_message") as mock_create:
                    mock_msg = MagicMock()
                    mock_msg.id = "g1"
                    mock_msg.to_dict.return_value = {"id": "g1"}
                    mock_create.return_value = mock_msg
                    with patch(
                        "server.game.chat_message_senders.publish_chat_message_to_nats",
                        new_callable=AsyncMock,
                        return_value=True,
                    ):
                        result = await send_global_message(
                            uuid.uuid4(),
                            "hello all",
                            player_service,
                            user_manager,
                            rate_limiter,
                            chat_logger,
                            room_messages,
                            10,
                            MagicMock(),
                            None,
                        )
    assert result["success"] is True


@pytest.mark.asyncio
async def test_send_predefined_emote_success():
    player = _player()
    player_service = MagicMock()
    player_service.get_player_by_id = AsyncMock(return_value=player)
    user_manager = MagicMock()
    user_manager.is_channel_muted.return_value = False
    user_manager.is_globally_muted.return_value = False
    user_manager.can_send_message.return_value = True
    rate_limiter = MagicMock()
    rate_limiter.check_rate_limit.return_value = True
    chat_logger = MagicMock()
    with patch("server.game.emote_service.EmoteService") as mock_emote_cls:
        emote = mock_emote_cls.return_value
        emote.is_emote_alias.return_value = True
        emote.format_emote_messages.return_value = ("You twibble.", "Armitage twibbles.")
        with patch(
            "server.game.chat_message_senders.publish_chat_message_to_nats",
            new_callable=AsyncMock,
            return_value=True,
        ):
            result = await send_predefined_emote(
                uuid.uuid4(), "twibble", player_service, user_manager, rate_limiter, chat_logger, MagicMock(), None
            )
    assert result["success"] is True
    assert result["self_message"] == "You twibble."


@pytest.mark.asyncio
async def test_send_local_message_success_with_echo_suppression():
    player_service = MagicMock()
    player_service.get_player_by_id = AsyncMock(return_value=_player())
    user_manager = MagicMock()
    rate_limiter = MagicMock()
    rate_limiter.check_rate_limit.return_value = True
    room_messages: dict = {}
    with patch("server.game.chat_message_senders.validate_say_message", return_value=None):
        with patch("server.game.chat_message_senders.check_channel_permissions", return_value=None):
            with patch("server.game.chat_message_senders.create_and_log_chat_message") as mock_create:
                mock_msg = MagicMock()
                mock_msg.id = "local-1"
                mock_msg.to_dict.return_value = {"id": "local-1", "content": "hi"}
                mock_create.return_value = mock_msg
                with patch(
                    "server.game.chat_message_senders.publish_chat_message_to_nats",
                    new_callable=AsyncMock,
                    return_value=True,
                ):
                    result = await send_local_message(
                        uuid.uuid4(),
                        "hi",
                        player_service,
                        user_manager,
                        rate_limiter,
                        room_messages,
                        10,
                        MagicMock(),
                        None,
                    )
    assert result["success"] is True
    assert result["message"]["echo_sent"] is True


@pytest.mark.asyncio
async def test_send_local_message_player_not_in_room():
    player_service = MagicMock()
    player = _player()
    player.current_room_id = None
    player_service.get_player_by_id = AsyncMock(return_value=player)
    user_manager = MagicMock()
    rate_limiter = MagicMock()
    rate_limiter.check_rate_limit.return_value = True
    with patch("server.game.chat_message_senders.validate_say_message", return_value=None):
        result = await send_local_message(
            uuid.uuid4(), "hi", player_service, user_manager, rate_limiter, {}, 10, MagicMock(), None
        )
    assert result["success"] is False
