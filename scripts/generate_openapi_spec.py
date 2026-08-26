#!/usr/bin/env python3
"""
Generate OpenAPI specification from the MythosMUD FastAPI application.

Exports the OpenAPI 3.0 schema to docs/openapi/openapi.json for:
- API contract documentation
- Client generation (e.g. openapi-generator, orval)
- CI validation
- Contract testing

Usage:
    uv run python scripts/generate_openapi_spec.py
    # or from project root:
    python scripts/generate_openapi_spec.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Load environment before any server imports (same as server/main.py). .env.local is the local
# dev convention; .env.unit_test is what CI creates before this script runs (see ci.yml's "Set up
# test environment file" step) and carries SERVER_PORT, which config validation requires and no
# job-level env var supplies.
project_root = Path(__file__).resolve().parent.parent
env_local = project_root / ".env.local"
env_unit_test = project_root / ".env.unit_test"
env_file = env_local if env_local.exists() else env_unit_test if env_unit_test.exists() else None
if env_file is not None:
    from dotenv import load_dotenv

    load_dotenv(env_file, override=False)

# Add project root to path so server imports resolve
sys.path.insert(0, str(project_root))


TAG_TABLE_START = "<!-- BEGIN GENERATED: openapi-tags -- edit server/app/factory.py OPENAPI_TAGS, then run `make openapi-spec` -->"  # noqa: E501
TAG_TABLE_END = "<!-- END GENERATED: openapi-tags -->"
TAG_TABLE_DOC = Path("docs") / "architecture" / "API_OPENAPI_SPECIFICATION.md"


def _route_declared_tags(spec: dict[str, object]) -> list[str]:
    """Tags actually declared by routes, in first-seen order. This is the authority."""
    paths = spec.get("paths", {})
    if not isinstance(paths, dict):
        return []
    seen: dict[str, None] = {}
    for operations in paths.values():
        if not isinstance(operations, dict):
            continue
        for operation in operations.values():
            if not isinstance(operation, dict):
                continue
            for tag in operation.get("tags", []):
                if isinstance(tag, str):
                    seen[tag] = None
    return list(seen)


def _tag_descriptions(spec: dict[str, object]) -> dict[str, str]:
    """name -> description, from the spec's top-level tags block (OPENAPI_TAGS)."""
    tags = spec.get("tags", [])
    if not isinstance(tags, list):
        return {}
    descriptions: dict[str, str] = {}
    for entry in tags:
        if isinstance(entry, dict) and isinstance(entry.get("name"), str):
            descriptions[entry["name"]] = str(entry.get("description", ""))
    return descriptions


def _render_tag_table(spec: dict[str, object]) -> str:
    """Build the markdown table, failing loudly if a route tag has no description."""
    route_tags = _route_declared_tags(spec)
    descriptions = _tag_descriptions(spec)

    undescribed = [t for t in route_tags if t not in descriptions]
    if undescribed:
        raise SystemExit(
            f"OpenAPI tag(s) declared by routes but missing from OPENAPI_TAGS "
            f"(server/app/factory.py): {', '.join(sorted(undescribed))}"
        )

    dead = [name for name in descriptions if name not in route_tags]
    if dead:
        raise SystemExit(
            f"OPENAPI_TAGS entry(ies) not declared by any route "
            f"(server/app/factory.py): {', '.join(sorted(dead))}"
        )

    lines = ["| Tag | Description |", "|-----|-------------|"]
    for name in descriptions:
        lines.append(f"| {name} | {descriptions[name]} |")
    return "\n".join(lines)


def _update_tag_table_doc(spec: dict[str, object]) -> None:
    """Rewrite the generated tag table between its markers in the spec doc."""
    doc_path = project_root / TAG_TABLE_DOC
    content = doc_path.read_text(encoding="utf-8")
    if TAG_TABLE_START not in content or TAG_TABLE_END not in content:
        raise SystemExit(f"Generated tag table markers not found in {TAG_TABLE_DOC}")

    before, rest = content.split(TAG_TABLE_START, 1)
    _, after = rest.split(TAG_TABLE_END, 1)
    table = _render_tag_table(spec)
    new_content = f"{before}{TAG_TABLE_START}\n\n{table}\n\n{TAG_TABLE_END}{after}"
    doc_path.write_text(new_content, encoding="utf-8", newline="\n")


def _sanitize_token_examples(obj: object) -> object:
    """Replace auth token examples with clearly fake placeholders."""
    if isinstance(obj, dict):
        sanitized: dict[object, object] = {}
        for key, value in obj.items():
            if isinstance(key, str) and key in {"access_token", "refresh_token"} and isinstance(value, str):
                sanitized[key] = "FAKE_TOKEN_FOR_DOCUMENTATION_ONLY"
            else:
                sanitized[key] = _sanitize_token_examples(value)
        return sanitized
    if isinstance(obj, list):
        return [_sanitize_token_examples(item) for item in obj]
    return obj


def main() -> int:
    """Generate and write OpenAPI spec to docs/openapi/openapi.json."""
    from server.app.factory import create_app

    app = create_app()
    spec = _sanitize_token_examples(app.openapi())
    if not isinstance(spec, dict):
        raise SystemExit("app.openapi() did not produce a JSON object")

    out_dir = project_root / "docs" / "openapi"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "openapi.json"

    # Keep file ending stable for pre-commit: exactly one trailing newline, never a blank extra line.
    rendered = json.dumps(spec, indent=2)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        _ = f.write(rendered.rstrip("\n") + "\n")

    print(f"OpenAPI spec written to {out_path}")

    _update_tag_table_doc(spec)
    print(f"Tag table regenerated in {TAG_TABLE_DOC}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
