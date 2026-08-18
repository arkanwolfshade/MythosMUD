import json
from pathlib import Path

from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.diagnostics import diagnose_extraction, format_diagnostic_report
from graphify.export import to_json
from graphify.report import generate

ROOT = Path(r"C:\projects\MythosMUD\server")
OUT = Path("graphify-out")

ast = json.loads((OUT / ".graphify_ast.json").read_text(encoding="utf-8"))
sem = json.loads((OUT / ".graphify_semantic.json").read_text(encoding="utf-8"))

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
(OUT / ".graphify_extract.json").write_text(
    json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(f"Merged: {len(merged_nodes)} nodes, {len(merged['edges'])} edges "
      f"({len(ast['nodes'])} AST + {len(sem['nodes'])} semantic)")

detection = json.loads((OUT / ".graphify_detect.json").read_text(encoding="utf-8"))
G = build_from_json(merged, root=str(ROOT), directed=False)
if G.number_of_nodes() == 0:
    print("ERROR: Graph is empty - extraction produced no nodes.")
    raise SystemExit(1)

communities = cluster(G)
cohesion = score_all(G, communities)
tokens = {"input": merged.get("input_tokens", 0), "output": merged.get("output_tokens", 0)}
gods = god_nodes(G)
surprises = surprising_connections(G, communities)
labels = {cid: "Community " + str(cid) for cid in communities}
questions = suggest_questions(G, communities, labels)

wrote = to_json(G, communities, str(OUT / "graph.json"))
if not wrote:
    print("ERROR: refused to shrink graphify-out/graph.json (existing graph has more nodes; #479).")
    print("If this shrink is intentional (you deleted files), re-run a full build with --force.")
    raise SystemExit(1)

report = generate(
    G, communities, cohesion, labels, gods, surprises, detection, tokens, str(ROOT),
    suggested_questions=questions,
)
(OUT / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
analysis = {
    "communities": {str(k): v for k, v in communities.items()},
    "cohesion": {str(k): v for k, v in cohesion.items()},
    "gods": gods,
    "surprises": surprises,
    "questions": questions,
}
(OUT / ".graphify_analysis.json").write_text(
    json.dumps(analysis, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges, {len(communities)} communities")

summary = diagnose_extraction(merged, directed=False, root=str(ROOT))
print(format_diagnostic_report(summary))
flags = [
    f"{summary[k]} {label}"
    for k, label in (
        ("dangling_endpoint_edges", "dangling-endpoint edges"),
        ("missing_endpoint_edges", "missing-endpoint edges"),
        ("self_loop_edges", "self-loop edges"),
        ("directed_same_endpoint_collapsed_edges", "collapsed (directed) edges"),
        ("undirected_same_endpoint_collapsed_edges", "collapsed (undirected) edges"),
    )
    if summary.get(k, 0)
]
print(
    "GRAPH HEALTH WARNING: " + "; ".join(flags) + " - graph may be incomplete/corrupt."
    if flags
    else "Graph health: OK (no dangling/missing/collapsed edges)."
)
