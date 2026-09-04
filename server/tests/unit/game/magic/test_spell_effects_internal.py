"""Unit tests for internal spell effect helpers."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from server.game.magic.spell_effects_internal import (
    coerce_effect_float_times_mastery_as_int,
    coerce_effect_int_times_mastery,
    combat_room_id_for_npc_spell,
)


def test_coerce_effect_int_times_mastery() -> None:
    assert coerce_effect_int_times_mastery(10, 1.5) == 15
    assert coerce_effect_int_times_mastery(10.9, 1.0) == 10
    assert coerce_effect_int_times_mastery("7", 2.0) == 14
    assert coerce_effect_int_times_mastery("bad", 2.0) == 0
    assert coerce_effect_int_times_mastery(None, 2.0) == 0
    assert coerce_effect_int_times_mastery("", 2.0) == 0


def test_coerce_effect_float_times_mastery_as_int() -> None:
    assert coerce_effect_float_times_mastery_as_int(2.5, 2.0) == 5
    assert coerce_effect_float_times_mastery_as_int(3, 1.0) == 3
    assert coerce_effect_float_times_mastery_as_int("1.5", 2.0) == 3
    assert coerce_effect_float_times_mastery_as_int("bad", 2.0) == 0
    assert coerce_effect_float_times_mastery_as_int(None, 2.0) == 0


def test_combat_room_id_for_npc_spell_paths() -> None:
    assert combat_room_id_for_npc_spell(None, "npc-1") is None

    cs = MagicMock()
    with patch("server.game.magic.spell_effects_internal.get_combat_id_for_npc", return_value=None):
        assert combat_room_id_for_npc_spell(cs, "npc-1") is None

    combat = MagicMock()
    combat.room_id = None
    with patch("server.game.magic.spell_effects_internal.get_combat_id_for_npc", return_value="c1"):
        cs.get_combat.return_value = combat
        assert combat_room_id_for_npc_spell(cs, "npc-1") is None

    combat_ok = MagicMock()
    combat_ok.room_id = "earth_room_1"
    with patch("server.game.magic.spell_effects_internal.get_combat_id_for_npc", return_value="c1"):
        cs.get_combat.return_value = combat_ok
        assert combat_room_id_for_npc_spell(cs, "npc-1") == "earth_room_1"
