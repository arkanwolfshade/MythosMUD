import json
from pathlib import Path

from graphify.analyze import god_nodes, suggest_questions, surprising_connections
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.export import to_json
from graphify.report import generate

extraction = json.loads(Path("graphify-out/.graphify_extract.json").read_text(encoding="utf-8"))
detection = json.loads(Path("graphify-out/.graphify_detect.json").read_text(encoding="utf-8"))

G = build_from_json(extraction, root=".", directed=False)
if G.number_of_nodes() == 0:
    print("ERROR: Graph is empty - extraction produced no nodes.")
    raise SystemExit(1)

communities = cluster(G)
cohesion = score_all(G, communities)
tokens = {"input": extraction.get("input_tokens", 0), "output": extraction.get("output_tokens", 0)}
gods = god_nodes(G)
surprises = surprising_connections(G, communities)
labels = {cid: "Community " + str(cid) for cid in communities}
questions = suggest_questions(G, communities, labels)

wrote = to_json(G, communities, "graphify-out/graph.json", force=True)
if not wrote:
    print("ERROR: refused to shrink graphify-out/graph.json (existing graph has more nodes; #479).")
    print("If this shrink is intentional (you deleted files), re-run a full build with --force.")
    raise SystemExit(1)

report = generate(
    G,
    communities,
    cohesion,
    labels,
    gods,
    surprises,
    detection,
    tokens,
    ".",
    suggested_questions=questions,
)
Path("graphify-out/GRAPH_REPORT.md").write_text(report, encoding="utf-8")
analysis = {
    "communities": {str(k): v for k, v in communities.items()},
    "cohesion": {str(k): v for k, v in cohesion.items()},
    "gods": gods,
    "surprises": surprises,
    "questions": questions,
}
Path("graphify-out/.graphify_analysis.json").write_text(
    json.dumps(analysis, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges, {len(communities)} communities")
