"""Realtime domain schemas: realtime API, NATS messages, WebSocket messages."""

from .nats_messages import validate_message
from .realtime import (
    ConnectionStatisticsResponse,
    NewGameSessionResponse,
    PlayerConnectionsResponse,
    SessionInfo,
)

__all__ = [
    "ConnectionStatisticsResponse",
    "NewGameSessionResponse",
    "PlayerConnectionsResponse",
    "SessionInfo",
    "validate_message",
]
