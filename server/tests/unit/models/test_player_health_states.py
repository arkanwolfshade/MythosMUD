"""
Unit tests for Player model health state methods.

Tests the new death/respawn functionality including mortally wounded state,
death state detection, and respawn room configuration.
"""

from uuid import uuid4

import pytest

from server.models.player import Player


class TestPlayerHealthStates:
    """Test player health state detection methods."""

    @pytest.fixture
    def sample_player(self):
        """Create a sample player for testing."""
        player = Player(
            player_id=str(uuid4()),
            user_id=str(uuid4()),
            name="TestInvestigator",
            current_room_id="earth_arkhamcity_downtown_001",
        )
        # Set default stats
        stats = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10,
            "lucidity": 100,
            "occult_knowledge": 0,
            "fear": 0,
            "corruption": 0,
            "cult_affiliation": 0,
            "current_dp": 100,
            "max_dp": 100,
        }
        player.set_stats(stats)
        return player

    def test_player_alive_with_positive_hp(self, sample_player):
        """Test that player is alive with positive DP."""
        stats = sample_player.get_stats()
        stats["current_dp"] = 50
        sample_player.set_stats(stats)

        assert sample_player.is_alive() is True
        assert sample_player.is_mortally_wounded() is False
        assert sample_player.is_dead() is False
        assert sample_player.get_health_state() == "alive"

    def test_player_alive_at_full_hp(self, sample_player):
        """Test that player is alive at full DP."""
        stats = sample_player.get_stats()
        stats["current_dp"] = 100
        sample_player.set_stats(stats)

        assert sample_player.is_alive() is True
        assert sample_player.is_mortally_wounded() is False
        assert sample_player.is_dead() is False
        assert sample_player.get_health_state() == "alive"

    def test_player_mortally_wounded_at_zero_hp(self, sample_player):
        """Test that player is mortally wounded at exactly 0 DP."""
        stats = sample_player.get_stats()
        stats["current_dp"] = 0
        sample_player.set_stats(stats)

        assert sample_player.is_alive() is False
        assert sample_player.is_mortally_wounded() is True
        assert sample_player.is_dead() is False
        assert sample_player.get_health_state() == "mortally_wounded"

    def test_player_mortally_wounded_at_negative_hp(self, sample_player):
        """Test that player is mortally wounded at negative DP (above -10)."""
        test_values = [-1, -2, -5, -9]

        for dp_value in test_values:
            stats = sample_player.get_stats()
            stats["current_dp"] = dp_value
            sample_player.set_stats(stats)

            assert sample_player.is_alive() is False
            assert sample_player.is_mortally_wounded() is True
            assert sample_player.is_dead() is False
            assert sample_player.get_health_state() == "mortally_wounded"

    def test_player_dead_at_minus_ten_hp(self, sample_player):
        """Test that player is dead at exactly -10 DP."""
        stats = sample_player.get_stats()
        stats["current_dp"] = -10
        sample_player.set_stats(stats)

        assert sample_player.is_alive() is False
        assert sample_player.is_mortally_wounded() is False
        assert sample_player.is_dead() is True
        assert sample_player.get_health_state() == "dead"

    def test_player_dead_below_minus_ten_hp(self, sample_player):
        """Test that player is dead below -10 DP (should be capped at -10 by combat system)."""
        # This tests the edge case where DP somehow goes below -10
        test_values = [-11, -15, -100]

        for dp_value in test_values:
            stats = sample_player.get_stats()
            stats["current_dp"] = dp_value
            sample_player.set_stats(stats)

            assert sample_player.is_alive() is False
            assert sample_player.is_mortally_wounded() is False
            assert sample_player.is_dead() is True
            assert sample_player.get_health_state() == "dead"

    def test_health_state_boundaries(self, sample_player):
        """Test boundary conditions for health states."""
        # Boundary test: 1 DP (alive)
        stats = sample_player.get_stats()
        stats["current_dp"] = 1
        sample_player.set_stats(stats)
        assert sample_player.get_health_state() == "alive"

        # Boundary test: 0 DP (mortally wounded)
        stats["current_dp"] = 0
        sample_player.set_stats(stats)
        assert sample_player.get_health_state() == "mortally_wounded"

        # Boundary test: -9 DP (mortally wounded)
        stats["current_dp"] = -9
        sample_player.set_stats(stats)
        assert sample_player.get_health_state() == "mortally_wounded"

        # Boundary test: -10 DP (dead)
        stats["current_dp"] = -10
        sample_player.set_stats(stats)
        assert sample_player.get_health_state() == "dead"


class TestPlayerRespawnRoom:
    """Test player respawn room field."""

    @pytest.fixture
    def sample_player(self):
        """Create a sample player for testing."""
        player = Player(
            player_id=str(uuid4()),
            user_id=str(uuid4()),
            name="TestInvestigator",
            current_room_id="earth_arkhamcity_downtown_001",
        )
        return player

    def test_default_respawn_room(self, sample_player):
        """Test that default respawn room is sanitarium."""
        # Player without explicit respawn_room_id will be None until saved to DB
        # The default is applied by the database on INSERT
        # For a new unsaved player, it should be None or the default
        assert (
            sample_player.respawn_room_id is None
            or sample_player.respawn_room_id == "earth_arkhamcity_sanitarium_room_foyer_001"
        )

    def test_custom_respawn_room(self, sample_player):
        """Test setting a custom respawn room."""
        custom_room = "earth_arkhamcity_campus_library_001"
        sample_player.respawn_room_id = custom_room

        assert sample_player.respawn_room_id == custom_room

    def test_respawn_room_persistence(self, sample_player):
        """Test that respawn room is set correctly on creation."""
        # Create player with explicit respawn room
        player_with_custom_respawn = Player(
            player_id=str(uuid4()),
            user_id=str(uuid4()),
            name="CustomRespawnPlayer",
            current_room_id="earth_arkhamcity_downtown_001",
            respawn_room_id="earth_innsmouth_waterfront_001",
        )

        assert player_with_custom_respawn.respawn_room_id == "earth_innsmouth_waterfront_001"

    def test_respawn_room_nullable(self, sample_player):
        """Test that respawn room can be None (triggering default behavior)."""
        sample_player.respawn_room_id = None

        # None should be allowed (application will use default)
        assert sample_player.respawn_room_id is None
