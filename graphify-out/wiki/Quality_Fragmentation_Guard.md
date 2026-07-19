# Quality Fragmentation Guard

> 22 nodes · cohesion 0.24

## Key Concepts

- **test_quality_fragmentation_guard.py** (20 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **scan_changed_files()** (13 connections) — `scripts/ci/quality_fragmentation_ai_guardrails.py`
- **_load_guard_module()** (12 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **_set_repo_root()** (11 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **Path** (8 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **test_collect_repo_texts_reports_unreadable_files()** (5 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **test_scan_changed_files_does_not_flag_tiny_function_with_two_usages()** (5 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **test_scan_changed_files_flags_single_use_for_non_test_file()** (5 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **test_scan_changed_files_flags_tiny_single_use_function()** (5 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **test_scan_changed_files_skips_single_use_for_grouped_file()** (5 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **test_scan_changed_files_skips_single_use_for_test_file()** (5 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **test_scan_changed_files_skips_tiny_single_use_for_grouped_file()** (5 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **_load_trends_module()** (4 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **_QualityGuardModule** (4 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **_QualityTrendsModule** (3 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **test_append_fragmentation_failures_when_files_added_and_avg_function_length_drops()** (3 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **test_append_rule_b_failure_for_fragmentation_limit()** (3 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **test_is_safe_git_ref_accepts_sha_and_branch_like_ref()** (3 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **test_is_safe_git_ref_rejects_suspicious_values()** (3 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **test_parse_lizard_output_maps_function_nodes()** (3 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **_ChangedFile** (2 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **Point guard submodules at a temporary repo root for isolated scans.** (1 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`

## Relationships

- [[AI Quality Guardrails]] (12 shared connections)
- [[Quality Fragmentation Ci]] (3 shared connections)
- [[Player Combat XP]] (3 shared connections)

## Source Files

- `scripts/ci/quality_fragmentation_ai_guardrails.py`
- `server/tests/unit/test_quality_fragmentation_guard.py`

## Audit Trail

- EXTRACTED: 110 (86%)
- INFERRED: 18 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
