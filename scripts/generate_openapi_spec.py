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


def main() -> int:
    """Generate and write OpenAPI spec to docs/openapi/openapi.json."""
    from server.app.factory import create_app

    app = create_app()
    spec = app.openapi()

    out_dir = project_root / "docs" / "openapi"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "openapi.json"

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2)

    print(f"OpenAPI spec written to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
