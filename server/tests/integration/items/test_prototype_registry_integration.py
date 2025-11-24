import json
from pathlib import Path

from server.game.items.prototype_registry import PrototypeRegistry


def write_payload(directory: Path, name: str, payload: dict):
    file_path = directory / f"{name}.json"
    file_path.write_text(json.dumps(payload, indent=2))
    return file_path


def test_registry_emits_observability_warning_for_malformed_payload(tmp_path: Path, caplog):
    valid = {
        "prototype_id": "artifact.miskatonic.codex",
        "name": "Codex of Whispered Secrets",
        "short_description": "a codex bound in eel-skin",
        "long_description": "Pages that shimmer with impossible glyphs.",
        "item_type": "artifact",
        "weight": 3.5,
        "base_value": 1200,
        "durability": 100,
        "flags": ["MAGICAL"],
        "wear_slots": ["off_hand"],
        "usage_restrictions": {},
        "stacking_rules": {"max_stack": 1},
        "effect_components": ["component.sanity_whisper"],
        "metadata": {},
        "tags": ["lore"],
    }
    malformed = {
        "prototype_id": "artifact.miskatonic.corrupted",
        "name": "",
        "item_type": "artifact",
        "flags": ["MAGICAL"],
        "wear_slots": [],
        "usage_restrictions": {},
        "stacking_rules": {"max_stack": 1},
        "effect_components": ["component.sanity_whisper"],
        "metadata": {},
        "tags": ["lore"],
    }
    write_payload(tmp_path, "valid_codex", valid)
    write_payload(tmp_path, "malformed_codex", malformed)

    with caplog.at_level("WARNING"):
        registry = PrototypeRegistry.load_from_path(tmp_path)

    assert any("invalid prototype payload" in record.message for record in caplog.records)
    assert registry.invalid_entries()[0]["prototype_id"] == "artifact.miskatonic.corrupted"
