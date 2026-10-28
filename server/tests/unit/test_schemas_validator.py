"""Unit tests for the shared JSON-schema validator (schemas/validator.py).

Exercises the real jsonschema library (a required runtime dependency, so the module no
longer carries an "unavailable" fallback) against small throwaway schemas.
"""

import json
from pathlib import Path

import pytest

from schemas.validator import SchemaValidator, create_validator

_SCHEMA: dict[str, object] = {
    "type": "object",
    "properties": {"id": {"type": "string"}, "exits": {"type": "object"}},
    "required": ["id"],
}


@pytest.fixture
def validator(tmp_path: Path) -> SchemaValidator:
    schema_file = tmp_path / "schema.json"
    _ = schema_file.write_text(json.dumps(_SCHEMA), encoding="utf-8")
    return SchemaValidator(str(schema_file), schema_name="test")


def test_valid_document_has_no_errors(validator: SchemaValidator) -> None:
    assert validator.validate_data({"id": "room_1"}) == []


def test_invalid_document_reports_path_and_file(validator: SchemaValidator) -> None:
    [error] = validator.validate_data({"id": 7}, "rooms/a.json")
    assert error.startswith("rooms/a.json: Schema validation failed at id:")


def test_missing_required_field_reported_at_root(validator: SchemaValidator) -> None:
    [error] = validator.validate_room({})
    assert error.startswith("Schema validation failed at root:")


def test_validate_room_file_handles_bad_json(validator: SchemaValidator, tmp_path: Path) -> None:
    bad = tmp_path / "bad.json"
    _ = bad.write_text("{not json", encoding="utf-8")
    [error] = validator.validate_room_file(bad)
    assert "Invalid JSON" in error


def test_validate_room_database_keeps_only_failures(validator: SchemaValidator) -> None:
    results = validator.validate_room_database({"ok": {"id": "ok"}, "bad": {"id": 1}})
    assert list(results) == ["bad"]
    assert results["bad"][0].startswith("Room bad: ")


def test_missing_schema_file_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="Schema file not found"):
        _ = SchemaValidator(str(tmp_path / "nope.json"))


def test_invalid_schema_file_raises(tmp_path: Path) -> None:
    broken = tmp_path / "broken.json"
    _ = broken.write_text("{", encoding="utf-8")
    with pytest.raises(ValueError, match="Invalid schema file"):
        _ = SchemaValidator(str(broken))


@pytest.mark.parametrize("name", ["unified", "room", "intersection", "emote"])
def test_create_validator_known_schemas_load(name: str) -> None:
    assert create_validator(name).schema_name == name


def test_create_validator_alias_schema_removed() -> None:
    """#680: player aliases moved to PostgreSQL, so the JSON alias bundle schema is gone."""
    with pytest.raises(ValueError, match="Unknown schema name: alias"):
        _ = create_validator("alias")


def test_exit_helpers_accept_both_exit_formats(validator: SchemaValidator) -> None:
    assert validator.get_exit_target("room_2") == "room_2"
    assert validator.get_exit_target({"target": "room_3", "flags": ["one_way"]}) == "room_3"
    assert validator.get_exit_target(None) is None
    assert validator.get_exit_flags({"target": "room_3", "flags": ["one_way"]}) == ["one_way"]
    assert validator.get_exit_flags("room_2") == []


@pytest.mark.parametrize(
    ("room_id", "valid"),
    [
        ("earth_arkhamcity_sanitarium_room_foyer_001", True),
        ("earth_arkhamcity_downtown_intersection_main_church", True),
        ("Earth_Bad_Room", False),
        ("earth_arkhamcity_sanitarium_room_foyer_1", False),
    ],
)
def test_is_room_id_valid(validator: SchemaValidator, room_id: str, valid: bool) -> None:
    assert validator.is_room_id_valid(room_id) is valid
