import json
from pathlib import Path

from graphify.cache import save_semantic_cache
from graphify.llm import extract_corpus_parallel

uncached = [line for line in Path("graphify-out/.graphify_uncached.txt").read_text(encoding="utf-8").splitlines() if line]
spec = Path.home() / ".claude" / "skills" / "graphify" / "references" / "extraction-spec.md"

if not uncached:
    result = {"nodes": [], "edges": [], "hyperedges": [], "input_tokens": 0, "output_tokens": 0}
    print("No uncached semantic files")
else:
    print(f"Gemini semantic extract: {len(uncached)} files")
    result = extract_corpus_parallel(uncached, backend="gemini")

Path("graphify-out/.graphify_semantic_new.json").write_text(
    json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
)
saved = save_semantic_cache(
    result.get("nodes", []),
    result.get("edges", []),
    result.get("hyperedges", []),
    root=".",
    allowed_source_files=uncached,
    prompt_file=str(spec),
)
print(f"Cached {saved} files; tokens in={result.get('input_tokens', 0)} out={result.get('output_tokens', 0)}")
print(f"New semantic: {len(result.get('nodes', []))} nodes, {len(result.get('edges', []))} edges")
