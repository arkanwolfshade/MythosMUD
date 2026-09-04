import json
import glob
from pathlib import Path
from graphify.cache import save_semantic_cache

root = r"C:\projects\MythosMUD"
spec = r"C:\Users\arkan\.claude\skills\graphify\references\extraction-spec.md"

new = json.loads(Path("graphify-out/.graphify_semantic_new.json").read_text(encoding="utf-8"))
uncached = [line for line in Path("graphify-out/.graphify_uncached.txt").read_text(encoding="utf-8").splitlines() if line]
saved = save_semantic_cache(
    new.get("nodes", []),
    new.get("edges", []),
    new.get("hyperedges", []),
    root=root,
    allowed_source_files=uncached,
    prompt_file=spec,
)
print(f"Cached {saved} files")

cached = (
    json.loads(Path("graphify-out/.graphify_cached.json").read_text(encoding="utf-8"))
    if Path("graphify-out/.graphify_cached.json").exists()
    else {"nodes": [], "edges": [], "hyperedges": []}
)
all_nodes = cached["nodes"] + new.get("nodes", [])
all_edges = cached["edges"] + new.get("edges", [])
all_hyperedges = cached.get("hyperedges", []) + new.get("hyperedges", [])
seen = set()
deduped = []
for n in all_nodes:
    if n["id"] not in seen:
        seen.add(n["id"])
        deduped.append(n)
merged = {
    "nodes": deduped,
    "edges": all_edges,
    "hyperedges": all_hyperedges,
    "input_tokens": new.get("input_tokens", 0),
    "output_tokens": new.get("output_tokens", 0),
}
Path("graphify-out/.graphify_semantic.json").write_text(
    json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(f"Semantic merge: {len(deduped)} nodes, {len(all_edges)} edges")

ast = json.loads(Path("graphify-out/.graphify_ast.json").read_text(encoding="utf-8"))
sem = merged
seen = {n["id"] for n in ast["nodes"]}
merged_nodes = list(ast["nodes"])
for n in sem["nodes"]:
    if n["id"] not in seen:
        merged_nodes.append(n)
        seen.add(n["id"])
extract = {
    "nodes": merged_nodes,
    "edges": ast["edges"] + sem["edges"],
    "hyperedges": sem.get("hyperedges", []),
    "input_tokens": sem.get("input_tokens", 0),
    "output_tokens": sem.get("output_tokens", 0),
}
Path("graphify-out/.graphify_extract.json").write_text(
    json.dumps(extract, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(f"Extract: {len(extract['nodes'])} nodes, {len(extract['edges'])} edges")
