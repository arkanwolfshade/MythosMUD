#!/usr/bin/env python3
"""
Create the new test suite directory structure.

This script creates all directories and __init__.py files for the new
test suite organization.
"""

import sys
from pathlib import Path

# Define the complete structure
STRUCTURE = {
    "fixtures": [],
    "unit": [
        "api",
        "commands",
        "chat",
        "player",
        "npc",
        "world",
        "events",
        "auth",
        "infrastructure",
        "middleware",
        "models",
        "services",
        "realtime",
        "logging",
        "utilities",
    ],
    "integration": ["api", "commands", "chat", "events", "npc", "movement", "nats", "comprehensive"],
    "e2e": [],
    "performance": [],
    "security": [],
    "coverage": [],
    "regression": [],
    "monitoring": [],
    "verification": [],
}


def main():
    """Create the directory structure."""
    # Get base path (server/tests)
    script_dir = Path(__file__).parent
    base = script_dir.parent

    created_dirs = []
    created_inits = []

    # Create directories and __init__.py files
    for category, subdirs in STRUCTURE.items():
        cat_path = base / category

        # Create category directory
        if not cat_path.exists():
            cat_path.mkdir(parents=True, exist_ok=True)
            created_dirs.append(str(cat_path.relative_to(base)))

        # Create __init__.py for category
        init_file = cat_path / "__init__.py"
        if not init_file.exists():
            init_file.write_text(f'"""Test suite - {category.capitalize()} category."""\n')
            created_inits.append(str(init_file.relative_to(base)))

        # Create subdirectories
        for subdir in subdirs:
            sub_path = cat_path / subdir

            # Create subdirectory
            if not sub_path.exists():
                sub_path.mkdir(parents=True, exist_ok=True)
                created_dirs.append(str(sub_path.relative_to(base)))

            # Create __init__.py for subdirectory
            sub_init = sub_path / "__init__.py"
            if not sub_init.exists():
                sub_init.write_text(f'"""Test suite - {category.capitalize()}/{subdir} tests."""\n')
                created_inits.append(str(sub_init.relative_to(base)))

    # Print summary
    print("=" * 70)
    print("NEW TEST STRUCTURE CREATED")
    print("=" * 70)
    print()
    print(f"Created {len(created_dirs)} new directories")
    print(f"Created {len(created_inits)} __init__.py files")
    print()

    if created_dirs:
        print("New directories:")
        for d in sorted(created_dirs):
            print(f"  + {d}/")

    if created_inits:
        print()
        print("New __init__.py files:")
        for f in sorted(created_inits):
            print(f"  + {f}")

    print()
    print("[SUCCESS] Directory structure creation complete!")
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
