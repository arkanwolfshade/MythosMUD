"""The quest channel: personal lines like the system channel, labelled [QUEST] and categorised quest.info."""

# pyright: reportPrivateUsage=false
# Reason: the subject a quest line is published on and the channel->category table are module-private, and they
# decide who receives a quest line and which client filter shows it, so these tests pin them directly.

import uuid
from types import SimpleNamespace
from typing import cast

from server.constants.message_category import MessageCategory
from server.game.chat_message import ChatMessage
from server.game.chat_nats_publisher import _build_legacy_subject
from server.realtime.channel_broadcasting_strategies import (
    ChannelBroadcastingStrategyFactory,
    SystemAdminChannelStrategy,
)
from server.realtime.message_formatters import format_message_content
from server.realtime.nats_message_handler_processing import _CHANNEL_CATEGORY


def test_quest_lines_are_labelled_quest() -> None:
    assert format_message_content("quest", "System", "The bones rattle.") == "[QUEST] The bones rattle."


def test_quest_lines_are_categorised_quest_info() -> None:
    assert _CHANNEL_CATEGORY["quest"] is MessageCategory.QUEST_INFO


def test_a_quest_line_is_published_to_its_one_player() -> None:
    target = str(uuid.uuid4())
    message = cast(ChatMessage, cast(object, SimpleNamespace(channel="quest", target_id=target)))

    assert _build_legacy_subject(message, None) == f"chat.whisper.player.{target}"


def test_quest_lines_are_delivered_by_the_personal_system_strategy() -> None:
    strategy = ChannelBroadcastingStrategyFactory().get_strategy("quest")

    assert isinstance(strategy, SystemAdminChannelStrategy)
    assert strategy.channel_type == "quest"
