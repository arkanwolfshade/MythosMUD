# Combat Command Helpers

> 26 nodes

## Key Concepts

- **safe_run_static()** (17 connections) — `scripts/utils/safe_subprocess.py`
- **worktree-ops.py** (9 connections) — `scripts/worktree-ops.py`
- **get_project_root()** (8 connections) — `scripts/worktree-ops.py`
- **get_current_worktree()** (7 connections) — `scripts/worktree-ops.py`
- **install_dependencies()** (6 connections) — `scripts/worktree-ops.py`
- **run_tests()** (6 connections) — `scripts/worktree-ops.py`
- **run_lint()** (6 connections) — `scripts/worktree-ops.py`
- **run_format()** (6 connections) — `scripts/worktree-ops.py`
- **show_status()** (6 connections) — `scripts/worktree-ops.py`
- **main()** (6 connections) — `scripts/worktree-ops.py`
- **sqlint.py** (4 connections) — `scripts/sqlint.py`
- **_resolve_sqlint_cmd()** (4 connections) — `scripts/sqlint.py`
- **run_command()** (4 connections) — `scripts/worktree-ops.py`
- **_is_tool_crash()** (3 connections) — `scripts/sqlint.py`
- **_skip_sqlint()** (1 connections) — `scripts/sqlint.py`
- **Return True when sqlint failed to start rather than reporting SQL issues.** (1 connections) — `scripts/sqlint.py`
- **Return sqlint command argv when the tool is installed and runnable.** (1 connections) — `scripts/sqlint.py`
- **Execute a command with static arguments (safest option).      This is the safest** (1 connections) — `scripts/utils/safe_subprocess.py`
- **Determine the project root based on current working directory** (1 connections) — `scripts/worktree-ops.py`
- **Get the current worktree name** (1 connections) — `scripts/worktree-ops.py`
- **Run a command with proper error handling** (1 connections) — `scripts/worktree-ops.py`
- **Install dependencies (worktree-aware)** (1 connections) — `scripts/worktree-ops.py`
- **Run tests (worktree-aware)** (1 connections) — `scripts/worktree-ops.py`
- **Run linting (worktree-aware)** (1 connections) — `scripts/worktree-ops.py`
- **Run formatting (worktree-aware)** (1 connections) — `scripts/worktree-ops.py`
- *... and 1 more nodes in this community*

## Relationships

- [CI Quality Scripts](CI_Quality_Scripts.md) (8 shared connections)
- [Dependency Risk Analyzer](Dependency_Risk_Analyzer.md) (2 shared connections)
- [Linting Results Comparator](Linting_Results_Comparator.md) (1 shared connections)
- [Grype Command Handle Result](Grype_Command_Handle_Result.md) (1 shared connections)

## Source Files

- `scripts/sqlint.py`
- `scripts/utils/safe_subprocess.py`
- `scripts/worktree-ops.py`

## Audit Trail

- EXTRACTED: 86 (83%)
- INFERRED: 18 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*