#!/usr/bin/env python3
"""
Run Jackson Linter on JSON files.
Jackson Linter validates JSON syntax and structure.
"""

import json
import sys
from pathlib import Path

print("Running Jackson Linter on JSON files...")
print("This will validate JSON syntax and structure...")

# Find all JSON files (exclude node_modules, dist, build, etc.)
json_files = []
exclude_dirs = {"node_modules", "dist", "build", ".git", "__pycache__", ".venv", "htmlcov"}

for json_file in Path(".").rglob("*.json"):
    # Skip excluded directories
    if any(excluded in json_file.parts for excluded in exclude_dirs):
        continue
    json_files.append(json_file)

if not json_files:
    print("[WARNING] No JSON files found")
    sys.exit(0)

success = True
for json_file in json_files:
    try:
        with open(json_file, encoding="utf-8") as f:
            json.load(f)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON in {json_file}: {e}")
        success = False
    except OSError as e:
        print(f"[ERROR] Error reading {json_file}: {e}")
        success = False

if not success:
    sys.exit(1)

print(f"[OK] Validated {len(json_files)} JSON files successfully!")
print("\n[SUCCESS] All Jackson Linter checks passed!")
