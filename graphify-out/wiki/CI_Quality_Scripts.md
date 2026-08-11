# CI Quality Scripts

> 38 nodes

## Key Concepts

- **safe_subprocess.py** (21 connections) — `scripts/utils/safe_subprocess.py`
- **safe_run()** (19 connections) — `scripts/utils/safe_subprocess.py`
- **run_quality_fragmentation_guard.py** (12 connections) — `scripts/run_quality_fragmentation_guard.py`
- **main()** (6 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_run_git()** (5 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_resolved_changed_files()** (5 connections) — `scripts/run_quality_fragmentation_guard.py`
- **validate_path()** (5 connections) — `scripts/utils/safe_subprocess.py`
- **run_psql_command()** (4 connections) — `scripts/load_seed_data.py`
- **_git_executable()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_changed_files_between()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_local_changed_files()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_build_guard_command()** (4 connections) — `scripts/run_quality_fragmentation_guard.py`
- **validate_command()** (4 connections) — `scripts/utils/safe_subprocess.py`
- **main()** (3 connections) — `scripts/load_seed_data.py`
- **_resolve_base_sha()** (3 connections) — `scripts/run_quality_fragmentation_guard.py`
- **_is_graphify_path()** (3 connections) — `scripts/run_quality_fragmentation_guard.py`
- **Path** (3 connections)
- **install.py** (2 connections) — `scripts/install.py`
- **get_project_root()** (2 connections) — `scripts/install.py`
- **load_seed_data.py** (2 connections) — `scripts/load_seed_data.py`
- **_argv_char_len()** (2 connections) — `scripts/run_quality_fragmentation_guard.py`
- **Any** (2 connections)
- **CompletedProcess** (2 connections)
- **bandit.py** (1 connections) — `scripts/bandit.py`
- **build.py** (1 connections) — `scripts/build.py`
- *... and 13 more nodes in this community*

## Relationships

- [Combat Command Helpers](Combat_Command_Helpers.md) (7 shared connections)
- [AI Quality Guardrails](AI_Quality_Guardrails.md) (3 shared connections)
- [Runner Path](Runner_Path.md) (2 shared connections)
- [Linting Results Comparator](Linting_Results_Comparator.md) (1 shared connections)
- [Dependency Risk Analyzer](Dependency_Risk_Analyzer.md) (1 shared connections)
- [Grype Command Handle Result](Grype_Command_Handle_Result.md) (1 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)
- [Architecture Container System](Architecture_Container_System.md) (1 shared connections)
- [Quality Fragmentation Ci](Quality_Fragmentation_Ci.md) (1 shared connections)

## Source Files

- `scripts/bandit.py`
- `scripts/build.py`
- `scripts/format.py`
- `scripts/install.py`
- `scripts/lint.py`
- `scripts/load_seed_data.py`
- `scripts/run.py`
- `scripts/run_quality_fragmentation_guard.py`
- `scripts/sqlfluff.py`
- `scripts/utils/safe_subprocess.py`

## Audit Trail

- EXTRACTED: 132 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*