"""
Unit tests for SpellDB model.

Tests the SpellDB SQLAlchemy model.
"""

from server.models.spell_db import SpellDB


def test_spell_db_repr():
    """Test __repr__ returns expected string format."""
    spell = SpellDB()
    spell.spell_id = "test_spell_123"
    spell.name = "Test Spell"
    spell.school = "mythos"

    repr_str = repr(spell)

    assert "SpellDB" in repr_str
    assert "test_spell_123" in repr_str
    assert "Test Spell" in repr_str
    assert "mythos" in repr_str
