# Combat Command Helpers

> 31 nodes

## Key Concepts

- **safe_run_static()** (19 connections) — `scripts/utils/safe_subprocess.py`
- **worktree-ops.py** (9 connections) — `scripts/worktree-ops.py`
- **get_project_root()** (8 connections) — `scripts/worktree-ops.py`
- **pylint.py** (7 connections) — `scripts/pylint.py`
- **get_current_worktree()** (7 connections) — `scripts/worktree-ops.py`
- **install_dependencies()** (6 connections) — `scripts/worktree-ops.py`
- **run_tests()** (6 connections) — `scripts/worktree-ops.py`
- **run_lint()** (6 connections) — `scripts/worktree-ops.py`
- **run_format()** (6 connections) — `scripts/worktree-ops.py`
- **show_status()** (6 connections) — `scripts/worktree-ops.py`
- **main()** (6 connections) — `scripts/worktree-ops.py`
- **is_pylint_startup_failure()** (5 connections) — `scripts/pylint.py`
- **main()** (5 connections) — `scripts/pylint.py`
- **_CompletedProcessLike** (4 connections) — `scripts/pylint.py`
- **_resolve_pylint_cmd()** (4 connections) — `scripts/pylint.py`
- **_require_pylint_runnable()** (4 connections) — `scripts/pylint.py`
- **run_command()** (4 connections) — `scripts/worktree-ops.py`
- **_combined_output()** (3 connections) — `scripts/pylint.py`
- **Protocol** (1 connections)
- **Prefer current interpreter -m pylint (works under uv run --no-sync).** (1 connections) — `scripts/pylint.py`
- **Fail fast before scanning if pylint cannot start (missing package, broken venv).** (1 connections) — `scripts/pylint.py`
- **True when pylint never ran as a linter (missing module, usage/invocation error).** (1 connections) — `scripts/pylint.py`
- **Execute a command with static arguments (safest option).      This is the safest** (1 connections) — `scripts/utils/safe_subprocess.py`
- **Determine the project root based on current working directory** (1 connections) — `scripts/worktree-ops.py`
- **Get the current worktree name** (1 connections) — `scripts/worktree-ops.py`
- *... and 6 more nodes in this community*

## Relationships

- [CI Quality Scripts](CI_Quality_Scripts.md) (7 shared connections)
- [Dependency Risk Analyzer](Dependency_Risk_Analyzer.md) (2 shared connections)
- [Linting Results Comparator](Linting_Results_Comparator.md) (1 shared connections)
- [Grype Command Handle Result](Grype_Command_Handle_Result.md) (1 shared connections)
- [Architecture Container System](Architecture_Container_System.md) (1 shared connections)

## Source Files

- `scripts/pylint.py`
- `scripts/utils/safe_subprocess.py`
- `scripts/worktree-ops.py`

## Audit Trail

- EXTRACTED: 106 (83%)
- INFERRED: 22 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*