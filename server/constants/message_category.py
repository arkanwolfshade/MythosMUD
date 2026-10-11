"""
Semantic categories for player-visible text.

The server tags each outgoing text message with one of these; the client maps the category to its
presentation (color, typography, glyph) and to the panel it appears in. Kept import-free so commands,
services, and realtime can all share it without import cycles.

Mirrored by ``client/src/types/messageCategory.ts`` (kept in step by
``server/tests/unit/constants/test_message_category.py``).

Reserved namespaces with no members yet: ``lore.*``, ``item.*``, ``npc.*``, ``command.misfire``.

Categories are assigned only in shared formatters and builders. Hallucination code must never choose one
(ADR-024): a hallucinated message gets exactly the category of the real thing it imitates.
"""

from enum import StrEnum


class MessageCategory(StrEnum):
    """Dotted ``domain.kind`` names; the client styles by domain prefix with per-kind overrides."""

    CHAT_SAY = "chat.say"
    CHAT_LOCAL = "chat.local"
    CHAT_GLOBAL = "chat.global"
    CHAT_PARTY = "chat.party"
    CHAT_WHISPER = "chat.whisper"
    CHAT_SHOUT = "chat.shout"
    CHAT_EMOTE = "chat.emote"
    CHAT_ADMIN = "chat.admin"

    COMBAT_HIT = "combat.hit"
    COMBAT_HURT = "combat.hurt"
    COMBAT_MISS = "combat.miss"
    COMBAT_DEATH = "combat.death"
    COMBAT_STATUS = "combat.status"

    ROOM_NAME = "room.name"
    ROOM_DESCRIPTION = "room.description"
    ROOM_EXITS = "room.exits"
    ROOM_MOVEMENT = "room.movement"

    SYSTEM_INFO = "system.info"
    SYSTEM_WARNING = "system.warning"
    SYSTEM_ERROR = "system.error"

    STATUS_LUCIDITY = "status.lucidity"
    STATUS_HEALTH = "status.health"
    STATUS_RESCUE = "status.rescue"

    COMMAND_OUTPUT = "command.output"
