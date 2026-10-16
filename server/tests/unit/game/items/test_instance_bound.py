"""Unit tests for the pure INSTANCE_BOUND stack helpers."""

from copy import deepcopy
from typing import cast

from server.game.items.constants import INSTANCE_BOUND_FLAG
from server.game.items.instance_bound import is_instance_bound_stack, strip_instance_bound_stacks


def _stack(item_id: str, **extra: object) -> dict[str, object]:
    return {"item_id": item_id, "quantity": 1, **extra}


def test_a_stack_is_instance_bound_only_when_its_flags_list_says_so() -> None:
    assert is_instance_bound_stack(_stack("amulet", flags=[INSTANCE_BOUND_FLAG, "MAGICAL"]))
    assert not is_instance_bound_stack(_stack("lantern", flags=["MAGICAL"]))
    assert not is_instance_bound_stack(_stack("lantern"))


def test_malformed_flags_never_count_as_instance_bound() -> None:
    assert not is_instance_bound_stack(_stack("odd", flags=INSTANCE_BOUND_FLAG))  # a string, not a list
    assert not is_instance_bound_stack(_stack("odd", flags=None))


def test_stripping_leaves_the_input_untouched_even_when_a_container_loses_an_item() -> None:
    """The caller's list (and the containers inside it) must come back unmodified; changes are made on copies."""
    backpack = _stack(
        "backpack", inner_container={"items": [_stack("amulet", flags=[INSTANCE_BOUND_FLAG]), _stack("bandage")]}
    )
    stacks = [backpack, _stack("tonic")]
    snapshot = deepcopy(stacks)

    kept, removed = strip_instance_bound_stacks(stacks)

    assert removed == 1
    assert stacks == snapshot  # untouched
    assert [stack["item_id"] for stack in kept] == ["backpack", "tonic"]
    assert kept[0] is not backpack  # the container that lost an item is a copy


def test_a_container_that_loses_nothing_is_returned_as_is() -> None:
    backpack = _stack("backpack", inner_container={"items": [_stack("bandage")]})

    kept, removed = strip_instance_bound_stacks([backpack])

    assert removed == 0
    assert kept == [backpack]
    assert kept[0] is backpack


def test_instance_bound_items_are_stripped_at_every_depth() -> None:
    inner_pouch = _stack("pouch", inner_container={"items": [_stack("charm", flags=[INSTANCE_BOUND_FLAG])]})
    backpack = _stack(
        "backpack", inner_container={"items": [inner_pouch, _stack("amulet", flags=[INSTANCE_BOUND_FLAG])]}
    )

    kept, removed = strip_instance_bound_stacks([backpack])

    assert removed == 2
    [outer] = kept
    outer_inner = cast(dict[str, list[dict[str, object]]], outer["inner_container"])
    assert [item["item_id"] for item in outer_inner["items"]] == ["pouch"]
