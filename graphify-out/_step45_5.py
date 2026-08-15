import json
from pathlib import Path
from graphify.diagnostics import diagnose_extraction, format_diagnostic_report
from graphify.build import build_from_json
from graphify.cluster import score_all
from graphify.analyze import suggest_questions
from graphify.report import generate
from graphify.export import to_json

root = r"C:\projects\MythosMUD"
extraction = json.loads(Path("graphify-out/.graphify_extract.json").read_text(encoding="utf-8"))
summary = diagnose_extraction(extraction, directed=False, root=root)
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

analysis = json.loads(Path("graphify-out/.graphify_analysis.json").read_text(encoding="utf-8"))
detection = json.loads(Path("graphify-out/.graphify_detect.json").read_text(encoding="utf-8"))
communities = {int(k): v for k, v in analysis["communities"].items()}
cohesion = {int(k): v for k, v in analysis["cohesion"].items()}

# Lazy labels: highest-degree-looking id (shortest last path segment), 2-5 words.
labels = {}
for cid, nodes in communities.items():
    sample = nodes[0] if nodes else f"community-{cid}"
    tail = str(sample).replace("\\", "/").split("/")[-1].replace("_", " ").replace("-", " ")
    words = [w for w in tail.split() if w][:5]
    labels[cid] = " ".join(words) if words else f"Community {cid}"

G = build_from_json(extraction, root=root, directed=False)
tokens = {"input": extraction.get("input_tokens", 0), "output": extraction.get("output_tokens", 0)}
questions = suggest_questions(G, communities, labels)
report = generate(
    G,
    communities,
    cohesion,
    labels,
    analysis["gods"],
    analysis["surprises"],
    detection,
    tokens,
    root,
    suggested_questions=questions,
)
Path("graphify-out/GRAPH_REPORT.md").write_text(report, encoding="utf-8")
Path("graphify-out/.graphify_labels.json").write_text(
    json.dumps({str(k): v for k, v in labels.items()}, ensure_ascii=False), encoding="utf-8"
)
wrote = to_json(G, communities, "graphify-out/graph.json", community_labels=labels, force=True)
print("Report updated with community labels; to_json wrote=", wrote)
