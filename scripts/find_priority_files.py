#!/usr/bin/env python3
"""Quick script to find files with most missing suppressions."""

import json
from pathlib import Path

data = json.load(open(Path("artifacts/suppression_audit.json")))
missing = list(data["missing_explanations"])
files = {}
for s in missing:
    files.setdefault(s["file"], []).append(s)

sorted_files = sorted(files.items(), key=lambda x: len(x[1]), reverse=True)
print("Top 30 files with missing explanations:")
for k, v in sorted_files[:30]:
    print(f"{len(v):3d}: {k}")
