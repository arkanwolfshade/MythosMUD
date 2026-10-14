# safe_run_static

> 54 nodes

## Key Concepts

- **safe_run_static()** (35 connections) — `scripts/utils/safe_subprocess.py`
- **safe_run()** (22 connections) — `scripts/utils/safe_subprocess.py`
- **safe_subprocess.py** (22 connections) — `scripts/utils/safe_subprocess.py`
- **worktree-ops.py** (11 connections) — `scripts/worktree-ops.py`
- **get_project_root()** (8 connections) — `scripts/worktree-ops.py`
- **get_current_worktree()** (7 connections) — `scripts/worktree-ops.py`
- **run_test_ci.py** (7 connections) — `scripts/run_test_ci.py`
- **validate_path()** (6 connections) — `scripts/utils/safe_subprocess.py`
- **install_dependencies()** (6 connections) — `scripts/worktree-ops.py`
- **main()** (6 connections) — `scripts/worktree-ops.py`
- **run_format()** (6 connections) — `scripts/worktree-ops.py`
- **run_lint()** (6 connections) — `scripts/worktree-ops.py`
- **run_tests()** (6 connections) — `scripts/worktree-ops.py`
- **show_status()** (6 connections) — `scripts/worktree-ops.py`
- **validate_command()** (5 connections) — `scripts/utils/safe_subprocess.py`
- **sqlint.py** (5 connections) — `scripts/sqlint.py`
- **run_psql_command()** (4 connections) — `scripts/load_seed_data.py`
- **_resolve_sqlint_cmd()** (4 connections) — `scripts/sqlint.py`
- **run_command()** (4 connections) — `scripts/worktree-ops.py`
- **main()** (3 connections) — `scripts/load_seed_data.py`
- **_is_tool_crash()** (3 connections) — `scripts/sqlint.py`
- **install.py** (3 connections) — `scripts/install.py`
- **load_seed_data.py** (3 connections) — `scripts/load_seed_data.py`
- **Path** (3 connections)
- **get_project_root()** (2 connections) — `scripts/install.py`
- *... and 29 more nodes in this community*

## Relationships

- [run_quality_fragmentation_guard.py](run_quality_fragmentation_guard.py.md) (6 shared connections)
- [pylint.py](pylint.py.md) (5 shared connections)
- [quality_fragmentation_lizard.py](quality_fragmentation_lizard.py.md) (4 shared connections)
- [manual_dependency_analysis.py](manual_dependency_analysis.py.md) (4 shared connections)
- [TestRunner](TestRunner.md) (3 shared connections)
- [compare_linting_results.py](compare_linting_results.py.md) (3 shared connections)
- [grype.py](grype.py.md) (3 shared connections)
- [lint_imports.py](lint_imports.py.md) (3 shared connections)
- [ValueError](ValueError.md) (2 shared connections)
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
- `scripts/run_test_ci.py`
- `scripts/sqlfluff.py`
- `scripts/sqlint.py`
- `scripts/utils/safe_subprocess.py`
- `scripts/worktree-ops.py`

## Audit Trail

- EXTRACTED: 132 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*