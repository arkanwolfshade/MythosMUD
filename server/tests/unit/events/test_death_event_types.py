"""Tests for death and respawn event types."""

from datetime import UTC, datetime

from server.events.event_types import (
    PlayerDiedEvent,
    PlayerHPDecayEvent,
    PlayerMortallyWoundedEvent,
    PlayerRespawnedEvent,
)


class TestPlayerMortallyWoundedEvent:
    """Test suite for PlayerMortallyWoundedEvent."""

    def test_event_creation_basic(self):
        """Test basic event creation."""
        event = PlayerMortallyWoundedEvent(
            timestamp=datetime.now(UTC),
            event_type="PlayerMortallyWoundedEvent",
            player_id="player-123",
            player_name="TestPlayer",
            room_id="test-room",
        )

        assert event.player_id == "player-123"
        assert event.player_name == "TestPlayer"
        assert event.room_id == "test-room"
        assert event.event_type == "PlayerMortallyWoundedEvent"
        assert event.attacker_id is None
        assert event.attacker_name is None

    def test_event_creation_with_attacker(self):
        """Test event creation with attacker info."""
        event = PlayerMortallyWoundedEvent(
            timestamp=datetime.now(UTC),
            event_type="PlayerMortallyWoundedEvent",
            player_id="player-123",
            player_name="TestPlayer",
            room_id="test-room",
            attacker_id="npc-456",
            attacker_name="Terrible Beast",
            combat_id="combat-789",
        )

        assert event.attacker_id == "npc-456"
        assert event.attacker_name == "Terrible Beast"
        assert event.combat_id == "combat-789"


class TestPlayerHPDecayEvent:
    """Test suite for PlayerHPDecayEvent."""

    def test_event_creation_basic(self):
        """Test basic HP decay event creation."""
        event = PlayerHPDecayEvent(
            timestamp=datetime.now(UTC),
            event_type="PlayerHPDecayEvent",
            player_id="player-123",
            old_hp=-3,
            new_hp=-4,
        )

        assert event.player_id == "player-123"
        assert event.old_hp == -3
        assert event.new_hp == -4
        assert event.decay_amount == 1
        assert event.event_type == "PlayerHPDecayEvent"

    def test_event_creation_with_room(self):
        """Test event creation with room info."""
        event = PlayerHPDecayEvent(
            timestamp=datetime.now(UTC),
            event_type="PlayerHPDecayEvent",
            player_id="player-123",
            old_hp=0,
            new_hp=-1,
            decay_amount=1,
            room_id="test-room",
        )

        assert event.room_id == "test-room"


class TestPlayerDiedEvent:
    """Test suite for PlayerDiedEvent."""

    def test_event_creation_basic(self):
        """Test basic death event creation."""
        event = PlayerDiedEvent(
            timestamp=datetime.now(UTC),
            event_type="PlayerDiedEvent",
            player_id="player-123",
            player_name="TestPlayer",
            room_id="death-room",
        )

        assert event.player_id == "player-123"
        assert event.player_name == "TestPlayer"
        assert event.room_id == "death-room"
        assert event.event_type == "PlayerDiedEvent"
        assert event.killer_id is None
        assert event.killer_name is None

    def test_event_creation_with_killer(self):
        """Test event creation with killer info."""
        event = PlayerDiedEvent(
            timestamp=datetime.now(UTC),
            event_type="PlayerDiedEvent",
            player_id="player-123",
            player_name="TestPlayer",
            room_id="death-room",
            killer_id="npc-456",
            killer_name="Terrible Beast",
            combat_id="combat-789",
            death_location="The Dark Cave",
        )

        assert event.killer_id == "npc-456"
        assert event.killer_name == "Terrible Beast"
        assert event.combat_id == "combat-789"
        assert event.death_location == "The Dark Cave"


class TestPlayerRespawnedEvent:
    """Test suite for PlayerRespawnedEvent."""

    def test_event_creation_basic(self):
        """Test basic respawn event creation."""
        event = PlayerRespawnedEvent(
            timestamp=datetime.now(UTC),
            event_type="PlayerRespawnedEvent",
            player_id="player-123",
            player_name="TestPlayer",
            respawn_room_id="sanitarium-foyer",
            old_hp=-10,
            new_hp=100,
        )

        assert event.player_id == "player-123"
        assert event.player_name == "TestPlayer"
        assert event.respawn_room_id == "sanitarium-foyer"
        assert event.old_hp == -10
        assert event.new_hp == 100
        assert event.event_type == "PlayerRespawnedEvent"

    def test_event_creation_with_death_room(self):
        """Test event creation with death room info."""
        event = PlayerRespawnedEvent(
            timestamp=datetime.now(UTC),
            event_type="PlayerRespawnedEvent",
            player_id="player-123",
            player_name="TestPlayer",
            respawn_room_id="sanitarium-foyer",
            old_hp=-10,
            new_hp=100,
            death_room_id="dangerous-cave",
        )

        assert event.death_room_id == "dangerous-cave"
