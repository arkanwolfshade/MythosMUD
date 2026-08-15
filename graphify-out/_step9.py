import json
from pathlib import Path
from datetime import datetime, timezone
from graphify.detect import save_manifest
from graphify.cli import _stamped_manifest_files
from graphify.analyze import graph_diff
from graphify.build import build_from_json
from networkx.readwrite import json_graph

extract = json.loads(Path("graphify-out/.graphify_extract.json").read_text(encoding="utf-8"))
detect = json.loads(Path("graphify-out/.graphify_detect.json").read_text(encoding="utf-8"))
G_new = build_from_json(extract, directed=False)
if Path("graphify-out/.graphify_old.json").exists():
    old_data = json.loads(Path("graphify-out/.graphify_old.json").read_text(encoding="utf-8"))
    G_old = json_graph.node_link_graph(old_data, edges="links")
    diff = graph_diff(G_old, G_new)
    print(diff["summary"])
    if diff["new_nodes"]:
        print("New nodes:", ", ".join(n["label"] for n in diff["new_nodes"][:5]))
    if diff["new_edges"]:
        print("New edges:", len(diff["new_edges"]))

input_tok = extract.get("input_tokens", 0)
output_tok = extract.get("output_tokens", 0)
cost_path = Path("graphify-out/cost.json")
if cost_path.exists():
    cost = json.loads(cost_path.read_text(encoding="utf-8"))
else:
    cost = {"runs": [], "total_input_tokens": 0, "total_output_tokens": 0}
cost["runs"].append(
    {
        "date": datetime.now(timezone.utc).isoformat(),
        "input_tokens": input_tok,
        "output_tokens": output_tok,
        "files": detect.get("total_files", 0),
    }
)
cost["total_input_tokens"] += input_tok
cost["total_output_tokens"] += output_tok
cost_path.write_text(json.dumps(cost, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"This run: {input_tok:,} input tokens, {output_tok:,} output tokens")
print(
    f"All time: {cost['total_input_tokens']:,} input, {cost['total_output_tokens']:,} output "
    f"({len(cost['runs'])} runs)"
)
