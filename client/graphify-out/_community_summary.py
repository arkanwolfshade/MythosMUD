import json
from collections import Counter
from pathlib import Path

from graphify.build import build_from_json

extraction = json.loads(Path("graphify-out/.graphify_extract.json").read_text(encoding="utf-8"))
analysis = json.loads(Path("graphify-out/.graphify_analysis.json").read_text(encoding="utf-8"))
G = build_from_json(extraction, root=r"C:\projects\MythosMUD\client\src", directed=False)
communities = {int(k): v for k, v in analysis["communities"].items()}
id_to_label = {n: G.nodes[n].get("label") or n for n in G.nodes}

print(f"COMMUNITIES={len(communities)}")
for cid, members in sorted(communities.items(), key=lambda kv: -len(kv[1])):
    labels = [id_to_label.get(n, n) for n in members]
    stems = []
    for n in members:
        src = G.nodes[n].get("source_file") or ""
        parts = str(src).replace("\\", "/").split("/")
        if "src" in parts:
            i = parts.index("src")
            folder = "/".join(parts[i + 1 : i + 3]) if i + 1 < len(parts) else ""
        else:
            folder = "/".join(parts[-3:-1])
        if folder:
            stems.append(folder)
    top_folder = Counter(stems).most_common(1)[0][0] if stems else "?"
    sample = ", ".join(labels[:8])
    extra = f" +{len(labels) - 8}" if len(labels) > 8 else ""
    print(f"{cid}\t{len(members)}\t{top_folder}\t{sample}{extra}")
