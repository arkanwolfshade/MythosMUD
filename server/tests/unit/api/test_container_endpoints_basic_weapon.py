"""Unit tests for weapon coercion on container inventory stacks.

Covers the second call site of the WeaponStats projection: container payloads carry the
same ADR-026 ``metadata.weapon`` shape as player inventory, so they hit the identical
``extra="forbid"`` mismatch.
"""

# Exercising a module-internal helper directly, as the other endpoint tests here do.
# pyright: reportPrivateUsage=false

from types import SimpleNamespace

from server.api.container_endpoints_basic import _coerce_weapon_on_item
from server.schemas.containers.container_data import InventoryStack
from server.schemas.game.weapon import WeaponStats
from server.services.container_service_transfer_from import ContainerTransferFromMixin
from server.tests.fixtures.shared.weapon_metadata import SLING_PROTOTYPE_WEAPON


def test_coerce_weapon_on_item_accepts_full_prototype_metadata() -> None:
    """Regression: the rich prototype keys must be projected away, not rejected.

    This used to leave ``weapon`` as a raw dict, which InventoryStack then dropped, so
    looted weapons reached the client with no stats at all.
    """
    item: dict[str, object] = {"item_id": "sling_01", "weapon": dict(SLING_PROTOTYPE_WEAPON)}

    _coerce_weapon_on_item(item)

    weapon = item["weapon"]
    assert isinstance(weapon, WeaponStats)
    # Pylint infers the dict literal's value type and misses the isinstance narrowing above;
    # same false positive suppressed in test_player_schema_converter_weapon.py.
    assert weapon.min_damage == 1  # pylint: disable=no-member
    assert weapon.max_damage == 4  # pylint: disable=no-member
    assert weapon.damage_types == ["bludgeoning"]  # pylint: disable=no-member


def test_coerce_weapon_on_item_leaves_invalid_modelled_value_as_dict() -> None:
    """A bad value on a key WeaponStats does model still falls back to the raw dict."""
    raw: dict[str, object] = {**SLING_PROTOTYPE_WEAPON, "max_damage": -1}
    item: dict[str, object] = {"item_id": "sling_01", "weapon": raw}

    _coerce_weapon_on_item(item)

    assert item["weapon"] == raw


def test_coerce_weapon_on_item_ignores_non_dict_weapon() -> None:
    """Items with no weapon dict are left untouched."""
    item: dict[str, object] = {"item_id": "rope_01", "weapon": None}

    _coerce_weapon_on_item(item)

    assert item["weapon"] is None


def test_inventory_stack_accepts_persisted_condition_and_position() -> None:
    """Regression: a stored container item must validate against the wire model.

    InventoryStack sets extra="forbid" and did not model `condition` or `position`, both of
    which real stacks carry, so /api/containers/open raised ValidationError -> HTTP 500 for any
    container holding a genuine item. Corpses always hold one, so GUI looting was unreachable.
    """
    stack = InventoryStack.model_validate(
        {
            "item_instance_id": "50e61885-194e-4737-8f0d-78534242d925",
            "prototype_id": "pack_dark_ages.weapon.sling",
            "item_id": "pack_dark_ages.weapon.sling",
            "item_name": "Sling",
            "slot_type": "inventory",
            "quantity": 1,
            "condition": "pristine",
            "position": 0,
        }
    )

    assert stack.condition == "pristine"
    assert stack.position == 0


def test_resolve_container_stack_expands_client_identifier() -> None:
    """Regression: the GUI sends only {item_id, item_instance_id}; the server must expand it.

    Downstream inventory validation requires item_name, so the partial stack raised
    InventoryValidationError -> HTTP 500 on every GUI loot. The server resolves the stack from
    its own container state rather than trusting the client for name/quantity
    (.cursor/rules/server-authority.mdc).
    """
    stored: dict[str, object] = {
        "item_instance_id": "inst-1",
        "prototype_id": "pack_dark_ages.weapon.sling",
        "item_id": "pack_dark_ages.weapon.sling",
        "item_name": "Sling",
        "slot_type": "inventory",
        "quantity": 2,
    }
    container = SimpleNamespace(items=[stored])
    partial: dict[str, object] = {"item_id": "pack_dark_ages.weapon.sling", "item_instance_id": "inst-1"}

    resolved = ContainerTransferFromMixin._resolve_container_stack(
        container,  # pyright: ignore[reportArgumentType]
        # Deliberately partial: this is exactly the shape the GUI sends.
        partial,  # pyright: ignore[reportArgumentType]
    )

    assert resolved is stored
    assert resolved["item_name"] == "Sling"


def test_resolve_container_stack_keeps_caller_item_when_instance_absent() -> None:
    """An unknown instance id falls through unchanged so existing callers keep working."""
    container = SimpleNamespace(items=[{"item_instance_id": "other"}])
    partial: dict[str, object] = {"item_id": "x", "item_instance_id": "inst-1"}

    resolved = ContainerTransferFromMixin._resolve_container_stack(
        container,  # pyright: ignore[reportArgumentType]
        # Deliberately partial: this is exactly the shape the GUI sends.
        partial,  # pyright: ignore[reportArgumentType]
    )

    assert resolved is partial
