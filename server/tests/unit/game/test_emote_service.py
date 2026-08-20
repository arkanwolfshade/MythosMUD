"""Unit tests for EmoteService lookup, formatting, and async loading (#624)."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

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


def test_emote_service_init_does_not_load() -> None:
    """Construction is synchronous and does no I/O -- the sync/async boundary #624 fixes.
    load_emotes() must be awaited separately (see server/container/bundles/game.py)."""
    mock_repo = MagicMock()
    mock_repo.get_emotes = AsyncMock()
    mock_repo.get_emote_aliases = AsyncMock()
    svc = EmoteService(mock_repo)
    assert svc.emotes == {}
    assert svc.alias_to_emote == {}
    mock_repo.get_emotes.assert_not_called()
    mock_repo.get_emote_aliases.assert_not_called()


@pytest.mark.asyncio
async def test_load_emotes_populates_from_repository() -> None:
    mock_repo = MagicMock()
    mock_repo.get_emotes = AsyncMock(
        return_value=[
            {"stable_id": "twibble", "self_message": "You twibble.", "other_message": "{player_name} twibbles."}
        ]
    )
    mock_repo.get_emote_aliases = AsyncMock(return_value=[{"stable_id": "twibble", "alias": "tw"}])
    svc = EmoteService(mock_repo)

    await svc.load_emotes()

    assert svc.emotes["twibble"]["self_message"] == "You twibble."
    assert svc.emotes["twibble"]["aliases"] == ["tw"]
    assert svc.alias_to_emote == {"twibble": "twibble", "tw": "twibble"}


@pytest.mark.asyncio
async def test_load_emotes_handles_missing_table_gracefully() -> None:
    """A missing emotes table (e.g. in test/dev environments) logs a warning and leaves emotes
    empty rather than raising -- custom emotes must keep working without the DB table."""
    mock_repo = MagicMock()
    mock_repo.get_emotes = AsyncMock(side_effect=RuntimeError('relation "emotes" does not exist'))
    mock_repo.get_emote_aliases = AsyncMock()
    svc = EmoteService(mock_repo)

    await svc.load_emotes()

    assert svc.emotes == {}
    assert svc.alias_to_emote == {}


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


@pytest.mark.asyncio
async def test_reload_emotes_calls_load() -> None:
    svc = _service_with_emotes()
    with patch.object(svc, "load_emotes", new_callable=AsyncMock) as load_mock:
        await svc.reload_emotes()
    load_mock.assert_awaited_once()


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
