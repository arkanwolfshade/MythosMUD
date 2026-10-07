"""Tests that `bank`, `deposit` and `withdraw` are reachable end to end: route, help (both systems), not emotes (#977)."""

# pyright: reportPrivateUsage=false
# Reason: _COMMAND_HANDLERS is the registration point under test.

from __future__ import annotations

from typing import cast

import pytest

from server.command_handler.command_input import should_treat_as_emote
from server.commands.bank_commands import handle_bank_command, handle_deposit_command, handle_withdraw_command
from server.commands.command_service import _COMMAND_HANDLERS
from server.help.help_content import COMMANDS, get_command_categories, get_commands_by_category, get_help_content
from server.utils.command_helpers import get_command_help

BANK_VERBS = ["bank", "deposit", "withdraw"]


def test_the_bank_verbs_are_registered_with_the_command_service() -> None:
    assert _COMMAND_HANDLERS["bank"] is handle_bank_command
    assert _COMMAND_HANDLERS["deposit"] is handle_deposit_command
    assert _COMMAND_HANDLERS["withdraw"] is handle_withdraw_command


@pytest.mark.parametrize("verb", [*BANK_VERBS, "BANK", "Deposit"])
def test_a_bank_verb_is_never_mistaken_for_an_emote(verb: str) -> None:
    assert should_treat_as_emote(verb) is False


def test_plain_help_describes_each_bank_verb() -> None:
    assert "bank deposit box" in get_command_help("bank")
    assert "deposit <item> [quantity]" in get_command_help("deposit")
    assert "withdraw <item> [quantity]" in get_command_help("withdraw")
    for verb in BANK_VERBS:
        assert "No help available" not in get_command_help(verb)


def test_general_help_lists_each_bank_verb() -> None:
    general = get_command_help()
    assert "- bank - " in general
    assert "- deposit <item> [quantity]" in general
    assert "- withdraw <item> [quantity]" in general


@pytest.mark.parametrize("verb", BANK_VERBS)
def test_detailed_help_exists_and_says_you_must_be_at_a_bank(verb: str) -> None:
    entry = COMMANDS[verb]
    assert entry["category"] == "Inventory"
    assert cast(str, entry["usage"]).startswith(verb)
    assert entry["examples"]
    detailed = get_help_content(verb)
    assert f"<h3>{verb.upper()} Command</h3>" in detailed
    assert "bank" in detailed.lower()


def test_the_bank_verbs_appear_under_the_inventory_help_category() -> None:
    assert "Inventory" in get_command_categories()
    inventory_commands = {name for name, _ in get_commands_by_category("Inventory")}
    assert set(BANK_VERBS) <= inventory_commands
