# scripts ci quality fragmentation ai

> 55 nodes

## Key Concepts

- **quality_fragmentation_ai_guardrails.py** (30 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **quality_fragmentation_guard.py** (24 connections) — `scripts/ci/quality_fragmentation_guard.py`
- **quality_fragmentation_core.py** (18 connections) — `scripts/ci/quality_fragmentation_core.py`
- **check_ai_guardrails()** (9 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **check_fragmentation_trends()** (9 connections) — `scripts/ci/quality_fragmentation_guard.py`
- **quality_fragmentation_trends.py** (9 connections) — `scripts/ci/quality_fragmentation_trends.py`
- **_collect_python_public_defs_and_tiny()** (8 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **scan_changed_files()** (8 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **main()** (8 connections) — `scripts/ci/quality_fragmentation_guard.py`
- **build_context()** (7 connections) — `scripts/ci/quality_fragmentation_core.py`
- **ChangedFile** (6 connections) — `scripts/ci/quality_fragmentation_core.py`
- **GuardContext** (6 connections) — `scripts/ci/quality_fragmentation_core.py`
- **_is_public_function_stmt()** (6 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **_process_added_file_checks()** (6 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **run_cmd()** (6 connections) — `scripts/ci/quality_fragmentation_core.py`
- **_is_test_file_path()** (5 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **collect_repo_texts()** (5 connections) — `scripts/ci/quality_fragmentation_core.py`
- **is_code_file()** (5 connections) — `scripts/ci/quality_fragmentation_core.py`
- **is_safe_git_ref()** (5 connections) — `scripts/ci/quality_fragmentation_core.py`
- **nloc_for_text()** (5 connections) — `scripts/ci/quality_fragmentation_core.py`
- **parse_args()** (5 connections) — `scripts/ci/quality_fragmentation_core.py`
- **_build_python_call_usage_map()** (4 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **_check_exports_and_tiny_functions()** (4 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **_check_single_use_file()** (4 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **_guardrail_scan_inputs()** (4 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- *... and 30 more nodes in this community*

## Relationships

- [guardcontext](guardcontext.md) (7 shared connections)
- [scripts ci quality fragmentation graph](scripts_ci_quality_fragmentation_graph.md) (3 shared connections)
- [scripts load seed data main](scripts_load_seed_data_main.md) (3 shared connections)
- [scripts bandit](scripts_bandit.md) (1 shared connections)

## Source Files

- `scripts/ci/quality_fragmentation_ai_guardrails.py`
- `scripts/ci/quality_fragmentation_core.py`
- `scripts/ci/quality_fragmentation_guard.py`
- `scripts/ci/quality_fragmentation_trends.py`
- `scripts/ci/quality_fragmentation_usage.py`

## Audit Trail

- EXTRACTED: 142 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*