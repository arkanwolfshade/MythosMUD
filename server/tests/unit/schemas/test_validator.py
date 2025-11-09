"""
Tests for shared JSON schema validator utilities.

These tests ensure that room validation remains functional while the new
alias and emote validation helpers behave as expected. As chronicled in
the restricted archives, consistent schema enforcement guards against
data corruption from the Outer Dark.
"""

from schemas.validator import create_validator


def test_unified_room_schema_accepts_minimal_valid_room():
    """A minimal valid room payload passes schema validation."""
    room_validator = create_validator("unified")

    room_payload = {
        "id": "earth_arkhamcity_test_room_silver_key_001",
        "name": "Silver Key Threshold",
        "description": "An antechamber shimmering with impossible geometries.",
        "plane": "earth",
        "zone": "arkhamcity",
        "sub_zone": "test_zone",
        "exits": {},
    }

    assert room_validator.validate_room(room_payload) == []


def test_alias_schema_flags_invalid_alias_name():
    """Alias validator rejects names that violate naming convention."""
    alias_validator = create_validator("alias")

    alias_payload = {
        "version": "1.0",
        "aliases": [
            {
                "name": "bad alias",  # whitespace disallowed
                "command": "say hello",
            }
        ],
    }

    errors = alias_validator.validate_alias_bundle(alias_payload, "bad_alias.json")
    assert errors
    assert "bad_alias.json" in errors[0]


def test_emote_schema_requires_player_name_placeholder():
    """Emote validator enforces {player_name} placeholder in observer message."""
    emote_validator = create_validator("emote")

    emote_payload = {
        "emotes": {
            "ominous": {
                "self_message": "You whisper secrets to the void.",
                "other_message": "An unsettling whisper echoes through the chamber.",
            }
        }
    }

    errors = emote_validator.validate_emote_file(emote_payload, "invalid_emote.json")
    assert errors
    assert "invalid_emote.json" in errors[0]
