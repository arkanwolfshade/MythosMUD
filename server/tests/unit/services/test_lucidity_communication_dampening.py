"""Unit tests for lucidity communication dampening."""

from unittest.mock import patch

from server.services.lucidity_communication_dampening import (
    apply_communication_dampening,
    should_block_shout,
)


def test_should_block_shout_deranged():
    assert should_block_shout("deranged") is True
    assert should_block_shout("lucid") is False


def test_whisper_uneasy_adds_strained_tag():
    result = apply_communication_dampening("hello", sender_tier="uneasy", message_type="whisper")
    assert "strained" in result["tags"]
    assert result["message"] == "hello"


def test_deranged_shout_blocked():
    result = apply_communication_dampening("help!", sender_tier="deranged", message_type="shout")
    assert result["blocked"] is True
    assert result["message"] == ""
    assert "hallucination" in result["tags"]


@patch("server.services.lucidity_communication_dampening.random.random", return_value=0.99)
def test_fractured_outgoing_no_glyph_when_roll_high(_mock_random):
    result = apply_communication_dampening("hi", sender_tier="fractured", message_type="say")
    assert result["message"] == "hi"


@patch("server.services.lucidity_communication_dampening.random.random", return_value=0.1)
@patch("server.services.lucidity_communication_dampening.random.choice", return_value="*")
def test_fractured_outgoing_appends_glyph(_mock_choice, _mock_random):
    result = apply_communication_dampening("hi", sender_tier="fractured", message_type="chat")
    assert result["message"].startswith("hi ")


@patch("server.services.lucidity_communication_dampening.random.random", return_value=0.0)
def test_fractured_incoming_strips_punctuation(_mock_random):
    result = apply_communication_dampening(
        "Wait, what?",
        sender_tier="lucid",
        receiver_tier="fractured",
        message_type="say",
    )
    assert result["message"] == "Wait what"
    assert "muffled" in result["tags"]


@patch("server.services.lucidity_communication_dampening.random.random", return_value=0.0)
@patch("server.services.lucidity_communication_dampening.random.randint", return_value=0)
def test_deranged_incoming_scrambles_words(_mock_randint, _mock_random):
    result = apply_communication_dampening(
        "one two three four",
        sender_tier="lucid",
        receiver_tier="deranged",
        message_type="chat",
    )
    assert "scrambled" in result["tags"]
    assert result["message"] != "one two three four"
