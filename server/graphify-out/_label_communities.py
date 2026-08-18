import json
import re
from pathlib import Path

from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.build import build_from_json
from graphify.export import to_json
from graphify.report import generate

ROOT = Path(r"C:\projects\MythosMUD\server")
OUT = Path("graphify-out")

CURATED = {
    0: "Command Factories Mix",
    1: "Combat Events NATS",
    2: "NPC Population Event Bus",
    3: "Realtime Memory Rooms",
    4: "NPC Combat Services",
    5: "CORS And NATS Pool",
    6: "Auth Endpoints Subjects",
    7: "Player Effects Schemas",
    8: "Container Models Corpses",
    9: "Dialogue Definitions API",
    10: "WebSocket Connection Manager",
    11: "Exceptions Error Context",
    12: "Command Factory Base",
    13: "Character Creation Stats",
    14: "Admin Mute Combat Loader",
    15: "Maps API Zones",
    16: "Container Service Persistence",
    17: "Inventory Pickup Commands",
    18: "Async Persistence Layer",
    19: "Inventory Item Matching",
    20: "Pydantic Error Handlers",
    21: "Connection Manager Methods",
    22: "NPC Admin Instances",
    23: "Magic Service Lifespan",
    24: "Quest Service Flow",
    25: "Lifespan Event Subscriptions",
    26: "Lifespan Protocols Time",
    27: "Command Communication Models",
    28: "Chat Whisper Command Flows",
    29: "Container Persistence Helpers",
    30: "Teleport Goto Helpers",
    31: "Container Inventory Helpers",
    32: "Spell Effect Types",
    33: "Cache Service LRU",
    34: "Passive Lucidity Flux",
    35: "Websocket Initial State",
    36: "Command Type Models",
    37: "NPC Definition CRUD",
    38: "Chat Channel Senders",
    39: "Room Models Movement",
}


def humanize(text: str) -> str:
    stem = Path(str(text).replace("\\", "/")).name
    stem = re.sub(r"\.(py|md)$", "", stem)
    stem = stem.replace("-", "_")
    parts = [p for p in stem.split("_") if p and p not in {"py", "md"}]
    words = [p.capitalize() if p.islower() else p for p in parts[:4]]
    return " ".join(words)[:40] if words else "Community"


rows = json.loads((OUT / "_community_summary.json").read_text(encoding="utf-8"))
labels: dict[int, str] = {}
used: set[str] = set(CURATED.values())
for row in rows:
    cid = int(row["cid"])
    if cid in CURATED:
        labels[cid] = CURATED[cid]
        continue
    dir_name = humanize(row["top_dir"])
    file_hint = ""
    if row["top_files"]:
        file_hint = humanize(row["top_files"][0].split(":")[0])
    name = f"{dir_name} {file_hint}".strip()
    if name in used or not name:
        name = f"{name} {cid}".strip()
    used.add(name)
    labels[cid] = name[:48]

extraction = json.loads((OUT / ".graphify_extract.json").read_text(encoding="utf-8"))
detection = json.loads((OUT / ".graphify_detect.json").read_text(encoding="utf-8"))
analysis = json.loads((OUT / ".graphify_analysis.json").read_text(encoding="utf-8"))

G = build_from_json(extraction, root=str(ROOT), directed=False)
communities = {int(k): v for k, v in analysis["communities"].items()}
cohesion = {int(k): v for k, v in analysis["cohesion"].items()}
tokens = {"input": extraction.get("input_tokens", 0), "output": extraction.get("output_tokens", 0)}

questions = suggest_questions(G, communities, labels)
report = generate(
    G, communities, cohesion, labels, analysis["gods"], analysis["surprises"],
    detection, tokens, str(ROOT), suggested_questions=questions,
)
(OUT / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
(OUT / ".graphify_labels.json").write_text(
    json.dumps({str(k): v for k, v in labels.items()}, ensure_ascii=False), encoding="utf-8"
)
wrote = to_json(G, communities, str(OUT / "graph.json"), community_labels=labels)
if not wrote:
    print("ERROR: refused to shrink graphify-out/graph.json (existing graph has more nodes; #479).")
    print("If this shrink is intentional (you deleted files), re-run a full build with --force.")
    raise SystemExit(1)
print(f"Report updated with {len(labels)} community labels")
