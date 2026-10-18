"""PlayerSchemaConverter keeps tick-loop effects out of the typed StatusEffect view.

Regression: ``heal_over_time`` (stored by a scripted action as ``{"type": ...}``) made ``StatusEffect(**effect)`` raise,
so every command the player typed while it ran failed with a validation error.
"""

from server.game.player_schema_converter import status_effect_models
from server.models.game import StatusEffect, StatusEffectType


def test_tick_loop_effects_are_not_part_of_the_typed_view() -> None:
    effects: list[object] = [
        {"type": "heal_over_time", "healing": 5, "duration": 15, "remaining": 13},
        {"type": "lucidity_drain_over_time", "rate": 1, "floor": -10},
    ]

    assert status_effect_models(effects) == []


def test_typed_effects_still_become_status_effect_models() -> None:
    typed = {"effect_type": "stunned", "duration": 3, "intensity": 2}
    tick_loop = {"type": "heal_over_time", "healing": 5, "duration": 15, "remaining": 13}

    [model] = status_effect_models([tick_loop, typed])

    assert isinstance(model, StatusEffect)
    assert model.effect_type == StatusEffectType.STUNNED
