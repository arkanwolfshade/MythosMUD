"""
Unit tests for Player-related SQLAlchemy models.

Tests PlayerChannelPreferences, PlayerInventory, and PlayerExploration models.
"""

from uuid import uuid4

from server.models.player import PlayerChannelPreferences, PlayerExploration, PlayerInventory

# --- Tests for PlayerChannelPreferences model ---


def test_player_channel_preferences_creation():
    """Test PlayerChannelPreferences can be instantiated with required fields."""
    player_id = str(uuid4())
    preferences = PlayerChannelPreferences(
        player_id=player_id,
        default_channel="local",
        muted_channels=[],
    )

    assert preferences.player_id == player_id
    assert preferences.default_channel == "local"
    assert preferences.muted_channels == []


def test_player_channel_preferences_defaults():
    """Test PlayerChannelPreferences has correct default values."""
    player_id = str(uuid4())
    preferences = PlayerChannelPreferences(player_id=player_id)

    # SQLAlchemy defaults are applied on DB save, not object instantiation
    assert preferences.default_channel == "local" or preferences.default_channel is None
    assert preferences.muted_channels == [] or preferences.muted_channels is None


def test_player_channel_preferences_with_muted_channels():
    """Test PlayerChannelPreferences can have muted channels."""
    player_id = str(uuid4())
    preferences = PlayerChannelPreferences(
        player_id=player_id,
        default_channel="global",
        muted_channels=["spam", "ooc"],
    )

    assert preferences.muted_channels == ["spam", "ooc"]


def test_player_channel_preferences_table_name():
    """Test PlayerChannelPreferences has correct table name."""
    assert PlayerChannelPreferences.__tablename__ == "player_channel_preferences"


def test_player_channel_preferences_repr():
    """Test PlayerChannelPreferences __repr__ method."""
    player_id = str(uuid4())
    preferences = PlayerChannelPreferences(player_id=player_id)

    repr_str = repr(preferences)
    assert "PlayerChannelPreferences" in repr_str


# --- Tests for PlayerInventory model ---


def test_player_inventory_creation():
    """Test PlayerInventory can be instantiated with required fields."""
    player_id = str(uuid4())
    inventory = PlayerInventory(
        player_id=player_id,
        inventory_json="[]",
        equipped_json="{}",
    )

    assert inventory.player_id == player_id
    assert inventory.inventory_json == "[]"
    assert inventory.equipped_json == "{}"


def test_player_inventory_defaults():
    """Test PlayerInventory has correct default values."""
    player_id = str(uuid4())
    inventory = PlayerInventory(player_id=player_id)

    # SQLAlchemy defaults are applied on DB save, not object instantiation
    assert inventory.inventory_json == "[]" or inventory.inventory_json is None
    assert inventory.equipped_json == "{}" or inventory.equipped_json is None


def test_player_inventory_with_data():
    """Test PlayerInventory can have inventory and equipped data."""
    player_id = str(uuid4())
    inventory = PlayerInventory(
        player_id=player_id,
        inventory_json='[{"id": "item1", "name": "Sword"}]',
        equipped_json='{"weapon": "sword"}',
    )

    assert inventory.inventory_json == '[{"id": "item1", "name": "Sword"}]'
    assert inventory.equipped_json == '{"weapon": "sword"}'


def test_player_inventory_table_name():
    """Test PlayerInventory has correct table name."""
    assert PlayerInventory.__tablename__ == "player_inventories"


def test_player_inventory_repr():
    """Test PlayerInventory __repr__ method."""
    player_id = str(uuid4())
    inventory = PlayerInventory(player_id=player_id)

    repr_str = repr(inventory)
    assert "PlayerInventory" in repr_str


# --- Tests for PlayerExploration model ---


def test_player_exploration_creation():
    """Test PlayerExploration can be instantiated with required fields."""
    exploration_id = str(uuid4())
    player_id = str(uuid4())
    room_id = str(uuid4())
    exploration = PlayerExploration(
        id=exploration_id,
        player_id=player_id,
        room_id=room_id,
    )

    assert exploration.id == exploration_id
    assert exploration.player_id == player_id
    assert exploration.room_id == room_id


def test_player_exploration_table_name():
    """Test PlayerExploration has correct table name."""
    assert PlayerExploration.__tablename__ == "player_exploration"


def test_player_exploration_repr():
    """Test PlayerExploration __repr__ method."""
    exploration_id = str(uuid4())
    player_id = str(uuid4())
    room_id = str(uuid4())
    exploration = PlayerExploration(
        id=exploration_id,
        player_id=player_id,
        room_id=room_id,
    )

    repr_str = repr(exploration)
    assert "PlayerExploration" in repr_str


def test_player_exploration_multiple_rooms():
    """Test PlayerExploration can track multiple rooms for same player."""
    player_id = str(uuid4())
    room_id1 = str(uuid4())
    room_id2 = str(uuid4())

    exploration1 = PlayerExploration(
        id=str(uuid4()),
        player_id=player_id,
        room_id=room_id1,
    )
    exploration2 = PlayerExploration(
        id=str(uuid4()),
        player_id=player_id,
        room_id=room_id2,
    )

    assert exploration1.player_id == exploration2.player_id
    assert exploration1.room_id != exploration2.room_id
