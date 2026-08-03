"""Unit tests for lucidity command disruption."""

from unittest.mock import patch

from server.services.lucidity_command_disruption import (
    can_perform_action,
    get_misfire_message,
    should_involuntary_flee,
    should_misfire_command,
)


def test_should_misfire_ignores_simple_commands():
    assert should_misfire_command("look", "deranged") is False


def test_should_misfire_catatonic_always():
    assert should_misfire_command("cast", "catatonic") is True


@patch("server.services.lucidity_command_disruption.random.random", return_value=0.05)
def test_should_misfire_fractured_roll(_mock_random):
    assert should_misfire_command("cast", "fractured") is True


@patch("server.services.lucidity_command_disruption.random.random", return_value=0.99)
def test_should_misfire_fractured_miss(_mock_random):
    assert should_misfire_command("craft", "fractured") is False


def test_get_misfire_messages_by_tier():
    assert "limbs refuse" in get_misfire_message("cast", "catatonic")
    assert "falters" in get_misfire_message("cast", "deranged")
    assert "sputters" in get_misfire_message("cast", "fractured")


@patch("server.services.lucidity_command_disruption.random.random", return_value=0.0)
def test_should_involuntary_flee_deranged_high_damage(_mock_random):
    assert should_involuntary_flee("deranged", 0.20) is True


def test_should_involuntary_flee_wrong_tier_or_low_damage():
    assert should_involuntary_flee("fractured", 0.50) is False
    assert should_involuntary_flee("deranged", 0.05) is False


def test_can_perform_action():
    assert can_perform_action("lucid") is True
    assert can_perform_action("catatonic") is False
