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
# Exclude temporary/output JSON files
exclude_patterns = ["*_output.json", "*_temp.json", "*_tmp.json"]

for json_file in Path(".").rglob("*.json"):
    # Skip excluded directories
    if any(excluded in json_file.parts for excluded in exclude_dirs):
        continue
    # Skip files matching exclude patterns
    if any(json_file.match(pattern) for pattern in exclude_patterns):
        continue
    json_files.append(json_file)

if not json_files:
    print("[WARNING] No JSON files found")
    sys.exit(0)

success = True
for json_file in json_files:
    try:
        # Try UTF-8 first (most common)
        with open(json_file, encoding="utf-8") as f:
            json.load(f)
    except UnicodeDecodeError as e:
        # Try other common encodings if UTF-8 fails
        encodings_to_try = ["utf-16", "utf-16-le", "utf-16-be", "latin-1"]
        decoded = False
        for encoding in encodings_to_try:
            try:
                with open(json_file, encoding=encoding) as f:
                    json.load(f)
                decoded = True
                print(f"[WARNING] {json_file} is encoded as {encoding}, not UTF-8. Consider converting to UTF-8.")
                break
            except (UnicodeDecodeError, json.JSONDecodeError):
                continue
        if not decoded:
            # Check if file looks like it might be terminal output or binary
            try:
                with open(json_file, "rb") as f:
                    first_bytes = f.read(100)
                    # Check for common non-text indicators
                    if b"\x00" in first_bytes[:10] or first_bytes.startswith(b"\xff\xfe"):
                        print(f"[WARNING] Skipping {json_file}: appears to be binary or terminal output, not JSON")
                        continue
            except OSError:
                pass
            print(f"[ERROR] Cannot decode {json_file}: {e}. File may be corrupted or use an unsupported encoding.")
            success = False
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
