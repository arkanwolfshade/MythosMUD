import json
from collections import Counter
from pathlib import Path

analysis = json.loads(Path("graphify-out/.graphify_analysis.json").read_text(encoding="utf-8"))
extract = json.loads(Path("graphify-out/.graphify_extract.json").read_text(encoding="utf-8"))
nodes = {n["id"]: n for n in extract["nodes"]}
communities = analysis["communities"]
cohesion = analysis.get("cohesion", {})

rows = []
for cid, member_ids in communities.items():
    labels = []
    files = []
    for nid in member_ids:
        n = nodes.get(nid, {})
        labels.append(n.get("label") or nid)
        sf = n.get("source_file") or ""
        files.append(sf)
    file_stems = []
    dirs = []
    for sf in files:
        p = sf.replace("\\", "/").split("/")
        if "server" in p:
            idx = p.index("server")
            rel = p[idx + 1 :]
        else:
            rel = p[-3:]
        if rel:
            dirs.append(rel[0] if rel[0] != "tests" else "/".join(rel[:2]))
            file_stems.append("/".join(rel[-2:]) if len(rel) >= 2 else rel[-1])
    top_dir = Counter(dirs).most_common(1)[0] if dirs else ("unknown", 0)
    top_files = Counter(file_stems).most_common(3)
    sample = labels[:8]
    rows.append({
        "cid": int(cid),
        "size": len(member_ids),
        "cohesion": cohesion.get(cid, cohesion.get(str(cid), "")),
        "top_dir": top_dir[0],
        "top_dir_n": top_dir[1],
        "top_files": [f"{n}:{c}" for n, c in top_files],
        "sample": sample,
    })

rows.sort(key=lambda r: r["size"], reverse=True)
Path("graphify-out/_community_summary.json").write_text(
    json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(f"communities={len(rows)}")
print("TOP 40 BY SIZE")
for r in rows[:40]:
    print(f"{r['cid']}\t{r['size']}\t{r['cohesion']}\t{r['top_dir']}\t{r['top_files'][:2]}\t{r['sample'][:4]}")
print("SIZE_HIST")
from collections import Counter as C
hist = C()
for r in rows:
    if r["size"] >= 100:
        hist["100+"] += 1
    elif r["size"] >= 20:
        hist["20-99"] += 1
    elif r["size"] >= 5:
        hist["5-19"] += 1
    else:
        hist["1-4"] += 1
print(dict(hist))
