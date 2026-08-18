import json
import glob
from pathlib import Path
from graphify.cache import save_semantic_cache

chunks = sorted(glob.glob("graphify-out/.graphify_chunk_*.json"))
print("chunks:", chunks)
all_nodes, all_edges, all_hyperedges = [], [], []
total_in, total_out = 0, 0
for c in chunks:
    d = json.loads(Path(c).read_text(encoding="utf-8"))
    n, e, h = len(d.get("nodes", [])), len(d.get("edges", [])), len(d.get("hyperedges", []))
    print(f"  {c}: {n} nodes, {e} edges, {h} hyperedges")
    if "nodes" not in d or "edges" not in d:
        raise SystemExit(f"invalid chunk {c}")
    all_nodes += d.get("nodes", [])
    all_edges += d.get("edges", [])
    all_hyperedges += d.get("hyperedges", [])
    total_in += d.get("input_tokens", 0)
    total_out += d.get("output_tokens", 0)

Path("graphify-out/.graphify_semantic_new.json").write_text(
    json.dumps(
        {
            "nodes": all_nodes,
            "edges": all_edges,
            "hyperedges": all_hyperedges,
            "input_tokens": total_in,
            "output_tokens": total_out,
        },
        indent=2,
        ensure_ascii=False,
    ),
    encoding="utf-8",
)
print(f"Merged {len(chunks)} chunks: {len(all_nodes)} nodes, {len(all_edges)} edges")

new = json.loads(Path("graphify-out/.graphify_semantic_new.json").read_text(encoding="utf-8"))
uncached_path = Path("graphify-out/.graphify_uncached.txt")
uncached = (
    [line for line in uncached_path.read_text(encoding="utf-8").splitlines() if line]
    if uncached_path.exists()
    else []
)
saved = save_semantic_cache(
    new.get("nodes", []),
    new.get("edges", []),
    new.get("hyperedges", []),
    root=r"c:\projects\MythosMUD",
    allowed_source_files=uncached,
    prompt_file=r"C:\Users\arkan\.claude\skills\graphify\references\extraction-spec.md",
)
print(f"Cached {saved} files")

cached_path = Path("graphify-out/.graphify_cached.json")
cached = (
    json.loads(cached_path.read_text(encoding="utf-8"))
    if cached_path.exists()
    else {"nodes": [], "edges": [], "hyperedges": []}
)
all_nodes2 = cached["nodes"] + new.get("nodes", [])
all_edges2 = cached["edges"] + new.get("edges", [])
all_hyper2 = cached.get("hyperedges", []) + new.get("hyperedges", [])
seen: set[str] = set()
deduped = []
for n in all_nodes2:
    if n["id"] not in seen:
        seen.add(n["id"])
        deduped.append(n)
Path("graphify-out/.graphify_semantic.json").write_text(
    json.dumps(
        {
            "nodes": deduped,
            "edges": all_edges2,
            "hyperedges": all_hyper2,
            "input_tokens": new.get("input_tokens", 0),
            "output_tokens": new.get("output_tokens", 0),
        },
        indent=2,
        ensure_ascii=False,
    ),
    encoding="utf-8",
)
print(f"Semantic: {len(deduped)} nodes, {len(all_edges2)} edges")

ast = json.loads(Path("graphify-out/.graphify_ast.json").read_text(encoding="utf-8"))
sem = json.loads(Path("graphify-out/.graphify_semantic.json").read_text(encoding="utf-8"))
seen = {n["id"] for n in ast["nodes"]}
merged_nodes = list(ast["nodes"])
for n in sem["nodes"]:
    if n["id"] not in seen:
        merged_nodes.append(n)
        seen.add(n["id"])
merged = {
    "nodes": merged_nodes,
    "edges": ast["edges"] + sem["edges"],
    "hyperedges": sem.get("hyperedges", []),
    "input_tokens": sem.get("input_tokens", 0),
    "output_tokens": sem.get("output_tokens", 0),
}
Path("graphify-out/.graphify_extract.json").write_text(
    json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(
    f"Extract: {len(merged_nodes)} nodes, {len(merged['edges'])} edges "
    f"({len(ast['nodes'])} AST + {len(sem['nodes'])} semantic)"
)
