"""Save incremental manifest after force-write (was restored from git)."""

# graphify is a CLI (not in the MythosMUD venv); payloads are untyped JSON dumps.
# graphify-out is excluded from CLI basedpyright, but Pylance still checks open files.
# pyright: reportMissingImports=false, reportAny=false, reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false, reportUnknownArgumentType=false
from __future__ import annotations

import json
from pathlib import Path

from graphify.cli import _stamped_manifest_files
from graphify.detect import save_manifest

incremental = json.loads(Path("graphify-out/.graphify_incremental.json").read_text(encoding="utf-8"))
# Stamp from THIS-run AST+semantic, not the merged 53k extract (#2015).
ast = json.loads(Path("graphify-out/.graphify_ast.json").read_text(encoding="utf-8"))
sem = json.loads(Path("graphify-out/.graphify_semantic.json").read_text(encoding="utf-8"))
new_extraction = {
    "nodes": list(ast.get("nodes", [])) + list(sem.get("nodes", [])),
    "edges": list(ast.get("edges", [])) + list(sem.get("edges", [])),
    "hyperedges": list(sem.get("hyperedges", [])),
}

_manifest_files = _stamped_manifest_files(
    incremental["files"],
    new_extraction,
    Path("."),
    failed_ast_sources=ast.get("failed_sources"),
)
_sem_types = ("document", "paper", "image")
_dispatched = {
    f for t, fl in incremental.get("new_files", {}).items() if t in _sem_types for f in fl
}
_stamped = {f for fl in _manifest_files.values() for f in fl}
_cleared = _dispatched - _stamped
_scan = {f for fl in incremental["files"].values() for f in fl}
save_manifest(_manifest_files, root=".", scan_corpus=_scan, clear_semantic=_cleared or None)
print(f"Manifest saved. Unstamped semantic files: {len(_cleared)}")
