"""One-off scan: blank line immediately before \\. in data/db DML (invalid COPY row)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
for name in ("mythos_unit_dml.sql", "mythos_e2e_dml.sql", "mythos_dev_dml.sql"):
    p = ROOT / "data" / "db" / name
    if not p.exists():
        continue
    lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
    bad: list[int] = []
    for i in range(1, len(lines)):
        if lines[i].strip() == r"\.":
            if lines[i - 1].strip() == "":
                bad.append(i + 1)
    print(name, bad, "count", len(bad))
