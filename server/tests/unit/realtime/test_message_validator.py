"""Unit tests for WebSocketMessageValidator (size, JSON depth, string length, CSRF)."""

from __future__ import annotations

import json
from typing import cast

import pytest

from server.realtime.message_validator import MessageValidationError, WebSocketMessageValidator


def _deep_dict(levels: int) -> dict[str, object]:
    """Build {\"k\": {\"k\": ... \"leaf\": 1}} with `levels` nesting below root."""
    inner: dict[str, object] = {}
    inner["leaf"] = 1
    for _ in range(levels - 1):
        inner = cast(dict[str, object], {"k": inner})
    return cast(dict[str, object], {"k": inner})


@pytest.fixture
def validator() -> WebSocketMessageValidator:
    return WebSocketMessageValidator(max_message_size=256, max_json_depth=4)


def test_validate_size_within_limit(validator: WebSocketMessageValidator) -> None:
    ok: bool = validator.validate_size('{"type":"ping"}')
    assert ok is True


def test_validate_size_exceeds_limit(validator: WebSocketMessageValidator) -> None:
    payload = "x" * 300
    with pytest.raises(MessageValidationError) as exc:
        _ = validator.validate_size(payload)
    assert exc.value.error_type == "size_limit_exceeded"


def test_validate_size_counts_utf8_bytes() -> None:
    """Size limit uses UTF-8 byte length, not Python len(str)."""
    v = WebSocketMessageValidator(max_message_size=4, max_json_depth=10)
    # 2 chars, 6 UTF-8 bytes
    with pytest.raises(MessageValidationError) as exc:
        _ = v.validate_size('{"a":"€"}')
    assert exc.value.error_type == "size_limit_exceeded"


def test_validate_json_structure_depth_exceeded(validator: WebSocketMessageValidator) -> None:
    # max_json_depth=4: root dict + 4 nested dicts under "k" => depth 5 > 4
    deep = _deep_dict(5)
    with pytest.raises(MessageValidationError) as exc:
        _ = validator.validate_json_structure(deep)
    assert exc.value.error_type == "depth_limit_exceeded"


def test_validate_json_structure_string_length_exceeded(validator: WebSocketMessageValidator) -> None:
    long_str = "a" * (WebSocketMessageValidator.MAX_JSON_STRING_LENGTH + 1)
    msg = {"type": "x", "body": long_str}
    with pytest.raises(MessageValidationError) as exc:
        _ = validator.validate_json_structure(msg)
    assert exc.value.error_type == "string_length_exceeded"


def test_validate_json_structure_key_length_exceeded(validator: WebSocketMessageValidator) -> None:
    long_key = "k" * (WebSocketMessageValidator.MAX_JSON_STRING_LENGTH + 1)
    msg = {long_key: 1}
    with pytest.raises(MessageValidationError) as exc:
        _ = validator.validate_json_structure(msg)
    assert exc.value.error_type == "string_length_exceeded"


def test_extract_csrf_invalid_type_rejected(validator: WebSocketMessageValidator) -> None:
    with pytest.raises(MessageValidationError) as exc:
        _ = validator.validate_csrf({"csrfToken": 123}, "player-1", None)
    assert exc.value.error_type == "csrf_invalid_type"


def test_validate_csrf_missing_when_expected(validator: WebSocketMessageValidator) -> None:
    with pytest.raises(MessageValidationError) as exc:
        _ = validator.validate_csrf({"type": "cmd"}, "player-1", "expected-secret")
    assert exc.value.error_type == "csrf_token_missing"


def test_validate_csrf_mismatch(validator: WebSocketMessageValidator) -> None:
    with pytest.raises(MessageValidationError) as exc:
        _ = validator.validate_csrf(
            {"type": "cmd", "csrfToken": "wrong"},
            "player-1",
            "expected-secret",
        )
    assert exc.value.error_type == "csrf_token_invalid"


def test_validate_csrf_matches_expected(validator: WebSocketMessageValidator) -> None:
    assert (
        validator.validate_csrf(
            {"type": "cmd", "csrfToken": "expected-secret"},
            "player-1",
            "expected-secret",
        )
        is True
    )


def test_validate_csrf_snake_case_key(validator: WebSocketMessageValidator) -> None:
    assert (
        validator.validate_csrf(
            {"type": "cmd", "csrf_token": "t"},
            "player-1",
            "t",
        )
        is True
    )


def test_parse_and_validate_strips_csrf_after_success(validator: WebSocketMessageValidator) -> None:
    raw = json.dumps({"type": "ping", "csrfToken": "tok"})
    out = validator.parse_and_validate(raw, "pid", schema=None, csrf_token="tok")
    assert "csrfToken" not in out
    assert "csrf_token" not in out
    assert out.get("type") == "ping"


def test_parse_and_validate_inner_json_inherits_outer_csrf(validator: WebSocketMessageValidator) -> None:
    inner = json.dumps({"type": "command", "data": {}})
    raw = json.dumps({"message": inner, "csrfToken": "outer"})
    out = validator.parse_and_validate(raw, "pid", schema=None, csrf_token="outer")
    assert out.get("type") == "command"
    assert "csrfToken" not in out


def test_parse_and_validate_unwraps_string_inner_message() -> None:
    v = WebSocketMessageValidator(max_message_size=4096, max_json_depth=10)
    inner = json.dumps({"type": "command", "data": {}})
    raw = json.dumps({"message": inner})
    assert v.parse_and_validate(raw, "pid", schema=None, csrf_token=None).get("type") == "command"


def test_parse_and_validate_inner_json_depth_exceeded() -> None:
    """Inner JSON string is validated with the same depth limits as the outer object."""
    v = WebSocketMessageValidator(max_message_size=64 * 1024, max_json_depth=3)
    inner = json.dumps(_deep_dict(5))
    raw = json.dumps({"message": inner})
    with pytest.raises(MessageValidationError) as exc:
        _ = v.parse_and_validate(raw, "pid", schema=None, csrf_token=None)
    assert exc.value.error_type == "depth_limit_exceeded"
