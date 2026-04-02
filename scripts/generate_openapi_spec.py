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

# Load environment before any server imports (same as server/main.py)
project_root = Path(__file__).resolve().parent.parent
env_local = project_root / ".env.local"
if env_local.exists():
    from dotenv import load_dotenv

    load_dotenv(env_local, override=False)

# Add project root to path so server imports resolve
sys.path.insert(0, str(project_root))


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

    out_dir = project_root / "docs" / "openapi"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "openapi.json"

    # Keep file ending stable for pre-commit: exactly one trailing newline, never a blank extra line.
    rendered = json.dumps(spec, indent=2)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        _ = f.write(rendered.rstrip("\n") + "\n")

    print(f"OpenAPI spec written to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
