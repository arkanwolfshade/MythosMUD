"""Unit tests guarding OPENAPI_TAGS against drift from route-declared tags.

route-declared tags (what FastAPI actually renders) are the authority; OPENAPI_TAGS is
description metadata that must match them exactly. See #638.
"""

from __future__ import annotations

from server.app.factory import OPENAPI_TAGS, create_app


def _openapi_spec() -> object:
    """FastAPI's .openapi() is typed dict[str, Any]; erase that at the boundary."""
    return create_app().openapi()


def _route_declared_tags() -> set[str]:
    """Every tag any mounted route actually declares."""
    spec = _openapi_spec()
    tags: set[str] = set()
    if not isinstance(spec, dict):
        return tags
    paths = spec.get("paths", {})
    if not isinstance(paths, dict):
        return tags
    for operations in paths.values():
        if not isinstance(operations, dict):
            continue
        for operation in operations.values():
            if not isinstance(operation, dict):
                continue
            for tag in operation.get("tags", []):
                if isinstance(tag, str):
                    tags.add(tag)
    return tags


def test_openapi_tags_matches_route_declared_tags() -> None:
    route_tags = _route_declared_tags()
    metadata_tags = {tag["name"] for tag in OPENAPI_TAGS}

    missing = route_tags - metadata_tags
    assert not missing, (
        f"Tag(s) declared by a route but missing from OPENAPI_TAGS in server/app/factory.py: {sorted(missing)}"
    )

    dead = metadata_tags - route_tags
    assert not dead, f"OPENAPI_TAGS entry(ies) in server/app/factory.py not declared by any route: {sorted(dead)}"
