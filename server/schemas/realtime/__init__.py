"""Realtime domain schemas: realtime API, NATS messages, WebSocket messages."""

from .nats_messages import validate_message
from .realtime import (
    ConnectionStatisticsResponse,
    NewGameSessionResponse,
    PlayerConnectionsResponse,
    SessionInfo,
)
from .websocket_messages import (
    ChatData,
    ChatMessage,
    ClientErrorReportData,
    ClientErrorReportMessage,
    CommandData,
    CommandMessage,
    FollowResponseData,
    FollowResponseMessage,
    GameCommandMessage,
    PartyInviteResponseData,
    PartyInviteResponseMessage,
    PingMessage,
    WebSocketInboundMessage,
)

__all__ = [
    "ChatData",
    "ChatMessage",
    "ClientErrorReportData",
    "ClientErrorReportMessage",
    "CommandData",
    "CommandMessage",
    "ConnectionStatisticsResponse",
    "FollowResponseData",
    "FollowResponseMessage",
    "GameCommandMessage",
    "NewGameSessionResponse",
    "PartyInviteResponseData",
    "PartyInviteResponseMessage",
    "PingMessage",
    "PlayerConnectionsResponse",
    "SessionInfo",
    "WebSocketInboundMessage",
    "validate_message",
]
