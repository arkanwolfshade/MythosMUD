"""Tests that `bank`, `deposit` and `withdraw` are reachable end to end: route, help, not emotes (#977)."""

# pyright: reportPrivateUsage=false
# Reason: _COMMAND_HANDLERS is the registration point under test.

from __future__ import annotations

import pytest

from server.command_handler.command_input import should_treat_as_emote
from server.commands.bank_commands import handle_bank_command, handle_deposit_command, handle_withdraw_command
from server.commands.command_service import _COMMAND_HANDLERS
from server.help.help_content import CommandDoc, get_help_content, load_help_docs

BANK_VERBS = ["bank", "deposit", "withdraw"]


def test_the_bank_verbs_are_registered_with_the_command_service() -> None:
    assert _COMMAND_HANDLERS["bank"] is handle_bank_command
    assert _COMMAND_HANDLERS["deposit"] is handle_deposit_command
    assert _COMMAND_HANDLERS["withdraw"] is handle_withdraw_command


@pytest.mark.parametrize("verb", [*BANK_VERBS, "BANK", "Deposit"])
def test_a_bank_verb_is_never_mistaken_for_an_emote(verb: str) -> None:
    assert should_treat_as_emote(verb) is False


def _doc(name: str) -> CommandDoc:
    return next(cmd for cmd in load_help_docs()["commands"] if cmd["name"] == name)


def test_plain_help_describes_each_bank_verb() -> None:
    for verb in BANK_VERBS:
        assert "Topic Not Found" not in get_help_content(verb)


def test_general_help_lists_each_bank_verb() -> None:
    general = get_help_content()
    for verb in BANK_VERBS:
        assert f"<strong>{verb}</strong>" in general


@pytest.mark.parametrize("verb", BANK_VERBS)
def test_detailed_help_exists_and_says_you_must_be_at_a_bank(verb: str) -> None:
    entry = _doc(verb)
    assert entry["category"] == "Inventory"
    assert entry["usage"][0].startswith(verb)
    assert entry.get("examples")
    detailed = get_help_content(verb)
    assert f"<strong>{verb.upper()}</strong>" in detailed
    assert "bank" in detailed.lower()


def test_the_bank_verbs_appear_under_the_inventory_help_category() -> None:
    inventory_commands = {cmd["name"] for cmd in load_help_docs()["commands"] if cmd["category"] == "Inventory"}
    assert set(BANK_VERBS) <= inventory_commands
