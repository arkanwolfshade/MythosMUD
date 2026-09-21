# safe_run_static

> 49 nodes

## Key Concepts

- **safe_run_static()** (35 connections) — `scripts/utils/safe_subprocess.py`
- **safe_run()** (22 connections) — `scripts/utils/safe_subprocess.py`
- **safe_subprocess.py** (22 connections) — `scripts/utils/safe_subprocess.py`
- **run_quality_fragmentation_guard.py** (12 connections) — `scripts/run_quality_fragmentation_guard.py`
- **run_test_ci.py** (7 connections) — `scripts/run_test_ci.py`
- **main()** (6 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_resolved_changed_files()** (5 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_run_git()** (5 connections) — `scripts/run_quality_fragmentation_guard.py`
- **validate_path()** (5 connections) — `scripts/utils/safe_subprocess.py`
- **sqlint.py** (5 connections) — `scripts/sqlint.py`
- **run_psql_command()** (4 connections) — `scripts/load_seed_data.py`
- **_build_guard_command()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_changed_files_between()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_git_executable()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_local_changed_files()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_resolve_sqlint_cmd()** (4 connections) — `scripts/sqlint.py`
- **validate_command()** (4 connections) — `scripts/utils/safe_subprocess.py`
- **main()** (3 connections) — `scripts/load_seed_data.py`
- **_is_graphify_path()** (3 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_resolve_base_sha()** (3 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_is_tool_crash()** (3 connections) — `scripts/sqlint.py`
- **install.py** (3 connections) — `scripts/install.py`
- **load_seed_data.py** (3 connections) — `scripts/load_seed_data.py`
- **Path** (3 connections)
- **get_project_root()** (2 connections) — `scripts/install.py`
- *... and 24 more nodes in this community*

## Relationships

- [worktree-ops.py](worktree-ops.py.md) (8 shared connections)
- [pylint.py](pylint.py.md) (5 shared connections)
- [quality_fragmentation_lizard.py](quality_fragmentation_lizard.py.md) (4 shared connections)
- [manual_dependency_analysis.py](manual_dependency_analysis.py.md) (4 shared connections)
- [TestRunner](TestRunner.md) (3 shared connections)
- [compare_linting_results.py](compare_linting_results.py.md) (3 shared connections)
- [grype.py](grype.py.md) (3 shared connections)
- [lint_imports.py](lint_imports.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (1 shared connections)
- [Result](Result.md) (1 shared connections)

## Source Files

- `scripts/bandit.py`
- `scripts/build.py`
- `scripts/format.py`
- `scripts/install.py`
- `scripts/lint.py`
- `scripts/load_seed_data.py`
- `scripts/run.py`
- `scripts/run_quality_fragmentation_guard.py`
- `scripts/run_test_ci.py`
- `scripts/sqlfluff.py`
- `scripts/sqlint.py`
- `scripts/utils/safe_subprocess.py`

## Audit Trail

- EXTRACTED: 123 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*