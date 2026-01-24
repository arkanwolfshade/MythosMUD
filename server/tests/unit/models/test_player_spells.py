"""
Unit tests for PlayerSpell model.

Tests the PlayerSpell SQLAlchemy model.
"""

import uuid

from server.models.player_spells import PlayerSpell


def test_player_spell_repr() -> None:
    """Test __repr__ returns expected string format."""
    player_spell = PlayerSpell()
    player_spell.player_id = str(uuid.uuid4())
    player_spell.spell_id = "test_spell_123"
    player_spell.mastery = 5

    repr_str = repr(player_spell)

    assert "PlayerSpell" in repr_str
    assert player_spell.player_id in repr_str
    assert "test_spell_123" in repr_str
    assert "5" in repr_str or "mastery=5" in repr_str
