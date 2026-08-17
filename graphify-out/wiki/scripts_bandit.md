# scripts bandit

> 69 nodes

## Key Concepts

- **safe_run_static()** (29 connections) — `scripts/utils/safe_subprocess.py`
- **compare_linting_results.py** (21 connections) — `scripts/compare_linting_results.py`
- **safe_subprocess.py** (21 connections) — `scripts/utils/safe_subprocess.py`
- **Finding** (18 connections) — `scripts/compare_linting_results.py`
- **main()** (10 connections) — `scripts/compare_linting_results.py`
- **compare_findings()** (8 connections) — `scripts/compare_linting_results.py`
- **generate_report()** (8 connections) — `scripts/compare_linting_results.py`
- **run_test_ci.py** (7 connections) — `scripts/run_test_ci.py`
- **categorize_findings()** (6 connections) — `scripts/compare_linting_results.py`
- **_format_findings_section()** (6 connections) — `scripts/compare_linting_results.py`
- **parse_ruff_json_output()** (5 connections) — `scripts/compare_linting_results.py`
- **sqlint.py** (5 connections) — `scripts/sqlint.py`
- **_build_file_line_index()** (4 connections) — `scripts/compare_linting_results.py`
- **_categorize_pylint_finding()** (4 connections) — `scripts/compare_linting_results.py`
- **_categorize_ruff_finding()** (4 connections) — `scripts/compare_linting_results.py`
- **_find_overlapping_findings()** (4 connections) — `scripts/compare_linting_results.py`
- **_find_unmatched_findings()** (4 connections) — `scripts/compare_linting_results.py`
- **_format_category_section()** (4 connections) — `scripts/compare_linting_results.py`
- **_format_overlapping_section()** (4 connections) — `scripts/compare_linting_results.py`
- **_format_summary_statistics()** (4 connections) — `scripts/compare_linting_results.py`
- **get_ruff_output()** (4 connections) — `scripts/compare_linting_results.py`
- **load_pylint_output()** (4 connections) — `scripts/compare_linting_results.py`
- **parse_pylint_text_output()** (4 connections) — `scripts/compare_linting_results.py`
- **parse_ruff_text_output()** (4 connections) — `scripts/compare_linting_results.py`
- **_resolve_sqlint_cmd()** (4 connections) — `scripts/sqlint.py`
- *... and 44 more nodes in this community*

## Relationships

- [scripts load seed data main](scripts_load_seed_data_main.md) (8 shared connections)
- [scripts worktree ops](scripts_worktree_ops.md) (6 shared connections)
- [scripts dependency analyzer](scripts_dependency_analyzer.md) (4 shared connections)
- [scripts grype](scripts_grype.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [formatter](formatter.md) (1 shared connections)
- [docs examples logging correct patterns](docs_examples_logging_correct_patterns.md) (1 shared connections)
- [scripts ci quality fragmentation ai](scripts_ci_quality_fragmentation_ai.md) (1 shared connections)
- [scripts pylint](scripts_pylint.md) (1 shared connections)
- [scripts test runner](scripts_test_runner.md) (1 shared connections)

## Source Files

- `scripts/bandit.py`
- `scripts/build.py`
- `scripts/compare_linting_results.py`
- `scripts/format.py`
- `scripts/install.py`
- `scripts/lint.py`
- `scripts/run.py`
- `scripts/run_test_ci.py`
- `scripts/sqlfluff.py`
- `scripts/sqlint.py`
- `scripts/utils/safe_subprocess.py`

## Audit Trail

- EXTRACTED: 144 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*