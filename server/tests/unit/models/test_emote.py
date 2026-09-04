"""
Unit tests for emote models.

Tests the Emote and EmoteAlias SQLAlchemy models.
"""

from uuid import uuid4

from server.models.emote import Emote, EmoteAlias

# --- Tests for Emote model ---


def test_emote_creation():
    """Test Emote can be instantiated with required fields."""
    emote_id = str(uuid4())
    emote = Emote(
        id=emote_id,
        stable_id="test_emote_001",
        self_message="You wave hello.",
        other_message="{name} waves hello.",
    )

    assert emote.id == emote_id
    assert emote.stable_id == "test_emote_001"
    assert emote.self_message == "You wave hello."
    assert emote.other_message == "{name} waves hello."


def test_emote_table_name():
    """Test Emote has correct table name."""
    assert Emote.__tablename__ == "emotes"


def test_emote_repr():
    """Test Emote __repr__ method."""
    emote_id = str(uuid4())
    emote = Emote(
        id=emote_id,
        stable_id="test_emote_002",
        self_message="Test message",
        other_message="Test other message",
    )

    repr_str = repr(emote)
    assert "Emote" in repr_str


def test_emote_with_placeholders():
    """Test Emote can have placeholders in messages."""
    emote_id = str(uuid4())
    emote = Emote(
        id=emote_id,
        stable_id="test_emote_003",
        self_message="You smile at {target}.",
        other_message="{name} smiles at {target}.",
    )

    assert "{target}" in emote.self_message
    assert "{name}" in emote.other_message
    assert "{target}" in emote.other_message


# --- Tests for EmoteAlias model ---


def test_emote_alias_creation():
    """Test EmoteAlias can be instantiated with required fields."""
    emote_id = str(uuid4())
    alias = EmoteAlias(
        emote_id=emote_id,
        alias="wave",
    )

    assert alias.emote_id == emote_id
    assert alias.alias == "wave"


def test_emote_alias_table_name():
    """Test EmoteAlias has correct table name."""
    assert EmoteAlias.__tablename__ == "emote_aliases"


def test_emote_alias_repr():
    """Test EmoteAlias __repr__ method."""
    emote_id = str(uuid4())
    alias = EmoteAlias(
        emote_id=emote_id,
        alias="greet",
    )

    repr_str = repr(alias)
    assert "EmoteAlias" in repr_str


def test_emote_alias_multiple_aliases():
    """Test EmoteAlias can have different aliases for same emote."""
    emote_id = str(uuid4())
    alias1 = EmoteAlias(emote_id=emote_id, alias="wave")
    alias2 = EmoteAlias(emote_id=emote_id, alias="hello")

    assert alias1.emote_id == alias2.emote_id
    assert alias1.alias != alias2.alias


def test_emote_alias_case_sensitive():
    """Test EmoteAlias aliases are case sensitive."""
    emote_id = str(uuid4())
    alias1 = EmoteAlias(emote_id=emote_id, alias="Wave")
    alias2 = EmoteAlias(emote_id=emote_id, alias="wave")

    assert alias1.alias == "Wave"
    assert alias2.alias == "wave"
    assert alias1.alias != alias2.alias
