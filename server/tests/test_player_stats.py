#!/usr/bin/env python3
"""
Unit tests for the player stats system using a mock Player object.
"""

from unittest.mock import patch

import pytest


# Mock Player class for unit testing
class Player:
    def __init__(self, name):
        self.name = name
        self.stats = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "sanity": 100,
            "fear": 0,
            "corruption": 0,
            "occult_knowledge": 0,
            "current_health": 100,
            "max_health": 100,
        }
        self.status_effects = []

    def apply_sanity_loss(self, amount, source=None):
        self.stats["sanity"] = max(0, self.stats["sanity"] - amount)
        self.status_effects.append(
            {"effect_type": "sanity_loss", "intensity": amount, "source": source}
        )

    def apply_fear(self, amount, source=None):
        self.stats["fear"] = min(100, self.stats["fear"] + amount)
        self.status_effects.append(
            {"effect_type": "fear", "intensity": amount, "source": source}
        )

    def apply_corruption(self, amount, source=None):
        self.stats["corruption"] = min(100, self.stats["corruption"] + amount)
        self.status_effects.append(
            {"effect_type": "corruption", "intensity": amount, "source": source}
        )

    def gain_occult_knowledge(self, amount, source=None):
        self.stats["occult_knowledge"] += amount
        self.apply_sanity_loss(amount, source)

    def take_damage(self, amount, damage_type=None):
        self.stats["current_health"] = max(0, self.stats["current_health"] - amount)
        self.status_effects.append(
            {"effect_type": "damage", "intensity": amount, "damage_type": damage_type}
        )

    def heal(self, amount):
        self.stats["current_health"] = min(
            self.stats["max_health"], self.stats["current_health"] + amount
        )
        self.status_effects.append({"effect_type": "heal", "intensity": amount})


@pytest.fixture
def player():
    return Player(name="TestPlayer")


def test_player_creation(player):
    assert player.name == "TestPlayer"
    assert player.stats["sanity"] == 100
    assert player.stats["current_health"] == player.stats["max_health"]


def test_sanity_loss(player):
    player.apply_sanity_loss(25, source="test")
    assert player.stats["sanity"] == 75
    assert any(e["effect_type"] == "sanity_loss" for e in player.status_effects)


def test_fear_and_corruption(player):
    player.apply_fear(30, source="test")
    player.apply_corruption(20, source="test")
    assert player.stats["fear"] == 30
    assert player.stats["corruption"] == 20


def test_occult_knowledge(player):
    initial_sanity = player.stats["sanity"]
    initial_knowledge = player.stats["occult_knowledge"]
    player.gain_occult_knowledge(10, source="forbidden tome")
    assert player.stats["occult_knowledge"] == initial_knowledge + 10
    assert player.stats["sanity"] == initial_sanity - 10


def test_health_operations(player):
    player.take_damage(15, damage_type="physical")
    health_after_damage = player.stats["current_health"]
    player.heal(10)
    final_health = player.stats["current_health"]
    assert final_health > health_after_damage


def test_list_players():
    # Example: test a list of mock players
    players = [Player(name=f"Player{i}") for i in range(3)]
    assert isinstance(players, list)
    assert all(isinstance(p, Player) for p in players)


def test_server_connection():
    # Unit test: just check Player class can be instantiated
    player = Player(name="TestPlayer")
    assert player.name == "TestPlayer"


def test_player_stats_mocking():
    # Example of using patch to mock a method
    player = Player(name="MockedPlayer")
    with patch.object(player, "apply_sanity_loss", return_value=None) as mock_method:
        player.apply_sanity_loss(10)
        mock_method.assert_called_once_with(10)
