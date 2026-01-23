"""
Unit tests for Player SQLAlchemy model.

Tests the Player model methods including stats, inventory, status effects, and health state.
"""

from uuid import uuid4

from server.models.player import Player


def test_player_creation() -> None:
    """Test Player can be instantiated with required fields."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
    )

    assert player.player_id == player_id
    assert player.user_id == user_id
    assert player.name == "TestPlayer"


def test_player_defaults() -> None:
    """Test Player has correct default values."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(player_id=player_id, user_id=user_id, name="TestPlayer")

    # SQLAlchemy defaults are applied on DB save, not object instantiation
    assert player.inventory == "[]" or player.inventory is None
    assert player.status_effects == "[]" or player.status_effects is None
    assert player.experience_points == 0 or player.experience_points is None
    assert player.level == 1 or player.level is None
    assert player.is_admin == 0 or player.is_admin is None


def test_player_get_stats() -> None:
    """Test Player.get_stats() returns stats dictionary."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        stats={"strength": 60, "dexterity": 55},
    )

    stats = player.get_stats()

    # get_stats() automatically adds "position": "standing" if not present
    assert stats["strength"] == 60
    assert stats["dexterity"] == 55
    assert "position" in stats


def test_player_get_stats_default() -> None:
    """Test Player.get_stats() returns default stats if not set."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(player_id=player_id, user_id=user_id, name="TestPlayer")

    stats = player.get_stats()

    # Should return default stats structure
    assert isinstance(stats, dict)
    assert "strength" in stats or stats == {}


def test_player_set_stats() -> None:
    """Test Player.set_stats() updates stats dictionary."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(player_id=player_id, user_id=user_id, name="TestPlayer")

    new_stats = {"strength": 70, "constitution": 65}
    player.set_stats(new_stats)

    stats = player.get_stats()
    # get_stats() automatically adds "position": "standing" if not present
    assert stats["strength"] == 70
    assert stats["constitution"] == 65
    assert "position" in stats


def test_player_get_inventory() -> None:
    """Test Player.get_inventory() parses JSON inventory."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        inventory='[{"id": "item1", "name": "Sword"}]',
    )

    inventory = player.get_inventory()

    assert inventory == [{"id": "item1", "name": "Sword"}]


def test_player_get_inventory_empty() -> None:
    """Test Player.get_inventory() handles empty inventory."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        inventory="[]",
    )

    inventory = player.get_inventory()

    assert inventory == []


def test_player_set_inventory() -> None:
    """Test Player.set_inventory() serializes to JSON."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(player_id=player_id, user_id=user_id, name="TestPlayer")

    new_inventory = [{"id": "item2", "name": "Shield"}]
    player.set_inventory(new_inventory)

    assert player.get_inventory() == new_inventory


def test_player_get_status_effects() -> None:
    """Test Player.get_status_effects() parses JSON status effects."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        status_effects='[{"type": "poisoned", "duration": 10}]',
    )

    effects = player.get_status_effects()

    assert effects == [{"type": "poisoned", "duration": 10}]


def test_player_set_status_effects() -> None:
    """Test Player.set_status_effects() serializes to JSON."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(player_id=player_id, user_id=user_id, name="TestPlayer")

    new_effects = [{"type": "stunned", "duration": 5}]
    player.set_status_effects(new_effects)

    assert player.get_status_effects() == new_effects


def test_player_get_equipped_items() -> None:
    """Test Player.get_equipped_items() returns equipped items from _equipped_items attribute."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(player_id=player_id, user_id=user_id, name="TestPlayer")

    # Set equipped items using the method
    player.set_equipped_items({"weapon": "sword", "armor": "leather"})

    equipped = player.get_equipped_items()

    assert equipped == {"weapon": "sword", "armor": "leather"}


def test_player_get_equipped_items_empty() -> None:
    """Test Player.get_equipped_items() returns empty dict if no equipped items."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        stats={},
    )

    equipped = player.get_equipped_items()

    assert equipped == {}


def test_player_set_equipped_items() -> None:
    """Test Player.set_equipped_items() updates equipped items in stats."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(player_id=player_id, user_id=user_id, name="TestPlayer")

    new_equipped = {"weapon": "axe", "shield": "round"}
    player.set_equipped_items(new_equipped)

    assert player.get_equipped_items() == new_equipped


def test_player_add_experience() -> None:
    """Test Player.add_experience() increases experience points."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        experience_points=100,
    )

    player.add_experience(50)

    assert player.experience_points == 150


