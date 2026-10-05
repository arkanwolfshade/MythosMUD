"""Tests for item-name matching order: exact -> whole word (name) -> prefix -> substring (#870).

The same ladder serves room drops (pickup/get), inventory (equip/use) and equipped items (unequip), so every
case runs against all three.
"""

from collections.abc import Callable

import pytest

from server.commands.inventory_item_matching import (
    match_equipped_item_by_name,
    match_inventory_item_by_name,
    match_room_drop_by_name,
)

Stack = dict[str, object]

CODEX: Stack = {
    "item_name": "Codex of Whispered Secrets",
    "item_id": "artifact.miskatonic.codex",
    "prototype_id": "artifact.miskatonic.codex",
}
TONIC: Stack = {
    "item_name": "Folk Tonic",
    "item_id": "consumable.folk_tonic",
    "prototype_id": "consumable.folk_tonic",
}


def _stack(name: str, prototype_id: str | None = None) -> Stack:
    identifier = prototype_id or f"test.{name.lower().replace(' ', '_')}"
    return {"item_name": name, "item_id": identifier, "prototype_id": identifier}


def _room(stacks: list[Stack], term: str) -> int | None:
    return match_room_drop_by_name(stacks, term)


def _inventory(stacks: list[Stack], term: str) -> int | None:
    return match_inventory_item_by_name(stacks, term)


def _equipped(stacks: list[Stack], term: str) -> int | None:
    """Equipped items resolve to a slot key; slots here are numbered so results compare with list indexes."""
    slot = match_equipped_item_by_name({f"slot_{i}": stack for i, stack in enumerate(stacks)}, term)
    return None if slot is None else int(slot.removeprefix("slot_"))


ALL_FAMILIES = pytest.mark.parametrize("match", [_room, _inventory, _equipped], ids=["room", "inventory", "equipped"])


@ALL_FAMILIES
def test_a_whole_word_beats_a_longer_word_that_starts_with_it(match: Callable[[list[Stack], str], int | None]) -> None:
    stacks = [_stack("Slingshot"), _stack("Leather Sling")]

    assert match(stacks, "sling") == 1


@ALL_FAMILIES
def test_the_earliest_word_position_wins_among_whole_words(match: Callable[[list[Stack], str], int | None]) -> None:
    stacks = [_stack("Silver Ring"), _stack("Ring of Whispers")]

    assert match(stacks, "ring") == 1


@ALL_FAMILIES
def test_equal_word_positions_keep_list_order(match: Callable[[list[Stack], str], int | None]) -> None:
    stacks = [_stack("Old Key"), _stack("Brass Key")]

    assert match(stacks, "key") == 0


@ALL_FAMILIES
def test_a_term_inside_an_id_is_not_a_whole_word_of_another_item(
    match: Callable[[list[Stack], str], int | None],
) -> None:
    """The codex's id `artifact.miskatonic.codex` contains "tonic", but its name does not."""
    assert match([CODEX, TONIC], "tonic") == 1
    assert match([CODEX, TONIC], "folk") == 1


@ALL_FAMILIES
def test_multi_word_terms_match_as_a_phrase(match: Callable[[list[Stack], str], int | None]) -> None:
    stacks = [_stack("Short Bow"), _stack("Short Sword Mk2")]

    assert match(stacks, "short sword") == 1


@ALL_FAMILIES
def test_an_exact_name_still_beats_a_whole_word(match: Callable[[list[Stack], str], int | None]) -> None:
    stacks = [_stack("Silver Key"), _stack("Key")]

    assert match(stacks, "key") == 1


@ALL_FAMILIES
def test_an_exact_id_still_beats_a_whole_word(match: Callable[[list[Stack], str], int | None]) -> None:
    stacks = [_stack("Sword of Dawn"), _stack("Rapier", "weapon.sword")]

    assert match(stacks, "weapon.sword") == 1


@ALL_FAMILIES
def test_an_abbreviation_falls_through_to_prefix(match: Callable[[list[Stack], str], int | None]) -> None:
    assert match([_stack("Brass Key"), CODEX], "cod") == 1


@ALL_FAMILIES
def test_ids_are_the_substring_fallback(match: Callable[[list[Stack], str], int | None]) -> None:
    """No name has the word, but an id contains it: still found, as before."""
    assert match([_stack("Rapier", "weapon.sword")], "sword") == 0


@ALL_FAMILIES
def test_ids_are_not_word_matched_ahead_of_name_prefixes(match: Callable[[list[Stack], str], int | None]) -> None:
    """`weapon` is a whole word of the first item's id only; the second item's name starts with it."""
    stacks = [_stack("Rapier", "equipment.weapon.rapier"), _stack("Weaponsmith's Hammer")]

    assert match(stacks, "weapon") == 1


@ALL_FAMILIES
def test_no_match_and_blank_terms(match: Callable[[list[Stack], str], int | None]) -> None:
    assert match([_stack("Brass Key")], "lantern") is None
    assert match([_stack("Brass Key")], "   ") is None


@ALL_FAMILIES
def test_regex_metacharacters_in_the_term_are_literal(match: Callable[[list[Stack], str], int | None]) -> None:
    assert match([_stack("Brass Key"), _stack("Key (cracked)")], "(cracked)") == 1
    assert match([_stack("Brass Key")], ".*") is None
