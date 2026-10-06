"""Tests that `assist` (and `taunt`) are reachable end to end: parse, route, help, and not mistaken for emotes (#833)."""

# pyright: reportPrivateUsage=false
# Reason: _is_combat_command and _COMMAND_HANDLERS are the registration points under test.

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.command_handler.command_input import should_treat_as_emote
from server.commands import combat_loader
from server.commands.combat import CombatCommandHandler, CombatCommandHandlerExtras
from server.commands.combat_loader import handle_assist_command
from server.commands.command_service import _COMMAND_HANDLERS
from server.models.command import AssistCommand, CommandType
from server.utils.command_factories_combat import CombatCommandFactory
from server.utils.command_helpers import get_command_help
from server.utils.command_parser import CommandParser
from server.utils.command_processor import CommandProcessor


def test_the_factory_builds_an_assist_command_with_or_without_a_name() -> None:
    named = CombatCommandFactory.create_assist_command(["ashcroft"])
    bare = CombatCommandFactory.create_assist_command([])
    multi = CombatCommandFactory.create_assist_command(["dr", "armitage"])

    assert isinstance(named, AssistCommand)
    assert named.target == "ashcroft"
    assert bare.target is None
    assert multi.target == "dr armitage"
    assert bare.command_type is CommandType.ASSIST


def test_the_parser_turns_assist_text_into_an_assist_command() -> None:
    parser = CommandParser()

    named = parser.parse_command("assist ashcroft")
    bare = parser.parse_command("assist")

    assert isinstance(named, AssistCommand)
    assert named.target == "ashcroft"
    assert isinstance(bare, AssistCommand)
    assert bare.target is None


def test_assist_is_a_combat_command_for_the_processor() -> None:
    processor = CommandProcessor()
    assert processor._is_combat_command(CommandType.ASSIST) is True
    assert processor._is_combat_command(CommandType.TAUNT) is True


def test_assist_is_registered_with_the_command_service() -> None:
    assert _COMMAND_HANDLERS["assist"] is handle_assist_command


@pytest.mark.asyncio
async def test_the_loader_delegates_assist_to_the_combat_handler() -> None:
    request: MagicMock = MagicMock()
    handler: MagicMock = MagicMock()
    handle_assist: AsyncMock = AsyncMock(return_value={"result": "assisted"})
    handler.handle_assist_command = handle_assist

    with (
        patch.object(combat_loader, "_app_from_request", return_value=MagicMock()),
        patch.object(combat_loader, "get_combat_command_handler", return_value=handler),
    ):
        result = await handle_assist_command({"target_player": "x"}, {"username": "p"}, request, None, "p")

    assert result == {"result": "assisted"}
    handle_assist.assert_awaited_once_with({"target_player": "x"}, {"username": "p"}, request, None, "p")


@pytest.mark.asyncio
async def test_the_combat_handler_routes_assist_to_its_command_module() -> None:
    handler = CombatCommandHandler(async_persistence=MagicMock())
    run: AsyncMock = AsyncMock(return_value={"result": "ok"})

    with patch("server.commands.combat_handler.run_handle_assist_command", new=run):
        result = await handler.handle_assist_command({"target_player": "x"}, {"username": "p"}, None, None, "p")

    assert result == {"result": "ok"}
    run.assert_awaited_once_with(handler, {"target_player": "x"}, {"username": "p"}, None, None, "p")


def test_the_combat_handler_exposes_the_party_service_it_was_given() -> None:
    party_service = object()
    handler = CombatCommandHandler(
        async_persistence=MagicMock(), extras=CombatCommandHandlerExtras(party_service=party_service)
    )
    assert handler.party_service is party_service
    assert CombatCommandHandler(async_persistence=MagicMock()).party_service is None


def test_help_explains_both_new_combat_verbs() -> None:
    assert "assist [player]" in get_command_help("assist")
    assert "party" in get_command_help("assist")
    assert "taunt <npc>" in get_command_help("taunt")
    assert "Intimidate" in get_command_help("taunt")
    general = get_command_help()
    assert "- assist [player]" in general
    assert "- taunt <npc>" in general


@pytest.mark.parametrize("verb", ["assist", "taunt", "ASSIST"])
def test_a_combat_verb_is_never_mistaken_for_an_emote(verb: str) -> None:
    assert should_treat_as_emote(verb) is False
