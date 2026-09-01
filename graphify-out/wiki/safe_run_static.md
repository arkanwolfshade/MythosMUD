# safe_run_static

> 52 nodes

## Key Concepts

- **safe_run_static()** (33 connections) — `scripts/utils/safe_subprocess.py`
- **safe_subprocess.py** (21 connections) — `scripts/utils/safe_subprocess.py`
- **worktree-ops.py** (11 connections) — `scripts/worktree-ops.py`
- **grype.py** (9 connections) — `scripts/grype.py`
- **get_project_root()** (8 connections) — `scripts/worktree-ops.py`
- **get_current_worktree()** (7 connections) — `scripts/worktree-ops.py`
- **run_test_ci.py** (7 connections) — `scripts/run_test_ci.py`
- **install_dependencies()** (6 connections) — `scripts/worktree-ops.py`
- **main()** (6 connections) — `scripts/worktree-ops.py`
- **run_format()** (6 connections) — `scripts/worktree-ops.py`
- **run_lint()** (6 connections) — `scripts/worktree-ops.py`
- **run_tests()** (6 connections) — `scripts/worktree-ops.py`
- **show_status()** (6 connections) — `scripts/worktree-ops.py`
- **_run_grype_scan()** (5 connections) — `scripts/grype.py`
- **sqlint.py** (5 connections) — `scripts/sqlint.py`
- **main()** (4 connections) — `scripts/grype.py`
- **_resolve_sqlint_cmd()** (4 connections) — `scripts/sqlint.py`
- **run_command()** (4 connections) — `scripts/worktree-ops.py`
- **_handle_grype_result()** (3 connections) — `scripts/grype.py`
- **merge_windows_machine_user_path_into_environ()** (3 connections) — `scripts/grype.py`
- **repo_root()** (3 connections) — `scripts/grype.py`
- **_resolve_grype_executable()** (3 connections) — `scripts/grype.py`
- **_is_tool_crash()** (3 connections) — `scripts/sqlint.py`
- **install.py** (3 connections) — `scripts/install.py`
- **_grype_command()** (2 connections) — `scripts/grype.py`
- *... and 27 more nodes in this community*

## Relationships

- [safe_run](safe_run.md) (10 shared connections)
- [pylint.py](pylint.py.md) (5 shared connections)
- [manual_dependency_analysis.py](manual_dependency_analysis.py.md) (4 shared connections)
- [compare_linting_results.py](compare_linting_results.py.md) (3 shared connections)
- [time.py](time.py.md) (1 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (1 shared connections)
- [quality_fragmentation_ai_guardrails.py](quality_fragmentation_ai_guardrails.py.md) (1 shared connections)
- [TestRunner](TestRunner.md) (1 shared connections)

## Source Files

- `scripts/bandit.py`
- `scripts/build.py`
- `scripts/format.py`
- `scripts/grype.py`
- `scripts/install.py`
- `scripts/lint.py`
- `scripts/run.py`
- `scripts/run_test_ci.py`
- `scripts/sqlfluff.py`
- `scripts/sqlint.py`
- `scripts/utils/safe_subprocess.py`
- `scripts/worktree-ops.py`

## Audit Trail

- EXTRACTED: 119 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*