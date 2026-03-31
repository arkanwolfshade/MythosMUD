#!/usr/bin/env python3
"""Cross-file call-depth helpers for quality fragmentation guard."""

from __future__ import annotations

import ast
from pathlib import Path


def compute_python_cross_file_depth(repo_root: Path, changed_python_files: list[str]) -> int:
    definitions, calls = collect_python_defs_and_calls(repo_root, changed_python_files)
    graph = build_call_graph(definitions, calls)
    return max_path_length(graph)


def collect_python_defs_and_calls(
    repo_root: Path, changed_python_files: list[str]
) -> tuple[dict[str, str], dict[str, set[str]]]:
    definitions: dict[str, str] = {}
    calls_by_file: dict[str, set[str]] = {}
    for rel_path in changed_python_files:
        abs_path = repo_root / rel_path
        if not abs_path.exists():
            continue
        try:
            tree = ast.parse(abs_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, ValueError, SyntaxError):
            continue
        definitions.update(dict.fromkeys(_top_level_definitions(tree), rel_path))
        calls_by_file[rel_path] = _named_calls(tree)
    return definitions, calls_by_file


def _top_level_definitions(tree: ast.Module) -> list[str]:
    names: list[str] = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
            names.append(node.name)
    return names


def _named_calls(tree: ast.Module) -> set[str]:
    calls: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            calls.add(node.func.id)
    return calls


def build_call_graph(definitions: dict[str, str], calls_by_file: dict[str, set[str]]) -> dict[str, set[str]]:
    graph: dict[str, set[str]] = {path: set() for path in calls_by_file}
    for source, calls in calls_by_file.items():
        for call_name in calls:
            target = definitions.get(call_name)
            if target and target != source:
                graph[source].add(target)
    return graph


def max_path_length(graph: dict[str, set[str]]) -> int:
    def dfs(node: str, visiting: set[str]) -> int:
        if node in visiting:
            return 0
        visiting.add(node)
        child_lengths = [dfs(child, visiting) for child in graph.get(node, set())]
        visiting.remove(node)
        return 1 + (max(child_lengths) if child_lengths else 0)

    return max((dfs(start, set()) for start in graph), default=0)
