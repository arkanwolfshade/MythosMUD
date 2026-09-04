import json
from pathlib import Path
from graphify.llm import extract_corpus_parallel

uncached = [
    line
    for line in Path("graphify-out/.graphify_uncached.txt").read_text(encoding="utf-8").splitlines()
    if line
]
result = extract_corpus_parallel(uncached, backend="gemini")
Path("graphify-out/.graphify_semantic_new.json").write_text(
    json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(
    f"Semantic: {len(result.get('nodes', []))} nodes, "
    f"{len(result.get('edges', []))} edges, "
    f"{result.get('input_tokens', 0)} in / {result.get('output_tokens', 0)} out"
)
