"""Tests that `protect` is reachable end to end: parse, route, help, and not mistaken for an emote (#991)."""

# pyright: reportPrivateUsage=false
# Reason: _is_combat_command and _COMMAND_HANDLERS are the registration points under test.

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.command_handler.command_input import should_treat_as_emote
from server.commands import combat_loader
from server.commands.combat import CombatCommandHandler
from server.commands.combat_loader import handle_protect_command
from server.commands.command_service import _COMMAND_HANDLERS
from server.models.command import CommandType, ProtectCommand
from server.utils.command_factories_combat import CombatCommandFactory
from server.utils.command_helpers import get_command_help
from server.utils.command_parser import CommandParser
from server.utils.command_processor import CommandProcessor


def test_the_factory_builds_a_protect_command_with_or_without_a_name() -> None:
    named = CombatCommandFactory.create_protect_command(["ashcroft"])
    bare = CombatCommandFactory.create_protect_command([])
    multi = CombatCommandFactory.create_protect_command(["dr", "armitage"])

    assert isinstance(named, ProtectCommand)
    assert named.target == "ashcroft"
    assert bare.target is None
    assert multi.target == "dr armitage"
    assert bare.command_type is CommandType.PROTECT


def test_the_parser_turns_protect_text_into_a_protect_command() -> None:
    parsed = CommandParser().parse_command("protect ashcroft")

    assert isinstance(parsed, ProtectCommand)
    assert parsed.target == "ashcroft"


def test_protect_is_a_combat_command_for_the_processor() -> None:
    assert CommandProcessor()._is_combat_command(CommandType.PROTECT) is True


def test_protect_is_registered_with_the_command_service() -> None:
    assert _COMMAND_HANDLERS["protect"] is handle_protect_command


@pytest.mark.asyncio
async def test_the_loader_delegates_protect_to_the_combat_handler() -> None:
    request: MagicMock = MagicMock()
    handler: MagicMock = MagicMock()
    handle_protect: AsyncMock = AsyncMock(return_value={"result": "covered"})
    handler.handle_protect_command = handle_protect

    with (
        patch.object(combat_loader, "_app_from_request", return_value=MagicMock()),
        patch.object(combat_loader, "get_combat_command_handler", return_value=handler),
    ):
        result = await handle_protect_command({"target_player": "x"}, {"username": "p"}, request, None, "p")

    assert result == {"result": "covered"}
    handle_protect.assert_awaited_once_with({"target_player": "x"}, {"username": "p"}, request, None, "p")


@pytest.mark.asyncio
async def test_the_combat_handler_routes_protect_to_its_command_module() -> None:
    handler = CombatCommandHandler(async_persistence=MagicMock())
    run: AsyncMock = AsyncMock(return_value={"result": "ok"})

    with patch("server.commands.combat_handler.run_handle_protect_command", new=run):
        result = await handler.handle_protect_command({"target_player": "x"}, {"username": "p"}, None, None, "p")

    assert result == {"result": "ok"}
    run.assert_awaited_once_with(handler, {"target_player": "x"}, {"username": "p"}, None, None, "p")


def test_help_explains_protect() -> None:
    assert "protect <player>" in get_command_help("protect")
    assert "Fighting" in get_command_help("protect")
    assert "- protect <player>" in get_command_help()


@pytest.mark.parametrize("verb", ["protect", "PROTECT"])
def test_protect_is_never_mistaken_for_an_emote(verb: str) -> None:
    assert should_treat_as_emote(verb) is False
