"""The stats the client is sent show a player's real MP: 0 means drained, not full (ADR-029 step 6b)."""

from __future__ import annotations

from unittest.mock import MagicMock

from server.game.player_schema_converter import PlayerSchemaConverter


def test_a_drained_player_shows_zero_mp_and_the_computed_max() -> None:
    stats = PlayerSchemaConverter(MagicMock()).compute_derived_stats_fields({"power": 50, "magic_points": 0})

    assert stats["magic_points"] == 0
    assert stats["max_magic_points"] == 10
