"""Label communities from dominant node labels (top communities get curated names)."""
import json
import re
from collections import Counter
from pathlib import Path

from graphify.analyze import god_nodes, suggest_questions, surprising_connections
from graphify.build import build_from_json
from graphify.cluster import score_all
from graphify.report import generate

extraction = json.loads(Path("graphify-out/.graphify_extract.json").read_text(encoding="utf-8"))
detection = json.loads(Path("graphify-out/.graphify_detect.json").read_text(encoding="utf-8"))
analysis = json.loads(Path("graphify-out/.graphify_analysis.json").read_text(encoding="utf-8"))

G = build_from_json(extraction, root=".", directed=False)
communities = {int(k): v for k, v in analysis["communities"].items()}
cohesion = {int(k): v for k, v in analysis["cohesion"].items()}
tokens = {"input": extraction.get("input_tokens", 0), "output": extraction.get("output_tokens", 0)}


def _auto_label(node_ids: list[str]) -> str:
    labels = []
    for nid in node_ids[:40]:
        data = G.nodes.get(nid, {})
        label = str(data.get("label") or nid)
        # strip file suffixes / path noise
        label = re.sub(r"\.[a-z]{1,4}$", "", label, flags=re.I)
        label = label.replace("_", " ").replace("-", " ")
        labels.append(label.strip())
    if not labels:
        return "Unlabeled"
    # Prefer shorter, title-cased top label words
    top = Counter(labels).most_common(1)[0][0]
    words = [w for w in top.split() if w][:5]
    name = " ".join(words)
    return name[:60] if name else "Unlabeled"


labels: dict[int, str] = {}
sized = sorted(communities.items(), key=lambda kv: len(kv[1]), reverse=True)
for cid, members in sized:
    labels[cid] = _auto_label(members)

# Curate a few largest communities with clearer names where auto-label is weak
for cid, members in sized[:15]:
    sample = " ".join(str(G.nodes.get(n, {}).get("label", n)) for n in members[:25]).lower()
    if "connectionmanager" in sample or "connection_manager" in sample:
        labels[cid] = "Connection Manager"
    elif "playerposition" in sample or "player_position" in sample:
        labels[cid] = "Player Position Service"
    elif "spell" in sample and "target" in sample:
        labels[cid] = "Spell Targeting"
    elif "projector" in sample or "eventlog" in sample:
        labels[cid] = "Client Event Projector"
    elif "whisper" in sample:
        labels[cid] = "Whisper E2E Specs"
    elif "quest" in sample and ("collect" in sample or "e2e" in sample):
        labels[cid] = "Quest E2E Specs"
    elif "websocket" in sample and "room" in sample:
        labels[cid] = "WebSocket Room Updates"

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
    ".",
    suggested_questions=questions,
)
Path("graphify-out/GRAPH_REPORT.md").write_text(report, encoding="utf-8")
Path("graphify-out/.graphify_labels.json").write_text(
    json.dumps({str(k): v for k, v in labels.items()}, ensure_ascii=False), encoding="utf-8"
)
# refresh analysis questions
analysis["questions"] = questions
Path("graphify-out/.graphify_analysis.json").write_text(
    json.dumps(analysis, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(f"Labeled {len(labels)} communities; top 8:")
for cid, members in sized[:8]:
    print(f"  {cid}: {labels[cid]} ({len(members)} nodes)")
