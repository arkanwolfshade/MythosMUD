"""Unit tests for scripts/generate_openapi_spec.py's tag-table generation logic.

Covers the pure functions that turn an OpenAPI spec dict into section 4's markdown table:
route-declared tags are the authority (paths.*.*.tags), OPENAPI_TAGS supplies descriptions only,
and a mismatch between the two must fail loudly rather than emit a silently-wrong table. See #638.
"""

# pyright: reportPrivateUsage=false
# Reason: this module unit-tests the script's private tag-table helpers (_route_declared_tags, etc.).

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Protocol, cast

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "generate_openapi_spec.py"


class _GenerateOpenapiSpecModule(Protocol):
    """Typed surface of the loaded script, for the parts these tests exercise."""

    def _route_declared_tags(self, spec: dict[str, object]) -> list[str]: ...
    def _tag_descriptions(self, spec: dict[str, object]) -> dict[str, str]: ...
    def _render_tag_table(self, spec: dict[str, object]) -> str: ...


def _load_script() -> _GenerateOpenapiSpecModule:
    spec = importlib.util.spec_from_file_location("generate_openapi_spec_for_tests", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return cast(_GenerateOpenapiSpecModule, cast(object, mod))


@pytest.fixture(scope="module")
def script() -> _GenerateOpenapiSpecModule:
    return _load_script()


def _spec(paths_tags: list[list[str]], tag_block: list[dict[str, str]]) -> dict[str, object]:
    """Build a minimal OpenAPI-shaped dict: one operation per tag list in paths_tags."""
    paths: dict[str, object] = {}
    for i, tags in enumerate(paths_tags):
        paths[f"/route-{i}"] = {"get": {"tags": tags}}
    return {"paths": paths, "tags": tag_block}


def test_route_declared_tags_dedupes_and_preserves_first_seen_order(
    script: _GenerateOpenapiSpecModule,
) -> None:
    spec = _spec([["auth"], ["users", "auth"], ["users"]], [])
    assert script._route_declared_tags(spec) == ["auth", "users"]


def test_route_declared_tags_ignores_non_string_and_malformed_entries(
    script: _GenerateOpenapiSpecModule,
) -> None:
    spec: dict[str, object] = {
        "paths": {
            "/a": {"get": {"tags": ["auth", 123]}},
            "/b": "not-a-dict",
            "/c": {"get": "not-a-dict", "post": {"tags": ["users"]}},
        }
    }
    assert script._route_declared_tags(spec) == ["auth", "users"]


def test_tag_descriptions_reads_top_level_tags_block(script: _GenerateOpenapiSpecModule) -> None:
    spec = _spec([], [{"name": "auth", "description": "Login and registration."}])
    assert script._tag_descriptions(spec) == {"auth": "Login and registration."}


def test_render_tag_table_orders_by_description_block_and_matches_route_tags(
    script: _GenerateOpenapiSpecModule,
) -> None:
    spec = _spec(
        [["users"], ["auth"]],
        [
            {"name": "auth", "description": "Authn."},
            {"name": "users", "description": "Users."},
        ],
    )
    table = script._render_tag_table(spec)
    assert table.splitlines() == [
        "| Tag | Description |",
        "|-----|-------------|",
        "| auth | Authn. |",
        "| users | Users. |",
    ]


def test_render_tag_table_raises_when_route_tag_has_no_description(
    script: _GenerateOpenapiSpecModule,
) -> None:
    spec = _spec([["command"]], [])
    with pytest.raises(SystemExit, match="command"):
        _ = script._render_tag_table(spec)


def test_render_tag_table_raises_when_metadata_tag_has_no_route(
    script: _GenerateOpenapiSpecModule,
) -> None:
    spec = _spec([], [{"name": "api", "description": "Dead tag."}])
    with pytest.raises(SystemExit, match="api"):
        _ = script._render_tag_table(spec)
