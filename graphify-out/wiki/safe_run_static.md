# safe_run_static

> 33 nodes

## Key Concepts

- **safe_run_static()** (33 connections) — `scripts/utils/safe_subprocess.py`
- **safe_subprocess.py** (21 connections) — `scripts/utils/safe_subprocess.py`
- **pylint.py** (8 connections) — `scripts/pylint.py`
- **run_test_ci.py** (7 connections) — `scripts/run_test_ci.py`
- **is_pylint_startup_failure()** (5 connections) — `scripts/pylint.py`
- **main()** (5 connections) — `scripts/pylint.py`
- **sqlint.py** (5 connections) — `scripts/sqlint.py`
- **_CompletedProcessLike** (4 connections) — `scripts/pylint.py`
- **_require_pylint_runnable()** (4 connections) — `scripts/pylint.py`
- **_resolve_pylint_cmd()** (4 connections) — `scripts/pylint.py`
- **_resolve_sqlint_cmd()** (4 connections) — `scripts/sqlint.py`
- **_combined_output()** (3 connections) — `scripts/pylint.py`
- **_is_tool_crash()** (3 connections) — `scripts/sqlint.py`
- **install.py** (3 connections) — `scripts/install.py`
- **get_project_root()** (2 connections) — `scripts/install.py`
- **read_output()** (2 connections) — `scripts/run_test_ci.py`
- **bandit.py** (2 connections) — `scripts/bandit.py`
- **build.py** (2 connections) — `scripts/build.py`
- **format.py** (2 connections) — `scripts/format.py`
- **lint.py** (2 connections) — `scripts/lint.py`
- **run.py** (2 connections) — `scripts/run.py`
- **sqlfluff.py** (2 connections) — `scripts/sqlfluff.py`
- **_skip_sqlint()** (1 connections) — `scripts/sqlint.py`
- **Protocol** (1 connections)
- **Determine the project root based on current working directory** (1 connections) — `scripts/install.py`
- *... and 8 more nodes in this community*

## Relationships

- [safe_run](safe_run.md) (8 shared connections)
- [worktree-ops.py](worktree-ops.py.md) (6 shared connections)
- [manual_dependency_analysis.py](manual_dependency_analysis.py.md) (4 shared connections)
- [compare_linting_results.py](compare_linting_results.py.md) (3 shared connections)
- [grype.py](grype.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (1 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (1 shared connections)
- [quality_fragmentation_lizard.py](quality_fragmentation_lizard.py.md) (1 shared connections)
- [TestRunner](TestRunner.md) (1 shared connections)

## Source Files

- `scripts/bandit.py`
- `scripts/build.py`
- `scripts/format.py`
- `scripts/install.py`
- `scripts/lint.py`
- `scripts/pylint.py`
- `scripts/run.py`
- `scripts/run_test_ci.py`
- `scripts/sqlfluff.py`
- `scripts/sqlint.py`
- `scripts/utils/safe_subprocess.py`

## Audit Trail

- EXTRACTED: 83 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*