"""
Guard and round-trip tests for the WebSocket inbound message schema registry (`#765`).

Covers:
- The schema union's discriminator values exactly match `MessageHandlerFactory`'s registered
  keys (mirroring `#755`'s route-reachability guard test for the HTTP side).
- One round-trip per registered type, built from the literal payload each real client send site
  produces (see `#765`'s client-send audit) — the regression net for enforcement risk.
- Ping validates with no `data` and no `timestamp` (the shape the deleted `#754` `PingMessage`
  modelled wrong).
- An unrecognized field is rejected (the actual point of `extra="forbid"`).
- An unknown `type` raises `unknown_message_type`, distinct from the factory's own
  `INVALID_COMMAND` for a message that bypasses validation entirely.
"""

import json

import pytest

# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names
from server.realtime.message_handler_factory import MessageHandlerFactory
from server.realtime.message_validator import MessageValidationError, WebSocketMessageValidator
from server.schemas.realtime.websocket_messages import (
    ChatMessage,
    ClientErrorReportMessage,
    CommandMessage,
    FollowResponseMessage,
    GameCommandMessage,
    PartyInviteResponseMessage,
    PingMessage,
    WebSocketInboundMessage,
)


def _discriminator_values() -> set[str]:
    """The `type` literal each union member accepts, read off a minimal instance of each."""
    return {
        CommandMessage(type="command").type,
        GameCommandMessage(type="game_command").type,
        ChatMessage(type="chat").type,
        PingMessage(type="ping").type,
        FollowResponseMessage(type="follow_response").type,
        PartyInviteResponseMessage(type="party_invite_response").type,
        ClientErrorReportMessage(type="client_error_report").type,
    }


def test_schema_registry_matches_handler_factory_registry() -> None:
    """The discriminated union and the factory's handler registry cover exactly the same types."""
    factory_types = set(MessageHandlerFactory().get_supported_message_types())
    assert _discriminator_values() == factory_types


@pytest.fixture
def validator() -> WebSocketMessageValidator:
    """A validator with default size/depth limits."""
    return WebSocketMessageValidator()


# Each entry is the literal wire payload the named client send site produces, per #765's audit.
_REAL_CLIENT_PAYLOADS: dict[str, dict[str, object]] = {
    "game_command (useGameConnectionRefactored.ts:353, movement)": {
        "type": "game_command",
        "data": {"command": "look", "args": []},
        "timestamp": "2026-01-01T00:00:00.000Z",
    },
    "game_command (useCommandHandlers.ts:73, chat is sent as a game_command)": {
        "type": "game_command",
        "data": {"command": "chat", "args": ["local", "hello"]},
        "timestamp": "2026-01-01T00:00:00.000Z",
    },
    "follow_response (GameClientV2ContainerView.tsx:153)": {
        "type": "follow_response",
        "data": {"request_id": "req-1", "accept": True},
        "timestamp": "2026-01-01T00:00:00.000Z",
    },
    "party_invite_response (GameClientV2ContainerView.tsx:160)": {
        "type": "party_invite_response",
        "data": {"invite_id": "invite-1", "accept": False},
        "timestamp": "2026-01-01T00:00:00.000Z",
    },
    "client_error_report (clientErrorReporter.ts:26)": {
        "type": "client_error_report",
        "data": {"error_type": "occupants_panel_empty_players", "message": "empty", "context": {"room": "r1"}},
        "timestamp": "2026-01-01T00:00:00.000Z",
    },
}


@pytest.mark.parametrize("payload", _REAL_CLIENT_PAYLOADS.values(), ids=_REAL_CLIENT_PAYLOADS.keys())
def test_real_client_payload_validates(validator: WebSocketMessageValidator, payload: dict[str, object]) -> None:
    """Every literal payload a real client send site produces validates unchanged."""
    wrapped = json.dumps({"message": json.dumps(payload), "csrfToken": "tok"})
    result = validator.parse_and_validate(wrapped, "pid", csrf_token="tok")
    assert result.type == payload["type"]


def test_ping_validates_unwrapped_with_no_data_and_no_timestamp(validator: WebSocketMessageValidator) -> None:
    """
    Ping is sent raw, unwrapped, with only `type` and `csrfToken` — no `data`, no `timestamp`.

    This is the shape the deleted `#754` `PingMessage` modelled wrong (it permitted a
    `timestamp` field ping never sends).
    """
    raw = json.dumps({"type": "ping", "csrfToken": "tok"})
    result = validator.parse_and_validate(raw, "pid", csrf_token="tok")
    assert result.type == "ping"


def test_unrecognized_field_is_rejected(validator: WebSocketMessageValidator) -> None:
    """extra='forbid' rejects a field no schema for the type declares."""
    raw = json.dumps({"type": "ping", "csrfToken": "tok", "unexpected_field": "should not be here"})
    with pytest.raises(MessageValidationError) as exc:
        _ = validator.parse_and_validate(raw, "pid", csrf_token="tok")
    assert exc.value.error_type == "schema_validation_failed"


def test_unknown_message_type_is_rejected(validator: WebSocketMessageValidator) -> None:
    """A `type` with no registered schema is rejected distinctly from a field mismatch."""
    raw = json.dumps({"type": "not_a_real_type", "csrfToken": "tok"})
    with pytest.raises(MessageValidationError) as exc:
        _ = validator.parse_and_validate(raw, "pid", csrf_token="tok")
    assert exc.value.error_type == "unknown_message_type"


def test_union_alias_is_exported_from_package() -> None:
    """WebSocketInboundMessage is re-exported from schemas.realtime, unlike the deleted models."""
    from server.schemas import realtime as realtime_schemas

    assert realtime_schemas.WebSocketInboundMessage is WebSocketInboundMessage
