# Load Seed

> 35 nodes · cohesion 0.09

## Key Concepts

- **safe_subprocess.py** (21 connections) — `scripts/utils/safe_subprocess.py`
- **safe_run()** (19 connections) — `scripts/utils/safe_subprocess.py`
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
- **_resolve_base_sha()** (3 connections) — `scripts/run_quality_fragmentation_guard.py`
- **Path** (3 connections)
- **install.py** (2 connections) — `scripts/install.py`
- **get_project_root()** (2 connections) — `scripts/install.py`
- **load_seed_data.py** (2 connections) — `scripts/load_seed_data.py`
- **Any** (2 connections)
- **CompletedProcess** (2 connections)
- **bandit.py** (1 connections) — `scripts/bandit.py`
- **build.py** (1 connections) — `scripts/build.py`
- **format.py** (1 connections) — `scripts/format.py`
- **Determine the project root based on current working directory** (1 connections) — `scripts/install.py`
- *... and 10 more nodes in this community*

## Relationships

- [CI Quality Scripts](CI_Quality_Scripts.md) (7 shared connections)
- [Quality Fragmentation Ci](Quality_Fragmentation_Ci.md) (4 shared connections)
- [Runner Path](Runner_Path.md) (2 shared connections)
- [Linting Results Comparator](Linting_Results_Comparator.md) (1 shared connections)
- [Dependency Risk Analyzer](Dependency_Risk_Analyzer.md) (1 shared connections)
- [Grype Command Handle Result](Grype_Command_Handle_Result.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `scripts/bandit.py`
- `scripts/build.py`
- `scripts/format.py`
- `scripts/install.py`
- `scripts/lint.py`
- `scripts/load_seed_data.py`
- `scripts/pylint.py`
- `scripts/run.py`
- `scripts/run_quality_fragmentation_guard.py`
- `scripts/sqlfluff.py`
- `scripts/utils/safe_subprocess.py`

## Audit Trail

- EXTRACTED: 126 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*