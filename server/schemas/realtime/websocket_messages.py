"""
Typed schemas for the WebSocket inbound trust boundary.

Mirrors the HTTP-side pattern from `#755` (`SecureBaseModel`, `extra="forbid"`) applied to the
other untrusted input surface. See `#765` for the client-send audit that derived every field list
below from a citable code path, and `#754` for why the previous attempt at this (guessed field
lists, validated before the wrapper was unwrapped) was deleted instead of revived.

`WebSocketMessageValidator.parse_and_validate` (server/realtime/message_validator.py) validates the
*unwrapped inner message only* against `WebSocketInboundMessage`, after the csrfToken has already
been popped — so no model here needs to carry `csrfToken`.

The discriminator values in `WebSocketInboundMessage` must exactly match
`MessageHandlerFactory._handlers` (server/realtime/message_handler_factory.py); a drift guard test
(server/tests/unit/realtime/test_websocket_message_schema_registry.py) enforces that.
"""

from typing import Annotated, Literal

from pydantic import Field

from ..shared.base import SecureBaseModel


class CommandData(SecureBaseModel):
    """Payload for `command`/`game_command` messages."""

    command: str = ""
    args: list[str] = Field(default_factory=list)


class ChatData(SecureBaseModel):
    """Payload for `chat` messages."""

    message: str = ""


class FollowResponseData(SecureBaseModel):
    """Payload for `follow_response` messages (accept/decline a follow request)."""

    request_id: str | None = None
    accept: bool = False


class PartyInviteResponseData(SecureBaseModel):
    """Payload for `party_invite_response` messages (accept/decline a party invite)."""

    invite_id: str | None = None
    accept: bool = False


class ClientErrorReportData(SecureBaseModel):
    """Payload for `client_error_report` messages."""

    error_type: str | None = None
    message: str | None = None
    context: dict[str, object] | None = None


class CommandMessage(SecureBaseModel):
    """Envelope for `type: "command"` (no known producer; kept for factory-registry parity)."""

    type: Literal["command"]
    data: CommandData = Field(default_factory=CommandData)
    timestamp: str | None = None


class GameCommandMessage(SecureBaseModel):
    """Envelope for `type: "game_command"` — movement/action commands from the game client."""

    type: Literal["game_command"]
    data: CommandData = Field(default_factory=CommandData)
    timestamp: str | None = None


class ChatMessage(SecureBaseModel):
    """Envelope for `type: "chat"` (no known producer; kept for factory-registry parity)."""

    type: Literal["chat"]
    data: ChatData = Field(default_factory=ChatData)
    timestamp: str | None = None


class PingMessage(SecureBaseModel):
    """Envelope for `type: "ping"`. Sent unwrapped, with no `data` and no `timestamp`."""

    type: Literal["ping"]


class FollowResponseMessage(SecureBaseModel):
    """Envelope for `type: "follow_response"`."""

    type: Literal["follow_response"]
    data: FollowResponseData = Field(default_factory=FollowResponseData)
    timestamp: str | None = None


class PartyInviteResponseMessage(SecureBaseModel):
    """Envelope for `type: "party_invite_response"`."""

    type: Literal["party_invite_response"]
    data: PartyInviteResponseData = Field(default_factory=PartyInviteResponseData)
    timestamp: str | None = None


class ClientErrorReportMessage(SecureBaseModel):
    """Envelope for `type: "client_error_report"`."""

    type: Literal["client_error_report"]
    data: ClientErrorReportData = Field(default_factory=ClientErrorReportData)
    timestamp: str | None = None


WebSocketInboundMessage = Annotated[
    CommandMessage
    | GameCommandMessage
    | ChatMessage
    | PingMessage
    | FollowResponseMessage
    | PartyInviteResponseMessage
    | ClientErrorReportMessage,
    Field(discriminator="type"),
]
