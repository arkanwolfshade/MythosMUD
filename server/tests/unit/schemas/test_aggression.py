"""#999: NPC aggression_level is one contract (int 0-10, or the catalog names passive/aggressive)."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from server.api.admin.npc_schemas import NPCBehaviorConfigModel
from server.schemas.combat import CombatSchemaValidationError, validate_behavior_config_combat_data
from server.schemas.combat.aggression import parse_aggression_level
from server.services.aggro_threat import _aggression_scale  # pyright: ignore[reportPrivateUsage]


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("aggressive", 10),
        ("passive", 0),
        (" Aggressive ", 10),
        (7, 7),
        ("7", 7),
        (7.0, 7),
        (99, 10),
        (-3, 0),
        ("frenzied", None),
        ("", None),
        (None, None),
        ([5], None),
    ],
)
def test_parse_aggression_level(raw: object, expected: int | None) -> None:
    """Names map to the ends of the 0-10 scale, numbers are clamped, anything unreadable means 'unset'."""
    assert parse_aggression_level(raw) == expected


def test_catalog_names_land_on_the_ends_of_the_threat_scale() -> None:
    """aggressive is full threat (same as unset); passive is the damped end."""
    assert _aggression_scale(parse_aggression_level("aggressive")) == _aggression_scale(None) == 1.0
    assert _aggression_scale(parse_aggression_level("passive")) == 0.5


@pytest.mark.parametrize("value", ["passive", "aggressive", 0, 7, 10])
def test_combat_schema_accepts_both_spellings(value: object) -> None:
    validate_behavior_config_combat_data({"combat_behavior": {"aggression_level": value}})


@pytest.mark.parametrize("value", ["frenzied", 11, -1, 2.5])
def test_combat_schema_rejects_everything_else(value: object) -> None:
    with pytest.raises(CombatSchemaValidationError):
        validate_behavior_config_combat_data({"combat_behavior": {"aggression_level": value}})


@pytest.mark.parametrize(
    ("value", "expected"), [("aggressive", 10), ("passive", 0), (" Passive ", 0), (7, 7), (None, None)]
)
def test_admin_model_normalises_to_an_int(value: object, expected: int | None) -> None:
    """A catalog NPC (string level) loads through the admin model and is reported as an int."""
    assert NPCBehaviorConfigModel.model_validate({"aggression_level": value}).aggression_level == expected


@pytest.mark.parametrize("value", ["frenzied", 11, -1])
def test_admin_model_still_rejects_bad_levels(value: object) -> None:
    with pytest.raises(ValidationError):
        _ = NPCBehaviorConfigModel.model_validate({"aggression_level": value})
