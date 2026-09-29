"""Unit tests for the shared mute-command payload helpers in admin_mute_commands."""

import pytest

from server.commands.admin_mute_commands import (
    extract_mute_target,
    mute_duration_display,
    parse_mute_duration_minutes,
)


@pytest.mark.parametrize(
    ("command_data", "expected"),
    [
        ({"target_player": "Armitage"}, "Armitage"),
        ({"target_name": "Wilmarth"}, "Wilmarth"),
        ({"target_player": "", "target_name": "Wilmarth"}, "Wilmarth"),
        ({}, None),
        ({"target_player": 42}, None),  # non-string payloads are rejected, not str()-ed
    ],
)
def test_extract_mute_target(command_data: dict[str, object], expected: str | None) -> None:
    assert extract_mute_target(command_data) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [(30, 30), ("45", 45), (None, None), (0, None), ("", None), (1.5, None)],
)
def test_parse_mute_duration_minutes(raw: object, expected: int | None) -> None:
    assert parse_mute_duration_minutes(raw) == expected


def test_mute_duration_display() -> None:
    assert mute_duration_display(30) == "for 30 minutes"
    assert mute_duration_display(None) == "permanently"
