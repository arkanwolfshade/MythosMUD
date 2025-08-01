import uuid
from datetime import datetime

from server.models import Invite, Player, User


def test_user_creation():
    """Test creating a User object."""
    user = User(
        user_id=uuid.uuid4(),
        email="test@example.com",
        hashed_password="hashed_password",
        is_active=True,
        is_superuser=False,
    )
    assert user.email == "test@example.com"
    assert user.is_active is True
    assert user.is_superuser is False
    assert user.is_authenticated is True


def test_user_display_name():
    """Test user display name generation."""
    user = User(
        user_id=uuid.uuid4(),
        email="test@example.com",
        hashed_password="hashed_password",
    )
    assert user.get_display_name() == "test"


def test_player_creation():
    """Test creating a Player object."""
    user_id = uuid.uuid4()
    player = Player(
        player_id=uuid.uuid4(),
        user_id=user_id,
        name="TestPlayer",
        current_room_id="arkham_001",
        experience_points=0,
        level=1,
    )
    assert player.name == "TestPlayer"
    assert player.user_id == user_id
    assert player.current_room_id == "arkham_001"
    assert player.experience_points == 0
    assert player.level == 1


def test_player_stats():
    """Test player stats JSON handling."""
    player = Player(
        player_id=uuid.uuid4(),
        user_id=uuid.uuid4(),
        name="TestPlayer",
    )

    # Test default stats
    stats = player.get_stats()
    assert stats["health"] == 100
    assert stats["sanity"] == 100
    assert stats["strength"] == 10

    # Test setting stats
    new_stats = {"health": 50, "sanity": 80, "strength": 15}
    player.set_stats(new_stats)
    assert player.get_stats() == new_stats


def test_player_inventory():
    """Test player inventory JSON handling."""
    player = Player(
        player_id=uuid.uuid4(),
        user_id=uuid.uuid4(),
        name="TestPlayer",
    )

    # Test default inventory
    inventory = player.get_inventory()
    assert inventory == []

    # Test setting inventory
    new_inventory = [{"item_id": "sword", "quantity": 1}]
    player.set_inventory(new_inventory)
    assert player.get_inventory() == new_inventory


def test_player_status_effects():
    """Test player status effects JSON handling."""
    player = Player(
        player_id=uuid.uuid4(),
        user_id=uuid.uuid4(),
        name="TestPlayer",
    )

    # Test default status effects
    effects = player.get_status_effects()
    assert effects == []

    # Test setting status effects
    new_effects = [{"type": "poison", "duration": 5}]
    player.set_status_effects(new_effects)
    assert player.get_status_effects() == new_effects


def test_player_experience():
    """Test player experience and leveling."""
    player = Player(
        player_id=uuid.uuid4(),
        user_id=uuid.uuid4(),
        name="TestPlayer",
        experience_points=0,
        level=1,
    )

    # Test adding experience
    player.add_experience(150)
    assert player.experience_points == 150
    assert player.level == 2  # (150 // 100) + 1


def test_player_health():
    """Test player health methods."""
    player = Player(
        player_id=uuid.uuid4(),
        user_id=uuid.uuid4(),
        name="TestPlayer",
    )

    # Test default health
    assert player.is_alive() is True
    assert player.get_health_percentage() == 100.0

    # Test low health
    player.set_stats({"health": 0, "sanity": 100, "strength": 10})
    assert player.is_alive() is False
    assert player.get_health_percentage() == 0.0


def test_invite_creation():
    """Test creating an Invite object."""
    invite = Invite(
        id=uuid.uuid4(),
        invite_code="TEST123",
        is_used=False,
    )
    assert invite.invite_code == "TEST123"
    assert invite.is_used is False


def test_invite_validation():
    """Test invite validation logic."""
    invite = Invite(
        id=uuid.uuid4(),
        invite_code="TEST123",
        is_used=False,
    )

    # Test valid invite
    assert invite.is_valid() is True

    # Test used invite
    invite.is_used = True
    assert invite.is_valid() is False

    # Test expired invite
    invite.is_used = False
    invite.expires_at = datetime(2020, 1, 1)  # Past date
    assert invite.is_valid() is False


def test_invite_usage():
    """Test invite usage tracking."""
    user_id = uuid.uuid4()
    invite = Invite(
        id=uuid.uuid4(),
        invite_code="TEST123",
        is_used=False,
    )

    invite.use_invite(user_id)
    assert invite.is_used is True
    assert invite.used_by_user_id == user_id


def test_invite_display_code():
    """Test invite code formatting."""
    invite = Invite(
        id=uuid.uuid4(),
        invite_code="ABCDEF123456",
        is_used=False,
    )

    display_code = invite.get_display_code()
    assert display_code == "ABCD-EF12-3456"


def test_invite_code_generation():
    """Test invite code generation."""
    code = Invite.generate_code()
    assert len(code) == 12
    assert code.isupper()
    assert code.isalnum()