def test_player_add_experience_zero() -> None:
    """Test Player.add_experience() handles zero experience."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        experience_points=100,
    )

    player.add_experience(0)

    assert player.experience_points == 100


def test_player_is_alive() -> None:
    """Test Player.is_alive() returns True when current_dp > 0."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        stats={"current_dp": 10},
    )

    assert player.is_alive() is True


def test_player_is_alive_false() -> None:
    """Test Player.is_alive() returns False when current_dp <= 0."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        stats={"current_dp": 0},
    )

    assert player.is_alive() is False


def test_player_is_mortally_wounded() -> None:
    """Test Player.is_mortally_wounded() returns True when current_dp < 0."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        stats={"current_dp": -5},
    )

    assert player.is_mortally_wounded() is True


def test_player_is_mortally_wounded_false() -> None:
    """Test Player.is_mortally_wounded() returns False when current_dp >= 0."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        stats={"current_dp": 10},
    )

    assert player.is_mortally_wounded() is False


def test_player_is_dead() -> None:
    """Test Player.is_dead() returns True when current_dp <= -10."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        stats={"current_dp": -10},
    )

    assert player.is_dead() is True


def test_player_is_dead_false() -> None:
    """Test Player.is_dead() returns False when current_dp > -10."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        stats={"current_dp": -5},
    )

    assert player.is_dead() is False


def test_player_get_health_state() -> None:
    """Test Player.get_health_state() returns correct state."""
    player_id = str(uuid4())
    user_id = str(uuid4())

    # Alive
    player1 = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer1",
        stats={"current_dp": 10},
    )
    assert player1.get_health_state() == "alive"

    # Mortally wounded
    player2 = Player(
        player_id=str(uuid4()),
        user_id=user_id,
        name="TestPlayer2",
        stats={"current_dp": -5},
    )
    assert player2.get_health_state() == "mortally_wounded"

    # Dead
    player3 = Player(
        player_id=str(uuid4()),
        user_id=user_id,
        name="TestPlayer3",
        stats={"current_dp": -10},
    )
    assert player3.get_health_state() == "dead"


def test_player_is_admin_user() -> None:
    """Test Player.is_admin_user() returns True when is_admin > 0."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        is_admin=1,
    )

    assert player.is_admin_user() is True


def test_player_is_admin_user_false() -> None:
    """Test Player.is_admin_user() returns False when is_admin == 0."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        is_admin=0,
    )

    assert player.is_admin_user() is False


def test_player_set_admin_status() -> None:
    """Test Player.set_admin_status() updates is_admin."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        is_admin=0,
    )

    player.set_admin_status(True)

    assert player.is_admin == 1
    assert player.is_admin_user() is True


def test_player_set_admin_status_false() -> None:
    """Test Player.set_admin_status(False) sets is_admin to 0."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        is_admin=1,
    )

    player.set_admin_status(False)

    assert player.is_admin == 0
    assert player.is_admin_user() is False


def test_player_get_health_percentage() -> None:
    """Test Player.get_health_percentage() calculates percentage correctly."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        stats={"current_dp": 10, "max_dp": 20},
    )

    percentage = player.get_health_percentage()

    assert percentage == 50.0


def test_player_get_health_percentage_full() -> None:
    """Test Player.get_health_percentage() returns 100.0 when at full health."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        stats={"current_dp": 20, "max_dp": 20},
    )

    percentage = player.get_health_percentage()

    assert percentage == 100.0


def test_player_get_health_percentage_zero() -> None:
    """Test Player.get_health_percentage() returns 0.0 when current_dp is 0."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="TestPlayer",
        stats={"current_dp": 0, "max_dp": 20},
    )

    percentage = player.get_health_percentage()

    assert percentage == 0.0


def test_player_table_name() -> None:
    """Test Player has correct table name."""
    assert Player.__tablename__ == "players"


def test_player_repr() -> None:
    """Test Player __repr__ method."""
    player_id = str(uuid4())
    user_id = str(uuid4())
    player = Player(player_id=player_id, user_id=user_id, name="TestPlayer")

    repr_str = repr(player)
    assert "Player" in repr_str
    assert "TestPlayer" in repr_str
