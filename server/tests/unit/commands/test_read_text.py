"""`read` shows the text of any item whose prototype declares metadata.readable.text (ADR-028 newspapers, notes)."""

from __future__ import annotations

from types import SimpleNamespace

import pytest

from server.commands.read_command import handle_read_command
from server.commands.read_text import readable_result

ADVERTISER = "The *Arkham Advertiser* is folded to the page about the graveyard."


def _stack(name: str, metadata: object) -> dict[str, object]:
    return {
        "item_id": name.lower(),
        "item_name": name,
        "name": name,
        "prototype_id": name.lower(),
        "metadata": metadata,
    }


def _player(*stacks: dict[str, object]) -> SimpleNamespace:
    return SimpleNamespace(get_inventory=lambda: list(stacks))


def test_a_readable_item_yields_its_text() -> None:
    player = _player(_stack("Arkham Advertiser", {"readable": {"text": ADVERTISER}}))

    assert readable_result(player, ["arkham", "advertiser"]) == {"result": ADVERTISER}


def test_a_partial_name_finds_the_item() -> None:
    player = _player(_stack("Arkham Advertiser", {"readable": {"text": ADVERTISER}}))

    assert readable_result(player, ["advertiser"]) == {"result": ADVERTISER}


def test_an_item_that_is_not_readable_is_left_to_the_spellbook_path() -> None:
    player = _player(_stack("Arkham Advertiser", {"spellbook": True, "spells": ["x"]}))

    assert readable_result(player, ["advertiser"]) is None


@pytest.mark.parametrize("metadata", [None, "text", {"readable": None}, {"readable": {"text": ""}}, {"readable": {}}])
def test_malformed_or_empty_readable_metadata_is_ignored(metadata: object) -> None:
    assert readable_result(_player(_stack("Note", metadata)), ["note"]) is None


def test_an_item_the_player_does_not_carry_is_not_found() -> None:
    assert readable_result(_player(_stack("Lantern", {})), ["advertiser"]) is None


def test_an_empty_query_reads_nothing() -> None:
    assert readable_result(_player(_stack("Note", {"readable": {"text": "hi"}})), []) is None


def test_a_player_without_a_usable_inventory_reads_nothing() -> None:
    assert readable_result(SimpleNamespace(get_inventory=lambda: "not a list"), ["note"]) is None
    assert readable_result(object(), ["note"]) is None


@pytest.mark.asyncio
async def test_the_read_command_shows_a_readable_items_text_before_trying_spellbooks() -> None:
    player = _player(_stack("Arkham Advertiser", {"readable": {"text": ADVERTISER}}))

    async def get_player_by_name(name: str) -> SimpleNamespace:
        _ = name
        return player

    app = SimpleNamespace(
        state=SimpleNamespace(
            persistence=SimpleNamespace(get_player_by_name=get_player_by_name),
            spell_learning_service=SimpleNamespace(),
        )
    )

    result = await handle_read_command(
        {"args": ["arkham", "advertiser"]}, {"username": "tester"}, SimpleNamespace(app=app), None, "tester"
    )

    assert result == {"result": ADVERTISER}
