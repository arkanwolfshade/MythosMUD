# scripts run guard

> 55 nodes

## Key Concepts

- **safe_subprocess.py** (21 connections) — `scripts/utils/safe_subprocess.py`
- **safe_run()** (19 connections) — `scripts/utils/safe_subprocess.py`
- **safe_run_static()** (16 connections) — `scripts/utils/safe_subprocess.py`
- **worktree-ops.py** (9 connections) — `scripts/worktree-ops.py`
- **get_project_root()** (8 connections) — `scripts/worktree-ops.py`
- **get_current_worktree()** (7 connections) — `scripts/worktree-ops.py`
- **run_test_ci.py** (6 connections) — `scripts/run_test_ci.py`
- **install_dependencies()** (6 connections) — `scripts/worktree-ops.py`
- **run_tests()** (6 connections) — `scripts/worktree-ops.py`
- **run_lint()** (6 connections) — `scripts/worktree-ops.py`
- **run_format()** (6 connections) — `scripts/worktree-ops.py`
- **show_status()** (6 connections) — `scripts/worktree-ops.py`
- **main()** (6 connections) — `scripts/worktree-ops.py`
- **validate_path()** (5 connections) — `scripts/utils/safe_subprocess.py`
- **run_psql_command()** (4 connections) — `scripts/load_seed_data.py`
- **sqlint.py** (4 connections) — `scripts/sqlint.py`
- **_resolve_sqlint_cmd()** (4 connections) — `scripts/sqlint.py`
- **validate_command()** (4 connections) — `scripts/utils/safe_subprocess.py`
- **run_command()** (4 connections) — `scripts/worktree-ops.py`
- **main()** (3 connections) — `scripts/load_seed_data.py`
- **_is_tool_crash()** (3 connections) — `scripts/sqlint.py`
- **Path** (3 connections)
- **install.py** (2 connections) — `scripts/install.py`
- **get_project_root()** (2 connections) — `scripts/install.py`
- **load_seed_data.py** (2 connections) — `scripts/load_seed_data.py`
- *... and 30 more nodes in this community*

## Relationships

- [commands time handle](commands_time_handle.md) (6 shared connections)
- [quality fragmentation scripts](quality_fragmentation_scripts.md) (3 shared connections)
- [dependency scripts analyzer](dependency_scripts_analyzer.md) (3 shared connections)
- [compare linting results](compare_linting_results.md) (2 shared connections)
- [grype scripts rationale](grype_scripts_rationale.md) (2 shared connections)
- [runner scripts rationale](runner_scripts_rationale.md) (2 shared connections)
- [logging structured utilities](logging_structured_utilities.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (1 shared connections)
- [fragmentation quality scripts](fragmentation_quality_scripts.md) (1 shared connections)

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
- `scripts/utils/safe_subprocess.py`
- `scripts/worktree-ops.py`

## Audit Trail

- EXTRACTED: 174 (89%)
- INFERRED: 21 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*