"""Unit tests for EmoteService lookup and formatting."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from server.exceptions import ValidationError
from server.game.emote_service import EmoteDefinition, EmoteService


def _service_with_emotes() -> EmoteService:
    svc = EmoteService.__new__(EmoteService)
    svc.emote_file_path = None
    svc.emotes = {
        "twibble": EmoteDefinition(
            self_message="You twibble.",
            other_message="{player_name} twibbles mysteriously.",
            aliases=["tw"],
        )
    }
    svc.alias_to_emote = {"twibble": "twibble", "tw": "twibble"}
    return svc


def test_emote_service_init_loads_via_mock() -> None:
    with patch.object(EmoteService, "_load_emotes") as load_mock:
        svc = EmoteService()
    load_mock.assert_called_once()
    assert svc.emotes == {}


def test_is_emote_alias_and_get_definition() -> None:
    svc = _service_with_emotes()
    assert svc.is_emote_alias("TW") is True
    assert svc.is_emote_alias("look") is False
    definition = svc.get_emote_definition("tw")
    assert definition is not None
    assert definition["self_message"] == "You twibble."


def test_format_emote_messages() -> None:
    svc = _service_with_emotes()
    self_msg, other_msg = svc.format_emote_messages("twibble", "Arkan")
    assert self_msg == "You twibble."
    assert other_msg == "Arkan twibbles mysteriously."


def test_format_emote_messages_unknown_raises() -> None:
    svc = _service_with_emotes()
    with pytest.raises(ValidationError):
        svc.format_emote_messages("unknown", "Arkan")


def test_list_available_emotes() -> None:
    svc = _service_with_emotes()
    listing = svc.list_available_emotes()
    assert "twibble" in listing
    assert "tw" in listing["twibble"]


def test_reload_emotes_calls_load() -> None:
    svc = _service_with_emotes()
    with patch.object(svc, "_load_emotes") as load_mock:
        svc.reload_emotes()
    load_mock.assert_called_once()


def test_validate_emote_payload_no_validator() -> None:
    svc = _service_with_emotes()
    with patch("server.game.emote_service._get_emote_validator", return_value=None):
        assert svc._validate_emote_payload({"emotes": {}}) == []  # pylint: disable=protected-access


def test_validate_emote_payload_with_validator() -> None:
    svc = _service_with_emotes()
    validator = MagicMock()
    validator.validate_emote_file.return_value = ["bad schema"]
    with patch("server.game.emote_service._get_emote_validator", return_value=validator):
        errors = svc._validate_emote_payload({"emotes": {}})  # pylint: disable=protected-access
    assert errors == ["bad schema"]
