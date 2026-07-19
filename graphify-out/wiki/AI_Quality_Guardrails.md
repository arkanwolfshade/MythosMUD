# AI Quality Guardrails

> 66 nodes · cohesion 0.08

## Key Concepts

- **quality_fragmentation_guard.py** (26 connections) — `scripts/ci/quality_fragmentation_guard.py`
- **quality_fragmentation_ai_guardrails.py** (25 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **ChangedFile** (19 connections) — `scripts/ci/quality_fragmentation_core.py`
- **GuardContext** (18 connections) — `scripts/ci/quality_fragmentation_core.py`
- **quality_fragmentation_core.py** (13 connections) — `scripts/ci/quality_fragmentation_core.py`
- **run_cmd()** (10 connections) — `scripts/ci/quality_fragmentation_core.py`
- **check_ai_guardrails()** (9 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **_collect_python_public_defs_and_tiny()** (8 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **compute_python_cross_file_depth()** (8 connections) — `scripts/ci/quality_fragmentation_graph.py`
- **check_fragmentation_trends()** (8 connections) — `scripts/ci/quality_fragmentation_guard.py`
- **main()** (8 connections) — `scripts/ci/quality_fragmentation_guard.py`
- **build_context()** (7 connections) — `scripts/ci/quality_fragmentation_core.py`
- **is_safe_git_ref()** (7 connections) — `scripts/ci/quality_fragmentation_core.py`
- **nloc_for_text()** (7 connections) — `scripts/ci/quality_fragmentation_core.py`
- **quality_fragmentation_trends.py** (7 connections) — `scripts/ci/quality_fragmentation_trends.py`
- **_is_public_function_stmt()** (6 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **_process_added_file_checks()** (6 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **collect_repo_texts()** (6 connections) — `scripts/ci/quality_fragmentation_core.py`
- **quality_fragmentation_graph.py** (6 connections) — `scripts/ci/quality_fragmentation_graph.py`
- **_is_test_file_path()** (5 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **collect_python_defs_and_calls()** (5 connections) — `scripts/ci/quality_fragmentation_graph.py`
- **file_nloc_failures()** (5 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **append_rule_b_failure()** (5 connections) — `scripts/ci/quality_fragmentation_trends.py`
- **imported_by_count()** (5 connections) — `scripts/ci/quality_fragmentation_usage.py`
- **is_single_use_small_file()** (5 connections) — `scripts/ci/quality_fragmentation_usage.py`
- *... and 41 more nodes in this community*

## Relationships

- [[Quality Fragmentation Ci]] (20 shared connections)
- [[Quality Fragmentation Guard]] (12 shared connections)
- [[CI Quality Scripts]] (3 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `scripts/ci/quality_fragmentation_ai_guardrails.py`
- `scripts/ci/quality_fragmentation_core.py`
- `scripts/ci/quality_fragmentation_graph.py`
- `scripts/ci/quality_fragmentation_guard.py`
- `scripts/ci/quality_fragmentation_lizard.py`
- `scripts/ci/quality_fragmentation_trends.py`
- `scripts/ci/quality_fragmentation_usage.py`

## Audit Trail

- EXTRACTED: 305 (84%)
- INFERRED: 57 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
