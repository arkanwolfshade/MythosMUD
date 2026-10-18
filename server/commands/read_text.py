"""Readable items: `read <item>` shows the text of anything whose prototype declares ``metadata.readable.text``.

A prototype's metadata is copied onto every stack minted from it, so a newspaper or a note is just item data. Spellbooks
keep their own path in ``read_command``; this runs first and only answers when the item is readable text.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, cast

from .inventory_item_matching import match_inventory_item_by_name


class _HasInventory(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    def get_inventory(self) -> object:
        """The player's inventory, as stored."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


def _text_of(stack: dict[str, object]) -> str | None:
    metadata = stack.get("metadata")
    if not isinstance(metadata, dict):
        return None
    readable = cast(dict[str, object], metadata).get("readable")
    if not isinstance(readable, dict):
        return None
    text = cast(dict[str, object], readable).get("text")
    return text if isinstance(text, str) and text else None


def readable_result(player: object, args: Sequence[object]) -> dict[str, str] | None:
    """The command result for reading a readable item the player carries, or None to fall through to spellbooks."""
    if not hasattr(player, "get_inventory"):
        return None
    inventory = cast(_HasInventory, player).get_inventory()
    if not isinstance(inventory, list):
        return None
    stacks = [cast(dict[str, object], stack) for stack in cast(list[object], inventory) if isinstance(stack, dict)]
    index = match_inventory_item_by_name(stacks, " ".join(str(arg) for arg in args))
    text = _text_of(stacks[index]) if index is not None else None
    return {"result": text} if text is not None else None
