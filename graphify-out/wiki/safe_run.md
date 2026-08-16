# safe_run

> 27 nodes

## Key Concepts

- **safe_run()** (22 connections) — `scripts/utils/safe_subprocess.py`
- **run_quality_fragmentation_guard.py** (12 connections) — `scripts/run_quality_fragmentation_guard.py`
- **main()** (6 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_resolved_changed_files()** (5 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_run_git()** (5 connections) — `scripts/run_quality_fragmentation_guard.py`
- **validate_path()** (5 connections) — `scripts/utils/safe_subprocess.py`
- **run_psql_command()** (4 connections) — `scripts/load_seed_data.py`
- **_build_guard_command()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_changed_files_between()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_git_executable()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_local_changed_files()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **validate_command()** (4 connections) — `scripts/utils/safe_subprocess.py`
- **main()** (3 connections) — `scripts/load_seed_data.py`
- **_is_graphify_path()** (3 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_resolve_base_sha()** (3 connections) — `scripts/run_quality_fragmentation_guard.py`
- **load_seed_data.py** (3 connections) — `scripts/load_seed_data.py`
- **Path** (3 connections)
- **_argv_char_len()** (2 connections) — `scripts/run_quality_fragmentation_guard.py`
- **Any** (2 connections)
- **CompletedProcess** (2 connections)
- **Path** (1 connections)
- **Run a psql command and return the result.** (1 connections) — `scripts/load_seed_data.py`
- **Load all seed data files.** (1 connections) — `scripts/load_seed_data.py`
- **Generated graphify trees are not product code; skip guard/lint argv bloat.** (1 connections) — `scripts/run_quality_fragmentation_guard.py`
- **Safely execute a subprocess command with validation. This function prevents…** (1 connections) — `scripts/utils/safe_subprocess.py`
- *... and 2 more nodes in this community*

## Relationships

- [safe_run_static](safe_run_static.md) (8 shared connections)
- [quality_fragmentation_lizard.py](quality_fragmentation_lizard.py.md) (3 shared connections)
- [TestRunner](TestRunner.md) (2 shared connections)
- [worktree-ops.py](worktree-ops.py.md) (2 shared connections)

## Source Files

- `scripts/load_seed_data.py`
- `scripts/run_quality_fragmentation_guard.py`
- `scripts/utils/safe_subprocess.py`

## Audit Trail

- EXTRACTED: 61 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*