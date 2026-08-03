# quality fragmentation scripts

> 53 nodes

## Key Concepts

- **quality_fragmentation_ai_guardrails.py** (30 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **quality_fragmentation_guard.py** (24 connections) — `scripts/ci/quality_fragmentation_guard.py`
- **quality_fragmentation_core.py** (18 connections) — `scripts/ci/quality_fragmentation_core.py`
- **GuardContext** (10 connections) — `scripts/ci/quality_fragmentation_core.py`
- **check_ai_guardrails()** (9 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **run_cmd()** (9 connections) — `scripts/ci/quality_fragmentation_core.py`
- **check_fragmentation_trends()** (9 connections) — `scripts/ci/quality_fragmentation_guard.py`
- **quality_fragmentation_trends.py** (9 connections) — `scripts/ci/quality_fragmentation_trends.py`
- **_collect_python_public_defs_and_tiny()** (8 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **main()** (8 connections) — `scripts/ci/quality_fragmentation_guard.py`
- **ChangedFile** (7 connections) — `scripts/ci/quality_fragmentation_core.py`
- **is_safe_git_ref()** (7 connections) — `scripts/ci/quality_fragmentation_core.py`
- **build_context()** (7 connections) — `scripts/ci/quality_fragmentation_core.py`
- **nloc_for_text()** (7 connections) — `scripts/ci/quality_fragmentation_core.py`
- **_process_added_file_checks()** (6 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **_is_public_function_stmt()** (6 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **collect_repo_texts()** (6 connections) — `scripts/ci/quality_fragmentation_core.py`
- **_is_test_file_path()** (5 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **is_code_file()** (5 connections) — `scripts/ci/quality_fragmentation_core.py`
- **parse_args()** (5 connections) — `scripts/ci/quality_fragmentation_core.py`
- **file_nloc_failures()** (5 connections) — `scripts/ci/quality_fragmentation_lizard.py`
- **_guardrail_scan_inputs()** (4 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **_check_single_use_file()** (4 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **_is_single_use_small_file()** (4 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **_check_exports_and_tiny_functions()** (4 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- *... and 28 more nodes in this community*

## Relationships

- [fragmentation quality scripts](fragmentation_quality_scripts.md) (20 shared connections)
- [fragmentation quality guard](fragmentation_quality_guard.md) (12 shared connections)
- [quality fragmentation graph](quality_fragmentation_graph.md) (3 shared connections)
- [scripts run guard](scripts_run_guard.md) (3 shared connections)

## Source Files

- `scripts/ci/quality_fragmentation_ai_guardrails.py`
- `scripts/ci/quality_fragmentation_core.py`
- `scripts/ci/quality_fragmentation_guard.py`
- `scripts/ci/quality_fragmentation_lizard.py`
- `scripts/ci/quality_fragmentation_trends.py`
- `scripts/ci/quality_fragmentation_usage.py`

## Audit Trail

- EXTRACTED: 279 (96%)
- INFERRED: 13 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*