# safe_run_static

> 67 nodes

## Key Concepts

- **safe_run_static()** (33 connections) — `scripts/utils/safe_subprocess.py`
- **safe_run()** (22 connections) — `scripts/utils/safe_subprocess.py`
- **safe_subprocess.py** (21 connections) — `scripts/utils/safe_subprocess.py`
- **worktree-ops.py** (11 connections) — `scripts/worktree-ops.py`
- **get_project_root()** (8 connections) — `scripts/worktree-ops.py`
- **pylint.py** (8 connections) — `scripts/pylint.py`
- **get_current_worktree()** (7 connections) — `scripts/worktree-ops.py`
- **run_test_ci.py** (7 connections) — `scripts/run_test_ci.py`
- **install_dependencies()** (6 connections) — `scripts/worktree-ops.py`
- **main()** (6 connections) — `scripts/worktree-ops.py`
- **run_format()** (6 connections) — `scripts/worktree-ops.py`
- **run_lint()** (6 connections) — `scripts/worktree-ops.py`
- **run_tests()** (6 connections) — `scripts/worktree-ops.py`
- **show_status()** (6 connections) — `scripts/worktree-ops.py`
- **test_runner.py** (6 connections) — `scripts/test_runner.py`
- **is_pylint_startup_failure()** (5 connections) — `scripts/pylint.py`
- **main()** (5 connections) — `scripts/pylint.py`
- **validate_path()** (5 connections) — `scripts/utils/safe_subprocess.py`
- **sqlint.py** (5 connections) — `scripts/sqlint.py`
- **_CompletedProcessLike** (4 connections) — `scripts/pylint.py`
- **run_psql_command()** (4 connections) — `scripts/load_seed_data.py`
- **_require_pylint_runnable()** (4 connections) — `scripts/pylint.py`
- **_resolve_pylint_cmd()** (4 connections) — `scripts/pylint.py`
- **_resolve_sqlint_cmd()** (4 connections) — `scripts/sqlint.py`
- **validate_command()** (4 connections) — `scripts/utils/safe_subprocess.py`
- *... and 42 more nodes in this community*

## Relationships

- [run_quality_fragmentation_guard.py](run_quality_fragmentation_guard.py.md) (6 shared connections)
- [quality_fragmentation_ai_guardrails.py](quality_fragmentation_ai_guardrails.py.md) (4 shared connections)
- [manual_dependency_analysis.py](manual_dependency_analysis.py.md) (4 shared connections)
- [TestRunner](TestRunner.md) (3 shared connections)
- [compare_linting_results.py](compare_linting_results.py.md) (3 shared connections)
- [grype.py](grype.py.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (1 shared connections)

## Source Files

- `scripts/bandit.py`
- `scripts/build.py`
- `scripts/format.py`
- `scripts/install.py`
- `scripts/lint.py`
- `scripts/load_seed_data.py`
- `scripts/pylint.py`
- `scripts/run.py`
- `scripts/run_test_ci.py`
- `scripts/sqlfluff.py`
- `scripts/sqlint.py`
- `scripts/test_runner.py`
- `scripts/utils/safe_subprocess.py`
- `scripts/worktree-ops.py`

## Audit Trail

- EXTRACTED: 149 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*