# CI Quality Scripts

> 56 nodes · cohesion 0.06

## Key Concepts

- **safe_run()** (20 connections) — `scripts/utils/safe_subprocess.py`
- **safe_subprocess.py** (19 connections) — `scripts/utils/safe_subprocess.py`
- **safe_run_static()** (16 connections) — `scripts/utils/safe_subprocess.py`
- **run_quality_fragmentation_guard.py** (9 connections) — `scripts/run_quality_fragmentation_guard.py`
- **worktree-ops.py** (9 connections) — `scripts/worktree-ops.py`
- **get_project_root()** (8 connections) — `scripts/worktree-ops.py`
- **get_current_worktree()** (7 connections) — `scripts/worktree-ops.py`
- **main()** (6 connections) — `scripts/run_quality_fragmentation_guard.py`
- **install_dependencies()** (6 connections) — `scripts/worktree-ops.py`
- **main()** (6 connections) — `scripts/worktree-ops.py`
- **run_format()** (6 connections) — `scripts/worktree-ops.py`
- **run_lint()** (6 connections) — `scripts/worktree-ops.py`
- **run_tests()** (6 connections) — `scripts/worktree-ops.py`
- **show_status()** (6 connections) — `scripts/worktree-ops.py`
- **_run_git()** (5 connections) — `scripts/run_quality_fragmentation_guard.py`
- **validate_path()** (5 connections) — `scripts/utils/safe_subprocess.py`
- **_changed_files_between()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_git_executable()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_local_changed_files()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_resolved_changed_files()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **sqlint.py** (4 connections) — `scripts/sqlint.py`
- **_resolve_sqlint_cmd()** (4 connections) — `scripts/sqlint.py`
- **run_command()** (4 connections) — `scripts/worktree-ops.py`
- **validate_command()** (4 connections) — `scripts/utils/safe_subprocess.py`
- **_resolve_base_sha()** (3 connections) — `scripts/run_quality_fragmentation_guard.py`
- *... and 31 more nodes in this community*

## Relationships

- [[Dependency Risk Analyzer]] (3 shared connections)
- [[AI Quality Guardrails]] (3 shared connections)
- [[Linting Results Comparator]] (2 shared connections)
- [[Grype Command Handle Result]] (2 shared connections)
- [[Runner Path]] (2 shared connections)
- [[Logging Migration Examples]] (1 shared connections)
- [[Quality Fragmentation Ci]] (1 shared connections)
- [[Load Seed]] (1 shared connections)

## Source Files

- `scripts/bandit.py`
- `scripts/build.py`
- `scripts/format.py`
- `scripts/install.py`
- `scripts/lint.py`
- `scripts/pylint.py`
- `scripts/run.py`
- `scripts/run_quality_fragmentation_guard.py`
- `scripts/sqlfluff.py`
- `scripts/sqlint.py`
- `scripts/utils/safe_subprocess.py`
- `scripts/worktree-ops.py`

## Audit Trail

- EXTRACTED: 202 (94%)
- INFERRED: 13 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
