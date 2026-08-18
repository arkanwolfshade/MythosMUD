import json
from pathlib import Path

from graphify.cache import check_semantic_cache, save_semantic_cache
from graphify.llm import extract_corpus_parallel

SPEC_PATH = r"C:\Users\arkan\.claude\skills\graphify\references\extraction-spec.md"
ROOT = Path(r"C:\projects\MythosMUD\server")

detect = json.loads(Path("graphify-out/.graphify_detect.json").read_text(encoding="utf-8"))
all_files = [f for cat in ("document", "paper", "image") for f in detect["files"].get(cat, [])]
cached_nodes, cached_edges, cached_hyperedges, uncached = check_semantic_cache(
    all_files, root=str(ROOT), prompt_file=SPEC_PATH
)
print(f"Cache: {len(all_files) - len(uncached)} files hit, {len(uncached)} files need extraction")

new = {"nodes": [], "edges": [], "hyperedges": [], "input_tokens": 0, "output_tokens": 0}
if uncached:
    paths = [Path(f) for f in uncached]
    print(f"Gemini semantic extract: {len(paths)} files")
    new = extract_corpus_parallel(paths, backend="gemini", root=ROOT, cache_root=ROOT)
    saved = save_semantic_cache(
        new.get("nodes", []),
        new.get("edges", []),
        new.get("hyperedges", []),
        root=str(ROOT),
        allowed_source_files=uncached,
        prompt_file=SPEC_PATH,
    )
    print(f"Cached {saved} files")
    print(f"Gemini tokens in={new.get('input_tokens', 0)} out={new.get('output_tokens', 0)}")

seen: set[str] = set()
deduped = []
for n in cached_nodes + new.get("nodes", []):
    if n["id"] not in seen:
        seen.add(n["id"])
        deduped.append(n)
merged = {
    "nodes": deduped,
    "edges": cached_edges + new.get("edges", []),
    "hyperedges": cached_hyperedges + new.get("hyperedges", []),
    "input_tokens": new.get("input_tokens", 0),
    "output_tokens": new.get("output_tokens", 0),
}
Path("graphify-out/.graphify_semantic.json").write_text(
    json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(
    f"Extraction complete - {len(deduped)} nodes, {len(merged['edges'])} edges "
    f"({len(cached_nodes)} from cache, {len(new.get('nodes', []))} new)"
)
