# scripts bandit

> 35 nodes

## Key Concepts

- **safe_run_static()** (33 connections) — `scripts/utils/safe_subprocess.py`
- **safe_subprocess.py** (21 connections) — `scripts/utils/safe_subprocess.py`
- **pylint.py** (10 connections) — `scripts/pylint.py`
- **_CompletedProcessLike** (8 connections) — `scripts/pylint.py`
- **main()** (8 connections) — `scripts/pylint.py`
- **is_pylint_startup_failure()** (5 connections) — `scripts/pylint.py`
- **sqlint.py** (5 connections) — `scripts/sqlint.py`
- **_report_pylint_failure()** (4 connections) — `scripts/pylint.py`
- **_require_pylint_runnable()** (4 connections) — `scripts/pylint.py`
- **_resolve_pylint_cmd()** (4 connections) — `scripts/pylint.py`
- **_write_pylint_output()** (4 connections) — `scripts/pylint.py`
- **_resolve_sqlint_cmd()** (4 connections) — `scripts/sqlint.py`
- **_combined_output()** (3 connections) — `scripts/pylint.py`
- **_is_tool_crash()** (3 connections) — `scripts/sqlint.py`
- **install.py** (3 connections) — `scripts/install.py`
- **Path** (3 connections)
- **get_project_root()** (2 connections) — `scripts/install.py`
- **bandit.py** (2 connections) — `scripts/bandit.py`
- **build.py** (2 connections) — `scripts/build.py`
- **format.py** (2 connections) — `scripts/format.py`
- **lint.py** (2 connections) — `scripts/lint.py`
- **run.py** (2 connections) — `scripts/run.py`
- **sqlfluff.py** (2 connections) — `scripts/sqlfluff.py`
- **.stderr()** (1 connections) — `scripts/pylint.py`
- **.stdout()** (1 connections) — `scripts/pylint.py`
- *... and 10 more nodes in this community*

## Relationships

- [scripts load seed data main](scripts_load_seed_data_main.md) (8 shared connections)
- [scripts worktree ops](scripts_worktree_ops.md) (6 shared connections)
- [scripts dependency analyzer](scripts_dependency_analyzer.md) (4 shared connections)
- [scripts compare linting results](scripts_compare_linting_results.md) (3 shared connections)
- [scripts grype](scripts_grype.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [scripts ci quality fragmentation ai](scripts_ci_quality_fragmentation_ai.md) (1 shared connections)
- [scripts test runner](scripts_test_runner.md) (1 shared connections)

## Source Files

- `scripts/bandit.py`
- `scripts/build.py`
- `scripts/format.py`
- `scripts/install.py`
- `scripts/lint.py`
- `scripts/pylint.py`
- `scripts/run.py`
- `scripts/sqlfluff.py`
- `scripts/sqlint.py`
- `scripts/utils/safe_subprocess.py`

## Audit Trail

- EXTRACTED: 88 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*