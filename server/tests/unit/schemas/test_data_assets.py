"""
Repository data asset validation tests.

These tests walk the canonical data directories and ensure that all JSON
content adheres to the shared schemas. Professor Armitage would insist we
double-check every scrap of lore before presenting it to unsuspecting recruits.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from schemas.validator import create_validator


@pytest.mark.parametrize("environment", ["local", "unit_test", "e2e_test"])
def test_environment_data_assets_validate(environment: str) -> None:
    """All JSON content in data/<environment>/ complies with shared schemas."""
    project_root = Path(__file__).resolve().parents[3]
    data_root = project_root / "data" / environment

    if not data_root.exists():
        pytest.skip(f"Data directory for environment '{environment}' not present")

    room_validator = create_validator("unified")
    alias_validator = create_validator("alias")
    emote_validator = create_validator("emote")

    validation_errors: list[str] = []

    # Validate room files
    rooms_dir = data_root / "rooms"
    if rooms_dir.exists():
        for room_file in rooms_dir.rglob("*.json"):
            # Skip zone/subzone configuration files
            if room_file.name.endswith("zone_config.json"):
                continue
            if room_file.name.startswith("subzone_config"):
                continue

            with open(room_file, encoding="utf-8") as reader:
                room_payload = json.load(reader)

            errors = room_validator.validate_room(room_payload, str(room_file))
            validation_errors.extend(errors)

    # Validate emote definition file
    emote_file = data_root / "emotes.json"
    if emote_file.exists():
        with open(emote_file, encoding="utf-8") as reader:
            emote_payload = json.load(reader)
        validation_errors.extend(emote_validator.validate_emote_file(emote_payload, str(emote_file)))

    # Validate alias bundles, if any
    for alias_file in data_root.rglob("*_aliases.json"):
        with open(alias_file, encoding="utf-8") as reader:
            alias_payload = json.load(reader)
        validation_errors.extend(alias_validator.validate_alias_bundle(alias_payload, str(alias_file)))

    if validation_errors:
        failure_message = "\n".join(validation_errors)
        pytest.fail(f"Schema validation failures detected:\n{failure_message}")
