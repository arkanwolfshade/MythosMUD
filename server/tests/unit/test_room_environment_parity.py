"""
Parity test for the room environment enum (#623).

Guards against the exact failure #623 documented: the canonical environment list
(server.models.world.ROOM_ENVIRONMENTS) drifting out of sync with the room validator schemas
and the map editor's dropdown, because each copy was maintained by hand.
"""

import json
import re
from pathlib import Path

from server.models.world import ROOM_ENVIRONMENTS

PROJECT_ROOT = Path(__file__).resolve().parents[3]
ROOM_HIERARCHY_SCHEMA = (
    PROJECT_ROOT / "tools" / "room_toolkit" / "room_validator" / "schemas" / "room_hierarchy_schema.json"
)
UNIFIED_ROOM_SCHEMA = (
    PROJECT_ROOT / "tools" / "room_toolkit" / "room_validator" / "schemas" / "unified_room_schema.json"
)
ROOM_EDIT_MODAL = PROJECT_ROOT / "client" / "src" / "components" / "map" / "RoomEditModal.tsx"


def _environment_enum_from_schema(schema_path: Path) -> set[str]:
    """Return the `environment` property's `enum` values from a room JSON schema."""
    with schema_path.open(encoding="utf-8") as f:
        schema = json.load(f)
    enum_values = schema["properties"]["environment"]["enum"]
    assert isinstance(enum_values, list)
    return set(enum_values)


def _environment_options_from_room_edit_modal() -> set[str]:
    """Return the non-empty `value`s of RoomEditModal.tsx's ENVIRONMENT_OPTIONS literal."""
    content = ROOM_EDIT_MODAL.read_text(encoding="utf-8")
    match = re.search(r"ENVIRONMENT_OPTIONS: EnvironmentOption\[\] = \[(.*?)\];", content, re.DOTALL)
    assert match is not None, "ENVIRONMENT_OPTIONS literal not found in RoomEditModal.tsx"
    values = re.findall(r"value:\s*'([^']*)'", match.group(1))
    return {value for value in values if value}


def test_room_hierarchy_schema_matches_canonical_environments() -> None:
    """room_hierarchy_schema.json's environment enum must equal ROOM_ENVIRONMENTS."""
    assert _environment_enum_from_schema(ROOM_HIERARCHY_SCHEMA) == set(ROOM_ENVIRONMENTS)


def test_unified_room_schema_matches_canonical_environments() -> None:
    """unified_room_schema.json's environment enum must equal ROOM_ENVIRONMENTS."""
    assert _environment_enum_from_schema(UNIFIED_ROOM_SCHEMA) == set(ROOM_ENVIRONMENTS)


def test_room_edit_modal_matches_canonical_environments() -> None:
    """RoomEditModal.tsx's dropdown options must equal ROOM_ENVIRONMENTS (ignoring the 'Not Set' sentinel)."""
    assert _environment_options_from_room_edit_modal() == set(ROOM_ENVIRONMENTS)
