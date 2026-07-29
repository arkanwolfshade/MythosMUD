import json
from pathlib import Path

from graphify.extract import extract

detect = json.loads(Path("graphify-out/.graphify_detect.json").read_text(encoding="utf-8"))
code_files = [Path(f) for f in detect.get("files", {}).get("code", [])]
existing = json.loads(Path("graphify-out/.graphify_ast.json").read_text(encoding="utf-8"))
covered = {n.get("source_file") for n in existing.get("nodes", []) if n.get("source_file")}

# Retry files that produced no nodes (normalize to absolute for comparison)
missing = []
for f in code_files:
    abs_s = str(f.resolve())
    rel_s = str(f.relative_to(Path(".").resolve())) if f.is_relative_to(Path(".").resolve()) else abs_s
    if abs_s not in covered and rel_s not in covered and abs_s.replace("\\", "/") not in {
        str(c).replace("\\", "/") for c in covered
    } and rel_s.replace("\\", "/") not in {str(c).replace("\\", "/") for c in covered}:
        missing.append(f)

print(f"Retrying {len(missing)} files with parallel=False")
if missing:
    result = extract(missing, cache_root=Path("."), parallel=False)
    existing["nodes"].extend(result.get("nodes", []))
    existing["edges"].extend(result.get("edges", []))
    Path("graphify-out/.graphify_ast.json").write_text(
        json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Retry added {len(result.get('nodes', []))} nodes, {len(result.get('edges', []))} edges")
print(f"AST total: {len(existing['nodes'])} nodes, {len(existing['edges'])} edges")
