"""Shared types and helpers for MythosMUD follow state."""

# pylint: disable=missing-function-docstring  # Reason: Protocol method stubs; contracts live in class docstrings

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Literal, NotRequired, Protocol, TypedDict, TypeGuard

FOLLOW_REQUEST_TTL_SECONDS = 60
TargetType = Literal["player", "npc"]
# Stored value: (target_id, target_type) for player; (target_id, target_type, display_name) for NPC.
FollowTargetValue = tuple[str, TargetType] | tuple[str, TargetType, str]


class FollowPlayerView(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Player surface used by follow display and auto-stand."""

    name: str | None
    current_room_id: object

    def get_stats(self) -> dict[str, object]: ...


class FollowPersistence(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Persistence surface required for follow name/posture lookups."""

    async def get_player_by_id(self, player_id: uuid.UUID) -> FollowPlayerView | None: ...


class PendingFollowRequest(TypedDict):
    """In-memory pending player-to-player follow request."""

    requestor_id: str
    requestor_name: str
    target_id: str
    created_at: datetime


class FollowActionResult(TypedDict):
    """Command-shaped follow mutation result."""

    success: bool
    result: str
    request_id: NotRequired[str]
    requestor_id: NotRequired[str]


class FollowStatePayload(TypedDict):
    """Client title-panel follow_state payload."""

    target_name: str
    target_type: TargetType


def is_npc_follow_value(v: FollowTargetValue) -> TypeGuard[tuple[str, TargetType, str]]:
    """True when v is the 3-tuple (target_id, 'npc', display_name)."""
    return len(v) == 3


def str_id(value: uuid.UUID | str) -> str:
    """Normalize ID to string for dict keys."""
    return str(value) if isinstance(value, uuid.UUID) else value
