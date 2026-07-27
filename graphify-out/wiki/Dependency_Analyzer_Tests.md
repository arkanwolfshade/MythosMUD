# Dependency Analyzer Tests

> 35 nodes · cohesion 0.09

## Key Concepts

- **test_dependency_analysis.py** (21 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **DependencyAnalyzerTestApi** (10 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **DependencyRiskTestApi** (6 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **analyzer_api_module_scope()** (4 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **_load_dependency_analyzer_script()** (4 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **risk_api_module_scope()** (4 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **test_analyze_npm_dependencies_parses_stdout_from_expected_outdated_exit_code()** (4 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **test_analyze_python_dependencies_parses_outdated_table_output()** (4 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **_load_dependency_risk_script()** (3 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **test_assess_npm_risk_uses_update_type_and_package_tiers()** (3 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **test_assess_python_risk_uses_update_type_and_package_tiers()** (3 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **test_assess_risks_maps_breaking_change_counts_to_overall_risk()** (3 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **test_categorize_update_handles_semver_and_invalid_input()** (3 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **test_dep_info_from_npm_row_coerces_types_and_applies_defaults()** (3 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **test_determine_strategy_covers_incremental_batched_and_immediate_paths()** (3 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **test_parse_npm_outdated_json_handles_non_object_and_valid_payload()** (3 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **test_prioritize_updates_scores_and_sorts_descending()** (3 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **_DependencyAnalyzerScriptInternals** (2 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **_DependencyRiskScriptInternals** (2 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **_scripts_path_on_syspath()** (2 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **MonkeyPatch** (2 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **_FakeCompletedProcess** (1 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **Regression tests for scripts/dependency_analyzer.py and scripts/utils/dependency** (1 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **Load scripts/dependency_analyzer.py and expose tested helpers.** (1 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- **categorize_update should classify major/minor/patch/none/unknown consistently.** (1 connections) — `server/tests/unit/scripts/test_dependency_analysis.py`
- *... and 10 more nodes in this community*

## Relationships

- [[Player Combat XP]] (2 shared connections)

## Source Files

- `server/tests/unit/scripts/test_dependency_analysis.py`

## Audit Trail

- EXTRACTED: 106 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
