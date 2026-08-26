#!/usr/bin/env python3
"""
Fail if docs/openapi/openapi.json or the §4 tag table in
docs/architecture/API_OPENAPI_SPECIFICATION.md are stale relative to the app's routes.

Regenerates both via generate_openapi_spec.py, then diffs against what's committed.
Used by the pre-commit hook and `make openapi-check`; also runnable standalone.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

WATCHED_PATHS = [
    "docs/openapi/openapi.json",
    "docs/architecture/API_OPENAPI_SPECIFICATION.md",
]


def main() -> int:
    # `uv run`, not sys.executable: pre-commit's python hooks run in an isolated venv that
    # lacks the project's dependencies (fastapi, python-dotenv, ...). `uv run` resolves to
    # the project's own environment regardless of what interpreter invoked this script.
    generate = subprocess.run(
        ["uv", "run", "python", "scripts/generate_openapi_spec.py"],
        cwd=project_root,
        check=False,
    )
    if generate.returncode != 0:
        return generate.returncode

    diff = subprocess.run(
        ["git", "diff", "--exit-code", "--", *WATCHED_PATHS],
        cwd=project_root,
        check=False,
    )
    if diff.returncode != 0:
        print(
            "OpenAPI spec or tag table is stale (see diff above). "
            "Run 'make openapi-spec' and commit the result.",
            file=sys.stderr,
        )
        return 1

    print("OpenAPI spec and tag table are current.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
